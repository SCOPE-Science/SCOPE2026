#!/usr/bin/env python3
import itertools
import sympy as sp

X = sp.symbols('x')


def connected(adj):
    n=len(adj)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in range(n):
            if adj[u][v] and v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==n


def canonical_code(adj):
    n=len(adj)
    best=None
    for p in itertools.permutations(range(n)):
        code=tuple(adj[p[i]][p[j]] for i in range(n) for j in range(i+1,n))
        if best is None or code<best:
            best=code
    return best


def unlabeled_connected(n):
    edges=list(itertools.combinations(range(n),2))
    seen=set(); out=[]
    for mask in range(1<<len(edges)):
        adj=[[0]*n for _ in range(n)]
        m=0
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                adj[u][v]=adj[v][u]=1
                m+=1
        if not connected(adj):
            continue
        code=canonical_code(adj)
        if code in seen:
            continue
        seen.add(code)
        out.append((m,adj,code))
    return out


def spectral_interval(adj):
    A=sp.Matrix(adj)
    poly=A.charpoly(X).as_poly()
    intervals=poly.intervals(eps=sp.Rational(1,10**16))
    roots=[]
    for (lo,hi),mult in intervals:
        roots.extend([(lo,hi)]*mult)
    # Adjacency matrices are real symmetric, so all roots are real.
    lo,hi=max(roots,key=lambda z:z[0])
    return poly,lo,hi

expected_classes={2:1,3:2,4:6,5:21}
certified={}
for n in range(2,6):
    gs=unlabeled_connected(n)
    assert len(gs)==expected_classes[n], (n,len(gs))
    rows=[]
    for m,adj,code in gs:
        poly,lo,hi=spectral_interval(adj)
        rows.append((m,lo,hi,poly,code))
    # At fixed n average degree is strictly ordered by edge count.
    # To rule out a reversal it suffices to show that whenever m1<m2,
    # rho(G1)<=rho(G2). The root-isolating intervals are exact rationals.
    for a,b in itertools.combinations(rows,2):
        m1,lo1,hi1,_,_=a
        m2,lo2,hi2,_,_=b
        if m1==m2:
            continue
        if m1>m2:
            m1,lo1,hi1,m2,lo2,hi2=m2,lo2,hi2,m1,lo1,hi1
        assert hi1<=lo2, (n,m1,(lo1,hi1),m2,(lo2,hi2))
    certified[n]=len(rows)

# Exact witness and persistent family: star K_{1,n-1} versus cycle C_n.
# Average degrees: 2(n-1)/n < 2. Spectral radii: sqrt(n-1) and 2.
assert sp.sqrt(4)==2
for n in range(6,101):
    avg_star=sp.Rational(2*(n-1),n)
    avg_cycle=sp.Integer(2)
    rho_star=sp.sqrt(n-1)
    rho_cycle=sp.Integer(2)
    assert avg_star < avg_cycle
    assert rho_star > rho_cycle
    # Homogeneous threshold 1/<k> therefore ranks cycle as more vulnerable,
    # while the eigenvalue threshold 1/rho ranks the star as more vulnerable.
    assert 1/avg_star > 1/avg_cycle
    assert 1/rho_star < 1/rho_cycle

print('VERIFY_OK')
print('sympy_version', sp.__version__)
print('sympy_path', sp.__file__)
print('unlabeled_connected_classes', certified)
print('first_reversal_n', 6)
print('witness_star_avg', sp.Rational(5,3), 'witness_star_rho', sp.sqrt(5))
print('witness_cycle_avg', 2, 'witness_cycle_rho', 2)
print('persistent_family_checked_n_6_to_100')
