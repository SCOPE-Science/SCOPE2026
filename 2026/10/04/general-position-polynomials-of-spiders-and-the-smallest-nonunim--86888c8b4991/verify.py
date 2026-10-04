import math
from collections import deque

def partitions(n,k,lo=1):
    if k==1:
        if n>=lo: yield (n,)
        return
    for x in range(lo,n//k+1):
        for rest in partitions(n-x,k-1,x):
            yield (x,)+rest

def all_spiders(max_order):
    for order in range(4,max_order+1):
        L=order-1
        for k in range(3,L+1):
            for p in partitions(L,k):
                yield p

def spider_graph(lengths):
    edges=[]; nxt=1
    for L in lengths:
        prev=0
        for _ in range(L):
            cur=nxt; nxt+=1
            edges.append((prev,cur)); prev=cur
    return nxt,edges

def distances(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    D=[]
    for s in range(n):
        d=[-1]*n; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D

def is_gp(mask,D):
    V=[i for i in range(len(D)) if mask>>i & 1]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            u,v=V[i],V[j]
            for h in range(len(V)):
                if h==i or h==j: continue
                w=V[h]
                if D[u][v]==D[u][w]+D[w][v]:
                    return False
    return True

def formula(lengths):
    L=sum(lengths); n=L+1; k=len(lengths)
    e=[0]*(k+1); e[0]=1
    for a in lengths:
        for j in range(k,0,-1): e[j]+=a*e[j-1]
    coeff=[0]*(k+1)
    coeff[0]=1; coeff[1]=n; coeff[2]=math.comb(n,2)
    for j in range(3,k+1): coeff[j]=e[j]
    return coeff

def unimodal(a):
    i=0
    while i+1<len(a) and a[i]<=a[i+1]: i+=1
    while i+1<len(a) and a[i]>=a[i+1]: i+=1
    return i==len(a)-1

direct_types=direct_subsets=0
for lengths in all_spiders(11):
    n,edges=spider_graph(lengths); D=distances(n,edges)
    actual=[0]*(len(lengths)+1)
    for mask in range(1<<n):
        direct_subsets+=1
        if is_gp(mask,D):
            s=mask.bit_count()
            if s>=len(actual):
                raise AssertionError((lengths,s))
            actual[s]+=1
    assert actual==formula(lengths),(lengths,actual,formula(lengths))
    direct_types+=1

cutoff_types=0; bad=[]
for lengths in all_spiders(22):
    cutoff_types+=1
    c=formula(lengths)
    if not unimodal(c): bad.append((lengths,c))
assert bad==[((1,1,1,1,2,15),[1,22,231,226,249,137,30])],bad

# Infinite family exact inequalities.
for m in range(1,101):
    c=formula((1,1,1,1,2,m))
    expected=[1,m+7,math.comb(m+7,2),14*m+16,16*m+9,9*m+2,2*m]
    assert c==expected
    assert (not unimodal(c))==(m>=15), (m,c)

print('VERIFY_OK')
print('direct_spider_types_checked =',direct_types)
print('direct_vertex_subsets_checked =',direct_subsets)
print('formula_cutoff_spider_types_checked =',cutoff_types)
print('orders_direct = 4..11')
print('orders_cutoff = 4..22')
print('unique_nonunimodal_spider_through_order_22 = S(1,1,1,1,2,15)')
print('unique_order_22_coefficients = 1,22,231,226,249,137,30')
print('family_S(1,1,1,1,2,m)_nonunimodal_iff_m_ge_15_checked_for_m_1..100')
