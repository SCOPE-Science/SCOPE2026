#!/usr/bin/env python3
"""Direct independent finite checks for cyclic Abelian powers of Zimin words."""
from collections import Counter

def zimin(n):
    if n < 1: raise ValueError('n must be >=1')
    z = [1]
    for k in range(2,n+1): z = z + [k] + z
    return tuple(z)

def abelian_squares_counter(w):
    N=len(w)
    return {(i,d) for d in range(1,N//2+1) for i in range(N)
            if Counter(w[(i+t)%N] for t in range(d)) ==
               Counter(w[(i+d+t)%N] for t in range(d))}

def abelian_squares_prefix(w):
    N=len(w); m=max(w)
    extended=w*2
    pref=[[0]*(2*N+1) for _ in range(m)]
    for j,v in enumerate(extended,1):
        for k in range(m): pref[k][j]=pref[k][j-1]+(v==k+1)
    result=set()
    for d in range(1,N//2+1):
        for i in range(N):
            if all(pref[k][i+d]-pref[k][i] == pref[k][i+2*d]-pref[k][i+d] for k in range(m)):
                result.add((i,d))
    return result

def linear_squares(w):
    N=len(w)
    return {(i,d) for d in range(1,N//2+1) for i in range(N-2*d+1)
            if Counter(w[i:i+d])==Counter(w[i+d:i+2*d])}

def abelian_cubes(w):
    N=len(w)
    return {(i,d) for d in range(1,N//3+1) for i in range(N)
            if Counter(w[(i+t)%N] for t in range(d)) == Counter(w[(i+d+t)%N] for t in range(d))
            ==Counter(w[(i+2*d+t)%N] for t in range(d))}

def main():
    checked=0; rotations=0; squares=0
    for n in range(1,9):
        w=zimin(n);N=len(w)
        expected={(N-d,d) for d in range(1,N//2+1)}
        a=abelian_squares_counter(w)
        b=abelian_squares_prefix(w)
        assert a==b==expected, (n,a^expected,b^expected)
        assert not abelian_cubes(w)
        for c in range(N):
            shifted=w[c:]+w[:c]
            count=len(linear_squares(shifted))
            assert count==min(c,N-c), (n,c,count,min(c,N-c))
            rotations+=1
        assert all(w[j-1] == 1+(j&-j).bit_length()-1 for j in range(1,N+1))
        checked+=1;squares+=len(a)
    p=tuple(int(c) for c in '012301021242120103210')
    assert p==p[::-1] and not linear_squares(p)
    extra=abelian_squares_counter(p)
    assert all((i,7) in extra for i in (11,14,17))
    assert len({i for i,d in extra if d==7})==3
    print('VERIFY_OK levels=1..8 independent_counter_and_prefix_methods=2 circular_occurrences=%d linear_rotation_profiles=%d no_circular_abelian_cubes_through_level8=true counterexample_palindrome_length21_checked=true' % (squares,rotations))
if __name__=='__main__':main()
