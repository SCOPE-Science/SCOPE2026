#!/usr/bin/env python3
"""Exhaustive independent check of an alternating-word complement theorem.
Only Python standard library is needed.
"""
from itertools import combinations, product
from math import comb

def outputs_from_embeddings(n, k):
    w = 'ab' * n
    u = 'ab' * k
    seen = set()
    for indices in combinations(range(2*n), 2*k):
        if ''.join(w[i] for i in indices) != u:
            continue
        selected = set(indices)
        seen.add(''.join(ch for i,ch in enumerate(w) if i not in selected))
    return seen

def predicted_outputs(n, k):
    r = n-k
    seen = set()
    for z in product((0,1), repeat=r):
        runs = sum(x==1 and (i==0 or z[i-1]==0) for i,x in enumerate(z))
        if runs <= k:
            seen.add(''.join(('ab','ba')[x] for x in z))
    return seen

nchecks=0; total_outputs=0
for n in range(0,11):
    for k in range(0,n+1):
        observed = outputs_from_embeddings(n,k)
        predicted = predicted_outputs(n,k)
        r=n-k
        count=sum(comb(r+1,2*j) for j in range(0,k+1) if 2*j <= r+1)
        assert observed == predicted, (n,k,len(observed),len(predicted),next(iter(observed^predicted)))
        assert len(observed)==count,(n,k,len(observed),count)
        nchecks += 1
        total_outputs+=len(observed)
print(f'PASS n=0..10, all 66 parameter pairs; {nchecks} complete set equalities; {total_outputs} summed distinct residuals')
print('count table n=1..10, k increasing:')
for n in range(1,11):
    print(f'n={n}: '+','.join(str(len(predicted_outputs(n,k))) for k in range(n+1)))
