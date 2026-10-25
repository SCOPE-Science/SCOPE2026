"""Numerical checks for the six/eight-sided central-section theorem.

Run: python checks/check_sections.py
Only NumPy and SciPy are needed. The asymptotic theorem is proved analytically;
finite orientation samples are supplementary diagnostics, not its proof.
"""
import itertools
import math

import numpy as np
from scipy.integrate import quad


def p8_formula(scales):
    terms = []
    for i in range(3):
        a = scales[i]
        b, c = (scales[j] for j in range(3) if j != i)
        t = a*a / ((math.hypot(a, b)+b)*(math.hypot(a, c)+c))
        terms.append(math.atan(t))
    return (4/math.pi)*sum(terms)


def positive_octant_integral(scales):
    result = 0.0
    for i in range(3):
        a = scales[i]
        b, c = (scales[j] for j in range(3) if j != i)
        def f(phi):
            z = b*math.cos(phi) + c*math.sin(phi)
            return 1 - z/math.hypot(a, z)
        result += quad(f, 0, math.pi/2, epsabs=3e-12)[0]
    return 2*result/math.pi


def arcs(scales):
    ans = []
    for i in range(3):
        a = scales[i]
        b, c = (scales[j] for j in range(3) if j != i)
        ans.append(math.acos(b*c / (math.hypot(a,b)*math.hypot(a,c))))
    return ans


def geometric_edges(scales):
    # 24 polyhedral edges from each of the six four-valent axis vertices to
    # its four adjacent three-valent vertices.
    E = []
    for j in range(3):
        for sign in (-1., 1.):
            axis = np.zeros(3)
            axis[j] = 2 * sign * scales[j]
            for signs in itertools.product((-1., 1.), repeat=3):
                if signs[j] == sign:
                    E.append((axis, np.array(signs)*scales))
    assert len(E) == 24
    return np.array(E)


def edge_counts(normals, edges):
    out = np.empty(len(normals), dtype=np.int16)
    for start in range(0,len(normals),20000):
        sub=normals[start:start+20000]
        out[start:start+len(sub)] = np.count_nonzero((sub @ edges[:,0,:].T)*(sub @ edges[:,1,:].T)<0,axis=1)
    return out


def analytic_types(normals, scales):
    w=np.abs(normals)*np.asarray(scales)
    return np.where(2*np.max(w,axis=1)>np.sum(w,axis=1),8,6)


def spherical_uniform(rng, n):
    x=rng.normal(size=(n,3))
    return x/np.linalg.norm(x,axis=1)[:,None]


def check():
    rng=np.random.default_rng(703801)
    test_scales=[(1.,1.,1.),(3.,1.,0.5),(0.4,0.7,2.)]
    for scales in test_scales:
        pp=p8_formula(scales)
        pquad=positive_octant_integral(scales)
        assert abs(pp-pquad)<2e-12,(scales,pp,pquad)
        d=arcs(scales)
        assert abs(sum(d)-math.pi)<2e-13
        a,b,c=scales
        S2=a*a+b*b+c*c
        cot=(b*c/(a*math.sqrt(S2)),a*c/(b*math.sqrt(S2)),a*b/(c*math.sqrt(S2)))
        assert abs(cot[0]*cot[1]+cot[1]*cot[2]+cot[2]*cot[0]-1)<1e-13
        x=spherical_uniform(rng,350000)
        predicted=analytic_types(x,scales)
        from_edges=edge_counts(x,geometric_edges(np.asarray(scales)))
        assert np.array_equal(from_edges,predicted)
        measured=np.mean(from_edges==8)
        assert abs(measured-pp)<0.005
        print('CROSS_SECTION_EDGE_ENUMERATION_AND_INDEPENDENT_OCTANT_QUADRATURE_OK',scales,'P8=',round(pp,8),'MC=',round(measured,8))
    # Uniform random geodesic motion and 6-to-8 / 8-to-6 transitions.
    n=1350000
    x=spherical_uniform(rng,n)
    w=spherical_uniform(rng,n)
    w-=np.sum(w*x,axis=1)[:,None]*x
    w/=np.linalg.norm(w,axis=1)[:,None]
    for scales in ((1.,1.,1.),(3.,1.,0.5)):
        before=analytic_types(x,scales)
        t=.012
        after=analytic_types(math.cos(t)*x+math.sin(t)*w,scales)
        ch=np.mean(before!=after)/t
        forward=np.mean((before==6)&(after==8))/t
        backward=np.mean((before==8)&(after==6))/t
        assert abs(ch-4/math.pi)<0.045,(scales,ch)
        assert abs(forward-2/math.pi)<0.032
        assert abs(backward-2/math.pi)<0.032
        print('GEODESIC_TYPE_TRANSITION_STATISTICS_OK',scales,'total/t=',round(ch,6),'forward/t=',round(forward,6),'backward/t=',round(backward,6))
    equal=12*math.acos(1/math.sqrt(3))/math.pi-3
    assert abs(equal-p8_formula((1.,1.,1.)))<2e-14
    assert p8_formula((40,1,1))>.98
    print('EQUAL_AXIS_FORMULA_AND_ANISOTROPIC_VARIATION_OK')
    print('ALL_RHOMBIC_DODECAHEDRON_SECTION_TESTS_OK')


if __name__=='__main__':
    check()
