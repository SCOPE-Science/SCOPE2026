#!/usr/bin/env python3
"""Independent finite checks for valuation-edge classification of a binomial parity sum."""
from collections import defaultdict
from math import comb

def v2(n):
    assert n > 0
    return (n & -n).bit_length()-1

def block_value(length):
    if length % 2 == 0:
        return 1
    return (length+1)//2

def transform(n):
    product = 1
    while n:
        while n and not (n&1): n >>= 1
        length = 0
        while n&1:
            length += 1
            n >>= 1
        if length: product *= block_value(length)
    return product

def direct_binomial_parity_sum(n):
    total = 0
    k = n
    while True:
        top = 6*k
        bottom = n + 3*k
        if bottom <= top and (top & bottom) == bottom:
            total += 1
        if k == 0: break
        k = (k-1)&n
    return total

def power_coeff(power,k):
    return sum(comb(power+k-j-1,k-j)*comb(k-j,j) for j in range(k//2+1))

def predicted(r):
    k,s = divmod(r+1,4)
    ans = [power_coeff(1,k), power_coeff(2,k), power_coeff(2,k)+power_coeff(3,k),power_coeff(2,k)+2*power_coeff(3,k)+power_coeff(4,k)][s]
    return k,ans

def dynamic_distribution(max_r):
    # independent path: append bits left to right; record current one-run length and closed-run valuations
    state = {(0,0):1}
    for r in range(max_r+1):
        freqs = defaultdict(int)
        for (ell, val),mult in state.items():
            freqs[val + (v2(block_value(ell)) if ell else 0)] += mult
        k,c = predicted(r)
        assert max(freqs) == k,(r,max(freqs),k)
        assert freqs[k] == c,(r,freqs[k],c)
        assert set(freqs) == set(range(k+1)),(r,sorted(freqs),k)
        assert sum(freqs.values()) == (1<<r)
        next_state=defaultdict(int)
        for (ell,val),mult in state.items():
            next_state[(0,val+(v2(block_value(ell)) if ell else 0))] += mult
            next_state[(ell+1,val)] += mult
        state = next_state
    return True

def check_token_deficits(max_length):
    minima=[]
    for ell in range(1,max_length+1):
        deficit=ell+1-4*v2(block_value(ell))
        assert deficit>=0
        if ell==3 or ell==7: assert deficit==0
        elif ell==1: assert deficit==2
        elif ell==2: assert deficit==3
        else: assert deficit>=4,(ell,deficit)
    return True

def main():
    for n in range(1<<12):
        a=direct_binomial_parity_sum(n)
        b=transform(n)
        assert a==b,(n,a,b)
    check_token_deficits(2000)
    dynamic_distribution(120)
    for r in range(18):
        k,c=predicted(r)
        vals=[v2(transform(n)) for n in range(1<<r)]
        assert max(vals)==k,(r,max(vals),k)
        assert vals.count(k)==c,(r,vals.count(k),c)
        assert set(vals)==set(range(k+1))
    print('VERIFY_OK: 4096 independent binomial-sum values, 2000 run-deficit inequalities, 121 full distribution recurrences, 262143 brute binary values and extremizer counts through r=17')
if __name__=='__main__':main()
