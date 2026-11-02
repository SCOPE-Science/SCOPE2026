"""Exact algebra and independent finite graph checks for a Reed--Frost allocation theorem.

Python 3 and SymPy are required.  Every graph and initial seed subset is enumerated
for households of at most three individuals; no probabilistic simulations are used.
"""
from itertools import product
from fractions import Fraction
import sympy as S

p,q=S.symbols('p q')
r=1-q
F1=q
F2=2*(q+p*q*(1-q))
F3=3*(1-((1-p)**2*r+2*p*(1-p)**2*r**2+p**2*(3-2*p)*r**3))
D3=S.factor(2*F2-F1-F3)
required=p*q*(q-1)*((2+6*p-6*p*p)-q*(9*p-6*p*p))
assert S.factor(D3-required)==0
assert S.factor((2*F1-F2)-(-2*p*q*(1-q)))==0
assert S.factor((2+6*p-6*p*p)-(9*p-6*p*p))==S.factor(2-3*p)
for n in range(3,31):
    x=1-p
    lead=S.expand(-2*(n-1)*x**(n-2)+(n-2)*x**(n-3)+n*x**(n-1))
    assert S.factor(lead-p*x**(n-3)*(n*p-2))==0
assert S.factor(((2+6*p-6*p*p)/(9*p-6*p*p)).subs(p,S.Rational(9,10))-S.Rational(127,162))==0
for qq,target in [(S.Rational(1,2),-S.Rational(207,1000)),
                  (S.Rational(9,10),S.Rational(3807,125000))]:
    assert S.cancel(required.subs({p:S.Rational(9,10),q:qq})-target)==0

def independent_expected(n,P,Q):
    """Exact expectation using all directed contact graphs and seed sets."""
    if n==0: return Fraction(0)
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    total=Fraction(0)
    for bits in product((0,1),repeat=len(edges)):
        eprob=P**sum(bits)*(1-P)**(len(edges)-sum(bits))
        arcs=[[] for _ in range(n)]
        for (a,b),flag in zip(edges,bits):
            if flag: arcs[a].append(b)
        for seeds in product((0,1),repeat=n):
            prob=eprob*Q**sum(seeds)*(1-Q)**(n-sum(seeds))
            reached={i for i in range(n) if seeds[i]}
            queue=list(reached)
            for z in queue:
                for w in arcs[z]:
                    if w not in reached:
                        reached.add(w)
                        queue.append(w)
            total+=prob*len(reached)
    return total

count=0
for P in [Fraction(i,10) for i in [1,2,4,6,7,8,9]]:
    for Q in [Fraction(i,10) for i in [1,2,4,5,6,8,9]]:
        for n,closed in [(1,F1),(2,F2),(3,F3)]:
            got=independent_expected(n,P,Q)
            symbolic=closed.subs({p:S.Rational(P.numerator,P.denominator),
                                  q:S.Rational(Q.numerator,Q.denominator)})
            assert S.Rational(got.numerator,got.denominator)==symbolic,(n,P,Q)
            count+=1
print('PASS: polynomial identities, 28 high-seeding leading-term identities,')
print(f'{count} fully enumerated independent exact-rational epidemic expectations,')
print('and two exact vaccine-allocation witnesses.')
