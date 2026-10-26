"""Standalone reproducibility checker for the Hamming oscillatory-kernel phase test.
Python 3 with standard library. Verifies finite Fourier sums independently of the tensor formula.
"""
import cmath, itertools, math, random
from fractions import Fraction

def spectral_exact(q,n,r,theta):
    G=list(itertools.product(range(q),repeat=n))
    dists=[sum(x!=0 for x in v) for v in G]
    result={}
    for chi in G:
        k=sum(j!=0 for j in chi)
        if k in result:continue
        v=sum(r**dist*math.cos(theta*dist)*cmath.exp(-2j*math.pi*sum(a*b for a,b in zip(chi,x))/q) for x,dist in zip(G,dists))
        result[k]=v
    return result

def closed(q,n,r,theta):
    z=r*cmath.exp(1j*theta)
    return {k:((1+(q-1)*z)**(n-k)*(1-z)**k).real for k in range(n+1)}

def two_tests(q,n,r,theta):
    phi=math.pi/(2*n)
    return (r*math.sin(theta+phi)<=math.sin(phi)+1e-11 and
            (q-1)*r*math.sin(theta-phi)<=math.sin(phi)+1e-11)

def run():
    rng=random.Random(271026)
    nc=0
    for q,n in itertools.product((2,3,4,5),(1,2,3)):
        for t in range(45):
            r=rng.random()
            theta=rng.random()*math.pi/2
            a=spectral_exact(q,n,r,theta)
            b=closed(q,n,r,theta)
            assert len(a)==n+1
            assert max(abs(a[k]-b[k]) for k in b)<5e-11,(q,n,r,theta,a,b)
            assert max(abs(a[k].imag) for k in a)<5e-11
            positive=min(v.real for v in a.values())>=-1e-11
            assert two_tests(q,n,r,theta)==positive,(q,n,r,theta,a)
            nc+=1
    q,n,r=3,2,Fraction(3,4)
    rr=float(r); phi=math.pi/(2*n)
    a=math.sin(phi)/rr
    low=math.asin(a)-phi
    high=math.pi-math.asin(a)-phi
    cap=phi+math.asin(math.sin(phi)/((q-1)*rr))
    critical=math.sqrt(q*q+(q-2)**2)/(2*(q-1))
    assert 1/math.sqrt(2)<rr<critical
    assert 0<low<high<cap<math.pi/2
    for theta in (low/2,(low+high)/2,(high+cap)/2,(cap+math.pi/2)/2):
        assert (min(v.real for v in spectral_exact(q,n,rr,theta).values()) >= -1e-10)==two_tests(q,n,rr,theta)
    print('PASS: direct finite-group character sums, all eigenvalues and boundary-sensitive sign tests:',nc)
    print('q=3 n=2 r=3/4: low endpoint',repr(low),'upper island',repr((high,cap)),'critical',repr(critical))
    print('No finite sample establishes the result for arbitrary q,n; use the analytic character-factorization proof.')
if __name__=='__main__':run()
