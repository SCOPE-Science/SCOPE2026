from fractions import Fraction
# Pic coordinates (h,e1,e2,e3)
def dot(a,b): return a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
H=(1,0,0,0); E1=(0,1,0,0); E2=(0,0,1,0); E3=(0,0,0,1)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
D1=E1; D2=sub(sub(H,E1),E3); D3=E3; D4=sub(sub(H,E2),E3); D5=E2; D6=sub(sub(H,E1),E2)
Ds=[D1,D2,D3,D4,D5,D6]
beta=(4,-2,-1,-1)
Kneg=(3,-1,-1,-1)
assert dot(Kneg,beta)==8, "c1.beta must be 8"
assert 2-3+1+8==8
# linear relations in Pic
def add(a,b): return tuple(x+y for x,y in zip(a,b))
assert add(D1,D2)==add(D4,D5), "D1+D2=D4+D5"
assert add(D2,D3)==add(D5,D6), "D2+D3=D5+D6"
# hence every k-vector satisfies:
# k1+k2-k4-k5=0, k2+k3-k5-k6=0 ; check for beta
ks=[dot(d,beta) for d in Ds]
assert ks==[2,1,1,2,1,1], ks
assert ks[0]+ks[1]-ks[3]-ks[4]==0
assert ks[1]+ks[2]-ks[4]-ks[5]==0
# single-1 patterns violate relations
import itertools
for i in range(6):
    e=[0]*6; e[i]=1
    r1=e[0]+e[1]-e[3]-e[4]; r2=e[1]+e[2]-e[4]-e[5]
    assert (r1,r2)!=(0,0), f"e{i} should violate"
print("relations + pattern elimination OK")
# dual basis checks: <H,H>=1, <H,Ei>=0, <Ei,Ej>=-dij, <pt,1>=1
assert dot(H,H)==1
assert dot(E1,E1)==-1 and dot(H,E1)==0
print("pairing OK")
# effectivity combo
def smul(c,a): return tuple(c*x for x in a)
combo=add(add(add(smul(2,E2),smul(2,E3)),add(smul(2,D4),D2)),D6)
assert combo==beta
print("effectivity OK")
# invariant
from math import factorial
pf=1
for k in ks: pf*=factorial(k)
assert pf==4
def harm(k): return sum(Fraction(1,m) for m in range(1,k+1))
S=[Fraction(0)]*4
for k,d in zip(ks,Ds):
    h=harm(k)
    S=[s+h*x for s,x in zip(S,d)]
assert S[0]==Fraction(7,2), S
assert -Fraction(1,4)*S[0]==Fraction(-7,8)
print("invariant -7/8 OK")
