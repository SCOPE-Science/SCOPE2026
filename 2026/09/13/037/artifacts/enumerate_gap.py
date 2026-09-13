"""Enumerate m=5 Kunz tuples to find min W for e=3 (uses verified formulas)."""
import itertools

def kunz_valid(k):
    k1, k2, k3, k4 = k
    return (2*k1 >= k2 and k1+k2 >= k3 and k1+k3 >= k4 and 2*k2 >= k4
            and k2+k4+1 >= k1 and 2*k3+1 >= k1 and k3+k4+1 >= k2
            and 2*k4+1 >= k3)

def atoms(k):
    k1, k2, k3, k4 = k
    a1 = (2*k3+1 > k1) and (k2+k4+1 > k1)
    a2 = (2*k1 > k2) and (k3+k4+1 > k2)
    a3 = (k1+k2 > k3) and (2*k4+1 > k3)
    a4 = (k1+k3 > k4) and (2*k2 > k4)
    return (a1, a2, a3, a4)

def cnw(k):
    k1, k2, k3, k4 = k
    w = [0, 5*k1+1, 5*k2+2, 5*k3+3, 5*k4+4]
    c = max(w) - 4
    g = sum(k)
    n = c - g
    return c, n, 3*n - c

if __name__ == "__main__":
    B = 40
    best = None
    wit = {}
    for k in itertools.product(range(1, B+1), repeat=4):
        if not kunz_valid(k):
            continue
        a = atoms(k)
        if sum(a) != 2:
            continue
        c, n, W = cnw(k)
        pat = tuple(i+1 for i, x in enumerate(a) if x)
        if pat not in wit or W < wit[pat][0]:
            wit[pat] = (W, c, n, k)
        if best is None or W < best[0]:
            best = (W, pat, k, c, n)
    print("global min e=3:", best)
    for p in sorted(wit):
        print("pattern", p, "min (W,c,n,k) =", wit[p])
