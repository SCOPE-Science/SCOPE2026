#!/usr/bin/env python3
"""Independent exact checks for the 1-Frobenius formulas of prime-triplet templates.
Uses separate residue-pair enumeration and coin-change DP.
"""

def candidate(family, k):
    if family == 1:
        return (5, 7, 11, 24) if k == 0 else (6*k+5, 6*k+7, 6*k+11, 12*k*k+40*k+23)
    return (7, 11, 13, 45) if k == 0 else (6*k+7, 6*k+11, 6*k+13, 12*k*k+50*k+56)

def second_residue_baselines(a,b,c, bound):
    # Every residue has at least two baselines below bound by the stated theorem.
    minima=[[] for _ in range(a)]
    for y in range(bound//b+1):
        by=b*y
        for z in range((bound-by)//c+1):
            v=by+c*z
            r=v%a
            minima[r].append(v)
    return [sorted(row)[:2] for row in minima]

def direct_dp(a,b,c, bound):
    ways=[0]*(bound+1)
    ways[0]=1
    for d in (a,b,c):
        for n in range(d,bound+1):
            ways[n]=min(3,ways[n]+ways[n-d])
    return ways

def run():
    num=0
    for family in (1,2):
        for k in range(0,36):
            a,b,c,expected=candidate(family,k)
            bound=expected+a+1
            baselines=second_residue_baselines(a,b,c,bound)
            assert all(len(row)==2 for row in baselines),(family,k,'incomplete')
            second=max(row[1] for row in baselines)
            assert second-a==expected,(family,k,'residue',second-a,expected)
            ways=direct_dp(a,b,c,expected+2*a)
            assert ways[expected]<=1,(family,k,'bad candidate')
            assert all(ways[n]>=2 for n in range(expected+1,expected+2*a+1)),(family,k,'successor failure')
            num+=1
    print('PASS',num,'parameter instances; every residue has two baselines and DP confirms final gaps')
if __name__ == '__main__':run()
