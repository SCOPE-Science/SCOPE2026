#!/usr/bin/env python3
"""Exact finite-state certificate checks for trinomial residue discrepancies."""
from math import comb

WEIGHTS = (1, 1, 3, 2, 4)
MAX_2 = {1:(6,8,9,7),2:(3,0,1,2),3:(3,2,1,4),4:(0,2,1,-1)}
MIN_2 = {1:(0,2,1,3),2:(-5,-6,-3,-4),3:(-2,-2,-3,-2),4:(-5,-4,-3,-6)}
MIN_3 = {1:(-2,1,0,-1),2:(-6,-8,-7,-5),3:(-4,-4,-6,-5),4:(-6,-8,-7,-9)}
MIN_4 = {1:(-5,-3,-4,-2),2:(-10,-11,-8,-9),3:(-6,-7,-8,-7),4:(-10,-9,-8,-11)}
MAX_OFFSET = {1:3,2:-3,3:-2,4:-4}
MIN_OFFSET = {1:-10,2:2,3:-3,4:3}


def literal_trinomials(limit):
    """Integer recurrence unrelated to digit-state counting."""
    out = [1,1]
    for n in range(1,limit-1):
        num = (2*n+1)*out[-1] + 3*n*out[-2]
        assert num % (n+1) == 0
        out.append(num//(n+1))
    return out[:limit]


def trans_delta(residue, state, digit):
    return 4*sum((state*WEIGHTS[j]) % 5 == residue for j in range(digit))-digit


def transfer(v, residue, maximizing):
    extreme = max if maximizing else min
    return tuple(extreme(v[state-1]+trans_delta(residue,state,digit)
                         for state in range(1,5) for digit in range(5)
                         if state*WEIGHTS[digit] % 5 == target)
                 for target in range(1,5))


def discrepancy_from_digits(n, residue):
    """Evaluate the exact digit-prefix recursion without scanning n indices."""
    digits = []
    while n:
        digits.append(n%5)
        n//=5
    score=0
    state=1
    for digit in reversed(digits):
        score += trans_delta(residue,state,digit)
        state = state*WEIGHTS[digit] % 5
    return score


def main():
    for n,term in enumerate(literal_trinomials(700)):
        q=n
        residue=1
        while q:
            residue=residue*WEIGHTS[q%5]%5
            q//=5
        assert residue==term%5,(n,term,residue)
    for n in range(80):
        direct = sum(comb(n,2*k)*comb(2*k,k) for k in range(n//2+1))
        assert direct == literal_trinomials(80)[n]
    for residue in (1,2,3,4):
        vmin=(0,10**6,10**6,10**6)
        vmax=(0,-10**6,-10**6,-10**6)
        for depth in range(1,9):
            vmin=transfer(vmin,residue,False)
            vmax=transfer(vmax,residue,True)
            if depth==2:
                assert vmin==MIN_2[residue] and vmax==MAX_2[residue]
            if depth==3:assert vmin==MIN_3[residue]
            if depth==4:assert vmin==MIN_4[residue]
            if depth>=2:
                assert max(vmax)==3*depth+MAX_OFFSET[residue]
                assert min(vmin)==-((5*depth+MIN_OFFSET[residue])//2)
        assert transfer(MAX_2[residue],residue,True)==tuple(x+3 for x in MAX_2[residue])
        assert transfer(MIN_3[residue],residue,False)==MIN_4[residue]
        assert transfer(MIN_4[residue],residue,False)==tuple(x-5 for x in MIN_3[residue])
        for depth in range(2,13):
            first = {1:1,2:3,3:2,4:4}[residue]
            word = str(first)+'1'*(depth-2)+'2'
            extremal = int(word,5)
            assert extremal < 5**depth
            assert discrepancy_from_digits(extremal,residue)==3*depth+MAX_OFFSET[residue], (residue,depth,word)
    # Complete prefix counts, independently built by direct digit-product recurrence.
    total = 5**6
    weights = bytearray(total)
    weights[0]=1
    for n in range(1,total):
        weights[n] = (weights[n//5]*WEIGHTS[n%5])%5
    counts=[0]*5
    extrema={depth: {r:[10**9,-10**9] for r in range(1,5)} for depth in range(2,7)}
    for N in range(total):
        for depth in range(2,7):
            if N<5**depth:
                for r in range(1,5):
                    value = 4*counts[r]-N
                    extrema[depth][r][0] = min(extrema[depth][r][0],value)
                    extrema[depth][r][1] = max(extrema[depth][r][1],value)
        counts[weights[N]] += 1
    for depth in range(2,7):
        for r in range(1,5):
            expected = (-((5*depth+MIN_OFFSET[r])//2), 3*depth+MAX_OFFSET[r])
            assert tuple(extrema[depth][r])==expected,(depth,r,extrema[depth][r],expected)
    for depth in range(0,7):
        counts=[0]*5
        for n in range(5**depth):counts[weights[n]]+=1
        assert counts[1]==(5**depth+3)//4
        for r in (2,3,4): assert counts[r]==(5**depth-1)//4
    print('VERIFY_OK: 700 exact integer recurrence terms; 80 independent binomial sums; 4 residue-state Bellman certificates; 15625-index exhaustive digital prefix scan for four residues; exact witnesses through 12 digits')

if __name__=='__main__':main()
