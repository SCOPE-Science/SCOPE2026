#!/usr/bin/env python3
"""Independent rectangle difference-density integral checks of a cone tail expansion."""
import mpmath as mp
mp.mp.dps=70

def coefficients(a,b):
    d=mp.sqrt(a*a+b*b)
    A=d*d/(2*a*b)
    M=A*(a/b-b/a)/3
    Q=A*(b*b/(a*a)+a*a/(b*b)-1)/6
    B=2*Q*A/15+M*M/10
    c0=2*A*A/(3*a*a*b*b)
    c1=12*B/(d*a*a*b*b)
    return d,c0,c1

def independent_tail(a,b,eps):
    d=mp.sqrt(a*a+b*b)
    xstar=a-mp.sqrt((d-eps)**2-b*b)
    def integrand(x):
        y=b-mp.sqrt((d-eps)**2-(a-x)**2)
        return 2*x*y*y/(a*a*b*b)
    return mp.quad(integrand,[0,xstar])

def main():
    cases=[(mp.mpf(1),mp.mpf(1)),(mp.mpf(2),mp.mpf(1)),
           (mp.mpf(3)/2,mp.mpf(4)/3)]
    tests=0
    for a,b in cases:
        d,c0,c1=coefficients(a,b)
        assert c0>0 and c1>0
        for ep in ['0.04','0.02','0.01','0.005']:
            eps=mp.mpf(ep)
            actual=independent_tail(a,b,eps)
            assert actual>0
            fifth=(actual-c0*eps**4)/eps**5
            if eps<=mp.mpf('0.01'):
                assert abs(fifth/c1-1)<mp.mpf('0.035'), (a,b,ep,fifth,c1)
            tests+=1
        if a==b==1:
            assert mp.almosteq(c0,mp.mpf(2)/3)
            assert mp.almosteq(c1,4/(15*mp.sqrt(2)))
    print('DIAMETER_TAIL_CHECK_OK comparisons='+str(tests))

if __name__=='__main__':main()
