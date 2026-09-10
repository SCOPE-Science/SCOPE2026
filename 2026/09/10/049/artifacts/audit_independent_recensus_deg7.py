"""AUDITOR independent re-census of the preset-fallback family (no shared code).

Family: monic degree-7 over F_13, f(0)=0, x^6 coeff 0, a1..a5 free
  -> C=[0,a1,a2,a3,a4,a5,0,1], 13^5 = 371293 representatives.
Method: batched Vandermonde evaluation + vectorized pair-slope tallies +
  sort-based distinct-direction counts. Shares no code with direc.py.
PASS iff zero representatives determine exactly 9 directions.
"""
import numpy as np

P = 13
XS = np.arange(P, dtype=np.int64)
PAIRS = [(x, y) for x in range(P) for y in range(x + 1, P)]
DXINV = np.array([pow((x - y) % P, -1, P) for (x, y) in PAIRS], dtype=np.int64)
XI = np.array([x for (x, y) in PAIRS])
YI = np.array([y for (x, y) in PAIRS])
XPOW = np.stack([XS ** e % P for e in range(8)], axis=1)  # (13,8)


def main():
    total = 13 ** 5
    assert total == 371293
    hist = {}
    n9 = 0
    first_survivors = []
    B = 2048
    for start in range(0, total, B):
        end = min(start + B, total)
        idx = np.arange(start, end, dtype=np.int64)
        tmp = idx.copy()
        C = np.zeros((end - start, 8), dtype=np.int64)
        C[:, 7] = 1  # monic x^7; col 6 (x^6) and col 0 (a0) stay 0
        for j in range(5):  # cols 1..5 = a1..a5
            C[:, 1 + j] = tmp % 13
            tmp //= 13
        F = (C @ XPOW.T) % P  # (B,13) function values
        S = ((F[:, XI] - F[:, YI]) * DXINV[None, :]) % P  # (B,78) slopes
        S.sort(axis=1)
        ns = (np.diff(S, axis=1) != 0).sum(axis=1) + 1
        for k, n in enumerate(ns):
            n = int(n)
            hist[n] = hist.get(n, 0) + 1
            if n == 9:
                n9 += 1
                if len(first_survivors) < 5:
                    first_survivors.append((start + k, C[k, :].tolist()))
    print("total", total, "hist", dict(sorted(hist.items())), "n9", n9)
    assert sum(hist.values()) == total
    if n9 == 0:
        print("AUDIT_RECENSUS_OK")
    else:
        print("SURVIVORS", first_survivors)
        print("AUDIT_RECENSUS_FAIL")


if __name__ == "__main__":
    main()
