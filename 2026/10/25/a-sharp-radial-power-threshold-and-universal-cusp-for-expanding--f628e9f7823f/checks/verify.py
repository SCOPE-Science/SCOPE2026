"""Independent numerical checks for a sharp radial-weighted sphere perimeter theorem.

Requires mpmath. All numerical tests are supplementary to the written proof.
"""
import mpmath as mp

mp.mp.dps = 65


def normalized_spherical_mean(n, p, a, r):
    """Angular quadrature, not based on hypergeometric evaluation."""
    c = mp.gamma(mp.mpf(n)/2)/(mp.sqrt(mp.pi)*mp.gamma(mp.mpf(n-1)/2))
    # Each half interval is integrated separately; endpoints are integrable.
    def integrand(theta):
        dist2 = (r-a)**2 + 4*a*r*mp.sin(theta/2)**2
        return (dist2**(p/2))*mp.sin(theta)**(n-2)
    return c*mp.quad(integrand, [0,mp.pi/16,mp.pi/4,mp.pi/2,mp.pi])


def normalized_perimeter_hypergeom(n,p,a,r):
    """Closed spherical potential, for cross-checks and cusp extraction."""
    rho=a/r
    A=-p/2; B=1-(n+p)/2; C=mp.mpf(n)/2
    if rho<=1:
        return r**(n-1+p)*mp.hyp2f1(A,B,C,rho**2)
    return r**(n-1+p)*rho**p*mp.hyp2f1(A,B,C,rho**(-2))


checks=0
# Compare independently integrated sphere data to the known closed kernel.
for n,p in [(2,mp.mpf('-.5')),(3,mp.mpf('-1.5')),
            (4,mp.mpf('-2.5')),(5,mp.mpf('-3.4')),
            (3,mp.mpf('-.5')),(4,mp.mpf('-1.5'))]:
    a=mp.mpf('1.3')
    for r in [mp.mpf('.67'),mp.mpf('1.13'),mp.mpf('1.3'),mp.mpf('1.7'),mp.mpf('3.1')]:
        # The normalized perimeter uses r^(n-1) times the angular average.
        actual=r**(n-1)*normalized_spherical_mean(n,p,a,r)
        predicted=normalized_perimeter_hypergeom(n,p,a,r)
        assert mp.almosteq(actual,predicted,rel_eps=mp.mpf('1e-25')), (n,p,a,r,actual,predicted)
        checks+=1
# Critical Newtonian power (outside/inside) and subcritical cusp coefficient.
for n in [3,4,5,6]:
    a=mp.mpf('1.3');p=mp.mpf(2-n)
    for r in [mp.mpf('.5'),a,mp.mpf('2.0')]:
        predicted=r**(n-1)*a**(2-n) if r<=a else r
        actual=normalized_perimeter_hypergeom(n,p,a,r)
        assert mp.almosteq(actual,predicted,rel_eps=mp.mpf('1e-40'))
        checks+=1
for n,p in [(2,mp.mpf('-.5')),(3,mp.mpf('-1.5')),
            (4,mp.mpf('-2.5')),(5,mp.mpf('-3.4'))]:
    a=mp.mpf('1.3');q=n-1+p
    coeff=mp.gamma(mp.mpf(n)/2)*mp.gamma(1-q/2)/(mp.sqrt(mp.pi)*q*mp.gamma(-p/2))
    at=normalized_perimeter_hypergeom(n,p,a,a)
    for h in [mp.mpf('1e-9'),mp.mpf('1e-11')]:
        for sign in [-1,1]:
            actual=(at-normalized_perimeter_hypergeom(n,p,a,a+sign*h))/h**q
            # relative deviation is O(h^(1-q)).
            assert abs(actual/coeff-1)<mp.mpf('.004'),(n,p,h,sign,actual,coeff)
            checks+=1
    assert normalized_perimeter_hypergeom(n,p,a,a-mp.mpf('1e-4'))<at
    assert normalized_perimeter_hypergeom(n,p,a,a+mp.mpf('1e-4'))<at
    checks+=2
for n,p in [(2,mp.mpf('0')),(3,mp.mpf('-.5')),(4,mp.mpf('-1.5')),
            (5,mp.mpf('-2.4')),(6,mp.mpf('1.5'))]:
    a=mp.mpf('1.3')
    radii=[mp.mpf(z) for z in ['.3','.7','1.05','1.27','1.3','1.4','1.8','2.5','4.0']]
    v=[normalized_perimeter_hypergeom(n,p,a,r) for r in radii]
    assert all(x<y for x,y in zip(v,v[1:])),(n,p,v)
    checks+=1
print('WEIGHTED_SPHERE_OK numerical_cases=',checks)
