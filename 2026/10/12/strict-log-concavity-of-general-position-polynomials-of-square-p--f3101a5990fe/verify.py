from collections import Counter, deque
from itertools import combinations
from math import comb

def book_graph(r):
    # spine x=0, y=1; page i has a_i=2+2i, b_i=3+2i
    n = 2 + 2*r
    adj = [set() for _ in range(n)]
    adj[0].add(1); adj[1].add(0)
    for i in range(r):
        a = 2 + 2*i
        b = a + 1
        for u,v in ((0,a),(a,b),(b,1)):
            adj[u].add(v); adj[v].add(u)
    return adj

def all_distances(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj)
        d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return D

def is_general_position(D, mask):
    S=[v for v in range(len(D)) if (mask>>v)&1]
    for u,v in combinations(S,2):
        for z in S:
            if z!=u and z!=v and D[u][z]+D[z][v]==D[u][v]:
                return False
    return True

def is_independent(adj, mask):
    for u in range(len(adj)):
        if (mask>>u)&1:
            for v in adj[u]:
                if u < v and (mask>>v)&1:
                    return False
    return True

def formula_coeffs(r):
    a=[0]*(r+2)
    a[0]=1
    a[1]=2*r+2
    a[2]=comb(2*r+2,2)
    for k in range(3,r+2):
        a[k]=(2**k)*(comb(r,k) if k<=r else 0)+2*comb(r,k-1)
    return a

subset_trials=0
classification_checks=0
logconcavity_checks=0

for r in range(2,9):
    adj=book_graph(r)
    D=all_distances(adj)
    n=len(adj)
    counts=Counter()
    maxima=[]

    for mask in range(1<<n):
        subset_trials += 1
        gp=is_general_position(D,mask)
        k=mask.bit_count()
        if gp:
            counts[k]+=1
            if k>=3:
                assert is_independent(adj,mask), (r,mask)
                classification_checks += 1

    expected=formula_coeffs(r)
    actual=[counts[k] for k in range(r+2)]
    assert actual==expected, (r,actual,expected)

    maxk=max(counts)
    assert maxk==r+1
    maxsets=[]
    for mask in range(1<<n):
        if mask.bit_count()==maxk and is_general_position(D,mask):
            maxsets.append(mask)
    assert len(maxsets)==2

    for k in range(1,len(expected)-1):
        assert expected[k]*expected[k] > expected[k-1]*expected[k+1], (r,k,expected)
        logconcavity_checks += 1

print("VERIFY_OK")
print("book_parameters_checked =", 7)
print("parameters r = 2..8")
print("vertex_subsets_checked =", subset_trials)
print("size_at_least_3_gp_sets_checked_independent =", classification_checks)
print("strict_logconcavity_inequalities_checked =", logconcavity_checks)
print("all polynomial coefficients matched the closed formula")
print("all general-position sets of size at least 3 were independent")
print("all general-position numbers matched r+1")
print("all maximum-set counts equaled 2")
print("all coefficient sequences were strictly log-concave")
