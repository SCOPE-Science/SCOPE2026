"""Numerical and symbolic regression checks for a universal leaf-corona mixing formula.

Requires Python 3.10+, numpy, scipy, sympy, networkx. This is finite
verification only; the theorem's proof is contained in RESULT.md.
"""
import math
import numpy as np
import networkx as nx
import sympy as sp
from scipy.optimize import minimize_scalar


def optimum(alpha, degree):
    c = alpha / (2.0 * degree)
    s = math.sqrt(2.0 * c)
    den = 2.0 + (1.0 - c) * s
    a = (c + (1.0 - c) * s) / den
    b = (1.0 - a) / degree
    mu = (2.0 - 2.0*c + s) / den
    return a, b, mu


def make_transition(A, a, b):
    n = len(A)
    degree = np.sum(A, axis=1)
    P = np.zeros((2*n, 2*n))
    P[:n, :n] = b*A + np.diag(1-a-b*degree)
    P[n:, n:] = np.eye(n)*(1-a)
    P[:n, n:] = a*np.eye(n)
    P[n:, :n] = a*np.eye(n)
    return P


def slem(P):
    eig = np.linalg.eigvalsh(P)
    return max(abs(eig[:-1]))


def graph_cases():
    for n in range(3, 16):
        yield f'cycle-{n}', nx.cycle_graph(n)
    for n in range(2, 14):
        yield f'complete-{n}', nx.complete_graph(n)
    for d in range(1, 6):
        yield f'cube-{d}', nx.hypercube_graph(d)
    for n in range(2, 10):
        yield f'biclique-{n}', nx.complete_bipartite_graph(n, n)
    yield 'Petersen', nx.petersen_graph()
    for n in (5, 7, 9):
        yield f'Johnson-{n}', nx.johnson_graph(n, 2) if hasattr(nx, 'johnson_graph') else johnson(n)


def johnson(n):
    import itertools
    combos = list(itertools.combinations(range(n), 2))
    G = nx.Graph()
    G.add_nodes_from(combos)
    for i, x in enumerate(combos):
        for y in combos[i+1:]:
            if len(set(x) & set(y)) == 1:
                G.add_edge(x, y)
    return G


def check():
    count = 0
    c, z = sp.symbols('c z', positive=True, real=True)
    d = 2+(1-c)*z
    a = (c+(1-c)*z)/d
    t = a/(1-a)
    assert sp.simplify(t - (c+(1-c)*z)/(2-c)) == 0
    # Rationalized stationarity identity after setting z^2=2c.
    stationarity = sp.together((t-c*c)**2 - (1-c)**2*(t*t+c*c))
    assert sp.simplify(sp.factor(stationarity).subs(c,z*z/2)) == 0
    count += 2
    for name, G in graph_cases():
        A = nx.to_numpy_array(G)
        n = len(A)
        degrees = np.sum(A, axis=1)
        assert np.max(degrees)-np.min(degrees)<1e-9
        deg = float(degrees[0])
        eigL = np.linalg.eigvalsh(np.diag(degrees)-A)
        alpha = float(eigL[1]); beta = float(eigL[-1]);
        assert 0 < alpha <= 2*deg+1e-8
        a0, b0, mu = optimum(alpha,deg)
        assert a0 > 0 and b0 > 0 and a0 <=0.5+1e-10
        assert abs(a0+deg*b0-1)<1e-11
        P = make_transition(A,a0,b0)
        assert np.min(P)>-1e-10
        assert np.max(abs(P-P.T)) < 1e-12
        assert np.max(abs(P.sum(axis=1)-1))<1e-10
        assert abs(slem(P)-mu)<1e-9, (name,slem(P),mu)
        assert mu<1
        count += 8
        def spectral(a, b):
            return slem(make_transition(A,a,b))
        def f(a):
            return spectral(a,(1-a)/deg)
        res = minimize_scalar(f,bounds=(0.00001,0.99999),method='bounded',options={'xatol':1e-12})
        assert res.fun >= mu-4e-8, (name,res.fun,mu)
        assert abs(res.x-a0)<1e-5, (name, res.x,a0)
        count += 2
        for a1 in np.linspace(0.08,0.93,7):
            for r in [0.2, 0.5, 0.8, 1.0]:
                b1 = (1-a1)/deg*r
                assert spectral(a1,b1)>=mu-1e-9, (name,a1,b1,spectral(a1,b1),mu)
                count+=1
        # Directional sample of asymmetry (does not certify global optimality).
        rng=np.random.default_rng(1729+n)
        for j in range(4):
            W = np.zeros((2*n,2*n))
            for u, v in G.edges():
                uu=list(G.nodes()).index(u); vv=list(G.nodes()).index(v)
                w=rng.uniform(0.01,0.9)/(deg+1)
                W[uu,vv]=W[vv,uu]=w
            for i in range(n):
                w=rng.uniform(0.01,0.9)/(deg+1)
                W[i,n+i]=W[n+i,i]=w
            maxrow=max(W.sum(axis=1))
            W *= .99/maxrow
            P2=W+np.diag(1-W.sum(axis=1))
            assert spectral(a0,b0)<=slem(P2)+1e-9
            count+=1
        print(name,'alpha',round(alpha,8),'a',round(a0,8),'b',round(b0,8),'mu',round(mu,8))
    # Exact K2 base = P4, and asymptotic clique limit.
    assert abs(optimum(2,1)[2]-2**-.5)<1e-12
    assert abs(optimum(10000,9999)[2]-0.8)<1e-4
    count+=2
    print('PASS',count,'symbolic/numeric grouped assertions')

if __name__=='__main__':
    check()
