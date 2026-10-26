"""Exact symbolic and independent numerical checks for a two-state Magnus endpoint theorem."""
from math import sqrt, log, exp, isclose
from random import Random
from sympy import Matrix, symbols, Rational, sqrt as Sqrt, simplify, eye


def Q(a,b):
    return Matrix([[-a,b],[a,-b]])

a,b,c,d,s,h=symbols('a b c d s h', real=True)
alpha=Rational(1,2)+Sqrt(3)/3
beta=Rational(1,2)-Sqrt(3)/3
assert simplify(alpha+beta-1)==0
assert simplify(alpha/(-beta)-(7+4*Sqrt(3)))==0
A=Q(a,s-a); B=Q(b,s-b)
L=alpha*A+beta*B
R=beta*A+alpha*B
assert (L*R + s*R).applyfunc(simplify)==Matrix.zeros(2)
assert (L*L + s*L).applyfunc(simplify)==Matrix.zeros(2)
assert (R*R + s*R).applyfunc(simplify)==Matrix.zeros(2)
q,e=symbols('q e', positive=True)
P=(eye(2)+q*L/s)*(eye(2)+q*R/s)
# For q=1-e, we have P=I+(q/s)*(L+e R).
target=eye(2)+q*(L+e*R)/s
assert (P-target.subs(e,1-q)).applyfunc(simplify)==Matrix.zeros(2)
w1=alpha+beta*e; w2=beta+alpha*e
assert (L+e*R-(w1*A+w2*B)).applyfunc(simplify)==Matrix.zeros(2)
assert simplify(w1+w2-(1+e))==0
assert simplify((1-q*(1+e)-e*e).subs(q,1-e))==0

# The universal threshold is characterized by w2=0; after threshold,
# row-2/column-1 transition is q*(w1*a+w2*b)/s, and its transpose by
# the corresponding complementary exit intensities.
ecrit=simplify(-beta/alpha)
assert simplify(ecrit-(7-4*Sqrt(3)))==0
assert simplify(w2.subs(e,ecrit))==0
assert simplify(w1.subs(e,ecrit))>0

# Counterexample, at all h past threshold, B makes the one-way rate
# while A moves in the opposite direction.
A_bad=Q(0,s); B_bad=Q(s,0)
P_bad=(eye(2)+q*(alpha*A_bad+beta*B_bad)/s)*(eye(2)+q*(beta*A_bad+alpha*B_bad)/s)
assert simplify(P_bad[1,0]-q*w2.subs(e,1-q))==0
# Each individual right/left exponential has a negative offdiagonal
# for all h>0 at the counterexample.
assert simplify((alpha*A_bad+beta*B_bad)[1,0]/s-beta)==0
assert simplify((beta*A_bad+alpha*B_bad)[0,1]/s-beta)==0

rng=Random(81737)
af=float(alpha); bf=float(beta)
for _ in range(4096):
    sf=10**rng.uniform(-2,2)
    a1=rng.random()*sf; a2=rng.random()*sf
    hh=10**rng.uniform(-4,2)/sf
    t=sf*hh/2
    ef=exp(-t); qf=-__import__('math').expm1(-t)
    W1=af+bf*ef; W2=bf+af*ef
    m21=qf*(W1*a1+W2*a2)/sf
    m12=qf*(W1*(sf-a1)+W2*(sf-a2))/sf
    # Positive real column-stochasticity iff both offdiagonals >= 0;
    # diagonal entries then >= e^(-2t) by the exact column budget.
    assert isclose(m21+m12,1-ef**2,abs_tol=8e-13)
    assert (m21>=-1e-14 and m12>=-1e-14) == (
        W1*a1+W2*a2>=-1e-12 and W1*(sf-a1)+W2*(sf-a2)>=-1e-12
    )
    assert isclose((1-m21),ef**2+m12,rel_tol=1e-12,abs_tol=1e-12)

hcrit=2*log(7+4*sqrt(3))
assert 5.26<hcrit<5.28
for n in range(1,400):
    z=hcrit*(1+n/1000)
    W2=bf+af*exp(-z/2)
    assert W2 < 0
for n in range(1,400):
    z=hcrit*(1-n/400)
    W2=bf+af*exp(-z/2)
    assert W2>0
print('VERIFY_OK: exact two-state products, coefficients, sharp universal threshold, counterexample, 4096 numerical crosschecks')
