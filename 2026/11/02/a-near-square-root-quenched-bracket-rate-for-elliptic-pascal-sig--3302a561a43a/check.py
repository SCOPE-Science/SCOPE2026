"""Self-contained exact finite checks for static Pascal-sign covariance identities.

This checks finite combinatorics, not the almost-sure conclusions.
"""
from fractions import Fraction
from itertools import product
from math import comb

assertions = 0

def check(ok, message):
    global assertions
    assertions += 1
    if not ok:
        raise AssertionError(message)

def downmask(n):
    return frozenset(k for k in range(n+1) if k & n == k)

def g(n, rho):
    return rho ** Fraction(1 << (n.bit_count()-1)) if n else Fraction(1)

def mean_prod(s,t,params):
    z = Fraction(1)
    for k in downmask(s) ^ downmask(t):
        z *= 1 - 2*params[k]
    return z

for n in range(128):
    d = downmask(n)
    for k in range(n+1):
        check((comb(n,k)%2 == 1) == (k in d), ('Lucas',n,k))
    check(len(d)==1<<n.bit_count(),('count',n))

for a in range(64):
    for b in range(a+1,64):
        d = len(downmask(a)^downmask(b))
        check(d >= (1 << (max(a.bit_count(),b.bit_count())-1)), ('distance',a,b))

profiles = [
    [Fraction(1,2)]*8,
    [Fraction(1,3) if k%2 else Fraction(2,3) for k in range(8)],
    [Fraction(k+2,12) for k in range(8)],
]
for ps in profiles:
    rho = max(abs(1-2*p) for p in ps)
    for s in range(8):
        for t in range(8):
            exact = Fraction(0)
            # Exhaustively evaluate all 256 environments with product probabilities.
            for bits in product((0,1),repeat=8):
                prob=Fraction(1)
                for p,b in zip(ps,bits):
                    prob *= p if b else 1-p
                fs = -1 if sum(bits[k] for k in downmask(s))%2 else 1
                ft = -1 if sum(bits[k] for k in downmask(t))%2 else 1
                exact += prob * fs * ft
            check(exact==mean_prod(s,t,ps),('moment',s,t))
            if s<t:
                check(abs(exact)<=rho**(1<<(t.bit_count()-1)),('pairbound',s,t))
    for lo in range(8):
        for hi in range(lo+1,9):
            lhs=sum((mean_prod(i,j,ps) for i in range(lo,hi) for j in range(lo,hi)),Fraction(0))
            rhs=(hi-lo)+2*(hi-lo)*sum((rho**Fraction(1<<(t.bit_count()-1)) if t else Fraction(1) for t in range(lo,hi)),Fraction(0))
            check(lhs<=rhs,('interval',lo,hi))

# The parity Pascal transform has triangular inverse over GF(2).
for coeff in product((0,1),repeat=7):
    transformed=[sum(coeff[k] for k in downmask(s))%2 for s in range(7)]
    reconstructed=[]
    for s in range(7):
        reconstructed.append((transformed[s]-sum(reconstructed[k] for k in downmask(s) if k<s))%2)
    check(reconstructed==list(coeff), ('inverse',coeff))

print('PASS',assertions,'exact Lucas, submask, product-moment, interval and inverse assertions')
