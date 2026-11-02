"""Independent arithmetic and geometry checks for the Gamma spectral-index area formulas.
Analytic proof is in RESULT.md; these finite tests do not replace it.
"""
import math
import cmath


def numerical_integral(f, lo, hi, n=16000):
    assert n % 2 == 0
    h = (hi-lo)/n
    return (f(lo)+f(hi)+4*sum(f(lo+h*j) for j in range(1,n,2))
            +2*sum(f(lo+h*j) for j in range(2,n-1,2)))*h/3


def predicted_area(alpha, radius=1):
    if alpha <= 2:
        return 0.0
    assert alpha < 4
    return alpha * radius**(2*alpha) * numerical_integral(
        lambda u: math.cos(u)**(2*alpha), math.pi/alpha, math.pi/2)


def count_preimages(alpha, target, radius=1):
    if abs(target) == 0:
        return 0
    theta = cmath.phase(target)
    rr = abs(target)**(1/alpha)
    count=0
    for k in range(-6,7):
        phi = (theta+2*math.pi*k)/alpha
        if abs(phi) < math.pi/2 and rr < radius*math.cos(phi)-1e-12:
            count+=1
    return count


def check():
    exact = (5*math.pi-9*math.sqrt(3))/32
    assert abs(predicted_area(3)-exact) < 5e-11
    assert predicted_area(2)==0
    assert predicted_area(1.9)==0
    assert count_preimages(3,-0.01)==2
    assert count_preimages(3,0.01)==1
    assert count_preimages(2.5,-0.000001)==2
    assert count_preimages(2.5,0.01)==1
    for a in (2.01,2.05,2.2,2.5,3,3.5,3.9):
        th0=math.pi*(2-a/2)
        for j in range(1,20):
            theta=th0+(math.pi-th0)*j/20
            cap=math.cos((2*math.pi-theta)/a)**a
            assert count_preimages(a,0.5*cap*cmath.exp(1j*theta))==2
            assert count_preimages(a,1.1*cap*cmath.exp(1j*theta))==1
    eps=0.005
    asympt=(math.pi**5)/2560
    ratio=predicted_area(2+eps)/(eps**5)
    assert abs(ratio/asympt-1)<0.08
    print("PASS: sampled phase-count, closed-form, and asymptotic consistency checks")
    print("order 3 normalized index-2 area:",exact)
    print("critical coefficient:",asympt)

if __name__=='__main__':
    check()
