from itertools import product

def norm(v,p):
    for x in v:
        if x%p:
            inv=pow(x,-1,p)
            return tuple((a*inv)%p for a in v)
    raise ValueError

def proj(n,p):
    return sorted({norm(v,p) for v in product(range(p), repeat=n) if any(v)})

def dot(a,b,p):
    return sum(x*y for x,y in zip(a,b))%p

def qnum(m,q):
    return (q**m-1)//(q-1)

def check(n,q):
    pts=proj(n,q)
    hypers=pts[:]  # normalized nonzero covectors
    V=[(P,H) for P in pts for H in hypers if dot(H,P,q)!=0]
    idx={v:i for i,v in enumerate(V)}
    N=len(V)
    expectN=q**(n-1)*qnum(n,q)
    assert N==expectN
    A=[set() for _ in V]
    for i,(P,H) in enumerate(V):
        for j in range(i+1,N):
            Q,M=V[j]
            if dot(H,Q,q)==0 and dot(M,P,q)==0:
                A[i].add(j); A[j].add(i)
    k=q**(n-2)*qnum(n-1,q)
    lam=q**(n-3)*qnum(n-2,q)
    assert {len(s) for s in A}=={k}
    for i in range(N):
        for j in A[i]:
            if i<j:
                assert len(A[i]&A[j])==lam
    E=sum(map(len,A))//2
    T=sum(len(A[i]&A[j]) for i in range(N) for j in A[i] if i<j)//3
    assert E==N*k//2
    assert T==N*k*lam//6
    # Local graph degree equals lambda.
    for i in range(N):
        Nei=A[i]
        for j in Nei:
            assert len(A[j]&Nei)==lam
    if n==3:
        assert lam==1
        # Every local graph is a perfect matching.
        assert all(all(len(A[j]&A[i])==1 for j in A[i]) for i in range(N))
    return N,k,lam,E,T

for n,q in [(3,2),(3,3),(3,5),(4,2),(5,2)]:
    vals=check(n,q)
    print(f"n={n} q={q} N={vals[0]} k={vals[1]} lambda={vals[2]} E={vals[3]} T={vals[4]}")
print("VERIFY_OK")
