from itertools import product

def matmul(A,B,n,q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))

def eye(n):
    return tuple(1 if i==j else 0 for i in range(n) for j in range(n))

def zero(n): return (0,)*(n*n)

def rank(A,n,q):
    M=[list(A[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for c in range(n):
        piv=next((i for i in range(r,n) if M[i][c]%q),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c],-1,q)
        M[r]=[(x*inv)%q for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]%q:
                f=M[i][c]%q
                M[i]=[(M[i][j]-f*M[r][j])%q for j in range(n)]
        r+=1
    return r

def is_nilpotent(A,n,q):
    P=eye(n)
    for _ in range(1,n+1):
        P=matmul(P,A,n,q)
        if P==zero(n): return True
    return False

def check(n,q):
    mats=list(product(range(q), repeat=n*n))
    nz=[A for A in mats if A!=zero(n)]
    profiles={}
    for A in nz:
        r=rank(A,n,q); eps=int(is_nilpotent(A,n,q))
        deg=0
        for B in nz:
            if B==A: continue
            if is_nilpotent(matmul(A,B,n,q),n,q): deg+=1
        pred=q**(n*n-r)-1-eps
        assert deg==pred,(n,q,A,r,eps,deg,pred)
        profiles.setdefault((r,eps),set()).add(deg)
    assert all(len(v)==1 for v in profiles.values())
    vals=[next(iter(v)) for v in profiles.values()]
    assert len(vals)==len(set(vals))
    maxdeg=max(vals); mindeg=min(vals)
    assert maxdeg==q**(n*n-1)-1
    assert mindeg==q**(n*n-n)-1
    print(f"case n={n} q={q}: vertices={len(nz)} profiles={sorted((k,next(iter(v))) for k,v in profiles.items())}")

for case in [(2,2),(2,3),(3,2)]: check(*case)
print('VERIFY_OK')
