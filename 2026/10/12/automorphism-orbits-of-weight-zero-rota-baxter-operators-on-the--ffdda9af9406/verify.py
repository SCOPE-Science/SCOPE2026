import sympy as sp

# Basis is (1,x,y,z), with xy=z and yx=-z.
def mul(u,v):
    u0,u1,u2,u3=u
    v0,v1,v2,v3=v
    return sp.Matrix([
        u0*v0,
        u0*v1+u1*v0,
        u0*v2+u2*v0,
        u0*v3+u3*v0+u1*v2-u2*v1,
    ])

e=[sp.eye(4)[:,i] for i in range(4)]

def rb_residual(R,i,j):
    Ri=R*e[i]; Rj=R*e[j]
    lhs=mul(Ri,Rj)
    rhs=R*(mul(Ri,e[j])+mul(e[i],Rj))
    return sp.simplify(lhs-rhs)

def check_rb(R):
    for i in range(4):
        for j in range(4):
            assert rb_residual(R,i,j)==sp.zeros(4,1)

def rank1(img_col, functional):
    # R(w)=functional(w)*img_col
    return img_col*sp.Matrix([functional])

x,y,z=e[1],e[2],e[3]

# Six rank-one representatives.
rank1_reps={
    'S1': rank1(z,[1,0,0,0]),
    'S2': rank1(z,[0,1,0,0]),
    'S3': rank1(z,[1,1,0,0]),
    'N1': rank1(x,[1,0,0,0]),
    'N2': rank1(x,[0,0,1,0]),
    'N3': rank1(x,[1,0,1,0]),
}
for name,R in rank1_reps.items():
    check_rb(R)
    assert R.rank()==1
    assert R*R==sp.zeros(4)

# Three rank-two normal-form strata.
t,sigma=sp.symbols('t sigma', nonzero=True, real=True)
A=sp.zeros(4); A[:,0]=y; A[:,1]=t*z
B=sp.zeros(4); B[:,0]=sigma*z; B[:,1]=y
C=sp.zeros(4); C[:,0]=y; C[:,1]=y+t*z
for name,R in [('A_t',A),('B_sigma',B),('C_t',C)]:
    check_rb(R)
    assert R.rank()==2
    assert R*R==sp.zeros(4)

# General automorphism and multiplication preservation.
A11,A12,A21,A22,alpha,beta=sp.symbols('A11 A12 A21 A22 alpha beta')
det=A11*A22-A12*A21
Phi=sp.Matrix([
    [1,0,0,0],
    [0,A11,A12,0],
    [0,A21,A22,0],
    [0,alpha,beta,det],
])
assert sp.factor(Phi.det())==det**2
for i in range(4):
    for j in range(4):
        assert sp.simplify(mul(Phi*e[i],Phi*e[j])-Phi*mul(e[i],e[j]))==sp.zeros(4,1)

# Stabilizer action on the rank-two slice W=span(y,z).
a,b,c,d,s,u,h,al,be=sp.symbols('a b c d s u h al be', nonzero=False)
M=sp.zeros(4)
M[:,0]=a*y+b*z
M[:,1]=c*y+d*z
PhiW=sp.Matrix([
    [1,0,0,0],
    [0,s,0,0],
    [0,h,u,0],
    [0,al,be,s*u],
])
Conj=sp.simplify(PhiW*M*PhiW.inv())
assert sp.simplify(Conj[2,0]-u*a)==0
assert sp.simplify(Conj[2,1]-u*c/s)==0
assert sp.simplify(Conj[3,0]-(be*a+s*u*b))==0
assert sp.simplify(Conj[3,1]-(be*c/s+u*d))==0

# Polynomial invariants of the three rank-two strata under the stabilizer action.
ap=u*a; cp=u*c/s; bp=be*a+s*u*b; dp=be*c/s+u*d
Det=a*d-b*c
Detp=sp.factor(ap*dp-bp*cp)
assert sp.simplify(Detp-u**2*Det)==0
assert sp.simplify(dp/ap-d/a).subs(c,0)==0
assert sp.simplify(bp*cp-u**2*b*c).subs(a,0)==0
assert sp.simplify(Detp/ap**2-Det/a**2)==0

print('rank_one_representatives=6')
print('rank_two_strata=A_t,B_sigma,C_t')
print('automorphism_determinant=(det A)^2')
print('rank_two_stabilizer_action=verified')
print('rank_two_invariants=verified')
print('CHECK_OK')
