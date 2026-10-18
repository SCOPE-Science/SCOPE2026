"""Exact checks for a four-site dephased boundary-driven tight-binding chain.

Dependencies: Python >=3.10, SymPy; NumPy and SciPy for the optional
full-Fock-space independent comparison.
"""
import sympy as sp

u, g, t = sp.symbols('u g t', real=True)
N = 2*(8*g**6 + 28*g**5 + (104*t+94)*g**4 + (188*t+157)*g**3
       +(288*t**2+142*t+196)*g**2+(144*t**2+109*t+117)*g+36*t+20)
D = (24*g**7+124*g**6+(336*t+422)*g**5+(1160*t+941)*g**4
     +(1176*t**2+1624*t+1373)*g**3+(2332*t**2+1426*t+1331)*g**2
     +(864*t**3+1010*t**2+1121*t+645)*g+144*t**3+253*t**2+385*t+100)
J = N/D
B = 6*g**3+13*g**2+(6*t+5)*g+t
Jtri = 2*g*(2*g+1)/B
C = 8*t*(2*g**3+5*g**2+(18*t+8)*g+9*t+5)
P = 20736*t**5+21024*t**4+46225*t**3+25410*t**2+10305*t-1200
assert sp.cancel(J-Jtri-C/(B*D)) == 0
assert sp.factor(sp.diff(J,g).subs(g,0)-2*P/((16*t+5)**2*(9*t**2+13*t+20)**2)) == 0

# Independently reconstruct the stationary covariance from 16 real equations.
n=4
h=sp.zeros(n)
for i in range(n):
    h[i,i]=u*i
    if i<n-1: h[i,i+1]=h[i+1,i]=1
real={};imag={};unknown=[]
for i in range(n):
    for j in range(i,n):
        a=sp.Symbol(f'x{i}{j}',real=True)
        real[i,j]=real[j,i]=a
        unknown.append(a)
        if i<j:
            b=sp.Symbol(f'y{i}{j}',real=True)
            imag[i,j]=b;imag[j,i]=-b
            unknown.append(b)
        else: imag[i,j]=0
K=sp.Matrix(n,n,lambda i,j:real[i,j]+sp.I*imag[i,j])
R=sp.diag(sp.Rational(1,2),0,0,sp.Rational(1,2))
S=sp.zeros(n);S[0,0]=1
F=-sp.I*(h*K-K*h)-R*K-K*R+S
for i in range(n):
    for j in range(n):
        if i!=j: F[i,j]-=g*K[i,j]
eq=[]
for i in range(n):
    for j in range(i,n):
        z=sp.expand_complex(F[i,j])
        eq.append(sp.re(z).expand())
        if i<j: eq.append(sp.im(z).expand())
A,b=sp.linear_eq_to_matrix(eq,unknown)
expected_det=(2*g+1)*(4*g**2+4*g+16*u**2+5)*D.subs(t,u**2)/16
assert sp.factor(A.det(method='domain-ge')-expected_det)==0
X=A.inv()*b
assert sp.cancel(X[unknown.index(sp.Symbol('x33',real=True))]-J.subs(t,u**2))==0

# Independently reconstruct the nearest-neighbor-only closure.
near=[]
for a in unknown:
    i,j=map(int,a.name[1:]);
    if j-i<=1:near.append(a)
cut={a:0 for a in unknown if a not in near}
near_eq=[eq[unknown.index(a)].subs(cut) for a in near]
At,bt=sp.linear_eq_to_matrix(near_eq,near)
Xt=At.inv()*bt
assert sp.cancel(Xt[near.index(sp.Symbol('x33',real=True))]-Jtri.subs(t,u**2))==0

# Sign coefficients of the exact derivative in dephasing.
Q=sp.Poly(sp.expand(sp.diff(N,g)*D-N*sp.diff(D,g)),g)
assert Q.degree()==12
low=[
 2*P,
 8*(20736*t**5+46656*t**4+45539*t**3+17541*t**2+6612*t-3510),
 2*(248832*t**5+158976*t**4+259588*t**3+13311*t**2-8604*t-64587),
 8*(11520*t**4+21592*t**3-49439*t**2-31690*t-39108)
]
for k in range(4):assert sp.expand(Q.nth(k)-low[k])==0
for k in range(4,13):
    coeff=sp.Poly(Q.nth(k),t)
    assert all(c<0 for c in coeff.all_coeffs())
# Each low coefficient has one positive zero, bracketed in disjoint intervals.
brackets=[(sp.Rational(9,100),sp.Rational(1,10)),(sp.Rational(1,5),sp.Rational(1,4)),
          (sp.Rational(1,2),sp.Rational(3,5)),(sp.Rational(9,5),sp.Integer(2))]
for p,(left,right) in zip(low,brackets):
    poly=sp.Poly(p,t)
    assert sp.sign(poly.eval(left))==-1
    assert sp.sign(poly.eval(right))==1
    signs=[sp.sign(c) for c in poly.all_coeffs() if c]
    assert sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))==1

print('PASS: exact 16-dimensional covariance, determinant, current, closure gap, and derivative sign certificate')
print('critical squared tilt:',sp.nroots(P)[0])

# This independent calculation uses the full 16-state Fock space and the
# original Lindblad equation, not the closed covariance equations.
try:
    import numpy as np
    def full_lindblad(tilt,rate):
        minus=np.array([[0,1],[0,0]],complex)
        z=np.diag([1,-1]).astype(complex)
        ident=np.eye(2,dtype=complex)
        ann=[]
        for site in range(4):
            op=np.array([[1]],complex)
            for k in range(4):
                op=np.kron(op,z if k<site else minus if k==site else ident)
            ann.append(op)
        dim=16; eye=np.eye(dim,dtype=complex)
        ham=np.zeros((dim,dim),complex)
        for site in range(4):ham+=tilt*site*(ann[site].conj().T@ann[site])
        for site in range(3):
            ham+=ann[site].conj().T@ann[site+1]+ann[site+1].conj().T@ann[site]
        jumps=[ann[0].conj().T,ann[3]]+[np.sqrt(rate)*(op.conj().T@op) for op in ann]
        lind=-1j*(np.kron(eye,ham)-np.kron(ham.T,eye))
        for l in jumps:
            b=l.conj().T@l
            lind+=np.kron(l.conj(),l)-0.5*(np.kron(eye,b)+np.kron(b.T,eye))
        lind[-1,:]=eye.reshape(-1,order='F')
        rhs=np.zeros(dim*dim,complex);rhs[-1]=1
        rho=np.linalg.solve(lind,rhs).reshape((dim,dim),order='F')
        return (np.trace(rho@ann[3].conj().T@ann[3])).real
    for tilt,rate in [(0,0),(.4,0),(.4,.6),(2,1),(4,3)]:
        exact=float(J.subs({t:tilt**2,g:rate}))
        direct=full_lindblad(tilt,rate)
        assert abs(direct-exact)<1e-11,(tilt,rate,exact,direct)
    print('PASS: five independent full-Fock-space Lindblad comparisons')
except ImportError:
    print('SKIPPED optional NumPy full-Fock-space comparison')
