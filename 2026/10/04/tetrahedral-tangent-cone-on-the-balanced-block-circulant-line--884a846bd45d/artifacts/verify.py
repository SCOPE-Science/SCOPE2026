import sympy as s
p,A,B,C,D=s.symbols('p A B C D')
q=1-p
M=s.Matrix([
[(p+A)/2,(p-A)/2,(q+B)/2,(q-B)/2],
[(p-A)/2,(p+A)/2,(q-B)/2,(q+B)/2],
[(q+C)/2,(q-C)/2,(p+D)/2,(p-D)/2],
[(q-C)/2,(q+C)/2,(p-D)/2,(p+D)/2],
])
assert all(s.expand(sum(M[i,j] for j in range(4))-1)==0 for i in range(4))
assert all(s.expand(sum(M[i,j] for i in range(4))-1)==0 for j in range(4))
def E_rows(i,j):
    x=[s.expand(M[i,k]*M[j,k]) for k in range(4)]
    return s.expand(((x[0]+x[1]-x[2]-x[3])**2-4*x[0]*x[1]-4*x[2]*x[3])**2-64*s.prod(x))
E01=s.factor(E_rows(0,1)); E02=s.factor(E_rows(0,2)); E12=s.factor(E_rows(1,2))
assert E01==0
assert s.expand(E02-E12)==0
L1=-q*A-p*B-p*C-q*D
L2=-q*A-p*B+p*C+q*D
L3=-q*A+p*B-p*C+q*D
L4=-q*A+p*B+p*C-q*D
formula=(L1*L2*L3*L4-4*(A*B-C*D)*(A*C-B*D)*(A*D*q**2-B*C*p**2))/16
assert s.expand(E02-formula)==0

# Squarefreeness over characteristic zero
g=E02
for z in (p,A,B,C,D):
    g=s.gcd(g,s.diff(E02,z))
assert s.factor(g)==1

# Normal degree pieces
poly=s.Poly(s.expand(E02),A,B,C,D)
bydeg={}
for mon,c in poly.terms():
    bydeg.setdefault(sum(mon),0)
    bydeg[sum(mon)] += c*A**mon[0]*B**mon[1]*C**mon[2]*D**mon[3]
assert set(bydeg)=={4,6}
assert s.expand(bydeg[4]-L1*L2*L3*L4/16)==0
assert s.expand(bydeg[6]+(A*B-C*D)*(A*C-B*D)*(A*D*q**2-B*C*p**2)/4)==0
coeff=s.Matrix([[s.expand(L).coeff(v) for v in (A,B,C,D)] for L in (L1,L2,L3,L4)])
det=s.factor(coeff.det())
assert s.expand(det + 16*p**2*q**2)==0
# Explicit orthogonal square root for real 0<p<1 on a quadratic extension
u,v=s.symbols('u v')
O=s.Matrix([[u,u,v,v],[u,-u,v,-v],[v,v,-u,-u],[v,-v,-u,u]])/s.sqrt(2)
G=s.simplify(O*O.T)
# replace u^2+v^2 by 1, verify off-diagonals zero and diagonals u^2+v^2
for i in range(4):
    for j in range(4):
        z=s.expand(G[i,j])
        if i==j:
            assert s.expand(z-(u**2+v**2))==0
        else:
            assert z==0
Sq=O.applyfunc(lambda z:s.expand(z**2))
Bp=M.subs({A:0,B:0,C:0,D:0,p:u**2})
# q=1-p becomes 1-u^2; replace v^2=1-u^2
for i in range(4):
    for j in range(4):
        assert s.expand(Sq[i,j]-Bp[i,j]).subs(v**2,1-u**2)==0
print('VERIFY_OK')
print('det=',det)
print('restricted_octic_identity=OK')
