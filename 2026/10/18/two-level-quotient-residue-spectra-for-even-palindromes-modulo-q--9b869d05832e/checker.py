"""Exact integer checks for the quotient-residue distribution of even palindromes.

Run with Python 3; no third-party packages required. Finite checks support, but
cannot replace, the algebraic proof for arbitrary prime and half-length.
"""
from itertools import product


def predicted(q, m):
    """Formula for all residues of P/q modulo q."""
    assert q >= 3 and m >= 1
    z = sum((2*m - 1 - 2*j) % q == 0 for j in range(1, m))
    total = (q-2) * (q-1)**(m-1)
    out = []
    for r in range(q):
        if (2*m-1) % q:
            indicator = int((r-(m-1)) % q == 0) + int((r+m) % q == 0)
            correction = (-1)**(m-z)*(q-1)**z*(q*indicator - 2)
        else:
            indicator = int((r-(m-1)) % q == 0)
            correction = (q-2)*(-1)**(m-1-z)*(q-1)**z*(q*indicator - 1)
        numerator = total + correction
        assert numerator % q == 0
        out.append(numerator//q)
    assert sum(out) == total
    return out


def modular_convolution(q, m):
    """Independent integer DP on actual palindrome coefficients modulo q**2."""
    b = q-1
    modulus = q*q
    weights = [((pow(b,j,modulus)+pow(b,2*m-1-j,modulus)) % modulus)
               for j in range(m)]
    state = [0]*modulus
    for digit in range(1,b):
        state[(digit*weights[0])%modulus] += 1
    for w in weights[1:]:
        nxt = [0]*modulus
        for old, count in enumerate(state):
            if count:
                for digit in range(b):
                    nxt[(old + digit*w)%modulus] += count
        state = nxt
    assert all(state[x]==0 for x in range(modulus) if x%q)
    return [state[q*r] for r in range(q)]


def brute(q, m):
    """Enumerate actual integers, not the formal Fourier weights."""
    b = q-1
    out = [0]*q
    for lead in range(1,b):
        for rest in product(range(b), repeat=m-1):
            digits = (lead,) + rest
            value = sum(digit*(b**j + b**(2*m-1-j))
                        for j,digit in enumerate(digits))
            assert value % q == 0
            out[(value//q)%q] += 1
    return out


def main():
    for q in (3,5,7,11,13,17):
        for m in range(1,26):
            theory = predicted(q,m)
            assert theory == modular_convolution(q,m), (q,m,theory)
            if q<=7 and m<=4:
                assert theory == brute(q,m), (q,m)
        print(f"PASS: q={q}; m=1..25, all residue classes")
    print("PASS: all independent modular-convolution and brute checks")


if __name__ == '__main__':
    main()
