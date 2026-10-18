#!/usr/bin/env python3
"""Independent exhaustive check of the total-domination polynomial for M(K_{2,n})."""
from math import comb
from collections import Counter


def neighborhood_masks(n):
    # 0,1: two hubs; 2..n+1: n peripheral vertices;
    # n+2..2n+1: edge vertices of first row; 2n+2..3n+1: second row.
    count=3*n+2
    neighbors=[0]*count
    def add(i,j):
        neighbors[i]|=1<<j
        neighbors[j]|=1<<i
    for col in range(n):
        y=2+col
        a=n+2+col
        b=2*n+2+col
        add(0,a);add(1,b);add(y,a);add(y,b);add(a,b)
        for prior in range(col):
            add(a,n+2+prior)
            add(b,2*n+2+prior)
    return neighbors


def predicted_coefficients(n):
    # D_n(z)=z^n(1+z)^n([((2+z)^n-2](1+z)^2-2n)
    result=Counter()
    for j in range(n+1):
        for i in range(n+1):
            for k in range(3):
                result[n+j+i+k]+=comb(n,j)*comb(n,i)*2**(n-i)*comb(2,k)
    for j in range(n+1):
        for k in range(3):
            result[n+j+k]-=2*comb(n,j)*comb(2,k)
        result[n+j]-=2*n*comb(n,j)
    return {degree:val for degree,val in result.items() if val}


def brute_coefficients(n):
    masks=neighborhood_masks(n)
    coeff=Counter()
    for chosen in range(1<<len(masks)):
        if all(chosen & nbr for nbr in masks):
            coeff[chosen.bit_count()]+=1
    return dict(coeff)


def main():
    total=0
    for n in range(3,7):
        got=brute_coefficients(n)
        expected=predicted_coefficients(n)
        assert got==expected,(n,got,expected)
        assert got[3*n+2]==1
        assert got[3*n+1]==3*n+2
        assert min(got)==(4 if n==3 else n)
        assert got[min(got)]==(24 if n==3 else 2**n-2*n-2)
        total+=1<<(3*n+2)
        print('PASS n=%d order=%d total_dominating_sets=%d minimum=%d optimal_sets=%d' %
              (n,3*n+2,sum(got.values()),min(got),got[min(got)]))
    print('VERIFICATION_OK graph_cases=4 examined_subsets=%d' % total)


if __name__=='__main__':main()
