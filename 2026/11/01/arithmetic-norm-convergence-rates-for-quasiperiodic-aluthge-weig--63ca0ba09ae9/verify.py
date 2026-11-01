"""Reproducibility checks for quasiperiodic Aluthge binomial smoothing.

Pure Python; these finite checks are supplementary to the analytic proof.
"""
import cmath
import math


def centered_poisson(x, rho=0.8, modes=35):
    return 2.0 * sum(math.exp(-rho*m) * math.cos(2*math.pi*m*x)
                     for m in range(1, modes+1))


def binomial_average(k, theta, x, rho=0.8, modes=35):
    return sum(math.comb(k, j)*centered_poisson(x+j*theta, rho, modes)
               for j in range(k+1)) / 2**k


def fourier_average(k, theta, x, rho=0.8, modes=35):
    ans = 0j
    for m in range(1, modes+1):
        multiplier = (1.0 + cmath.exp(2j*math.pi*m*theta))/2.0
        ans += (2.0*math.exp(-rho*m)*
                (multiplier**k)*cmath.exp(2j*math.pi*m*x))
    return ans.real


def run():
    theta = (math.sqrt(5)-1)/2
    rho = 0.8
    count = 0
    for k in range(16):
        for x in [0.002, 0.123, 0.271, 0.419, 0.711]:
            direct = binomial_average(k, theta, x, rho)
            spectral = fourier_average(k, theta, x, rho)
            assert abs(direct-spectral) < 3e-9, (k, x, direct, spectral)
            count += 1
    # Check real-weight mean-value comparison at representative test values.
    M = 2.0*math.exp(-rho)/(1-math.exp(-rho))
    for k in range(20):
        for j in range(17):
            x = (j+0.32)/17
            f = fourier_average(k, theta, x, rho)
            discrepancy = abs(math.expm1(f))
            assert math.exp(-M)*abs(f)-1e-12 <= discrepancy
            assert discrepancy <= math.exp(M)*abs(f)+1e-12
            count += 1
    # The irrational-resonance barrier is checked using Fibonacci denominators.
    fib = [1, 2]
    while fib[-1] < 2000000:
        fib.append(fib[-1]+fib[-2])
    for k in [1000, 3000, 10000, 30000, 100000, 300000, 1000000]:
        threshold = k**(1/3)
        den = max(q for q in fib if q <= threshold)
        delta = abs(den*theta-round(den*theta))
        assert delta < 1/threshold
        coeff = math.exp(-rho*den)*abs(math.cos(math.pi*delta))**k
        assert coeff >= math.exp(-(rho+10)*threshold)*0.999999
        count += 1
    # Near-rational harmonics retain substantial amplitude for long times.
    k = 10000
    den = 11
    almost_resonant_theta = 1/11 + 1/10**8
    gain = abs(math.cos(math.pi*den*almost_resonant_theta))**k
    assert gain > 0.999999
    count += 1
    print(f"PASS: {count} supplementary Fourier, binomial and arithmetic checks")


if __name__ == '__main__':
    run()
