#!/usr/bin/env python3
"""Exact integer verification for square-marked commutative 3-nilpotent semigroups.
No external dependencies.  Run: python verify.py
"""
from math import comb
from itertools import product


def formula_profile(n):
    assert n >= 3
    result = [0] * (n - 1)
    for m in range(1, n - 1):
        k = n - 1 - m
        off = comb(m, 2)
        multiplicity = n * comb(n - 1, m)
        for j in range(k + 1):
            c = (-1)**j * comb(k, j) * (k + 1 - j)**off
            for s in range(m + 1):
                result[s] += multiplicity * c * comb(m, s) * (k - j)**s
    assert all(z >= 0 for z in result)
    return result


def brute_profile_stratum(m, k):
    """Enumerate tables directly; no inclusion-exclusion or generating formula."""
    pairs = [(a,b) for a in range(m) for b in range(a,m)]
    diag = [j for j,(a,b) in enumerate(pairs) if a == b]
    answers = [0] * (m + 1)
    for values in product(range(k + 1), repeat=len(pairs)):
        if not all(color in values for color in range(1, k + 1)):
            continue
        s = sum(values[j] != 0 for j in diag)
        answers[s] += 1
    return answers


def predicted_stratum(m, k):
    result = [0] * (m + 1)
    for j in range(k + 1):
        c = (-1)**j * comb(k,j) * (k + 1 - j)**comb(m,2)
        for s in range(m + 1):
            result[s] += c * comb(m,s) * (k-j)**s
    return result


def main():
    tested = 0
    for n in range(3, 8):
        brute = [0]*(n-1)
        for m in range(1,n-1):
            k = n-1-m
            if (k+1)**comb(m+1,2) > 100000:
                raise RuntimeError('Unexpected workload in bounded check')
            by_enum = brute_profile_stratum(m,k)
            assert by_enum == predicted_stratum(m,k), (m,k,by_enum,predicted_stratum(m,k))
            for s,value in enumerate(by_enum):
                brute[s] += n * comb(n-1,m) * value
            tested += 1
        assert brute == formula_profile(n), (n,brute,formula_profile(n))
    # Old literature totals are used only as known independent benchmarks,
    # not as evidence that the refined formula was already reported.
    literature_totals={3:6,4:84,5:1620,6:67170,7:7655424,
                       8:2762847752,9:3177531099864,
                       10:11942816968513350,
                       11:170387990514807763280}
    for n,known in literature_totals.items():
        assert sum(formula_profile(n))==known, (n,sum(formula_profile(n)),known)
    expected_bad={3:0,4:12,5:140,6:2610,7:107016,
                  8:11999288,9:4193269416,10:4661707146390}
    for n,b in expected_bad.items():
        assert formula_profile(n)[0]==b
    # Direct inequality from the proof: in every stratum having no-square
    # examples, all nonzero labels must occur off the diagonal.
    for n in range(4,80):
        for m in range(1,n-1):
            k=n-m-1
            if k>comb(m,2):
                continue
            if k<n/2:
                assert m>(n-2)/2
            else:
                assert m>n**0.5
    print('VERIFY_OK: brute symmetric multiplication tables for %d (m,k) strata, n=3..7;'
          ' exact total benchmarks n=3..11; refined and asymptotic boundary checks' % tested)
    for n in range(3,11):
        p=formula_profile(n)
        print('n=%d: nonfinite=%d, finite=%d, total=%d' % (n,p[0],sum(p[1:]),sum(p)))

if __name__=='__main__':
    main()

# ---- Unlabelled isomorphism-class refinement (Burnside, exact fractions) ----
from collections import Counter
from fractions import Fraction
from itertools import permutations


def partitions(t, maxpart=None):
    if t == 0:
        yield ()
        return
    if maxpart is None:
        maxpart=t
    for v in range(min(t,maxpart),0,-1):
        for tail in partitions(t-v,v):
            yield (v,)+tail


