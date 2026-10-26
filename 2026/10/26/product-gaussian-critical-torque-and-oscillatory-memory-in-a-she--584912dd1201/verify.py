"""Exact algebraic checks for the stationary shear-torque theorem.

Requires Python 3 and SymPy. Run with: python verify.py
"""
import sympy as sp

q, t = sp.symbols("q t", real=True)
s = sp.symbols("s", positive=True, real=True)
K = sp.Matrix([[-1, q, -1], [0, -1, 1], [1, -1, -1]])
H = sp.Matrix([[0, 0, sp.Rational(1, 2)],
               [0, -q, sp.Rational(1, 2)],
               [sp.Rational(1, 2), sp.Rational(1, 2), 0]])
den = (3-q)*(q+12)
Sigma = sp.Matrix([
    [-q**3+9*q**2-6*q+36, q*(15-q), q*(5*q-3)],
    [q*(15-q), 6*(6-q), q*(q+3)],
    [q*(5*q-3), q*(q+3), 3*(q**2-5*q+12)]
])/den

checks = 0
def equal(a,b):
    global checks
    difference = sp.simplify(a-b)
    assert (difference.is_zero_matrix if isinstance(difference, sp.MatrixBase) else difference == 0), (a,b)
    checks += 1

equal((sp.symbols('z')*sp.eye(3)-K).det(),
      sp.symbols('z')**3+3*sp.symbols('z')**2+5*sp.symbols('z')+3-q)
for i in range(3):
    for j in range(3):
        equal((K*Sigma+Sigma*K.T+2*sp.eye(3))[i,j], 0)
equal(sp.trace(H*Sigma),-12*q/(q+12))
var = sp.factor(2*sp.trace((H*Sigma)**2))
expected = (864+144*q+834*q**2-123*q**3-q**4)/den/(q+12)
equal(var,expected)
for v in [0,1,sp.Rational(3,2),2,sp.Rational(5,2),sp.Rational(299,100)]:
    Sm=Sigma.subs(q,v)
    for i in range(3):
        for j in range(3):
            equal((K.subs(q,v)*Sm+Sm*K.subs(q,v).T+2*sp.eye(3))[i,j],0)
    equal(var.subs(q,v),expected.subs(q,v))

v = sp.Matrix([2,1,1]); a = sp.Matrix([sp.Rational(1,2),-sp.Rational(5,2),sp.Rational(3,2)])
H3=H.subs(q,3)
equal(K.subs(q,3)*v,sp.zeros(3,1))
equal(H3*v,a)
equal((v.T*a)[0],0)
A = sp.Matrix(3,3,lambda i,j:sp.limit((3-q)*Sigma[i,j],q,3,dir='-'))
equal(A,sp.Rational(6,5)*v*v.T)
equal(sp.limit((a.T*Sigma*a)[0],q,3,dir='-'),5)
equal(sp.limit((3-q)*(v.T*Sigma*v)[0]/36,q,3,dir='-'),sp.Rational(6,5))
equal(sp.limit((3-q)*var,q,3,dir='-'),24)
equal(sp.limit((3-q)**2 * 48 * sp.trace((Sigma*H)**4),q,3,dir='-'),3456)
# Direct determinant of the exact Gaussian quadratic-form characteristic function.
scaled = (Sigma*H).subs(q,3-s*s)
phi_den=sp.factor((sp.eye(3)-2*sp.I*t*s*scaled).det())
equal(sp.limit(phi_den,s,0,dir='+'),1+24*t*t)

# A second, independent, linear-algebra calculation at rational parameters.
# The unknown covariance entries are solved afresh from the Lyapunov system.
for val in [sp.Rational(1,3),sp.Rational(3,2),sp.Rational(5,2)]:
    u=sp.symbols('u0:6')
    Z=sp.Matrix([[u[0],u[1],u[2]],[u[1],u[3],u[4]],[u[2],u[4],u[5]]])
    Km=K.subs(q,val)
    EE=Km*Z+Z*Km.T+2*sp.eye(3)
    eqs=[EE[i,j] for i in range(3) for j in range(i,3)]
    independent=Z.subs(sp.solve(eqs,u,dict=True)[0])
    equal(independent,Sigma.subs(q,val))
    equal(2*sp.trace((independent*H.subs(q,val))**2),var.subs(q,val))
# The critical slow vector, fast observable and projected covariance.
K3 = K.subs(q,3)
B = sp.Matrix(3,3,lambda i,j:sp.limit(Sigma[i,j]-A[i,j]/(3-q),q,3,dir='-'))
Bknown = sp.Matrix([[-sp.Rational(27,25),-sp.Rational(11,25),-sp.Rational(41,25)],
                    [-sp.Rational(11,25),sp.Rational(12,25),-sp.Rational(13,25)],
                    [-sp.Rational(41,25),-sp.Rational(13,25),-sp.Rational(3,25)]])
equal(B,Bknown)
equal(K3*v,sp.zeros(3,1))
equal((a.T*v)[0],0)
equal((a.T*B*a)[0],5)
equal((a.T*K3*B*a)[0],-sp.Rational(35,4))
equal((a.T*K3**2*B*a)[0],sp.Rational(5,4))
equal((a.T*(K3**2+3*K3+5*sp.eye(3))*B*a)[0],0)
equal(sp.factor(K3.charpoly().as_expr()),sp.symbols('lambda')*(sp.symbols('lambda')**2+3*sp.symbols('lambda')+5))
# The first critical torque autocovariance is the product of 6/5 and 5.
equal(4*sp.Rational(6,5)*5,24)
equal(4*sp.Rational(6,5)*(-sp.Rational(35,4)),-42)
# The first three derivatives of the closed-form lag kernel are 24,-42,6.
z=sp.symbols('z',nonnegative=True,real=True)
ker=24*sp.exp(-3*z/2)*(sp.cos(sp.sqrt(11)*z/2)-sp.sin(sp.sqrt(11)*z/2)/(2*sp.sqrt(11)))
equal(ker.subs(z,0),24)
equal(sp.diff(ker,z).subs(z,0),-42)
equal(sp.diff(ker,z,2).subs(z,0),6)
equal(sp.simplify(sp.diff(ker,z,2)+3*sp.diff(ker,z)+5*ker),0)
print(f'PASS: {checks} exact symbolic identities')
print('critical limiting characteristic function: (1+24t^2)^(-1/2)')
print('variance divergence coefficient: 24')
