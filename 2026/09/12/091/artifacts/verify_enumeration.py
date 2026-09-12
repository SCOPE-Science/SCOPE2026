"""Artifact C: complete enumeration — every F2 Lagrangian admits a local pattern with
invertible X-block (the mod-2 lemma behind Part 2), and every Z4 free AME module is
torsion-8 (Part 1 cross-check on random Z4 Lagrangians incl. free ones)."""
import itertools, sys
sys.path.insert(0, '.')
from verify_reduction import (find_pattern_bruteforce, span2, s2, Z2, mod2, span4,
                              is_ame4, torsion2, symp4, add4, mul4, ZERO)
import random

def all_f2_lagrangians():
    ALL = [v for v in itertools.product((0,1), repeat=6)]
    seen = set()
    for a in ALL:
        if a == Z2:
            continue
        for b in ALL:
            if b == Z2 or b == a or s2(a, b) != 0:
                continue
            for c in ALL:
                if c == Z2 or s2(a, c) != 0 or s2(b, c) != 0:
                    continue
                S = span2([a, b, c])
                if len(S) == 8:
                    seen.add(frozenset(S))
    return seen

def rand4():
    return (random.randrange(4), random.randrange(4), random.randrange(4),
            random.randrange(4), random.randrange(4), random.randrange(4))

if __name__ == "__main__":
    L = all_f2_lagrangians()
    print("F2 Lagrangians:", len(L))
    fails = 0
    for S in L:
        S = sorted(S)
        nz = [v for v in S if v != Z2]
        # find some basis triple
        found = None
        for a in nz:
            for b in nz:
                if b == a:
                    continue
                for c in nz:
                    if c in (a, b):
                        continue
                    if len(span2([a, b, c])) == 8:
                        found = [a, b, c]
                        break
                if found:
                    break
            if found:
                break
        ops = find_pattern_bruteforce(found)
        if ops is None:
            fails += 1
    print("Lagrangians with NO good local pattern (must be 0):", fails)
    # Z4 cross-check: random Lagrangians (free and torsion) — AME => free
    random.seed(3)
    ame_free = 0
    ame_tors = 0
    n64 = 0
    for _ in range(40000):
        a = rand4()
        if a == ZERO or mul4(2, a) == ZERO:
            continue
        b = rand4()
        if b == ZERO or symp4(a, b) != 0:
            continue
        c = rand4()
        if c == ZERO or symp4(a, c) != 0 or symp4(b, c) != 0:
            continue
        S = span4([a, b, c])
        if len(S) != 64:
            continue
        n64 += 1
        if is_ame4(S):
            if torsion2(S) == 8:
                ame_free += 1
            else:
                ame_tors += 1
                print("TORSION AME FOUND!", [a, b, c])
                break
    print("Z4 Lagrangians sampled:", n64, "AME free:", ame_free, "AME torsion:", ame_tors)
    print("ENUMERATION VERIFIED" if (fails == 0 and ame_tors == 0 and ame_free > 0) else "CHECK")
