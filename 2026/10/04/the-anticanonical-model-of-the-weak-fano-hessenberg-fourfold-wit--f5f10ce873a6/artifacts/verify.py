import sympy as sp
from itertools import permutations

# Generic eigenvalues and a generic 2-plane basis.
l1,l2,l3,l4 = sp.symbols('l1 l2 l3 l4')
lam = [l1,l2,l3,l4]
u = sp.symbols('u1:5')
v = sp.symbols('v1:5')
B = sp.Matrix([[u[i],v[i],lam[i]*u[i],lam[i]*v[i]] for i in range(4)])
D = sp.expand(B.det())

def p(i,j):
    return sp.expand(u[i]*v[j]-u[j]*v[i])
A = sp.expand((l1-l3)*(l2-l4))
C = sp.expand(-(l1-l2)*(l3-l4))
Q_uv = sp.expand(A*p(0,1)*p(2,3) + C*p(0,2)*p(1,3))
assert sp.expand(D-Q_uv) == 0
assert sp.factor(A+C) == (l1-l4)*(l2-l3)

# Pluecker coordinates x12,x13,x14,x23,x24,x34.
x12,x13,x14,x23,x24,x34 = sp.symbols('x12 x13 x14 x23 x24 x34')
xs=[x12,x13,x14,x23,x24,x34]
G = x12*x34 - x13*x24 + x14*x23
Q = A*x12*x34 + C*x13*x24

# The pencil Q - tG has three complementary 2x2 blocks with coefficients
# A-t, C+t, -t. Their zeros are distinct under pairwise distinct eigenvalues.
t=sp.symbols('t')
coeffs=[A-t,C+t,-t]
roots=[A,-C,sp.Integer(0)]
assert sp.expand(A-(l1-l3)*(l2-l4)) == 0
assert sp.expand(C+(l1-l2)*(l3-l4)) == 0
assert sp.expand((A+C)-(l1-l4)*(l2-l3)) == 0

# At each of the six coordinate 2-planes, eliminate the paired coordinate using G.
# The remaining quadratic must be nondegenerate.  We compute Hessian determinants.
pairs=[(0,5),(1,4),(2,3)]
local_hess=[]
for i,j in pairs:
    for pivot,comp in [(i,j),(j,i)]:
        # pivot=1, solve G=0 for its complementary coordinate comp.
        subs={xs[pivot]:1}
        # G is linear in comp and coefficient is +/-1 after pivot=1.
        g=sp.expand(G.subs(subs))
        q=sp.expand(Q.subs(subs))
        sol=sp.solve(sp.Eq(g,0), xs[comp], dict=False)[0]
        qloc=sp.expand(q.subs(xs[comp],sol))
        vars4=[z for k,z in enumerate(xs) if k not in (pivot,comp)]
        H=sp.hessian(qloc,vars4)
        detH=sp.factor(H.det())
        local_hess.append((str(xs[pivot]),sp.factor(qloc),detH))
        assert detH != 0

# Anticanonical weight: alpha12+alpha13+alpha23+alpha34 = 2 omega1 + omega2.
# Express xi in fundamental weights w1,w2,w3 with x4=-(x1+x2+x3).
w1,w2,w3=sp.symbols('w1 w2 w3')
# x1=w1, x2=w2-w1, x3=w3-w2, x4=-w3.
x=[w1,w2-w1,w3-w2,-w3]
xi=sp.expand((x[0]-x[1])+(x[0]-x[2])+(x[1]-x[2])+(x[2]-x[3]))
assert sp.expand(xi-(2*w1+w2)) == 0

# Optional independent localization check: (-K_X)^4 = 192.
vals=[sp.Rational(0),sp.Rational(1),sp.Rational(3),sp.Rational(7)]
root_pairs=[(0,1),(0,2),(1,2),(2,3)]
total=sp.Rational(0)
for w in permutations(range(4)):
    rv=[vals[w[a]]-vals[w[b]] for a,b in root_pairs]
    total += sum(rv)**4/sp.prod(rv)
assert sp.simplify(total-192)==0

print('DETERMINANT_IDENTITY_OK')
print('PENCIL_ROOTS', [sp.factor(r) for r in roots])
for name,qloc,detH in local_hess:
    print('LOCAL',name,'Q=',sp.factor(qloc),'HESSDET=',sp.factor(detH))
print('ANTICANONICAL_WEIGHT', xi)
print('ANTICANONICAL_DEGREE', total)
print('VERIFY_OK')
