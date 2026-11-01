"""Finite-dimensional numerical checks for a mortal-recruited Brownian first-arrival theorem.

Requires Python 3, NumPy, and SciPy. Checks supplement an analytical proof.
"""
import math
from scipy.integrate import quad
from scipy.special import erfc

CHECKS = 0


def check(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def free_density(t):
    return math.exp(-0.25 / t) / (2.0 * math.sqrt(math.pi) * t**1.5)


def kernel_fj(s, m):
    """Endpoint-integral representations of mortal hitting CDF and convolution."""
    w = 0.25 / s
    pref = math.exp(-w) / math.sqrt(math.pi)
    factor = lambda v: math.exp(-v - m / (4.0 * (w + v)))
    fv = quad(lambda v: factor(v) / math.sqrt(w + v), 0, 60,
              epsabs=5e-14, epsrel=5e-13)[0]
    jv = quad(lambda v: (v / (4.0 * w * (w + v))) *
              factor(v) / math.sqrt(w + v), 0, 60,
              epsabs=5e-14, epsrel=5e-13)[0]
    return pref * fv, pref * jv


def direct_fj(s, m):
    f = quad(lambda u: math.exp(-m*u)*free_density(u), 0, s,
             epsabs=1e-13, epsrel=1e-12)[0]
    j = quad(lambda u: (s-u)*math.exp(-m*u)*free_density(u), 0, s,
             epsabs=1e-13, epsrel=1e-12)[0]
    return f, j


def closed_f(s, m):
    a = 0.5 / math.sqrt(s)
    b = math.sqrt(m*s)
    return 0.5*(math.exp(-math.sqrt(m))*erfc(a-b) +
                math.exp(math.sqrt(m))*erfc(a+b))


def survival(s, log_rho, x):
    m = x*log_rho
    w=0.25/s
    jscaled=quad(lambda v: (v/(4.0*w*(w+v)))*
                  math.exp(-v-m/(4.0*(w+v)))/math.sqrt(math.pi*(w+v)),
                  0, 60, epsabs=5e-14, epsrel=5e-13)[0]
    f, _ = kernel_fj(s, m)
    h = math.exp(log_rho-w)*m*jscaled
    return (1.0-f)*math.exp(-h)


def gumbel_cdf(z, log_rho, x):
    L = log_rho
    c = L-1.5*math.log(L)+math.log(x/(4*math.sqrt(math.pi)))-x/4
    w = c+z
    return survival(0.25/w, L, x)


def mean_time(log_rho, x, alternative=False):
    m = log_rho*x
    rate = math.exp(log_rho)*m
    def integrand(s):
        if s == 0:
            return 1.0
        f, j = kernel_fj(s, m)
        e = math.exp(-rate*j)
        return e if alternative else (1-f)*e
    # The interval above 2 is far into the exponentially small tail
    # for these prescribed numerical test parameters.
    ans = quad(integrand, 0, 2.0, epsabs=2e-11,
               epsrel=2e-10, limit=120,
               points=[0.25/log_rho])[0]
    return ans - (1.0/rate if alternative else 0.0)


def mean_reciprocal(log_rho, x):
    """Independent reciprocal-time quadrature for the large-ratio mean."""
    L=log_rho
    c=L-1.5*math.log(L)+math.log(x/(4*math.sqrt(math.pi)))-x/4
    segments=sorted({L/2, max(L/2,c-8), c, min(3*L,c+8), 3*L})
    def fw(w):
        return survival(0.25/w,L,x)/(4*w*w)
    value=sum(quad(fw,a,b,epsabs=2e-13,epsrel=1e-12)[0]
              for a,b in zip(segments,segments[1:]))
    return value+1/(12*L)  # the omitted upper tail differs negligibly from its free value


def main():
    for m in [0.25, 1.0, 3.0, 7.0]:
        for s in [0.12, 0.25, 0.7]:
            f, j = kernel_fj(s, m)
            fd, jd = direct_fj(s, m)
            check(abs(f-fd)<2e-10, 'mortal hitting CDF mismatch')
            check(abs(j-jd)<2e-10, 'recruited convolution mismatch')
            check(abs(f-closed_f(s, m))<2e-10, 'erfc mismatch')
            check(j>0 and f>0 and j<s*f, 'kernel positivity')

    for m in [0.5, 2., 5.]:
        for s in [0.15, 0.4, 0.9]:
            step=1e-5*s
            _, jp=kernel_fj(s+step, m)
            _, jm=kernel_fj(s-step, m)
            f, _=kernel_fj(s,m)
            check(abs((jp-jm)/(2*step)-f)<1e-7,'J derivative must be F')

    for x in [1.,4.,8.]:
        for z in [-1.,0.,1.]:
            target=math.exp(-math.exp(-z))
            a=gumbel_cdf(z, 200., x)
            b=gumbel_cdf(z, 1000., x)
            check(abs(b-target)<abs(a-target), 'Gumbel convergence mismatch')
            check(abs(b-target)<0.012, 'Gumbel limiting value mismatch')
        for L in [12.,20.]:
            e=mean_time(L,x)
            ea=mean_time(L,x,True)
            check(abs(e-ea)<2e-8, 'exact mean identity mismatch')
            check(e>0 and math.isfinite(e),'mean must be finite positive')

    for L in [12., 20.]:
        e4=mean_time(L,4.)
        check(mean_time(L,1.)>e4, 'x=1 mean comparison')
        check(mean_time(L,8.)>e4, 'x=8 mean comparison')

    limiting=lambda x:x/4-1-math.log(x/4)
    for x in [1.,2.,8.]:
        m80=[mean_reciprocal(80.,y) for y in [x,4.]]
        m200=[mean_reciprocal(200.,y) for y in [x,4.]]
        d80=4*80**2*(m80[0]-m80[1])
        d200=4*200**2*(m200[0]-m200[1])
        check(abs(d200-limiting(x))<abs(d80-limiting(x)),
              'second-order mean excess convergence')
        check(abs(d200-limiting(x))<0.09,
              'second-order mean excess limiting value')

    print('PASS:',CHECKS,'deterministic numerical assertions')


if __name__=='__main__':
    main()
