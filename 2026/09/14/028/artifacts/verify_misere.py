import json
from functools import lru_cache
from collections import deque

def sm(n):
    return [(max(k-1,0), max(n-k-3,0)) for k in range(n-1)]

def canon(ps):
    return tuple(sorted(p for p in ps if p > 0))

@lru_cache(maxsize=None)
def win(s):
    f = False
    for i, n in enumerate(s):
        r = s[:i] + s[i+1:]
        for L, R in sm(n):
            f = True
            ns = canon(r + ((L,) if L > 0 else ()) + ((R,) if R > 0 else ()))
            assert sum(ns) < sum(s)
            if not win(ns):
                return True
    return True if not f else False

reach = set([(), ] + [(n,) if n > 0 else () for n in range(37)])
q = deque(reach)
while q:
    s = q.popleft()
    for i, n in enumerate(s):
        r = s[:i] + s[i+1:]
        for L, R in sm(n):
            ns = canon(r + ((L,) if L > 0 else ()) + ((R,) if R > 0 else ()))
            if ns not in reach:
                reach.add(ns)
                q.append(ns)
print("reachable states:", len(reach))
print("max total:", max(sum(s) for s in reach))

order = sorted(reach, key=sum)
memo = {}
for s in order:
    f = any(True for _ in [1 for i, n in enumerate(s) for _ in sm(n)])
    if not f:
        memo[s] = True
    else:
        w = False
        for i, n in enumerate(s):
            r = s[:i] + s[i+1:]
            for L, R in sm(n):
                ns = canon(r + ((L,) if L > 0 else ()) + ((R,) if R > 0 else ()))
                assert ns in memo
                if memo[ns] is False:
                    w = True
                    break
            if w:
                break
        memo[s] = w
    assert memo[s] == win(s), (s, memo[s], win(s))
print("bottom-up agrees with recursion on all reachable states")
P = [n for n in range(37) if memo[(n,) if n > 0 else ()] is False]
print("P=", P)
cert = json.load(open("output/artifacts/certificate.json"))
out = json.load(open("output/artifacts/outcomes.json"))
assert out["P"] == P, (out["P"], P)
for n in range(37):
    c = cert[str(n)]
    if len(sm(n)) == 0:
        assert c["outcome"] == "N" and memo[(n,) if n > 0 else ()] is True
    elif memo[(n,) if n > 0 else ()] is False:
        assert c["outcome"] == "P"
        seen = set()
        for L, R in sm(n):
            s = canon(((L,) if L > 0 else ()) + ((R,) if R > 0 else ()))
            if s in seen:
                continue
            seen.add(s)
            assert memo[s] is True, (n, L, R, s)
        assert len(c["distinct_options"]) == len(seen)
    else:
        assert c["outcome"] == "N"
        L, R = c["winning_move"]["move"]
        s = canon(((L,) if L > 0 else ()) + ((R,) if R > 0 else ()))
        assert memo[s] is False, (n, s)
print("certificate fully verified against bottom-up table")
