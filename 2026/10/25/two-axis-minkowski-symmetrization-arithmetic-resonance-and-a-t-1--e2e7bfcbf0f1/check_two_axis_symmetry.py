"""Standalone mathematical checks for two-axis Minkowski symmetrization.

Uses direct harmonic reflection matrices, exact weighted enumeration of axis
sequences, and independent high-precision area quadrature. Numerical checks
corroborate but do not prove claims for all positive times and parameters.
"""
import math
import itertools


def epsilon(sig):
    return (1.0-math.exp(-sig))/4.0


def coefficients(sig, mmax):
    return {m:epsilon(sig)*math.exp(-sig*m)/m**2 for m in range(2,mmax+1)}


def project(a,b,m,alpha):
    c=math.cos(m*alpha)
    s=math.sin(m*alpha)
    dot=a*c+b*s
    return dot*c,dot*s


def harmonic_defect_from_state(coeff, state):
    return math.pi/2*sum((m*m-1)*(state[m][0]**2+state[m][1]**2) for m in coeff)


def exact_mean(sig, alpha, steps, mmax):
    coeff=coefficients(sig,mmax)
    return math.pi/2*sum((m*m-1)*a*a*(1-0.5*math.sin(m*alpha)**2)**steps for m,a in coeff.items())


def exhaustive_mean(sig, alpha, steps, mmax):
    coeff=coefficients(sig,mmax)
    total=0.0
    for seq in itertools.product([0.,alpha],repeat=steps):
        v={m:(a,0.) for m,a in coeff.items()}
        for axis in seq:
            for m in coeff:
                v[m]=project(*v[m],m,axis)
        total+=harmonic_defect_from_state(coeff,v)
    return total/(2**steps)


def boundary_area(sig, mmax, axes, ngrid=36000):
    coeff=coefficients(sig,mmax)
    v={m:(a,0.) for m,a in coeff.items()}
    for axis in axes:
        v={m:project(*v[m],m,axis) for m in coeff}
    pts=[]
    for k in range(ngrid):
        th=2*math.pi*k/ngrid
        h=1+sum(a*math.cos(m*th)+b*math.sin(m*th) for m,(a,b) in v.items())
        hp=sum(-m*a*math.sin(m*th)+m*b*math.cos(m*th) for m,(a,b) in v.items())
        x=h*math.cos(th)-hp*math.sin(th)
        y=h*math.sin(th)+hp*math.cos(th)
        pts.append((x,y))
    area=sum(pts[k][0]*pts[(k+1)%ngrid][1]-pts[(k+1)%ngrid][0]*pts[k][1] for k in range(ngrid))/2
    spectral_area=math.pi-harmonic_defect_from_state(coeff,v)
    return area,spectral_area


def log_exact_mean(sig, alpha, steps, mmax):
    w=[]
    for m in range(2,mmax+1):
        lam=1-0.5*math.sin(m*alpha)**2
        a=epsilon(sig)*math.exp(-sig*m)/m**2
        w.append(math.log(math.pi/2*(m*m-1)*a*a)+steps*math.log(lam))
    u=max(w)
    return u+math.log(sum(math.exp(x-u) for x in w))


def run():
    sig=.32
    alph=math.pi*((math.sqrt(5)-1)/2)
    for t in range(9):
        a=exhaustive_mean(sig,alph,t,8)
        b=exact_mean(sig,alph,t,8)
        assert math.isclose(a,b,rel_tol=2e-13,abs_tol=1e-15), (t,a,b)
    print('EXHAUSTIVE_TWO_AXIS_PROJECTION_SEQUENCES_OK steps=0..8, modes=2..8')
    for seq in [(),(0.,),(alph,),(0.,alph,0.,alph),(alph,0.,alph)]:
        numerical,formula=boundary_area(sig,8,seq,ngrid=7200)
        assert abs(numerical-formula)<5e-6,(numerical,formula)
    print('INDEPENDENT_SUPPORT_BOUNDARY_SHOELACE_AREAS_OK')
    rat=math.pi/3
    q=3
    residual=sum(math.pi/2*(m*m-1)*a*a for m,a in coefficients(sig,200).items() if m%q==0)
    for steps in (100,200,400):
        val=exact_mean(sig,rat,steps,200)
        assert abs(val-residual)<2e-7,(steps,val,residual)
    print('RATIONAL_AXIS_NONZERO_AREA_DEFECT_RESIDUAL_OK')
    vals=[(n,log_exact_mean(.12,alph,n,2000)) for n in (1000,10000,100000,1000000,10000000)]
    assert all(vals[i+1][1]<vals[i][1] for i in range(len(vals)-1))
    for t,logv in vals:
        assert math.isfinite(logv)
        print('BOUNDED_TYPE_LOG_MEAN_DEFECT',t,round(logv,6),'OVER_CUBEROOT',round(-logv/t**(1/3),6))
    print('ALL_TWO_AXIS_SYMMETRIZATION_CHECKS_OK')

if __name__=='__main__':
    run()
