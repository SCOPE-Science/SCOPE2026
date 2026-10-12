from itertools import product


def chi(a,q):
    a %= q
    if a == 0:
        return 0
    # This checker uses odd prime q in exhaustive tests.
    v = pow(a,(q-1)//2,q)
    return 1 if v == 1 else -1


def formula_rank1(q, diag):
    n=len(diag)
    base=n*q**(n-1) - (q**n-1)//(q-1)
    corr=0
    prod_diag=1
    for k,g in enumerate(diag, start=1):
        prod_diag=(prod_diag*g)%q
        if k%2==0:
            m=k//2
            eps=chi(((-1)**m)*prod_diag,q)
            corr += (q-1)*eps*q**(n-m-1)
    return base+corr


def rank_mod(A,q):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=None
        for i in range(r,m):
            if A[i][c] % q:
                piv=i; break
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c] % q,-1,q)
        A[r]=[(x*inv)%q for x in A[r]]
        for i in range(r+1,m):
            f=A[i][c]%q
            if f:
                A[i]=[(A[i][j]-f*A[r][j])%q for j in range(n)]
        r+=1
        if r==m:
            break
    return r


def exhaustive_rank1(q,diag):
    n=len(diag)
    pos=[(i,j) for i in range(n) for j in range(i,n)]
    total=0
    for vals in product(range(q), repeat=len(pos)):
        U=[[0]*n for _ in range(n)]
        for v,(i,j) in zip(vals,pos):
            U[i][j]=v
        if rank_mod(U,q)!=1:
            continue
        ok=True
        for a in range(n):
            for b in range(n):
                s=sum(U[i][a]*diag[i]*U[i][b] for i in range(n))%q
                if s:
                    ok=False; break
            if not ok:
                break
        if ok:
            total+=1
    return total


def main():
    cases=[
        (3,[1,1,1,2],44),
        (3,[1,2,1,1],80),
        (3,[1,1,1],8),
        (5,[1,1,1],64),
        (7,[1,1,1],48),
    ]
    for q,d,expected in cases:
        f=formula_rank1(q,d)
        assert f==expected,(q,d,f,expected)
        if len(d)<=4 and (q,len(d)) in {(3,4),(3,3),(5,3),(7,3)}:
            brute=exhaustive_rank1(q,d)
            assert brute==f,(q,d,brute,f)
        print(f"q={q} diag={d} count={f}")
    # Same global form, distinct flag-sensitive counts.
    assert sorted([1,1,1,2])==sorted([1,2,1,1])
    assert formula_rank1(3,[1,1,1,2]) != formula_rank1(3,[1,2,1,1])
    print("VERIFY_OK")

if __name__=='__main__':
    main()
