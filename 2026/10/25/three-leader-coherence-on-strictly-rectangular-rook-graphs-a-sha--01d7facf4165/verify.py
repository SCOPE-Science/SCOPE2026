"""Exact reproducible certificate for three grounded leaders on strictly rectangular rook graphs.
Run: python verify.py (requires SymPy >=1.13)."""
from itertools import combinations
from math import comb
import sympy as S

m, n = S.symbols('m n', integer=True, positive=True)
x, y, t = S.symbols('x y t', integer=True, nonnegative=True)
REP = {
    'matching': ((0,0),(1,1),(2,2)),
    'two_same_first': ((0,0),(0,1),(1,2)),
    'two_same_second': ((0,0),(1,0),(2,1)),
    'corner': ((0,0),(0,1),(1,0)),
    'three_same_first': ((0,0),(0,1),(0,2)),
    'three_same_second': ((0,0),(1,0),(2,0)),
}

def proj(a,b,sz):
    return S.Integer(a == b) - 1/sz

def H(u,v,p=1):
    a,b=u; c,d=v
    return proj(a,c,m)/(m**p*n) + proj(b,d,n)/(n**p*m) + proj(a,c,m)*proj(b,d,n)/(m+n)**p

BASE = S.factor((m-1)/m+(n-1)/n+(m-1)*(n-1)/(m+n)+m*n*H((0,0),(0,0)))

def formula(triple):
    a,b,c=triple
    other=(b,c)
    h0=H(a,a)
    def M(u,v): return H(u,v)-H(u,a)-H(v,a)+h0
    def Z(u,v):
        return H(u,v,2)-H(u,a,2)-H(v,a,2)+H(a,a,2) + m*n*(h0-H(u,a))*(h0-H(v,a))
    aa,ab,bb=[S.factor(M(*pair)) for pair in ((b,b),(b,c),(c,c))]
    za,zb,zc=[S.factor(Z(*pair)) for pair in ((b,b),(b,c),(c,c))]
    return S.factor(BASE-(bb*za+aa*zc-2*ab*zb)/(aa*bb-ab**2))

COST={name:formula(v) for name,v in REP.items()}

def positive_polynomial(expr,shift):
    f=S.factor(expr)
    numerator,denominator=S.fraction(f)
    assert denominator.is_polynomial(m,n) or denominator.is_polynomial(n)
    poly=S.Poly(S.expand(numerator.subs(shift, simultaneous=True)),*(x,y) if m in shift else (t,))
    assert poly.total_degree()>=0 and all(c>0 for c in poly.coeffs()), (expr,poly)
    return len(poly.coeffs()),max(sum(monom) for monom in poly.monoms())

for k in ('two_same_first','two_same_second','corner','three_same_first','three_same_second'):
    count,degree=positive_polynomial(COST[k]-COST['matching'],{m:x+3,n:x+y+4})
    print('POSITIVE_CERT',k,'coefficients',count,'max_total_degree',degree)
for k in ('corner','three_same_first'):
    diff=S.factor((COST[k]-COST['two_same_first']).subs(m,2))
    assert all(c>0 for c in S.Poly(S.expand(S.fraction(diff)[0].subs(n,3+t)),t).coeffs())
    print('TWO_ROW_POSITIVE',k)

# Exact comparison with direct grounded Laplacian inverses for all six possible leader shapes.
def direct(mv,nv,triple):
    N=mv*nv
    L=S.zeros(N)
    for i in range(mv):
        for j in range(nv):
            z=i*nv+j
            for k in range(mv):
                if k!=i:
                    w=k*nv+j;L[z,z]+=1;L[z,w]-=1
            for k in range(nv):
                if k!=j:
                    w=i*nv+k;L[z,z]+=1;L[z,w]-=1
    drop={i*nv+j for i,j in triple}
    keep=[z for z in range(N) if z not in drop]
    return S.trace(L.extract(keep,keep).inv())

checks=0
for mv,nv in ((2,2),(2,3),(2,5),(3,3),(3,4),(4,4),(4,5),(5,6)):
    for name,rep in REP.items():
        if max(i for i,j in rep)>=mv or max(j for i,j in rep)>=nv:continue
        analytic=COST[name].subs({m:mv,n:nv})
        exact=direct(mv,nv,rep)
        assert analytic==exact,(mv,nv,name,analytic,exact)
        checks+=1

# All relevant triple shapes are represented by the six partition types.
# Square instances are checked only as additional consistency tests;
# the reported optimization theorem assumes strictly unequal factors.
assert COST['corner'].subs({m:2,n:2})==S.Rational(1,2)
for mv,nv in ((2,3),(2,5),(3,4),(4,5),(5,6)):
    families={name:float(cost.subs({m:mv,n:nv})) for name,cost in COST.items()
              if max(i for i,j in REP[name])<mv and max(j for i,j in REP[name])<nv}
    target='two_same_first' if mv==2 else 'matching'
    assert families[target]==min(families.values())

print('VERIFY_OK symbolic_positive=7 exact_direct_inverses=',checks,
      'optimum_checks=5')
