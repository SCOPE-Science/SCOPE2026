#!/usr/bin/env python3
"""Standalone checks for competitive irreversible monomer/dimer adsorption.
Only Python standard-library modules are required. These checks do not certify
an infinite-size limit; the analytical coupling is supplied separately.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, exp, factorial, log, sqrt


def count_law(n, mu):
    """Exact scalar recursion; outputs probabilities indexed by monomer count."""
    zero = [Fraction(1)]
    one = [Fraction(0), Fraction(1)]
    if n == 0: return zero
    if n == 1: return one
    a, b = zero, one
    for k in range(2, n+1):
        q = 2*mu / (k-1+2*mu)
        now = [Fraction(0)]*(k+1)
        for m, p in enumerate(a): now[m] += (1-q)*p
        for m, p in enumerate(b): now[m+1] += q*p
        a, b = b, now
    return b


def full_label_law(n, mu):
    """Independent state-space recursion tracking each monomer label subset."""
    @lru_cache(None)
    def solve(vacant):
        k = vacant.bit_count()
        if k == 0: return {0: Fraction(1)}
        if k == 1: return {vacant: Fraction(1)}
        sites = [i for i in range(n) if vacant & (1<<i)]
        tot = k*mu + Fraction(k*(k-1),2)
        ans = {}
        for i in sites:
            for M, p in solve(vacant ^ (1<<i)).items():
                out = M | (1<<i)
                ans[out] = ans.get(out, Fraction(0)) + p*mu/tot
        for a in range(len(sites)):
            for b in range(a+1,len(sites)):
                rest = vacant ^ (1<<sites[a]) ^ (1<<sites[b])
                for M, p in solve(rest).items():
                    ans[M] = ans.get(M, Fraction(0)) + p/tot
        return ans
    return solve((1<<n)-1)


def approximate_law(n, mu, trunc=25):
    """Floating scalar recursion for much larger finite systems."""
    a = [0.0]*(trunc+1); b = a.copy()
    a[0]=1.0; b[1]=1.0
    for k in range(2,n+1):
        q = 2*mu/(k-1+2*mu)
        now = [(1-q)*v for v in a]
        for j in range(trunc): now[j+1]+=q*b[j]
        a,b=b,now
    return b


def rounded_poisson(n, lam, trunc=25):
    probs = [0.0]*(trunc+1)
    for j in range(trunc+1):
        out = j + ((n-j)%2)
        if out<=trunc:
            probs[out]+=exp(-lam)*lam**j/factorial(j)
    return probs


def main():
    count=0
    for n in range(2,9):
        for mu in (Fraction(1,4), Fraction(2,3)):
            a = count_law(n,mu)
            b = full_label_law(n,mu)
            assert sum(b.values()) == 1
            assert sum(a) == 1
            for m in range(n+1):
                expected = a[m]
                observed = sum(prob for mask,prob in b.items() if mask.bit_count()==m)
                assert expected == observed, (n,mu,m,expected,observed)
                assert (m-n)%2==0 or expected==0
                if expected:
                    per_subset=expected/comb(n,m)
                    for mask,prob in b.items():
                        if mask.bit_count()==m:
                            assert prob==per_subset, (n,mu,m,mask)
                count+=3
    # Even-system no-monomer probability: finite exact product of dimer choices.
    for n in (2,4,6,8,10,12):
        mu=Fraction(1,7)
        product=Fraction(1)
        for k in range(n,0,-2): product *= Fraction(k-1,1)/(k-1+2*mu)
        assert count_law(n,mu)[0]==product
        count+=1
    # Distribution comparison checks are numerical finite-N checks only.
    for c in (0.4,1.2):
        for n in (2000,2001,10000,10001,100000,100001):
            mu=c/log(n)
            actual=approximate_law(n,mu)
            expected=rounded_poisson(n,c)
            tv=sum(abs(x-y) for x,y in zip(actual,expected))/2
            assert tv < 0.20, (c,n,tv)
            assert abs(sum(actual)-1)<1e-8
            assert all(actual[k]<1e-9 for k in range(len(actual)) if (k-n)%2)
            count+=3
    print(f"PASS: {count} exact/numerical assertions across finite graph and large-N tests")
    print("No numerical experiment was used to prove the infinite-system theorem.")

if __name__=='__main__': main()
