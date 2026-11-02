#!/usr/bin/env python3
"""Independent exact-arithmetic checks of a planar randomized splitting example.

Requires Python 3.10+ standard library. No external source code or data files.
Finite enumeration is a consistency check; the all-parameter results use the
matrix identities and analytic inequalities given in the accompanying proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import exp, log, sqrt

CHECKS = 0

def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)

def transpose(M):
    return ((M[0][0], M[1][0]), (M[0][1], M[1][1]))

def matmul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def matvec(A, y):
    return tuple(sum(A[i][k]*y[k] for k in range(2)) for i in range(2))

def normsq(y):
    return y[0]*y[0]+y[1]*y[1]

def matadd(A, B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))

def mat_scale(A, q):
    return tuple(tuple(q*A[i][j] for j in range(2)) for i in range(2))

def one(s):
    return ((1-s*s, s), (-s, Q(1)))

def two(s):
    return ((Q(1), s), (-s, 1-s*s))

def determinant(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def trace(M):
    return M[0][0]+M[1][1]

parameters = [Q(1, 8), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(5, 2), Q(3), Q(4), Q(5, 3)]
initials = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(2), Q(-3))]
for s in parameters:
    F, G = one(s), two(s)
    c = Q(1)+s**4/Q(2)
    for M in (F, G):
        require(determinant(M)==1, 'unit determinant')
        require(trace(M)==2-s*s, 'shared trace')
    K = mat_scale(matadd(matmul(transpose(F), F), matmul(transpose(G), G)), Q(1, 2))
    require(K == ((c, Q(0)), (Q(0), c)), 'scalar mean Gram matrix')
    for y in initials:
        require((normsq(matvec(F,y))+normsq(matvec(G,y)))/2 == c*normsq(y), 'conditional exact norm')

# An exact 2^n-sequence enumeration of the independent fair order choices.
for s in [Q(1,2), Q(1), Q(3,2), Q(3)]:
    F, G = one(s), two(s)
    c = Q(1)+s**4/Q(2)
    for y0 in [(Q(1),Q(0)), (Q(1),Q(1))]:
        for n in range(0,9):
            t = Q(0)
            for seq in product([F,G], repeat=n):
                y = y0
                for M in seq:
                    y = matvec(M,y)
                t += normsq(y)
            require(t/Q(2**n) == c**n*normsq(y0), 'exact all-sequence mean')

def f(x):
    return x*x*x-8*x*x+4*x-16

# Two explicit opposite-direction stability witnesses.
s, q = Q(1), Q(9,10)
c = 1+s**4/Q(2)
require(q*q*c == Q(243,200), 'random instability witness')
require(q < 1, 'both frozen orders stable at s=1')
s = Q(3)
c = 1+s**4/Q(2)
require(c/Q(44) == Q(83,88), 'random stability witness')
require(Q(83,88)<1, 'strict mean-square decay')
require((47+21*sqrt(5))/2>44, 'frozen instability witness')

# The key numerator sign and the unique crossing above x=4.
require(f(Q(4)) == -64, 'cubic at x=4')
require(f(Q(8)) == 16, 'cubic at x=8')
require(3*4*4-16*4+4 == -12, 'first derivative at left endpoint')
require(6*4-16 >0, 'positive increasing derivative beyond 4')
lo, hi = 4., 8.
for _ in range(120):
    mid = (lo+hi)/2
    if f(mid)>0: hi=mid
    else: lo=mid
xstar = (lo+hi)/2
sstar=sqrt(xstar)
require(abs(xstar-7.75025958832556)<2e-13, 'x crossover')
require(abs(sstar-2.783928804464216)<2e-13, 's crossover')
for sx in [2.0001, 2.1, 2.5, 2.783, sstar, 2.785, 3, 5, 10]:
    x=sx*sx
    R=(x-2+sx*sqrt(x-4))/2
    c=1+x*x/2
    lhs=(R*R+1/(R*R))-(c+1/c)
    rhs=x*f(x)/(2*(x*x+2))
    require(abs(lhs-rhs)<1e-8*max(1,abs(lhs)), 'cubic sign identity')
    if abs(sx-sstar)>1e-7:
        require((R*R>c) == (sx>sstar), 'unique crossover sign')

# Below and above the crossover, exhibit damping parameters strictly between thresholds.
for sx in [Q(1,2),Q(1),Q(2),Q(5,2),Q(3),Q(4),Q(8)]:
    sf=float(sx); x=sf*sf
    R=1. if sf<=2 else (x-2+sf*sqrt(x-4))/2
    random_threshold=log(1+x*x/2)/4
    fixed_threshold=log(R)/2
    require((random_threshold>fixed_threshold)==(sf<sstar), 'threshold ordering')
    amid=(random_threshold+fixed_threshold)/2
    random_amp=exp(-4*amid)*(1+x*x/2)
    fixed_amp=exp(-4*amid)*R**2
    require((random_amp>1)==(sf<sstar), 'random stable side')
    require((fixed_amp>1)==(sf>sstar), 'frozen stable side')

print('VERIFICATION_OK', CHECKS, 'checks', 'x_star', f'{xstar:.15f}', 's_star', f'{sstar:.15f}')
