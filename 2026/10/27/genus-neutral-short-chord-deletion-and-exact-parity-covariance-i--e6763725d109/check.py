#!/usr/bin/env python3
"""Exact independent enumeration of short chords and orientable genus in cyclic perfect matchings."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial

def matchings(v):
    if not v:
        yield ()
    else:
        a=v[0]
        for j in range(1,len(v)):
            b=v[j]
            for rest in matchings(v[1:j]+v[j+1:]):
                yield ((a,b),)+rest

def double_fact(n):
    if n<=0:return 1
    out=1
    for a in range(1,n+1,2):out*=a
    return out

def genus(m,n):
    pairing=list(range(2*n))
    for a,b in m:pairing[a]=b;pairing[b]=a
    # boundary successor multiplied by chord involution; number of cycles F = n+1-2g
    seen=set(); faces=0
    for a in range(2*n):
        if a not in seen:
            faces+=1;j=a
            while j not in seen:
                seen.add(j);j=(pairing[j]+1)%(2*n)
    assert (n+1-faces)%2==0
    return (n+1-faces)//2

def short(m,n):
    return sum((a-b)%(2*n) in (1,2*n-1) for a,b in m)

def acyc_count(n,k):
    if k==0:return 1
    return 2*n*comb(2*n-k,k)//(2*n-k)

def main():
    assertions=0
    for n in range(2,8):
        counts=Counter((genus(m,n),short(m,n)) for m in matchings(tuple(range(2*n))))
        assert sum(counts.values())==double_fact(2*n-1);assertions+=1
        counts_g=Counter()
        for (g,s),num in counts.items():counts_g[g]+=num
        # direct positive coefficient equality via exact polynomial-in-s for each genus
        for g in range(n//2+1):
            for s in range(n+1):
                rhs=0
                for k in range(s,n+1):
                    # coefficient expansion: genus-g residual count times falling number
                    val=counts_by_n[n-k][g] if n-k in counts_by_n else None
                    if val is None:
                        val=Counter(genus(m,n-k) for m in matchings(tuple(range(2*(n-k)))))[g] if n-k else (1 if g==0 else 0)
                    rhs+=acyc_count(n,k)*(-1)**(k-s)*comb(k,s)*val
                assert counts[g,s]==rhs, (n,g,s,counts[g,s],rhs);assertions+=1
        T=double_fact(2*n-1)
        EX=Fraction(sum(s*v for (g,s),v in counts.items()),T)
        EG=Fraction(sum(g*v for (g,s),v in counts.items()),T)
        EXG=Fraction(sum(s*g*v for (g,s),v in counts.items()),T)
        assert EX==Fraction(2*n,2*n-1);assertions+=1
        cov=EXG-EX*EG
        expect=-Fraction(n*n,(2*n-1)*(n+1)) if n%2==0 else -Fraction(n-1,2*n-1)
        assert cov==expect,(n,cov,expect);assertions+=1
        print('n',n,'matchings',T,'genus_counts',dict(counts_g),'Cov',cov,'short distribution',dict(sorted(Counter({s:sum(v for (g,t),v in counts.items() if s==t) for s in range(n+1)}).items())))
    print('PASS',assertions,'exact assertions')

# independent recursive genus tables via direct enumeration; no reference to polynomial recurrence
counts_by_n={0:Counter({0:1})}
for m in range(1,8):
    counts_by_n[m]=Counter(genus(p,m) for p in matchings(tuple(range(2*m))))
if __name__=='__main__':main()
