"""Independent finite diagnostics for unequal-order tangential regular polygons.
Run: python3 verify.py  (Python standard library only).
Finite tests do not replace the analytic universal proof.
"""
import math

TAU = 2*math.pi


def parameters(n, m):
    assert 3 <= n < m
    d = math.gcd(n, m)
    return d, n//d, TAU*d/(n*m), TAU/m


def exact_energy(n, m, t, f):
    d, q, h, beta = parameters(n, m)
    assert 0 <= t <= h+1e-14
    return (m-n)*f(beta)+d*sum(
        f(k*h-t)+f((q-k)*h+t) for k in range(1,q+1))


def direct_energy(n, m, t, f):
    d, q, h, beta = parameters(n,m)
    # Offset theta=-t modulo the fundamental phase h.
    angles = sorted(([(j*TAU/m)%TAU for j in range(m)]
        + [((i*TAU/n-t)%TAU) for i in range(n)]))
    differences = [angles[i+1]-angles[i] for i in range(len(angles)-1)]
    differences.append(TAU+angles[0]-angles[-1])
    # Coincident normals give zero angular gaps; f(0)=0.
    return sum(f(max(0,x)) for x in differences)


def polygon(n, radius=1, orientation=0):
    h=TAU/n
    # Every side tangent to the unit disk, outward normals h*j+orientation.
    r=radius/math.cos(h/2)
    return [(r*math.cos(orientation+(j+.5)*h),
             r*math.sin(orientation+(j+.5)*h)) for j in range(n)]


def clip_polygon(poly, normal, radius=1):
    nx,ny=normal
    def projection(v): return v[0]*nx+v[1]*ny-radius
    result=[]
    for a,b in zip(poly, poly[1:]+poly[:1]):
        da, db = projection(a),projection(b)
        ia,ib = da<=1e-13, db<=1e-13
        if ia != ib:
            z=da/(da-db)
            result.append((a[0]+z*(b[0]-a[0]),a[1]+z*(b[1]-a[1])))
        if ib: result.append(b)
    return result


def clip_area(n,m,t):
    p=polygon(m)
    for j in range(n):
        angle=j*TAU/n-t
        p=clip_polygon(p,(math.cos(angle),math.sin(angle)))
    return abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in zip(p,p[1:]+p[:1]))/2)


def area(n,m,t): return exact_energy(n,m,t,lambda g:math.tan(g/2))


def mean_exact(n,m):
    return (m-n)*math.tan(math.pi/m) - 2*n*m/math.pi*math.log(math.cos(math.pi/m))


def area_max_min(n,m):
    d,q,h,b=parameters(n,m)
    hi=(m-n+d)*math.tan(b/2)+2*d*sum(math.tan(k*h/2) for k in range(1,q))
    lo=(m-n)*math.tan(b/2)+2*d*sum(math.tan((k+.5)*h/2) for k in range(q))
    return hi,lo


def simpson(f, a, b, N=1200):
    assert N % 2 == 0
    z=(f(a)+f(b))
    h=(b-a)/N
    for k in range(1,N): z+=(4 if k%2 else 2)*f(a+k*h)
    return z*h/3


def main():
    tests=0
    for n in range(3,17):
        for m in range(n+1,22):
            d,q,h,b=parameters(n,m)
            fns=[lambda x:x*x, lambda x:x**3, lambda x:math.expm1(x), lambda x:math.tan(x/2)]
            for fraction in [.00001,.07,.21,.5,.81,.94,.99999]:
                t=h*fraction
                for f in fns:
                    rhs=exact_energy(n,m,t,f)
                    lhs=direct_energy(n,m,t,f)
                    assert abs(rhs-lhs)<3e-10*(1+abs(rhs)), (n,m,t,lhs,rhs)
                    tests+=1
                if m < 15:
                    rhs=area(n,m,t)
                    lhs=clip_area(n,m,t)
                    assert abs(rhs-lhs)<2e-10*(1+rhs), (n,m,t,lhs,rhs)
                    tests+=1
            amax,amin=area_max_min(n,m)
            assert abs(amax-area(n,m,0))<1e-11
            assert abs(amin-area(n,m,h/2))<1e-11
            assert amin < amax
            for frac in [.05,.19,.4]:
                assert amin < area(n,m,h*frac) < amax
            ave=simpson(lambda t:area(n,m,t),0,h)/h
            assert abs(ave-mean_exact(n,m))<2e-11*(1+ave),(n,m,ave,mean_exact(n,m))
            tests+=5
    # Independent high-order limit checks at fixed sparse n and differing gcd patterns.
    for n,m in [(3,300),(4,301),(6,303),(8,304),(9,306)]:
        d,q,h,b=parameters(n,m)
        amax,amin=area_max_min(n,m)
        leading=math.pi**3*d*d/(4*n*m**3)
        ratio=(amax-amin)/leading
        assert abs(ratio-1)<0.002,(n,m,ratio)
        tests+=1
    print('VERIFY_OK',tests,'finite_energy_clip_mean_and_asymptotic_checks')

if __name__=='__main__': main()
