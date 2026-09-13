# Search for a finite quotient of G3 separating u=R^3 from v=a R^3 a^-1.
# Strategy: enumerate homomorphisms G3 -> S_n by choosing images of (a,b,c) as
# permutations with R(a,b,c)^6 = id, then check u,v images distinct.
# R(a,b,c) = A B^-1 A B C^2 as a permutation product (left-to-right application).
import itertools

def compose(p, q):
    # apply p then q: (p*q)(i) = q(p(i))
    return tuple(q[p[i]] for i in range(len(p)))

def invert(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return tuple(q)

def pw(p, k):
    n = len(p)
    e = tuple(range(n))
    if k < 0:
        p, k = invert(p), -k
    r = e
    for _ in range(k):
        r = compose(r, p)
    return r

def word_R(A, B, C):
    return compose(compose(compose(compose(pw(A, 1), pw(B, -1)), pw(A, 1)), pw(B, 1)), pw(C, 2))

def all_perms(n):
    return list(itertools.permutations(range(n)))

def find(n, max_show=5, cap_images_a=None):
    perms = all_perms(n)
    ident = tuple(range(n))
    found = []
    # iterate a,b,c; constrain a to small set if given
    Aset = perms if cap_images_a is None else cap_images_a
    for A in Aset:
        Ai = invert(A)
        for B in perms:
            for C in perms:
                R = word_R(A, B, C)
                if pw(R, 6) != ident:
                    continue
                u = pw(R, 3)
                v = compose(compose(A, u), Ai)
                if u != v:
                    found.append((A, B, C, u, v, R))
                    if len(found) >= max_show:
                        return found
    return found

for n in (3, 4):
    f = find(n, max_show=3)
    print(f"S_{n}: {len(f)} separating reps found (showing up to 3)")
    for A, B, C, u, v, R in f:
        print("  A=", A, "B=", B, "C=", C)
        print("  R =", R, "R^6=e:", pw(R, 6) == tuple(range(n)))
        print("  u=R^3:", u, " v=a u a^-1:", v, " distinct:", u != v)
        break
