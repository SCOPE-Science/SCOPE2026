#!/usr/bin/env python3
"""Finite computational checks of connected dominating sets in crown graphs.
Run: python3 verify_crown.py. Uses only the Python standard library.
"""
import math


def graph(n):
    adj = [0] * (2*n)
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i] |= 1 << (n + j)
                adj[n+j] |= 1 << i
    return adj


def brute_coefficients(n):
    adj = graph(n)
    universe = (1 << (2*n)) - 1
    coefficients = [0] * (2*n + 1)
    for mask in range(1, universe + 1):
        if mask.bit_count() < 4:
            continue
        dominated = mask
        pending = mask
        while pending:
            bit = pending & -pending
            pending -= bit
            dominated |= adj[bit.bit_length()-1]
        if dominated != universe:
            continue
        reached = mask & -mask
        while True:
            neighbor_mask = 0
            pending = reached
            while pending:
                bit = pending & -pending
                pending -= bit
                neighbor_mask |= adj[bit.bit_length()-1]
            new = reached | (neighbor_mask & mask)
            if new == reached:
                break
            reached = new
        if reached == mask:
            coefficients[mask.bit_count()] += 1
    return coefficients


def predicted_coefficients(n):
    q = [0]*(n+1)
    for k in range(2,n+1):
        q[k] = math.comb(n,k)
    c=[0]*(2*n+1)
    for a in range(n+1):
        for b in range(n+1):
            c[a+b] += q[a]*q[b]
    c[4] -= math.comb(n,2)
    return c


def normalized_R(n,y):
    # R_n(-y) where y>0; use floating-point only for illustrative roots.
    return ((1.0-y)**n-1.0+n*y)/(y*y)


def real_roots(n):
    threshold=math.sqrt(math.comb(n,2))
    # y in (1,2), R(-y)=+threshold.
    lo,hi=1.,2.
    for _ in range(90):
        mid=(lo+hi)/2
        if normalized_R(n,mid)>threshold: lo=mid
        else: hi=mid
    right=-(lo+hi)/2
    # left root y>2, with R(-y)=threshold (even) or -threshold (odd).
    target = threshold if n%2==0 else -threshold
    lo,hi=2.,3.
    while (normalized_R(n,hi)-target)*(normalized_R(n,lo)-target)>0:
        hi+=1.
    for _ in range(90):
        mid=(lo+hi)/2
        v=normalized_R(n,mid)-target
        if n%2==0:
            if v<0:lo=mid
            else:hi=mid
        else:
            if v>0:lo=mid
            else:hi=mid
    left=-(lo+hi)/2
    assert left< -2 < right< -1
    return left,right


def main():
    for n in range(3,9):
        exact=brute_coefficients(n)
        prediction=predicted_coefficients(n)
        assert exact==prediction,(n,exact,prediction)
        print(f'n={n}: exhaustive subsets={1<<(2*n)}: coefficient match; D_c/x^4={exact[4:]}')
    for n in [3,4,5,6,10,21,50,101,200,301]:
        left,right=real_roots(n)
        c=2*(math.sqrt(2)+1) if n%2 else 2*(math.sqrt(2)-1)
        residual=n*(-left-2)-math.log(n)-math.log(c)
        print(f'n={n}: left={left:.12g}, right={right:.12g}, n*epsilon-log(n)-log(c)={residual:.7g}')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
