"""Independent numerical/exact-identity checks for icosahedral shadow diameter law.

Run: python verify.py. The analytic proof is in RESULT.md; these checks are corroborative.
"""
import itertools
import math
import numpy as np
from scipy.integrate import quad

PHI = (1.0 + math.sqrt(5.0))/2.0
R = math.sqrt(1.0 + PHI*PHI)
AXES = np.array([(0,1,PHI),(0,-1,PHI),(1,PHI,0),(-1,PHI,0),
                 (PHI,0,1),(PHI,0,-1)], dtype=float)/R
TSTAR = math.sqrt((1.0 - 2.0/math.sqrt(5.0))/3.0)


def primitive(k,t):
    a = k*t/math.sqrt(1.0-t*t)
    assert abs(a) < 1.0
    return (t*math.asin(a) +
            math.atan(math.sqrt(1.0-(1.0+k*k)*t*t)/k)-math.atan(1.0/k))


def law(t):
    return 6.0*t-30.0/math.pi*(primitive(PHI,t)+primitive(1.0/PHI,t))


def check_pair_structure():
    vals = [abs(float(np.dot(AXES[i],AXES[j]))) for i,j in itertools.combinations(range(6),2)]
    assert all(abs(x-1/math.sqrt(5))<1e-13 for x in vals)
    assert len(vals)==15
    positives=[]; negatives=[]
    signs=np.array(list(itertools.product([-1.,1.],repeat=3)))
    for triple in itertools.combinations(range(6),3):
        A=AXES[list(triple)]
        gram=A@A.T
        prod=gram[0,1]*gram[0,2]*gram[1,2]
        if prod>0: positives.append(triple)
        else: negatives.append(triple)
        inverse=np.linalg.inv(A)
        radius=max(float(np.linalg.norm(inverse@q)) for q in signs)
        got=1/radius
        expected=1/math.sqrt(5) if prod>0 else TSTAR
        assert abs(got-expected)<1e-12, (triple,got,expected)
    assert len(positives)==len(negatives)==10
    print('SIX_AXIS_EQUILINEAR_GRAM_AND_TRIPLE_THRESHOLD_OK',len(positives),len(negatives))


def check_closed_form():
    for t in [0.0001,0.01,.04,.08,.12,.17,TSTAR]:
        def integrand(x):
            q=x/math.sqrt(1-x*x)
            return (math.asin(PHI*q)+math.asin(q/PHI))*2/math.pi
        overlap=quad(integrand,0,t,epsabs=2e-13,epsrel=2e-13)[0]
        assert abs(law(t)-(6*t-15*overlap))<2e-12
    for t in [1e-4,.0005,.001]:
        asym=6*t-(15*math.sqrt(5)/math.pi)*t*t-(25*math.sqrt(5)/(4*math.pi))*t**4
        assert abs(law(t)-asym)<3e-10
    print('PAIR_BELT_INTEGRAL_AND_QUARTIC_ASYMPTOTIC_OK')


def check_direct_geometry():
    rng=np.random.default_rng(24165)
    vertices=np.concatenate([R*AXES,-R*AXES])
    for u in rng.normal(size=(300,3)):
        u=u/np.linalg.norm(u)
        proj=vertices-np.outer(vertices@u,u)
        brute=np.sqrt(np.max(np.sum((proj[:,None,:]-proj[None,:,:])**2,axis=2)))
        m=np.min(np.abs(AXES@u))
        via=2*R*math.sqrt(1-m*m)
        assert abs(brute-via)<1e-12
    print('INDEPENDENT_TWELVE_VERTEX_PROJECTED_DIAMETER_OK')


def check_haar_sampling():
    rng=np.random.default_rng(293042)
    n=1_200_000
    hit=np.zeros(3,dtype=int)
    ts=np.array([.07,.12,.17])
    for _ in range(12):
        normals=rng.normal(size=(100000,3))
        normals/=np.linalg.norm(normals,axis=1)[:,None]
        marks=np.min(np.abs(normals@AXES.T),axis=1)
        hit+=(marks[:,None]<ts).sum(axis=0)
    for t,hits in zip(ts,hit):
        observed=hits/n
        expected=law(float(t))
        stderr=math.sqrt(expected*(1-expected)/n)
        assert abs(observed-expected) <= 5*stderr+0.0002,(t,observed,expected,stderr)
        print('HAAR_SHADOW_DIAMETER_TAIL',format(float(t),'.3f'),format(observed,'.6f'),format(expected,'.6f'))
    print('INDEPENDENT_HAAR_SAMPLING_OK',n)


if __name__=='__main__':
    check_pair_structure()
    check_closed_form()
    check_direct_geometry()
    check_haar_sampling()
    print('ALL_ICOSAHEDRAL_SHADOW_DIAMETER_CHECKS_OK')
