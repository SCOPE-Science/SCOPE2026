#!/usr/bin/env python3
from itertools import product
from collections import Counter
from math import comb

def is_valid(n, vals):
    x=vals[:n]; y=vals[n:]; W=sum(vals)
    for i in range(n):
        for j in range(n):
            if i != j and x[i] == 0 and y[j] == 0:
                if W - x[j] - y[i] < 2:
                    return False
    return True

def total_coeff(n, w):
    # coefficient of (1+z+z^2)^(2n)
    dp=[0]*(4*n+1); dp[0]=1
    for _ in range(2*n):
        nd=[0]*len(dp)
        for s,a in enumerate(dp):
            if a:
                for v in (0,1,2): nd[s+v]+=a
        dp=nd
    return dp[w]

def bad_formula(n):
    return {
        0:1,
        1:2*n,
        2:2*n*n,
        3:n*(n-1)*(n+2),
        4:n*(n-1)*(3*n-5),
        5:2*n*(n-1)*(n-2),
    }

def theorem_coeffs(n):
    bad=bad_formula(n)
    return {w: total_coeff(n,w)-bad.get(w,0) for w in range(4*n+1)}

def low_weight_pattern_count(n):
    # Independent count from the pattern families in the proof table.
    return {
      0: 1,
      1: 2*n,
      2: 2*n + 2*comb(n,2) + n*(n-1),
      3: 2*n*(n-1) + 2*n*(n-1) + n*(n-1)*(n-2),
      4: n*(n-1) + 2*n*(n-1)*(n-2) + n*(n-1)*(n-2),
      5: 2*n*(n-1)*(n-2),
    }

def main():
    exhaustive=0
    mins=0
    for n in range(3,7):
        observed=Counter()
        minvals=[]
        for vals in product(range(3), repeat=2*n):
            exhaustive += 1
            if is_valid(n, vals):
                observed[sum(vals)] += 1
                if sum(vals)==2: minvals.append(vals)
        expected=theorem_coeffs(n)
        for w in range(4*n+1):
            assert observed[w] == expected[w], (n,w,observed[w],expected[w])
        expected_min=[]
        for i in range(n):
            vals=[0]*(2*n); vals[i]=1; vals[n+i]=1
            expected_min.append(tuple(vals))
        assert set(minvals)==set(expected_min), (n,len(minvals))
        mins += len(minvals)
    for n in range(3,31):
        assert low_weight_pattern_count(n)==bad_formula(n), n
    print('ALL CHECKS PASSED; exhaustive_orders=[3, 4, 5, 6]; exhaustive_labelings=%d; low_weight_orders=28; minimum_functions_checked=%d' % (exhaustive, mins))

if __name__=='__main__':
    main()
