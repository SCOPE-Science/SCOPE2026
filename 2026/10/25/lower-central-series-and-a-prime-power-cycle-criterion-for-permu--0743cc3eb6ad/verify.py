"""Independent finite checks of the permutation-twist group invariants.
Run with Python 3 and SymPy 1.x: python verify.py
"""
from itertools import combinations, permutations
from math import gcd
from functools import reduce
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def cycle_permutation(lengths):
    n = sum(lengths)
    p = list(range(n))
    start = 0
    for length in lengths:
        for j in range(length):
            p[start + j] = start + ((j+1) % length)
        start += length
    return tuple(p)


def permute(p, a, times=1):
    b = tuple(a)
    for _ in range(times % perm_order(p)):
        c = [0] * len(p)
        for i, x in enumerate(b):
            c[p[i]] = x
        b = tuple(c)
    return b


def perm_order(p):
    seen = set()
    from math import lcm
    ans = 1
    for i in range(len(p)):
        if i in seen:
            continue
        j = i
        ell = 0
        while j not in seen:
            seen.add(j)
            j = p[j]
            ell += 1
        ans = lcm(ans, ell)
    return ans


def mul(p, a, b):
    pb = permute(p, b, sum(a))
    return tuple(x+y for x,y in zip(a,pb))


def inv(p,a):
    return tuple(-x for x in permute(p,a,-sum(a)))


def comm(p,a,b):
    return mul(p,mul(p,mul(p,a,b),inv(p,a)),inv(p,b))


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for k in range(lo,n+1):
        for t in partitions(n-k,k):
            yield (k,)+t


def invariants(lengths):
    n = sum(lengths)
    p = cycle_permutation(lengths)
    E = Matrix.eye(n)
    P = Matrix.zeros(n,n)
    for i,j in enumerate(p):
        P[j,i] = 1
    A = E-P
    B = Matrix(n,n-1,lambda i,j: (1 if i==j else (-1 if i==n-1 else 0))) if n>1 else Matrix.zeros(1,0)
    C = A*B
    D = smith_normal_form(C,domain=ZZ)
    diag = [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]!=0]
    positive = [d for d in diag if d>1]
    expected = reduce(gcd,lengths)
    assert positive == ([] if expected==1 else [expected]), (lengths, positive, expected)
    assert len(diag) == n-len(lengths), (lengths,diag)
    for i,j in combinations(range(n),2):
        a=tuple(int(x==i) for x in range(n))
        b=tuple(int(x==j) for x in range(n))
        ab=mul(p,a,b)
        ba=mul(p,b,a)
        # Both products have degree 2; their quotient is the ordinary difference.
        diff=tuple(x-y for x,y in zip(ab,ba))
        target=tuple(int(C[k,i]) - int(C[k,j]) for k in range(n)) if i<n-1 and j<n-1 else None
        if target is not None:
            assert diff==target, (lengths,i,j,diff,target)
        assert comm(p,a,b)==diff
        assert mul(p,a,inv(p,a))==tuple([0]*n)
        assert mul(p,inv(p,a),a)==tuple([0]*n)
    return positive


if __name__ == '__main__':
    checks=0
    for n in range(1,9):
        for lengths in partitions(n):
            invariants(lengths)
            checks+=1
    assert checks == 66, checks
    # Short direct check of the non-prime-power cyclotomic unit: Phi_6(t)=t^2-t+1.
    # In Z[t]/(Phi_6), (1-t)*t = 1 by Phi_6(t)=0.
    import sympy as s
    t=s.Symbol('t')
    assert s.rem((1-t)*t-1,t**2-t+1,t)==0
    print('VERIFY_OK: {} partition types; group laws, generators, Smith invariants, Phi_6 unit'.format(checks))
