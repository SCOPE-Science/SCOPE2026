"""Separate high-precision checks for rare-target fidelity-hitting Laplace bounds.

The computations test finite parameter sets; the mathematical proof establishes all
stated quantifiers without relying on numerical testing.
"""
import mpmath as mp

mp.mp.dps = 65
checks = 0

def check(ok, label):
    global checks
    assert bool(ok), label
    checks += 1

def alpha(n):
    return mp.harmonic(n - 1) / (n - 1)

def mean(n, b):
    eps = 1 - b
    return (mp.log(1 / eps) + sum((eps ** (-j) - 1) / j for j in range(1, n-1))) / (n-1)

def regular_solution(n, b, s):
    M = n - 1
    root = mp.sqrt(M*M - 4*s)
    return mp.hyp2f1((M-root)/2, (M+root)/2, 1, b)

def integral_K(n, b, g):
    # This directly numerically evaluates both nested integrals; avoid endpoints.
    return mp.quad(lambda x: mp.quad(lambda y: (1-y)**(n-2)*g(y), [0, x]) / (x*(1-x)**(n-1)), [0, b])

# Check independent hypergeometric ODE normalization and first two derivatives.
for n in range(2, 7):
    for btext in ['0.20', '0.65', '0.90', '0.99']:
        b = mp.mpf(btext)
        m = mean(n,b)
        f = lambda s: regular_solution(n,b,s)
        f1 = mp.diff(f, 0, 1)
        f2 = mp.diff(f, 0, 2) / 2
        A2 = f2
        check(mp.almosteq(f(0),1), f'f0 n={n},b={b}')
        check(mp.almosteq(f1,m,rel_eps=mp.mpf('1e-48')),f'mean n={n},b={b}: {f1} != {m}')
        check(0<A2<alpha(n)*m, f'positive subharmonic bound n={n},b={b}')
        check(0<1-2*A2/m**2<1, f'coefficient of variation n={n},b={b}')
        for theta in ['0.2','0.9','2.0']:
            theta=mp.mpf(theta)
            if theta*alpha(n)>=m: continue
            phi=f(theta/m)
            check(abs(mp.im(phi))<mp.mpf('1e-42'),f'imaginary numerical artefact n={n},b={b}')
            actual=mp.re(1/(1+theta)-1/phi)
            bound=alpha(n)*theta**2/(m*(1+theta)**2*(1-alpha(n)*theta/m))
            check(0<actual<bound, f'Laplace n={n},b={b},theta={theta}; actual={actual}, bound={bound}')

# Independently integrate the weighted first passage mean to verify H_{n-1}.
for n in range(2,7):
    M=n-1
    J=mp.quad(lambda y: (1-y)**(n-2)*mean(n,y), [0, mp.mpf('0.5'), mp.mpf('0.9'), mp.mpf('0.99'), 1])
    target=mp.harmonic(M)/M**2
    check(abs(J-target)<mp.mpf('1e-43'), f'integral identity n={n}, error={J-target}')

# Verify the first correction approaches the exact alpha_n coefficient.
for n in range(2,7):
    b=mp.mpf('0.999999') if n==2 else mp.mpf('0.999')
    m=mean(n,b)
    A2=mp.diff(lambda s: regular_solution(n,b,s),0,2)/2
    check(abs(A2/m-alpha(n)) < (mp.mpf('.12') if n==2 else mp.mpf('.05')),
          f'asymptotic prefactor n={n}: {A2/m}')

print(f'PASS: {checks} high-precision numerical checks (no infinite-proof claim).')
