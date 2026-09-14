"""Misere Dawson's Kayles single-row P-positions 0<=n<=36.
Exhaustive misere outcome recursion with memoization over all
disjunctive sums of rows totaling at most 36 pins.
Rule: knock down adjacent pair k,k+1; neighbours k-1,k+2 (if present)
become unavailable. Misere: player unable to move WINS (last move loses).
Outcome: WIN=True means player-to-move eventually wins (N-position);
         LOSE=False means player-to-move loses (P-position).
Terminal (no legal moves in any component, incl. all-dead rows): WIN.
"""
from functools import lru_cache
import json

MAXN = 36

def single_moves(n):
    """All (L,R) pairs (lengths, zeros allowed) from a single row of length n."""
    opts = []
    for k in range(n - 1):  # k = 0..n-2 indexes left pin of struck pair
        L = k - 1
        if L < 0:
            L = 0
        R = n - k - 3
        if R < 0:
            R = 0
        opts.append((L, R))
    return opts

def canon(parts):
    return tuple(sorted(p for p in parts if p > 0))

@lru_cache(maxsize=None)
def win(state):
    """state: canonical tuple of positive row lengths. True=N, False=P (misere)."""
    found = False
    for i, n in enumerate(state):
        rest = state[:i] + state[i+1:]
        for (L, R) in single_moves(n):
            found = True
            ns = canon(rest + ((L,) if L > 0 else ()) + ((R,) if R > 0 else ()))
            assert sum(ns) < sum(state), (state, ns)  # strict decrease
            if not win(ns):
                return True
    if not found:
        return True  # terminal incl. (), (0..), (1,), (1,1..): player to move wins
    return False

def main():
    singles = [None]*(MAXN+1)
    for n in range(MAXN+1):
        singles[n] = win((n,) if n > 0 else ())
    P = [n for n in range(MAXN+1) if not singles[n]]
    N = [n for n in range(MAXN+1) if singles[n]]
    print("P =", P)
    print("N =", N)
    print("states evaluated:", win.cache_info())
    # hand-check small cases
    # n=0: terminal -> N(True); n=1: terminal -> N(True)
    # n=2: only move to () which is N -> P(False). verify:
    print("win(())=", win(()), "win((1,))=", win((1,)), "win((2,))=", win((2,)), "win((3,))=", win((3,)))
    cert = {}
    for n in range(MAXN+1):
        opts = single_moves(n)
        if len(opts) == 0:
            assert win((n,) if n > 0 else ()) is True
            cert[str(n)] = {"outcome": "N", "reason": "terminal: no adjacent pair exists; player to move wins (misere)"}
        elif not singles[n]:
            det = []
            seen = set()
            for (L, R) in opts:
                s = canon(((L,) if L > 0 else ())+((R,) if R > 0 else ()))
                if s in seen:
                    continue
                seen.add(s)
                assert win(s) is True
                det.append({"move": [L, R], "sum": list(s), "sum_outcome": "N"})
            cert[str(n)] = {"outcome": "P", "distinct_options": det}
        else:
            wit = None
            for (L, R) in opts:
                s = canon(((L,) if L > 0 else ())+((R,) if R > 0 else ()))
                if not win(s):
                    wit = {"move": [L, R], "sum": list(s)}
                    break
            assert wit is not None
            cert[str(n)] = {"outcome": "N", "winning_move": wit}
    with open("output/artifacts/outcomes.json", "w") as f:
        json.dump({"P": P, "N": N,
                   "singles_win": {str(n): bool(singles[n]) for n in range(MAXN+1)}}, f, indent=1)
    with open("output/artifacts/certificate.json", "w") as f:
        json.dump(cert, f, indent=1)
    print("done")

if __name__ == "__main__":
    main()
