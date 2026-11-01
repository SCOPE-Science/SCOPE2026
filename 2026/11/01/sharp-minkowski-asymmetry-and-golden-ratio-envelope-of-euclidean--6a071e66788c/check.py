"""Independent symbolic and polygonal checks of ball-slab asymmetry.

Usage: python check.py
Requires numpy, scipy, sympy. Numerical polygon tests corroborate but do not
replace the all-dimensional analytic containment proof.
"""
from __future__ import annotations
import math
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog, brentq
from scipy.spatial import ConvexHull
import sympy as sp

PHI = (1 + math.sqrt(5)) / 2

def exact_root(a,b):
    if abs(a + b)<1e-13:
        return 1.0, 0.0
    if a+b<0:
        s,z=exact_root(-b,-a)
        return s,-z
    aa = 1-a*a
    q = -2*a*(b-a)
    r = -(1+b*b-2*a*b)
    s = (-q + math.sqrt(q*q-4*aa*r))/(2*aa)
    z=(b+s*a)/(1+s)
    return s,z

def polygonal_lp(a,b,resolution=1400):
    # The polygon is an *independently constructed* inscribed approximation
    # to the Euclidean circle clipped by the two horizontal support planes.
    angles=np.linspace(0,2*math.pi,resolution,endpoint=False)
    points=np.array([(math.cos(q),math.sin(q)) for q in angles if a-1e-13 <= math.cos(q) <= b+1e-13])
    points=np.vstack([points, [a,math.sqrt(max(0,1-a*a))], [a,-math.sqrt(max(0,1-a*a))],
                      [b,math.sqrt(max(0,1-b*b))],[b,-math.sqrt(max(0,1-b*b))]])
    hull=ConvexHull(points)
    vertices=points[hull.vertices]
    normals=hull.equations[:,:2]
    offsets=hull.equations[:,2]
    rhs=(normals@vertices.T).min(axis=1)
    A=np.column_stack([normals,offsets])
    solution=linprog([0,0,1],A_ub=A,b_ub=rhs,bounds=[(None,None),(None,None),(1,None)],method='highs')
    if not solution.success:raise RuntimeError(solution.message)
    return solution.x[2],solution.x[:2]/(1+solution.x[2])

def main():
    a,b,s=sp.symbols('a b s',real=True)
    F=(1-a*a)*s*s-2*a*(b-a)*s-(1+b*b-2*a*b)
    G=s*(2-s)*(s*s-1)
    Fcomp=s*(2-s)*(a-b*(s-1)/(s*(2-s)))**2 +s*s-1-b*b/(s*(2-s))
    assert sp.cancel(F-Fcomp)==0
    assert sp.simplify(sp.diff(G,s)-2*(2*s-1)*(1+s-s*s))==0
    assert sp.simplify(F.subs(s,1))==a*a-b*b
    assert sp.simplify(F.subs(b,1)-(1-a)*((1+a)*s*s-2*a*s-2))==0
    print('EXACT_QUADRATIC_AND_COMPLETED_SQUARE_IDENTITIES_PASSED')

    cases=[(-1,1),(-.9,.9),(-.9,.95),(-.5,.8),(-.5,1),
           (-.2,.9),(0,.2),(0,1),(.05,.55),(.25,.75),(.5,1),(.9,.95),(.95,.99),(-1,.2)]
    tests=0
    for lo,hi in cases:
        expected,center=exact_root(lo,hi)
        observed,lc=polygonal_lp(lo,hi)
        assert abs(observed-expected)<3.5e-4,(lo,hi,expected,observed)
        assert np.linalg.norm(lc-np.array([center,0]))<3e-3,(lo,hi,center,lc)
        tests+=1
    print('INDEPENDENT_POLYGONAL_MINKOWSKI_LP_CHECKS_PASSED',tests)

    # Verify that every nontrivial formula is a valid containment and that
    # lowering the scale violates a rim inequality, using rational inputs.
    pairs=[(Fraction(-9,10),Fraction(19,20)),
           (Fraction(-1,2),Fraction(1,1)),
           (Fraction(0,1),Fraction(1,1)),
           (Fraction(1,4),Fraction(3,4)),
           (Fraction(7,8),Fraction(15,16))]
    for lo,hi in pairs:
        a=float(lo); b=float(hi)
        r,z=exact_root(a,b)
        C=(r+1)*z
        assert 0 < C < r+1
        assert abs((C-a)**2+1-a*a-r*r)<2e-11
        assert C>=b+r*a-1e-11
        assert C<=a+r*b+1e-11
        assert a<z<b
        for t in [1+(r-1)*k/10 for k in range(1,10)]:
            # Necessary rim and upper-cut constraints are inconsistent.
            assert (b+(t-1)*a)**2+1-a*a>t*t
    print('RIM_CONTACT_AND_STRICT_LOWER_SCALE_CERTIFICATES_PASSED',len(pairs))

    for upper in [.1,.2,.5,.8,.95,.999]:
        m=brentq(lambda v:v*(2-v)*(v*v-1)-upper*upper,1,PHI)
        lo=upper*(m-1)/(m*(2-m))
        assert 0<lo<upper
        predicted,_=exact_root(lo,upper)
        assert abs(predicted-m)<1e-10
        for j in range(101):
            cut=-upper+(2*upper-1e-10)*j/100
            val,_=exact_root(cut,upper)
            assert val<=m+1e-9,(upper,cut,val,m)
            if abs(cut-lo)>upper*.02:
                assert val<m-1e-8
    print('SHARP_FIXED_UPPER_CUT_ENVELOPE_AND_UNIQUE_OPTIMIZER_PASSED',6)

    for lo,hi in [(-.99,1),(-.8,1),(-.2,.8),(0,1),(.5,.95),(.95,1)]:
        v,_=exact_root(lo,hi)
        assert 1<=v<PHI
    assert abs(exact_root(1-1e-8,1)[0]-PHI)<5e-8
    print('GOLDEN_RATIO_CEILING_AND_ENDPOINT_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
