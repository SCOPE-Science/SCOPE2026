"""Finite verification of rank-four profiles of symplectic generalized-quadrangle incidence graphs. Standard library only."""
from itertools import product
from collections import Counter
from math import gcd


def symplectic_incidence(q):
    def normalize(v):
        first=next(x for x in v if x%q)
        inv=pow(first,-1,q)
        return tuple(x*inv%q for x in v)
    pts=sorted({normalize(v) for v in product(range(q),repeat=4) if any(v)})
    ix={v:i for i,v in enumerate(pts)}
    def form(a,b):
        return (a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2])%q
    lines=set()
    for i,x in enumerate(pts):
        for y in pts[i+1:]:
            if form(x,y): continue
            lines.add(frozenset(ix[normalize(tuple((r*x[h]+s*y[h])%q for h in range(4)))]
                                for r,s in product(range(q),repeat=2) if r or s))
    lines=sorted(lines,key=lambda z:tuple(sorted(z)))
    n=len(pts)
    assert len(lines)==n==(q+1)*(q*q+1)
    N=2*n
    adj=[0]*N
    for j,line in enumerate(lines):
        assert len(line)==q+1
        for i in line:
            adj[i]|=1<<(n+j)
            adj[n+j]|=1<<i
    assert all(a.bit_count()==q+1 for a in adj)
    return adj


def distances(adj):
    n=len(adj); out=[]
    for i in range(n):
        d=[-1]*n; d[i]=0; q=[i]
        for a in q:
            for b in range(n):
                if d[b]<0 and adj[a]>>b&1:
                    d[b]=d[a]+1;q.append(b)
        assert max(d)==4 and min(d)==0
        out.append(d)
    return out


def first_order_profiles(adj, ds):
    n=len(adj);allbits=(1<<n)-1
    return_type={}; triple_types=[0]*(n**3)
    clip_types={}; observed_by_pair_distance={d:set() for d in range(5)}
    for a in range(n):
        aa=adj[a];bit_a=1<<a
        for b in range(n):
            bb=adj[b];bit_b=1<<b
            atomic_ab=2 if a==b else int((aa>>b)&1)
            for c in range(n):
                cc=adj[c];bit_c=1<<c
                atom=atomic_ab +3*(2 if a==c else int((aa>>c)&1))\
                                   +9*(2 if b==c else int((bb>>c)&1))
                fresh=allbits^(bit_a|bit_b|bit_c)
                extmask=0
                for pattern in range(8):
                    rem=fresh
                    rem&=aa if pattern&1 else allbits^aa
                    rem&=bb if pattern&2 else allbits^bb
                    rem&=cc if pattern&4 else allbits^cc
                    if rem:extmask|=1<<pattern
                typ=(atom,extmask)
                triple_types[(a*n+b)*n+c]=typ
                d=(min(3,ds[a][b]),min(3,ds[a][c]),min(3,ds[b][c]))
                clip_types.setdefault(d,set()).add(typ)
                observed_by_pair_distance[ds[a][b]].add(d[1:])
    assert len(clip_types)==30
    assert all(len(types)==1 for types in clip_types.values())
    # For the converse, every rank-one triple signature here determines its clipped distance triple.
    inv={}
    for d, types in clip_types.items():
        tt=next(iter(types));inv.setdefault(tt,set()).add(d)
    assert len(inv)==30 and all(len(t)==1 for t in inv.values())
    pair_types=[]
    by_dist={d:set() for d in range(5)}
    for a in range(n):
        for b in range(n):
            full=frozenset(triple_types[(a*n+b)*n+c] for c in range(n))
            # Equality/adjacency is included separately.
            atomic=2 if a==b else int((adj[a]>>b)&1)
            typ=(atomic,full)
            by_dist[ds[a][b]].add(typ)
            pair_types.append(typ)
    assert all(len(by_dist[d])==1 for d in range(5))
    representatives=[next(iter(by_dist[d])) for d in range(5)]
    assert len(set(representatives))==5
    vertex_profiles=[]
    for a in range(n):
        vertex_profiles.append(frozenset(pair_types[a*n+b] for b in range(n)))
    assert len(set(vertex_profiles))==1
    return (frozenset(vertex_profiles),{d:sorted(observed_by_pair_distance[d]) for d in range(5)},clip_types)


def intersection_support(q):
    # Distance matrices as a commutative algebra. All matrices below are 5 by 5.
    n=5
    def matmul(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    I=[[int(i==j) for j in range(n)] for i in range(n)]
    L=[[0]*n for _ in range(n)]
    for i,j,x in [(1,0,1),(0,1,q+1),(2,1,1),(1,2,q),(3,2,1),
                  (2,3,q),(4,3,q+1),(3,4,q)]:L[i][j]=x
    def sub(A,B,coef=1):return [[A[i][j]-coef*B[i][j] for j in range(n)] for i in range(n)]
    L2=matmul(L,L)
    L3=matmul(L2,L)
    L4=matmul(L3,L)
    D2=sub(L2,I,q+1)
    D3=sub(L3,L,2*q+1)
    nom=sub(sub(L4,L2,3*q+1),I,-q*(q+1))
    assert all(x%(q+1)==0 for row in nom for x in row)
    D4=[[x//(q+1) for x in row] for row in nom]
    Ds=[I,L,D2,D3,D4]
    assert all([A[i][0] for i in range(n)]==[int(i==j) for i in range(n)] for j,A in enumerate(Ds))
    return {d:sorted({(min(a,3),min(b,3)) for a in range(5) for b in range(5)
                      if matmul(Ds[a],Ds[b])[d][0] > 0}) for d in range(5)}


def main():
    theory=None; supports=None
    for q in (2,3):
        adj=symplectic_incidence(q)
        ds=distances(adj)
        sig,local,clipped=first_order_profiles(adj,ds)
        p=intersection_support(q)
        assert local==p
        if theory is None: theory=sig; supports=local
        else:assert sig==theory and local==supports
        print(f'q={q}, vertices={len(adj)}, distance pair signatures=5, rank-one triple signatures={len(clipped)}, rank-four theory matches')
    print('Pair-distance extension supports (distances truncated at 3):')
    for d,values in supports.items():print('distance',d,':',values)
    print('ALL CHECKS PASSED')


if __name__=='__main__':main()
