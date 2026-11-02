#!/usr/bin/env python3
"""Exact independent finite corroboration of two-representation coin thresholds."""
def f(t):
    return t // 3 + t % 3

def predicted(m, r):
    return (1 + f(m + r)) if r < 3 else (2 + f(r))

checked = 0
for m in range(4, 151):
    thresholds = [predicted(m, r) for r in range(m)]
    limit = (max(thresholds) + 3)*m+m
    count = [0]*(limit+1)
    count[0] = 1
    for coin in (m, m+1, m+3):
        for n in range(coin, limit+1):
            count[n] += count[n-coin]
    for r in range(m):
        t = thresholds[r]
        actual = next(q for q in range(limit // m) if count[q*m+r] >= 2)
        assert t == actual, (m,r,t,actual)
        for q in range(max(0,t-2),t+3):
            assert (count[q*m+r] >= 2) == (q >= t), (m,r,q)
        checked += 1
    h,a = divmod(m,3)
    max_from_threshold = max((t-1)*m+r for r,t in enumerate(thresholds))
    formula_f1 = 13 if m==4 else (h+3)*m-1-int(a==1)
    assert max_from_threshold == formula_f1, m
    positive_count = sum(thresholds)-1
    direct_positive_count = sum(count[n]<2 for n in range(1,max_from_threshold+1))
    assert positive_count == direct_positive_count, m
    formula_positive_count = {0:(3*h*h+21*h-8)//2,1:(3*h*h+23*h-2)//2,2:(3*h*h+25*h+6)//2}[a]
    assert positive_count == formula_positive_count, m
print('PASS:', checked, 'complete residue thresholds over 147 parameters; F1, 1-gap counts, and boundary quotients verified')
