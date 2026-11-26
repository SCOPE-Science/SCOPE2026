"""One-atom depth types and exact validity on small path/loop witnesses."""


def path(j, loop):
    return tuple((i+1,) for i in range(j)) + (((j,) if loop else ()),)


def depth_types(R, V, d):
    row = [bool(V & (1<<i)) for i in range(len(R))]
    for _ in range(d):
        row = [(bool(V & (1<<i)), frozenset(row[t] for t in R[i])) for i in range(len(R))]
    return row


def all_types(components, d):
    return {t for R in components for V in range(1<<len(R)) for t in depth_types(R, V, d)}


def diamond(R, X, j):
    for _ in range(j):
        X = {i for i, N in enumerate(R) if any(t in X for t in N)}
    return X


def validates(components, h):
    if h == 0:
        return not any(N for R in components for N in R)
    for R in components:
        U = set(range(len(R)))
        for V in range(1<<len(R)):
            X = {i for i in U if V & (1<<i)}
            if diamond(R, X, h-1) & diamond(R, U-X, h) & diamond(R, U, h+1):
                return False
    return True


for h in range(7):
    G = (path(h, False),) if h == 0 else (path(h, False), path(h-1, True))
    F = G+(path(h, True),)
    assert all_types(G,h) == all_types(F,h)
    assert all_types(G,h+1) < all_types(F,h+1)
    assert validates(G,h) and not validates(F,h)
print('PASS: seven frame-level pairs, depth-h one-atom types and exact separators')
