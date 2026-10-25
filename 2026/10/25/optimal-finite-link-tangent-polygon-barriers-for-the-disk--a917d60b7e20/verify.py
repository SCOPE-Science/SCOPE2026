"""Reproduce the exact finite-link tangential disk-chain formula (no external packages)."""
from math import pi, atan, tan, cos, sin, hypot, sqrt, isclose


def parameters(k):
    assert isinstance(k, int) and k >= 2
    q = k-1
    def residual(b):
        return 2*atan(sqrt(1+2*tan(b)**2))+q*b-pi
    lo, hi = 0.0, pi/2
    for _ in range(90):
        mid = (lo+hi)/2
        if residual(mid) > 0:
            hi = mid
        else:
            lo = mid
    b = (lo+hi)/2
    a = (pi-q*b)/2
    return a,b


def formula(k):
    a,b = parameters(k)
    return 2*tan(a)+2*(k-1)*tan(b)


def vertex_intersections(k):
    a,b=parameters(k)
    x=[a]+[b]*(k-1)+[a]
    normals=[]
    angle=0.0
    for i in range(len(x)):
        normals.append((cos(angle),sin(angle)))
        if i+1 < len(x):
            angle+=2*x[i+1]
    assert abs(angle+2*x[0]-2*pi)<5e-13
    v=[]
    for i in range(len(x)):
        p=normals[i-1]
        n=normals[i]
        det=p[0]*n[1]-p[1]*n[0]
        vx=(n[1]-p[1])/det
        vy=(p[0]-n[0])/det
        v.append((vx,vy))
        assert abs(vx*n[0]+vy*n[1]-1)<2e-12
        assert abs(vx*p[0]+vy*p[1]-1)<2e-12
    length=sum(hypot(v[i+1][0]-v[i][0],v[i+1][1]-v[i][1])
               for i in range(k))
    # Unit disk is the intersection of the tangent supporting half-planes;
    # verify that every tangency point satisfies all other supporting constraints.
    for ni in normals:
        for nj in normals:
            assert ni[0]*nj[0]+ni[1]*nj[1] <= 1+2e-13
    return length


if __name__ == '__main__':
    k2_exact=(1+sqrt(5))*sqrt(2+sqrt(5))
    k3_exact=4*sqrt(2)
    assert isclose(formula(2), k2_exact, rel_tol=1e-13)
    assert isclose(formula(3), k3_exact, rel_tol=1e-13)
    previous=1e9
    for k in [2,3,4,5,6,8,12,20,50,100,300]:
        a,b=parameters(k)
        length=formula(k)
        polyline_length=vertex_intersections(k)
        assert isclose(length,polyline_length,abs_tol=1e-10,rel_tol=1e-12)
        assert isclose(2*a+(k-1)*b,pi,abs_tol=1e-13)
        assert isclose(1+tan(a)**2,2*(1+tan(b)**2),rel_tol=1e-12)
        assert length < previous
        assert length > pi+2
        previous=length
        err=(k-1)**2*(length-pi-2)
        print(f'k={k:3d}, length={length:.12f}, scaled_excess={err:.9f}')
    assert abs((299)**2*(formula(300)-pi-2)-pi**3/12)<0.0005
    print('PASS finite examples, tangent geometry, strict decrease in samples, sharp rate')
