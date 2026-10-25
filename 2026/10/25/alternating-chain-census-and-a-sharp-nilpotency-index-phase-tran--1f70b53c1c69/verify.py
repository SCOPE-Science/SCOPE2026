"""Reproduce exact nilpotent rank/index counts for bipartite partial isometries.

Uses direct enumeration and an independently evaluated truncated labelled
component exponential, without external dependencies.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def all_partial_injections(n):
    for k in range(n + 1):
        for D in combinations(range(n), k):
            for I in permutations(range(n), k):
                arr = [-1] * n
                for d, i in zip(D, I):
                    arr[d] = i
                yield tuple(arr)


def preserves_bipartite_distance(f, a):
    n = len(f)
    for i in range(n):
        if f[i] == -1:
            continue
        for j in range(i):
            if f[j] != -1 and ((i < a) == (j < a)) != ((f[i] < a) == (f[j] < a)):
                return False
    return True


def nilpotency_index(f):
    n = len(f)
    top = 1
    for i in range(n):
        v = i
        seen = set()
        count = 0
        while v != -1:
            if v in seen:
                return 0
            seen.add(v)
            count += 1
            v = f[v]
        top = max(top, count)
    return top


def brute(a, b):
    counts = Counter()
    for f in all_partial_injections(a + b):
        if not preserves_bipartite_distance(f, a):
            continue
        j = nilpotency_index(f)
        if j:
            counts[(sum(z != -1 for z in f), j)] += 1
    return counts


def components(a, b, ell, orientation):
    terms = Counter()
    if orientation == 'preserving':
        for j in range(1, ell + 1):
            if j <= a:
                terms[(j, 0, j - 1)] += 1
            if j <= b:
                terms[(0, j, j - 1)] += 1
    else:
        for r in range((ell - 1)//2 + 1):
            if 2*r + 1 <= ell:
                if r + 1 <= a and r <= b:
                    terms[(r + 1, r, 2*r)] += 1
                if r <= a and r + 1 <= b:
                    terms[(r, r + 1, 2*r)] += 1
        for r in range(1, ell//2 + 1):
            if r <= min(a,b):
                terms[(r, r, 2*r-1)] += 2
    return terms


def truncated_exp_coeff(a, b, ell, orientation):
    """Return rank counts for component assemblies, nilpotency index <= ell."""
    c = components(a, b, ell, orientation)
    power = {(0, 0, 0): 1}
    total = {(0, 0, 0): Fraction(1)}
    for k in range(1, a+b+1):
        new = Counter()
        for (i,j,r),v in power.items():
            for (di,dj,dr),w in c.items():
                if i+di <= a and j+dj <= b:
                    new[(i+di,j+dj,r+dr)] += v*w
        if not new:
            break
        power = new
        for key, v in power.items():
            total[key] = total.get(key, Fraction(0)) + Fraction(v, factorial(k))
    out = Counter()
    for (i,j,r),v in total.items():
        if i == a and j == b:
            q = v*factorial(a)*factorial(b)
            assert q.denominator == 1
            out[r] += int(q)
    return out


def predicted(a,b):
    out = Counter()
    previous = Counter()
    for ell in range(1, a+b+1):
        current = truncated_exp_coeff(a,b,ell,'preserving') + truncated_exp_coeff(a,b,ell,'swapping')
        current[0] -= 1
        for r in current:
            x = current[r]-previous[r]
            if x:
                out[(r,ell)] = x
        previous = current
    return out


def total_one_color_nilpotents(n):
    return sum(1 for f in all_partial_injections(n) if nilpotency_index(f))


def sharp_phase(a,b):
    if a < b:
        a,b=b,a
    if a == b:
        return 2*b, 2*factorial(b)**2
    if a < 2*b+1:
        return 2*b+1, factorial(a)*factorial(b)//factorial(a-b-1)
    if a == 2*b+1:
        return a, factorial(a)*(total_one_color_nilpotents(b)+1)
    return a, factorial(a)*total_one_color_nilpotents(b)


def run():
    tested=0
    for a in range(1,5):
        for b in range(1,5):
            if a+b > 7:
                continue
            direct=brute(a,b)
            formula=predicted(a,b)
            assert direct==formula, (a,b,direct-formula,formula-direct)
            top,count=sharp_phase(a,b)
            top_actual=max(j for _,j in direct)
            count_actual=sum(n for (_,j),n in direct.items() if j==top_actual)
            assert (top,count)==(top_actual,count_actual),(a,b,top,count,top_actual,count_actual)
            tested+=1
    print('VERIFY_OK',tested,'complete bipartite graph sizes; every rank/index cell and maximal-chain count')

if __name__ == '__main__':
    run()
