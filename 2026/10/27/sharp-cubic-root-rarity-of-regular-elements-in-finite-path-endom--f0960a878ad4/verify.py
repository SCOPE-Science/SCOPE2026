"""Finite checks for the path-endomorphism regularity and spectral bounds."""
from itertools import product
from math import cos, sin, pi, log


def endos(n):
    out = []
    for first in range(n):
        for steps in product((-1, 1), repeat=n - 1):
            a = [first]
            for step in steps:
                a.append(a[-1] + step)
                if not 0 <= a[-1] < n:
                    break
            if len(a) == n and all(0 <= v < n for v in a):
                out.append(tuple(a))
    return out


def criterion(f):
    h = max(f) - min(f)
    return any(
        (all(f[i+j] == f[i] + j for j in range(h + 1)) or
         all(f[i+j] == f[i] - j for j in range(h + 1)))
        for i in range(len(f) - h)
    )


def direct_regular(f, endomorphisms):
    return any(all(f[g[f[i]]] == f[i] for i in range(len(f))) for g in endomorphisms)


def count_walks(h, length):
    x = [1] * (h + 1)
    for _ in range(length):
        x = [(x[j-1] if j > 0 else 0) + (x[j+1] if j < h else 0)
             for j in range(h + 1)]
    return x


def main():
    for n in range(2, 13):
        es = endos(n)
        reg = sum(criterion(f) for f in es)
        if n <= 7:
            assert all(criterion(f) == direct_regular(f, es) for f in es), n
        m = n - 1
        upper = 0.0
        for h in range(1, m+1):
            lam = 2 * cos(pi / (h+2))
            upper += 2*(n-h)*(m-h+1)*(h+1)*lam**(m-h)
            lower = (n-h)*sin(pi/(h+2))*lam**(m-h)
            assert reg + 1.e-7 >= lower, (n, h)
        assert reg <= upper + 1.e-7, n
        assert reg <= len(es) <= n * 2**m
        print("FINITE_ENDOMORPHISM_COUNTS", n, len(es), reg)
    rate = 1.5 * pi**(2/3) * log(2)**(2/3)
    print("SHARP_LOG_RATE", f"{rate:.12f}")
    for m in (10_000, 1_000_000, 100_000_000):
        # Compute the minimum near its theoretically controlled cubic-root scale.
        u = (pi*pi/log(2))**(1/3)
        center = round(u*m**(1/3))
        best = min(
            (h*log(2) - (m-h)*log(cos(pi/(h+2))), h)
            for h in range(max(1, center//2), min(m, center*2)+1)
        )
        print("SPECTRAL_VARIATIONAL_CHECK", m, best[1], f"{best[0]/m**(1/3):.9f}")
    print("ALL_REGULAR_PATH_CHECKS_PASSED")


if __name__ == "__main__":
    main()
