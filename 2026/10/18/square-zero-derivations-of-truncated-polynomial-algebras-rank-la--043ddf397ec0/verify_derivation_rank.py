#!/usr/bin/env python3
"""Exact finite-field brute-force checks for square-zero ordinary derivations.

No third-party packages. Run: python verify_derivation_rank.py
The direct routine builds the full coefficient matrix of every K-derivation,
multiplies matrices, and computes ranks independently of the valuation formulas.
"""
from collections import Counter
from itertools import product


class Field:
    def __init__(self, q):
        if q not in (2, 3, 4, 5):
            raise ValueError('The brute-force examples support q=2,3,4,5.')
        self.q = q
        self.p = 2 if q == 4 else q
        self.add = (lambda a, b: a ^ b) if q == 4 else (lambda a, b: (a + b) % q)
        self.mul = self._mul4 if q == 4 else (lambda a, b: (a * b) % q)
        self.inv = [None] + [next(b for b in range(1, q) if self.mul(a, b) == 1)
                                  for a in range(1, q)]

    @staticmethod
    def _mul4(a, b):
        # GF(4)=GF(2)[z]/(z^2+z+1), bits encode 1,z.
        v = 0
        for i in range(2):
            for j in range(2):
                if ((a >> i) & 1) and ((b >> j) & 1):
                    v ^= 1 << (i+j)
        if v & 8:
            raise AssertionError('Product degree exceeds two')
        if v & 4:
            v ^= 7  # z^2=z+1 (subtract polynomial z^2+z+1)
        return v

    def scale_integer(self, n, a):
        return a if n % self.p == 1 else 0 if n % self.p == 0 else (n * a) % self.q


def matrix_rank(M, F):
    M = [row[:] for row in M]
    n = len(M)
    d = 0
    for col in range(n):
        pivot = next((i for i in range(d, n) if M[i][col] != 0), None)
        if pivot is None:
            continue
        M[d], M[pivot] = M[pivot], M[d]
        fac = F.inv[M[d][col]]
        M[d] = [F.mul(fac, x) for x in M[d]]
        for i in range(n):
            if i != d and M[i][col]:
                c = M[i][col]
                M[i] = [F.add(x, F.mul(c, y)) if F.p == 2 else
                        (x-F.mul(c,y)) % F.q for x,y in zip(M[i],M[d])]
        d += 1
        if d == n:
            break
    return d


def exhaustive(n, F):
    q, p = F.q, F.p
    output = Counter()
    for f in product(range(q), repeat=n):
        if n % p and f[0]:
            continue  # Leibniz relation D(t^n)=0.
        D = [[0] * n for _ in range(n)]
        for j in range(1, n):
            for a in range(n-j+1):
                D[j+a-1][j] = F.scale_integer(j, f[a])
        square_is_zero = True
        for i in range(n):
            for j in range(n):
                tot=0
                for k in range(n):
                    tot=F.add(tot,F.mul(D[i][k],D[k][j]))
                if tot:
                    square_is_zero=False
                    break
            if not square_is_zero:
                break
        if square_is_zero:
            output[matrix_rank(D,F)] += 1
    return dict(sorted(output.items()))


def count_val(length, v, q):
    return 1 if v == length else (q-1)*q**(length-v-1)


def predicted(n, q):
    p = 2 if q % 2 == 0 else q
    ans=Counter()
    if n == 1:
        return {0:1}
    if p != 2:
        # n=2 gives only the zero derivation.
        a0 = (n+1)//2 if n % 2 else n//2+1
        if n % 2 == 0 and (n//2) % p == 0:
            a0=n//2
        for a in range(a0,n):
            k=n-a
            ans[k-k//p] += count_val(n,a,q)
        ans[0]+=1
    else:
        m = n//2
        for a in range(m+1):
            for b in range((m+1)//2,m+1):
                if a+b<m:
                    continue
                ans[m-min(a,b)] += count_val(m,a,q)*count_val(m,b,q)
    return dict(sorted(ans.items()))


def global_count(n, q):
    p=2 if q%2==0 else q
    if p==2:
        m=n//2
        if m==0:return 1
        return q**m + (m//2)*(q-1)*q**(m-1)
    if n<=2:return 1
    a0=n//2 +1 if n%2==0 else (n+1)//2
    if n%2==0 and (n//2)%p==0:
        a0=n//2
    return q**(n-a0)


def run():
    cases=[]
    for q, nmax in ((2,9),(3,7),(4,6),(5,5)):
        F=Field(q)
        for n in range(1,nmax+1):
            found=exhaustive(n,F)
            formula=predicted(n,q)
            assert found==formula,(q,n,found,formula)
            assert sum(found.values())==global_count(n,q)
            assert max(found,default=0)<=n//2
            cases.append((q,n,len(found),sum(found.values())))
    # For every even n=2m, the number of acyclic derivations
    # in char 2 is (q-1)q^(m-1) (rank=m).
    for q in (2,4):
        for m in range(1,4):
            e=predicted(2*m,q)
            assert e[m]==(q-1)*q**(m-1)
            assert e==predicted(2*m+1,q)
    for row in cases:print('OK q=%s n=%s ranks=%s total=%s'%row)
    print('ALL_EXACT_CHECKS_PASSED %d exhaustive field/length cases' %len(cases))

if __name__=='__main__':run()
