"""Replayable census: maximal prime-quadruplet (0,2,6,8) gap + Legendre-square
occupancy to 5e6. Stdlib only. Prints VERIFY_OK on full agreement."""
import math

N = 5000000
H4 = 4.151180863656573  # Hardy-Littlewood prime-quadruplet constant
C4 = 1.0 / H4

def build():
    is_prime = bytearray(b'\x01') * (N + 1)
    is_prime[0:2] = b'\x00\x00'
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i*i:N+1:i] = b'\x00' * (((N - i*i) // i) + 1)
    quads = [p for p in range(2, N - 7)
             if is_prime[p] and is_prime[p+2] and is_prime[p+6] and is_prime[p+8]]
    return is_prime, quads

def mr_prime(n):
    if n < 2: return False
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 7, 61):
        if a >= n: continue
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

def main():
    is_prime, quads = build()
    assert len(quads) == 546, len(quads)
    assert quads[0] == 5 and quads[-1] == 4997381
    gaps = [(quads[i+1]-quads[i], quads[i], quads[i+1]) for i in range(len(quads)-1)]
    Gmax = max(g[0] for g in gaps)
    assert Gmax == 56910
    assert sum(1 for g in gaps if g[0] == Gmax) == 1
    q1, q2 = 3741161, 3798071
    assert (Gmax, q1, q2) in gaps
    for v in (q1, q1+2, q1+6, q1+8, q2, q2+2, q2+6, q2+8):
        assert mr_prime(v) and is_prime[v], v
    # Kourbatov estimator at x=q2: a=C4 log^4 x, T0=a log(x/a); residual R=(G-T0)/a
    x = q2
    a = C4 * math.log(x) ** 4
    T0 = a * math.log(x / a)
    R0 = (Gmax - T0) / a
    assert abs(a - 12690.52) < 1.0, a
    assert abs(T0 - 72353.6) < 5.0, T0
    assert abs(R0 - (-1.2169)) < 0.005, R0
    # Legendre-square binning over n=1..2235
    occ = {}
    for p in quads:
        occ.setdefault(math.isqrt(p), []).append(p)
    K = sum(1 for n in range(1, 2236) if n in occ)
    assert K == 478, K
    inside = [p for p in quads if 187**2 <= p <= 209**2]
    assert inside == [], inside
    assert occ.get(186) == [34841] and occ.get(209) == [43781]
    cur = 0; start = None; best = (0, -1, 0)
    for n in range(1, 2236):
        if n in occ:
            if cur > best[2]: best = (start, n - 1, cur)
            cur = 0; start = None
        else:
            if cur == 0: start = n
            cur += 1
    if cur > best[2]: best = (start, 2235, cur)
    assert (best[0], best[2]) == (187, 22), best
    assert (best[0]**2, (best[1]+1)**2) == (34969, 43681)
    # HL expected occupancy: E_n=(2n+1)*H4/log^4(mid); totals
    tot = sum((2*n+1)*H4/math.log((n*n+(n+1)*(n+1))/2)**4 for n in range(1, 2236))
    expocc = sum(1-math.exp(-(2*n+1)*H4/math.log((n*n+(n+1)*(n+1))/2)**4) for n in range(1, 2236))
    assert abs(tot - 538.45) < 1.0, tot
    assert abs(expocc - 461.40) < 1.0, expocc
    print(f"quads=546 Gmax=56910 witness=({q1},{q2}) a={a:.2f} T0={T0:.2f} R0={R0:.4f}")
    print(f"K=478 E=22 witness=[34969,43681] HLexp_total={tot:.2f} HLexp_occ={expocc:.2f}")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
