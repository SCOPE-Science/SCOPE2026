import math
import numpy as np


def bisect(f, lo, hi, iters=100):
    flo = f(lo)
    fhi = f(hi)
    if not (flo <= 0.0 <= fhi):
        raise ValueError((flo, fhi, lo, hi))
    for _ in range(iters):
        mid = (lo + hi) / 2.0
        if f(mid) <= 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def xi_limit(a):
    if a == 0.0:
        return 0.0
    return bisect(lambda x: x * math.tan(x / 2.0) - a,
                  0.0, math.pi * (1.0 - 1e-14))


def omega1(N, rho):
    def theta(w):
        return math.atan2(rho * math.sin(w), 1.0 - rho * math.cos(w))
    return bisect(lambda w: (N + 1) * w + 2.0 * theta(w) - math.pi,
                  0.0, math.pi / (N + 1))


def overlap_exact(N, omega):
    if omega == 0.0:
        return 1.0
    numerator = math.sin(N * omega / 2.0) / math.sin(omega / 2.0)
    norm_sq = N / 2.0 + math.sin(N * omega) / (2.0 * math.sin(omega))
    return numerator / math.sqrt(N * norm_sq)


def overlap_limit(xi):
    if xi == 0.0:
        return 1.0
    mean = 2.0 * math.sin(xi / 2.0) / xi
    norm_sq = 0.5 + math.sin(xi) / (2.0 * xi)
    return mean / math.sqrt(norm_sq)


def lambda1(N, rho, omega):
    return (1.0 - rho * rho) / (1.0 - 2.0 * rho * math.cos(omega) + rho * rho)


def direct_principal_eigenpair(N, rho):
    idx = np.arange(N)
    covariance = rho ** np.abs(idx[:, None] - idx[None, :])
    values, vectors = np.linalg.eigh(covariance)
    w = vectors[:, -1]
    if np.sum(w) < 0.0:
        w = -w
    dc = np.ones(N) / math.sqrt(N)
    return values[-1], float(np.dot(w, dc))


def main():
    print('Local-to-unity scaling rho_N = exp(-a/N)')
    max_overlap_err = 0.0
    max_eval_err = 0.0
    for a in (0.1, 1.0, 5.0):
        xi_star = xi_limit(a)
        c_star = overlap_limit(xi_star)
        eig_star = math.sin(xi_star) / xi_star
        print(f'a={a}')
        for N in (64, 128, 256, 512):
            rho = math.exp(-a / N)
            omega = omega1(N, rho)
            overlap = overlap_exact(N, omega)
            eig = lambda1(N, rho, omega) / N
            eig_direct, overlap_direct = direct_principal_eigenpair(N, rho)
            eig_direct /= N
            max_overlap_err = max(max_overlap_err, abs(overlap - overlap_direct))
            max_eval_err = max(max_eval_err, abs(eig - eig_direct))
            print('  N=%4d Nomega=%.12f xi*=%.12f overlap=%.12f C*=%.12f lambda/N=%.12f L*=%.12f' %
                  (N, N * omega, xi_star, overlap, c_star, eig, eig_star))
    print('max |closed-form overlap - direct eig| = %.3e' % max_overlap_err)
    print('max |closed-form lambda/N - direct eig/N| = %.3e' % max_eval_err)

    print('\nA diagonal sequence with rho_N -> 1 but N(1-rho_N) -> infinity')
    target = 2.0 * math.sqrt(2.0) / math.pi
    for N in (256, 1024, 4096, 16384):
        rho = 1.0 - 1.0 / math.sqrt(N)
        omega = omega1(N, rho)
        print('  N=%5d rho=%.12f N(1-rho)=%.6f overlap=%.12f' %
              (N, rho, N * (1.0 - rho), overlap_exact(N, omega)))
    print('limiting overlap = 2sqrt(2)/pi = %.15f' % target)
    print('limiting optimal-sign row distance = %.15f' % math.sqrt(2.0 - 2.0 * target))

    print('\nFixed rho: N*omega -> pi and overlap -> 2sqrt(2)/pi')
    for rho in (0.90, 0.99, 0.999):
        for N in (128, 512, 2048, 8192):
            omega = omega1(N, rho)
            print('  rho=%.3f N=%5d Nomega=%.12f overlap=%.12f' %
                  (rho, N, N * omega, overlap_exact(N, omega)))
        print()

    print('Small-a check: d(a)/(a/sqrt(180)) -> 1')
    for a in (1e-1, 3e-2, 1e-2, 3e-3):
        xi = xi_limit(a)
        distance = math.sqrt(2.0 - 2.0 * overlap_limit(xi))
        print('  a=%.4g ratio=%.12f' % (a, distance / (a / math.sqrt(180.0))))


if __name__ == '__main__':
    main()
