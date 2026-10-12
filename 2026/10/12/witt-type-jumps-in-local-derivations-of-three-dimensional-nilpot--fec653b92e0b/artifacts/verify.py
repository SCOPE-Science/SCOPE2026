"""Reproducible checks for local derivations of the quadratic two-step algebra.
Requires Python 3 and SymPy for symbolic verification.
"""
import itertools
import sympy as s

# Base field with odd characteristic, Q(v)=v1^2+d*v2^2.
a,b,d,p1,p2,gamma=s.symbols('a b d p1 p2 gamma')
V=s.Matrix([[1,0],[0,d]])
J=s.Matrix([[0,-d],[1,0]])
M=a*s.eye(2)+b*J
assert s.simplify(M.T*V+V*M-2*a*V)==s.zeros(2)
assert J**2==-d*s.eye(2)
# determinant[v,Jv]=Q(v), forcing evaluation injectivity off the isotropic cone.
x,y=s.symbols('x y')
v=s.Matrix([x,y])
assert s.simplify(s.det(s.Matrix.hstack(v,J*v))-(x*x+d*y*y))==0

# Three-dimensional multiplication, and derivation identities for generic D.
def mul(X,Y):
    return s.Matrix([0,0,X[0]*Y[0]+d*X[1]*Y[1]])
D=s.Matrix([[M[0,0],M[0,1],0],[M[1,0],M[1,1],0],[p1,p2,2*a]])
e=[s.eye(3)[:,i] for i in range(3)]
for X in e:
    for Y in e:
        assert s.simplify(D*mul(X,Y)-mul(D*X,Y)-mul(X,D*Y))==s.zeros(3,1)

# Finite-field exhaustivity of the projected local-derivation condition.
def square_flag(q,u): return bool(u%q and pow(u,(q-1)//2,q)==1)

def span_member(a,b,w,q):
    """Whether w belongs to span(a,b) in F_q^2, independently of basis."""
    det=(a[0]*b[1]-a[1]*b[0])%q
    if det: return True
    return (a[0]*w[1]-a[1]*w[0])%q==0

def makeJ(v,d,q): return ((-d*v[1])%q,v[0]%q)

def linearN(v,N,q):
    m00,m01,m10,m11=N
    return ((m00*v[0]+m01*v[1])%q,(m10*v[0]+m11*v[1])%q)

def localN(N,d,q):
    for v in itertools.product(range(q),repeat=2):
        if v==(0,0): continue
        if not span_member(v,makeJ(v,d,q),linearN(v,N,q),q): return False
    return True

def derivN(N,d,q):
    m00,m01,m10,m11=N
    return m00==m11 and (m01+d*m10)%q==0

for q in (3,5,7,11):
    for dval in range(1,q):
        anisotropic=not square_flag(q,-dval)
        Nlist=[N for N in itertools.product(range(q),repeat=4) if localN(N,dval,q)]
        expected=q**4 if anisotropic else q**2
        assert len(Nlist)==expected,(q,dval,len(Nlist),expected)
        deriv=[N for N in Nlist if derivN(N,dval,q)]
        assert len(deriv)==q*q
        if not anisotropic: assert len(deriv)==len(Nlist)
    # Representative pair of Witt types, with exact full-dimensional point counts
    split_d=next(t for t in range(1,q) if square_flag(q,-t))
    nonsplit_d=next(t for t in range(1,q) if not square_flag(q,-t))
    print(f'F_{q}: split d={split_d}, local={q**5}, deriv={q**4}; '
          f'anisotropic d={nonsplit_d}, local={q**7}, deriv={q**4}; '
          f'linear-2-local={q**4}')

# Exhaustive direct local-witness test over F_3 for every candidate linear map,
# including all 3^7 maps satisfying the mandatory Δ(z) in Kz condition.
q=3
all_X=list(itertools.product(range(q),repeat=3))
for dval in (1,2):
    # Every derivation matrix has the four parameters a,b,p1,p2.
    derivs=[]
    for av,bv,c1,c2 in itertools.product(range(q),repeat=4):
        mat=((av,(-dval*bv)%q,0),(bv,av,0),(c1,c2,(2*av)%q))
        derivs.append(mat)
    def apply(mat,w):
        return tuple(sum(row[k]*w[k] for k in range(3))%q for row in mat)
    reachable={w:{apply(mat,w) for mat in derivs} for w in all_X}
    n_ok=0
    n_formula=0
    n_der=0
    for N in itertools.product(range(q),repeat=4):
        predicted_N=localN(N,dval,q)
        for f1,f2,g in itertools.product(range(q),repeat=3):
            mat=((N[0],N[1],0),(N[2],N[3],0),(f1,f2,g))
            islocal=all(apply(mat,w) in reachable[w] for w in all_X)
            predicted=predicted_N
            assert islocal==predicted,(dval,mat)
            n_ok+=islocal
            n_formula+=predicted
            n_der+=bool(derivN(N,dval,q) and g==(2*N[0])%q)
    assert n_ok==n_formula==(q**7 if dval==1 else q**5)
    assert n_der==q**4
    print(f'F_3: full direct local-witness replay d={dval} yields {n_ok} local and {n_der} derivations')

print('VERIFY_OK')
