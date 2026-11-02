#!/usr/bin/env python3
"""Finite checks for the exact mathematical wave theorem (standard library only).

Tests do not establish the infinite-length spectral and dynamical claims;
those follow from the analytical proof.
"""
from itertools import product
from math import comb, cos, pi


def adjacency(theta):
    words = list(product((0, 1), repeat=3))
    index = {w: i for i, w in enumerate(words)}
    M = [[0] * 8 for _ in range(8)]
    for a, b, c, d in product((0, 1), repeat=4):
        predators = 2 * c + (c ^ d) + a * b
        valid = predators >= theta if c else predators < theta
        if valid:
            M[index[a, b, c]][index[b, c, d]] += 1
    return M


def mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def charpoly(M):
    n = len(M)
    power = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = [0]
    for _ in range(n):
        power = mul(power, M)
        traces.append(sum(power[i][i] for i in range(n)))
    coeff = [1]
    for k in range(1, n + 1):
        numerator = sum(coeff[k-j] * traces[j] for j in range(1, k+1))
        assert numerator % k == 0
        coeff.append(-numerator // k)
    return coeff


def wave_word(bits):
    colors = [0]
    for bit in bits:
        colors.append((colors[-1] + bit) % 3)
    if colors[-1] != 0:
        return None
    return tuple(colors[:-1])


def update_stripe(word,theta,direction):
    n=len(word)
    # 2D torus with both sides length n >=3; count 8 neighbor offsets.
    c=lambda i,j: word[i % n] if direction=='horizontal' else word[(i+j)%n]
    old=[[c(i,j) for j in range(n)] for i in range(n)]
    new=[]
    for i in range(n):
        row=[]
        for j in range(n):
            v=old[i][j]
            predators=sum(old[(i+dx)%n][(j+dy)%n]==(v+1)%3
                          for dx in (-1,0,1) for dy in (-1,0,1) if (dx,dy)!=(0,0))
            row.append((v+1)%3 if predators>=theta else v)
        new.append(row)
    target=[[c(i+1,j) for j in range(n)] for i in range(n)]
    return new == target


def predicted(bits,theta,direction):
    n=len(bits)
    if direction=='horizontal':
        return theta<=3 or not any(bits)
    for i,b in enumerate(bits):
        predators=2*b+(b^bits[(i+1)%n])+bits[(i-2)%n]*bits[(i-1)%n]
        if (predators>=theta)!=bool(b):
            return False
    return True


def main():
    expected={1:[1,-2,1,0,0,0,0,0,0],
              2:[1,-2,0,1,-1,0,0,0,0],
              3:[1,-2,0,1,0,0,0,0,0],
              4:[1,-1,0,0,0,0,0,0,0]}
    for theta in range(1,9):
        got=charpoly(adjacency(theta))
        assert got==expected[min(theta,4)],(theta,got)
    print('PASS all eight diagonal transfer-matrix characteristic polynomials')
    counts=[]
    for n in range(3,9):
        words=[(bits,wave_word(bits)) for bits in product((0,1),repeat=n)]
        words=[(bits,word) for bits,word in words if word is not None]
        assert 3*len(words)==round(2**n+2*cos(pi*n/3))
        for theta in range(1,9):
            for direction in ('horizontal','diagonal'):
                for bits,word in words:
                    assert predicted(bits,theta,direction)==update_stripe(word,theta,direction),\
                           (n,theta,direction,bits)
        counts.append((n,3*len(words)))
    print('PASS exact 2D Moore local rule against symbolic criteria for all widths 3..8')
    print('periodic stripe word counts:',counts)
    for t in (1,2,3,4):
        M=adjacency(t)
        T=M
        counts=[]
        for n in range(1,13):
            counts.append(sum(T[i][i] for i in range(8)))
            T=mul(T,M)
        assert counts[0] in (1,2)
        print('diagonal binary trace theta',t,':',counts)
    print('ALL CHECKS PASSED')

if __name__=='__main__': main()
