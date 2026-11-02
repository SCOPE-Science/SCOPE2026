#!/usr/bin/env python3
"""Independent finite group multiplication and automorphism-orbit verifier.
Run: python3 verify_extraspecial_involution_orbits.py
No external packages required.
"""
from itertools import product
from math import prod

def getbit(v,i):return (v>>i)&1

def q(v,m,eps):
    s=0
    for j in range(m):
        a,b=getbit(v,2*j),getbit(v,2*j+1)
        s ^= a&b
    if eps=='-': s ^= getbit(v,0)^getbit(v,1)
    return s

def omega(u,v,m):
    s=0
    for j in range(m):
        s^=getbit(u,2*j)*getbit(v,2*j+1)^getbit(u,2*j+1)*getbit(v,2*j)
    return s

def mul(g,h,m,eps):
    u,c=g;v,d=h
    k=c^d
    for j in range(m): k ^= getbit(u,2*j+1)&getbit(v,2*j)
    if eps=='-': k ^= getbit(u,0)&getbit(v,0);k ^= getbit(u,1)&getbit(v,1)
    return (u^v,k)

def gmul(a,b,m,eps):
    return mul((a>>1,a&1),(b>>1,b&1),m,eps)[0]*2+mul((a>>1,a&1),(b>>1,b&1),m,eps)[1]

def iso(v,cols):
    y=0;i=0
    while v:
        if v&1:y^=cols[i]
        v>>=1;i+=1
    return y

def generate_isometries(m,eps):
    n=2*m; N=1<<n
    # enumerate images of an ordered quadratic basis preserving all Gram and square entries
    out=[]
    def back(cols,span):
        i=len(cols)
        if i==n:
            out.append(tuple(cols));return
        for v in range(1,N):
            if v in span or q(v,m,eps)!=q(1<<i,m,eps):continue
            if any(omega(v,cols[j],m)!=omega(1<<i,1<<j,m) for j in range(i)):continue
            back(cols+[v],span|{v^w for w in span})
    back([], {0})
    return out

def auto_table(cols,twist,m,eps):
    n=2*m;N=1<<n; res=[]
    for g in range(2*N):
        v,c=g>>1,g&1; h=(0,c)
        for i in range(n):
            if v>>i & 1: h=mul(h,(cols[i],getbit(twist,i)),m,eps)
        res.append(2*h[0]+h[1])
    return res

def homs(m,eps,r):
    n=2*m;gsize=1<<(n+1)
    inv=[g for g in range(gsize) if q(g>>1,m,eps)==0]
    return [tt for tt in product(inv,repeat=r) if all(omega(tt[i]>>1,tt[j]>>1,m)==0 for i in range(r) for j in range(i))]

def invariant(tt,m,eps):
    r=len(tt); K=[]
    for b in range(1<<r):
        p=(0,0)
        for i in range(r):
            if b>>i & 1: p=mul(p,(tt[i]>>1,tt[i]&1),m,eps)
        if p[0]==0:K.append((b,p[1]))
    return tuple(K)

def gauss(r,d):
    if d<0 or d>r:return 0
    num=prod(2**r-2**i for i in range(d))
    den=prod(2**d-2**i for i in range(d))
    return num//den

def singular_count(m,eps,d):
    if d==0:return 1
    if eps=='+':
        if d>m:return 0
        return gauss(m,d)*prod(2**(m-i-1)+1 for i in range(d))
    if d>=m:return 0
    return gauss(m-1,d)*prod(2**(m-i)+1 for i in range(d))

def formulas(m,eps,r):
    w=m if eps=='+' else m-1
    total=sum((2**r)*singular_count(m,eps,d)*prod(2**r-2**j for j in range(d)) for d in range(min(w,r)+1))
    orbits=sum(gauss(r,d)*2**(r-d) for d in range(min(w,r)+1))
    return total,orbits

def check(m,eps,r):
    n=2*m; N=1<<n;tt=homs(m,eps,r)
    exp_count,exp_orbits=formulas(m,eps,r)
    assert len(tt)==exp_count,(m,eps,r,len(tt),exp_count)
    invs={invariant(x,m,eps) for x in tt}
    assert len(invs)==exp_orbits,(m,eps,r,len(invs),exp_orbits)
    O=generate_isometries(m,eps)
    expect_order={(1,'+'):2,(1,'-'):6,(2,'+'):72,(2,'-'):120}[(m,eps)]
    assert len(O)==expect_order,(m,eps,len(O))
    # Independent action verification: identify genuine automorphism orbits by union-find.
    tables=[auto_table(cols,0,m,eps) for cols in O]
    tables += [auto_table(tuple(1<<i for i in range(n)),1<<i,m,eps) for i in range(n)]
    ix={t:i for i,t in enumerate(tt)}
    par=list(range(len(tt)))
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]];x=par[x]
        return x
    def union(a,b):
        a=find(a);b=find(b)
        if a!=b:par[b]=a
    for t in tt:
        i=ix[t]
        for tab in tables:
            dest=tuple(tab[x] for x in t)
            assert dest in ix
            union(i,ix[dest])
    orbit_map={}
    for t in tt:
        root=find(ix[t]); orbit_map.setdefault(root,[]).append(t)
    assert len(orbit_map)==exp_orbits,(m,eps,r,'actual',len(orbit_map),'expected',exp_orbits)
    assert len({invariant(members[0],m,eps) for members in orbit_map.values()})==exp_orbits
    for members in orbit_map.values():
        assert len({invariant(x,m,eps) for x in members})==1
    print('PASS',m,eps,r,'homs',len(tt),'automorphism_orbits',len(orbit_map),'isometries',len(O))

if __name__=='__main__':
    for m in (1,2):
        for eps in ('+','-'):
            for r in (1,2,3):check(m,eps,r)
    print('VERIFY_OK')
