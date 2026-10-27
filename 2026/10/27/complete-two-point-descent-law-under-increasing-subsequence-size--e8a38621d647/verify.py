"""Independent exact-arithmetic enumeration of increasing-subsequence-weighted descent moments.

Run: python verify.py
No external dependencies. This finite check supplements the general algebraic proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def formula(n, k):
    x = Fraction(k*(k-1), n*(n-1))
    p = (1-x)/2
    qa = (1-Fraction(k*(k-1)*(3*n-2*k-2), n*(n-1)*(n-2)))/6 if n>=3 else None
    y = Fraction(k*(k-1)*(k-2)*(k-3),n*(n-1)*(n-2)*(n-3)) if n>=4 else None
    qf = (1-2*x+y)/4 if n>=4 else None
    mean = Fraction(n-1)*p
    var = Fraction((n-k)*(n-k+1)*(3*k*k+2*k*n-3*k+n*n-n),12*n*n*(n-1))
    return p, qa, qf, mean, var


def check():
    assertions=0
    examined=0
    for n in range(2,9):
        subsets = {k:list(combinations(range(n),k)) for k in range(2,n+1)}
        d0={k:0 for k in subsets}
        one={k:[0]*(n-1) for k in subsets}
        pair={k:{(i,j):0 for i in range(n-1) for j in range(i+1,n-1)} for k in subsets}
        total_d={k:0 for k in subsets}
        total_d_sq={k:0 for k in subsets}
        for pi in permutations(range(n)):
            examined+=1
            di=[int(pi[i]>pi[i+1]) for i in range(n-1)]
            dt=sum(di)
            for k, sets in subsets.items():
                z=sum(all(pi[s[t]]<pi[s[t+1]] for t in range(k-1)) for s in sets)
                d0[k]+=z
                total_d[k]+=z*dt
                total_d_sq[k]+=z*dt*dt
                for i in range(n-1):one[k][i]+=z*di[i]
                for (i,j) in pair[k]:pair[k][(i,j)]+=z*di[i]*di[j]
        for k in subsets:
            expected_denom=comb(n,k)*factorial(n)//factorial(k)
            assert d0[k]==expected_denom, (n,k,'normalization')
            assertions+=1
            p,qa,qf,mean,var=formula(n,k)
            for i,v in enumerate(one[k]):
                assert Fraction(v,d0[k])==p,(n,k,i,'single')
                assertions+=1
            for (i,j),v in pair[k].items():
                expected=qa if j==i+1 else qf
                assert Fraction(v,d0[k])==expected,(n,k,i,j,'pair')
                assertions+=1
            assert Fraction(total_d[k],d0[k])==mean,(n,k,'mean')
            assertions+=1
            assert Fraction(total_d_sq[k],d0[k])-mean*mean==var,(n,k,'variance')
            assertions+=1
    # Exact strict long-range repulsion and positive variances away from k=n.
    for n in range(4,35):
        for k in range(2,n):
            p,qa,qf,mean,var=formula(n,k)
            assert qf-p*p < 0,(n,k,'repulsion')
            assertions+=1
            assert var>0,(n,k,'variance positivity')
            assertions+=1
    print(f'PASS: {examined} permutations enumerated across n=2..8; {assertions} exact-rational assertions.')


if __name__=='__main__':
    check()
