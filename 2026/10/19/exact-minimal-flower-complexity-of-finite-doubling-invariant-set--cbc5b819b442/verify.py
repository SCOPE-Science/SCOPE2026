#!/usr/bin/env python3
"""Exact rational tests for finite invariant sets of the doubling circle map.
Tests supplement, and do not replace, the mathematical proof."""
from fractions import Fraction
from itertools import combinations, product
from math import gcd

def doubling(x):
    return (2*x)%1

def orbit(n,j):
    modulus=2**n-1
    x=Fraction(j,modulus)
    result=set()
    while x not in result:
        result.add(x)
        x=doubling(x)
    return frozenset(result)

def prescribed_bits(K):
    K=sorted(K)
    inverse={doubling(x):x for x in K}
    assert len(inverse)==len(K)
    return [int(2*inverse[y]) for y in K]

def cost(bits):
    return sum(a!=b for a,b in zip(bits,bits[1:]))+(bits[0]==bits[-1])

def construct_jump_locations(K):
    """Place all jumps in open gaps, never at constrained orbit points."""
    ys=sorted(K)
    bits=prescribed_bits(K)
    locations=[]
    for i in range(len(ys)-1):
        if bits[i]!=bits[i+1]:
            locations.append((ys[i]+ys[i+1])/2)
    if bits[-1]==bits[0]:
        locations.append(((ys[-1]+ys[0]+1)/2)%1)
    assert len(locations)==cost(bits)
    assert all(0<=x<1 and x not in K for x in locations)
    return locations

def brute_min(bits):
    """Enumerate all discrete piecewise-branch choices on 2N test segments.
    There are two segments around every prescribed point; at each point
    at least one adjacent segment must carry its prescribed preimage branch.
    Additional switches inside open gaps cannot reduce the cost.
    The circle seam carries the degree-two monodromy.
    """
    N=len(bits)
    result=10000
    for choices in product((0,1),repeat=2*N):
        # right-near-point and left-near-point labels, linear [0,1) coordinates
        if any(bits[i] not in (choices[2*i],choices[2*i+1]) for i in range(N)):
            continue
        internal=sum(choices[2*i+1]!=choices[2*(i+1)] for i in range(N-1))
        # each point has a branch mismatch if its left and right bits disagree
        boundaries=sum(choices[2*i]!=choices[2*i+1] for i in range(N))
        # from last right-near-point to first left-near-point across seam;
        # physically continuous if the bits are different.
        seam=(choices[-1]==choices[0])
        total=internal+boundaries+seam
        if total<result:
            result=total
    return result

def main():
    assertions=0
    tested=0
    for n in range(1,8):
        D=2**n-1
        # Periodic grid formula, directly from modular inverse computation.
        K=frozenset(Fraction(j,D) for j in range(D))
        bits=prescribed_bits(K)
        assert bits==[j%2 for j in range(D)]
        assert cost(bits)==D
        assert len(construct_jump_locations(K))==D
        assertions+=3
        orbits=set()
        for j in range(D):
            O=orbit(n,j)
            assert doubling(next(iter(O))) in O
            orbits.add(O)
            assertions+=1
        # Every full orbit with >=2 points has BWT predecessor-order formula.
        for O in orbits:
            b=prescribed_bits(O)
            if len(O)>1:
                assert b[0]==1 and b[-1]==0
                assert cost(b)==sum(x!=y for x,y in zip(b,b[1:]))
                assertions+=2
            assert len(construct_jump_locations(O))==cost(b)
            assertions+=1
            if len(O)<=5:
                assert brute_min(b)==cost(b)
                assertions+=1
            tested+=1
    # Enumerate all unions for the period-four grid: fixed point, 2-cycle,
    # three-cycle(s), four-cycle(s); check full inverse invariance exactly.
    n=4
    D=2**n-1
    orbits=sorted(set(orbit(n,j) for j in range(D)),key=lambda o:(len(o),min(o)))
    for mask in range(1,2**len(orbits)):
        K=frozenset().union(*(o for i,o in enumerate(orbits) if mask>>i &1))
        b=prescribed_bits(K)
        assert cost(b)%2==1
        assert len(construct_jump_locations(K))==cost(b)
        assertions+=2
        if len(K)<=4:
            assert brute_min(b)==cost(b)
            assertions+=1
        tested+=1
    # Alphabetic BWT and modular-period coding computed independently.
    for n in range(2,11):
        D=2**n-1
        if n>7: # sample deterministic primitive words of length up to 10
            words=['0'*(n-1)+'1', '01'*(n//2)+'0'*(n%2)]
        else:
            words=[''.join(t) for t in product('01',repeat=n)]
        for w in words:
            if len(set(w[i:]+w[:i] for i in range(n)))!=n:continue
            value=int(w,2)
            O=orbit(n,value)
            assert len(O)==n
            rots=sorted(w[i:]+w[:i] for i in range(n))
            bwt=''.join(r[-1] for r in rots)
            b=''.join(map(str,prescribed_bits(O)))
            assert b==bwt and b[0]=='1' and b[-1]=='0'
            assert cost([int(x) for x in bwt])==len([1 for i in range(n-1) if bwt[i]!=bwt[i+1]])
            assertions+=3
            tested+=1
    print(f'VERIFIED: {assertions} exact rational assertions; {tested} finite families; no infinite theorem inferred from tests')

if __name__=='__main__':main()
