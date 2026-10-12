from sympy import symbols, Matrix, factor, expand

lam, mu = symbols('lam mu')
M = Matrix([[0,0,lam/2],[0,mu,0],[lam/2,0,0]])
assert factor(M.det()) == -lam**2*mu/4

y,z,a,u,v = symbols('y z a u v', nonzero=True)
Y = y
Z = u*z-v*y**2
b = u*a+v
assert expand(Z+b*Y**2-u*(z+a*y**2)) == 0

alpha,delta,gamma = symbols('alpha delta gamma', nonzero=True)
# Along z=-a*y^2: Z=(gamma-delta*a)y^2 and Y^2=alpha^2 y^2 + O(y^3).
# Z+bY^2=0 therefore forces this affine law.
bjet = (delta*a-gamma)/alpha**2
assert expand(alpha**2*bjet-(delta*a-gamma)) == 0

A={1,2,4}
B={2,3,5}
assert {x+1 for x in A} == B
assert not any({c*x for x in A} == B for c in B)  # 1 in A, so a scaling c must lie in B.

for m in range(3,9):
    # m smooth branches, every pair with intersection multiplicity 2.
    delta_G = 2*(m*(m-1)//2)
    mu_G = 2*delta_G-m+1
    assert mu_G == (m-1)*(2*m-1)
    # Add one transverse branch meeting each of the m branches once.
    delta_H = delta_G+m
    mu_H = 2*delta_H-(m+1)+1
    assert mu_H == m*(2*m-1)

# For m=3 the two identical singular points recover the source's global Tjurina numbers.
assert 2*((3-1)*(2*3-1)) == 6**2-3*6+2 == 20
assert 2*(3*(2*3-1)) == 7**2-3*7+2 == 30
print('VERIFY_OK')
