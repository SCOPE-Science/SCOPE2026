"""Exact-rational verification of Gaussian Hermite moment and curvature certificates.
No nonstandard dependencies. Run: python verify.py
"""
from fractions import Fraction as Q
from math import comb

def add(p,q):
    n=max(len(p),len(q)); return [(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(n)]
def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out
def pmul(p,k):return [k*v for v in p]
def hermite(n):
    if n==0:return [1]
    p=[1];r=[0,1]
    for k in range(1,n):p,r=r,add(mul([0,1],r),pmul(p,-k))
    return r
def gm(p):
    s=0;doublefact=1
    for k in range(0,len(p),2):
        if k>0:doublefact*=k-1
        s+=p[k]*doublefact
    return s
def moment(a,i,b,j):
    p=[1]
    for _ in range(i):p=mul(p,a)
    for _ in range(j):p=mul(p,b)
    return gm(p)
A,B=hermite(4),hermite(8)
assert A==[3,0,-6,0,1] and B==[105,0,-420,0,210,0,-28,0,1]
expected={(2,0):24,(3,0):1728,(4,0):368064,(0,2):40320,(0,4):3507873984921600,(1,1):0,(2,1):40320,(2,2):10115159040}
for (i,j),v in expected.items():
    w=moment(A,i,B,j);assert w==v,((i,j),w,v)
C30,C21,C12,C03=2973,121821,20195129,11892749013
# Cauchy-Schwarz for four absolute Gaussian moments; these use no quadrature.
assert C30**2 > expected[(2,0)]*expected[(4,0)]
assert C21**2 > expected[(4,0)]*expected[(0,2)]
assert C12**2 > expected[(2,2)]*expected[(0,2)]
assert C03**2 > expected[(0,2)]*expected[(0,4)]
e=Q(1,100);m=(1-6*e)**2
# Uniform upper bound on the magnitude of the Taylor error in D_z,
# divided by epsilon^2*S.
A0=e/m*(C30+Q(3,8)*e*C21+Q(5,128)*e**2*C12+e**3*Q(1,512)*C03)
# Uniform lower-bound loss from the logarithmic term in D_zz/epsilon^2.
B0=e**2/m*(C21+Q(1,8)*e*C12+e**2*Q(1,256)*C03)
assert A0<40 and B0<18
assert Q(96,1)/(1+Q(72,100)+Q(1680,10000*16))>Q(3840,73)
assert Q(3840,73)-B0>34
assert 48-Q(252,1000)-A0>7
print('Exact Hermite moments: PASS')
print('Cauchy absolute-moment ceilings: PASS')
print('Uniform D_z certificate: A0 =',A0,'=',float(A0),'(<40)')
print('Uniform D_zz certificate: B0 =',B0,'=',float(B0),'(<18)')
print('Consequent F\'\' <= -7 epsilon^2 for every 0<epsilon<=1/100 and 0<t<1: PASS (subject to analytic inequalities documented in RESULT.md)')
