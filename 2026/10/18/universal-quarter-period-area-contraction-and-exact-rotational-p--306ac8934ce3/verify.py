"""Independent numerical and analytic regression checks for rotation/area identities.

Uses only the Python standard library. Finite checks do not prove the theorem.
"""
import math


def close(x, y, tol=2e-8):
    assert abs(x-y) <= tol*max(1.0, abs(x), abs(y)), (x, y, x-y)


def support_reuleaux(x, n, w):
    delta = math.pi / n
    R = w/(2.0*math.cos(delta/2.0))
    x = (x+delta/2.0) % (2.0*delta)-delta/2.0
    if x <= delta/2.0:
        return w-R*math.cos(x)
    return R*math.cos(x-delta)


def regular_formula(n, w, theta):
    d = math.pi/n
    return n*w*w/4.0*(2*d-math.tan(d/2.0)-theta
                          -math.sin(d/2.0-theta)/math.cos(d/2.0))


def direct_mixed(n, w, theta, steps=18000):
    d = math.pi/n
    dx=d/steps
    s=sum(support_reuleaux(-d/2.0+(j+0.5)*dx-theta, n, w)
          for j in range(steps))
    return n*w*dx*s/2.0


def smooth_modes_area(n, w, theta, samples=24000):
    # A smooth strictly convex support, with two distinct admissible modes.
    k1, k3 = n, 3*n
    a, b = .07*w/(k1*k1-1), -.06*w/(k3*k3-1)
    def h(x):
        return w/2.0+a*math.cos(k1*x)+b*math.sin(k3*x)
    def rho(x):
        return w/2.0+(1-k1*k1)*a*math.cos(k1*x)+(1-k3*k3)*b*math.sin(k3*x)
    step=2.0*math.pi/samples
    def averaged_value(x):
        return (h(x)+h(x-theta))/2.0, (rho(x)+rho(x-theta))/2.0
    area=sum(math.prod(averaged_value((j+.5)*step)) for j in range(samples))*step/2.0
    disk=math.pi*w*w/4.0
    D0=math.pi/2.0*((k1*k1-1)*a*a+(k3*k3-1)*b*b)
    Dc=math.pi/2.0*((k1*k1-1)*a*a*math.cos(k1*theta/2.0)**2
                   +(k3*k3-1)*b*b*math.cos(k3*theta/2.0)**2)
    close(disk-area,Dc,1e-8)
    assert min(rho(2.0*math.pi*j/1000) for j in range(1000))>0
    return D0,Dc


def main():
    for n in (3,5,7,11,25):
        for w in (0.75,1.4):
            d=math.pi/n
            minarea=n*w*w*(d-math.tan(d/2.0))/2.0
            disk=math.pi*w*w/4.0
            close(regular_formula(n,w,0.0),minarea)
            close(regular_formula(n,w,d),disk)
            for t in (0.0,.13,.37,.5,.77,1.0):
                theta=t*d
                # Independently integrate the rotated support over curvature arcs.
                mixed=direct_mixed(n,w,theta)
                close((minarea+mixed)/2.0, regular_formula(n,w,theta), 3e-8)
                close(regular_formula(n,w,theta)+regular_formula(n,w,d-theta),
                      minarea+disk)
                if 0<t<1:
                    assert regular_formula(n,w,theta)>minarea
                    assert regular_formula(n,w,theta)<disk
            for t,q in ((0.0,1.0),(.5,.5),(1.0,0.0)):
                D0,Dc=smooth_modes_area(n,w,t*d)
                close(Dc,q*D0,1e-9)
            for t in (.1,.27,.58,.81):
                one=math.cos(n*(t*d)/2.0)**2
                three=math.cos(3*n*(t*d)/2.0)**2
                assert abs(one-three)>1e-5
    # Quantitative verification of the uniform asymptotic coefficient.
    for n in (51,101,201,401):
        d=math.pi/n
        errs=[]
        for t in (0.0,.16,.4,.63,1.0):
            deficit=math.pi/4.0-regular_formula(n,1.0,t*d)
            main=math.pi**3/(48.0*n*n)*(1.0-t)**2*(1.0+2.0*t)
            errs.append(abs(deficit-main)*n**4)
        assert max(errs)<3.0, (n,errs)
    print('VERIFY_OK: Reuleaux support integration, exact complementary identity,')
    print('universal three multipliers, off-grid obstruction, asymptotic scaling')


if __name__ == '__main__':
    main()
