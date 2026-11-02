"""Exact finite-field checks for singular Hurwitz plane curves.

Runs with Python 3 and its standard library. The general theorem follows from
an exact torus equation and a local formal-power-series proof, not from these
finite tests.
"""


def valuation(x, p):
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e, x


def local_coefficients(n, p):
    """First three coefficients of (-1)^(n+1)*t^n/(1-t) at t=1-n."""
    t = (1 - n) % p
    a = (1 - t) % p
    assert a != 0
    sign = (-1) ** (n + 1)
    iv = pow(a, -1, p)
    c0 = sign * pow(t, n, p) * iv
    c1 = sign * (n * pow(t, n - 1, p) * iv + pow(t, n, p) * iv**2)
    c2 = sign * (
        (n * (n - 1) // 2) * pow(t, n - 2, p) * iv
        + n * pow(t, n - 1, p) * iv**2
        + pow(t, n, p) * iv**3
    )
    return c0 % p, c1 % p, c2 % p


def count_prime_plane(n, p):
    return 2 + sum(
        (pow(x, n, p) * y + pow(y, n, p) + x) % p == 0
        for x in range(p) for y in range(p)
    )


def count_prime_kummer(n, p, M):
    sign = (-1) ** (n + 1)
    return 3 + sum(
        pow(w, M, p) == (sign * pow(t, n, p) * pow(1-t, -1, p)) % p
        for t in range(2, p) for w in range(p)
    )


def quadratic_extension(p):
    squares = {a * a % p for a in range(p)}
    d = next(a for a in range(2, p) if a not in squares)
    elts = [(a, b) for a in range(p) for b in range(p)]
    zero, one = (0, 0), (1, 0)
    def add(u, v):
        return ((u[0]+v[0])%p, (u[1]+v[1])%p)
    def mul(u, v):
        return ((u[0]*v[0]+d*u[1]*v[1])%p,
                (u[0]*v[1]+u[1]*v[0])%p)
    def power(u, e):
        assert e >= 0
        r = one
        while e:
            if e & 1: r=mul(r,u)
            u=mul(u,u); e//=2
        return r
    def inv(u):
        assert u != zero
        return power(u, p*p-2)
    def sub(u,v):
        return ((u[0]-v[0])%p,(u[1]-v[1])%p)
    return elts,zero,one,add,mul,power,inv,sub


def count_quadratic(n,p,M):
    elts,z,o,add,mul,power,inv,sub = quadratic_extension(p)
    sign = o if n % 2 == 1 else (p-1,0)
    plane = 2 + sum(
        add(add(mul(power(x,n),y),power(y,n)),x)==z
        for x in elts for y in elts)
    kummer = 3 + sum(
        power(w,M)==mul(mul(sign,power(t,n)),inv(sub(o,t)))
        for t in elts if t!=z and t!=o for w in elts)
    return plane,kummer


def main():
    # Mix of cusp exponents and nontrivial tame residual genera.
    tests = [(2,3),(3,7),(4,13),(5,3),(5,7),(6,31),
             (8,3),(8,19),(19,7),(31,7)]
    print('CASE n p v_p(N) M predicted_cusps normalized_genus plane_Fp tame_Fp')
    for n,p in tests:
        N=n*n-n+1
        e,M=valuation(N,p)
        assert e>=1 and M%p!=0 and M%2==1
        assert n%p not in (0,1)
        c0,c1,c2=local_coefficients(n,p)
        assert c0!=0 and c1==0 and c2!=0
        assert pow(c0,p**e,p)==c0
        num1=count_prime_plane(n,p)
        num2=count_prime_kummer(n,p,M)
        assert num1==num2,(n,p,num1,num2)
        assert (N-1)//2-M*(p**e-1)//2 == (M-1)//2
        print(n,p,e,M,M,(M-1)//2,num1,num2)
    print('LOCAL_TAYLOR_SIMPLE_CRITICAL_POINT=PASS')
    print('GENUS_DELTA_IDENTITY=PASS')
    for n,p in [(5,3),(5,7),(19,7)]:
        N=n*n-n+1; e,M=valuation(N,p)
        a,b=count_quadratic(n,p,M)
        assert a==b,(n,p,a,b)
        print('F_%d^2 n=%d plane=%d tame_normalization=%d'%(p,n,a,b))
        if M==1: assert a==p*p+1
    print('FINITE_FIELD_POINT_COUNTS=PASS')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
