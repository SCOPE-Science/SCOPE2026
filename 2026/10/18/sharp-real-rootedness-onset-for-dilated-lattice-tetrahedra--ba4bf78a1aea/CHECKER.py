"""Exact finite checks for dilation box-polynomial identities of lattice tetrahedra.

Run: python CHECKER.py
Requires SymPy. Finite tests corroborate, rather than prove, universal identities.
"""
import math
import itertools
import sympy as sp

n,m,h1,h2,h3,E=sp.symbols('n m h1 h2 h3 E',integer=True)
h=[sp.Integer(1),h1,h2,h3]
L=sp.expand(sum(h[j]*sp.prod(n+k-j for k in (1,2,3))/6 for j in range(4)))
a,b,c=[L.coeff(n,k) for k in (3,2,1)]
A=sp.expand(-L.subs(n,-m))
gamma=sp.expand(2*a*m**3+(E-4*c)*m+1)
assert sp.simplify(A-sum(h[j]*sp.prod(m+j-k for k in (1,2,3))/6 for j in range(4)))==0
assert sp.expand(gamma.subs(m,1))==E-6-h1+h2-h3
assert sp.expand(gamma.subs(m,2))==2*E+4*h2-11
assert sp.expand(gamma.subs(m,3))==3*E+5*h1+11*h2+5*h3-12
H=1+h1+h2+h3
assert sp.simplify(gamma-(m*(gamma.subs(m,2)-1)/2+H*(m**3-4*m)/3+1))==0

def normalize_vertices(vertices):
    return [tuple(map(int,p)) for p in vertices]

def det_adjugate(columns):
    M=sp.Matrix.hstack(*map(lambda c:sp.Matrix(c),columns))
    return int(M.det()),[[int(M.adjugate()[i,j]) for j in range(M.rows)] for i in range(M.cols)]

def matrix_apply(M,w):
    return [sum(row[j]*w[j] for j in range(len(w))) for row in M]

def bounds(vertices):
    return [range(min(p[j] for p in vertices),max(p[j] for p in vertices)+1) for j in range(3)]

def closed_count(vertices,n):
    v=normalize_vertices(vertices)
    cols=[tuple(v[i][j]-v[0][j] for j in range(3)) for i in (1,2,3)]
    D,adj=det_adjugate(cols)
    assert D
    vv=[tuple(n*x for x in p) for p in v]
    count=0
    for x in itertools.product(*bounds(vv)):
        raw=matrix_apply(adj,[x[j]-n*v[0][j] for j in range(3)])
        nums=[z*D for z in raw]
        if all(z>=0 for z in nums) and sum(nums)<=n*D*D: count+=1
    return count

def box_counts(vertices,m):
    v=normalize_vertices(vertices)
    gens=[tuple(m*x for x in p)+(1,) for p in v]
    D,adj=det_adjugate(gens)
    ranges=[range(sum(min(0,g[j]) for g in gens),sum(max(0,g[j]) for g in gens)+1) for j in range(3)]
    counts=[0,0,0,0]
    for x in itertools.product(*ranges):
        for height in (1,2,3):
            raw=matrix_apply(adj,(*x,height))
            if all(0<z*D<D*D for z in raw):counts[height]+=1
    return counts

def edge_length_sum(vertices):
    return sum(math.gcd(*(abs(x-y) for x,y in zip(p,q))) for p,q in itertools.combinations(vertices,2))

examples={
    'unimodular':[(0,0,0),(1,0,0),(0,1,0),(0,0,1)],
    'Reeve-2':[(0,0,0),(1,0,0),(0,1,0),(1,1,2)],
    'Reeve-4':[(0,0,0),(1,0,0),(0,1,0),(1,1,4)],
    'edge-length-2':[(0,0,0),(2,0,0),(0,1,0),(0,0,1)],
    'nonempty-facets':[(0,0,0),(2,0,0),(0,2,0),(0,0,2)],
    'interior-rich':[(0,0,0),(3,0,0),(0,3,0),(0,0,3)],
    'oblique':[(0,0,0),(2,1,0),(0,2,1),(1,0,2)],
}
num=0
for name,v in examples.items():
    L1,L2,L3=(closed_count(v,j) for j in (1,2,3))
    hnum=[1,L1-4,L2-4*L1+6,L3-4*L2+6*L1-4]
    assert all(x>=0 for x in hnum),(name,hnum)
    edge=edge_length_sum(v)
    for dilation in (1,2,3,4):
        counts=box_counts(v,dilation)
        subs={m:dilation,h1:hnum[1],h2:hnum[2],h3:hnum[3],E:edge}
        a_exact=int(A.subs(subs));gamma_exact=int(gamma.subs(subs))
        assert counts[1]==a_exact and counts[3]==a_exact,(name,dilation,counts,a_exact)
        assert counts[2]-2*counts[1]==gamma_exact,(name,dilation,counts,gamma_exact)
        if dilation>=2:assert gamma_exact>0
        if dilation>=4:assert a_exact>0
        num+=1
print('PASS: symbolic polynomial identities; {} independent exact 4D open-box enumerations'.format(num))
