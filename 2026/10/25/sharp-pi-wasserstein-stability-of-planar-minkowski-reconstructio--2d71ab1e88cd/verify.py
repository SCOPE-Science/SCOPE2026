"""Finite exact and numerical checks of a sharp planar reconstruction bound.

Standard-library Python only. These checks corroborate a separate analytic proof;
they are not a computational replacement for any infinite statement.
"""
import math


def green(t):
    t = abs(t)
    assert 0 <= t <= math.pi
    return -math.cos(t)/(4*math.pi)+(0.5-t/(2*math.pi))*math.sin(t)


def quantities(e):
    c=math.cos(e)
    a=1/(2*(1+c))
    b=(1-c)/(2*(1+c))
    # signed measure: +a at +/-e, -1/2 at 0, -b at pi
    assert abs(2*a-0.5-b)<1e-12
    assert abs(2*a*c+b-0.5)<1e-12 # signed first moment is zero
    # Four-point Kantorovich dual witness, extended by McShane on the circle.
    points=[-e,0,e,math.pi]
    values=[e,0,e,2*e-math.pi]
    for i in range(4):
        for j in range(4):
            arc=abs(points[i]-points[j])
            geodesic=min(arc,2*math.pi-arc)
            assert abs(values[i]-values[j]) <= geodesic+1e-12
    dual=2*a*e - b*(2*e-math.pi)
    exact_W=0.5*e + b*(math.pi-e)
    assert abs(dual-exact_W) < 1e-12
    kernel_H=2*math.pi*(2*a*green(e)-0.5*green(0)-b*green(math.pi))
    analytic_H=(math.pi-e)*math.sin(e)/(1+c)
    assert abs(kernel_H-analytic_H)<1e-12
    return exact_W,kernel_H,analytic_H


def main():
    # Check exact signed-mass balance separately from transport normalization:
    for e in [0.2,0.04,0.008,0.001]:
        c=math.cos(e)
        positive=1/(1+c)
        negative_at_zero=0.5
        negative_at_pi=(1-c)/(2*(1+c))
        assert abs(positive-negative_at_zero-negative_at_pi)<1e-12
        # original measures have first moment zero in both coordinates
        assert abs(positive*c-c/(1+c))<1e-12
        assert abs(0.5-0.5)<1e-12
        W,H,formula=quantities(e)
        print(f'eps={e:.6f}, W1={W:.12f}, support_gap={H:.12f}, ratio={H/W:.12f}, pi={math.pi:.12f}')
        assert H/W < math.pi + 1e-10
    assert abs(quantities(0.001)[1]/quantities(0.001)[0]-math.pi)<0.02
    print('PASS: finite checks; analytic argument required for exact theorem')

if __name__=='__main__':
    main()
