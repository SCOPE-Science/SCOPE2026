"""Exact checks for the diameter-three Johnson-graph spectral theorem.

Requires sympy. Run: python verify.py
No downloaded data or network access is required.
"""
from itertools import combinations
from math import comb
import sympy as sp

n, h = sp.symbols('n h', integer=True, positive=True)
k = 3
b = lambda d: (3-d)*(n-3-d)
c = lambda d: d*d
a = lambda d: 3*(n-3)-b(d)-c(d)
ths = [(3-j)*(n-3-j)-j for j in range(4)]
expected_f = [
 (n-5)/(n-2),
 -(n-5)/((n-3)*(n-2)),
 2*(n-5)/((n-4)*(n-3)*(n-2)),
 -6/((n-4)*(n-3)*(n-2)),
]
f = [(n-5)/(n-2)]
for d in range(3):
    f.append(sp.factor(((-3-a(d))*f[d]-(c(d)*f[d-1] if d else 0))/b(d)))
for d in range(4):
    assert sp.factor(f[d]-expected_f[d]) == 0
assert sp.factor(c(3)*f[2]+(a(3)+3)*f[3]) == 0

pt = []
for j,th in enumerate(ths):
    p = [sp.Integer(1),th]
    for d in range(1,3):
        p.append(sp.factor((th*p[d]-b(d-1)*p[d-1]-a(d)*p[d])/c(d+1)))
    assert sp.factor(th*p[3]-b(2)*p[2]-a(3)*p[3]) == 0
    pt.append(p)

claimed = [
 (n-5)/(n-2),
 (n-6)*(n-5)/((n-4)*(n-3)),
 (n-5)*(n**3-14*n**2+63*n-86)/((n-4)**2*(n-3)**2),
 (n-6)*(n**3-13*n**2+56*n-74)/((n-4)**2*(n-3)*(n-2)),
]
for j in range(4):
    expression = sp.factor(sum(pt[j][d]*f[d]**2 for d in range(4)))
    assert sp.factor(expression-claimed[j]) == 0

# Explicit, non-numeric coefficient positivity certificates for n >= 7.
assert sp.expand((n**3-14*n**2+63*n-86).subs(n,h+7)) == h**3+7*h**2+14*h+12
assert sp.expand((n**3-13*n**2+56*n-74).subs(n,h+7)) == h**3+8*h**2+21*h+24
assert sp.expand((n**3-16*n**2+81*n-118).subs(n,h+7)) == h**3+5*h**2+4*h+8
assert sp.factor(claimed[0]-claimed[1]) == n*(n-5)/((n-4)*(n-3)*(n-2))
assert sp.factor(claimed[1]-claimed[2]) == (n-7)*(n-5)*(n-2)/((n-4)**2*(n-3)**2)
assert sp.factor(claimed[2]-claimed[3]) == (n**3-16*n**2+81*n-118)/((n-4)*(n-3)**2*(n-2))
assert [sp.simplify(x.subs(n,6)) for x in claimed]==[sp.Rational(1,4),0,sp.Rational(1,9),0]

# Independent construction of E_3 by a degree-three polynomial in the
# actual adjacency matrix; compare every entry, not just sample rows.
entries_checked = 0
for size in (6,7,8):
    triples = list(combinations(range(size),3))
    dim = len(triples)
    I=sp.eye(dim)
    A=sp.zeros(dim)
    for i,S in enumerate(triples):
        SS=set(S)
        for j in range(i):
            if len(SS.intersection(triples[j])) == 2:
                A[i,j]=A[j,i]=1
    th=[int(x.subs(n,size)) for x in ths]
    proj=sp.eye(dim)
    for j in range(3):
        proj = proj*(A-th[j]*I)/(th[3]-th[j])
    assert proj*proj==proj
    assert A*proj==-3*proj
    assert sp.trace(proj)==comb(size,3)-comb(size,2)
    for i,S in enumerate(triples):
        for j,T in enumerate(triples):
            d = 3-len(set(S).intersection(T))
            assert proj[i,j]==sp.factor(f[d].subs(n,size))
            entries_checked+=1
    if size==6:
        # Independently build ALL four adjacency spectral projectors,
        # then their exact time-averaged quantum mixing matrix.
        projectors=[]
        for u in range(4):
            Pu=sp.eye(dim)
            for v in range(4):
                if v!=u:
                    Pu=Pu*(A-th[v]*I)/(th[u]-th[v])
            assert Pu*Pu==Pu
            projectors.append(Pu)
        Mhat=sp.zeros(dim)
        for Pu in projectors:
            Mhat+=Pu.multiply_elementwise(Pu)
        assert Mhat.rank()==10
        assert (proj.multiply_elementwise(proj)).rank()==10
        where={S:i for i,S in enumerate(triples)}
        for i,S in enumerate(triples):
            j=where[tuple(x for x in range(size) if x not in S)]
            assert [proj[i,t]**2 for t in range(dim)]==[proj[j,t]**2 for t in range(dim)]

print('VERIFY_OK symbolic_projector_recurrence=4 symbolic_mode_eigenvalues=4 '+
      'positivity_polynomials=3 exact_matrix_sizes=20,35,56 '+
      f'exact_projector_entries={entries_checked} boundary_rank=10/20')
