from functools import lru_cache

def partitions(n, maxpart=None):
    if n == 0:
        yield ()
        return
    if maxpart is None or maxpart > n:
        maxpart = n
    for p in range(maxpart, 0, -1):
        for rest in partitions(n-p, p):
            yield (p,) + rest

def elements(part):
    return [(i,j) for i,s in enumerate(part) for j in range(s)]

def partial_iso(pairs):
    for x,y in pairs:
        for x2,y2 in pairs:
            if (x == x2) != (y == y2):
                return False
            if (x[0] == x2[0]) != (y[0] == y2[0]):
                return False
    return True

def duplicator_wins(A,B,q):
    EA, EB = elements(A), elements(B)
    @lru_cache(None)
    def rec(pairs_t, rounds):
        pairs = list(pairs_t)
        if rounds == 0:
            return True
        for side, src, dst in ((0,EA,EB),(1,EB,EA)):
            for x in src:
                ok = False
                for y in dst:
                    nxt = pairs + ([(x,y)] if side == 0 else [(y,x)])
                    if partial_iso(nxt) and rec(tuple(nxt), rounds-1):
                        ok = True
                        break
                if not ok:
                    return False
        return True
    return rec(tuple(), q)

def profile_equivalent(A,B,q):
    for k in range(1,q+1):
        cap = q-k+1
        a = sum(s >= k for s in A)
        b = sum(s >= k for s in B)
        if min(a,cap) != min(b,cap):
            return False
    for k in range(1,q):
        cap = q-k
        if min(A.count(k),cap) != min(B.count(k),cap):
            return False
    return True

def main():
    parts = [p for n in range(1,9) for p in partitions(n)]
    checked = 0
    for q in range(1,5):
        for i,A in enumerate(parts):
            for B in parts[i:]:
                checked += 1
                if duplicator_wins(A,B,q) != profile_equivalent(A,B,q):
                    raise SystemExit(f"MISMATCH q={q} A={A} B={B}")
    print(f"VERIFY_OK pairs={checked}")

if __name__ == '__main__':
    main()
