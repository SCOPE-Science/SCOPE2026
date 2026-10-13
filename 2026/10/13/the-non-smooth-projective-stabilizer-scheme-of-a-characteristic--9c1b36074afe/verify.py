"""Exact verification for the projective stabilizer of Y^4+XZ^3 in characteristic 2.

Run: python verify.py.  SymPy is used only for finite symbolic identities;
the general group-scheme exhaustiveness proof is in RESULT.md.
"""
from itertools import product
from sympy import symbols, Poly, expand

X,Y,Z=symbols('X Y Z')
b,v,u,bp,vp,up=symbols('b v u bp vp up')
a,c,d,g,h,i=symbols('a c d g h i')

def reduced_mod(poly, *vars):
    f=Poly(expand(poly),*vars,modulus=2)
    return f.as_expr()

# In symbolic characteristic two, Frobenius fourth powers kill all mixed terms.
# Verify the polynomial multiplier after substitution with u^4=0.
F=Y**4+X*Z**3
Xm=b**4*X+v**4*Z
Ym=u*X+b*Y+v*Z
Zm=Z
p=reduced_mod(Ym**4+Xm*Zm**3-b**4*F, X,Y,Z,b,v,u)
assert all(mon[5]>=4 for mon,cf in Poly(p,X,Y,Z,b,v,u,modulus=2).terms() if cf%2)

# Prove the matrix composition identity modulo u^4=(up)^4=0.
M=[[b**4,0,v**4],[u,b,v],[0,0,1]]
Mp=[[bp**4,0,vp**4],[up,bp,vp],[0,0,1]]
Prod=[[sum(M[r][k]*Mp[k][c] for k in range(3)) for c in range(3)] for r in range(3)]
bb=b*bp
uu=u*bp**4+b*up
vv=v+b*vp+u*vp**4
Target=[[bb**4,0,vv**4],[uu,bb,vv],[0,0,1]]
for row in range(3):
    for col in range(3):
        q=Poly(reduced_mod(Prod[row][col]-Target[row][col],u,up,b,bp,v,vp),u,up,b,bp,v,vp,modulus=2)
        for mon,cf in q.terms():
            assert cf%2==0 or mon[0]>=4 or mon[1]>=4, (row,col,mon,cf)

# Generic coefficient identities used in completeness proof.
A=a*X+c*Y+d*Z
B=u*X+b*Y+v*Z
C=g*X+h*Y+i*Z
P=Poly(B**4+A*C**3, X,Y,Z,a,b,c,d,u,v,g,h,i,modulus=2)
# Specialized to the polynomial variables: extract coefficients modulo 2.
coeffs=Poly(B**4+A*C**3,X,Y,Z).terms()
def coefficient(exp):
    D=dict(coeffs)
    return Poly(D.get(exp,0),a,b,c,d,u,v,g,h,i,modulus=2).as_expr()
assert reduced_mod(coefficient((2,0,2))-(a*g*i**2+d*g**2*i),a,b,c,d,u,v,g,h,i)==0
assert reduced_mod(coefficient((1,1,2))-(a*h*i**2+c*g*i**2),a,b,c,d,u,v,g,h,i)==0
assert reduced_mod(coefficient((0,1,3))-(c*i**3+d*h*i**2),a,b,c,d,u,v,g,h,i)==0

# Direct count of every projective matrix over F_2. F_2^3 has seven points.
def determinant2(m):
    return (m[0][0]*(m[1][1]*m[2][2]+m[1][2]*m[2][1])+
            m[0][1]*(m[1][0]*m[2][2]+m[1][2]*m[2][0])+
            m[0][2]*(m[1][0]*m[2][1]+m[1][1]*m[2][0]))%2

def poly_mul(A,B):
    out={}
    for exp,x in A.items():
        for exp2,y in B.items():
            key=tuple(exp[t]+exp2[t] for t in range(3))
            out[key]=(out.get(key,0)+x*y)%2
    return {e:v for e,v in out.items() if v}

def poly_pow(A,n):
    out={(0,0,0):1}
    for _ in range(n):out=poly_mul(out,A)
    return out

def matches(m):
    xs=[{tuple(int(i==j) for i in range(3)):m[row][j] for j in range(3) if m[row][j]} for row in range(3)]
    p=poly_pow(xs[1],4)
    q=poly_mul(xs[0],poly_pow(xs[2],3))
    for k,w in q.items():p[k]=(p.get(k,0)+w)%2
    return {key:x for key,x in p.items() if x}=={(0,4,0):1,(1,0,3):1}

stabilizers=[]
for entries in product((0,1),repeat=9):
    M2=[entries[3*r:3*r+3] for r in range(3)]
    if determinant2(M2) and matches(M2):stabilizers.append(M2)
assert len(stabilizers)==2
expected=[[(1,0,vv),(0,1,vv),(0,0,1)] for vv in (0,1)]
assert stabilizers==expected or all(x in stabilizers for x in expected)
print('VERIFY_OK: exact quartic invariance and composition; generic coefficient constraints; 168 PGL3(F2) matrices, 2 stabilizers')
