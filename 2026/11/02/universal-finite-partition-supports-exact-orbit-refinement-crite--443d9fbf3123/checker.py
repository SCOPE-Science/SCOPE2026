"""Finite exhaustive corroboration of a universal partition refinement criterion.
Only standard Python is required: python3 checker.py
"""
from functools import lru_cache


def parts(n, low=1):
    if n == 0:
        yield ()
    else:
        for a in range(low, n+1):
            for tail in parts(n-a,a):
                yield (a,)+tail


def can_group(weights,targets):
    weights=tuple(sorted(weights,reverse=True))
    targets=tuple(sorted(targets,reverse=True))
    @lru_cache(None)
    def go(i,left):
        if i==len(weights):
            return all(x==0 for x in left)
        a=weights[i]
        used=set()
        for j,x in enumerate(left):
            if x>=a and x not in used:
                used.add(x)
                residual=list(left)
                residual[j]-=a
                if go(i+1,tuple(sorted(residual,reverse=True))):
                    return True
        return False
    return go(0,targets)


def universal(weights,k):
    n=sum(weights)
    for t in parts(n):
        if len(t)<=k and not can_group(weights,t):
            return False
    return True


def prefix_condition(weights,k):
    s=0
    for a in weights:
        if (k-1)*(a-1)>s:
            return False
        s+=a
    return True

checked=0
for k in (2,3,4,5):
    for n in range(1,18):
        for w in parts(n):
            a=universal(w,k)
            b=prefix_condition(w,k)
            assert a==b,(k,n,w,a,b)
            checked+=1
for k in (2,3,4,5,6):
    cap=0
    for b in range(1,14):
        next_w=1+cap//(k-1)
        cap+=next_w
        # extremal sequence is universal, even when n > practical exhaustive range
        # its validity follows from the inductive construction.
        if cap<=17:
            ws=[]; old=0
            for j in range(1,b+1):
                a=1+old//(k-1)
                ws.append(a);old+=a
            assert universal(tuple(ws),k)
    # no exhaustive infinite proof is claimed
print(f'ALL_CHECKS_OK compared_weight_multisets={checked} k_ranges=2..5 n_ranges=1..17')
