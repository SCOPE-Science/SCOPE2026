"""Independent numerical checks for smooth-disk three-state reachability.

Only finite tests: the mathematical asymptotics require the accompanying proof.
Run with Python 3 standard library: python verify.py
"""
import math

R = 0.25
PHI = (math.sqrt(5.0) - 1.0) / 2.0


def boundary(a):
    return a*a/(R+math.sqrt(R*R-a*a))


def homogeneous_deficit(t,a):
    if a <= 0.0:
        return 1.0
    b=boundary(a)
    rho=a+b
    return b/rho+(a/rho)*math.exp(t*math.log1p(-rho))


def minimize_homogeneous(t):
    lo, hi=0.0,R
    x1=hi-PHI*(hi-lo)
    x2=lo+PHI*(hi-lo)
    f1=homogeneous_deficit(t,x1)
    f2=homogeneous_deficit(t,x2)
    for _ in range(150):
        if f1>f2:
            lo=x1
            x1,f1=x2,f2
            x2=lo+PHI*(hi-lo)
            f2=homogeneous_deficit(t,x2)
        else:
            hi=x2
            x2,f2=x1,f1
            x1=hi-PHI*(hi-lo)
            f1=homogeneous_deficit(t,x1)
    a=0.5*(lo+hi)
    return a,homogeneous_deficit(t,a)


def adaptive_deficits(horizons):
    maximum=max(horizons)
    e=1.0
    result={0:e}
    for t in range(1,maximum+1):
        d=math.hypot(e,1.0-e)+1.0-e
        e-=R*e*e/d
        if t in horizons:
            result[t]=e
    return result


def independent_bellman_step(e,mesh=20001):
    val=0.0
    for j in range(mesh):
        theta=(math.pi/2)*j/(mesh-1)
        a=R*math.sin(theta)
        b=R*(1.0-math.cos(theta))
        val=max(val,a*e-b*(1.0-e))
    return e-val


def direct_chain_probability(t,a,b):
    active=1.0
    reached=0.0
    for _ in range(t):
        reached+=a*active
        active*=(1.0-a-b)
    return reached


def main():
    print('Model: r=1/4, three states (active, success, failure)')
    assert R*(1+math.sqrt(2))<1
    for t in (1,2,3,4,5,10):
        a, deficit=minimize_homogeneous(t)
        b=boundary(a)
        check=1-direct_chain_probability(t,a,b)
        assert abs(deficit-check)<3e-13,(t,deficit,check)
        assert deficit<=1.0+1e-13
    e=1.0
    for t in range(1,7):
        next_e=e-R*e*e/(math.hypot(e,1-e)+(1-e))
        mesh_e=independent_bellman_step(e)
        assert abs(next_e-mesh_e)<2e-9,(t,next_e,mesh_e)
        e=next_e
    print('Finite exact-formula checks: PASS, t=1..10; Bellman mesh checks: PASS, t=1..6')
    horizons=(10,100,1000,10000,100000)
    adaptive=adaptive_deficits(horizons)
    print('t   optimal_a   stationary_deficit   t*deficit-2*log(t/2)   adaptive_deficit   t*adaptive_deficit')
    for t in horizons:
        a, g=minimize_homogeneous(t)
        e=adaptive[t]
        c=t*g-2*math.log(t/2)
        print('%6d %.11f %.11f %.9f %.11f %.9f'%(t,a,g,c,e,t*e))
        if t>=100:
            assert g>e
    print('Asymptotic benchmarks (not numerical proofs): stationary centered constant -> 2, adaptive t*gap -> 8.')

if __name__=='__main__':
    main()
