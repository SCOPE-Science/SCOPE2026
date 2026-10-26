"""Exact standalone checks for covariance defects of circular Parikh matrices."""
from fractions import Fraction
from itertools import product, permutations
from random import Random
from math import comb

ORDER = 'abcd'
D = 5

def eye():
    return [[Fraction(i == j) for j in range(D)] for i in range(D)]

def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(D))
             for j in range(D)] for i in range(D)]

def mpow(A, p):
    R = eye()
    while p:
        if p & 1:
            R = mmul(R, A)
        A = mmul(A, A)
        p //= 2
    return R

def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(D)] for i in range(D)]

def mavg(A):
    n = len(A)
    return [[sum(M[i][j] for M in A) / n for j in range(D)]
            for i in range(D)]

def parikh(word):
    # The append-letter recurrence builds exact scattered-subword counts.
    M = eye()
    for x in word:
        j = ORDER.index(x) + 1
        for i in range(j):
            M[i][j] += M[i][j-1]
    return M

def average(word):
    return mavg([parikh(word[i:] + word[:i]) for i in range(len(word))])

def inverse_unitriangular(A):
    I = eye()
    N = msub(A, I)
    S, P = I, I
    for k in range(1, D):
        P = mmul(P, N)
        sign = -1 if k & 1 else 1
        S = [[S[i][j] + sign * P[i][j] for j in range(D)]
             for i in range(D)]
    return S

def alternate(A):
    return [[(-1 if (j-i)&1 else 1) * A[i][j]
             for j in range(D)] for i in range(D)]

def paircount(word, x, y):
    num_x = num_xy = 0
    for ch in word:
        if ch == y:
            num_xy += num_x
        if ch == x:
            num_x += 1
    return num_xy

def covariance(word):
    n = len(word)
    x = [paircount(word[t:]+word[:t], 'a', 'b') for t in range(n)]
    y = [paircount(word[t:]+word[:t], 'c', 'd') for t in range(n)]
    return Fraction(n*sum(i*j for i,j in zip(x,y))-sum(x)*sum(y), n*n)

def assert_central(A, coeff):
    for i in range(D):
        for j in range(D):
            assert A[i][j] == (coeff if (i,j) == (0,D-1) else 0), (i,j,A[i][j],coeff)

def check(w):
    M = average(w)
    C = covariance(w)
    difference = msub(alternate(average(w[::-1])), inverse_unitriangular(M))
    assert_central(difference, C)
    for p in (2, 3, 5):
        power_difference = msub(average(w*p), mpow(M, p))
        assert_central(power_difference, comb(p,2)*C)
    return C

def block_formula(A,B,C,D,order):
    n=A+B+C+D
    product=A*B*C*D
    if order in ('abcd', 'adcb'):
        k=-(A+B)*(C+D)
    elif order in ('abdc', 'acdb'):
        k=(A+B)*(C+D)
    elif order in ('acbd','adbc'):
        k=(A-B)*(C-D)
    else:
        raise ValueError(order)
    return Fraction(product*k,4*n*n)

def main():
    cases=0
    for n in range(1,6):
        for tup in product(ORDER, repeat=n):
            check(''.join(tup)); cases+=1
    rng=Random(20210428)
    for n in range(6,16):
        for _ in range(16):
            w = ''.join(rng.choice(ORDER) for _ in range(n))
            check(w);cases+=1
    vals={}
    for p in permutations(ORDER):
        w=''.join(p);vals[w] = covariance(w)
        check(w); cases += 1
    assert {vals[w] for w in vals} == {Fraction(-1,16),Fraction(0),Fraction(1,16)}
    assert sum(v == 0 for v in vals.values())==8
    assert sum(v < 0 for v in vals.values())==8
    assert sum(v > 0 for v in vals.values())==8
    assert vals['abcd']==Fraction(-1,16)
    assert vals['abdc']==Fraction(1,16)
    assert vals['acbd']==0
    orders=('abcd','abdc','acbd','acdb','adbc','adcb')
    blocks=0
    for A,B,C,D in product(range(1,4), repeat=4):
        sizes={'a':A,'b':B,'c':C,'d':D}
        for o in orders:
            w=''.join(ch*sizes[ch] for ch in o)
            assert covariance(w)==block_formula(A,B,C,D,o), (w,covariance(w),block_formula(A,B,C,D,o))
            blocks+=1
    assert block_formula(2,2,3,1,'acbd') == 0
    print(f'CIRCULAR_PARIKH_COVARIANCE_PASS words={cases} lengths=1..15 powers=2,3,5 permutation_signs=8,8,8 blocks={blocks}')

if __name__ == '__main__':
    main()
