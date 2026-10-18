"""Independent implementation of finite checks for the two-step sketched eigenvalue example."""
import math
import numpy as np
from scipy.special import beta, betainc
from scipy.integrate import quad
import sympy as sp

COUNT = 0

def check(condition, label):
    global COUNT
    if not bool(condition):
        raise AssertionError(label)
    COUNT += 1

A = sp.diag(1, 2, 3)
q1 = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
q2 = sp.Matrix([-1, 0, 1]) / sp.sqrt(2)
q3 = sp.Matrix([1, -2, 1]) / sp.sqrt(6)
Q = sp.Matrix.hstack(q1,q2)
H0 = Q.T * A * Q
R = q3.T * A * Q
check(sp.simplify(Q.T*Q-sp.eye(2)) == sp.zeros(2), 'orthonormal trial basis')
check(sp.simplify(H0-sp.Matrix([[2,sp.sqrt(6)/3],[sp.sqrt(6)/3,2]]))==sp.zeros(2),'Euclidean compression')
check(sp.simplify(R-sp.Matrix([[0,1/sp.sqrt(3)]]))==sp.zeros(1,2),'coupling')
x,y=sp.symbols('x y',real=True)
H=H0+sp.Matrix([x,y])*R
disc=sp.factor(sp.trace(H)**2-4*H.det())
check(sp.simplify(disc-(y**2+8+4*sp.sqrt(2)*x)/3)==0,'discriminant')
check(sp.simplify(disc.subs({x:-2,y:0}))<0,'witness')

# Derivation: Gaussian least-squares leakage eta has density
# (s-1)/(2*pi) * (1+x*x+y*y)**(-(s+1)/2), s>=2.
def probability(s):
    def at_y(y):
        a=(y*y+8)/(4*math.sqrt(2))
        z=a/math.sqrt(1+y*y)
        # One-sided power tail via regularized incomplete beta.
        tail=.5*beta(s/2,.5)*betainc(s/2,.5,1/(1+z*z))
        return (1+y*y)**(-s/2)*tail
    integral,_=quad(at_y,0,30,epsabs=5e-14,epsrel=1e-10,limit=300)
    return (s-1)/math.pi*integral

for s,lo,hi in [(2,.11322489,.11322491),(4,.03350455,.03350458),(8,.00282713,.00282716),(16,.00002547,.00002549),(32,2.78e-9,2.80e-9)]:
    p=probability(s)
    check(lo<p<hi,f'probability s={s}: {p}')
    asym=math.sqrt(3/(2*math.pi*s))*3**(-s/2)
    print('prob',s,f'{p:.14g}','asym ratio',f'{p/asym:.10g}')
check(.98<probability(32)/(math.sqrt(3/(2*math.pi*32))*3**(-16))<.99,'Laplace scaling 32')

q1n=np.asarray(q1,dtype=float).reshape(3)
q2n=np.asarray(q2,dtype=float).reshape(3)
q3n=np.asarray(q3,dtype=float).reshape(3)
Qn=np.column_stack([q1n,q2n]); An=np.diag([1.,2.,3.]); H0n=Qn.T@An@Qn
rng=np.random.default_rng(20261015)
for s in (2,3,5,8,15):
    for j in range(96):
        S=rng.standard_normal((s,3))
        W=S@Qn; z=S@q3n
        eta=np.linalg.lstsq(W,z,rcond=None)[0]
        Hdirect=np.linalg.solve(W.T@W,W.T@S@An@Qn)
        Hformula=H0n+np.outer(eta,[0.,1./math.sqrt(3)])
        check(np.allclose(Hdirect,Hformula,rtol=1e-8,atol=1e-8),'Gaussian compression identity')
        detdisc=(np.trace(Hdirect))**2-4*np.linalg.det(Hdirect)
        formula=(eta[1]**2+8+4*math.sqrt(2)*eta[0])/3
        check(abs(detdisc-formula)<1e-7*(1+abs(formula)),'Gaussian discriminant')
print('ALL CHECKS PASSED:',COUNT)
