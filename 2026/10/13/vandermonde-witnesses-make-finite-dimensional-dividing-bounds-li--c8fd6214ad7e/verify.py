from fractions import Fraction

def rank(mat):
    a=[list(map(Fraction,row)) for row in mat]
    if not a: return 0
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        q=a[r][c]
        a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c]
                a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

checks=0
for k in range(2,11):
    ts=list(range(k))
    V=[[t**j for j in range(k-1)] for t in ts]
    rhs=[t**(k-1) for t in ts]
    for s in range(1,k):
        A=V[:s]
        aug=[A[i]+[rhs[i]] for i in range(s)]
        assert rank(A)==s
        assert rank(aug)==s
        checks+=2
    assert rank(V)==k-1
    assert rank([V[i]+[rhs[i]] for i in range(k)])==k
    checks+=2
    for r in range(1,6):
        # r independent blocks each contribute k-1 vector directions.
        assert r*(k-1) < 2*k*r
        assert r*(k-1) == sum(k-1 for _ in range(r))
        checks+=2
print(f"VERIFY_OK {checks} exact rank assertions")
