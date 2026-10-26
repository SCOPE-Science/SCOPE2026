from __future__ import annotations


def count_fixed_p_torsion(p: int, b: int) -> int:
    """Exhaustively count Aut(C_p x C_(p^b)) with Fix(phi) = A[p]."""
    n = p**b
    a_p = {(u, v) for u in range(p) for v in range(0, n, p**(b - 1))}
    count = 0
    # Every automorphism has phi(x)=a*x+p^(b-1)*c*y,
    # phi(y)=beta*x+d*y, with a,d units modulo p.
    for a in range(1, p):
        for c in range(p):
            for beta in range(p):
                for d in range(n):
                    if d % p == 0:
                        continue
                    fixed = set()
                    for u in range(p):
                        for v in range(n):
                            image = (
                                (a * u + beta * v) % p,
                                (p ** (b - 1) * c * u + d * v) % n,
                            )
                            if image == (u, v):
                                fixed.add((u, v))
                    if fixed == a_p:
                        count += 1
    return count


def formula(p: int, b: int) -> int:
    return (p - 1) * p ** (b - 1) + ((p - 1) if b == 2 else 0)


if __name__ == "__main__":
    cases = [(p, b) for p in (2, 3) for b in (2, 3, 4)] + [(5, 2), (5, 3)]
    for p, b in cases:
        got = count_fixed_p_torsion(p, b)
        expected = formula(p, b)
        print(f"p={p}, b={b}: exhaustive={got}, formula={expected}, match={got == expected}")
        if got != expected:
            raise SystemExit(1)
    print("ALL_CHECKS_PASSED")
