"""Independent numerical checks for short Euclidean distances on convex polyhedral boundaries.

Run: python check_polyhedral_surface_euclidean.py
Requires numpy and scipy. This checks specific identities, not the universal theorem.
"""
import math
import numpy as np
from scipy.integrate import quad, dblquad
from scipy.special import gamma
from scipy.stats import qmc


def wedge_cross(alpha):
    """Cross-facet unit-radius integral using the ORIGINAL (s,t) variables.

    Distance^2=s^2+t^2-2st cos(alpha)+u^2; integrating u gives
    2 sqrt(1-s^2-t^2+2st cos(alpha)).
    """
    c, sa = math.cos(alpha), math.sin(alpha)
    sm = 1/sa if c > 0 else 1.0
    def lower(s):
        disc=max(0.0,1-s*s*sa*sa)
        return max(0.0, s*c-math.sqrt(disc))
    def upper(s):
        disc=max(0.0,1-s*s*sa*sa)
        return max(0.0, s*c+math.sqrt(disc))
    def integrand(t,s):
        z = 1-s*s-t*t+2*s*t*c
        return 2*math.sqrt(max(z,0.0))
    return dblquad(integrand,0,sm,lower,upper,epsabs=2e-8,epsrel=2e-8)[0]

for alpha in [0.75,math.acos(1/3),math.pi/2,2.4]:
    numerical=wedge_cross(alpha)
    expected=2*(math.pi-alpha)/(3*math.sin(alpha))
    assert abs(numerical-expected)<5e-7,(alpha,numerical,expected)
    print('DIRECT_TWO_FACET_WEDGE_QUADRATURE_OK',f'alpha={alpha:.8f}',f'value={numerical:.10f}')

# The two independently integrated cube face-pair kernels are not supplied the predicted polynomials.
def same_square_quadrature(r):
    def theta_kernel(theta):
        c,s=abs(math.cos(theta)),abs(math.sin(theta))
        # radial integration of (1-rho*c)*(1-rho*s)*rho
        return r*r/2-(c+s)*r**3/3+c*s*r**4/4
    return quad(theta_kernel,0,2*math.pi,epsabs=1e-11,points=[math.pi/2,math.pi,3*math.pi/2])[0]

def across_right_angle_unit_squares(r):
    # Original coordinate integral after integrating positions along the common edge:
    # integral_{s^2+t^2<=r^2, s,t>=0} (2*q-q^2) ds dt, q=sqrt(r^2-s^2-t^2).
    return dblquad(lambda t,s: (2*math.sqrt(max(0,r*r-s*s-t*t))-(r*r-s*s-t*t)),
                   0,r,lambda s:0,lambda s:math.sqrt(max(0,r*r-s*s)),
                   epsabs=1e-9,epsrel=1e-9)[0]

for r in [0.2,0.45,0.8]:
    same=same_square_quadrature(r)
    cross=across_right_angle_unit_squares(r)
    same_exact=math.pi*r*r-8*r**3/3+r**4/2
    cross_exact=math.pi*r**3/3-math.pi*r**4/8
    assert abs(same-same_exact)<1e-9,(same,same_exact)
    assert abs(cross-cross_exact)<2e-8,(cross,cross_exact)
    unnormalized=6*same+24*cross
    formula=6*math.pi*r*r+(8*math.pi-16)*r**3+(3-3*math.pi)*r**4
    assert abs(unnormalized-formula)<5e-7
    print('INDEPENDENT_CUBE_FACE_PAIR_INTEGRALS_OK',r,f'P={unnormalized/36:.10f}')

# Independent direct sampling: choose two faces and two surface points, not decomposition formulas.
# Deterministic Sobol sampling on surface point pairs yields a rough external validation.
N=2**20
U=qmc.Sobol(d=6,scramble=True,seed=20261019).random_base2(int(math.log2(N)))
f1=np.floor(6*U[:,0]).astype(int)
f2=np.floor(6*U[:,1]).astype(int)
def makepoints(f,a,b):
    p=np.zeros((len(f),3))
    axis=f//2
    sgn=(f%2).astype(float)
    p[np.arange(len(f)),axis]=sgn
    other1=(axis+1)%3
    other2=(axis+2)%3
    p[np.arange(len(f)),other1]=a
    p[np.arange(len(f)),other2]=b
    return p
p=makepoints(f1,U[:,2],U[:,3]); q=makepoints(f2,U[:,4],U[:,5]); dist=np.linalg.norm(p-q,axis=1)
for r in [0.35,0.6,0.8]:
    empirical=np.mean(dist<=r)
    predicted=(6*math.pi*r*r+(8*math.pi-16)*r**3+(3-3*math.pi)*r**4)/36
    assert abs(empirical-predicted)<0.002,(r,empirical,predicted)
    print('DIRECT_FACE_SAMPLING_CUBE_CDF_OK',r,f'got={empirical:.8f}',f'wanted={predicted:.8f}')

# A crease closes with quadratic, not linear, edge coefficient.
for eps in [1e-2,1e-3,1e-4]:
    t= (4/3)*(eps/math.sin(eps)-1)
    assert abs(t/eps**2-2/9)<5e-6
print('QUADRATIC_HINGE_DEFECT_SCALING_OK')
print('ALL_POLYHEDRAL_SURFACE_EUCLIDEAN_CHECKS_OK')
