"""Rational-point search on E1: 5x^2+5y^2-12x^2y^2-2=0, x=a/b coprime, b>=1.
y^2 = (2b^2-5a^2)/(5b^2-12a^2); rationality <=> N=(2b^2-5a^2)(5b^2-12a^2)
= 60a^4-49a^2b^2+10b^4 is a nonzero square (>=0). Exhaustive to B=3000.
Replay: python3 e1_rational_search.py (takes a few minutes). Stdlib only.
"""
import math

def search(B):
    hits = []
    for b in range(1, B + 1):
        b2 = b * b
        for a in range(-B, B + 1):
            if math.gcd(abs(a), b) != 1:
                continue
            v = 60 * a ** 4 - 49 * a * a * b2 + 10 * b2 * b2
            if v <= 0:
                continue
            s = math.isqrt(v)
            if s * s == v:
                hits.append((a, b))
    return hits

if __name__ == "__main__":
    h = search(3000)
    print("E1 rational search B=3000 hits:", h)
    assert h == []
    print("SEARCH_OK: no E1(Q) point with |a|,b<=3000")
