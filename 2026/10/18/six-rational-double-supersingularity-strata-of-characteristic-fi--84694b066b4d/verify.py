#!/usr/bin/env python3
"""Exact finite-field polynomial checks for the characteristic-five Ciani strata.
Only Python's standard library is required; finite enumeration is supplementary.
"""
from itertools import product
PCHAR = 5
class Poly:
    def __init__(self, terms=None):
        self.d = {tuple(k):v%5 for k,v in (terms or {}).items() if v%5}
    @staticmethod
    def const(c): return Poly({(0,0,0): c})
    def __add__(self, b):
        b = cv(b)
        d = self.d.copy()
        for k,v in b.d.items(): d[k] = (d.get(k,0)+v)%5
        return Poly(d)
    __radd__ = __add__
    def __neg__(self): return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,b): return self + (-cv(b))
    def __rsub__(self,b): return cv(b)-self
    def __mul__(self,b):
        b=cv(b);d={}
        for k,v in self.d.items():
            for h,w in b.d.items():
                z=tuple(k[i]+h[i] for i in range(3))
                d[z]=(d.get(z,0)+v*w)%5
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        res=cv(1);base=self
        while n:
            if n&1: res=res*base
            base=base*base;n>>=1
        return res
    def __eq__(self,b): return self.d==cv(b).d
    def eval(self,r,s,t): return sum(v*(r**k[0])*(s**k[1])*(t**k[2]) for k,v in self.d.items())%5
    def subst(self,R,S,T):
        return sum((R**k[0])*(S**k[1])*(T**k[2])*v for k,v in self.d.items())
def cv(b): return b if isinstance(b,Poly) else Poly.const(b)
r=Poly({(1,0,0):1});s=Poly({(0,1,0):1});t=Poly({(0,0,1):1})
H1=2*(r*t-2*s)**2+(r**2-4)*(t**2-4)
H2=2*(r*s-2*t)**2+(r**2-4)*(s**2-4)
H3=2*(s*t-2*r)**2+(s**2-4)*(t**2-4)
assert H1-H2==-2*(r**2+1)*(t**2-s**2)
assert H1-H3==-2*(t**2+1)*(r**2-s**2)
assert H2-H3==-2*(s**2+1)*(r**2-t**2)
assert H1.subst(r,s,s)==(r-2)*((r+2)-2*s**2*(r+1))
assert H1.subst(r,s,-s)==(r+2)*((r-2)-2*s**2*(r-1))
# Parameter f(s)=N(s)/D(s). All equalities verified by clearing D^2.
N=2-2*s**2;D=2*s**2-1
assert N**2-4*D**2==-2*s**2*(s**2-4)
assert N**2+2*s**2*D**2-N*s**2*D-4*D**2 == 2*s**2*(s**2-4)**2
assert N**2-s**2*D**2 == (s**2-4)*(s**2+2*s-2)*(s**2-2*s-2)
# The signed graph r=epsilon f(s), t=epsilon s has H1=H2=0.
for eps in (1,-1):
    # H_i has degree <=2 in r, so substitution r=eps*N/D and t=eps*s
    def cleared(H):
        total=cv(0)
        for (a,b,c),v in H.d.items():
            assert a<=2
            total+=v*(eps*N)**a*s**b*(eps*s)**c*D**(2-a)
        return total
    assert cleared(H1)==0 and cleared(H2)==0
# Boundary excluded: s=0, s^2=4, D=0. All remaining graphs are smooth by the identity above.
# Every smooth F_5 parameter is exhaustively checked in 125 possibilities.
counts={i:0 for i in range(4)}
double=[]
for R,S,T in product(range(5),repeat=3):
    if (R*R-4)%5==0 or (S*S-4)%5==0 or (T*T-4)%5==0: continue
    if (R*R+S*S+T*T-R*S*T-4)%5==0: continue
    a=sum(H.eval(R,S,T)==0 for H in (H1,H2,H3))
    counts[a]+=1
    if a>=2: double.append((R,S,T,a))
assert counts=={0:11,1:0,2:12,3:0},counts
assert len(double)==12
# Exact factor identities for the finite triple-root census, in q.
q=s
assert ((q**2+2)**2-q**3)==(q+1)**2*(q**2+2*q-1)
assert (q**2+2*q-1).eval(0,4,0)!=0
print('POLYNOMIAL_IDENTITIES_OK')
print('GF5_SMOOTH_PARAMETER_COUNTS_BY_A_NUMBER',counts)
print('GF5_A2_PARAMETERS',double)
print('VERIFY_OK')
