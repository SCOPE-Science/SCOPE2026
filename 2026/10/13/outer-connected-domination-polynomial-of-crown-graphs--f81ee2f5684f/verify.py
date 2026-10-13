from itertools import combinations
from math import comb


def crown_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def dominates(S,adj):
    S=set(S)
    return all(v in S or any(u in S for u in adj[v]) for v in range(len(adj)))


def connected(T,adj):
    T=set(T)
    if not T:
        return False
    seen={next(iter(T))}
    stack=list(seen)
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w in T and w not in seen:
                seen.add(w)
                stack.append(w)
    return seen==T


def is_ocd(S,adj):
    S=set(S)
    if not dominates(S,adj):
        return False
    if len(S)==len(adj):
        return True
    return connected(set(range(len(adj)))-S,adj)


def formula(n):
    F=[comb(n,k) for k in range(n+1)]
    F[0]-=1
    F[1]-=n
    C=[0]*(2*n+1)
    for i,a in enumerate(F):
        for j,b in enumerate(F):
            C[i+j]+=a*b
    # Dominating sets with one selected vertex on one side and its mate selected
    for j in range(n):
        C[2+j]+=2*n*comb(n-1,j)
    C[2]-=n
    # Whole bipartition sides
    C[n]+=2
    # Remove dominating sets whose complement lies in one side with size >=2
    for a in range(n-1):
        C[n+a]-=2*comb(n,a)
    # Remove matched-singleton disconnections in a mixed complement
    for b in range(1,n):
        C[n-1+b]-=2*n*comb(n-1,b)
    C[2*n-2]+=n  # intersection of the two previous oriented mixed classes
    # Remove complements consisting of two deleted-matching pairs
    C[2*n-4]-=comb(n,2)
    return C


def classify_domination(n,S):
    I={i for i in range(n) if i in S}
    J={i for i in range(n) if n+i in S}
    a,b=len(I),len(J)
    if a==n and b==0: return True
    if b==n and a==0: return True
    if a>=2 and b>=2: return True
    if a==1 and b>=1:
        return next(iter(I)) in J
    if b==1 and a>=1:
        return next(iter(J)) in I
    return False


def complement_connected_type(n,S):
    I={i for i in range(n) if i not in S}
    J={i for i in range(n) if n+i not in S}
    p,q=len(I),len(J)
    if p+q==0:
        return 'empty'
    if p+q==1:
        return 'connected'
    if p==0 or q==0:
        return 'one_side_disconnected'
    c=len(I&J)
    if min(p,q)==1 and c==1:
        return 'matched_singleton_disconnected'
    if p==q==c==2:
        return 'two_matching_pairs_disconnected'
    return 'connected'


def main():
    subset_checks=0
    coefficient_checks=0
    structural_checks=0
    minimum_checks=0
    for n in range(3,9):
        adj=crown_adj(n)
        brute=[0]*(2*n+1)
        mins=[]
        for mask in range(1<<(2*n)):
            S={v for v in range(2*n) if (mask>>v)&1}
            subset_checks+=1
            d1=dominates(S,adj)
            d2=classify_domination(n,S)
            if d1!=d2:
                raise AssertionError(('domination classification',n,S,d1,d2))
            structural_checks+=1
            if len(S)<2*n:
                t=connected(set(range(2*n))-S,adj)
                typ=complement_connected_type(n,S)
                if t!=(typ=='connected'):
                    raise AssertionError(('connectivity classification',n,S,t,typ))
                structural_checks+=1
            if is_ocd(S,adj):
                brute[len(S)]+=1
        form=formula(n)
        if brute!=form:
            raise AssertionError(('coefficients',n,brute,form))
        coefficient_checks += len(brute)
        positive=[k for k,c in enumerate(brute) if c]
        gamma=min(positive)
        if n==3:
            if gamma!=4 or brute[4]!=6:
                raise AssertionError(('minimum n=3',brute))
        else:
            if gamma!=2 or brute[2]!=n:
                raise AssertionError(('minimum n>=4',n,brute[2]))
        minimum_checks+=1
        total=sum(brute)
        expected=(2**n-n-1)**2-2**(n+1)+4*n+4-comb(n,2)
        if total!=expected:
            raise AssertionError(('total',n,total,expected))
    print(f'VERIFY_OK n_range=3..8 subset_checks={subset_checks} structural_checks={structural_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=16')

if __name__=='__main__':
    main()