def cycle_permutation(part):
    out=list(range(sum(part)));start=0
    for length in part:
        for i in range(length):
            out[start+i]=start+(i+1)%length
        start+=length
    return tuple(out)


def centralizer_factor(part):
    from math import factorial
    out=1
    for j,multiplicity in Counter(part).items():
        out*=j**multiplicity*factorial(multiplicity)
    return out


def induced_orbits(pi):
    m=len(pi)
    visited=set();d=[];o=[]
    for first in range(m):
        for second in range(first,m):
            pair=(first,second)
            if pair in visited:continue
            L=0;cur=pair
            while cur not in visited:
                visited.add(cur);L+=1
                cur=tuple(sorted((pi[cur[0]],pi[cur[1]])))
            (d if first==second else o).append(L)
    return d,o


def mul_factor(poly,coefficient,degree):
    out=[0]*(len(poly)+degree)
    for i,x in enumerate(poly):
        out[i]+=x;out[i+degree]+=coefficient*x
    return out


def burnside_fixed_profile(lam,mu):
    diag,off=induced_orbits(cycle_permutation(lam))
    from itertools import product as choices
    out=[0]*(sum(lam)+1)
    for omitted in choices((0,1),repeat=len(mu)):
        active=[v for v,is_omitted in zip(mu,omitted) if not is_omitted]
        multiplier=(-1)**sum(omitted)
        def fixed_nonzero(length):
            return sum(v for v in active if length%v==0)
        constant=1
        for length in off:constant*=1+fixed_nonzero(length)
        poly=[constant]
        for length in diag:
            poly=mul_factor(poly,fixed_nonzero(length),length)
        for s,number in enumerate(poly):out[s]+=multiplier*number
    return out


def isomorphism_profile(n):
    out=[Fraction(0)]*(n-1)
    for m in range(1,n-1):
        k=n-m-1
        for lam in partitions(m):
            for mu in partitions(k):
                coef=Fraction(1,centralizer_factor(lam)*centralizer_factor(mu))
                for s,num in enumerate(burnside_fixed_profile(lam,mu)):
                    out[s]+=coef*num
    assert all(u.denominator==1 and u>=0 for u in out)
    return [int(u) for u in out]


def brute_isomorphism_profile(n):
    out=[0]*(n-1)
    for m in range(1,n-1):
        k=n-1-m
        pairs=[(a,b) for a in range(m) for b in range(a,m)]
        index={p:i for i,p in enumerate(pairs)}
        diag=[index[(a,a)] for a in range(m)]
        group=[]
        for pi in permutations(range(m)):
            target=[index[tuple(sorted((pi[a],pi[b])))] for a,b in pairs]
            for sigma in permutations(range(1,k+1)):
                group.append((target,(0,)+sigma))
        seen=set()
        for values in product(range(k+1),repeat=len(pairs)):
            if not all(u in values for u in range(1,k+1)) or values in seen:
                continue
            orbit=[]
            for target,sigma in group:
                new=[0]*len(values)
                for old_index,new_index in enumerate(target):
                    new[new_index]=sigma[values[old_index]]
                orbit.append(tuple(new))
            seen.update(orbit)
            s=sum(values[i]!=0 for i in diag)
            out[s]+=1
    return out


def isomorphism_checks():
    for n in range(3,7):
        p=isomorphism_profile(n)
        direct=brute_isomorphism_profile(n)
        assert p==direct,(n,p,direct)
    published={3:1,4:5,5:23,6:155,7:2106,8:79997,9:9350240}
    for n,total in published.items():
        assert sum(isomorphism_profile(n))==total,(n,iso_profile(n),total)
    print('VERIFY_OK: Burnside isomorphism refinement equals direct orbit enumeration n=3..6; published totals n=3..9')
    for n in range(3,9):
        print('n=%d unlabelled: nonfinite=%d, finite=%d, total=%d'%
              (n,isomorphism_profile(n)[0],sum(isomorphism_profile(n)[1:]),sum(isomorphism_profile(n))))

if __name__=='__main__':
    isomorphism_checks()
