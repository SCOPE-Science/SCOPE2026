"""Independent matrix-generator checks for a finite quantum path with local dephasing."""
import math
import numpy as np
from scipy.linalg import solve


def expected(n, trap, noisy_sites, initial):
    g = math.gcd(n + 1, trap)
    for j in noisy_sites:
        g = math.gcd(g, j)
    return 1.0 - (g / (n + 1) if initial % g else 0.0)


def numerical(n, trap, noisy_sites, initial, coupling, sink_rate, noise_rate, regularizer=1e-8):
    eye = np.eye(n)
    h = np.diag(np.ones(n - 1), 1) + np.diag(np.ones(n - 1), -1)
    h *= coupling
    pc = np.zeros((n, n))
    pc[trap - 1, trap - 1] = 1
    lhs = -1j * (np.kron(eye, h) - np.kron(h.T, eye))
    lhs -= 0.5 * sink_rate * (np.kron(eye, pc) + np.kron(pc.T, eye))
    for ix, j in enumerate(noisy_sites):
        p = np.zeros((n, n))
        p[j-1, j-1] = 1
        lhs += noise_rate * (0.65 + 0.31 * ix) * (np.kron(p.T, p) - 0.5 * (np.kron(eye, p) + np.kron(p.T, eye)))
    initial_vec = np.zeros(n*n, dtype=complex)
    initial_vec[(initial-1)*n + (initial-1)] = 1
    z = solve(regularizer * np.eye(n*n) - lhs, initial_vec, assume_a='gen')
    survival = regularizer * np.trace(z.reshape((n,n), order='F')).real
    return 1 - survival


def run():
    tests = [(5,3,[],1),(5,3,[3],1),(5,3,[2],1),
             (7,4,[2],1),(7,4,[1],1),(7,4,[2],2),
             (11,4,[6],1),(11,4,[6],2),(11,4,[6,8],1),
             (11,6,[2,4],1),(11,6,[4],3)]
    for n in range(3,9):
        for trap in range(1,n+1):
            for j in range(1,n+1):
                for initial in (1, n):
                    if (n+trap+j+initial)%5==0:
                        tests.append((n, trap, [j], initial))
    for n in range(4, 9):
        for c in (2, n // 2):
            for a in (1, n):
                for j in (1, 2, n):
                    tests.append((n, c, [j, n - j + 1], a))
    for i, (n,c,s,a) in enumerate(tests):
        rate = .45 + .04*(i%7)
        sink = .8 + .07*(i%5)
        calc = numerical(n,c,s,a,1.2,sink,rate)
        pred = expected(n,c,s,a)
        err = abs(calc - pred)
        if err > 1.5e-4:
            raise AssertionError(f'N={n},c={c},S={s},a={a}, predicted {pred}, computed {calc}, error {err}')
    print('Lindblad resolvent checks PASS',len(tests),'cases')
    print('Examples:',[(x,expected(*x)) for x in tests[:11]])
    print('maximum discrepancy tolerance: 1.5e-4 at s=1e-8; positive nonuniform per-site rates included')

if __name__ == '__main__':
    run()
