from itertools import product, combinations
from math import prod, factorial


def invmod(a,p): return pow(a,-1,p)

def rref(rows,p,d):
    A=[list(r) for r in rows if any(x%p for x in r)]
    if not A: return ()
    i=0
    for j in range(d):
        piv=None
        for k in range(i,len(A)):
            if A[k][j]%p:
                piv=k; break
        if piv is None: continue
        A[i],A[piv]=A[piv],A[i]
        z=invmod(A[i][j]%p,p)
        A[i]=[(x*z)%p for x in A[i]]
        for k in range(len(A)):
            if k!=i and A[k][j]%p:
                c=A[k][j]%p
                A[k]=[(A[k][t]-c*A[i][t])%p for t in range(d)]
        i+=1
        if i==len(A): break
    A=[tuple(row) for row in A if any(row)]
    A.sort(key=lambda row: next(i for i,x in enumerate(row) if x))
    return tuple(A)

def span_add(S,v,p,d): return rref(list(S)+[v],p,d)
def rank_union(S,T,p,d): return len(rref(list(S)+list(T),p,d))

def all_subspaces(p,d):
    zero=()
    seen={zero}; frontier=[zero]
    vecs=[v for v in product(range(p), repeat=d) if any(v)]
    while frontier:
        S=frontier.pop()
        for v in vecs:
            T=span_add(S,v,p,d)
            if T not in seen:
                seen.add(T); frontier.append(T)
    return sorted(seen,key=lambda S:(len(S),S))

def hyperplanes(V,d): return [S for S in V if len(S)==d-1]
def intersection_dim(subs,p,d):
    # annihilator normals would be easier; brute intersection vector set for small tests
    allv=list(product(range(p), repeat=d))
    sets=[]
    for S in subs:
        vals={tuple([0]*d)}
        for coeff in product(range(p), repeat=len(S)):
            x=tuple(sum(coeff[i]*S[i][j] for i in range(len(S)))%p for j in range(d))
            vals.add(x)
        sets.append(vals)
    inter=set.intersection(*sets)
    # size = p^dim
    n=len(inter); dim=0
    while n>1: assert n%p==0; n//=p; dim+=1
    return dim

def graph(p,d):
    allS=all_subspaces(p,d)
    V=[S for S in allS if 0<len(S)<d]
    N=[set() for _ in V]
    for i,j in combinations(range(len(V)),2):
        if rank_union(V[i],V[j],p,d)==d:
            N[i].add(j); N[j].add(i)
    return V,N

def is_total(C,N):
    C=set(C)
    return all(N[v]&C for v in range(len(N)))

def perfect_matching(C,N):
    C=frozenset(C)
    memo={}
    def f(S):
        if not S: return True
        if len(S)%2: return False
        if S in memo: return memo[S]
        v=next(iter(S)); T=S-{v}
        ans=any(u in N[v] and f(T-{u}) for u in T)
        memo[S]=ans; return ans
    return f(C)

def is_paired(C,N):
    C=set(C)
    return all(v in C or N[v]&C for v in range(len(N))) and perfect_matching(C,N)

def gl_order(p,d):
    return prod(p**d-p**i for i in range(d))

def check(p,d, exhaustive_total=True, exhaustive_paired=True):
    V,N=graph(p,d); n=len(V)
    Hidx=[i for i,S in enumerate(V) if len(S)==d-1]
    expected_count=gl_order(p,d)//((p-1)**d*factorial(d))
    tsets=[]
    if exhaustive_total:
        for C in combinations(range(n),d):
            if is_total(C,N): tsets.append(C)
        assert len(tsets)==expected_count,(p,d,len(tsets),expected_count)
        for C in tsets:
            assert all(i in Hidx for i in C)
            assert intersection_dim([V[i] for i in C],p,d)==0
        # every independent-normal equivalent set tested by count+intersection
        qualifying=0
        for C in combinations(Hidx,d):
            if intersection_dim([V[i] for i in C],p,d)==0: qualifying+=1
        assert qualifying==expected_count==len(tsets)
    gp=d if d%2==0 else d+1
    # prove lower size experimentally where feasible
    for k in range(1,min(gp,n+1)):
        if k%2==0:
            assert not any(is_paired(C,N) for C in combinations(range(n),k)), (p,d,k)
    # exhibit expected paired set of hyperplanes
    C=list(tsets[0]) if tsets else None
    if C is None:
        for cand in combinations(Hidx,d):
            if intersection_dim([V[i] for i in cand],p,d)==0:
                C=list(cand); break
    if d%2:
        extra=next(i for i in Hidx if i not in C)
        C=C+[extra]
    assert len(C)==gp and is_paired(C,N)
    if exhaustive_paired:
        first=None
        for k in range(2,n+1,2):
            arr=[C for C in combinations(range(n),k) if is_paired(C,N)]
            if arr:
                first=(k,len(arr)); break
        assert first and first[0]==gp,(p,d,first,gp)
    print(f'p={p} d={d} vertices={n} hyperplanes={len(Hidx)} gamma_t={d} min_total_count={expected_count} gamma_pr={gp}')

for p,d,et,ep in [(2,2,True,True),(3,2,True,True),(5,2,True,True),(2,3,True,True),(3,3,True,True),(2,4,True,False)]:
    check(p,d,et,ep)
print('VERIFY_OK')
