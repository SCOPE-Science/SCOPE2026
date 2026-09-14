"""Step 1: fix explicit triple for passport (4-2-1^6, 5-4-3, 7-3-2), verify.
Convention: perms are 0-indexed image arrays; compose(a,b)[i] = b[a[i]]
(apply a first). Triple condition: compose(compose(v0,v1),vinf) == identity.
"""
import json

N = 12

def compose(a, b):
    return [b[a[i]] for i in range(len(a))]

def inv(a):
    b = [0]*len(a)
    for i, v in enumerate(a):
        b[v] = i
    return b

def ident(n=N):
    return list(range(n))

def perm_from_cycles(cycles, n=N):
    p = list(range(n))
    for c in cycles:
        for i in range(len(c)):
            p[c[i]] = c[(i+1) % len(c)]
    return p

def cycles_of(p):
    seen = [False]*len(p); out = []
    for i in range(len(p)):
        if not seen[i]:
            j = i; c = []
            while not seen[j]:
                seen[j] = True; c.append(j); j = p[j]
            if len(c) > 1:
                out.append(c)
    return out

def cycle_type(p):
    t = sorted((len(c) for c in cycles_of(p)), reverse=True)
    # include 1s
    s = sum(t); t += [1]*(len(p)-s)
    return tuple(sorted(t, reverse=True))

def to_1indexed_cycles(p):
    return [[x+1 for x in c] for c in cycles_of(p)]

def is_transitive(a, b, n=N):
    ai, bi = inv(a), inv(b)
    seen = [False]*n; stack = [0]; seen[0] = True
    while stack:
        i = stack.pop()
        for nb in (a[i], b[i], ai[i], bi[i]):
            if not seen[nb]:
                seen[nb] = True; stack.append(nb)
    return all(seen)

def sign_of(p):
    # sign = (-1)^(n - #cycles incl fixed)
    seen = [False]*len(p); ncyc = 0
    for i in range(len(p)):
        if not seen[i]:
            ncyc += 1; j = i
            while not seen[j]:
                seen[j] = True; j = p[j]
    return 1 if ((len(p)-ncyc) % 2 == 0) else -1

# canonical v0 of type 4-2-1^6
v0 = perm_from_cycles([[0,1,2,3],[4,5]])
# v1 from randomized search hit (type 5-4-3)
v1 = [11,10,4,5,7,9,3,2,6,8,0,1]
v01 = compose(v0, v1)
vinf = inv(v01)

print("type(v0)  =", cycle_type(v0))
print("type(v1)  =", cycle_type(v1))
print("type(vinf)=", cycle_type(vinf))
print("product==id:", compose(v01, vinf) == ident())
print("transitive:", is_transitive(v0, v1))
print("signs:", sign_of(v0), sign_of(v1), sign_of(vinf))
print("v0   (1-idx):", to_1indexed_cycles(v0))
print("v1   (1-idx):", to_1indexed_cycles(v1))
print("vinf (1-idx):", to_1indexed_cycles(vinf))

# Riemann-Hurwitz check
parts = [len(cycle_type(v0)), len(cycle_type(v1)), len(cycle_type(vinf))]
chi = -2*N + sum(N-p for p in parts)
print("parts:", parts, "sum:", sum(parts), "2g-2 =", chi, "-> g =", chi//2+1)

assert cycle_type(v0) == (4,2,1,1,1,1,1,1)
assert cycle_type(v1) == (5,4,3)
assert cycle_type(vinf) == (7,3,2)
assert compose(v01, vinf) == ident()
assert is_transitive(v0, v1)
assert sum(parts) == 14 and chi == -2

with open("triple.json", "w") as f:
    json.dump({
        "n": N,
        "convention": "0-indexed image arrays; compose(a,b)[i]=b[a[i]]; v0*v1*vinf=id",
        "v0": v0, "v1": v1, "vinf": vinf,
        "v0_cycles_1idx": to_1indexed_cycles(v0),
        "v1_cycles_1idx": to_1indexed_cycles(v1),
        "vinf_cycles_1idx": to_1indexed_cycles(vinf),
    }, f)
print("wrote triple.json")
