"""Independent small-field exhaustive verification of rank-one retraction product fibers.
Use: python verify.py (Python 3 standard library)."""
from itertools import product
from collections import Counter


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # irreducible polynomial X^2+X+1 over F2
    return result


def inv(a, q):
    assert a
    return next(b for b in range(1, q) if mul(a,b,q) == 1)


def dot(v, w, q):
    s=0
    for a,b in zip(v,w):
        s=add(s,mul(a,b,q),q)
    return s


def mat_outer(v,w,q):
    return tuple(mul(a,b,q) for a in v for b in w)


def matmul(A,B,n,q):
    return tuple(
        sumprod([mul(A[i*n+k],B[k*n+j],q) for k in range(n)],q)
        for i in range(n) for j in range(n)
    )


def sumprod(v,q):
    s=0
    for a in v: s=add(s,a,q)
    return s


def projections(n,q):
    # First nonzero coordinate of each image vector is one.
    P=[]
    vectors=product(range(q),repeat=n)
    for v0 in vectors:
        if not any(v0):continue
        pos=next(i for i,x in enumerate(v0) if x)
        scale=inv(v0[pos],q)
        v=tuple(mul(x,scale,q) for x in v0)
        if v in {p[0] for p in P}:
            continue
        for phi in product(range(q),repeat=n):
            if dot(v,phi,q)==1:
                P.append((v,phi,mat_outer(v,phi,q)))
    return P


def rank1_nonzero_trace(A,n,q):
    tr=sumprod([A[i*n+i] for i in range(n)],q)
    # Nonzero target is rank one because it was built from rank-one factors.
    return tr


def formula_fiber(A,n,q):
    if not any(A):
        return ((q**n-1)//(q-1))*q**(n-1) * ((q**(n-1)-1)//(q-1))*q**(n-1)
    t=rank1_nonzero_trace(A,n,q)
    if t==0:
        return q**(2*n-3)
    if t==1:
        return q**(n-1)+(q**(n-1)-1)*q**(n-2)
    return (q**(n-1)-1)*q**(n-2)


def check(n,q):
    P=projections(n,q)
    pexp=((q**n-1)//(q-1))*q**(n-1)
    assert len(P)==pexp,(n,q,'projection count',len(P),pexp)
    fibers=Counter()
    for _,_,E in P:
        for _,_,F in P:
            fibers[matmul(E,F,n,q)]+=1
    assert sum(fibers.values())==len(P)**2
    for A,N in fibers.items():
        expected=formula_fiber(A,n,q)
        assert N==expected,(n,q,'fiber mismatch',A,N,expected)
    # Compare the full target support; all rank-one matrices are products.
    target_count=1
    for v in product(range(q),repeat=n):
        if not any(v):continue
        for phi in product(range(q),repeat=n):
            if not any(phi): continue
            A=mat_outer(v,phi,q)
            if A not in fibers:
                raise AssertionError((n,q,'rank-one target missing',A))
    expected_target=1+(q**n-1)*(q**n-1)//(q-1)
    assert len(fibers)==expected_target,(n,q,'support',len(fibers),expected_target)
    return len(P),len(fibers),len(P)**2


if __name__=='__main__':
    for n,q in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)]:
        p,t,pairs=check(n,q)
        print(f'n={n} q={q} rank_one_idempotents={p} targets={t} pairs={pairs} VERIFY_OK')
    print('ALL_VERIFY_OK')
