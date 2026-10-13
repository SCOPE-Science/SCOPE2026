from itertools import combinations
from math import comb


def crown_adj(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj


def power_dominates(adj, S):
    N=len(adj)
    colored=set(S)
    for v in list(S):
        colored.update(adj[v])
    while True:
        add=set()
        for v in colored:
            white=adj[v]-colored
            if len(white)==1:
                add.update(white)
        if not add:
            break
        colored.update(add)
    return len(colored)==N


def theorem(n, S):
    A=sum(1 for v in S if v<n)
    B=len(S)-A
    return (A>0 and B>0) or (B==0 and A>=n-2) or (A==0 and B>=n-2)


def formula_coeff(n,k):
    # mixed nonempty on both sides
    mixed=sum(comb(n,a)*comb(n,k-a) for a in range(1,n+1) if 1 <= k-a <= n)
    side=2*comb(n,k) if n-2 <= k <= n else 0
    return mixed+side


def run():
    subset_checks=0; coefficient_checks=0; total_checks=0; minimum_checks=0
    for n in range(3,9):
        adj=crown_adj(n)
        counts=[0]*(2*n+1)
        for mask in range(1<<(2*n)):
            S={v for v in range(2*n) if mask>>v & 1}
            actual=power_dominates(adj,S)
            predicted=theorem(n,S)
            subset_checks+=1
            if actual!=predicted:
                raise AssertionError((n,sorted(S),actual,predicted))
            if actual: counts[len(S)]+=1
        for k in range(1,2*n+1):
            f=formula_coeff(n,k)
            coefficient_checks+=1
            if counts[k]!=f:
                raise AssertionError(('coeff',n,k,counts[k],f))
        total=sum(counts)
        expected_total=4**n-2**(n+1)+n*n+n+3
        total_checks+=1
        if total!=expected_total:
            raise AssertionError(('total',n,total,expected_total))
        gamma=next(k for k,c in enumerate(counts) if c)
        if n==3:
            expected_gamma, expected_min=1,6
        elif n==4:
            expected_gamma, expected_min=2,28
        else:
            expected_gamma, expected_min=2,n*n
        minimum_checks+=1
        if (gamma,counts[gamma])!=(expected_gamma,expected_min):
            raise AssertionError(('min',n,gamma,counts[gamma],expected_gamma,expected_min))
    print(f'VERIFY_OK n_range=3..8 subset_checks={subset_checks} coefficient_checks={coefficient_checks} total_checks={total_checks} minimum_checks={minimum_checks} max_order=16')

if __name__=='__main__':
    run()
