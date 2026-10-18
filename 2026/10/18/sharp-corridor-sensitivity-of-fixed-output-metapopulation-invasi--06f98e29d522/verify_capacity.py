"""Independent finite checks for a degree-normalized patch-invasion theorem.

Requires Python 3 and numpy. This code is corroboration; the universal
bound and full attainable range are proved algebraically in RESULT.md.
"""
import itertools
import math
import numpy as np

TOL = 1e-10

def connected(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    found = {0}
    stack = [0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in found:
                found.add(v)
                stack.append(v)
    return len(found) == n


def rho(n, edges, qualities):
    deg = [0] * n
    for a,b in edges:
        deg[a] += 1
        deg[b] += 1
    h = np.zeros((n,n),dtype=float)
    for a,b in edges:
        w = math.sqrt(qualities[a] * qualities[b] / (deg[a] * deg[b]))
        h[a,b] = h[b,a] = w
    return float(np.linalg.eigvalsh(h)[-1])


def path_ratio(b):
    return (1 + math.sqrt(1+8*b))/(4*math.sqrt(b))


def test_three_patch():
    path = [(0,1),(1,2)]
    triangle = [(0,1),(1,2),(0,2)]
    for b in (1e-8,0.01,0.25,1,4,100,1e8):
        q = [1,b,1]
        a = rho(3,path,q)
        z = rho(3,triangle,q)
        assert abs(a-math.sqrt(b)) <= 2e-10 * (1+math.sqrt(b))
        assert abs(z-(1+math.sqrt(1+8*b))/4) <= 2e-10*(1+z)
        assert abs(z/a-path_ratio(b)) <= 2e-10*(1+z/a)
    assert path_ratio(4) < 1 and path_ratio(0.25) > 1
    assert 1/math.sqrt(2) < path_ratio(1e9) < .708
    assert path_ratio(1e-9) > 1000
    print('three-patch closed forms, signs, and sharp limits: verified')


def census():
    checked=0
    lows=(9.0,None)
    highs=(0.0,None)
    for n in (3,4,5):
        pairs=list(itertools.combinations(range(n),2))
        for mask in range(1,1<<len(pairs)):
            edges = [e for j,e in enumerate(pairs) if mask&(1<<j)]
            if len(edges)<n-1 or len(edges)==len(pairs) or not connected(n,edges):
                continue
            missing=[e for e in pairs if e not in edges]
            for qtuple in itertools.product((1/3,1,3),repeat=n):
                baseline=rho(n,edges,qtuple)
                for pair in missing:
                    ratio = rho(n, edges+[pair],qtuple)/baseline
                    assert ratio > 1/math.sqrt(2)-TOL
                    checked+=1
                    if ratio < lows[0]: lows=(ratio,(n,edges,qtuple,pair))
                    if ratio > highs[0]: highs=(ratio,(n,edges,qtuple,pair))
    print('connected graph/positive-quality/added-edge comparisons:',checked)
    print('sample smallest ratio:',lows[0])
    print('sample largest ratio:',highs[0])
    assert checked>40000

if __name__=='__main__':
    test_three_patch()
    census()
    print('All numerical tests passed. Infinite proof: see RESULT.md.')
