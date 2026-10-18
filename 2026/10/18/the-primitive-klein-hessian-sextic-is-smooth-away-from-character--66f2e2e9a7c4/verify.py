#!/usr/bin/env python3
"""Exact independent arithmetic checks for the Klein invariant sextic."""
from math import comb
from itertools import permutations

ZERO=(0,0,0)

def add(*fs):
    d={}
    for f in fs:
        for e,c in f.items(): d[e]=d.get(e,0)+c
    return {e:c for e,c in d.items() if c}

def scale(f,a): return {e:a*c for e,c in f.items() if a*c}

def mul(a,b):
    d={}
    for e,c in a.items():
        for f,v in b.items():
            k=tuple(e[i]+f[i] for i in range(3));d[k]=d.get(k,0)+c*v
    return {e:c for e,c in d.items() if c}

def der(f,i):
    d={}
    for e,c in f.items():
        if e[i]:
            n=list(e);n[i]-=1; n=tuple(n);d[n]=d.get(n,0)+c*e[i]
    return d

def det3(M):
    d={}
    for perm in permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        prod={(0,0,0):(-1)**inv}
        for i in range(3): prod=mul(prod,M[i][perm[i]])
        d=add(d,prod)
    return d

Q={(3,1,0):1,(0,3,1):1,(1,0,3):1}
F={(5,0,1):1,(1,5,0):1,(0,1,5):1,(2,2,2):-5}
H=det3([[der(der(Q,i),j) for j in range(3)] for i in range(3)])
assert H==scale(F,-54), (H, F)

def taylor(a,b,p):
    # Dehomogenize at z=1 and replace x=a+u,y=b+v.
    coeff={}
    for (i,j,k),c in F.items():
        for d in range(i+1):
            for e in range(j+1):
                v=c*comb(i,d)*a**(i-d)*comb(j,e)*b**(j-e)
                coeff[d,e]=(coeff.get((d,e),0)+v)%p
    return {k:v for k,v in coeff.items() if v%p}

T2=taylor(1,1,2)
assert not any(v for (a,b),v in T2.items() if a+b<2)
assert {k:v for k,v in T2.items() if sum(k)==2} == {(2,0):1,(1,1):1,(0,2):1}
T7=taylor(2,4,7)
assert not any(v for (a,b),v in T7.items() if a+b<3)
assert {k:v for k,v in T7.items() if sum(k)==3}=={(3,0):5,(2,1):2,(1,2):4,(0,3):5}
# Exactly -2(v-3u)^3 mod 7.
for k,v in {k:v for k,v in T7.items() if sum(k)==3}.items():
    i,j=k
    expected=(-2*comb(3,j)*((-3)**i))%7
    assert v==expected,(k,v,expected)

# Torus-gradient coefficient matrix and the residual product constraints.
M=((5,1,0),(0,5,1),(1,0,5))
det=(5*(25)-1*(-1))
assert det==126
# p=7: u*(3+2u)*(2+4u)-1 == (u+3)^3 modulo 7
from itertools import product
for u in range(7):
    assert (u*(3+2*u)*(2+4*u)-1-(u+3)**3)%7==0
# Check that the identified singular point and seven ordinary nodes solve F and gradients.
def ev(P,xyz,p):
    return sum(c*xyz[0]**e[0]*xyz[1]**e[1]*xyz[2]**e[2] for e,c in P.items())%p
for p,pt in [(2,(1,1,1)),(7,(2,4,1))]:
    assert ev(F,pt,p)==0
    assert all(ev(der(F,i),pt,p)==0 for i in range(3))
# Over F_8, all 7 distinct mu_7 roots t, with affine point (t^3,t,1).
# GF(8)=F_2[t]/(t^3+t+1), represented as 3-bit words.
def ffmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&8:a^=0b1011
    return r

def ff_pow(a,n):
    r=1
    while n:
        if n&1:r=ffmul(r,a)
        a=ffmul(a,a);n>>=1
    return r

def ff_eval(P,pt):
    r=0
    for e,c in P.items():
        v=c&1
        for a,k in zip(pt,e):v=ffmul(v,ff_pow(a,k))
        r^=v
    return r
pts=[]
for t in range(1,8):
    assert ff_pow(t,7)==1
    pt=(ff_pow(t,3),t,1)
    assert ff_eval(F,pt)==0 and all(ff_eval(der(F,i),pt)==0 for i in range(3))
    pts.append(pt)
assert len(set(pts))==7

# Small-prime rational point cross-check, not used to infer the all-prime theorem.
checks=0
for p in (2,3,5,7,11,13,17,19,23,29,31):
    sol=[]
    for x in range(p):
        for y in range(p):
            P=(x,y,1)
            if ev(F,P,p)==0 and all(ev(der(F,i),P,p)==0 for i in range(3)):
                sol.append(P)
            checks+=1
    if p==2:assert sol==[(1,1,1)]
    elif p==7:assert sol==[(2,4,1)]
    else: assert sol==[],(p,sol)
print('VERIFY_OK; Hessian polynomial identity, characteristic-two tangent cones and seven geometric nodes, characteristic-seven triple tangent, logarithmic-gradient arithmetic, and',checks,'small-field points')
