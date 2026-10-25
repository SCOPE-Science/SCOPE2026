#!/usr/bin/env python3
"""Exact finite-dimensional Ehrhart coefficient certificate for two hypersimplex sums.

Requires only Python 3's standard library. The positive-composition formula
is proved in RESULT.md; the independent dynamic program checks integer counts.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from hashlib import sha256
from pathlib import Path
import csv

@lru_cache(maxsize=None)
def bounded_compositions(t, s, a):
    """Number of ordered a-tuples in {1,...,t} whose sum is s."""
    if a == 0:
        return int(s == 0)
    if s < a or s > a * t:
        return 0
    return sum((-1) ** j * comb(a, j) * comb(s - j*t - 1, a-1)
               for j in range(a+1) if s - j*t - 1 >= a-1)


def count_by_compositions(n, k, r, t):
    """Lattice points of t*(Delta(k,n)+Delta(n-r,n)), n>=k+r."""
    if t == 0:
        return 1
    total = 0
    for positive_sum in range(k*t+1):
        negative_sum = positive_sum + (r-k)*t
        if not (0 <= negative_sum <= r*t):
            continue
        for a in range(min(n,positive_sum)+1):
            A = bounded_compositions(t,positive_sum,a)
            if not A:
                continue
            for b in range(min(n-a,negative_sum)+1):
                B = bounded_compositions(t,negative_sum,b)
                if B:
                    total += comb(n,a)*comb(n-a,b)*A*B
    return total


def binomial_to_power(values):
    """Exact coefficients of unique degree<=len(values)-1 interpolant."""
    differences = list(values)
    differences_at_zero = []
    while differences:
        differences_at_zero.append(differences[0])
        differences = [b-a for a,b in zip(differences,differences[1:])]
    degree = len(differences_at_zero)-1
    result = [Fraction(0)]*(degree+1)
    falling_coeffs = [1]       # polynomial (t)_0
    for j, value in enumerate(differences_at_zero):
        for i,c in enumerate(falling_coeffs):
            result[i] += Fraction(value*c, factorial(j))
        new_coeffs = [0]*(len(falling_coeffs)+1)
        for i,c in enumerate(falling_coeffs):
            new_coeffs[i] -= j*c
            new_coeffs[i+1] += c
        falling_coeffs = new_coeffs
    return result


def count_by_independent_dp(n,k,r,t):
    """Enumerate integer coordinates independently, with no compositions."""
    table = {(0,0):1} # (coordinate sum, positive part sum)
    for _ in range(n):
        nxt = {}
        for (s,a), multiplicity in table.items():
            for y in range(-t,t+1):
                A = a + max(y,0)
                if A > k*t:
                    continue
                key = (s+y,A)
                nxt[key] = nxt.get(key,0) + multiplicity
        table = nxt
    target = (k-r)*t
    return sum(v for (s,_),v in table.items() if s==target)


def cases(max_n=14):
    for n in range(2,max_n+1):
        for k in range(1,n//2+1):
            for r in range(k,n-k+1):
                yield n,k,r


def certify(output_csv=None):
    rows=[]
    negative=[]
    for n,k,r in cases():
        d=n-1
        counts=[count_by_compositions(n,k,r,t) for t in range(d+1)]
        coeff=binomial_to_power(counts)
        assert len(coeff)==n and coeff[0]==1 and coeff[-1]>0
        if n<=13:
            assert all(c>0 for c in coeff), (n,k,r,coeff)
        bad=[i for i,c in enumerate(coeff) if c<0]
        if bad:
            negative.append((n,k,r,tuple(bad),tuple(coeff[i] for i in bad)))
        # Certificate stores every exact coefficient, not merely its signs.
        rows.append((n,k,r,tuple(coeff)))
    expected={(14,3,5,(2,), (Fraction(-2743,118800),)),
              (14,3,7,(2,), (Fraction(-687323,79200),)),
              (14,4,4,(2,), (Fraction(-883961,29700),)),
              (14,4,6,(2,), (Fraction(-230425,2376),)),
              (14,5,5,(2,), (Fraction(-5523479,39600),))}
    assert set(negative)==expected, negative
    # Independent, coordinate-by-coordinate lattice enumeration checks.
    independent_checks = [(n,k,r,t) for n,k,r in cases(14)
                          for t in (1,2) if n>=4]
    independent_checks.extend((14,k,r,13) for k,r in
                              [(3,5),(3,7),(4,4),(4,6),(5,5)])
    for n,k,r,t in independent_checks:
        a=count_by_compositions(n,k,r,t)
        b=count_by_independent_dp(n,k,r,t)
        assert a==b,(n,k,r,t,a,b)
    # Existing published 2026 example is an independent benchmark.
    published = next(c for n,k,r,c in rows if (n,k,r)==(14,3,7))
    assert published[2]==Fraction(-687323,79200)
    if output_csv is not None:
        with open(output_csv,'w',newline='',encoding='utf-8') as f:
            w=csv.writer(f,lineterminator='\n')
            w.writerow(['ambient_n','rank_k','complement_rank_r']+
                       ['coefficient_t'+str(i) for i in range(14)])
            for n,k,r,coeff in rows:
                w.writerow([n,k,r]+[str(v) for v in coeff]+['']*(14-len(coeff)))
        data=Path(output_csv).read_bytes()
        print('CERTIFICATE_SIZE',len(data),'SHA256',sha256(data).hexdigest())
    print('EXACT_OK: orbits=',len(rows),'low_dim_orbits=',
          sum(n<=13 for n,_,_,_ in rows),
          'ambient_14_orbits=',sum(n==14 for n,_,_,_ in rows),
          'negative_classes=',len(negative),
          'independent_counts=',len(independent_checks))
    print('NEGATIVE',[(n,k,r,list(degrees),list(map(str,values)))
                     for n,k,r,degrees,values in negative])

if __name__=='__main__':
    certify(Path(__file__).with_name('coefficients.csv'))
