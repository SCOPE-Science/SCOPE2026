#!/usr/bin/env python3
"""Exact rational-number verification of the seven-edge banana singular-scheme Hilbert series.
Requires Python 3 and SymPy 1.14; no external data or network access.
"""
import itertools
from functools import lru_cache
import sympy as sp
from sympy.polys.orderings import monomial_key

N = 7
x = sp.symbols('x0:7')
f = sum(sp.prod(x[j] for j in range(N) if j != i) for i in range(N))
grad = [sp.diff(f, v) for v in x]
assert sp.Poly(f,*x).total_degree() == 6
G = sp.groebner(grad, *x, order='grevlex', domain=sp.QQ)
assert len(G.polys) == 51
assert all(G.reduce(g)[1] == 0 for g in grad)
# Verify that the GB has no accidental zero generator; SymPy's exact Buchberger algorithm
# establishes the ideal equality (all computations over QQ, not finite fields).
order = monomial_key('grevlex')
leads = tuple(max(p.monoms(), key=order) for p in G.polys)


def minimal(gens):
    items = sorted(set(gens), key=lambda t: (sum(t), t))
    out=[]
    for a in items:
        if not any(all(u >= v for u,v in zip(a,b)) for b in out):
            out.append(a)
    return tuple(sorted(out))


def plus(a,b,scale=1,shift=0):
    c=list(a)+[0]*max(0,len(b)+shift-len(a))
    for i,v in enumerate(b): c[i+shift] +=scale*v
    while len(c)>1 and c[-1]==0: c.pop()
    return tuple(c)

@lru_cache(maxsize=None)
def hilbert_numerator(n,gens):
    """Numerator over (1-t)^n of polynomial quotient by monomial ideal.
    Proved by the exact sequence for multiplication by the last variable.
    """
    if not gens: return (1,)
    if (0,)*n in gens: return (0,)
    assert n > 0
    mod = minimal(a[:-1] for a in gens if a[-1]==0)
    if all(a[-1]==0 for a in gens): return hilbert_numerator(n-1,mod)
    col = minimal(a[:-1]+(max(0,a[-1]-1),) for a in gens)
    left=hilbert_numerator(n-1,mod)
    right=hilbert_numerator(n,col)
    return plus(plus(left,left,scale=-1,shift=1),right,shift=1)

pj=hilbert_numerator(N,minimal(leads))
assert pj == (1,0,0,0,0,-7,0,6,0,0,21,-35,14),pj
# The radical of the Jacobian ideal is the squarefree ideal of degree five.
krad = minimal(tuple(int(i in c) for i in range(N))
               for c in itertools.combinations(range(N),5))
pk=hilbert_numerator(N,krad)
assert pk == (1,0,0,0,0,-21,35,-15),pk
num = plus(pj,pk,scale=-1)  # (1-t)^7 [H(S/J)-H(S/K)]
assert num == (0,0,0,0,0,14,-35,21,0,0,21,-35,14),num
# Divide numerator by (1-t)^4, leaving denominator (1-t)^3.
for _ in range(4):
    cumulative=[];r=0
    for v in num:
        r+=v;cumulative.append(r)
    assert cumulative[-1]==0
    num=tuple(cumulative[:-1])
assert num == (0,0,0,0,0,14,21,21,14),num

# Independent finite-dimensional consistency check: enumerate standard monomials.
def exponent_vectors(n,d):
    if n==1:
        yield (d,)
    else:
        for a in range(d+1):
            for rest in exponent_vectors(n-1,d-a):yield (a,)+rest

def outside(v,gens):
    return not any(all(a>=b for a,b in zip(v,g)) for g in gens)
for degree,expected in [(5,14),(6,63),(7,168),(8,343),(9,588)]:
    difference=sum(outside(a,minimal(leads)) - outside(a,krad)
                   for a in exponent_vectors(N,degree))
    assert difference == expected,(degree,difference)

# Four-variable transverse e_3 model; its reduced singular ideal is generated
# by the six pairwise coordinate products, whereas its Jacobian spans 4 quadrics.
y=sp.symbols('y0:4')
e3=sum(sp.prod(y[j] for j in range(4) if j!=i) for i in range(4))
Q=sp.groebner([sp.diff(e3,v) for v in y],*y,order='grevlex',domain=sp.QQ)
assert len([p for p in Q.polys if p.total_degree()==2])==4
assert sp.Matrix([[sp.Poly(sp.diff(e3,v),*y).coeff_monomial(y[i]*y[j])
                  for i,j in itertools.combinations(range(4),2)] for v in y]).rank()==4
# Every cubic monomial with support >=2 lies in the derivative ideal.
for a in exponent_vectors(4,3):
    if sum(v>0 for v in a)>=2:
        assert Q.reduce(sp.prod(v**e for v,e in zip(y,a)))[1] == 0
print('VERIFY_OK')
print('Jacobian GB elements:',len(G.polys))
print('Hilbert numerator S/J:',pj)
print('Hilbert numerator S/K:',pk)
print('Hilbert series of K/J = (14t^5+21t^6+21t^7+14t^8)/(1-t)^3')
print('Hilbert-polynomial difference = 35d^2 - 350d + 903')
