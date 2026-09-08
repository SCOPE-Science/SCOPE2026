"""Replayable verification for lane-189 partial census (stdlib only).

Verifies, from the stated integers alone:
 1. consecutiveness: the 10 least primes l = 7 mod 9 above 2000;
 2. cube-freeness of n = 3*l;
 3. global root number w(n) = 1 via the Birch--Stephens local formula;
 4. cubic residue symbol (3/l)_3 by exact Euler-criterion arithmetic
    (two independent implementations), which by Das-Jha Lemma 2.5
    determines the 3-rank h3(12*l), and by Das-Jha Theorem A decides
    six proved non-cube-sum witnesses.
"""
import math

LS = [2113, 2131, 2203, 2221, 2239, 2293, 2311, 2347, 2383, 2437]

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for p in range(3, r + 1, 2):
        if n % p == 0:
            return False
    return True

def modexp_loop(base, exp, mod):
    r = 1
    for _ in range(exp):
        r = (r * base) % mod
    return r

print("== 1. consecutiveness ==")
found = [n for n in range(2001, 2500) if n % 9 == 7 and is_prime(n)][:11]
print("first 11 primes 7 mod 9 above 2000:", found)
assert found[:10] == LS, "window mismatch"
print("OK: window is the 10 least such primes")

print("== 2/3/4. per-n table ==")
print(f"{'l':>6} {'n=3l':>6} {'n%9':>4} {'cubefree':>9} {'w(n)':>5} "
      f"{'3^((l-1)/3) mod l':>18} {'(3/l)_3=1?':>11} {'h3(12l)':>8} verdict")
witnesses = []
for l in LS:
    assert is_prime(l) and l % 9 == 7 and l > 2000
    n = 3 * l
    assert n % 9 == 3
    # cube-free: squarefree check (trial division suffices at this size)
    cf = True
    d = 2
    tmp = n
    while d * d <= tmp:
        if tmp % (d ** 3) == 0:
            cf = False
        while tmp % d == 0:
            tmp //= d
        d += 1 if d == 2 else 2
    assert cf
    # Birch-Stephens root number: w3=-1 since n=+/-3 mod 9;
    # p|n, p!=3: l=1 mod 3 so w_l=+1; w = -w3 * prod = +1
    w3 = -1 if n % 9 in (1, 3, 6, 8) else 1
    assert w3 == -1
    assert l % 3 == 1
    w = -w3 * 1
    assert w == 1
    # cubic residue symbol, two independent evaluations
    e = (l - 1) // 3
    r1 = pow(3, e, l)
    r2 = modexp_loop(3, e, l)
    assert r1 == r2
    assert pow(r1, 3, l) == 1  # sanity: value is a cube root of unity mod l
    is1 = (r1 == 1)
    h3 = 2 if is1 else 1  # Lemma 2.5: h3(12l)=2 iff symbol=1 (rank>=1 always)
    verdict = "OPEN (obstruction silent)" if is1 else "PROVED NON-CUBE-SUM"
    if not is1:
        witnesses.append(l)
    print(f"{l:>6} {n:>6} {n % 9:>4} {str(cf):>9} {w:>+5} "
          f"{r1:>18} {str(is1):>11} {h3:>8} {verdict}")

print("proved non-cube-sum witnesses (6):", witnesses)
assert witnesses == [2113, 2239, 2293, 2311, 2347, 2437]
print("ALL CHECKS PASSED")
