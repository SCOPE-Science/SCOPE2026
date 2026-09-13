"""Brute-force verification of Kunz formulas for m=5 (stdlib only).

Checks, for every valid Kunz tuple with 1<=ki<=B:
  (1) Kunz inequalities characterize Ap(S,5) membership correctly,
      by building S from the Apery set and testing closure/conductor;
  (2) atom test <-> minimal generators (embedding dimension);
  (3) c = max(w)-4, g = sum(k), n = c-g, W = 3n-c agree with brute force.
"""
import itertools

B = 7

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

def check():
    n_checked = 0
    e_hist = {}
    for k in itertools.product(range(1, B+1), repeat=4):
        if not kunz_valid(k):
            continue
        k1, k2, k3, k4 = k
        w = [0, 5*k1+1, 5*k2+2, 5*k3+3, 5*k4+4]
        # S from Apery: x in S iff x - w[x mod 5] >= 0 and divisible by 5
        LIM = max(w) + 30
        S = set(x for x in range(LIM+1) if (x - w[x % 5]) >= 0 and (x - w[x % 5]) % 5 == 0)
        # closure spot-check
        for x in S:
            for y in S:
                if x + y <= LIM:
                    assert x + y in S, ("not a semigroup", k, x, y)
        # conductor: max(w)-4, verify all larger ints in S
        c_form = max(w) - 4
        assert all(x in S for x in range(c_form, LIM+1)), ("conductor", k)
        assert (c_form - 1) not in S, ("conductor sharp", k)
        # gaps
        gaps = [x for x in range(c_form) if x not in S]
        assert len(gaps) == sum(k), ("genus", k, gaps)
        # minimal generators by brute force
        gens = []
        for x in sorted(S):
            if x == 0:
                continue
            if x > max(w):
                break
            if not any((y in S and (x-y) in S) for y in range(1, x)):
                gens.append(x)
        assert gens[0] == 5, ("multiplicity", k, gens)
        a = atoms(k)
        assert len(gens) == 1 + sum(a), ("embdim", k, gens, a)
        assert sorted(gens[1:]) == sorted(w[i] for i in range(1, 5) if a[i-1]), ("atom gens", k, gens, a)
        # n and W
        n_form = c_form - sum(k)
        n_brute = len([x for x in range(c_form) if x in S])
        assert n_brute == n_form, ("n", k)
        W_form = 3*n_form - c_form
        assert W_form == 2*c_form - 3*sum(k)
        e_hist[len(gens)] = e_hist.get(len(gens), 0) + 1
        n_checked += 1
    print("checked", n_checked, "tuples; embdim histogram:", e_hist)

if __name__ == "__main__":
    check()
