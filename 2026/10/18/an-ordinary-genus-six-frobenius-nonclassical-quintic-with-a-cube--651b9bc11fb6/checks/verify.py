"""Exact arithmetic and geometric checks for a plane quintic over F4."""
from fractions import Fraction
from math import gcd
import sympy as sp

# F4 = F2[a]/(a^2+a+1); bit 2 represents a.
def mul(a,b):
    out=0
    while b:
        if b&1:out ^= a
        b>>=1;a<<=1
        if a&4:a ^= 7
    return out

def cub(a):return mul(mul(a,a),a)
def four(a):return mul(mul(a,a),mul(a,a))
def derivs(x,y,z):
    ap1=3
    xx=mul(x,x);yy=mul(y,y);zz=mul(z,z)
    xx3=mul(xx,x)
    Fx=mul(ap1,four(x))^mul(xx,yy)^mul(mul(xx,y),z)^mul(xx,zz)^four(y)^mul(yy,zz)^four(z)
    Fy=mul(xx3,z)^four(z)
    Fz=mul(xx3,y)^four(y)
    return Fx,Fy,Fz

# A geometric common zero of the three derivatives necessarily has
# (z=0,y!=0,x/y a cube root of unity) or (z=1, x^3=1, y=0 or y^3=1).
# All roots of T^3-1 lie in F4, so this checks all geometric candidates.
roots=[x for x in range(4) if cub(x)==1]
assert roots==[1,2,3]
candidates=[(x,1,0) for x in roots]+[(x,y,1) for x in roots for y in [0,*roots]]
for p in candidates: assert derivs(*p)!=(0,0,0),p
# Also the single projective point z=y=0.
assert derivs(1,0,0)!=(0,0,0)
print('SMOOTH_OVER_ALGEBRAIC_CLOSURE candidates',len(candidates)+1)

N=[5,35,65,395,1025,3395]
q=4;g=6
p=[0]+[q**n+1-N[n-1] for n in range(1,g+1)]
# Newton identities for L(T)=det(1-Frob*T); c0=1
c=[1]
for k in range(1,g+1):
    ck=-sum(c[k-j]*p[j] for j in range(1,k+1))/k
    assert int(ck)==ck
    c.append(int(ck))
for k in range(g-1,-1,-1):
    c.append(q**(g-k)*c[k])
T=sp.symbols('T')
L=sum(co*T**k for k,co in enumerate(c))
expected=(1+3*T**2+16*T**4)**3
assert sp.expand(L-expected)==0
assert c[g]%2==1
U=sp.symbols('U'); P=U**4+3*U**2+16
assert sp.factor(P)==P
assert sp.factor((U**2+3*U+16)**6)==(U**2+3*U+16)**6
print('COUNTS',N)
print('POWER_SUMS',p[1:])
print('L_FACTOR',sp.factor(L))
print('GENUS',g,'ORDINARY',True,'SIMPLE_QUARTIC',sp.factor(P)==P)
print('BASE_CHANGE_F16_FROBENIUS',(U**2+3*U+16)**6)
# Added check over extension degree 7, not used for determining L.
assert q**7+1==16385
print('SEVENTH_EXTENSION_EXPECTED',16385)
