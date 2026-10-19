"""Reproducible numerical cross-checks of diagonal star two-cycle equations.
Finite tests are not substitutes for the analytic classification.
"""
import math

def root_s(c):
    lo,hi=0.,math.pi
    for _ in range(90):
        mid=(lo+hi)/2
        if 2*mid/math.sin(mid)<c: lo=mid
        else: hi=mid
    return (lo+hi)/2

def scalar(x,c):
    return x+c*math.sin(x)

def test():
    n=0
    top=math.sqrt(math.pi**2+2)
    for d in (2,3,5,11):
        for c in (2.05,2.3,2.75,math.pi-0.01,math.pi,math.pi+0.005,3.18,3.4,top):
            h=c/(d+1)
            s=root_s(c)
            if abs(scalar(math.pi-s,c)-(math.pi+s))>1e-11: raise AssertionError((c,'mirror'))
            t=(math.pi-s)
            def diag_mult(x,y):
                return (1+c*math.cos(x))*(1+c*math.cos(y))
            def transverse_mult(x,y):
                return (1+h*math.cos(x))*(1+h*math.cos(y))
            mirror_mu=(1-c*math.cos(s))**2
            mirror_nu=(1-h*math.cos(s))**2
            assert abs(diag_mult(math.pi-s,math.pi+s)-mirror_mu)<1e-11
            assert abs(transverse_mult(math.pi-s,math.pi+s)-mirror_nu)<1e-11
            if c<math.pi: assert mirror_mu<1 and mirror_nu<1
            if c>math.pi: assert mirror_mu>1 and mirror_nu>1
            n+=6
            if c>=math.pi:
                for t in (math.asin(math.pi/c),math.pi-math.asin(math.pi/c)):
                    assert abs(scalar(t,c)-(t+math.pi))<1e-11
                    assert abs(scalar(t+math.pi,c)-t)<1e-11
                    tang=1+math.pi**2-c**2
                    norm=1-(c*c-math.pi**2)/(d+1)**2
                    assert abs(diag_mult(t,t+math.pi)-tang)<1e-11
                    assert abs(transverse_mult(t,t+math.pi)-norm)<1e-11
                    if c>math.pi and c<top-1e-9: assert -1<tang<1 and -1<norm<1
                    n+=6
    print('CHECK_OK', n, 'equation, multiplier, and stability checks')
if __name__=='__main__': test()
