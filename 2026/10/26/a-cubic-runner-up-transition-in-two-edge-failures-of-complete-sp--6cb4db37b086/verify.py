"""Exact algebraic checks for split-network two-edge damage classifications.
Run: python verify.py  (requires sympy 1.14 or compatible).
No network or external files are accessed.
"""
import sympy as sp
from itertools import combinations

p, q = sp.symbols('p q', integer=True, positive=True)
N = p + q

def edge(a, b):
    return {a: sp.Integer(1), b: sp.Integer(-1)}

def inner(e, f, zone=None):
    return sum((val*f.get(node, 0) for node, val in e.items()
                if zone is None or node[0] == zone), sp.Integer(0))

def gram(e, f, power):
    beta = 1/p**power - 1/N**power
    sy1 = sum((val for node,val in e.items() if node[0]=='Y'), sp.Integer(0))
    sy2 = sum((val for node,val in f.items() if node[0]=='Y'), sp.Integer(0))
    return inner(e,f)/N**power + beta*(inner(e,f,'Y')-sy1*sy2/q)

def delta(e, f):
    r1, r2 = gram(e,e,1), gram(f,f,1)
    s1, s2 = gram(e,e,2), gram(f,f,2)
    z, t = gram(e,f,1), gram(e,f,2)
    return sp.factor(N*((1-r2)*s1 + (1-r1)*s2+2*z*t)
                     / ((1-r1)*(1-r2)-z*z))

X = lambda k: ('X', k)
Y = lambda k: ('Y', k)
CASES={
    'A_two_CY_same_Y': (edge(X(0),Y(0)), edge(X(1),Y(0))),
    'B_two_CY_same_X': (edge(X(0),Y(0)), edge(X(0),Y(1))),
    'C_two_CY_disjoint': (edge(X(0),Y(0)), edge(X(1),Y(1))),
    'D_CC_CY_meet': (edge(X(0),X(1)), edge(X(0),Y(0))),
    'E_CC_CY_disjoint': (edge(X(0),X(1)), edge(X(2),Y(0))),
    'F_CC_CC_meet': (edge(X(0),X(1)), edge(X(0),X(2))),
    'G_CC_CC_disjoint': (edge(X(0),X(1)), edge(X(2),X(3))),
}
D={key:delta(*edges) for key,edges in CASES.items()}
A,B,C=list(D)[:3]
assert sp.cancel(D[A]-2*(2*p**2+2*p*q-3*p+q**2-q)/(p*(p-2)*(N-1)))==0
assert sp.cancel(D[B]-2*(2*p**2+2*p*q-3*p+q**2-2*q)/(p*(p-1)*(N-2)))==0
P=p**2+p*q-2*p-q
M=(2*p**4+4*p**3*q-6*p**3+3*p**2*q**2-9*p**2*q+6*p**2
   +p*q**3-5*p*q**2+6*p*q-q**3+2*q**2)
assert sp.cancel(D[C]-2*M/(p*P*(P+2)))==0
F=-q*q+(p*p*(p-3)+2)*q+p*p*(p-2)**2
assert sp.cancel(D[B]-D[C]-2*F/((p-1)*(N-2)*P*(P+2)))==0
boundary=p**3-3*p**2+p+1
assert sp.expand(F.subs(q,boundary))==1
assert sp.expand(F.subs(q,boundary+1)+p*(p-2)*(p-1))==0

# All required strict comparisons admit a positive-coefficient certificate in
# the variables u=p-3>=0, v=q-2>=0. These are exact identities, not samples.
u,v=sp.symbols('u v', nonnegative=True)
checks=[(A,B), (A,C)] + [(B,key) for key in list(D)[3:]]
for lhs,rhs in checks:
    numerator,denominator=sp.fraction(sp.factor(D[lhs]-D[rhs]))
    pn=sp.Poly(sp.expand(numerator.subs({p:u+3,q:v+2})),u,v)
    pd=sp.Poly(sp.expand(denominator.subs({p:u+3,q:v+2})),u,v)
    assert pn.terms() and all(coef>=0 for _,coef in pn.terms())
    assert pn.eval({u:0,v:0})>0
    assert pd.terms() and all(coef>=0 for _,coef in pd.terms())
    assert pd.eval({u:0,v:0})>0
print('SYMBOLIC_OK seven orbit formulas; six strict comparisons; unique integer transition')

# Independent exact direct inverse: a second method constructs the original
# and edge-deleted graph Laplacians as concrete integer matrices.
cases_run=0
for pp in (3,4,5):
    for qq in (2,3,4,5):
        nn=pp+qq
        base=sp.zeros(nn)
        for i,j in combinations(range(nn),2):
            if i<pp or j<pp:
                base[i,i]+=1; base[j,j]+=1
                base[i,j]-=1; base[j,i]-=1
        J=sp.ones(nn)/nn
        kf0=nn*(sp.trace((base+J).inv())-1)
        assert kf0==pp+sp.Rational(nn*(qq-1),pp)
        def vertex(z):return z[1] if z[0]=='X' else pp+z[1]
        for name,(e,f) in CASES.items():
            if name.startswith('G_') and pp<4: continue
            post=base.copy()
            for z in (e,f):
                ii,jj=map(vertex,z)
                post[ii,ii]-=1;post[jj,jj]-=1
                post[ii,jj]+=1;post[jj,ii]+=1
            actual=sp.factor(nn*(sp.trace((post+J).inv())-1)-kf0)
            expected=D[name].subs({p:pp,q:qq})
            assert sp.cancel(actual-expected)==0,(pp,qq,name,actual,expected)
            cases_run+=1
print('DIRECT_INVERSE_OK',cases_run,'exact independent Laplacian inverse checks')

# For small labelled graphs, independently count the distinct orbit types.
for pp,qq in ((3,2),(3,3),(4,2),(4,3)):
    graph_edges=[(i,j) for i,j in combinations(range(pp+qq),2) if i<pp or j<pp]
    def signature(ef):
        a,b=ef
        ty=lambda e:'CC' if max(e)<pp else 'CY'
        if ty(a)=='CC' and ty(b)=='CC':
            return 'F_CC_CC_meet' if len(set(a)&set(b)) else 'G_CC_CC_disjoint'
        if ty(a)=='CC' or ty(b)=='CC':
            cc=a if ty(a)=='CC' else b
            cy=b if ty(a)=='CC' else a
            return 'D_CC_CY_meet' if cc[0]==cy[0] or cc[1]==cy[0] else 'E_CC_CY_disjoint'
        if a[0]==b[0]:return 'B_two_CY_same_X'
        if a[1]==b[1]:return 'A_two_CY_same_Y'
        return 'C_two_CY_disjoint'
    seen={signature(pair) for pair in combinations(graph_edges,2)}
    assert seen==set(CASES)-({'G_CC_CC_disjoint'} if pp==3 else set())
print('ORBIT_EXHAUSTION_OK four labelled families')
