"""Finite reproducibility checks for heterogeneous-impurity dimer adsorption.

The limiting theorem is proved analytically; finite checks only test its transition
rules, exact two-impurity identity, and numerical consistency.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, product
from math import exp, log


def reduced_law(n, rates):
    r = len(rates)
    full = (1 << r) - 1

    @lru_cache(None)
    def go(k, defect_mask):
        total = Fraction(k * (k - 1), 2) + k * sum(
            (rates[i] for i in range(r) if defect_mask & (1 << i)), 0)
        if total == 0:
            return {(defect_mask, k): Fraction(1)}
        ans = {}
        if k >= 2:
            for state, p in go(k - 2, defect_mask).items():
                ans[state] = ans.get(state, 0) + p * Fraction(k * (k - 1), 2) / total
        for i in range(r):
            if defect_mask & (1 << i):
                for state, p in go(k - 1, defect_mask ^ (1 << i)).items():
                    ans[state] = ans.get(state, 0) + p * rates[i] * k / total
        return ans
    return go(n - r, full)


def labeled_law(n, rates):
    r = len(rates)
    edges = []
    for a, b in combinations(range(n), 2):
        if a < r and b < r:
            continue
        weight = rates[a] if a < r else (rates[b] if b < r else Fraction(1))
        edges.append((a, b, weight))

    @lru_cache(None)
    def go(alive):
        available = [(a, b, w) for a, b, w in edges
                     if (alive >> a) & 1 and (alive >> b) & 1]
        total = sum((w for _, _, w in available), Fraction(0))
        if total == 0:
            dmask = alive & ((1 << r) - 1)
            normal = (alive >> r).bit_count()
            return {(dmask, normal): Fraction(1)}
        result = {}
        for a, b, w in available:
            for state, p in go(alive & ~(1 << a) & ~(1 << b)).items():
                result[state] = result.get(state, 0) + p * w / total
        return result
    return go((1 << n) - 1)


def numeric_law(n, rates):
    r = len(rates)
    states = {n-r: {(1 << r)-1: 1.0}}
    out = {}
    for k in range(n-r, -1, -1):
        for mask, prob in states.get(k, {}).items():
            remaining = [i for i in range(r) if mask & (1 << i)]
            total = k*(k-1)/2 + k*sum(rates[i] for i in remaining)
            if total == 0:
                out[(mask, k)] = out.get((mask, k), 0.0) + prob
                continue
            if k >= 2:
                d = states.setdefault(k-2, {})
                d[mask] = d.get(mask, 0.0)+prob*k*(k-1)/2/total
            for i in remaining:
                dest = mask ^ (1 << i)
                d = states.setdefault(k-1, {})
                d[dest] = d.get(dest, 0.0)+prob*rates[i]*k/total
    return out


def limiting_law(parity, c):
    r=len(c)
    out={}
    for bits in product((0,1), repeat=r):
        s=[i for i,b in enumerate(bits) if b]
        q=len(s)
        p=1.0
        for i,b in enumerate(bits):
            p *= exp(-c[i]) if b else 1-exp(-c[i])
        if (parity+q)%2 == 0:
            state=(sum(1 << i for i in s), 0)
            out[state]=out.get(state,0.0)+p
        elif q == 0:
            out[(0,1)]=out.get((0,1),0.0)+p
        else:
            total=sum(c[i] for i in s)
            for i in s:
                state=(sum(1 << j for j in s if j != i),0)
                out[state]=out.get(state,0.0)+p*c[i]/total
    return out


def check():
    exact_labeled=0
    products=0
    numeric=0
    for r in (2,3):
        rates=[Fraction(1,2),Fraction(3,4),Fraction(5,3)][:r]
        for n in range(r+2, min(r+8,11)):
            a=reduced_law(n, rates)
            b=labeled_law(n, rates)
            assert a == b,(n,r,a,b)
            assert sum(a.values()) == 1
            exact_labeled+=2
    for n in range(4,34,2):
        rates=[Fraction(2,5),Fraction(7,6)]
        a=reduced_law(n,rates)
        m=(n-2)//2
        product_value=Fraction(1)
        for j in range(1,m+1):
            product_value *= Fraction(2*j-1,1) / (2*j-1+2*sum(rates))
        assert a.get((3,0),0) == product_value,(n,a,product_value)
        assert all(mask.bit_count()+normal in (0,2) for mask,normal in a)
        products += 2
    for c in ([0.8,1.3], [0.3,1.1,1.7], [0.2,0.8,1.2,1.8]):
        for parity in (0,1):
            n=10000+parity
            actual=numeric_law(n,[x/log(n) for x in c])
            target=limiting_law(parity,c)
            tv=sum(abs(actual.get(x,0)-target.get(x,0))
                   for x in actual.keys() | target.keys())/2
            assert abs(sum(actual.values())-1)<1e-10
            assert abs(sum(target.values())-1)<1e-10
            assert tv < .1,(n,c,tv)
            numeric += 3
    print('PASS: labeled/reduced exact checks:',exact_labeled)
    print('PASS: exact two-defect product and support checks:',products)
    print('PASS: finite-size consistency checks:',numeric)
    print('Total assertions grouped:',exact_labeled+products+numeric)

if __name__ == '__main__':
    check()
