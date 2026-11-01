"""Supplementary finite checks of simultaneous square-zero q-range realization.

Run: python3 VERIFY.py. Uses only the Python 3 standard library.
The exact theorem for arbitrary Hilbert dimension is established analytically.
"""
import cmath
import math
import random

rng = random.Random(20261023)
checks = 0


def test(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def cnorm(x):
    return math.sqrt(sum(abs(z)**2 for z in x))


def dot(x, y):
    # Usual conjugate-first convention; the mathematical <x,y> is dot(y,x).
    return sum(z.conjugate() * w for z, w in zip(x, y))


def inner_first(x, y):
    return dot(y, x)


def cval(q):
    return (1 + math.sqrt(max(0.0, 1 - abs(q)**2))) / 2


def rand_complex():
    return complex(rng.gauss(0, 1), rng.gauss(0, 1))


def f_apply(values, s, x):
    # F(s) = [[0,D(s)],[0,0]] where D(s) is diagonal.
    m = len(values)
    return [values[i][s]*x[m+i] for i in range(m)] + [0j]*m


for m in [1, 2, 3, 7, 11]:
    values = [[rand_complex() for s in range(8)] for i in range(m)]
    for s in range(8):
        basis = [[int(i == j)+0j for i in range(2*m)] for j in range(2*m)]
        for x in basis:
            test(cnorm(f_apply(values,s,f_apply(values,s,x))) == 0.0,
                 'square-zero matrix')
            for t in range(8):
                test(cnorm(f_apply(values,s,f_apply(values,t,x))) == 0.0,
                     'pairwise annihilation')
    for rho in [0.0, 0.1, 0.5, 0.9, 1.0]:
        for angle in [0.0, 0.91, 2.2]:
            q = rho*cmath.exp(1j*angle)
            for trial in range(32):
                x = [rand_complex() for i in range(2*m)]
                xx = cnorm(x)
                x = [z/xx for z in x]
                w = [rand_complex() for i in range(2*m)]
                overlap = dot(x,w)
                w = [v-overlap*u for u,v in zip(x,w)]
                ww = cnorm(w)
                w = [z/ww for z in w]
                r = math.sqrt(max(0.0,1-rho*rho))
                y = [q.conjugate()*u+r*v for u,v in zip(x,w)]
                test(abs(inner_first(x,y)-q)<1e-9, 'q constraint')
                test(abs(cnorm(y)-1)<1e-9, 'unit second vector')
                coeff = [x[m+i]*y[i].conjugate() for i in range(m)]
                test(sum(abs(a) for a in coeff)<=cval(q)+1e-9,
                     'sharp coefficient budget')
                for s in range(8):
                    actual = inner_first(f_apply(values,s,x),y)
                    expected = sum(coeff[i]*values[i][s] for i in range(m))
                    test(abs(actual-expected)<1e-9, 'joint coefficient formula')
            for j in range(m):
                r=math.sqrt(max(0.0,1-rho*rho))
                t=(1+r)/2
                x=[0j]*(2*m)
                w=[0j]*(2*m)
                x[j],x[m+j]=math.sqrt(1-t),math.sqrt(t)
                w[j],w[m+j]=math.sqrt(t),-math.sqrt(1-t)
                y=[rho*u+r*v for u,v in zip(x,w)]
                test(abs(inner_first(x,y)-rho)<1e-9,
                     'real optimizing q constraint')
                for s in range(8):
                    test(abs(inner_first(f_apply(values,s,x),y)
                             -cval(q)*values[j][s])<1e-9,
                         'exact real q ray realization')
                if rho > 0:
                    unit = cmath.exp(-1j*angle)
                    xx=[x[i]*(unit if i>=m else 1) for i in range(2*m)]
                    yy=[y[i]*(unit if i>=m else 1)*unit for i in range(2*m)]
                    test(abs(inner_first(xx,yy)-q)<1e-9,
                         'complex optimizing q constraint')
                    for s in range(8):
                        test(abs(inner_first(f_apply(values,s,xx),yy)
                                 -cval(q)*values[j][s])<1e-9,
                             'exact complex q ray realization')

for j in range(101):
    rho=j/100
    r=math.sqrt(max(0.0,1-rho*rho))
    t=(1+r)/2
    x=[math.sqrt(1-t),math.sqrt(t)]
    w=[math.sqrt(t),-math.sqrt(1-t)]
    y=[rho*u+r*v for u,v in zip(x,w)]
    nx=[x[1],0.0]
    test(abs(inner_first(nx,y)-cval(rho))<1e-9,
         'two-coordinate sharp coefficient')

print('PASS',checks,'supplementary deterministic assertions')
