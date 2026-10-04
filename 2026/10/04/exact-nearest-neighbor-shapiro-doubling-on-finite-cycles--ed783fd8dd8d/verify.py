import math

TOL = 5e-11

def cval(n):
    return 1.0 if n % 2 == 0 else math.cos(math.pi/n)

for n in range(5, 401):
    c = cval(n)
    C = 4*c - 1
    q = n//2

    # Dual certificate: tauhat(k)=4(1-x)(x+c).
    vals = []
    for k in range(n):
        x = math.cos(2*math.pi*k/n)
        tauhat = 4*(1-x)*(x+c)
        assert tauhat >= -TOL, (n, k, tauhat)
        vals.append(tauhat)

    # Primal witness.
    f = [(c + math.cos(2*math.pi*q*j/n))/(1+c) for j in range(n)]
    assert min(f) >= -TOL, (n, min(f))
    assert abs(f[0]-1) < TOL
    assert abs(f[1]) < TOL and abs(f[-1]) < TOL
    assert abs(f[2]-(2*c-1)) < 2*TOL and abs(f[-2]-(2*c-1)) < 2*TOL

    denom = f[0] + f[1] + f[-1]
    numer = f[0] + f[1] + f[-1] + f[2] + f[-2]
    assert abs(numer/denom - C) < 5*TOL, (n, numer/denom, C)

    # Direct DFT positivity of the witness.
    for k in range(n):
        re = sum(f[j]*math.cos(2*math.pi*k*j/n) for j in range(n))
        im = -sum(f[j]*math.sin(2*math.pi*k*j/n) for j in range(n))
        assert abs(im) < 2e-8, (n, k, im)
        assert re >= -2e-8, (n, k, re)

print("VERIFY_OK")
