#!/usr/bin/env python3
"""Exact checks for the genus-four cyclic-trigonal Cartier stratification.

All finite-field operations use the standard-library integer representation;
F_25 = F_5[t]/(t*t-2).  No symbolic-math dependency is needed.
"""
from collections import Counter

class Field:
    def __init__(self, q):
        assert q in (5, 25)
        self.q = q
        self.p = 5
        self.one = 1
        def unpack(i): return (i, 0) if q == 5 else (i % 5, i // 5)
        def pack(x, y): return x % 5 if q == 5 else x % 5 + 5 * (y % 5)
        self.add = [[0] * q for _ in range(q)]
        self.mul = [[0] * q for _ in range(q)]
        for i in range(q):
            a, b = unpack(i)
            for j in range(q):
                c, d = unpack(j)
                self.add[i][j] = pack(a+c, b+d)
                self.mul[i][j] = pack(a*c+2*b*d, a*d+b*c)
        self.neg = [next(j for j in range(q) if self.add[i][j] == 0) for i in range(q)]
        self.inv = [None] + [next(j for j in range(1, q) if self.mul[i][j] == 1) for i in range(1, q)]
        self.frob = [self.power(i, 5) for i in range(q)]
    def power(self, a, n):
        acc = 1
        while n:
            if n & 1: acc = self.mul[acc][a]
            a = self.mul[a][a]
            n //= 2
        return acc
    def plus(self, *v):
        a = 0
        for b in v: a = self.add[a][b]
        return a
    def times(self, *v):
        a = 1
        for b in v: a = self.mul[a][b]
        return a
    def minus(self, a, b):
        return self.add[a][self.neg[b]]

def trim(v):
    while v and v[-1] == 0: v.pop()
    return v

def polynomial_mod(u, v, k):
    u = trim(u[:]); v = trim(v[:]); assert v
    while len(u) >= len(v):
        t = k.mul[u[-1]][k.inv[v[-1]]]
        off = len(u)-len(v)
        for j, e in enumerate(v):
            u[off+j] = k.minus(u[off+j], k.mul[t][e])
        trim(u)
    return u

def singular_by_gcd(a, b, c, k):
    f = [c,b,0,a,0,1]
    fp = trim([b,0,k.mul[3][a]])
    if not fp: return True
    while fp:
        f, fp = fp, polynomial_mod(f, fp, k)
    return len(f) > 1

def discriminant(a, b, c, k):
    a2 = k.power(a, 2)
    apb = k.plus(a2,b)
    return k.minus(k.times(k.power(a,5),k.power(c,2)),
                   k.times(3,k.power(b,3),k.power(apb,2)))

def poly_product(u, v, k):
    w = [0] * (len(u) + len(v) - 1)
    for i,a in enumerate(u):
        if not a: continue
        for j,b in enumerate(v):
            if b: w[i+j] = k.plus(w[i+j], k.mul[a][b])
    return w

def cartier_from_expansion(a, b, c, k):
    f = [c,b,0,a,0,1]
    f3 = poly_product(poly_product(f, f, k), f, k)
    # Extract coefficients at exponents 4,9,14 (p n + p-1).
    return (f3[4], f3[9], f3[14], f[3], f[4])

def matrix_rank(v, k):
    v = [row[:] for row in v]
    r = 0
    for j in range(len(v[0])):
        z = next((i for i in range(r,len(v)) if v[i][j]), None)
        if z is None: continue
        v[r],v[z] = v[z],v[r]
        fac = k.inv[v[r][j]]
        v[r] = [k.mul[fac][x] for x in v[r]]
        for i in range(len(v)):
            if i == r: continue
            e = v[i][j]
            if e:
                v[i] = [k.minus(u,k.mul[e][w]) for u,w in zip(v[i],v[r])]
        r += 1
    return r

def mmul(x,y,k):
    return [[k.plus(*(k.mul[x[i][m]][y[m][j]] for m in range(len(y))))
             for j in range(len(y[0]))] for i in range(len(x))]

def sample_matrix_test(a,b,c,k):
    u0,u1,u2,v0,v1=cartier_from_expansion(a,b,c,k)
    assert u2 == v1 == 0 and v0 == a
    assert u0 == k.times(a,b,c)
    assert u1 == k.times(a,k.plus(k.power(a,2), b))
    root=lambda x: k.frob[x] if k.q==25 else x
    M=[[0,0,root(a),0],
       [root(u0),0,0,0],
       [root(u1),0,0,0],
       [0,0,0,0]]
    a_number=4-matrix_rank(M,k)
    stable=M
    twisted=M
    for _ in range(1,5):
        twisted=[[k.frob[x] for x in row] for row in twisted]
        stable=mmul(stable, twisted, k)
    p_rank=matrix_rank(stable,k)
    expected=(0,4) if a == 0 else ((0,2) if b == k.neg[k.power(a,2)] else (2,2))
    assert (p_rank,a_number)==expected, (k.q,a,b,c,(p_rank,a_number),expected)


def run(q):
    k=Field(q)
    totals=Counter(); per_type=Counter()
    probes={}
    for a in range(q):
        for b in range(q):
            for c in range(q):
                singular=singular_by_gcd(a,b,c,k)
                assert singular == (discriminant(a,b,c,k)==0), (q,a,b,c)
                if singular:
                    totals['singular']+=1
                    continue
                expected=(0,4) if not a else ((0,2) if b == k.neg[k.power(a,2)] else (2,2))
                totals[expected]+=1
                if q==5 or len(probes.setdefault(expected,[]))<40:
                    sample_matrix_test(a,b,c,k)
                    probes.setdefault(expected,[]).append((a,b,c))
    assert totals['singular']==q*q
    assert totals[(0,4)]==q*(q-1)
    assert totals[(0,2)]==(q-1)**2
    assert totals[(2,2)]==(q-1)**3
    assert sum(totals.values())==q**3
    print('F_'+str(q)+':',dict(totals),'verified Cartier sample sizes',
          {str(t):len(s) for t,s in probes.items()})

if __name__=='__main__':
    run(5)
    run(25)
    print('VERIFY_OK')
