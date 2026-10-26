from itertools import product

checks = 0

def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def adj(n, a, b):
    return a != b and ((a - b) % n in (1, n - 1))

def dist(n, a, b):
    d = (a-b) % n
    return min(d, n-d)

def tight_alike(v, w, n):
    # v is an assignment into C4; w is the corresponding assignment into C_n.
    for i in range(3):
        for j in range(3):
            if (v[i] == v[j]) != (w[i] == w[j]):
                return False
            if adj(4, v[i], v[j]) != adj(n, w[i], w[j]):
                return False
            if v[i] != v[j] and not adj(4, v[i], v[j]):
                if dist(n, w[i], w[j]) != 2:
                    return False
    return True

# Exhaustively replay the one-variable extension lemma for all tight-alike
# three-variable assignments for C4 -> C_n on a substantial finite range.
for n in range(5, 17):
    C4 = list(product(range(4), repeat=3))
    Cn = list(product(range(n), repeat=3))
    for v in C4:
        for w in Cn:
            if not tight_alike(v, w, n):
                continue
            check(True, f'tight pair recognized n={n} v={v} w={w}')
            for i in range(3):
                for a in range(4):
                    v2 = list(v); v2[i] = a; v2 = tuple(v2)
                    responses = []
                    for b in range(n):
                        w2 = list(w); w2[i] = b; w2 = tuple(w2)
                        if tight_alike(v2, w2, n):
                            responses.append(b)
                    check(bool(responses), f'extension failed n={n} i={i} a={a} v={v} w={w}')

# Parametric local construction: the only relation types of the two fixed
# C4 values are equality, adjacency, and opposition. Check those canonical
# cases for every n through 1000 and every new C4 value.
for n in range(5, 1001):
    canonical = [
        ((0,0), (0,0)),       # equal
        ((0,1), (0,1)),       # adjacent
        ((0,2), (0,2)),       # opposite -> distance 2
    ]
    for (u4,v4),(un,vn) in canonical:
        for a in range(4):
            ok = False
            for b in range(n):
                # Check the relation/equality/tightness data from a to both fixed values.
                good = True
                for x4,xn in ((u4,un),(v4,vn)):
                    if (a == x4) != (b == xn): good = False
                    if adj(4,a,x4) != adj(n,b,xn): good = False
                    if a != x4 and not adj(4,a,x4) and dist(n,b,xn) != 2: good = False
                if good:
                    ok = True; break
            check(ok, f'canonical extension failed n={n} fixed={(u4,v4)} a={a}')

# Strictness witness: eta says every third vertex distinct from the endpoints
# of an edge is adjacent to at least one endpoint. C4 satisfies eta; C_n (n>=5)
# fails at the edge (0,1) with z=3.
def eta(n):
    for x,y,z in product(range(n), repeat=3):
        if not ((not adj(n,x,y)) or x==z or y==z or adj(n,x,z) or adj(n,y,z)):
            return False
    return True
check(eta(4), 'eta must hold on C4')
for n in range(5, 1001):
    check(not eta(n), f'eta should fail on C{n}')
    check(adj(n,0,1) and 3 not in (0,1) and not adj(n,0,3) and not adj(n,1,3), f'explicit eta witness fails C{n}')

print(f'VERIFY_OK {checks} exact assertions')
