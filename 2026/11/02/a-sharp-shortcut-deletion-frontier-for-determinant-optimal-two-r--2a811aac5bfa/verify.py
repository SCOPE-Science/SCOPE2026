"""Independent determinant and optimization checks for a priced theta network.

Requirements: Python 3, NumPy, SciPy, SymPy.
Run: python verify.py
"""
import math
import random
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize
import sympy as sp


def graph(a, b):
    """A length-a arm, a length-b arm, and one direct terminal edge."""
    assert a >= 2 and b >= 2
    edges = []
    paths = []
    node = 2
    for length in (a, b):
        vertices = [0] + list(range(node, node + length - 1)) + [1]
        node += length - 1
        paths.append(list(range(len(edges), len(edges) + length)))
        edges += list(zip(vertices[:-1], vertices[1:]))
    edges.append((0, 1))
    return node, edges, paths


def determinant(a, b, weights):
    n, edges, _ = graph(a, b)
    L = np.zeros((n, n))
    for (u, v), w in zip(edges, weights):
        L[u, u] += w
        L[v, v] += w
        L[u, v] -= w
        L[v, u] -= w
    return float(np.linalg.det(L[1:, 1:]))


def exact_determinant(a, b, weights):
    n, edges, _ = graph(a, b)
    L=sp.zeros(n)
    for (u,v),w in zip(edges,weights):
        L[u,u]+=w; L[v,v]+=w; L[u,v]-=w; L[v,u]-=w
    return L[1:,1:].det()


def formula(a, b, p, q, r, B=1.):
    A = a*a*p
    C = b*b*q
    n = a+b
    disc = (a*C+b*A)**2 - 4*(n-1)*A*C
    # Stable smaller quadratic root
    rc = 2*A*C/(a*C+b*A+math.sqrt(max(0., disc)))
    if r < rc:
        x = B*a*(a-1)/((n-1)*(A-r))
        y = B*b*(b-1)/((n-1)*(C-r))
        z = B/(n-1)*(1/r-(a-1)/(A-r)-(b-1)/(C-r))
    else:
        # Positive root of (b-1)p t^2 + (a p - b q)t - (a-1)q = 0.
        h = a*p - b*q
        d = math.sqrt(h*h+4*(a-1)*(b-1)*p*q)
        t = 2*(a-1)*q/(h+d)
        y = B/(a*p*t+b*q)
        x = t*y
        z = 0.
    return rc, x, y, z


def run():
    rng = random.Random(20261026)
    counts = dict(exact=0, determinant=0, feasible=0, optimized=0, threshold=0)
    # Matrix-Tree theorem with a genuinely non-constant assignment on each arm.
    for a,b in [(2,2),(2,3),(3,4),(5,2)]:
        n, edges, _ = graph(a,b)
        ws = [sp.Rational(i+2, i+5) for i in range(len(edges))]
        L=sp.zeros(n)
        for (u,v),w in zip(edges,ws):
            L[u,u]+=w; L[v,v]+=w; L[u,v]-=w; L[v,u]-=w
        ua=ws[:a]; vb=ws[a:a+b]; z=ws[-1]
        ea=sum(sp.prod(ua[:i]+ua[i+1:]) for i in range(a))
        eb=sum(sp.prod(vb[:i]+vb[i+1:]) for i in range(b))
        polynomial=sp.factor(z*ea*eb+ea*sp.prod(vb)+sp.prod(ua)*eb)
        assert sp.factor(L[1:,1:].det()-polynomial)==0
        counts['exact']+=1
    # Boundary case a=2,b=3,p=q=B=1,r=3/2 has x=y=1/5, z=0.
    rc,x,y,z=formula(2,3,1,1,1.5)
    assert abs(rc-1.5)<1e-13 and abs(x-.2)<1e-13 and abs(y-.2)<1e-13 and z==0
    assert exact_determinant(2,3,[sp.Rational(1,5)]*5+[sp.S(0)])==sp.Rational(1,125)
    counts['exact']+=1
    # Interior case with exact optimal weights and tree determinant.
    rc,x,y,z=formula(2,3,1,1,1)
    assert abs(x-1/6)<1e-13 and abs(y-3/16)<1e-13 and abs(z-5/48)<1e-13
    assert exact_determinant(2,3,[sp.Rational(1,6)]*2+[sp.Rational(3,16)]*3+[sp.Rational(5,48)])==sp.Rational(9,1024)
    counts['exact']+=1
    for a in range(2,6):
        for b in range(2,6):
            for k in range(5):
                p=rng.uniform(.4,2.2); q=rng.uniform(.4,2.2)
                B=rng.uniform(.7,2.5)
                rc,_,_,_=formula(a,b,p,q,1,B)
                r=rc*[.25,.8,1.,1.4,4.][k]
                rc,x,y,z=formula(a,b,p,q,r,B)
                prices=np.array([p]*a+[q]*b+[r]); ws=np.array([x]*a+[y]*b+[z]);
                assert x>0 and y>0 and z>=0
                assert abs(np.dot(prices,ws)-B)<1e-10
                if k==2: assert abs(z)<1e-14
                counts['threshold']+=1
                direct=determinant(a,b,ws)
                closed=x**(a-1)*y**(b-1)*(a*y+b*x+a*b*z)
                assert abs(direct-closed)<1e-8*max(direct,closed)
                counts['determinant']+=1
                for j in range(15):
                    # Unrestricted individual edge conductances, unequal inside arms.
                    rates=np.array([rng.expovariate(1) for _ in ws])
                    rates=B*rates/np.dot(prices,rates)
                    cand=determinant(a,b,rates)
                    assert cand < direct+1e-8*max(1.,direct), (a,b,k,j,cand,direct)
                    counts['feasible']+=1
                if a<=4 and b<=4 and k in (0,2,4):
                    from scipy.optimize import minimize
                    def objective(w):
                        value=determinant(a,b,w)
                        return -math.log(max(value,1e-200))
                    ans=minimize(objective,B/(len(ws)*prices),method='SLSQP',
                                 constraints=[{'type':'eq','fun':lambda w: np.dot(prices,w)-B}],
                                 bounds=[(0,None)]*len(ws),
                                 options={'maxiter':700,'ftol':1e-11})
                    assert ans.success, (a,b,k,ans.message)
                    assert abs(math.exp(-ans.fun)-direct)<2e-6*max(1.,direct)
                    counts['optimized']+=1
    print('VERIFIED',counts)
    return counts


if __name__ == '__main__':
    run()
