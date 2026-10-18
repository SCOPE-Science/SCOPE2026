#!/usr/bin/env python3
"""Independent finite checks of the four-node cyclic Fourier runner-up theorem.

Python standard library; all enumerations finite corroboration, not a proof for all N.
"""
import itertools
import math


def value_chords(n, S):
    z = [complex(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n)) for j in S]
    ans = 1.0
    for i in range(4):
        for j in range(i+1,4):
            ans *= abs(z[j]-z[i])
    return ans


def value_gaps(n, S):
    a,b,c = (S[i+1]-S[i] for i in range(3))
    d = n-S[3]+S[0]
    return 64*math.prod(math.sin(math.pi*t/n) for t in (a,b,c,d,a+b,b+c))


def is_square(n, S):
    m=n//4
    return frozenset(S)==frozenset((t+j*m)%n for j in range(4) for t in [S[0]])


def is_one_shift(n, S):
    m=n//4
    target=frozenset(S)
    for t in range(m):
        square=frozenset((t+j*m)%n for j in range(4))
        for x in square:
            for y in ((x-1)%n,(x+1)%n):
                if target == (square-{x})|{y}:
                    return True
    return False


total=0
for n in range(8,53,4):
    value_runner=16*math.cos(math.pi/n)*math.cos(2*math.pi/n)
    squares=0
    equals=[]
    nonsquare_top=0
    for S in itertools.combinations(range(n),4):
        total+=1
        d1=value_chords(n,S)
        d2=value_gaps(n,S)
        assert math.isclose(d1,d2,rel_tol=1e-11,abs_tol=1e-11),(n,S,d1,d2)
        if is_square(n,S):
            squares+=1
            assert math.isclose(d1,16,rel_tol=1e-11,abs_tol=1e-11)
        else:
            assert d1<=value_runner+1e-8, (n,S,d1,value_runner)
            nonsquare_top=max(nonsquare_top,d1)
            if math.isclose(d1,value_runner,rel_tol=1e-11,abs_tol=1e-11):
                assert is_one_shift(n,S),(n,S)
                equals.append(S)
    assert squares==n//4, (n,squares)
    assert len(equals)==2*n, (n,len(equals),2*n)
    assert math.isclose(nonsquare_top,value_runner,rel_tol=1e-11,abs_tol=1e-11)
    print(f'N={n:2d} subsets={math.comb(n,4):6d} squares={squares:2d} runner={len(equals):3d} runner_det={value_runner:.12f}')
print(f'CHECK_OK {total} configurations; all 12 cyclic orders checked')
