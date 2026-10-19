"""Standalone exact verification for directed-cycle/score-histogram covariances.

Enumerates each oriented complete graph through six vertices. It checks the
closed covariance formulas by integer cross-multiplication, without sampling.
"""
from itertools import combinations, permutations
from collections import defaultdict
from math import comb, factorial
from fractions import Fraction

def falling(x,r):
    z=1
    for t in range(r):z*=x-t
    return z

def mass(b,t):
    return Fraction(comb(b,t),2**b) if 0<=t<=b else Fraction(0)

def inspect(n):
    pairs=list(combinations(range(n),2))
    idx={edge:j for j,edge in enumerate(pairs)}
    cycle_tests={}
    for ell in range(3,n+1):
        checks=[]
        for subset in combinations(range(n),ell):
            base=subset[0]
            for rest in permutations(subset[1:]):
                seq=(base,*rest,base)
                all_bits=0;bits_positive=0
                for u,v in zip(seq,seq[1:]):
                    j=idx[min(u,v),max(u,v)]
                    all_bits|=1<<j
                    if u<v:bits_positive|=1<<j
                checks.append((all_bits,bits_positive))
        cycle_tests[ell]=checks
    totals={ell:[0,0] for ell in cycle_tests}
    sumsN=[0]*(n)
    sumsCN={ell:[0]*(n) for ell in cycle_tests}
    count=1<<len(pairs)
    for mask in range(count):
        degree=[0]*n
        for j,(a,b) in enumerate(pairs):
            if (mask>>j)&1:degree[a]+=1
            else:degree[b]+=1
        hist=[degree.count(d) for d in range(n)]
        for d in range(n):sumsN[d]+=hist[d]
        for ell,checks in cycle_tests.items():
            c=sum((mask&ab)==yes for ab,yes in checks)
            totals[ell][0]+=c
            for d in range(n):sumsCN[ell][d]+=c*hist[d]
    checks_done=0
    m=n-1
    for ell in cycle_tests:
        a=Fraction(falling(m-2,ell-3),2**(ell-2))
        for d in range(n):
            cov=Fraction(sumsCN[ell][d],count)-Fraction(totals[ell][0]*sumsN[d],count**2)
            expected=n*a*mass(m,d)*(d*(m-d)-Fraction(m*(m-1),4))
            assert cov==expected,(n,ell,d,cov,expected)
            checks_done+=1
        for k in range(1,n):
            cov=sum((Fraction(sumsCN[ell][d],count)-Fraction(totals[ell][0]*sumsN[d],count**2)) for d in range(k,n))
            expected=Fraction(n*m*(m-1)*falling(m-2,ell-3),2**(ell+2))*(mass(m-2,k-1)-mass(m-2,k-2))
            assert cov==expected,(n,ell,k,cov,expected)
            checks_done+=1
    print(f'n={n}; tournaments={count}; directed-cycle tests={sum(map(len,cycle_tests.values()))}; exact covariance cases={checks_done}')
    return checks_done

if __name__=='__main__':
    done=sum(inspect(n) for n in range(3,7))
    # Finite-range logical check of threshold signs, centered exact-score signs.
    more=0
    for n in range(3,301):
        m=n-1
        for k in range(1,n):
            a=mass(m-2,k-1)-mass(m-2,k-2)
            expected_sign=1 if 2*k<n else (-1 if 2*k>n else 0)
            assert (a>0)-(a<0)==expected_sign
            more+=1
        for d in range(n):
            expr=4*d*(m-d)-m*(m-1)
            expected_sign=(m-(2*d-m)**2>0)-(m-(2*d-m)**2<0)
            assert (expr>0)-(expr<0)==expected_sign
            more+=1
    print('verified exact enumeration cases:',done,'finite sign comparisons:',more)
