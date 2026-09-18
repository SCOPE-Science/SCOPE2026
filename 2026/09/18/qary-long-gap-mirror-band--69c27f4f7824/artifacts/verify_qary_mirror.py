from itertools import combinations, product
from math import ceil

def subspaces_rref(q,n,k):
    for piv in combinations(range(n),k):
        pset=set(piv)
        free=[]
        for i,p in enumerate(piv):
            for c in range(p+1,n):
                if c not in pset:
                    free.append((i,c))
        for vals in product(range(q), repeat=len(free)):
            G=[[0]*n for _ in range(k)]
            for i,p in enumerate(piv):
                G[i][p]=1
            for (i,c),v in zip(free,vals):
                G[i][c]=v
            yield G

def weight_distribution(G,q):
    k=len(G); n=len(G[0])
    A=[0]*(n+1)
    for coeff in product(range(q),repeat=k):
        w=0
        for j in range(n):
            x=0
            for i in range(k):
                x=(x+coeff[i]*G[i][j])%q
            w += (x!=0)
        A[w]+=1
    return A

def support(v):
    return {i for i,x in enumerate(v) if x}

def scalar_multiple(x,y,q):
    # x = lambda y for some nonzero lambda
    sy=support(y)
    if support(x)!=sy or not sy:
        return False
    i=next(iter(sy))
    lam=x[i]*pow(y[i],-1,q)%q
    return lam!=0 and all(x[j]%q==(lam*y[j])%q for j in range(len(x)))

def verify_cancellation_lemma(q=3,nmax=6):
    checked=0
    for n in range(1,nmax+1):
        vecs=[v for v in product(range(q),repeat=n) if any(v)]
        for c in vecs:
            sc=support(c)
            for u in vecs:
                su=support(u)
                if not su < sc or scalar_multiple(c,u,q):
                    continue
                d=len(su)
                best=0
                for lam in range(1,q):
                    canc=sum(1 for i in su if c[i]%q==(lam*u[i])%q)
                    best=max(best,canc)
                    y=tuple((c[i]-lam*u[i])%q for i in range(n))
                    assert any(y)
                assert best>=ceil(d/(q-1)),(n,c,u,best,d)
                checked+=1
    return checked

def verify_counterexample_family():
    for q in (3,5,7):
        G=[[1,0,0,0,1],[0,1,1,1,1]]
        A=weight_distribution(G,q)
        expected=[1,0,q-1,0,2*(q-1),(q-1)*(q-2)]
        assert A==expected,(q,A,expected)
        n,k,d,t=5,2,2,1
        assert k>=n-2*d+1 and A[d+1]==0 and A[2*d+1]>0

def verify_long_gap_theorem_ternary():
    q=3
    tested=0
    for n in range(2,7):
        for k in range(1,n+1):
            for G in subspaces_rref(q,n,k):
                A=weight_distribution(G,q)
                tested+=1
                d=next((w for w in range(1,n+1) if A[w]),None)
                if d is None:
                    continue
                t=0
                while d+t+1<=n and A[d+t+1]==0:
                    t+=1
                if t==0:
                    continue
                h=n-k+1-d
                if t<h:
                    continue
                r=ceil(d/(q-1))
                lo=max(n-k+2,2*d+1)
                hi=min(n,d+t+r)
                assert all(A[w]==0 for w in range(lo,hi+1)),(n,k,d,t,A,G,lo,hi)
    return tested

if __name__=="__main__":
    verify_counterexample_family()
    pair_count=verify_cancellation_lemma()
    code_count=verify_long_gap_theorem_ternary()
    print("counterexample_family: PASS for q=3,5,7")
    print("cancellation_lemma_pairs_checked:",pair_count)
    print("ternary_linear_codes_checked_n_le_6:",code_count)
    print("all_checks: PASS")
