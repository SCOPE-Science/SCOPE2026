"""Reproducible exact checks for ordering of diploid viability-selection epochs.

Requires Python 3 and SymPy >= 1.12. No simulation is used as proof of
any universally quantified statement; the algebraic identity and the
mathematical argument in RESULT.md supply that proof.
"""
from fractions import Fraction
from itertools import permutations
from sympy import symbols, cancel, factor, together, Poly, Rational, S

x, a, b, h = symbols('x a b h')

def N(x, s, h):
    return x * (1 + s * (h + (1 - h) * x))

def D(x, s, h):
    return 1 + s * (2 * h * x + (1 - 2 * h) * x*x)

def F(x, s, h):
    return N(x, s, h) / D(x, s, h)

count=0

def check(truth, message):
    global count
    assert truth, message
    count+=1

# Structural symbolic numerator identity: first strength a then strength b.
na, nb = N(x,a,h), N(x,b,h)
da, db = D(x,a,h), D(x,b,h)
za = factor(da*da + b*(2*h*na*da+(1-2*h)*na*na))
zb = factor(db*db + a*(2*h*nb*db+(1-2*h)*nb*nb))
fa_then_b = na*((1+b*h)*da+b*(1-h)*na)/za
fb_then_a = nb*((1+a*h)*db+a*(1-h)*nb)/zb
u=h+(1-2*h)*x
q=(1-h)*(1-x)+h*x*(1+a+b+a*b*(h*(1-x)+x))
expected = a*b*(a-b)*x*x*(1-x)**2*u*u*q
check(cancel((fa_then_b-fb_then_a)*za*zb - expected)==0,
      'two-epoch commutator factorization')
check(cancel(fa_then_b-F(F(x,a,h),b,h))==0,'first composition')
check(cancel(fb_then_a-F(F(x,b,h),a,h))==0,'second composition')
check(cancel(F(x,a,h)-x-a*x*(1-x)*u/D(x,a,h))==0,
      'one-generation directional drift')

# Positive genotype fitness implies strict monotonicity of F in allele frequency.
# An independent rational check samples positive fitness regimes; the proof
# derives strict monotonicity from a weighted-binomial covariance identity.
from random import Random
rng=Random(86405)
for _ in range(450):
    H=Fraction(rng.randrange(0, 31),10)
    s=Fraction(rng.randrange(1,61),20)
    y1=Fraction(rng.randrange(1,90),100)
    y2=Fraction(rng.randrange(91,100),100)
    check(F(y1,s,H)<F(y2,s,H),'strict monotonicity sample')

# Exact comparison over a dense rational grid of viable non-overdominant models.
for H in [Fraction(0),Fraction(1,12),Fraction(1,3),Fraction(1,2),
          Fraction(3,4),Fraction(11,12),Fraction(1)]:
    for aa,bb in [(Fraction(1,10),Fraction(1,20)),
                  (Fraction(2),Fraction(1)),
                  (Fraction(9,2),Fraction(1,3)),
                  (Fraction(12),Fraction(7))]:
        for xx in [Fraction(1,100),Fraction(1,10),Fraction(1,3),
                   Fraction(1,2),Fraction(4,5),Fraction(99,100)]:
            check(F(F(xx,aa,H),bb,H)>F(F(xx,bb,H),aa,H),
                  'directional strong-first exact comparison')

# All permutations of a natural four-generation multiset; varying initial x,h.
ss=(Fraction(1,5),Fraction(1,2),Fraction(1),Fraction(3))
for H in [Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(1)]:
    for xx in [Fraction(1,25),Fraction(2,5),Fraction(9,10)]:
        seq=[]
        for order in permutations(ss):
            y=xx
            for s in order:y=F(y,s,H)
            seq.append((order,y))
        max_order=max(seq,key=lambda z:z[1])[0]
        min_order=min(seq,key=lambda z:z[1])[0]
        check(max_order==tuple(sorted(ss,reverse=True)), 'global max order')
        check(min_order==tuple(sorted(ss)), 'global min order')
        check(len({v for _,v in seq})>1, 'nontrivial composition values')

# Sharp failure beyond directional-dominance range h>1, using exact fractions.
H=Fraction(2); aa=Fraction(2); bb=Fraction(1)
for xx,sign in [(Fraction(1,100),-1),(Fraction(1,3),1),
                (Fraction(1,2),1),(Fraction(2,3),0)]:
    delta=F(F(xx,aa,H),bb,H)-F(F(xx,bb,H),aa,H)
    check((delta>0)-(delta<0)==sign,'overdominance crossover')
# For these parameters Q=-1+17x-4x^2 has a unique root in (0,1).
check(factor(q.subs({h:2,a:2,b:1})) == -4*x*x+17*x-1,
      'explicit crossover quadratic')
check(q.subs({h:2,a:2,b:1,x:Fraction(1,100)})<0 and
      q.subs({h:2,a:2,b:1,x:Fraction(1,3)})>0,'crossover bracketing')

print('PASS: symbolic identities and',count,'exact checks')
