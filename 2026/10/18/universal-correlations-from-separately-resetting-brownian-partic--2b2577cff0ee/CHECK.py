"""Reproduce integral and finite-state checks for common-intensity Brownian resetting."""
from fractions import Fraction as Q
import mpmath as mp

mp.mp.dps = 45
count = 0


def check(predicate, note):
    global count
    assert predicate, note
    count += 1


def close(x, y, tol='1e-27'):
    return abs(mp.mpf(x) - mp.mpf(y)) <= mp.mpf(tol) * max(1, abs(mp.mpf(y)))


def formulas(nu, rates, probs, D=mp.mpf(1)):
    a = sum(p / (r + nu) for r, p in zip(rates, probs))
    b = sum(p / (2 * r + nu) for r, p in zip(rates, probs))
    a2 = sum(p / (r + nu)**2 for r, p in zip(rates, probs))
    c = sum(p / ((r + nu) * (2 * r + nu)) for r, p in zip(rates, probs))
    s, t = 1 - nu * a, 1 - nu * b
    M = 2 * D * a / s
    P = 8 * D * D * c / (s * t)
    H = 24 * D * D * a2 / s**2
    rho = (P - M * M) / (H - M * M)
    return M, P, H, rho, (a, b, a2, c)


# Independent direct solution of the finite environmental Markov generator.
for nus in ('0.05', '0.3', '1', '4.8'):
    nu = mp.mpf(nus)
    rates = [mp.mpf('0.2'), mp.mpf('3.7')]
    probs = [mp.mpf('0.3'), mp.mpf('0.7')]
    D = mp.mpf('1.6')
    matrix = lambda power: mp.matrix([[power * rates[i] * (i == j) + nu * (int(i == j) - probs[j])
                                       for j in range(2)] for i in range(2)])
    m_vec = mp.lu_solve(matrix(1), mp.matrix([2 * D, 2 * D]))
    p_vec = mp.lu_solve(matrix(2), mp.matrix([4 * D * m_vec[0], 4 * D * m_vec[1]]))
    h_vec = mp.lu_solve(matrix(1), mp.matrix([12 * D * m_vec[0], 12 * D * m_vec[1]]))
    got = [sum(probs[i] * vec[i] for i in range(2)) for vec in (m_vec, p_vec, h_vec)]
    predicted = formulas(nu, rates, probs, D)
    for j in range(3):
        check(close(got[j], predicted[j]), 'finite state stationary moment ' + str(j))
    check(mp.mpf(0) < predicted[3] < mp.mpf(1)/3, 'positive finite-state correlation')
    check(close(predicted[3], (got[1] - got[0]**2)/(got[2] - got[0]**2)), 'independent correlation quotient')

# A deterministic rate must yield *independent* stationary particles.
for nu in ('0.02', '0.7', '19'):
    M, P, H, rho, _ = formulas(mp.mpf(nu), [mp.mpf('2.5')], [mp.mpf(1)], mp.mpf('1.4'))
    check(close(P, M*M), 'independent deterministic reset moments')
    check(close(rho, 0), 'zero correlation under deterministic hazard')
    check(close(H, 6*M*M), 'Laplace one-particle fourth moment')

# Exact rational identity C=(2B-A)/nu for a discrete mixture.
for nu in (Q(1, 3), Q(3, 7), Q(25, 1)):
    rates, probs = [Q(1, 5), Q(9, 4)], [Q(2, 3), Q(1, 3)]
    a = sum(p/(r+nu) for p, r in zip(probs, rates))
    b = sum(p/(2*r+nu) for p, r in zip(probs, rates))
    c = sum(p/((r+nu)*(2*r+nu)) for p, r in zip(probs, rates))
    check(c == (2*b-a)/nu, 'rational partial fraction identity')


def gamma_moments(alpha, nu):
    alpha, nu = mp.mpf(str(alpha)), mp.mpf(str(nu))
    f = lambda x: x**alpha * mp.exp(-x) / mp.gamma(alpha+1)
    edges = [0, nu, mp.mpf('0.01'), mp.mpf('0.1'), 1, 5, mp.inf]
    def integral(g):
        return mp.quad(lambda x: f(x)*g(x), edges)
    a = integral(lambda x: 1/(x+nu))
    b = integral(lambda x: 1/(2*x+nu))
    a2 = integral(lambda x: 1/(x+nu)**2)
    c = integral(lambda x: 1/((x+nu)*(2*x+nu)))
    s, t = 1-nu*a, 1-nu*b
    rho = (2*c*s/t-a*a)/(6*a2-a*a)
    return rho, a, b, a2, c


# Scaling law for three different low-rate exponents.
for alpha in ('-0.5', '0', '0.5'):
    rho, a, b, a2, c = gamma_moments(alpha, '0.000001')
    aa = mp.mpf(alpha)
    target = (1-mp.power(2,-aa))/(3*aa) if aa else mp.log(2)/3
    check(abs(rho-target) < mp.mpf('0.0015'), 'universal gamma-density scaling ' + alpha)
    check(mp.mpf(0) < rho < mp.mpf(1)/3, 'positive gamma-rate correlation')
    check(close(c, (2*b-a)/mp.mpf('0.000001'), '1e-30'), 'quadrature C identity')

# The integral identity in the proof is checked independently at three exponents.
for alpha in ('-0.8', '0', '0.7'):
    aa = mp.mpf(alpha)
    k = mp.quad(lambda t: t**aa/(1+t)**2, [0, 1, mp.inf])
    j = mp.quad(lambda t: t**aa/((1+t)*(1+2*t)), [0, 1, mp.inf])
    target = (1-mp.power(2,-aa))/aa if aa else mp.log(2)
    check(close(j/k, target, '1e-9'), 'analytic universal-integral identity')

# Stable direct formula for exponentially distributed instantaneous rates.
for nu_s in ('0.000001', '0.001', '0.5', '12'):
    nu=mp.mpf(nu_s)
    a=mp.exp(nu)*mp.e1(nu)
    b=mp.exp(nu/2)*mp.e1(nu/2)/2
    a2=1/nu-a
    c=(2*b-a)/nu
    s,t=1-nu*a,1-nu*b
    rho=(2*c*s/t-a*a)/(6*a2-a*a)
    check(0<rho<mp.mpf(1)/3, 'exponential finite refresh')
    if nu_s=='0.000001':
        check(abs(rho-mp.log(2)/3) < mp.mpf('0.00003'), 'explicit logarithmic correlation limit')

print('PASS:', count, 'deterministic checks')
