"""Independent finite checks for binary complement-insertion descendant theorem.
Run: python verify.py (Python >= 3.9; standard library only).
"""
from itertools import product
from math import comb

def initial_run(w):
    return next((i for i, a in enumerate(w) if a != w[0]), len(w))

def is_subsequence(x, y):
    k = 0
    for c in y:
        if k < len(x) and x[k] == c:
            k += 1
    return k == len(x)

def criterion(x, y):
    return y[0] == x[0] and initial_run(y) <= initial_run(x) and is_subsequence(x,y)

def successors(w):
    return {w[:i+1] + ('1' if w[i]=='0' else '0') + w[i+1:] for i in range(len(w))}

def formula(n, r, t):
    return sum(comb(n+t-1, i) for i in range(t+1)) - sum(comb(n+t-r-1, i) for i in range(t))

def allwords(n):
    return [''.join(w) for w in product('01',repeat=n)]

cases=0; checked_targets=0; checked_lemma=0
for n in range(1,9):
    seeds=allwords(n)
    for x in seeds:
        actual={x}
        for t in range(0,5):
            N=n+t
            predicted={y for y in allwords(N) if criterion(x,y)}
            assert actual==predicted,(x,t,sorted(actual-predicted)[:2],sorted(predicted-actual)[:2])
            assert len(actual)==formula(n,initial_run(x),t),(x,t,len(actual))
            cases+=1;checked_targets+=2**N
            if t<4: actual=set.union(*(successors(y) for y in actual))
print('RC1_DESCENDANTS_PASS', 'seed_radius_cases='+str(cases),'candidate_targets='+str(checked_targets),'n=1..8','t=0..4')

# Verify that an admissible supersequence always permits one inverse legal step
# retaining the required original subsequence and initial-run inequality.
for N in range(2,11):
    for y in allwords(N):
        for n in range(1,N):
            for x in allwords(n):
                if criterion(x,y):
                    possible=any(criterion(x, y[:j]+y[j+1:]) for j in range(1,N) if y[j]!=y[j-1])
                    assert possible,(x,y)
                    checked_lemma+=1
print('RC1_INVERSE_LEMMA_PASS','admissible_pairs='+str(checked_lemma),'target_lengths=2..10')
