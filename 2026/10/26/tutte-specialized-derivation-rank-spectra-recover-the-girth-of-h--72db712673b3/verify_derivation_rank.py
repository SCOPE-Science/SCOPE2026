"""Independent finite-field derivation-space and rank-distribution checks.

Runs with Python 3 standard library. Only prime fields are required for the
independent matrix calculation; theorem and formula cover every prime power.
"""
from itertools import product
from collections import Counter
from math import comb


def rank_mod(a, p):
    if not a:
        return 0
    a = [list(map(lambda v: v % p, row)) for row in a]
    n = len(a)
    m = len(a[0])
    r = 0
    for j in range(m):
        piv = next((i for i in range(r, n) if a[i][j]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        z = pow(a[r][j], -1, p)
        a[r] = [(z * v) % p for v in a[r]]
        for i in range(r + 1, n):
            if a[i][j]:
                c = a[i][j]
                a[i] = [(v - c * w) % p for v, w in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def nullspace_mod(rows, nv, p):
    a = [row[:] for row in rows if any(row)]
    pivots = []
    r = 0
    for c in range(nv):
        idx = next((i for i in range(r, len(a)) if a[i][c] % p), None)
        if idx is None:
            continue
        a[r], a[idx] = a[idx], a[r]
        inv = pow(a[r][c] % p, -1, p)
        a[r] = [(inv * x) % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] % p:
                mult = a[i][c] % p
                a[i] = [(u - mult*v) % p for u, v in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    out = []
    for free in (j for j in range(nv) if j not in pivots):
        x = [0]*nv
        x[free] = 1
        for i, pivot in enumerate(pivots):
            x[pivot] = -a[i][free] % p
        out.append(x)
    return out


def all_derivation_ranks(vertices, edges, p):
    """Solve Leibniz equations, without assuming any derivation parametrization."""
    m = len(edges)
    d = vertices + m
    mult = {}
    for v in range(vertices):
        mult[v,v] = v
    for j,(u,v) in enumerate(edges):
        mult[u,vertices+j] = vertices+j
        mult[vertices+j,v] = vertices+j
    rows=[]
    # D(basis_a*basis_b) = D(basis_a)*basis_b + basis_a*D(basis_b)
    # D output coordinate t of input s is variable at t*d+s.
    for a in range(d):
        for b in range(d):
            for t in range(d):
                row=[0]*(d*d)
                if (a,b) in mult:
                    row[t*d + mult[a,b]] += 1
                for s in range(d):
                    if mult.get((s,b)) == t:
                        row[s*d+a] -= 1
                    if mult.get((a,s)) == t:
                        row[s*d+b] -= 1
                if any(z%p for z in row):
                    rows.append([v%p for v in row])
    basis=nullspace_mod(rows, d*d, p)
    assert len(basis)==2*m,(vertices,edges,p,len(basis))
    hist=Counter()
    for coefs in product(range(p), repeat=len(basis)):
        flat=[0]*(d*d)
        for c,b in zip(coefs,basis):
            if c:
                for idx,entry in enumerate(b):
                    flat[idx]=(flat[idx]+c*entry)%p
        mat=[[flat[i*d+j] for j in range(d)] for i in range(d)]
        hist[rank_mod(mat,p)]+=1
    assert sum(hist.values()) == p**(2*m)
    return hist


def formula_hist(vertices,edges,q):
    m=len(edges)
    result=Counter()
    # Expand factor (1+q(q-1)t)^(m-|B|) in each support B.
    for mask in range(1<<m):
        B=[edges[i] for i in range(m) if mask>>i & 1]
        parent=list(range(vertices))
        def root(i):
            while parent[i]!=i:
                i=parent[i]
            return i
        for u,v in B:
            parent[root(u)]=root(v)
        r=vertices-len({root(i) for i in range(vertices)})
        k=len(B)
        for j in range(m-k+1):
            result[r+j]+=(q-1)**k*comb(m-k,j)*(q*(q-1))**j
    return result


def examples():
    return [
      ("single",2,[(0,1)],3),
      ("disconnected",4,[(0,2),(1,3)],3),
      ("star",4,[(0,1),(0,2),(0,3)],3),
      ("path",4,[(0,2),(1,2),(1,3)],3),
      ("fourcycle",4,[(0,2),(0,3),(1,2),(1,3)],2),
      ("fourcycle_q3",4,[(0,2),(0,3),(1,2),(1,3)],3),
      ("cycleplusleaf",5,[(0,2),(0,3),(1,2),(1,3),(0,4)],2),
      ("sixcycle",6,[(0,3),(1,3),(1,4),(2,4),(2,5),(0,5)],2),
    ]


def main():
    for name,n,edges,p in examples():
        got=all_derivation_ranks(n,edges,p)
        want=formula_hist(n,edges,p)
        assert got==want,(name,got,want)
        print("PASS",name,"q",p,"derivations",p**(2*len(edges)),"ranks",sorted(got.items()))
        if name=="fourcycle":
            target=Counter({0:1,1:12,2:54,3:109,4:80})
            assert got==target
        if name=="fourcycle_q3":
            target=Counter({0:1,1:32,2:384,3:2064,4:4080})
            assert got==target
    # Additional q-agnostic algebraic combinatorial identity tests.
    for q in [2,3,4,5,7,9]:
        for n,edges in [(4,[(0,2),(0,3),(1,2),(1,3)]),
                        (6,[(0,3),(1,3),(1,4),(2,4),(2,5),(0,5)]),
                        (5,[(0,3),(0,4),(1,3),(1,4),(2,4)])]:
            hist=formula_hist(n,edges,q)
            assert sum(hist.values())==q**(2*len(edges))
            if len(edges)==4:
                base=Counter({j:comb(4,j)*(q*q-1)**j for j in range(5)})
                diff=hist-base
                assert diff[3]==(q-1)**4
    print("VERIFY_OK")

if __name__=='__main__':
    main()
