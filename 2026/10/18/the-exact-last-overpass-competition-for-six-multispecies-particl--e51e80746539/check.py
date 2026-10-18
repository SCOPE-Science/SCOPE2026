"""Exact symbolic verification for a six-particle continuous-time sorting chain.
Run: python check.py   (requires sympy>=1.11)
The recursion enumerates every nonterminal arrangement of 0,0,1,1,2,2.
"""
from functools import lru_cache
from itertools import permutations
from fractions import Fraction
import sympy as S

x = S.symbols('x', positive=True)
initial=(2,2,1,1,0,0)
terminal=(0,0,1,1,2,2)
A=256*x**9+3968*x**8+27648*x**7+114496*x**6+299902*x**5+498185*x**4+513714*x**3+313926*x**2+103375*x+14098
D=8*(x+1)**3*(x+2)**5*(2*x+1)**5
B=112784*x**8+991456*x**7+3729476*x**6+7807043*x**5+9913144*x**4+7807043*x**3+3729476*x**2+991456*x+112784
C=128*x**12+2112*x**11+15936*x**10+73184*x**9+216086*x**8+413491*x**7+513385*x**6+413491*x**5+216086*x**4+73184*x**3+15936*x**2+2112*x+128

def moves(state):
    ans=[]
    for j in range(5):
        high,low=state[j:j+2]
        if high<=low: continue
        rate = S.Integer(1) if (high,low)==(1,0) else x if (high,low)==(2,1) else 1+x
        new=list(state);new[j],new[j+1]=new[j+1],new[j]
        ans.append((rate,tuple(new),(high,low)))
    return ans

@lru_cache(None)
def probability(state):
    if state==terminal: return S.Integer(0)
    arcs=moves(state)
    assert arcs, state
    normalizer=sum(rate for rate,_,_ in arcs)
    total=S.Integer(0)
    for rate,nxt,pair in arcs:
        if nxt==terminal: value=S.Integer(int(pair==(1,0)))
        else: value=probability(nxt)
        total +=rate*value
    return S.cancel(total/normalizer)

all_states=set(permutations(initial))
assert len(all_states)==90
for state in all_states:
    if state!=terminal: probability(state)
assert probability.cache_info().currsize==89
F=probability(initial)
assert S.cancel(F-x**4*A/D)==0
assert S.cancel(S.diff(F,x)-x**3*B/(8*(x+1)**4*(x+2)**6*(2*x+1)**6))==0
assert S.expand(2*x**4*A-D-2*(x-1)*C)==0
assert S.cancel(F+F.subs(x,1/x)-1)==0
assert S.cancel(F.subs(x,1)-S.Rational(1,2))==0
assert S.cancel(F.subs(x,2)-S.Rational(1465319,1800000))==0
assert S.limit(F,x,0,dir='+')==0
assert S.limit(F,x,S.oo)==1
assert all(z>0 for z in S.Poly(B,x).all_coeffs())
assert all(z>0 for z in S.Poly(C,x).all_coeffs())
print('PASS: 90 arrangements, exact recurrence, rational formula, derivative, positivity, symmetry, two boundaries.')
print('P(2)=',F.subs(x,2))
