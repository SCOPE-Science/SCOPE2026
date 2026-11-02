"""Supplementary exact/sampled tests for elliptical polynomial phase measurements."""
from fractions import Fraction
import cmath, math, random

def gauss_add(a,b): return (a[0]+b[0],a[1]+b[1])
def gauss_mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gauss_conj(a):return (a[0],-a[1])
Z=(0,0); ONE=(1,0)
def poly_laurent(coeff,c=2,d=1):
    res={0:Z}; power={0:ONE}
    for coeff_j in coeff:
        for k,v in power.items():
            res[k]=gauss_add(res.get(k,Z),gauss_mul(coeff_j,v))
        pp={}
        for k,v in power.items():
            pp[k+1]=gauss_add(pp.get(k+1,Z),gauss_mul(v,(c,0)))
            pp[k-1]=gauss_add(pp.get(k-1,Z),gauss_mul(v,(d,0)))
        power=pp
    return {k:v for k,v in res.items() if v!=Z}
def intensity_laurent(coeff,c=2,d=1):
    v=poly_laurent(coeff,c,d); res={}
    for k,x in v.items():
        for m,y in v.items():
            term=gauss_mul(x,gauss_conj(y))
            res[k-m]=gauss_add(res.get(k-m,Z),term)
    return {k:x for k,x in res.items() if x!=Z}
def evaluate_poly(coeff,z):
    total=0j
    for a in coeff[::-1]:total=total*z+complex(*a)
    return total

def run():
    count=0
    # Exact deck symmetry for the ellipse: z(w)=2w+1/w, r=1/2.
    for w in [Fraction(1,1),Fraction(2,3),Fraction(-7,5),Fraction(13,11)]:
        z=lambda v:2*v+Fraction(1,1)/v
        assert z(w)==z(Fraction(1,2)/w);count+=1
    for w in [1+1j,2-3j,-3+4j,1/3+2j]:
        z=lambda v:2*v+1/v
        assert abs(z(w)-z(0.5/w))<1e-11;count+=1
    rng=random.Random(20261031)
    for n in range(0,9):
        for j in range(24):
            coeff=[(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(n+1)]
            if coeff[-1]==Z:coeff[-1]=ONE
            intensity=intensity_laurent(coeff)
            assert all(-2*n<=k<=2*n for k in intensity)
            assert intensity.get(-2*n,Z)==gauss_conj(intensity.get(2*n,Z))
            assert all(intensity.get(-k,Z)==gauss_conj(v) for k,v in intensity.items())
            for t in [0.13,0.48,1.23,2.01,3.04]:
                w=cmath.exp(1j*t);z=2*w+1/w
                direct=abs(evaluate_poly(coeff,z))**2
                harmonic=sum(complex(*a)*w**k for k,a in intensity.items())
                assert abs(harmonic-direct)<1e-8*max(1,abs(direct));count+=1
            count+=3
        # Degree n generically has the top 2n intensity harmonic.
        top=intensity_laurent([(1,0)]*(n+1))
        if n>0: assert top.get(2*n,Z)!=Z
        count+=1
    for t in [2*math.pi*j/35 for j in range(35)]:
        w=cmath.exp(1j*t)
        assert abs(abs(w-2)-abs(1-2*w))<1e-12;count+=1
    print(f'PASS {count} supplementary assertions')
if __name__=='__main__':run()
