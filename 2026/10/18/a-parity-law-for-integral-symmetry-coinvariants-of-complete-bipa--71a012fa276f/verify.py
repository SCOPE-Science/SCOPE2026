#!/usr/bin/env python3
"""Self-contained finite checks of oriented-face coinvariant presentations.
No outside files or third-party packages are required.
"""
from itertools import combinations


def predicted(m,n,r):
    k=r+1
    lo=max(1,k-n); hi=min(k-1,m)
    if lo>hi: return 0
    if r%2:
        return 1 if m+n==k else sum(a%2 for a in range(lo,hi+1))
    return (sum(any(lo<=a<=hi for a in (e,e+1)) for e in range(0,k,2))
            -int(n>=k)-int(m>=k))


def rank_mod_two(columns):
    pivots={}
    for column in columns:
        while column:
            p=column.bit_length()-1
            if p not in pivots:
                pivots[p]=column
                break
            column^=pivots[p]
    return len(pivots)


def from_original_chains(m,n,r):
    """Full oriented-simplex presentation, not the color-count reduction."""
    N=m+n;k=r+1
    faces=list(combinations(range(N),k))
    ix={face:i for i,face in enumerate(faces)}
    relations=[]
    for face in faces:
        if face[-1]<m or face[0]>=m:
            relations.append(1<<ix[face])
    for face in combinations(range(N),k+1):
        col=0
        for j in range(k+1):
            col ^=1<<ix[face[:j]+face[j+1:]]
        relations.append(col)
    for v in list(range(m-1))+list(range(m,N-1)):
        perm=list(range(N));perm[v],perm[v+1]=perm[v+1],perm[v]
        for face in faces:
            image=tuple(sorted(perm[x] for x in face))
            relations.append((1<<ix[face])^(1<<ix[image]))
    return len(faces)-rank_mod_two(relations)


def from_color_orbits(m,n,r):
    k=r+1
    lo=max(1,k-n);hi=min(k-1,m)
    colors=list(range(lo,hi+1));ix={a:i for i,a in enumerate(colors)}
    relations=[]
    for a in range(max(0,k+1-n),min(k+1,m)+1):
        b=k+1-a
        col=0
        if a%2 and a-1 in ix:col^=1<<ix[a-1]
        if b%2 and a in ix:col^=1<<ix[a]
        relations.append(col)
    return len(colors)-rank_mod_two(relations)


def main():
    samples=0
    for m in range(2,6):
        for n in range(2,6):
            for r in range(2,min(m+n,7)):
                a=from_original_chains(m,n,r)
                b=from_color_orbits(m,n,r)
                c=predicted(m,n,r)
                assert a==b==c,(m,n,r,a,b,c)
                samples+=1
    print('PASS full oriented-chain mod-2 rank = orbit relation rank = formula')
    print('verified_parameter_triples:',samples)
    print('critical_examples:')
    for m,n,r in [(2,2,2),(3,3,2),(3,3,3),(4,4,4),
                  (5,5,5),(2,4,5),(5,5,6)]:
        if r>=m+n:continue
        print(f'  (m,n,r)=({m},{n},{r}): (Z/2)^{predicted(m,n,r)}')
    for m in range(2,36):
        for n in range(2,36):
            for r in range(2,m+n):
                assert from_color_orbits(m,n,r)==predicted(m,n,r)
    print('PASS orbit formula for all 2<=m,n<=35 and 2<=r<m+n')
    print('Integer exponent-two assertion is proven via a same-color transposition;')
    print('finite mod-2 ranks alone do not establish that assertion.')

if __name__=='__main__':main()
