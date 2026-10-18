"""Independent finite-matrix and quadrature checks for the thermal RTP response.
This checks finite-dimensional algebra and examples; the infinite-domain theorem is analytical.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr

# An RTP with velocity +/-v and Poisson direction redraw rate alpha;
# its sign-flip rate is alpha/2. Translational Brownian motion has variance 2Dt.
def matrix_response(alpha, v, D, q, omega):
    s = D*q*q-1j*omega
    tilted=np.array([[-alpha/2-1j*q*v,alpha/2],
                     [alpha/2,-alpha/2+1j*q*v]],complex)
    return 0.5*np.sum(np.linalg.solve(s*np.eye(2)-tilted,np.ones(2)))

def closed_response(alpha, v, D, q, omega):
    s=D*q*q-1j*omega
    return (s+alpha)/(s*(s+alpha)+q*q*v*v)

def K(alpha, v, D, q, omega):
    d=D*q*q
    den_real=d*d+alpha*d+v*v*q*q-omega*omega
    den_im=-(2*d+alpha)*omega
    return ((alpha+d)**2+omega**2-v*v*q*q)/(den_real**2+den_im**2)

def signed_g(alpha,v,D,q,V):
    if abs(q)<1e-14: return 0.0
    return q**4 * K(alpha,v,D,q,q*V)

# Arbitrary evaluations away from singular origin, including finite frequency.
for alpha,v,D in [(1.,3.,0.1),(.7,1.2,.45),(2.,4.,1.8)]:
    for q in [.13,.4,.93,1.7,3.5,6.2]:
        for omega in [.07,.4,1.2,3.]:
            a=matrix_response(alpha,v,D,q,omega)
            b=closed_response(alpha,v,D,q,omega)
            assert abs(a-b)<5e-13,(alpha,v,D,q,omega,a,b)
            assert abs(a.imag/omega-K(alpha,v,D,q,omega))<1e-10
print('matrix-resolvent evaluations: 72 agreements')

alpha,v=1.,3.
for D in [0.05,0.4,2.25,2.5]:
    for V in [0.3,1.5,2.9]:
        # Scan q and compare with sharp discriminant: existence iff V^2+4 alpha D<v^2.
        qq=np.geomspace(.00001,500.,20000)
        empirical=np.any([K(alpha,v,D,q,q*V)<-1e-12 for q in qq])
        predicted=V*V+4*alpha*D<v*v-1e-12
        assert empirical==predicted,(D,V,empirical,predicted)
print('velocity-diffusion discriminant: 12 agreements')

# Integral for nonnegative potentials U_L=exp(-x²/2L²)*(1+cos(q0*x)) (amplitude=1).
# Fourier transform=sqrt(2pi)*L*(gaussian(q)+0.5 gaussian(q+q0)+0.5 gaussian(q-q0)).
D=.3; V=.7
A=np.sqrt(v*v-V*V)
qlo=(A-np.sqrt(A*A-4*alpha*D))/(2*D)
qhi=(A+np.sqrt(A*A-4*alpha*D))/(2*D)
q0=(qlo+qhi)/2
assert K(alpha,v,D,q0,q0*V)<0
for L in [20.,40.,80.]:
    def fun(q):
        f=np.exp(-.5*(L*q)**2)+.5*np.exp(-.5*(L*(q-q0))**2)+.5*np.exp(-.5*(L*(q+q0))**2)
        return L*L*f*f*signed_g(alpha,v,D,q,V)
    # The support is localized to three neighborhoods.
    integral=0
    for center in [-q0,0,q0]:
        integral+=quad(fun,center-9/L,center+9/L,epsabs=1e-8,limit=300)[0]
    expected=np.sqrt(np.pi)*L/2*signed_g(alpha,v,D,q0,V)
    assert integral<0 and abs(integral/expected-1)<.025,(L,integral,expected)
    print(f'nonnegative potential L={L:g} signed spectral integral={integral:.7g}; wavepacket limit={expected:.7g}')
print('all checks passed')
from scipy.optimize import minimize
# The sharp spectral power envelope, normalized by ||U||_2^2, near the cutoff.
Dc=v*v/(4*alpha); qc=2*alpha/v
C=4*alpha*alpha/(9*v*v)
for eta in [.1,.03,.01,.003,.001]:
    D=Dc*(1-eta)
    def f(par):
        q,V=par
        return V*V*signed_g(alpha,v,D,q,V)
    opt=minimize(f,[qc,v*np.sqrt(eta/2)],method='Nelder-Mead',options={'xatol':1e-13,'fatol':1e-14})
    qopt,Vopt=opt.x
    assert opt.success and abs(Vopt)<v*np.sqrt(eta)*(1+1e-8)
    actual=-opt.fun; forecast=C*eta*eta
    print(f'eta={eta:.3g}: optimal q/qc={qopt/qc:.7f}, V/(v sqrt eta)={Vopt/(v*np.sqrt(eta)):.7f}, envelope/coefficient={actual/forecast:.7f}')
    if eta<=.003: assert abs(actual/forecast-1)<.04
print('critical-envelope tests passed')
