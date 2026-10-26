"""Exact rational cross-checks for cut and cycle projections of adjacent Boolean ranks.

Run: python verify_boolean_layer_hodge.py  (requires SymPy).
Finite checks supplement, but do not replace, the all-parameter proof.
"""
from itertools import combinations
from math import comb
import sympy as sp


def expected(n, k):
    N = sp.Integer(comb(n, k))
    q = sp.Integer(2*k+1) - sp.Rational(2*k*(k+1), n)
    diagonal = sp.Rational(1, k+1) + (1-sp.Rational(1,N))/(n-k)
    return sp.factor(q), sp.factor(q+1-2*diagonal), sp.factor(diagonal)


def orbit_column(n, k):
    """Solve the exact edge-source Laplacian on stabilizer vertex orbits."""
    o = []
    for level in (k, k+1):
        for a in range(k+1):
            for b in (0,1):
                c = level-a-b
                if 0 <= c <= n-k-1:
                    o.append((level,a,b,c))
    loc = {z:i for i,z in enumerate(o)}
    L = sp.zeros(len(o));source = sp.zeros(len(o), 1)
    for j,(level,a,b,c) in enumerate(o):
        L[j,j] = n-k if level == k else k+1
        if level == k:
            nxt = ((a+1,b,c,k-a), (a,b+1,c,1-b),
                   (a,b,c+1,n-k-1-c))
            other = k+1
        else:
            nxt = ((a-1,b,c,a), (a,b-1,c,b), (a,b,c-1,c))
            other = k
        for aa,bb,cc,mul in nxt:
            if mul:
                L[j,loc[(other,aa,bb,cc)]] -= mul
    source[loc[(k,k,0,0)]] = 1
    source[loc[(k+1,k,1,0)]] = -1
    inds = list(range(1,len(o)))
    sol = list(L.extract(inds,inds).inv() * source.extract(inds,[0]))
    x = [sp.Integer(0)] + sol
    qnorm = sp.Integer(0)
    checks = 0
    for j,(level,a,b,c) in enumerate(o):
        if level != k:
            continue
        vertices = comb(k,a)*comb(n-k-1,c)
        for aa,bb,cc,mul in ((a+1,b,c,k-a), (a,b+1,c,1-b),
                              (a,b,c+1,n-k-1-c)):
            if mul:
                current = x[j]-x[loc[(k+1,aa,bb,cc)]]
                qnorm += vertices*mul*abs(current)
                checks += 1
    diag = x[loc[(k,k,0,0)]] - x[loc[(k+1,k,1,0)]]
    return sp.factor(qnorm), sp.factor(qnorm+1-2*diag), sp.factor(diag), checks


def full_column(n,k):
    """Independently build the entire graph and invert a grounded Laplacian."""
    lower = list(combinations(range(n),k))
    upper = list(combinations(range(n),k+1))
    verts = lower+upper
    ids = {v:i for i,v in enumerate(verts)}
    edges = []
    for T in upper:
        for S in combinations(T,k):
            edges.append((ids[S],ids[T]))
    L=sp.zeros(len(verts))
    for i,j in edges:
        L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    root = (tuple(range(k)),tuple(range(k+1)))
    ix = edges.index((ids[root[0]],ids[root[1]]))
    rhs = sp.zeros(len(verts)-1,1)
    i,j=edges[ix]
    if i<len(verts)-1: rhs[i]+=1
    if j<len(verts)-1: rhs[j]-=1
    x = list(L[:-1,:-1].inv()*rhs)+[sp.Integer(0)]
    currents=[x[i]-x[j] for i,j in edges]
    qnorm = sum(map(abs,currents))
    diag=currents[ix]
    return sp.factor(qnorm), sp.factor(qnorm+1-2*diag), sp.factor(diag),len(edges)


def symbolic_sign_certificate():
    """Verify the dual sign-potential equations as polynomial identities."""
    n,k,a,b=sp.symbols('n k a b')
    uk=lambda aa,bb: 1+2*(n-k-1)*aa/n+2*(k*k+k-n)*bb/n-2*aa*bb
    vu=lambda aa,bb: 2*(n-k)*aa/n+2*k*k*bb/n-2*aa*bb
    lower=(n-k)*uk(a,b)-(k-a)*vu(a+1,b)-(1-b)*vu(a,b+1) \
         -(n-2*k-1+a+b)*vu(a,b)
    upper=(k+1)*vu(a,b)-a*uk(a-1,b)-b*uk(a,b-1) \
         -(k+1-a-b)*uk(a,b)
    lower_div=(1-2*b)*(n-3*k+2*a)
    upper_div=-((1-2*b)*(k+1-2*a)+2*b)
    for bb in (0,1):
        assert sp.simplify((lower-lower_div).subs(b,bb)) == 0
        assert sp.simplify((upper-upper_div).subs(b,bb)) == 0
    q=sp.factor(uk(k,0)-vu(k,1))
    assert sp.simplify(q-(2*k+1-2*k*(k+1)/n)) == 0


def main():
    symbolic_sign_certificate()
    orbit_cases=0; orbit_types=0; full_cases=0; full_edges=0
    for n in range(3,17):
        for k in range(1,n-1):
            if k>min(n-k-1,6):
                continue
            got=orbit_column(n,k)
            assert got[:3]==expected(n,k),(n,k,got,expected(n,k))
            orbit_cases+=1;orbit_types+=got[3]
    for n,k in ((3,1),(4,1),(5,1),(5,2),(6,1),(6,2),(7,1),(7,2),(7,3)):
        got=full_column(n,k)
        assert got[:3]==expected(n,k),(n,k,got,expected(n,k))
        full_cases+=1;full_edges+=got[3]
    print('BOOLEAN_ADJACENT_RANK_HODGE_OK',
          'orbit_cases='+str(orbit_cases),
          'orbit_edge_types='+str(orbit_types),
          'full_cases='+str(full_cases),
          'full_edges='+str(full_edges),
          'symbolic_identities=PASS')

if __name__=='__main__':main()
