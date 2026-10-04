from mpmath import mp

mp.dps = 80

def Phi(x):
    return mp.mpf('0.5') * (1 + mp.erf(x / mp.sqrt(2)))

def barPhi(x):
    return mp.mpf('0.5') * mp.erfc(x / mp.sqrt(2))

def exact_modulus(n, b, x=0):
    n = mp.mpf(n)
    b = mp.mpf(b)
    L = mp.log(1 / b)
    C = mp.sqrt(b) * L / (4 * mp.sqrt(mp.pi))
    S = mp.log(n) - mp.mpf('1.5') * mp.log(mp.log(n)) + mp.log(C) + x
    r = L / mp.sqrt(2 * S)
    A = b * barPhi(L / r - r / 2) - barPhi(L / r + r / 2)
    a = 1 / (2 * n)
    gamma = r / 2 - mp.log(2 * n * b) / r
    B = a * Phi(gamma) - b * Phi(gamma - r)
    return r, max(A, B), A, B

for b in ('0.8', '0.4'):
    vals = []
    for power in (12, 24, 50, 100):
        n = mp.power(10, power)
        r, D, A, B = exact_modulus(n, b)
        vals.append(n * D)
        assert A >= 0 and B >= 0 and D >= A and D >= B
    assert abs(vals[-1] - 1) < mp.mpf('0.12')
print('VERIFY_OK')
