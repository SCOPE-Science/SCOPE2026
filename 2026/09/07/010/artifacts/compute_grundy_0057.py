"""Deterministic Sprague-Grundy computation for octal game 0.057.

Rules (d1=0, d2=5=101, d3=7=111, m=3):
  G(0) = 0.
  n=1: no moves -> 0.
  n>=2 take-2: if n==2: reachable += {0} (terminal whole-heap removal).
               else: splits a+b=n-2, a,b>=1 -> G[a]^G[b].
  n>=3 take-3: if n==3: reachable += {0} (terminal).
               else: singleton G[n-3] plus splits a+b=n-3 -> G[a]^G[b].
  G(n) = mex(reachable).
No randomness. Uses numpy vectorization for splits (C-speed), Python loop over n.
"""
import sys
import time
import numpy as np


def compute_grundy(Nmax: int):
    G = np.zeros(Nmax + 1, dtype=np.int64)
    t0 = time.time()
    for n in range(1, Nmax + 1):
        seen = bytearray(64)
        if n >= 2:
            if n == 2:
                seen[0] = 1
            else:
                S = n - 2
                if S >= 2:
                    idx = np.arange(1, S, dtype=np.int64)
                    x = G[idx] ^ G[S - idx]
                    for v in np.unique(x):
                        if int(v) < 64:
                            seen[int(v)] = 1
                        else:
                            raise RuntimeError("large xor %r at n=%d" % (v, n))
        if n >= 3:
            if n == 3:
                seen[0] = 1
            else:
                v = int(G[n - 3])
                assert v < 64
                seen[v] = 1
                S = n - 3
                if S >= 2:
                    idx = np.arange(1, S, dtype=np.int64)
                    x = G[idx] ^ G[S - idx]
                    for v in np.unique(x):
                        if int(v) < 64:
                            seen[int(v)] = 1
                        else:
                            raise RuntimeError("large xor %r at n=%d" % (v, n))
        g = 0
        while g < 64 and seen[g]:
            g += 1
        if g == 64:
            raise RuntimeError("Grundy overflow at n=%d" % n)
        G[n] = g
    dt = time.time() - t0
    return G, dt


def main():
    Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    out = sys.argv[2] if len(sys.argv) > 2 else None
    G, dt = compute_grundy(Nmax)
    print("Nmax=%d time=%.2fs maxG=%d uniq=%s" % (Nmax, dt, int(G.max()), sorted(map(int, np.unique(G)))))
    print("G[0..40]: " + str(list(map(int, G[:41]))))
    if out:
        import csv
        with open(out, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["heap", "grundy"])
            for n in range(Nmax + 1):
                w.writerow([n, int(G[n])])
        print("wrote %s" % out)


if __name__ == "__main__":
    main()
