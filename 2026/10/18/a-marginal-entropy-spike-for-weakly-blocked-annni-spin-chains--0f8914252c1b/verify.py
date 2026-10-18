"""Exact checks for blocked-state entropy in the one-dimensional ANNNI chain.

Requires Python 3.10+ and SymPy. No input data files are needed.
"""
import itertools
import sympy as sp

X = sp.Symbol('x')
WORDS = tuple(itertools.product((-1, 1), repeat=4))
INDEX = {w:i for i,w in enumerate(WORDS)}


def transfer(k):
    mat = sp.zeros(16)
    for a,b,c,d,e in itertools.product((-1, 1),repeat=5):
        if c*(b+d-k*(a+e)) >= 0:
            mat[INDEX[(a,b,c,d)], INDEX[(b,c,d,e)]] = 1
    return mat


def energy(spins,k):
    n = len(spins)
    return sum(-spins[i]*spins[(i+1)%n] + k*spins[i]*spins[(i+2)%n] for i in range(n))


def independent_count(n,k):
    count = 0
    for t in itertools.product((-1,1), repeat=n):
        en = energy(t,k)
        accepted = True
        for i in range(n):
            flipped = list(t)
            flipped[i] = -flipped[i]
            if energy(flipped,k) < en:
                accepted = False
                break
        count += accepted
    return count


def sccs(mat):
    graph = [[j for j in range(16) if mat[i,j]] for i in range(16)]
    back = [[j for j in range(16) if mat[j,i]] for i in range(16)]
    seen,order = set(),[]
    def dfs(v):
        seen.add(v)
        for w in graph[v]:
            if w not in seen: dfs(w)
        order.append(v)
    for v in range(16):
        if v not in seen: dfs(v)
    seen=set();groups=[]
    def dfs2(v,group):
        seen.add(v);group.append(v)
        for w in back[v]:
            if w not in seen:dfs2(w,group)
    for v in reversed(order):
        if v not in seen:
            g=[];dfs2(v,g);groups.append(sorted(g))
    return groups


def checker():
    specs = [
      ('low', sp.Rational(1,2), X**12*(X**2-X-1)*(X**2-X+1),
       [0,1,3,6,7,8,9,12,14,15],
       [10000000,6180340,10000000,6180340,10000000,10000000,6180340,10000000,6180340,10000000],(1618,1619)),
      ('threshold', sp.Integer(1), X**4*(X-1)**2*(X**5+X**3+X+1)*(X**5-X**3-2*X**2-X-1),
       [0,1,2,3,4,6,7,8,9,11,12,13,14,15],
       [9006898,6001313,2757411,10000000,4594679,7656122,9006898,9006898,7656122,4594679,10000000,2757411,6001313,9006898],(1665,1668)),
      ('high', sp.Integer(2), X**2*(X**7+X**5+X**3-X-1)*(X**7-X**5-2*X**4-X**3+X+1),
       [0,1,2,3,4,6,7,8,9,11,12,13,14,15],
       [4134611,6430094,3621368,10000000,5631906,8758668,6793204,6793204,8758668,5631906,10000000,3621368,6430094,4134611],(1554,1557)),
    ]
    total=0
    for label,k,polynomial,indices,v,(lo,hi) in specs:
        mat=transfer(k)
        assert sp.expand(mat.charpoly(X).as_expr()-polynomial)==0,(label,'charpoly')
        groups=sccs(mat)
        assert set(indices) in [set(g) for g in groups], (label,groups)
        core=mat.extract(indices,indices)
        vv=sp.Matrix(v)
        aa=core*vv
        assert all(lo*z < 1000*y < hi*z for y,z in zip(aa,vv)), (label,'Perron bounds')
        # Primitive: the directed core is irreducible (the SCC) and cycles
        # have gcd 1, certified here from trace of powers up to 16.
        from math import gcd
        cyclic=[n for n in range(1,17) if (core**n).trace()>0]
        g=0
        for n in cyclic:g=gcd(g,n)
        assert g==1, (label,'aperiodic',cyclic)
        for n in range(5,13):
            lhs=int((mat**n).trace())
            rhs=independent_count(n,k)
            assert lhs==rhs,(label,n,lhs,rhs)
            total+=2**n
        print(f'{label}: characteristic polynomial, largest SCC, rational Perron bounds, primitivity and n=5..12 trace/brute-force agreement PASS')
    assert 1665>1619>1557
    print(f'All PASS; verified {total} labelled spin configurations with independent Hamiltonian recomputation.')

if __name__=='__main__':checker()
