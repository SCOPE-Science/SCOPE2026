#!/usr/bin/env python3
"""Independent edge-intersection enumeration for a centered triangular prism.
This checks numerical consequences of the theorem; the analytic proof is separate.
Uses only Python standard library.
"""
import math

PI=math.pi
SQ3=math.sqrt(3.0)

def predicted(h):
    s=math.sqrt(1+h*h)
    a=math.asin(1/(2*s))
    b=math.asin(SQ3/(2*s))
    c=math.asin(1/s)
    return (1-6*a/PI, 6*(2*a-2*b+c)/PI, 6*(2*b-a-c)/PI)

def edge_counts(h, nphi=640, nz=640):
    """Deterministic equal-area spherical midpoint grid, without formula-based classification."""
    buckets=[0,0,0]
    for i in range(nphi):
        phi=2*PI*(i+.5)/nphi
        cs=[math.cos(phi-2*PI*j/3) for j in range(3)]
        for k in range(nz):
            z=(k+.5)/nz
            xy=math.sqrt(1-z*z)
            top=[xy*c+h*z for c in cs]
            bot=[xy*c-h*z for c in cs]
            n=0
            for xs in (top,bot):
                n+=int(xs[0]*xs[1]<0)
                n+=int(xs[1]*xs[2]<0)
                n+=int(xs[2]*xs[0]<0)
            for j in range(3):
                n+=int(top[j]*bot[j]<0)
            assert 3<=n<=5, ('invalid planar polygon',h,phi,z,n)
            buckets[n-3]+=1
    return tuple(b/(nphi*nz) for b in buckets)

def root():
    def g(h):
        return 1+h/math.sqrt(4*h*h+3)-2*SQ3*h/math.sqrt(4*h*h+1)
    lo,hi=0.0,4.0
    for _ in range(80):
        mid=(lo+hi)/2
        if g(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def main():
    assert abs(sum(predicted(.4))-1)<1e-13
    for h in (0.03,0.1,0.3,0.531469551063612,1.,3.):
        p=predicted(h)
        q=edge_counts(h)
        assert all(0<=v<=1 for v in p)
        errors=[abs(a-b) for a,b in zip(p,q)]
        print('h',h,'exact',tuple(round(x,9) for x in p),'grid',tuple(round(x,9) for x in q),'max_err',max(errors))
        assert max(errors)<.003, (h,p,q)
    x=root()
    assert abs(x-.531469551063612)<1e-12
    left=predicted(x-.02)[2]; mid=predicted(x)[2]; right=predicted(x+.02)[2]
    assert mid>left and mid>right
    print('unique-stationary-root',x,'pentagon-probability',mid)
    for h in (.005,.01,.02):
        p3,p4,p5=predicted(h)
        assert abs(p3/h**2 - SQ3/PI)<.02
        assert abs(p5/h - 6/PI)<.13
        print('thin_limit h',h,'p3/h^2',p3/h**2,'p5/h',p5/h)
    print('PASS: direct 9-edge counts, exact probabilities, root and limiting coefficients')
if __name__=='__main__':
    main()
