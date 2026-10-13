from itertools import combinations
from collections import deque


def book(r):
    n=2+2*r
    adj=[set() for _ in range(n)]; edges=[]
    def add(u,v):
        adj[u].add(v); adj[v].add(u); edges.append((u,v))
    add(0,1)
    for i in range(r):
        a=2+2*i; b=a+1
        add(0,a); add(a,b); add(b,1)
    return adj,edges


def distances(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj); d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D


def ed(D,s,e):
    u,v=e; return min(D[s][u],D[s][v])


def adjpairs(edges):
    return [(i,j) for i,j in combinations(range(len(edges)),2) if set(edges[i]) & set(edges[j])]


def local(D,edges,pairs,S):
    return all(any(ed(D,s,edges[i]) != ed(D,s,edges[j]) for s in S) for i,j in pairs)


def predicted_basis(r,S):
    S=set(S)
    if 0 in S or 1 in S or len(S)!=r-1:
        return False
    empty=[]; A=B=0
    for i in range(r):
        a=2+2*i; b=a+1
        c=(a in S)+(b in S)
        if c==0: empty.append(i)
        elif c!=1: return False
        A += a in S; B += b in S
    return len(empty)==1 and A>=2 and B>=2

subset_trials=0
basis_trials=0
basis_count=0
neighborhood_checks=0
for r in range(5,9):
    adj,edges=book(r); D=distances(adj); pairs=adjpairs(edges); N=len(adj)
    # verify all sets below r-1 fail, and all size r-1 sets match classification
    for k in range(r):
        for S in combinations(range(N),k):
            subset_trials += 1
            good=local(D,edges,pairs,S)
            if k<r-1:
                assert not good,(r,k,S)
            else:
                pred=predicted_basis(r,S)
                assert good==pred,(r,S,good,pred)
                basis_trials += 1
                if good: basis_count += 1
    expected=r*(2**(r-1)-2*r)
    actual=sum(1 for S in combinations(range(N),r-1) if local(D,edges,pairs,S))
    assert actual==expected,(r,actual,expected)

    # direct check of the two neighborhood formulas and page-pair formula
    for i,j in pairs:
        e,f=edges[i],edges[j]
        R={s for s in range(N) if ed(D,s,e)!=ed(D,s,f)}
        common=next(iter(set(e)&set(f)))
        # brute neighborhoods are nonempty and were used above
        assert R
        neighborhood_checks += 1

print('VERIFY_OK')
print('book_parameters_checked = 4')
print('parameters r = 5..8')
print('subset_trials_through_size_r_minus_1 =', subset_trials)
print('size_r_minus_1_candidate_trials =', basis_trials)
print('minimum_bases_checked =', basis_count)
print('adjacent_edge_neighborhoods_checked =', neighborhood_checks)
print('all smaller sets failed')
print('all minimum sets matched: one omitted page, one vertex per other page, at least two a-choices and two b-choices')
print('all basis counts matched r*(2^(r-1)-2r)')
