"""Exact rank certificates for single-degree S^3 harmonic sampling on a 5 by 5 Clifford grid.
Requires Python >=3.9, standard library only.
"""
from fractions import Fraction as F
from collections import Counter

class Q5:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        self.a=F(a);self.b=F(b)
    @staticmethod
    def coerce(v): return v if isinstance(v,Q5) else Q5(v)
    def __add__(self,other):
        o=self.coerce(other);return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Q5(-self.a,-self.b)
    def __sub__(self,other):return self+-self.coerce(other)
    def __rsub__(self,other):return self.coerce(other)+-self
    def __mul__(self,other):
        o=self.coerce(other);return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,other):
        o=self.coerce(other);den=o.a*o.a-5*o.b*o.b
        assert den!=0
        return Q5((self.a*o.a-5*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        return ((a*a>5*b*b)-(a*a<5*b*b))*(1 if a>0 else -1)
    def __eq__(self,other):
        o=self.coerce(other);return self.a==o.a and self.b==o.b
    def __repr__(self):return f'({self.a})+({self.b})sqrt(5)'

ZERO=Q5(0);ONE=Q5(1)
C=[ONE,Q5(F(-1,4),F(1,4)),Q5(F(-1,4),F(-1,4)),Q5(F(-1,4),F(-1,4)),Q5(F(-1,4),F(1,4))]
D=[[ (C[j]+C[k])/2 for k in range(5)] for j in range(5)]
assert D[0][0]==ONE

def eigenvalue_grid(arr,u,v):
    # Sum of each real-valued kernel times real DFT character.
    # The conjugate sine sum vanishes under simultaneous sign reversal.
    return sum((arr[j][k]*C[(u*j+v*k)%5] for j in range(5) for k in range(5)),ZERO)

U_before=[[ONE for k in range(5)] for j in range(5)] # U_0
U_now=[[2*D[j][k] for k in range(5)] for j in range(5)] # U_1
expected=[1,4,8,16,21,25,24]
for L in range(0,48):
    arr=(U_before if L==0 else U_now)
    ev={(u,v):eigenvalue_grid(arr,u,v) for u in range(5) for v in range(5)}
    signs=Counter(x.sign() for x in ev.values())
    assert signs[-1]==0,('not psd',L,ev)
    rank=signs[1]
    if L<len(expected): assert rank==expected[L],(L,rank)
    else:assert rank==25,(L,rank,[i for i,x in ev.items() if x.sign()==0])
    if L==5:
        expected_eigs={F(125,16):4,F(125,8):4,F(225,32):4,F(25,8):5,F(25,16):8}
        assert Counter({e.a:sum(z.a==e.a for z in ev.values()) for e in ev.values()}) == Counter(expected_eigs)
        assert all(x.b==0 for x in ev.values())
    if L==6:
        expected_eigs={F(0):1,F(125,16):4,F(25,64):4,F(725,64):4,F(75,16):4,F(625,64):8}
        assert Counter({e.a:sum(z.a==e.a for z in ev.values()) for e in ev.values()}) == Counter(expected_eigs)
        assert all(x.b==0 for x in ev.values())
        assert {key for key,v in ev.items() if v==ZERO}=={(0,0)}
        print('degree 6 only lost Fourier character = (0,0)')
    if L==5:
        print('degree 5 smallest eigenvalue numerically',min(float(q.a)+float(q.b)*5**.5 for q in ev.values()))
    if L in (0,1,2,3,4,5,6,7,47):
        print('degree',L,'rank',rank,'nullity',25-rank)
    # move forward U_{L+1} from U_L and U_{L-1}
    if L>=1:
        U_before,U_now=U_now,[[2*D[j][k]*U_now[j][k]-U_before[j][k] for k in range(5)] for j in range(5)]
print('All 25 exact algebraic Fourier eigenvalues nonnegative at degrees 0..47.')
print('Ranks (1,4,8,16,21,25,24) at degrees 0..6; rank25 at degrees7..47.')
print('Analytic tail: each nonzero difference has |dot| <= (1+sqrt5)/4 < sqrt(3)/2.')
print('Thus |U_L(dot)| < 2 and each Gershgorin row has off-diagonal sum <48,')
print('while diagonal U_L(1)=L+1>=49 for L>=48, implying strict PD.')
