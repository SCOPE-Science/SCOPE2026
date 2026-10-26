"""Direct numerical consistency checks for the free fractional-Gaussian crossover.

Requires mpmath>=1.3.0.  The analytic proof, not these finite tests,
justifies the asymptotic theorem.
"""
import mpmath as mp

mp.mp.dps = 55
I = mp.j
PI = mp.pi
RT = mp.sqrt(2 / PI)
INTERVALS = [mp.mpf(v) for v in
             (0, '0.125', '0.25', '0.5', 1, '1.5', 2, '2.5', 3,
              '3.5', 4, 5, 6, 7, 8, 10, 12, 14)]
assertions = 0


def verify(test, explanation):
    global assertions
    assertions += 1
    if not test:
        raise AssertionError(explanation)


def gaussian(t, x):
    a = 1 + I * t
    return mp.exp(-x*x/(4*a))/mp.sqrt(2*a)


def gaussian_quad(t, x):
    f = lambda p: mp.cos(x*p)*mp.exp(-(1 + I*t)*p*p)
    return RT*mp.quad(f, INTERVALS)


def difference(alpha, t, x):
    # Directly integrate the difference of the propagators; subtraction in
    # position space would lose precision when alpha approaches two.
    f = lambda p: (mp.cos(x*p)*mp.exp(-(1 + I*t)*p*p)
                   * mp.expm1(-I*t*(p**alpha-p*p)))
    return RT*mp.quad(f, INTERVALS)


def index_derivative(t, x):
    # d/d(2-alpha) of the solution, evaluated at alpha=2.
    def f(p):
        if p == 0:
            return 0
        return I*t*mp.cos(x*p)*p*p*mp.log(p)*mp.exp(-(1+I*t)*p*p)
    return RT*mp.quad(f, INTERVALS)


def crossover(epsilon, t, s=0):
    L = mp.log(1/epsilon)
    const = mp.log(4*(1+t*t)**(mp.mpf(5)/4)/(mp.sqrt(PI)*t))
    y = mp.findroot(lambda z: z - mp.mpf('1.5')*mp.log(z)-L-const-s,
                    (L+2, L+20))
    x = 2*mp.sqrt((1+t*t)*y)
    return y, x


for time in (mp.mpf('0.5'), mp.mpf('1.2')):
    for pos in (mp.mpf(0), mp.mpf(4), mp.mpf(8)):
        exact = gaussian(time, pos)
        numerical = gaussian_quad(time, pos)
        verify(abs(numerical-exact) < mp.mpf('1e-35'), 'Gaussian Fourier transform')
        verify(abs(gaussian(time, -pos)-exact) < mp.mpf('1e-35'), 'even spatial profile')

for time in (mp.mpf('0.5'), mp.mpf('1.2')):
    for pos in (mp.mpf(6), mp.mpf(9)):
        e = mp.mpf('0.0001')
        first = index_derivative(time, pos)
        d = difference(2-e, time, pos)
        verify(abs(d/e-first) < mp.mpf('0.006')*abs(first), 'first-order order derivative')

for time in (mp.mpf('0.5'), mp.mpf('1.2')):
    errors = []
    for epsilon in map(mp.mpf, ('0.001', '0.00001', '0.0000001')):
        y, x = crossover(epsilon, time)
        L = mp.log(1/epsilon)
        c = mp.log(4*(1+time*time)**(mp.mpf(5)/4)/(mp.sqrt(PI)*time))
        verify(abs(y-mp.mpf('1.5')*mp.log(y)-L-c)<mp.mpf('1e-45'),
               'implicit crossover center')
        observed = difference(2-epsilon, time, x)/gaussian(time, x)
        predicted = mp.exp(I*(PI/2+mp.atan(time)/2-time*y))
        errors.append(abs(observed-predicted))
        verify(abs(observed) > mp.mpf('.8'), 'leading crossover amplitude is nonzero')
    verify(errors[0]>errors[1]>errors[2], 'matched-asymptotic errors decrease')
    verify(errors[2] < mp.mpf('0.15'), 'fine-scale interference prediction')

# Check the nonstandard logarithmic Fourier coefficient driving the halo.
for time in (mp.mpf('0.5'), mp.mpf('1.2')):
    for pos in (mp.mpf(20), mp.mpf(30)):
        lead = I*time*mp.sqrt(2*PI)*pos**(-3)
        verify(abs(index_derivative(time, pos)/lead-1)<mp.mpf('0.06'),
               'Fourier transform of p^2 log(p) has the predicted coefficient')

# Check the coefficient of the algebraic wing at one fixed nonintegral index.
alpha = mp.mpf('1.6')
time = mp.mpf('0.8')
coef = I*time*RT*mp.gamma(1+alpha)*mp.sin(PI*alpha/2)
for pos in (mp.mpf(35), mp.mpf(45)):
    observed = gaussian(time, pos)+difference(alpha, time, pos)
    asymptotic = coef*pos**(-1-alpha)
    verify(abs(observed/asymptotic-1)<mp.mpf('0.10'), 'fractional far-field coefficient')

print('PASS:', assertions, 'direct numerical consistency assertions')
