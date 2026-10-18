"""Reproducible numerical and exact-convolution checks for a six-mode Fourier norm.
Python 3 standard library only. Finite checks supplement, and do not replace, the proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import cmath
import math
import random

S = ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
V = (0,3,5)
E = (4,2,1)  # edge midpoint opposite each member of V
pairs=defaultdict(list)
for i,j in product(range(6),repeat=2):
    s=(S[i][0]+S[j][0],S[i][1]+S[j][1])
    pairs[s].append((i,j))

def moment(v):
    return sum(abs(sum(v[i]*v[j] for i,j in q))**2 for q in pairs.values())

def bound_parts(v):
    x=[abs(v[i]) for i in V]
    y=[abs(v[i]) for i in E]
    X=sum(t*t for t in x)
    Y=sum(t*t for t in y)
    T=X+Y
    poly=2*T*T-sum(t**4 for t in x+y)
    cross=4*sum(x[(i+1)%3]*x[(i+2)%3]*y[i]**2 for i in range(3))
    tri=8*sum(x)*math.prod(y)
    return poly+cross+tri, 5*T*T/3+2*X*Y+8*math.sqrt(X)*Y**1.5/3

def symbolic_exact():
    # Compare coefficient dictionaries in six real indeterminates.
    P=defaultdict(int)
    def add(indices,coef):
        k=tuple(indices.count(i) for i in range(6)); P[k]+=coef
    for q in pairs.values():
        for i,j in q:
            for k,l in q: add([i,j,k,l],1)
    Q=defaultdict(int)
    def aq(indices,coef):
        key=tuple(indices.count(i) for i in range(6));Q[key]+=coef
    for i,j in product(range(6),repeat=2): aq([i,i,j,j],2)
    for i in range(6): aq([i]*4,-1)
    for i in range(3): aq([V[(i+1)%3],V[(i+2)%3],E[i],E[i]],4)
    for i in range(3): aq([V[i],*E],8)
    assert {k:v for k,v in P.items() if v}=={k:v for k,v in Q.items() if v}
    return len(P)

def f(r):
    return (15+48*r*r+24*r**3+15*r**4)/(9*(1+r*r)**2)

def evaluate_grid(v,n):
    total=0.
    for i,j in product(range(n),repeat=2):
        z=cmath.exp(2j*math.pi*i/n)
        w=cmath.exp(2j*math.pi*j/n)
        poly=sum(c*z**u*w**t for c,(u,t) in zip(v,S))
        total+=abs(poly)**4
    return total/(n*n)

def main():
    monomials=symbolic_exact()
    rng=random.Random(61029)
    lo,hi=1.,2.
    for _ in range(100):
        m=(lo+hi)/2
        if 2*m**3+3*m*m-6*m-3 > 0:hi=m
        else:lo=m
    rho=(lo+hi)/2
    K=f(rho)
    assert 1.40225578864 < rho < 1.40225578865
    assert 2.94923561204 < K < 2.94923561206
    worst=0.0
    for _ in range(600):
        c=[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for j in range(6)]
        Q=moment(c)
        absQ,rawmax=bound_parts(c)
        norm=sum(abs(z)**2 for z in c)
        assert Q<=absQ+1e-8*norm**2
        assert absQ<=rawmax+1e-8*norm**2
        assert Q<=K*norm*norm+1e-8*norm**2
        worst=max(worst,Q/(norm*norm))
    extrem=[]
    for i,(u,t) in enumerate(S):
        mag=rho if i in E else 1.
        extrem.append(mag*cmath.exp(1j*(.2+u*.4-t*.5)))
    T=sum(abs(c)**2 for c in extrem)
    predicted=K*T*T
    assert abs(moment(extrem)-predicted)<2e-11*predicted
    for n in (5,6,7,9):
        measured=evaluate_grid(extrem,n)
        assert abs(measured-predicted)<2e-11*predicted
    assert evaluate_grid([rho if i in E else 1.0 for i in range(6)],4)>predicted+1e-4
    print('PASS exact coefficient dictionary with',monomials,'monomial types')
    print('PASS 600 random complex coefficients and analytic majorant')
    print('PASS equality with nonuniform magnitudes, arbitrary character phases')
    print('PASS nonalias finite grids N=5,6,7,9; alias excess at N=4')
    print('rho = %.15f, sharp fourth-power constant = %.15f'%(rho,K))
    print('maximum sampled random normalized moment = %.15f'%worst)

if __name__=='__main__': main()
