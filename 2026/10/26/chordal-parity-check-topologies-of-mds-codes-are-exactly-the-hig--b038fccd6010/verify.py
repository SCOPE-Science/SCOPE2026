#!/usr/bin/env python3
"""Independent finite-field checks of the MDS chordal primal-graph theorem."""
from itertools import combinations,product
from random import Random
from math import comb

def rank(A,p):
    M=[list(map(lambda x:x%p,row)) for row in A]
    if not M:return 0
    m=len(M);n=len(M[0]);r=0
    for c in range(n):
        i=next((j for j in range(r,m) if M[j][c]),None)
        if i is None:continue
        M[r],M[i]=M[i],M[r]
        inv=pow(M[r][c],-1,p)
        M[r]=[(z*inv)%p for z in M[r]]
        for j in range(m):
            if j!=r and M[j][c]:
                t=M[j][c];M[j]=[(a-t*b)%p for a,b in zip(M[j],M[r])]
        r+=1
        if r==m:break
    return r

def kernel(A,p):
    M=[list(map(lambda x:x%p,row)) for row in A]
    m=len(M);n=len(M[0]);r=0;pivs=[]
    for c in range(n):
        i=next((j for j in range(r,m) if M[j][c]),None)
        if i is None:continue
        M[r],M[i]=M[i],M[r]
        inv=pow(M[r][c],-1,p);M[r]=[z*inv%p for z in M[r]]
        for j in range(m):
            if j!=r and M[j][c]:
                t=M[j][c];M[j]=[(a-t*b)%p for a,b in zip(M[j],M[r])]
        pivs.append(c);r+=1
        if r==m:break
    out=[]
    for c in range(n):
        if c in pivs:continue
        x=[0]*n;x[c]=1
        for i,d in enumerate(pivs):x[d]=(-M[i][c])%p
        out.append(x)
    return out

def primal(H):
    n=len(H[0]);E=set()
    for row in H:
        inds=[i for i,v in enumerate(row) if v]
        E.update(combinations(inds,2))
    return E

def connected(n,E,deleted):
    left=set(range(n))-set(deleted)
    if len(left)<2:return True
    seen={next(iter(left))}
    while True:
        new=seen|{b for a,b in E if a in seen and b in left}|{a for a,b in E if b in seen and a in left}
        if new==seen:break
        seen=new
    return seen==left

def k_connected(n,E,k):
    return all(connected(n,E,S) for s in range(k) for S in combinations(range(n),s))

def random_k_tree(n,k,rng):
    cliques=[tuple(range(k+1))]
    edges=set(combinations(range(k+1),2))
    for v in range(k+1,n):
        kcliques=set()
        for C in cliques:
            kcliques.update(combinations(C,k))
        K=rng.choice(sorted(kcliques))
        cliques.append(tuple(sorted((*K,v))))
        edges.update((min(u,v),max(u,v)) for u in K)
    return cliques,edges

def vandermonde(n,k,p):
    return [[pow(x,j,p) for x in range(n)] for j in range(k)]

def check_tree(n,k,p,seed):
    G=vandermonde(n,k,p)
    assert all(rank([[row[i] for i in S] for row in G],p)==k for S in combinations(range(n),k))
    cliques,E=random_k_tree(n,k,Random(seed))
    H=[]
    for S in cliques:
        u=kernel([[row[i] for i in S] for row in G],p)
        assert len(u)==1 and all(u[0]),('MDS support',S,u)
        v=[0]*n
        for j,x in zip(S,u[0]):v[j]=x
        H.append(v)
    assert rank(H,p)==n-k
    assert all(sum(a*b for a,b in zip(h,g))%p==0 for h in H for g in G)
    assert primal(H)==E
    assert len(E)==k*n-comb(k+1,2)
    assert k_connected(n,E,k)

