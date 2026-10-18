"""Independent finite consistency checks for the regular-line relaxed cyclic map.

Requires Python 3.9+ standard library. Run: python verify.py
The analytical proof, not this finite test, establishes the theorem.
"""
import math


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def scal(a, x):
    return [[x * a[i][j] for j in range(2)] for i in range(2)]


def identity():
    return [[1.0, 0.0], [0.0, 1.0]]


def projection(theta):
    c, s = math.cos(theta), math.sin(theta)
    return [[c*c, c*s], [c*s, s*s]]


def reflect(a):
    return matadd(scal(a, 2), scal(identity(), -1))


def pair(a, b, lam):
    pa, pb = projection(a), projection(b)
    return matadd(scal(matadd(matmul(reflect(pa), reflect(pb)), identity()), lam/2),
                  scal(pb, 1-lam))


def full(m, lam):
    res = identity()
    for j in range(m):
        res = matmul(res, pair(j * math.pi/m, (j+1)*math.pi/m, lam))
    return res


def power(a, n):
    x = identity()
    for j in range(n):
        x = matmul(x, a)
    return x


def formula(m, lam, k=1):
    t = math.pi/m
    a = (-math.cos(t)**m)**k
    return [[a, 0.0], [a * math.tan(t) * (1-lam**(m*k)), a*lam**(m*k)]]


def close(a, b, atol=2e-11):
    return all(abs(a[i][j]-b[i][j]) < atol for i in range(2) for j in range(2))


def two_norm(a):
    # Stable real 2-by-2 spectral norm: sum of two hypotenuses / two.
    x,y,z,w=a[0][0],a[0][1],a[1][0],a[1][1]
    return (math.hypot(x+w,z-y)+math.hypot(x-w,z+y))/2


def run():
    nchecks = 0
    for m in range(3, 31):
        c = math.cos(math.pi/m)**m
        for lam in (0.0, 0.1, 0.25, 0.5, 0.75, 0.99, 1.0):
            observed = full(m, lam)
            expected = formula(m, lam)
            assert close(observed, expected), (m, lam, observed, expected)
            nchecks += 4
            for k in (1, 2, 3, 5):
                assert close(power(observed, k), formula(m, lam, k)), (m, lam, k)
                nchecks += 4
                norm = two_norm(power(observed, k))
                base = c**k
                assert norm >= base-2e-11
                if lam == 1:
                    assert abs(norm-base)<2e-11, (m,k,norm,base)
                else:
                    assert norm > base, (m,lam,k,norm,base)
                nchecks += 2
    # Independent affine-offset check by evaluating real projectors and reflected points.
    def add(x,y):return [x[0]+y[0],x[1]+y[1]]
    def mul(v,t):return [v[0]*t,v[1]*t]
    def mp(M,v):return [M[0][0]*v[0]+M[0][1]*v[1],M[1][0]*v[0]+M[1][1]*v[1]]
    def point_proj(i,x,m):
        a = i * math.pi/m
        u=(math.cos(a), math.sin(a))
        offset = 0.1 * math.sin(3*i+1)
        normal=(-u[1],u[0]); residual=x[0]*normal[0]+x[1]*normal[1]-offset
        return [x[0]-residual*normal[0], x[1]-residual*normal[1]]
    def aff_pair(i,x,m,lam):
        p=point_proj((i+1)%m,x,m)
        reflected=add(mul(p,2),mul(x,-1))
        p2=point_proj(i,reflected,m)
        double_reflected=add(mul(p2,2),mul(reflected,-1))
        return add(mul(add(double_reflected,x),lam/2),mul(p,1-lam))
    def aff_full(x,m,lam):
        for i in reversed(range(m)):
            x=aff_pair(i,x,m,lam)
        return x
    for m in (3,4,5,8,11):
        for lam in (0.,.23,.61,1.):
            xx=(1.7,-.93); yy=(-1.1,2.5)
            dx=[xx[i]-yy[i] for i in range(2)]
            fx=aff_full(list(xx),m,lam); fy=aff_full(list(yy),m,lam)
            pred=mp(formula(m,lam),dx)
            assert max(abs(fx[i]-fy[i]-pred[i]) for i in range(2))<2e-11
            nchecks+=2
    print(f'PASS: {nchecks} finite independent matrix and affine checks')


if __name__=='__main__':
    run()
