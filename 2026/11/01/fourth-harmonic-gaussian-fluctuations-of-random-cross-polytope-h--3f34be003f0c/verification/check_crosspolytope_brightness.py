"""Self-contained numerical checks for cross-polytope random hyperplane brightness.
Requires Python >=3.10 and mpmath for stable high-precision gamma differences.
All finite tests are illustrations and do not replace the analytic proof.
"""
import itertools
import math
import random
import mpmath as mp

mp.mp.dps = 75


def theoretical_moments(d):
    d = int(d)
    mu = mp.sqrt(d) * mp.gamma(mp.mpf(d)/2) / (mp.sqrt(mp.pi)*mp.gamma(mp.mpf(d+1)/2))
    z2 = mp.fsum(mp.binomial(d,k)/mp.power(2,d)*2/mp.pi * (
        mp.sqrt(max(mp.mpf('0'),1-(1-mp.mpf(2)*k/d)**2))
        +(1-mp.mpf(2)*k/d)*mp.asin(1-mp.mpf(2)*k/d)) for k in range(d+1))
    return mu, z2, z2-mu*mu


def harmonic(d, u):
    return sum(t**4 for t in u)-3/(d+2)


def sign_expectation(u):
    n = len(u)
    return sum(abs(sum(t*s for t,s in zip(u, sign)))
               for sign in itertools.product((-1,1), repeat=n))/(2**n)


def hull_area(points):
    pts=sorted(set(points))
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def chain(seq):
        out=[]
        for p in seq:
            while len(out)>1 and cross(out[-2],out[-1],p)<=0:
                out.pop()
            out.append(p)
        return out
    hull=chain(pts)[:-1]+chain(pts[::-1])[:-1]
    return abs(sum(hull[i][0]*hull[(i+1)%len(hull)][1]-hull[(i+1)%len(hull)][0]*hull[i][1]
                   for i in range(len(hull))))/2


def direct_3d_shadow(u):
    # Orthonormal basis of the plane perpendicular to u.
    ref=(1.,0.,0.) if abs(u[0])<.8 else (0.,1.,0.)
    b=(u[1]*ref[2]-u[2]*ref[1],u[2]*ref[0]-u[0]*ref[2],u[0]*ref[1]-u[1]*ref[0])
    nb=math.sqrt(sum(v*v for v in b)); b=tuple(v/nb for v in b)
    c=(u[1]*b[2]-u[2]*b[1],u[2]*b[0]-u[0]*b[2],u[0]*b[1]-u[1]*b[0])
    pts=[]
    for i in range(3):
        for s in (-1,1): pts.append((s*b[i],s*c[i]))
    return hull_area(pts)


def main():
    rng=random.Random(76421)
    checks=0
    for d in (3,4,5,6,8,12,20,50,100,300):
        mu,z2,var=theoretical_moments(d)
        assert mu>0 and z2>mu*mu
        beta=mu*(d+2)*(d+4)*(d+6)/(12*d*(d+1)*(d+3))
        vh=mp.mpf(24)*(d-1)/((d+2)**2*(d+4)*(d+6))
        assert var-beta*beta*vh>mp.mpf('-1e-55')
        checks += 3
    for d in (80,160,320,640,1280):
        var=theoretical_moments(d)[2]
        scaled=d**3*var
        assert abs(scaled-1/(3*mp.pi)) < mp.mpf('0.012')
        checks+=1
    for _ in range(80):
        g=[rng.gauss(0,1) for _ in range(3)]
        norm=math.sqrt(sum(x*x for x in g)); u=tuple(x/norm for x in g)
        direct=direct_3d_shadow(u)
        signed=(2**2/math.factorial(2))*sign_expectation(u)
        assert abs(direct-signed)<3e-12, (direct,signed)
        checks+=1
    mu4,z4,v4=theoretical_moments(4)
    assert abs(mu4-8/(3*mp.pi))<mp.mpf('1e-65')
    assert abs(z4-(mp.mpf(5)/24+mp.sqrt(3)/(2*mp.pi)+3/(4*mp.pi)))<mp.mpf('1e-65')
    checks+=2
    print(f'PASS: {checks} checks. d=4 variance={float(v4):.12g}; d=1280 scaled variance={float(1280**3*theoretical_moments(1280)[2]):.12g}')


if __name__=='__main__':
    main()
