"""Supplementary numerical quadrature of spherical two-scale exponential Legendre coefficients."""
import mpmath as mp

mp.mp.dps = 45


def coefficient(a, n):
    a = mp.mpf(a)
    return mp.quad(lambda th: mp.exp(-a*th)*mp.legendre(n, mp.cos(th))*mp.sin(th), [0, mp.pi])


def recurrence(a, n):
    a = mp.mpf(a)
    E = mp.exp(-mp.pi*a)
    v = (1 + E)/(a*a + 1) if n % 2 == 0 else (1 - E)/(a*a + 4)
    for k in range(n % 2, n, 2):
        v *= (a*a+k*k)/(a*a+(k+3)**2)
    return v


if __name__ == '__main__':
    max_error = mp.mpf(0)
    for a in ['0.3', '1.2', '2.5']:
        for n in range(12):
            err = abs(coefficient(a, n) - recurrence(a, n))
            max_error = max(max_error, err)
    print('max absolute Legendre integral discrepancy:', mp.nstr(max_error, 12))
    for a, b in [('0.3', '1.2'), ('2.5', '0.8')]:
        a, b = mp.mpf(a), mp.mpf(b)
        if a < b:
            bound = a*(1-mp.exp(-mp.pi*a))/(b*(1-mp.exp(-mp.pi*b)))
        else:
            bound = ((1+mp.exp(-mp.pi*a))/(a*a+1))/((1+mp.exp(-mp.pi*b))/(b*b+1))
        ratios = [recurrence(a,n)/recurrence(b,n) for n in range(30)]
        assert min(ratios) >= bound - mp.mpf('1e-40')
        print('parameters:', mp.nstr(a), mp.nstr(b), 'sharp bound:',mp.nstr(bound,14),'smallest first 30 ratios:',mp.nstr(min(ratios),14))
    print('CHECK_OK')
