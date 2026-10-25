#!/usr/bin/env python3
"""Independent exact finite check for minimum palindromic factorization counts."""
from math import factorial

def check(limit=500):
    word = [0]+[(i & -i).bit_length() for i in range(1,limit+1)]
    distance=[10**9]*(limit+1)
    ways=[0]*(limit+1)
    distance[0]=0
    ways[0]=1
    for end in range(1,limit+1):
        for start in range(end):
            interval=word[start+1:end+1]
            if interval==interval[::-1]:
                value=distance[start]+1
                if value<distance[end]:
                    distance[end]=value
                    ways[end]=ways[start]
                elif value==distance[end]:
                    ways[end]+=ways[start]
        runs=(end^(end>>1)).bit_count()
        expected=factorial((runs+1)//2)*factorial(runs//2)
        assert distance[end]==runs, (end, distance[end],runs)
        assert ways[end]==expected, (end,ways[end],expected)
    print('VERIFY_OK brute_literal_palindrome_DP_lengths=0..'+str(limit))
    print('VERIFY_OK minimum_lengths_and_optimal_factorization_counts=yes')
    for n in (10,21,42,85,170,341):
        print('n=%d minimum=%d factorizations=%d'%(n,distance[n],ways[n]))
if __name__=='__main__':
    check()
