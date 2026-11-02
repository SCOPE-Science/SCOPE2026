"""Exact checks for a leaf/full broadcast-spin residual on recursive trees.

Requires only Python's standard library. Run: python checker.py
The finite tests are diagnostic, not a proof of the infinite-size CLT.
"""
from fractions import Fraction as F
from itertools import product


def states(n, t):
    for ps in product(*(range(j) for j in range(1, n))):
        parent_weight = F(1)
        for j in range(1, n):
            parent_weight /= j
        children = [0] * n
        for p in ps:
            children[p] += 1
        for signs in product((-1, 1), repeat=n-1):
            w = parent_weight
            for s in signs:
                w *= (1 + s * t) / 2
            if w == 0:
                continue
            spins = [1]
            for j, (p, s) in enumerate(zip(ps, signs), start=1):
                spins.append(s * spins[p])
            x = sum(spins)
            y = sum(spins[i] for i, c in enumerate(children) if c == 0)
            yield w, tuple(spins), tuple(children), x, y


def run():
    checks = 0
    params = [F(-3, 4), F(-1, 2), F(0), F(1, 3), F(1, 2), F(3, 4), F(1)]
    for t in params:
        alpha = t / (1 + t)
        variance_coefficient = (3 - t*t) / (6*(1+t)**2)
        expected_x = F(1)
        for n in range(2, 8):
            expected_x *= 1 + t / (n-1)
            m = {k: F(0) for k in ('prob', 'x', 'y', 'z', 'z2', 'leaf')}
            for w, spins, children, x, y in states(n, t):
                z = y - alpha*x
                m['prob'] += w
                m['x'] += w*x
                m['y'] += w*y
                m['z'] += w*z
                m['z2'] += w*z*z
                m['leaf'] += w*sum(c == 0 for c in children)
                if n <= 5:
                    # This branch re-derives the one-step identities by
                    # enumerating each possible parent and child spin.
                    eznext = eznext2 = F(0)
                    for parent in range(n):
                        for sign in (-1, 1):
                            p = (1 + sign*t)/(2*n)
                            xn = x + sign*spins[parent]
                            yn = y + sign*spins[parent] - (spins[parent] if children[parent] == 0 else 0)
                            zn = yn - alpha*xn
                            eznext += p*zn
                            eznext2 += p*zn*zn
                    assert eznext == (1-F(1, n))*z
                    checks += 1
                    v = (1-F(2,n))*z*z + F(1,(1+t)**2) + ((1-t)/(1+t))*F(sum(c == 0 for c in children),n)
                    assert eznext2 == v
                    checks += 1
            assert m['prob'] == 1
            assert m['x'] == expected_x
            assert m['y'] == alpha*expected_x
            assert m['z'] == 0
            assert m['leaf'] == F(n,2)
            assert m['z2'] == (n*variance_coefficient if n >= 3 else (1-t)/(1+t))
            checks += 6
            print(f't={t!s:>4}, n={n}: E(X)={m["x"]}, E(Z^2)={m["z2"]}')
    print(f'PASS: {checks} exact rational assertions')

if __name__ == '__main__':
    run()
