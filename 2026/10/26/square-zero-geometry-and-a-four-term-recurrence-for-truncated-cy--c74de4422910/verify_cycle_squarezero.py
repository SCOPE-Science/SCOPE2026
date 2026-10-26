#!/usr/bin/env python3
"""Standalone exact checks for square-zero radicals of fourth-truncated cyclic quiver algebras.

Usage: python verify_cycle_squarezero.py
No nonstandard Python packages are needed.
"""
from itertools import product
from math import comb


def support_data(n, mask):
    s = [(mask >> i) & 1 for i in range(n)]
    if any(s[i] * s[(i+1) % n] for i in range(n)):
        return None
    k = sum(s)
    p2 = sum(s[i] * s[(i+2) % n] for i in range(n))
    p3 = sum(s[i] * s[(i+3) % n] for i in range(n))
    return k, 2*k-p2-p3, p2+p3


def weighted_formula(n, q):
    return sum((q-1)**k * q**(2*n-r)
               for mask in range(1 << n)
               if (d := support_data(n, mask)) is not None
               for k, r, _ in [d])


def transfer(n, q):
    states = [(a,b,c) for a in (0,1) for b in (0,1) for c in (0,1)
              if not a*b and not b*c]
    mat = [[0]*5 for _ in range(5)]
    for i,(a,b,c) in enumerate(states):
        for d in (0,1):
            if c*d:
                continue
            j = states.index((b,c,d))
            mat[i][j] = q*q if not d else (q-1)*q**(a+b)
    P = [[int(i==j) for j in range(5)] for i in range(5)]
    def mul(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(5)) for j in range(5)]
                for i in range(5)]
    for _ in range(n):
        P = mul(P,mat)
    return sum(P[i][i] for i in range(5))


def leading_components(n):
    return 1 + sum(n * comb(k, n-2*k)//k
                   for k in range((n+2)//3, n//2+1))


def gf4mul(a,b):
    out = 0
    for i in range(2):
        if b & (1 << i):
            out ^= a << i
    for i in (2,):
        if out & (1 << i):
            out ^= 0b111 << (i-2)
    return out


def field_mul(q,a,b):
    return gf4mul(a,b) if q == 4 else (a*b)%q


def field_add(q,a,b):
    return a^b if q == 4 else (a+b)%q


def brute_alphabeta(n,q):
    nonzero = [(a,[(i,a[i]) for i in range(n) if a[i]])
               for a in product(range(q), repeat=n)]
    count = 0
    for alpha, nz in nonzero:
        if any(alpha[i] and alpha[(i+1)%n] for i in range(n)):
            continue
        for beta in product(range(q), repeat=n):
            if all(field_add(q, field_mul(q,alpha[i],beta[(i+1)%n]),
                             field_mul(q,beta[i],alpha[(i+2)%n])) == 0
                   for i in range(n)):
                count += 1
    return count * q**n


def literal_path_square(n,q,alpha,beta,gamma):
    v = {(i,1):alpha[i] for i in range(n)}
    v.update({(i,2):beta[i] for i in range(n)})
    v.update({(i,3):gamma[i] for i in range(n)})
    result = {(i,d):0 for i in range(n) for d in (2,3)}
    for (i,a),x in v.items():
        if not x:continue
        for (j,b),y in v.items():
            if not y or a+b>3 or (i+a)%n!=j:continue
            result[(i,a+b)] = field_add(q,result[(i,a+b)],field_mul(q,x,y))
    return all(x==0 for x in result.values())


def main():
    for q in (2,3,4,5):
        vals=[weighted_formula(n,q) for n in range(4,12)]
        for n,v in enumerate(vals, start=4):
            assert v==transfer(n,q), (n,q,v)
        for i in range(4):
            assert vals[i+4]==q**2*vals[i+3]+q**3*(q-1)*vals[i+2]-q**6*(q-1)**2*vals[i]
        print('TRANSFER_AND_RECURRENCE_OK',q)
    for n in range(4,16):
        count=sum(support_data(n,mask) is not None and
                  (lambda z:z[1]==z[0])(support_data(n,mask))
                  for mask in range(1<<n))
        assert count == leading_components(n)
    print('TOP_COMPONENTS_OK')
    tests=[(4,2),(5,2),(6,2),(7,2),(4,3),(5,3),(6,3),(4,4),(5,4)]
    for n,q in tests:
        got=brute_alphabeta(n,q)
        expected=weighted_formula(n,q)
        assert got==expected,(n,q,got,expected)
        print('EXHAUSTIVE_SQUARE_ZERO_OK',n,q,got)
    for n,q in ((4,2),(5,3),(5,4),(7,2)):
        for j in range(100):
            alpha=[(17*i+7*j+3*i*j)%q for i in range(n)]
            beta=[(5*i+11*j+2*i*j)%q for i in range(n)]
            gamma=[(19*i+3*j+7*i*j)%q for i in range(n)]
            from_equations=(all(not (alpha[i] and alpha[(i+1)%n]) for i in range(n)) and
                all(field_add(q,field_mul(q,alpha[i],beta[(i+1)%n]),
                            field_mul(q,beta[i],alpha[(i+2)%n]))==0
                    for i in range(n)))
            assert literal_path_square(n,q,alpha,beta,gamma)==from_equations
    print('LITERAL_PATH_MULTIPLICATION_OK')
    print('VERIFY_OK_CYCLIC_J4_SQUAREZERO')

if __name__=='__main__':
    main()
