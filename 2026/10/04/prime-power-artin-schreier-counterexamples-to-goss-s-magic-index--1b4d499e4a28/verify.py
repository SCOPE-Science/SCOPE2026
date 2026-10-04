#!/usr/bin/env python3
import itertools, math
from math import comb

# F_25 = F_5[u]/(u^2-3), encoded as a+5b for a+bu.
def add25(x,y):
    return ((x%5+y%5)%5) + 5*((x//5+y//5)%5)
def neg25(x):
    return ((-x%5)%5) + 5*((-(x//5))%5)
def mul25(x,y):
    a,b=x%5,x//5; c,d=y%5,y//5
    return ((a*c+3*b*d)%5) + 5*((a*d+b*c)%5)
ADD=[[add25(i,j) for j in range(25)] for i in range(25)]
NEG=[neg25(i) for i in range(25)]
MUL=[[mul25(i,j) for j in range(25)] for i in range(25)]
def pow25(x,e):
    r=1
    while e:
        if e&1:r=MUL[r][x]
        x=MUL[x][x];e//=2
    return r
INV=[0]+[pow25(x,23) for x in range(1,25)]
assert all(MUL[x][INV[x]]==1 for x in range(1,25))

# K = F_25[t]/(t^5-t-3), used only for the Frobenius and reciprocal-sum checks.
ZERO=(0,0,0,0,0); ONE=(1,0,0,0,0); THETA=(0,1,0,0,0)
def kadd(x,y): return tuple(ADD[x[i]][y[i]] for i in range(5))
def kneg(x): return tuple(NEG[x[i]] for i in range(5))
def kmul(x,y):
    c=[0]*9
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y):
                if b:c[i+j]=ADD[c[i+j]][MUL[a][b]]
    for k in range(8,4,-1):
        v=c[k]
        if v:
            c[k]=0
            c[k-4]=ADD[c[k-4]][v]
            c[k-5]=ADD[c[k-5]][MUL[v][3]]
    return tuple(c[:5])
def kpow(x,e):
    r=ONE
    while e:
        if e&1:r=kmul(r,x)
        x=kmul(x,x);e//=2
    return r
def kinv(x):
    assert x!=ZERO
    return kpow(x,25**5-2)
def kdiv(x,y): return kmul(x,kinv(y))

assert kpow(THETA,5)==(3,1,0,0,0)
assert kpow(THETA,25)==(1,1,0,0,0)
for r in range(1,5):
    assert kpow(THETA,25**r)==tuple([r%5,1,0,0,0])
assert kpow(THETA,25**5)==THETA

# Check sum_c 1/(z+c) = -1/(z^25-z) at z=theta exactly.
lhs=ZERO
for c in range(25):
    lhs=kadd(lhs,kinv(kadd(THETA,(c,0,0,0,0))))
rhs=kneg(kinv(kadd(kpow(THETA,25),kneg(THETA))))
assert lhs==rhs

# Polynomial finite-difference map h -> Delta(Yh)/m for a=1.
# Polynomials are low-to-high coefficient lists over F_25.
def poly_shift1(c):
    d=[0]*len(c)
    for j,cj in enumerate(c):
        if not cj: continue
        for k in range(j+1):
            d[k]=ADD[d[k]][MUL[cj][comb(j,k)%5]]
    return d

def phi(h,m):
    F=[0]+list(h)  # Y*h
    sh=poly_shift1(F)
    delta=[ADD[sh[j]][NEG[F[j]]] for j in range(len(F))]
    invm=INV[m%5]
    out=[MUL[x][invm] for x in delta[:-1]]
    assert out[-1]==1
    return tuple(out[:-1])  # lower coefficients; leading 1 is implicit

sizes=[]
for m in range(1,5):
    images=set()
    for low in itertools.product(range(25), repeat=m-1):
        h=tuple(low)+(1,)
        images.add(phi(h,m))
    expected=25**(m-1)
    assert len(images)==expected
    sizes.append(expected)

# Pascal recurrence forced by the verified bijections.
T=[[0]*5 for _ in range(5)]
for r in range(5): T[0][r]=1
for m in range(1,5): T[m][0]=0
for r in range(4):
    for m in range(1,5):
        T[m][r+1]=(T[m][r]-T[m-1][r])%5
for r in range(5):
    for m in range(5):
        assert T[m][r]==(((-1)**m)*comb(r,m))%5
coeff=[T[m][3] for m in range(5)]
assert coeff==[1,2,3,4,0]
print('VERIFY_OK q=25 p=5 n=3 frobenius_orbit=5 reciprocal_sum=exact phi_sizes=' + ','.join(map(str,sizes)) + ' coefficients=' + ','.join(map(str,coeff)))
