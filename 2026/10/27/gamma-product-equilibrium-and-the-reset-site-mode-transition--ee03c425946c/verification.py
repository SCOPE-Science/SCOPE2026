"""Numerical cross-checks for the radial diffusion/resetting theorem.

Dependencies: Python 3, mpmath 1.3 or later. All mathematical claims
are proved analytically in RESULT.md; these tests are diagnostics.
"""
import math
import mpmath as mp

mp.mp.dps = 35


def k_density(u, a):
    return 2 * u**((a-1)/2) * mp.besselk(a-1, 2*mp.sqrt(u)) / mp.gamma(a)


def spatial_density(radius, dim, alpha, diffusivity, reset_rate):
    n = alpha + 2
    a = (dim+alpha)/n
    u = reset_rate*radius**n/(diffusivity*n**2)
    omega = 2*mp.pi**(dim/2)/mp.gamma(dim/2)
    return reset_rate*radius**(n-dim)*k_density(u,a)/(diffusivity*n*omega)


def conditional_radial_density(radius, t, dim, alpha, diffusivity):
    n=alpha+2
    a=(dim+alpha)/n
    y=radius**n/(diffusivity*n**2)
    return n*y**a*mp.exp(-y/t)/(radius*mp.gamma(a)*t**a)


def check():
    total=0
    for dim,alpha in [(3,.4),(3,1),(3,2.5),(4,1.5),(4,2),(4,4),(6,2),(6,4),(6,7)]:
        d=mp.mpf(dim); al=mp.mpf(str(alpha)); kap=mp.mpf('1.7'); lam=mp.mpf('1.3')
        n=al+2; a=(d+al)/n; nu=(d-2)/n
        # Exact first and second Mellin moments of the gamma product,
        # independently integrated against its Bessel-K density.
        for s in [mp.mpf('.3'), mp.mpf('1')]:
            observed=mp.quad(lambda u: u**s*k_density(u,a), [0, 1, mp.inf])
            predicted=mp.gamma(a+s)*mp.gamma(1+s)/mp.gamma(a)
            assert mp.almosteq(observed,predicted,rel_eps=mp.mpf('2e-16'))
            total+=1
        # Numerical stationary mixture of the free radial heat kernel.
        for radius in [mp.mpf('.6'),mp.mpf('1.5')]:
            via_age=mp.quad(lambda t:lam*mp.exp(-lam*t)*conditional_radial_density(radius,t,d,al,kap),[0,1,mp.inf])
            omega=2*mp.pi**(d/2)/mp.gamma(d/2)
            via_bessel=omega*radius**(d-1)*spatial_density(radius,d,al,kap,lam)
            assert mp.almosteq(via_age,via_bessel,rel_eps=mp.mpf('1e-13'))
            total+=1
        # Universal origin exponent/amplitude and phase of the reset-site density.
        r=mp.mpf('1e-7')
        pref=lam/(kap*(d-2)*(2*mp.pi**(d/2)/mp.gamma(d/2)))
        ratio=spatial_density(r,d,al,kap,lam)/(pref*r**(al+2-d))
        assert abs(ratio-1)<mp.mpf('2e-4')
        total+=1
        # Verify the off-origin peak criterion using analytic sign of derivative.
        def slope(z):
            return (al+2-d)-(n/2)*z*mp.besselk(nu-1,z)/mp.besselk(nu,z)
        if al<=d-2:
            for z in [mp.mpf('0.001'),mp.mpf('.1'),mp.mpf('1'),mp.mpf('3')]:
                assert slope(z)<0
                total+=1
        else:
            assert slope(mp.mpf('1e-8'))>0 and slope(mp.mpf('100'))<0
            total+=2
            peak=mp.findroot(slope,(mp.mpf('0.2'),mp.mpf('3')))
            assert peak>0 and abs(slope(peak))<mp.mpf('1e-25')
            total+=1
    print(f'PASS {total} quadrature, asymptotic, and derivative-sign checks')


if __name__=='__main__':
    check()
