#!/usr/bin/env python3
"""Standalone finite verification of prefix-normal height-two Dyck paths.

The theorem's infinite scope is proved mathematically in RESULT.md; this
script checks all height-two Dyck words to semilength 14 and all finite
corresponding numerical semigroup signatures.
"""
from collections import Counter


def word_from_mask(n, mask):
    # Even vertex 2*i has height 2 iff bit i-1 is set, i=1..n-1.
    heights = [0]
    for j in range(1, 2*n+1):
        if j & 1:
            heights.append(1)
        elif j == 2*n:
            heights.append(0)
        else:
            heights.append(2 if (mask >> (j//2-1)) & 1 else 0)
    word = ''.join('0' if heights[j] > heights[j-1] else '1'
                   for j in range(1, 2*n+1))
    return word, heights


def prefix_normal_direct(word):
    counts = [0]
    for bit in word:
        counts.append(counts[-1] + (bit == '0'))
    for k in range(1, len(word) + 1):
        maximum = max(counts[j+k] - counts[j]
                      for j in range(len(word)-k+1))
        if maximum > counts[k]:
            return False
    return True


def semigroup_test_direct(n, mask):
    gaps = {i for i in range(1,n) if (mask >> (i-1)) & 1}
    small = set(range(n)).difference(gaps)
    return all((a+b) in small for a in small for b in small if a+b<n)


def stats(n, mask, heights):
    gaps = [i for i in range(1,n) if (mask >> (i-1)) & 1]
    g=len(gaps)
    c = gaps[-1]+1 if gaps else 0
    mult = next(i for i in range(1,n+1) if i not in gaps)
    area=sum(heights[1:2*n])
    return g,c,mult,area


def run():
    expected = [1,2,3,5,7,12,16,27,37,58,80,131,171,277]
    genus_at_n = {}
    checked=0
    for n in range(1, 15):
        hist=Counter()
        good=0
        for mask in range(1<<(n-1)):
            w,heights=word_from_mask(n,mask)
            assert heights[0]==0 and heights[-1]==0
            assert all(h in (0,1,2) for h in heights)
            assert all(abs(heights[j]-heights[j-1])==1 for j in range(1,2*n+1))
            pn=prefix_normal_direct(w)
            sg=semigroup_test_direct(n,mask)
            assert pn==sg, (n,mask,w,pn,sg)
            if pn:
                good+=1
                g,c,m,area=stats(n,mask,heights)
                assert area == n+2*g
                assert c<=n
                assert (m==n if not any(heights[2*i]==0 for i in range(1,n))
                        else m == next(i for i in range(1,n) if heights[2*i]==0))
                assert 2*m == next(i for i in range(1,2*n+1) if heights[i]==0)
                assert c == (1+max((i for i in range(1,n) if heights[2*i]==2),default=-1)
                             if g else 0)
                hist[g]+=1
            checked+=1
        assert good == expected[n-1], (n,good,expected[n-1])
        genus_at_n[n]=hist
    # Independently enumerate complete semigroup signatures for each n.
    for n in range(1,15):
        sig = Counter()
        for bits in range(1<<(n-1)):
            chosen={i+1 for i in range(n-1) if bits>>i&1}
            if all(a+b>=n or a+b in chosen for a in chosen for b in chosen):
                sig[len(set(range(1,n))-chosen)]+=1
        assert sig==genus_at_n[n],(n,sig,genus_at_n[n])
    # Sharp stabilization at the upper conductor bound 2*g.
    known_genus_counts=[1,1,2,4,7,12,23,39]
    for g in range(0,8):
        if g==0:
            assert all(genus_at_n[n][0]==1 for n in range(1,15))
        else:
            n=2*g
            if n<=14:
                assert genus_at_n[n][g]==known_genus_counts[g],(g,n,genus_at_n[n][g])
                assert genus_at_n[n-1][g]<known_genus_counts[g]
    print('HEIGHT_TWO_PREFIX_NORMAL_SEMIGROUP_PASS',
          'paths_tested='+str(checked),
          'semilength=1..14',
          'counts='+str(expected),
          'genus_1_to_7='+str(known_genus_counts[1:]))

if __name__=='__main__':
    run()
