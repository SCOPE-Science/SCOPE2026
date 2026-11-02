"""Finite cross-check of quantum-path sine nodes and their gcd-based mass."""
import math


def run():
    count = 0
    for n in range(2, 80):
        q = n + 1
        for sink in range(1, n + 1):
            for noise in (0, 1, n // 2, n):
                noisy = [] if noise == 0 else [noise]
                g = math.gcd(q, sink)
                for j in noisy:
                    g = math.gcd(g, j)
                node_indices = [k for k in range(1, q)
                                if all((k * t) % q == 0 for t in [sink] + noisy)]
                predicted_indices = [m * q // g for m in range(1, g)]
                assert node_indices == predicted_indices, (n, sink, noisy)
                for source in (1, n // 2, n):
                    v = (2 / q) * sum(math.sin(math.pi * source * k / q)**2
                                      for k in node_indices)
                    answer = g / q if source % g else 0
                    assert abs(v - answer) < 1e-11, (n, sink, noisy, source, v)
                    count += 1
    print('Spectral-arithmetic comparisons PASS:', count)


if __name__ == '__main__':
    run()
