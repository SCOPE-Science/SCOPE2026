"""Exact verification of a three-coupon sibling-deficit variance inequality.
Requires Python 3 and SymPy. Run: python verify.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
import sympy as s

x,y,z=s.symbols('x y z', nonnegative=True)
A,B,C=z+x+y,z+y,z
S=A+B+C
p,q,r=[u/S for u in (A,B,C)]
M=p*p+q*q+r*r+2*(p*q/(p+q)**2+p*r/(p+r)**2+q*r/(q+r)**2)
V=s.factor(3*M-2+12*p*q*r-M*M)
D=s.factor(s.Rational(7,12)-V)
num,den=s.fraction(D)
poly=s.Poly(num,x,y,z)
assert poly.total_degree()==16
assert len(poly.terms())==140
assert all(coef>0 for _,coef in poly.terms())
assert all((i+j)>0 for (i,j,k),coef in poly.terms())
assert s.factor(D-num/den)==0
assert s.factor(den-12*(y+2*z)**4*(x+y+2*z)**4*(x+2*y+2*z)**4*(x+2*y+3*z)**4)==0
assert s.factor(V.subs({x:0,y:0,z:1})-s.Rational(7,12))==0

# A separate finite-state exact-rational first-step calculation uses
# occupancy counts truncated at two; the third draw of a coupon cannot
# change its status in the second sibling's album.
def independent_distribution(weights):
    weights=[Fraction(w,sum(weights)) for w in weights]
    @lru_cache(None)
    def solve(state):
        if all(t>0 for t in state):
            return tuple(Fraction(int(k==sum(t==1 for t in state))) for k in (1,2,3))
        self_loop=sum(weights[i] for i in range(3) if state[i]==2)
        acc=[Fraction(0) for _ in range(3)]
        for i in range(3):
            if state[i]==2: continue
            ns=tuple(min(2,v+(i==j)) for j,v in enumerate(state))
            a=solve(ns)
            for j in range(3):acc[j]+=weights[i]*a[j]
        return tuple(v/(1-self_loop) for v in acc)
    return solve((0,0,0))

def closed_distribution(weights):
    pp=[s.Rational(u,sum(weights)) for u in weights]
    aa,bb,cc=pp
    mm=aa*aa+bb*bb+cc*cc+2*(aa*bb/(aa+bb)**2+aa*cc/(aa+cc)**2+bb*cc/(bb+cc)**2)
    t=6*aa*bb*cc
    return [s.cancel(2+t-mm),s.cancel(mm-1-2*t),s.cancel(t)]

for weights in [(1,1,1),(1,2,3),(1,1,9),(2,3,9),(1,7,19),(13,7,1),(2,2,11)]:
    a=independent_distribution(weights)
    b=closed_distribution(weights)
    assert tuple(s.Rational(v.numerator,v.denominator) for v in a)==tuple(b),(weights,a,b)
    mm=sum((k+1)*b[k] for k in range(3))
    vv=sum((k+1)**2*b[k] for k in range(3))-mm*mm
    pp,qq,rr=[s.Rational(v,sum(weights)) for v in weights]
    formula=s.cancel(3*mm-2+12*pp*qq*rr-mm*mm)
    assert vv==formula
    assert vv<=s.Rational(7,12) and (vv==s.Rational(7,12))==(weights[0]==weights[1]==weights[2])

# Comparison against an arbitrary probability law demonstrates why
# ordering all positive binomial moments/PGFs need not order variance.
# Uniform coupon-deficit law = (7,7,4)/18; generic supported law
# Q=(79,0,21)/100 has lower first and second factorial moments
# and lower PGF for z>1 (higher for 0<z<1), but greater variance.
A0=(s.Rational(7,18),s.Rational(7,18),s.Rational(4,18))
Q=(s.Rational(79,100),s.Rational(0),s.Rational(21,100))
EA=sum((k+1)*A0[k] for k in range(3));EQ=sum((k+1)*Q[k] for k in range(3))
FA=sum((k+1)*k*A0[k] for k in range(3)); FQ=sum((k+1)*k*Q[k] for k in range(3))
VA=sum((k+1)**2*A0[k] for k in range(3))-EA**2
VQ=sum((k+1)**2*Q[k] for k in range(3))-EQ**2
assert EQ<EA and FQ<FA and VQ>VA
assert (sum(A0[k] for k in (1,2))-sum(Q[k] for k in (1,2)))>0
assert A0[2]-Q[2]>0
print('PASS coefficient identity degree 16 with',len(poly.terms()),'positive terms and exact denominator')
print('PASS independent finite-state recursion at seven rate triples')
print('PASS strict uniqueness of uniform maximizer at seven triples')
print('PASS PGF/binomial-order nonimplication counterexample; VQ =',VQ,'> 7/12')
