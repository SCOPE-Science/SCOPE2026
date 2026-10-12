import sympy as sp
from itertools import product

# Printed commutative algebra B: e1^2=e2, e1*e4=e4.
def mul(x,y):
    return sp.Matrix([0, sp.expand(x[0]*y[0]), 0, sp.expand(x[0]*y[3]+x[3]*y[0])])

e=[sp.eye(4)[:,i] for i in range(4)]

def jac(x,y,z):
    return sp.simplify(mul(mul(x,y),z)+mul(mul(y,z),x)+mul(mul(z,x),y))

# Printed algebra fails the ordinary Jacobi identity in char !=2.
assert jac(e[0],e[0],e[3]) == sp.Matrix([0,0,0,2])

# Published alpha family is never an algebra self-morphism in char 0/char !=2.
a12,a23,a14,a34=sp.symbols('a12 a23 a14 a34')
alpha_print=sp.Matrix([
    [-1,a12,1,a14],
    [0,1,a23,-1],
    [-1,0,1,a34],
    [0,2,0,-1],
])
assert sp.simplify(mul(alpha_print*e[0],alpha_print*e[0])-alpha_print*e[1]) == sp.Matrix([-a12,0,0,-2])

# Symbolic valid endomorphism branches over char !=2.
lam,u,v,w,p,s,r,t=sp.symbols('lam u v w p s r t')
A0=sp.Matrix([
    [0,0,0,0],
    [u,0,p,0],
    [v,0,s,0],
    [w,0,r,0],
])
A1=sp.Matrix([
    [lam,0,0,0],
    [u,lam**2,p,0],
    [v,0,s,0],
    [0,0,0,0],
])
Aauto=sp.Matrix([
    [1,0,0,0],
    [u,1,p,0],
    [v,0,s,0],
    [0,0,0,t],
])

def is_endo_symbolic(A):
    for i,j in product(range(4),repeat=2):
        if sp.simplify(A*mul(e[i],e[j])-mul(A*e[i],A*e[j])) != sp.zeros(4,1):
            return False
    return True
assert is_endo_symbolic(A0)
assert is_endo_symbolic(A1)
assert is_endo_symbolic(Aauto)

# Hom-Jacobi on the twisted product mu_A=A o mu.
def hprod(A,x,y):
    return sp.simplify(A*mul(x,y))
def hjac(A,x,y,z):
    return sp.simplify(hprod(A,hprod(A,x,y),A*z)+hprod(A,hprod(A,y,z),A*x)+hprod(A,hprod(A,z,x),A*y))
for A in (A0,A1):
    for i,j,k in product(range(4),repeat=3):
        assert hjac(A,e[i],e[j],e[k]) == sp.zeros(4,1)
# On the lambda=1 endomorphism branch the obstruction is exactly t^2.
assert hjac(Aauto,e[0],e[0],e[3]) == sp.Matrix([0,0,0,2*t**2])

# Finite-field direct replay. We exhaustively construct every algebra endomorphism
# from its images, with alpha(e2) forced by alpha(e1)^2, then test the full table.
def mq(x,y,q):
    return (0,(x[0]*y[0])%q,0,(x[0]*y[3]+x[3]*y[0])%q)
def mv(M,x,q):
    return tuple(sum(M[i][j]*x[j] for j in range(4))%q for i in range(4))
def cols_to_rows(cols):
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
def endo(M,q):
    bas=[tuple(1 if i==j else 0 for i in range(4)) for j in range(4)]
    for i,j in product(range(4),repeat=2):
        if mv(M,mq(bas[i],bas[j],q),q) != mq(mv(M,bas[i],q),mv(M,bas[j],q),q):
            return False
    return True
def hvalid(M,q):
    bas=[tuple(1 if i==j else 0 for i in range(4)) for j in range(4)]
    def hp(x,y): return mv(M,mq(x,y,q),q)
    for x,y,z in product(bas,repeat=3):
        terms=[hp(hp(x,y),mv(M,z,q)),hp(hp(y,z),mv(M,x,q)),hp(hp(z,x),mv(M,y,q))]
        if any(sum(T[k] for T in terms)%q for k in range(4)):
            return False
    return True
def det4(M,q):
    # Gaussian elimination determinant nonzero test.
    A=[list(row) for row in M]
    r=0
    for c in range(4):
        piv=next((i for i in range(r,4) if A[i][c]%q),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,q)
        A[r]=[(z*inv)%q for z in A[r]]
        for i in range(4):
            if i!=r and A[i][c]%q:
                f=A[i][c]%q
                A[i]=[(A[i][j]-f*A[r][j])%q for j in range(4)]
        r+=1
    return r==4

def all_endos(q):
    V=list(product(range(q), repeat=4))
    zero=(0,0,0,0)
    out=[]
    for c1 in V:
        c2=mq(c1,c1,q)
        # e1*e2=0 is a cheap prune.
        if mq(c1,c2,q)!=zero: continue
        c3s=[c3 for c3 in V if mq(c3,c3,q)==zero and mq(c1,c3,q)==zero and mq(c2,c3,q)==zero]
        c4s=[c4 for c4 in V if mq(c4,c4,q)==zero and mq(c1,c4,q)==c4 and mq(c2,c4,q)==zero]
        for c3 in c3s:
            for c4 in c4s:
                if mq(c3,c4,q)!=zero: continue
                M=cols_to_rows((c1,c2,c3,c4))
                assert endo(M,q)
                out.append(M)
    return out

q=3
Es=all_endos(q)
expected_total=q**4*(q*q+2*q-2)
assert len(Es)==expected_total,(q,len(Es),expected_total)
valid=[M for M in Es if hvalid(M,q)]
expected_valid=q**6+q**5-q**4
assert len(valid)==expected_valid,(q,len(valid),expected_valid)
autos=[M for M in Es if det4(M,q)]
assert len(autos)==q**3*(q-1)**2
assert all(not hvalid(M,q) for M in autos)
print({'q':q,'endomorphisms':len(Es),'valid_twists':len(valid),'invalid_twists':len(Es)-len(valid),'automorphisms':len(autos),'mode':'exhaustive'})

# Closed-form arithmetic cross-checks in larger fields.
for q in (5,7,11):
    valid=q**6+q**5-q**4
    total=q**4*(q*q+2*q-2)
    invalid=q**4*(q-1)
    autos=q**3*(q-1)**2
    assert total-valid==invalid
    assert autos<=invalid
    print({'q':q,'valid_twists':valid,'endomorphisms':total,'invalid_twists':invalid,'automorphisms':autos,'mode':'formula_crosscheck'})
print('VERIFY_OK')