def check_basis_sample(n,k,p,seed):
    rng=Random(seed);G=vandermonde(n,k,p);D=kernel(G,p)
    assert len(D)==n-k
    for _ in range(100):
        M=[[rng.randrange(p) for j in range(n-k)] for i in range(n-k)]
        if rank(M,p)<n-k:continue
        H=[[sum(a*b for a,b in zip(row,col))%p for col in zip(*D)] for row in M]
        assert rank(H,p)==n-k
        E=primal(H)
        assert k_connected(n,E,k)
        # If chordal, the lower edge bound follows (checked for small examples).
        if n<=7 and is_chordal(n,E):
            assert len(E)>=k*n-comb(k+1,2)

def is_chordal(n,E):
    adj=[set() for _ in range(n)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    # Independent definition: no chordless induced cycle length at least four.
    for size in range(4,n+1):
        for S in combinations(range(n),size):
            for order in __import__('itertools').permutations(S[1:]):
                c=(S[0],)+order
                if c[1]>c[-1]:continue
                if all(c[(i+1)%size] in adj[c[i]] for i in range(size)):
                    if all(c[j] not in adj[c[i]] for i in range(size) for j in range(i+2,size) if not (i==0 and j==size-1)):
                        return False
    return True

def exhaustive_small(n,k,p):
    G=vandermonde(n,k,p);D=kernel(G,p);r=n-k
    if r!=2:return 0
    seen=set();count=0
    for tup in product(range(p),repeat=2*r):
        M=[list(tup[i*r:(i+1)*r]) for i in range(r)]
        if rank(M,p)<r:continue
        H=[[sum(a*b for a,b in zip(row,col))%p for col in zip(*D)] for row in M]
        E=primal(H)
        assert k_connected(n,E,k)
        assert is_chordal(n,E)
        assert len(E)>=k*n-comb(k+1,2)
        seen.add(tuple(sorted(E)));count+=1
    return count,len(seen)

if __name__=='__main__':
    total=0
    for n,k,p in [(3,1,5),(4,2,5),(5,2,7),(6,2,7),(6,3,7),(7,4,11),(8,5,11),(8,2,11),(9,3,11)]:
        for seed in range(20):check_tree(n,k,p,seed);total+=1
        for seed in range(4):check_basis_sample(n,k,p,seed)
    c,graphs=exhaustive_small(4,2,5)
    print('TREE_WITNESS_TESTS',total)
    print('FULL_RANK_BASIS_EXHAUSTIVE',c,'DISTINCT_PRIMAL_GRAPHS',graphs)
    print('RANDOM_BASIS_ATTEMPTS',9*4*100,'(including singular matrices skipped)')
    print('VERIFY_OK')

def is_chordal_fast(n,E):
    adj=[set() for _ in range(n)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    left=set(range(n))
    while left:
        v=next((v for v in left if all((a==b or b in adj[a]) for a in adj[v]&left for b in adj[v]&left)),None)
        if v is None:return False
        left.remove(v)
    return True

def all_graphs_test(n,k,p):
    G=vandermonde(n,k,p)
    poss=list(combinations(range(n),2))
    got=0
    for mask in range(1<<len(poss)):
        E={e for i,e in enumerate(poss) if mask>>i&1}
        if len(E)<k*n-comb(k+1,2):continue
        if not k_connected(n,E,k) or not is_chordal_fast(n,E):continue
        H=[]
        for S in combinations(range(n),k+1):
            if all(e in E for e in combinations(S,2)):
                K=kernel([[r[i] for i in S] for r in G],p)
                assert len(K)==1 and all(K[0])
                vec=[0]*n
                for i,a in zip(S,K[0]):vec[i]=a
                H.append(vec)
        assert rank(H,p)==n-k,('not spanning',n,k,E)
        assert primal(H)==E,('not exact',n,k,E)
        got+=1
    return got

if __name__=='__main__':
    for n,k,p in [(4,1,7),(4,2,7),(4,3,7),(5,1,7),(5,2,7),(5,3,7),(5,4,7),(6,1,7),(6,2,7),(6,3,7),(6,4,7),(6,5,7)]:
        total=all_graphs_test(n,k,p)
        print('ALL_CHORDAL_GRAPH_CASES',n,k,total)
    print('CHORDAL_REALIZATION_VERIFY_OK')
