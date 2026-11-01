"""Reproducibility checks for mixed harmonic-Bergman Toeplitz commutators.

Checks finite identities numerically; universal claims rely on the written proof.
"""
import math

def moment(j,alpha):
    assert j>=0 and alpha>-1
    return math.exp(math.lgamma(j+1)+math.lgamma(alpha+2)-math.lgamma(j+alpha+2))

def weight(m,k,alpha):
    h=lambda r: moment(r,alpha)
    if k>=0:
        return math.sqrt(h(k+m)/h(k))
    if k<=-m:
        return math.sqrt(h(-k)/h(-k-m))
    return h(m)/math.sqrt(h(-k)*h(k+m))

def coefficient(m,n,k,alpha):
    return weight(n,k-n,alpha)*weight(m,k-n,alpha)-weight(m,k,alpha)*weight(n,k+m-n,alpha)

def tail(m,n,r,alpha):
    h=lambda j: moment(j,alpha)
    return (h(r)*h(r+m+n)-h(r+m)*h(r+n))/(h(r)*math.sqrt(h(r+m)*h(r+n)))

def run():
    checks=0
    for alpha in (-0.8,-0.25,0.,0.75,3.):
        for m in range(1,6):
            for n in range(1,6):
                for k in range(-40,41):
                    d=coefficient(m,n,k,alpha)
                    other=coefficient(m,n,n-m-k,alpha)
                    assert abs(d+other)<5e-11, (alpha,m,n,k,d,other)
                    checks+=1
                for k in range(min(0,n-m),max(0,n-m)+1):
                    assert abs(coefficient(m,n,k,alpha))<5e-11
                    checks+=1
                for r in range(0,15):
                    t=tail(m,n,r,alpha)
                    assert t>0, (alpha,m,n,r,t)
                    assert abs(coefficient(m,n,n+r,alpha)+t)<5e-11
                    assert abs(coefficient(m,n,-m-r,alpha)-t)<5e-11
                    checks+=3
    # A sample of the exact alpha=0 rational tail and leading asymptotic.
    for m,n in ((1,1),(1,3),(2,5),(4,6)):
        for r in range(0,50):
            exact=m*n/((r+m+n+1)*math.sqrt((r+m+1)*(r+n+1)))
            assert abs(tail(m,n,r,0.)-exact)<5e-12
            checks+=1
    for alpha,m,n in ((0.,1,2),(.5,2,3),(2.,3,4)):
        r=1000
        beta=(alpha+1)*m*n
        scaled=tail(m,n,r,alpha)*r*r
        assert abs(scaled/beta-1)<0.03, (alpha,m,n,scaled,beta)
        checks+=1
    print(f'PASS {checks} finite assertions')

if __name__=='__main__':run()
