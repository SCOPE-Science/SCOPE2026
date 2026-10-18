"""Independent deterministic numerical checks for the affine-plane section theorem.

Run: python3 checker.py.  Only Python standard-library modules are required.
The geometric proof is in RESULT.md; numerical quadrature is not a proof.
"""
import math

PI = math.pi
ROOT2 = math.sqrt(2.0)


def angles(t):
    h = math.sqrt(1.0 + 2.0*t*t)
    return (2.0*math.acos(t/h), 2.0*math.acos(1.0/h))


def probability(t):
    ell = math.hypot(1.0,t)
    alpha,beta = angles(t)
    angular_average = (2.0*ell*alpha+ROOT2*beta)/(2.0*ell+ROOT2)
    return 2.0*PI/angular_average-3.0


def analytic_mean_width(t):
    ell=math.hypot(1.0,t)
    alpha,beta=angles(t)
    return (2.0*ell*alpha+ROOT2*beta)/PI


def plane_section_integrals(t, count=180001):
    """Fibonacci equal-area spherical rule, no sampling of plane offset needed."""
    points=((1.,1.,t),(1.,-1.,-t),(-1.,1.,-t),(-1.,-1.,t))
    golden=PI*(3.0-math.sqrt(5.0))
    quad_gap=width=total_crossing=0.
    for i in range(count):
        z=1.0-2.0*(i+0.5)/count
        r=math.sqrt(max(0.0,1.0-z*z))
        angle=i*golden
        ux,uy=r*math.cos(angle),r*math.sin(angle)
        vals=sorted(ux*x+uy*y+z*z0 for x,y,z0 in points)
        gaps=[vals[j+1]-vals[j] for j in range(3)]
        width+=vals[3]-vals[0]
        quad_gap+=gaps[1]
        # For four generic projected values, edge crossings total 3*g1+4*g2+3*g3.
        total_crossing+=3.0*gaps[0]+4.0*gaps[1]+3.0*gaps[2]
    width/=count;quad_gap/=count;total_crossing/=count
    return quad_gap/width,width,total_crossing/width


def main():
    root=2.0*PI/math.acos(-1.0/3.0)-3.0
    assert abs(probability(1.0)-root)<1.e-13
    assert abs(probability(1.e-7)-(ROOT2-1.0))<1.e-10
    assert abs(probability(1.e7)-1.0)<1.e-6
    for t in (.13,.3,.7,1.0,1.8,3.5,9.):
        q,w,n=plane_section_integrals(t)
        expected=probability(t)
        assert abs(q-expected)<2.0e-4,(t,q,expected)
        assert abs(w-analytic_mean_width(t))<3.e-4,(t,w,analytic_mean_width(t))
        assert abs(n-(3.0+q))<2.e-12
        print('t=%g empirical_quad=%.9f analytic=%.9f'%(t,q,expected))
    grid=[math.exp((i-60)/20.) for i in range(121)]
    for lo,hi in zip(grid,grid[1:]):
        if hi <= 1.0: assert probability(lo) > probability(hi)-1.e-13
        if lo >= 1.0: assert probability(lo) < probability(hi)+1.e-13
    coeff=PI*ROOT2/(9.0*math.acos(-1.0/3.0)**2)
    for e in (1.e-2,5.e-3,2.e-3):
        q=(probability(1.0+e)+probability(1.0-e))/2
        assert abs((q-root)/(e*e)-coeff)<4.e-4
    print('VERIFY_OK')


if __name__=='__main__':
    main()
