#!/usr/bin/env python3
"""Finite-field independent checks of Nijenhuis rank enumerators (stdlib only)."""
from collections import Counter
from itertools import product

class Field:
    def __init__(self, q):
        self.q = q
        assert q in (2, 3, 4, 5)
    def add(self, a, b):
        return (a ^ b) if self.q == 4 else (a + b) % self.q
    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q
    def sub(self, a, b):
        return self.add(a, self.neg(b))
    def mul(self, a, b):
        if self.q != 4:
            return a * b % self.q
        x = 0
        while b:
            if b & 1: x ^= a
            b >>= 1
            a <<= 1
            if a & 4: a ^= 7  # x^2 + x + 1
        return x
    def inv(self, a):
        assert a
        return next(b for b in range(1, self.q) if self.mul(a, b) == 1)

def rank(columns, f):
    if not columns: return 0
    nrow = len(columns[0]); ncol = len(columns)
    rows = [[columns[j][i] for j in range(ncol)] for i in range(nrow)]
    r = 0
    for c in range(ncol):
        i = next((j for j in range(r, nrow) if rows[j][c]), None)
        if i is None: continue
        rows[r], rows[i] = rows[i], rows[r]
        scale = f.inv(rows[r][c]); rows[r] = [f.mul(scale, x) for x in rows[r]]
        for k in range(nrow):
            if k != r and rows[k][c]:
                a = rows[k][c]; rows[k] = [f.sub(rows[k][j], f.mul(a, rows[r][j])) for j in range(ncol)]
        r += 1
        if r == nrow: break
    return r

def gaussian(n, r, q):
    if r < 0 or r > n: return 0
    # compute exact numerator and denominator before dividing
    num = den = 1
    for i in range(r): num *= q ** (n - i) - 1; den *= q ** (r - i) - 1
    assert num % den == 0
    return num // den

def GL(r, q):
    ans = 1
    for i in range(r): ans *= q ** r - q ** i
    return ans

def predicted(n, q):
    d = Counter()
    for r in range(n + 1):
        M = gaussian(n, r, q) ** 2 * GL(r, q)
        A = gaussian(n - 1, r, q) * gaussian(n - 1, r - 1, q) * GL(r, q)
        B = (q ** r) * gaussian(n - 1, r, q) ** 2 * GL(r, q)
        F = 0
        if r >= 1:
            F = gaussian(n - 1, r - 1, q) * q ** (n - 1)
            for i in range(r - 1): F *= q ** (n - 1) - q ** i
        d[r] += M + (q ** n - 1) * A
        d[r + 1] += (q ** n - 1) * B + (q - 1) * (M + (q ** n - 1) * F)
    assert sum(d.values()) == q ** (n * n - n + 1) * (2 * q ** n - 1)
    return d

def nij(columns, f):
    d = len(columns)
    def prod(x, y):
        return (f.mul(x[0],y[0]),) + tuple(f.add(f.mul(x[0],y[k]), f.mul(y[0],x[k])) for k in range(1,d))
    def sm(x,y): return tuple(f.sub(a,b) for a,b in zip(x,y))
    def ap(x,y): return tuple(f.add(a,b) for a,b in zip(x,y))
    def N(x):
        return tuple(sum_in_field([f.mul(x[j],columns[j][k]) for j in range(d)],f) for k in range(d))
    basis = [tuple(1 if i==j else 0 for i in range(d)) for j in range(d)]
    for i in range(d):
        for j in range(d):
            x, y = basis[i], basis[j]
            if prod(columns[i], columns[j]) != N(sm(ap(prod(columns[i],y),prod(x,columns[j])),N(prod(x,y)))):
                return False
    return True

def sum_in_field(a,f):
    t=0
    for x in a:t=f.add(t,x)
    return t

def canonical(columns, f):
    n=len(columns)-1; a=columns[0][0]
    if any(columns[j][0] for j in range(1,n+1)): return False
    u=columns[0][1:]
    for i in range(n):
        Tu = sum_in_field([f.mul(columns[j+1][i+1],u[j]) for j in range(n)],f)
        if Tu != f.mul(a,u[i]): return False
    return True

def exhaustive(n,q):
    f=Field(q);hist=Counter(); total=0
    for values in product(range(q),repeat=(n+1)**2):
        cols=[tuple(values[j*(n+1):(j+1)*(n+1)]) for j in range(n+1)]
        good=canonical(cols,f)
        if good != nij(cols,f): raise AssertionError(('canonical mismatch',n,q,values))
        if good:
            hist[rank(cols,f)]+=1;total+=1
    expected=predicted(n,q)
    assert hist == +expected, (n,q,hist,expected)
    print('EXHAUSTIVE_OK',f'n={n}, q={q}, N={total}, ranks={dict(sorted(hist.items()))}')

def canonical_q4(n):
    f=Field(4);h=Counter()
    for a in range(4):
        for data in product(range(4),repeat=n*n+n):
            u=data[:n]; flat=data[n:]
            T=[tuple(flat[j*n:(j+1)*n]) for j in range(n)]
            columns=[(a,)+u] + [(0,)+T[j] for j in range(n)]
            if canonical(columns,f):
                assert nij(columns,f)
                h[rank(columns,f)]+=1
    assert h==+predicted(n,4),(h,predicted(n,4))
    print('EXTENSION_FIELD_OK',f'n={n}, q=4, N={sum(h.values())}, ranks={dict(sorted(h.items()))}')

if __name__=='__main__':
    for n,q in [(1,2),(1,3),(2,2),(2,3),(3,2)]: exhaustive(n,q)
    canonical_q4(2)
    print('VERIFY_OK')
