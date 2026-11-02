#!/usr/bin/env python3
"""Independent exact checks of finite random-refresh coverage-cycle moments.
All fractions remain rational.  Requires only the Python standard library.
"""
from fractions import Fraction as Q
from math import comb, factorial, exp, sqrt, log


def linear_solve(a, b):
    n = len(b)
    x = [list(row) + [y] for row, y in zip(a, b)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if x[i][k] != 0)
        x[k], x[pivot] = x[pivot], x[k]
        d = x[k][k]
        x[k] = [z/d for z in x[k]]
        for i in range(n):
            if i != k:
                d = x[i][k]
                x[i] = [z - d*w for z, w in zip(x[i], x[k])]
    return [x[i][-1] for i in range(n)]


def independent_birth_death_cycle(m, p):
    q = 1-p
    mat = [[Q(int(i == j)) for j in range(m)] for i in range(m)]
    for y in range(1,m+1):
        up = Q(m-y,m)*p
        down = Q(y,m)*q
        mat[y-1][y-1] -= Q(1)-up-down
        if y > 1:
            mat[y-1][y-2] -= down
        if y < m:
            mat[y-1][y] -= up
    h = linear_solve(mat,[Q(1)]*m)
    # For second moments, E[(1+T')**2]=1+2 E[T']+E[T'**2].
    r = [2*h[y-1]-1 for y in range(1,m+1)]
    s = linear_solve(mat,r)
    mean = 1/p + h[0]
    var = (1-p)/p**2 + s[0]-h[0]**2
    return mean,var


def spectral_cycle(m,p):
    q=1-p
    weights=[Q(comb(m,j))*q**(m-j)*p**j for j in range(m+1)]
    pi=weights[0]
    r=sum((weights[j]/j for j in range(1,m+1)), Q(0))*m
    mean=1/(p*pi)
    cv2=(2-p)*pi + 2*p*r - 1
    return mean,mean**2*cv2

checks=0
for m in range(1,9):
    for p in (Q(1,10),Q(1,4),Q(2,5),Q(1,2),Q(4,5),Q(9,10)):
        a=independent_birth_death_cycle(m,p)
        b=spectral_cycle(m,p)
        assert a == b, (m,p,a,b)
        assert a[0] > 0 and a[1]>=0
        checks+=3

# Direct elementary verification of binomial return identity against
# exhaustive random-refresh transition powers on absent-count states.
for m in range(1,7):
    for p in (Q(1,3),Q(3,7)):
        q=1-p
        dist=[Q(0)]*(m+1)
        dist[0]=1
        for t in range(0,12):
            spectral=sum((Q(comb(m,j))*q**(m-j)*p**j * Q(m-j,m)**t for j in range(m+1)),Q(0))
            assert dist[0] == spectral, (m,p,t,dist[0],spectral)
            checks+=1
            future=[Q(0)]*(m+1)
            for y in range(m+1):
                up=Q(m-y,m)*p
                down=Q(y,m)*q
                future[y]+=dist[y]*(1-up-down)
                if y<m:future[y+1]+=dist[y]*up
                if y>0:future[y-1]+=dist[y]*down
            dist=future

# Strict negativity of the derivative of the critical shape's auxiliary
# derivative is an exact power-series fact proved in the accompanying text.
# The following numerical checks only check brackets and illustrations.
def A(c):
    term=1.0
    total=0.0
    for j in range(1,300):
        term*=c/j
        total+=term/j
        if j>c+15 and term<1e-16: break
    return total

def V(c):
    return 2*exp(-c)*(1+c*A(c))-1

def g(c):
    return (1-c)*A(c)+exp(c)-2

brackets=[(0.53858,0.53859),(3.86837,3.86838)]
for lo,hi in brackets:
    assert g(lo)*g(hi)<0
    checks+=1
assert (V(0.1)<1 and V(1)<1 and V(2)>1 and V(6)>1 and V(30)>1)
checks+=1
print(f'VERIFY_OK {checks} exact rational and numerical assertions')
