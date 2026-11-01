"""Independent deterministic checks for the stated regular-polygon width formula.

Requires only Python's standard library. Numerical quadrature is corroboration,
not a replacement for the analytic all-orders proof.
"""
import math

PI=math.pi

def diff_count(n):
    return n if n%2==0 else 2*n

def maxwidth_mean(n):
    N=diff_count(n)
    h=PI/N
    amp=2.0 if n%2==0 else 2*math.cos(PI/(2*n))
    return amp*math.sin(h)/h

def polygon_width(n, theta, rotation=0.0):
    # Make a width-maximizing (difference-body vertex) direction have phase 0.
    initial=0.0 if n%2==0 else -PI/(2*n)
    dots=[math.cos(theta-(2*PI*j/n+initial+rotation)) for j in range(n)]
    return max(dots)-min(dots)

def K(L, s):
    return 2*sum(math.cos(j*L*s)/(j*j*L*L-1)**2 for j in range(1,1500))

def exact_limits(L):
    h=PI/L
    kp=h*h/(2*math.sin(h)**2)+h*math.cos(h)/(2*math.sin(h))-1
    km=h*h*math.cos(h)/(2*math.sin(h)**2)+h/(2*math.sin(h))-1
    return km,kp

def numerical_cov(n,m,s,k=32768):
    mn=maxwidth_mean(n)
    mm=maxwidth_mean(m)
    out=0.0
    for j in range(k):
        theta=2*PI*(j+0.37)/k
        x=polygon_width(n,theta)/mn-1
        y=polygon_width(m,theta,rotation=s)/mm-1
        out += x*y
    return out/k

def main():
    for n,m in ((3,3),(3,4),(4,4),(4,6),(4,8),(6,10),(5,9),(7,8)):
        N,M=diff_count(n),diff_count(m)
        L=math.lcm(N,M)
        parity=(L//N + L//M)%2
        km,kp=exact_limits(L)
        assert km < 0 < kp
        assert abs(K(L,0)-kp)<2e-12
        assert abs(K(L,PI/L)-km)<2e-12
        for phase in (0,PI/L,0.37*PI/L):
            direct=numerical_cov(n,m,phase)
            theory=K(L,phase+parity*PI/L)
            assert abs(direct-theory)<2e-8,(n,m,phase,direct,theory)
        # The two endpoint choices are opposite strict extrema by the proof.
        val0=K(L,parity*PI/L)
        valhalf=K(L,(1+parity)*PI/L)
        if parity==0:
            assert val0>valhalf
        else:
            assert val0<valhalf
    for L in (4,6,8,12,20,40,80):
        km,kp=exact_limits(L)
        h=PI/L
        assert kp>0 and km<0
        if L>=40:
            assert abs(kp/(h**4/45)-1)<0.03
            assert abs(km/(-7*h**4/360)-1)<0.03
    print('POLYGON_SUPPORT_GEOMETRY_PASSED')
    print('LCM_CROSS_COVARIANCE_PASSED')
    print('SHARP_EXTREMA_AND_ASYMPTOTICS_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
