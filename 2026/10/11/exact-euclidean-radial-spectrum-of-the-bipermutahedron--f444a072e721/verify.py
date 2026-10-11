#!/usr/bin/env python3
from itertools import combinations, permutations
from math import factorial


def dyck_patterns(n):
    out=[]
    def rec(pref,u,b):
        if u==n and b==n:
            out.append(pref)
            return
        if u<n:
            rec(pref+'U',u+1,b)
        if b<u:
            rec(pref+'B',u,b+1)
    rec('',0,0)
    return out


def area(word):
    us=[i+1 for i,c in enumerate(word) if c=='U']
    return sum(u-(j+1) for j,u in enumerate(us))


def S2(n):
    return 2*n*(4*n*n-1)//3


def norm2_from_A(n,A):
    s=2*A-n*n
    return S2(n)+2*s*s+4*s


def R2(n):
    return 2*n*(n-1)*(3*n*n+7*n+1)//3

# All Dyck area levels and exact radial formula through n=8.
for n in range(2,9):
    pats=dyck_patterns(n)
    vals=sorted({area(w) for w in pats})
    N=n*(n-1)//2
    assert vals==list(range(N+1))
    radii=[norm2_from_A(n,A) for A in vals]
    assert len(set(radii))==N+1
    assert radii[0]==R2(n)
    assert all(radii[i]>radii[i+1] for i in range(len(radii)-1))

# Brute-force labeled expanded words.  A bipermutation is encoded by choosing
# the singleton k, a permutation of the multiset with k once and others twice,
# then expanding k to k,bar(k).  We deduplicate multiset permutations.
def multiset_perms(items):
    items=sorted(items)
    used=[False]*len(items)
    cur=[]
    def rec():
        if len(cur)==len(items):
            yield tuple(cur); return
        last=None
        for i,x in enumerate(items):
            if used[i] or x==last: continue
            last=x; used[i]=True; cur.append(x)
            yield from rec()
            cur.pop(); used[i]=False
    yield from rec()

for n in range(2,5):
    actual=[]
    outer=0
    for k in range(n):
        base=[]
        for i in range(n):
            base += [i] if i==k else [i,i]
        for B in multiset_perms(base):
            seen={i:0 for i in range(n)}
            expanded=[]
            for z in B:
                if z==k:
                    expanded.append((z,0)); expanded.append((z,1))
                else:
                    expanded.append((z,seen[z])); seen[z]+=1
            vals=list(range(-(2*n-1),2*n,2))
            pi={expanded[j]:vals[j] for j in range(2*n)}
            x=[pi[(i,0)] for i in range(n)]
            y=[-pi[(i,1)] for i in range(n)]
            s=sum(x)
            assert s==sum(y)
            x[k]-=s; y[k]-=s
            q=sum(t*t for t in x+y)
            word=''.join('U' if second==0 else 'B' for _,second in expanded)
            A=area(word)
            assert q==norm2_from_A(n,A)
            actual.append(q)
            if q==R2(n): outer+=1
    assert sorted(set(actual))==sorted(norm2_from_A(n,A) for A in range(n*(n-1)//2+1))
    assert outer==n*factorial(n-1)**2

print('VERIFY_OK bipermutahedron radial_spectrum dyck_n=2..8 labeled_n=2..4')
