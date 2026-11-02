#!/usr/bin/env python3
"""Exact arithmetic for the 28-line Fermat-quartic reduction theorem.
Standard library only. No numerical tolerances or external data.
"""
from collections import Counter
from itertools import combinations

def bareiss_det(a):
    a=[list(row) for row in a]
    n=len(a)
    sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((j for j in range(k+1,n) if a[j][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=a[i][j]*pivot-a[i][k]*a[k][j]
                assert x%prev==0
                a[i][j]=x//prev
            a[i][k]=0
        prev=pivot
    return sign*a[n-1][n-1]

# The cyclotomic ring Z[zeta]/(zeta^4+1) and the field norm.
def za(a,b):return tuple(x+y for x,y in zip(a,b))
def zn(a):return tuple(-x for x in a)
def zs(a,b):return za(a,zn(b))
def zm(a,b):
    u=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):u[i+j]+=x*y
    for i in range(6,3,-1):u[i-4]-=u[i]
    return tuple(u[:4])
def zp(a,n):
    y=(1,0,0,0)
    for _ in range(n):y=zm(y,a)
    return y
def norm(a):
    mult=[zm(a,tuple(int(i==j) for i in range(4))) for j in range(4)]
    return bareiss_det([[mult[j][i] for j in range(4)] for i in range(4)])
def zline():
    one=(1,0,0,0);zero=(0,0,0,0);z=(0,1,0,0)
    po=[zp(z,j) for j in range(8)]
    H=[];B=[]
    for t in range(3):
        for j in (1,3,5,7):
            u=po[j]
            H.append(((one,zn(u),zero),(zero,one,zn(u)),(zn(u),zero,one))[t])
    for a in range(4):
        for b in range(4): B.append((one,po[2*a],po[2*b]))
    return H+B

def det3(v):
    a,b,c=v
    return za(zs(zm(a[0],zs(zm(b[1],c[2]),zm(b[2],c[1]))),zm(a[1],zs(zm(b[0],c[2]),zm(b[2],c[0])))),zm(a[2],zs(zm(b[0],c[1]),zm(b[1],c[0]))))

def integral_certificate():
    L=zline();assert len(L)==28 and len(set(L))==28
    allnorm=Counter();byH={h:Counter() for h in range(4)}
    for I in combinations(range(28),3):
        N=abs(norm(det3([L[i] for i in I])))
        allnorm[N]+=1;byH[sum(i<12 for i in I)][N]+=1
    expected={0:60,1:384,2:64,4:864,8:384,9:192,16:560,17:192,32:96,36:192,64:192,256:64,400:32}
    assert dict(allnorm)==expected, (allnorm,expected)
    assert sum(allnorm.values())==3276
    assert {p for n in allnorm for p in (3,5,17) if n!=0 and n%p==0}=={3,5,17}
    assert all(n==0 or all(n%p for p in [7,11,13,19,23,29,31]) for n in allnorm)
    assert byH[3]==Counter({0:12,4:96,2:64,16:48})
    assert byH[2]==Counter({1:384,4:192,17:192,9:192,16:96})
    assert byH[1]==Counter({4:576,8:384,16:192,36:192,32:96})
    assert byH[0]==Counter({0:48,16:224,64:192,256:64,400:32})
    return expected

# F_p[T]/(minimal polynomial) where zeta^4=-1; p=17 uses zeta=2.
def finite_lines(p,co=None,root=None):
    if root is None:
        assert co is not None and co[-1]==1
        d=len(co)-1
    else:d=1
    z=(0,)*d;one=(1,)+(0,)*(d-1)
    def neg(a):return tuple(-x%p for x in a)
    def add(a,b):return tuple((x+y)%p for x,y in zip(a,b))
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):
        t=[0]*(2*d-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):t[i+j]+=x*y
        for i in range(len(t)-1,d-1,-1):
            for j in range(d):t[i-d+j]-=t[i]*co[j]
        return tuple(x%p for x in t[:d])
    def power(a,n):
        b=one
        for _ in range(n):b=mul(b,a)
        return b
    def cross(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
    def dot(a,b):return add(add(mul(a[0],b[0]),mul(a[1],b[1])),mul(a[2],b[2]))
    zz=(root%p,) if root is not None else tuple(int(i==1) for i in range(d))
    assert power(zz,4)==neg(one)
    pw=[power(zz,j) for j in range(8)]
    lines=[]
    for t in range(3):
        for j in (1,3,5,7):
            u=pw[j]
            lines.append(((one,neg(u),z),(z,one,neg(u)),(neg(u),z,one))[t])
    for a in range(4):
        for b in range(4):lines.append((one,pw[2*a],pw[2*b]))
    assert len(lines)==len(set(lines))==28
    intsets={}
    for i,j in combinations(range(28),2):
        point=cross(lines[i],lines[j]);assert any(point)
        hit=frozenset(k for k,L in enumerate(lines) if dot(L,point)==z)
        assert i in hit and j in hit
        intsets[hit]=point
    assert sum(len(s)*(len(s)-1)//2 for s in intsets)==378
    counts=Counter(map(len,intsets))
    patterns={m:Counter(tuple(sorted('H' if i<12 else 'B' for i in s)) for s in intsets if len(s)==m) for m in counts}
    return counts, patterns, intsets

def main():
    print('INTEGRAL_TRIPLE_DETERMINANT_NORMS',dict(sorted(integral_certificate().items())))
    data=[(3,[2,2,1],None,{4:63}),
          (5,[3,0,1],None,{2:240,3:16,4:15}),
          (7,[1,4,1],None,{2:288,4:15}),
          (17,None,2,{2:144,3:48,4:15})]
    for p,co,root,expected in data:
        counts,patterns,intsets=finite_lines(p,co,root)
        assert dict(counts)==expected,(p,counts)
        if p==5:
            assert patterns[3]==Counter({('B','B','B'):16})
        if p==17:
            assert patterns[3]==Counter({('B','H','H'):48})
        if p==3:
            assert patterns[4]==Counter({('B','B','H','H'):48,('B','B','B','B'):12,('H','H','H','H'):3}),patterns[4]
        print('CHARACTERISTIC',p,'INCIDENCE',dict(sorted(counts.items())),'TRIPLE_PATTERNS',dict(patterns.get(3,{})))
    print('FERMAT_28_BITANGENTS_ARITHMETIC_INCIDENCE_EXACT_OK')

if __name__=='__main__':main()
