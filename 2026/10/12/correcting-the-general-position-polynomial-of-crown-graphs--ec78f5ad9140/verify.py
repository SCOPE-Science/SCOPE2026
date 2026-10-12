from itertools import combinations
from math import comb
from collections import Counter, deque

def crown_graph(n):
    N=2*n; adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def all_dist(adj):
    N=len(adj); D=[]
    for s in range(N):
        d=[10**9]*N; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D

def gp(D, mask, dlim):
    S=[v for v in range(len(D)) if (mask>>v)&1]
    for tri in combinations(S,3):
        for z in tri:
            u,v=[x for x in tri if x!=z]
            if D[u][v] <= dlim and D[u][z]+D[z][v]==D[u][v]:
                return False
    return True

def ordinary_pred(n,mask):
    k=mask.bit_count()
    if k<=2: return True
    I=sum((mask>>i)&1 for i in range(n))
    J=k-I
    return I==0 or J==0

def gp2_pred(n,mask):
    I={i for i in range(n) if (mask>>i)&1}
    J={j for j in range(n) if (mask>>(n+j))&1}
    a,b=len(I),len(J)
    if a==0 or b==0: return True
    if (a,b)==(1,1): return True
    if (a,b)==(2,1): return J<=I
    if (a,b)==(1,2): return I<=J
    if (a,b)==(2,2): return I==J
    return False

def ordinary_coeffs(n):
    c=[0]*(2*n+1)
    for k in range(n+1): c[k]+=2*comb(n,k)
    c[0]-=1; c[2]+=n*n
    return c

def gp2_coeffs(n):
    c=ordinary_coeffs(n)
    c[3]+=2*n*(n-1)
    c[4]+=comb(n,2)
    return c

subset_trials=0
for n in range(3,10):
    D=all_dist(crown_graph(n)); co=Counter(); c2=Counter()
    for mask in range(1<<(2*n)):
        subset_trials+=1
        o=gp(D,mask,3)  # diameter is 3
        t=gp(D,mask,2)
        assert o==ordinary_pred(n,mask),(n,mask,'ordinary')
        assert t==gp2_pred(n,mask),(n,mask,'gp2')
        if o: co[mask.bit_count()]+=1
        if t: c2[mask.bit_count()]+=1
    assert [co[k] for k in range(2*n+1)]==ordinary_coeffs(n)
    assert [c2[k] for k in range(2*n+1)]==gp2_coeffs(n)
    # Published 2024 T*(n,2) formula equals gp2 coefficients, not ordinary coefficients.
    pub=ordinary_coeffs(n)
    pub[3]+=4*comb(n,2)
    pub[4]+=comb(n,2)
    assert pub==gp2_coeffs(n)
    assert pub!=ordinary_coeffs(n)
print('VERIFY_OK')
print('parameters n = 3..9')
print('vertex_subsets_checked =',subset_trials)
print('ordinary general-position classification and polynomial matched direct geodesic tests')
print('general-2-position classification and polynomial matched direct geodesic tests')
print('the published 2024 T*(n,2) coefficient formula matched the general-2-position polynomial exactly')
print('the published formula differed from the ordinary general-position polynomial for every checked n')
