"""Exact symbolic Pauli-closure and fermionic partial-time-reversal identities.

Run: python verify_symbolic.py
Requires SymPy. No numerical approximation or external data are used.
"""
import sympy as s
K=s.kronecker_product
I=s.eye(2)
X=s.Matrix([[0,1],[1,0]])
Y=s.Matrix([[0,-s.I],[s.I,0]])
Z=s.diag(1,-1)
c=s.Matrix([[0,1],[0,0]])
Z1,Z2=K(Z,I),K(I,Z)
W1,W2=K(Y,X),K(X,Y)
Z12=Z1*Z2
J,g1,g2=s.symbols('J g_1 g_2',real=True)
H=-J*K(X,X)
L1,L2=K(c,I),K(Z,c)

def adjoint(O):
    ans=s.I*(H*O-O*H)
    for gamma,L in ((g1,L1),(g2,L2)):
        for jump in (L,L.H):
            D=jump.H*jump
            ans+=gamma*(jump.H*O*jump-s.Rational(1,2)*(D*O+O*D))
    return s.simplify(ans)

expected=[
    -2*g1*Z1-2*J*W1,
    -2*g2*Z2-2*J*W2,
    2*J*Z1-(g1+g2)*W1,
    2*J*Z2-(g1+g2)*W2,
    -2*(g1+g2)*Z12,
]
for O,expected_O in zip((Z1,Z2,W1,W2,Z12),expected):
    assert all(s.simplify(x)==0 for x in adjoint(O)-expected_O)

z1,z2,w1,w2,r=s.symbols('z_1 z_2 w_1 w_2 r', real=True)
rho=(s.eye(4)+z1*Z1+z2*Z2+w1*W1+w2*W2+r*Z12)/4
ma=[K(X,I),K(Y,I),K(Z,X),K(Z,Y)]
PT=s.zeros(4)
for mask in range(16):
    inds=[j for j in range(4) if mask & (1<<j)]
    mon=s.eye(4)
    for j in inds: mon=mon*ma[j]
    phase=s.I**sum(j<2 for j in inds)
    coeff=s.trace(mon.H*rho)/4
    PT+=coeff*phase*mon
T=s.simplify(PT*Z1)
assert all(s.simplify(x)==0 for x in T-T.H)
A2=(1+r)**2+(w1-w2)**2
B2=(1-r)**2+(w1+w2)**2
v=s.symbols('v')
characteristic=s.expand((4*v+z1+z2)**2-A2)*s.expand((4*v+z1-z2)**2-B2)
assert s.simplify(s.expand(256*T.charpoly(v).as_expr()-characteristic))==0
assert s.expand(A2-B2-4*(r-w1*w2))==0
assert s.expand((A2-B2).subs(r,z1*z2+w1*w2)-4*z1*z2)==0

# The Gaussian/Wick identity is invariant under the exact dynamical flow.
# Its derivative equals -2(g1+g2) times itself after substituting r=z1*z2+w1*w2.
z1d=-2*g1*z1-2*J*w1
z2d=-2*g2*z2-2*J*w2
w1d=2*J*z1-(g1+g2)*w1
w2d=2*J*z2-(g1+g2)*w2
assert s.expand(z1d*z2+z1*z2d+w1d*w2+w1*w2d +
                2*(g1+g2)*(z1*z2+w1*w2))==0
print('VERIFY_SYMBOLIC_OK exact adjoint closure, twist spectrum, Wick invariance')
