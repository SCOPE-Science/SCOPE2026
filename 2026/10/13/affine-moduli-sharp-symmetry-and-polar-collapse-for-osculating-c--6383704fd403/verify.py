"""Exact finite-field and coefficient checks for osculating-conic moduli."""
from itertools import combinations, product
from math import comb


def phi(d):
    return sum(1 for i in range(1, d + 1) if gcd(i, d) == 1)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def coeff(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def orbit_count_formula(q, p, m):
    total = coeff(q, m)
    if m % p == 0:
        total += (q - 1) * coeff(q // p, m // p)
    for d in divisors(q - 1):
        if d == 1:
            continue
        c = (coeff((q - 1) // d, m // d) if m % d == 0 else 0)
        c += (coeff((q - 1) // d, (m - 1) // d) if (m - 1) % d == 0 else 0)
        total += q * phi(d) * c
    assert total % (q * (q - 1)) == 0
    return total // (q * (q - 1))


def orbit_count_prime(p, m):
    allsets = {tuple(c) for c in combinations(range(p), m)}
    orbits = 0
    while allsets:
        sample = allsets.pop()
        orbit = {tuple(sorted((a * t + b) % p for t in sample))
                 for a in range(1, p) for b in range(p)}
        allsets.difference_update(orbit)
        orbits += 1
    return orbits


def mult4(a, b):
    out = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                out ^= (1 << (i + j))
    if out & 8:
        out ^= 0b1110
    if out & 4:
        out ^= 0b111
    return out


def inverse4(a):
    return next(x for x in range(1, 4) if mult4(a, x) == 1)


def orbit_count_four(m):
    allsets = {tuple(c) for c in combinations(range(4), m)}
    out = 0
    while allsets:
        S = allsets.pop()
        images = {tuple(sorted(mult4(a, t) ^ b for t in S))
                  for a in range(1, 4) for b in range(4)}
        allsets.difference_update(images)
        out += 1
    return out


def polyprod(u, v, p):
    # Coefficients of xx, yy, zz, xy, xz, yz.
    return (u[0]*v[0]%p, u[1]*v[1]%p, u[2]*v[2]%p,
            (u[0]*v[1]+u[1]*v[0])%p,
            (u[0]*v[2]+u[2]*v[0])%p,
            (u[1]*v[2]+u[2]*v[1])%p)


def qcompose(M, t, p):
    xx = polyprod(M[2], M[2], p)
    xy = polyprod(M[0], M[1], p)
    xz = polyprod(M[0], M[2], p)
    return tuple((xx[i]-xy[i]+t*xz[i])%p for i in range(6))


def qcoeff(t, p):
    return (0, 0, 1, (-1)%p, t%p, 0)


def det3(M, p):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%p


def pgl_stabilizers_three():
    p=3
    allmat=set()
    for digits in product(range(p), repeat=9):
        M=(digits[:3],digits[3:6],digits[6:])
        if det3(M,p) == 0:
            continue
        leading=next(x for x in digits if x)
        inv=pow(leading,-1,p)
        canonical=tuple(x*inv%p for x in digits)
        allmat.add(canonical)
    assert len(allmat)==5616
    count=0
    for coords in allmat:
        M=(coords[:3],coords[3:6],coords[6:])
        outputs=set()
        for t in range(p):
            out=qcompose(M,t,p)
            matches=[s for s in range(p)
                     if any(all(out[j]==k*qcoeff(s,p)[j]%p for j in range(6))
                            for k in (1,2))]
            if len(matches)!=1:
                break
            outputs.add(matches[0])
        else:
            if len(outputs)==p:
                count+=1
    assert count==6,(count,)


def verify_affine_lifts():
    for p, alphas, betas, parameters in [
        (3, range(1,3), range(3), range(3)),
        (5, range(1,5), range(5), range(5)),
        (7, range(1,7), range(7), range(7))]:
        for a in alphas:
            inv=pow(a,-1,p)
            for b in betas:
                M=((inv,0,0),(0,a,b),(0,0,1))
                for t in parameters:
                    # The equation q_(a*t+b) after T equals q_t.
                    assert qcompose(M,(a*t+b)%p,p)==qcoeff(t,p)




def pol_add(A, B, p, sign=1):
    out=dict(A)
    for mon, val in B.items():
        out[mon]=(out.get(mon,0)+sign*val)%p
        if not out[mon]: del out[mon]
    return out


def pol_mul(A, B, p):
    out={}
    for a, av in A.items():
        for b,bv in B.items():
            mon=tuple(a[i]+b[i] for i in range(3))
            out[mon]=(out.get(mon,0)+av*bv)%p
            if not out[mon]:del out[mon]
    return out


def pol_pow(A, n, p):
    out={(0,0,0):1}
    while n:
        if n&1:out=pol_mul(out,A,p)
        A=pol_mul(A,A,p)
        n//=2
    return out


def pol_der(A, var, p):
    out={}
    for mon,c in A.items():
        if mon[var]:
            j=list(mon);j[var]-=1
            val=c*mon[var]%p
            if val:out[tuple(j)]=val
    return out


def verify_frobenius_gradient():
    for p in (3,5,7):
        X={(1,0,0):1};Y={(0,1,0):1};Z={(0,0,1):1}
        f=pol_mul(X,Z,p)
        g=pol_add(pol_pow(Z,2,p),pol_mul(X,Y,p),p,-1)
        prod={(0,0,0):1}
        for t in range(p):
            prod=pol_mul(prod,pol_add(g,{mon:t*coef%p for mon,coef in f.items()},p),p)
        expected=pol_add(pol_pow(g,p,p),pol_mul(pol_pow(f,p-1,p),g,p),p,-1)
        assert prod==expected,('Frobenius factorization',p)
        gradient_base=[pol_pow(Z,3,p),pol_mul(pol_pow(X,2,p),Z,p),pol_add({},pol_add(pol_mul(pol_pow(X,2,p),Y,p),pol_mul(X,pol_pow(Z,2,p),p),p),p,-1)]
        for j in range(3):
            assert pol_der(prod,j,p)==pol_mul(pol_pow(f,p-2,p),gradient_base[j],p),('gradient',p,j)

if __name__=='__main__':
    verify_affine_lifts()
    verify_frobenius_gradient()
    pgl_stabilizers_three()
    for p in (3,5,7,11,13):
        for m in range(3,p+1):
            assert orbit_count_formula(p,p,m)==orbit_count_prime(p,m),(p,m)
    assert orbit_count_formula(4,2,3)==orbit_count_four(3)==1
    assert orbit_count_formula(4,2,4)==orbit_count_four(4)==1
    for q,p in [(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(16,2)]:
        assert orbit_count_formula(q,p,q)==1
    print('VERIFY_OK: affine lifts; full PGL3(F3) stabilizer; Burnside formula for F3,F4,F5,F7,F11,F13 and prime powers; Frobenius product and gradient')
