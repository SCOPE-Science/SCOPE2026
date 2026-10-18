"""Exact, independent checks for signed-total-Roman labellings of crown graphs.

Run with: python VERIFY.py
Uses Python's standard library only.  A graph-neighborhood enumerator is
compared with a separate nine-type multinomial enumerator and a closed
formula for the minimum-weight coefficient.
"""
from collections import Counter
from itertools import product
from math import comb, factorial

LABELS = (-1, 1, 2)
TYPES = tuple(product(LABELS, repeat=2))


def direct_counts(n):
    # Explicit physical graph, with vertices A_0,...,A_{n-1},B_0,...,B_{n-1}.
    neighbors = [tuple(n + j for j in range(n) if j != i)
                 for i in range(n)]
    neighbors += [tuple(i for i in range(n) if i != j)
                  for j in range(n)]
    out = Counter()
    for labelling in product(LABELS, repeat=2*n):
        if any(sum(labelling[j] for j in neighbors[v]) < 1
               for v in range(2*n)):
            continue
        if any(labelling[v] == -1 and not any(
                labelling[j] == 2 for j in neighbors[v])
               for v in range(2*n)):
            continue
        out[sum(labelling)] += 1
    return out


def compositions(total, k):
    if k == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, k - 1):
                yield (first,) + tail


def coefficient_formula_counts(n):
    out = Counter()
    nf = factorial(n)
    for quantities in compositions(n, 9):
        sa = sum(quantities[i]*a for i, (a,b) in enumerate(TYPES))
        sb = sum(quantities[i]*b for i, (a,b) in enumerate(TYPES))
        ma = max(a for i, (a,b) in enumerate(TYPES) if quantities[i])
        mb = max(b for i, (a,b) in enumerate(TYPES) if quantities[i])
        if sa < 1 + ma or sb < 1 + mb:
            continue
        ta = sum(quantities[i] for i, (a,b) in enumerate(TYPES) if a==2)
        tb = sum(quantities[i] for i, (a,b) in enumerate(TYPES) if b==2)
        qa = sum(quantities[i] for i, (a,b) in enumerate(TYPES) if a==-1)
        qb = sum(quantities[i] for i, (a,b) in enumerate(TYPES) if b==-1)
        n_m2 = quantities[TYPES.index((-1,2))]
        n_2m = quantities[TYPES.index((2,-1))]
        if ta == 0 and qb or tb == 0 and qa:
            continue
        if ta == 1 and n_2m or tb == 1 and n_m2:
            continue
        denom = 1
        for c in quantities: denom *= factorial(c)
        out[sa+sb] += nf // denom
    return out


def positive_side_weight_three(n):
    # Enumerate one-side assignments with at least one 2, total weight 3;
    # return (total assignments, total occurrences of -1, unique-2 count).
    all_count = neg_occ = one_two_count = 0
    for t in range(1,n+1):
        if (n+3-3*t)%2: continue
        u = (n+3-3*t)//2
        v = n-t-u
        if u<0 or v<0: continue
        q = comb(n,t)*comb(n-t,u)
        all_count += q
        neg_occ += q*v
        if t == 1: one_two_count = q
    return all_count,neg_occ//n,one_two_count


def predicted_minimum_count(n):
    if n == 2: return 4, 1
    if n == 3: return 6, 10
    t,d,u = positive_side_weight_three(n)
    if n%2:
        return 6,t*t
    intersection = n*(n-1)*comb(n-2,n//2-2)**2
    return 6,t*t-2*u*d+intersection


def run():
    for n in range(2,8):
        explicit=direct_counts(n)
        formula=coefficient_formula_counts(n)
        assert explicit == formula, (n, explicit, formula)
        pred=predicted_minimum_count(n)
        found=(min(explicit), explicit[min(explicit)])
        assert found==pred, (n,found,pred)
        print('n=%s, gamma=%s, minimum functions=%s, coefficients=%s: PASS'
              % (n,*pred,len(explicit)))
    print('All six independent polynomial and minimum-count comparisons PASS.')


if __name__ == '__main__':
    run()
