import math
import mpmath as mp
mp.mp.dps = 40

def g_closed(r):
    return (2/mp.pi)*(mp.sqrt(1-r*r)+r*mp.asin(r))

def g_quad(r):
    # E|X||Y| via conditioning Y=rX+sZ and one-dimensional folded-normal mean.
    s=mp.sqrt(1-r*r)
    phi=lambda x: mp.e**(-x*x/2)/mp.sqrt(2*mp.pi)
    def folded_mean(m):
        if s == 0:
            return abs(m)
        return s*mp.sqrt(2/mp.pi)*mp.e**(-m*m/(2*s*s)) + m*(2*(0.5*(1+mp.erf(m/(s*mp.sqrt(2)))))-1)
    f=lambda x: abs(x)*folded_mean(r*x)*phi(x)
    return mp.quad(f, [-mp.inf,0,mp.inf])

def corr2(n):
    d=n-1
    den=(n-1)*(mp.pi+2*mp.sqrt(n*(n-2))+2*mp.asin(mp.mpf(1)/(n-1))-2*n)
    return mp.mpf(n)/den

def run():
    quad_checks=0
    for r in [-0.8,-0.5,-0.2,0,0.3,0.7]:
        assert abs(g_quad(mp.mpf(r))-g_closed(mp.mpf(r))) < mp.mpf("1e-25")
        quad_checks += 1

    chi_checks=0
    for d in [1,2,3,7,20]:
        for p in [0,1,2,3,5]:
            # chi moment ratio E Q^(p+2)/E Q^p = d+p
            m=lambda a: (2**(mp.mpf(a)/2))*mp.gamma((d+a)/2)/mp.gamma(mp.mpf(d)/2)
            assert abs(m(p+2)/m(p)-(d+p)) < mp.mpf("1e-30")
            chi_checks += 1

    formula_checks=0
    for n in range(2,5001):
        d=n-1
        rho=-mp.mpf(1)/d
        q=g_closed(rho)
        B=(1+d*q)/n-2/mp.pi
        assert B > 0
        c2=1/(mp.pi*d*B)
        assert abs(c2-corr2(n)) < mp.mpf("1e-25")
        assert 0 < c2 < 1
        formula_checks += 3

    target=1/(mp.pi-2)
    assert abs(corr2(2)-target) < mp.mpf("1e-30")
    assert abs(corr2(100000)-target) < mp.mpf("2e-5")
    print("VERIFY_OK")
    print(f"absolute_gaussian_quadrature_checks={quad_checks}")
    print(f"chi_moment_checks={chi_checks}")
    print(f"finite_formula_checks={formula_checks}")
    print("max_formula_n=5000")

if __name__=="__main__":
    run()
