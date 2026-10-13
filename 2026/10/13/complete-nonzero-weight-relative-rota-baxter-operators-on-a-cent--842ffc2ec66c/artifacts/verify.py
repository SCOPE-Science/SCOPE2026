"""Reproduce the relative Rota–Baxter reduction and finite-field counts."""
from itertools import combinations, product
import sympy as sp

# The only nonzero independent bracket is [e2,e3,e4]=e1.
# In the ordered decomposition Ke1 + span(e2,e3,e4), a map that
# preserves Ke1 has block matrix [[a,h],[0,A]].
a, weight = sp.symbols('a weight')
entries = sp.symbols('A00 A01 A02 A10 A11 A12 A20 A21 A22')
h_entries = sp.symbols('h0 h1 h2')
A = sp.Matrix(3,3,entries)
T = sp.Matrix.vstack(sp.Matrix.hstack(sp.Matrix([[a]]),sp.Matrix(1,3,h_entries)),
                     sp.Matrix.hstack(sp.zeros(3,1),A))
identity = sp.eye(4)

def bracket(x,y,z):
    return sp.Matrix([sp.det(sp.Matrix.hstack(x[1:4,0],y[1:4,0],z[1:4,0])),0,0,0])

def defect(M,lam,i,j,k):
    x,y,z=identity[:,i],identity[:,j],identity[:,k]
    X,Y,Z=M*x,M*y,M*z
    rhs=bracket(X,Y,z)+bracket(Y,Z,x)+bracket(Z,X,y)+lam*bracket(x,y,z)
    return sp.simplify(bracket(X,Y,Z)-M*rhs)

sigma=sum(sp.det(A.extract([i,j],[i,j])) for i,j in combinations(range(3),2))
F=sp.expand(A.det()-a*(sigma+weight))
for triple in combinations(range(4),3):
    d=defect(T,weight,*triple)
    if triple==(1,2,3):
        assert sp.simplify(d-sp.Matrix([F,0,0,0]))==sp.zeros(4,1)
    else:
        assert d==sp.zeros(4,1)
print('BLOCK_EQUATION_VERIFIED',sp.expand(F))

# For arbitrary maps, the W-part u of T(e1) multiplies the
# scalar sigma_2(A)+weight in the unique W-input triple.
u=sp.Matrix(sp.symbols('u0 u1 u2'))
full=sp.Matrix.vstack(sp.Matrix.hstack(sp.Matrix([[a]]),sp.Matrix(1,3,h_entries)),
                      sp.Matrix.hstack(u,A))
wf=defect(full,weight,1,2,3)
assert sp.expand(wf[0])==F
assert all(sp.expand(wf[i]+u[i-1]*(sigma+weight))==0 for i in range(1,4))
print('FULL_DEFECT_W_COMPONENT_VERIFIED')

# Quadratic form Q(A)=sigma_2(A) on 9 matrix entries has
# Gram determinant -1/256 in odd characteristic.
H=sp.hessian(sigma,entries)/2
assert sp.factor(H.det()) == -sp.Rational(1,256)
print('QUADRATIC_FORM_GRAM_DETERMINANT_VERIFIED')

# The characteristic-zero sharpness example becomes a valid
# weight-zero solution without preserving the derived line.
counter=sp.zeros(4,4)
counter[1,0]=1
for triple in combinations(range(4),3):
    assert defect(counter,0,*triple)==sp.zeros(4,1)
assert defect(counter,1,1,2,3)!=sp.zeros(4,1)
print('ZERO_WEIGHT_BOUNDARY_VERIFIED')

# Exhaustive full 4x4 search in F2 (all 65536 matrices).
def det3(x,y,z,q):
    return (x[0]*(y[1]*z[2]-y[2]*z[1])
        -x[1]*(y[0]*z[2]-y[2]*z[0])
        +x[2]*(y[0]*z[1]-y[1]*z[0]))%q

std=((0,0,0),(1,0,0),(0,1,0),(0,0,1))
def rb_full(cols,lam,q):
    for i,j,k in combinations(range(4),3):
        X,Y,Z=(cols[s][1:] for s in (i,j,k))
        alpha=det3(X,Y,Z,q)
        t=(det3(X,Y,std[k],q)+det3(Y,Z,std[i],q)
           +det3(Z,X,std[j],q)+(lam if (i,j,k)==(1,2,3) else 0))%q
        if (alpha-t*cols[0][0])%q or any((t*r)%q for r in cols[0][1:]):
            return False
    return True

sol=0
outside=0
for values in product(range(2),repeat=16):
    cols=[values[4*i:4*i+4] for i in range(4)]
    if rb_full(cols,1,2):
        sol+=1
        outside+=any(cols[0][1:])
assert (sol,outside)==(4736,0)
print('F2_ALL_65536',sol,'OUTSIDE_DERIVED_PRESERVING',outside)

# For q=3,5, exhaustive enumeration of all q^9 matrices A.
# For q=4 use GF(4) with alpha^2=alpha+1, testing the even case.
def prime_counts(q):
    n={s:[0,0] for s in range(1,q)}
    for p,b,c,d,e,f,g,h,i in product(range(q),repeat=9):
        s=(p*e+p*i+e*i-b*d-c*g-f*h)%q
        if not s: continue
        delta=(p*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%q
        n[s][0]+=1
        n[s][1]+=(delta==0)
    for s,(total,singular) in n.items():
        chi=lambda z: 1 if pow(z%q,(q-1)//2,q)==1 else -1
        assert total==q**8+chi(-s)*q**4
        assert singular==q**3*(q*q+q+1)*(q*q-1)
        lam=(-s)%q
        count=q**3*(q**9-total+q*singular)
        expected=q**12+q**10-q**8-(1+chi(lam))*q**7
        assert count==expected
        print('PRIME',q,'WEIGHT',lam,'SOLUTIONS',count)
for p in (3,5):prime_counts(p)

mul=[[0]*4 for _ in range(4)]
for x,y in product(range(4),repeat=2):
    z=0
    for i,j in product(range(2),repeat=2):
        if (x>>i)&1 and (y>>j)&1:z^=1<<(i+j)
    if z&4:z^=7
    mul[x][y]=z
m=lambda x,y:mul[x][y]
assert m(2,2)==3 and m(2,3)==1
n={s:[0,0] for s in (1,2,3)}
for p,b,c,d,e,f,g,h,i in product(range(4),repeat=9):
    s=m(p,e)^m(p,i)^m(e,i)^m(b,d)^m(c,g)^m(f,h)
    if not s: continue
    delta=m(p,m(e,i)^m(f,h))^m(b,m(d,i)^m(f,g))^m(c,m(d,h)^m(e,g))
    n[s][0]+=1
    n[s][1]+=(delta==0)
for s,(total,singular) in n.items():
    assert total==4**8
    assert singular==4**3*(4**2+4+1)*(4**2-1)
    count=4**3*(4**9-total+4*singular)
    assert count==4**12+4**10-4**8-4**7
    print('GF4','WEIGHT',s,'SOLUTIONS',count)

print('VERIFY_OK')
