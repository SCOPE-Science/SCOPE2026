"""Independent finite checks for the modular half-shuffle Zinbiel theorem.
Pure Python 3 standard library. No external research environment dependencies.
"""
from math import comb


def product_coefficient(i, j, n, p):
    return comb(i + j - 1, j) % p if i + j <= n else 0


def has_no_base_p_carry(a, b, p):
    while a or b:
        if a % p + b % p >= p:
            return False
        a //= p
        b //= p
    return True


def beta_by_exhaustive_pairs(n, p):
    # A proper ideal is span(e_r,...,e_n) for a unique r.
    for r in range(1, n + 1):
        if all(product_coefficient(i, j, n, p) == 0
               for i in range(r, n + 1)
               for j in range(r, n + 1)
               if i + j <= n):
            return n - r + 1
    raise AssertionError("No abelian ideal")


def test_identity(n, p):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if i + j + k <= n:
                    lhs = product_coefficient(i, j, n, p) * product_coefficient(i + j, k, n, p)
                    rhs = (product_coefficient(j, k, n, p)
                           + product_coefficient(k, j, n, p)) * product_coefficient(i, j + k, n, p)
                    assert (lhs - rhs) % p == 0, (i, j, k, n, p)


def main():
    checked = []
    for p in (2, 3, 5, 7, 11):
        for n in range(1, 14):
            test_identity(n, p)
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if i + j <= n:
                        assert (product_coefficient(i, j, n, p) != 0) == has_no_base_p_carry(i - 1, j, p)
        for k in range(0, 6):
            P = p ** k
            lower = (p + (p + 1) // 2) * P
            upper = (2 * p - 1) * P
            if upper > 115:
                break
            for n in range(lower, upper + 1):
                observed = beta_by_exhaustive_pairs(n, p)
                assert observed == p * P, (p, k, n, observed, p * P)
                r = n - p * P + 1
                assert product_coefficient(r-1, p*P, n, p) == 1
                checked.append((p, k, n))
    print("PASS: Zinbiel identity and Lucas criterion for p=2,3,5,7,11 and n<=13.")
    print("PASS: exact maximal abelian-ideal dimension on", len(checked),
          "parameter triples in claimed plateaux, maximum n=", max(n for _,_,n in checked))
    print("Sample (p,k,n,beta):", [(p,k,n,p*p**k) for p,k,n in checked if (p,k,n) in ((2,3,24),(3,1,15),(5,1,40),(7,1,77))])


if __name__ == "__main__":
    main()
