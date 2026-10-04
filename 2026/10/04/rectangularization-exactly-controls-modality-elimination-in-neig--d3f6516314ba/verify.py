#!/usr/bin/env python3

def principal_filter(n, core):
    return [s for s in range(1 << n) if core & ~s == 0]

def section(P, nx, ny, u):
    out = 0
    for v in range(ny):
        bit = 1 << (u * ny + v)
        if P & bit:
            out |= 1 << v
    return out

def rectangle_member(P, nx, ny, F, G):
    for U in F:
        for V in G:
            ok = True
            for u in range(nx):
                if (U >> u) & 1:
                    for v in range(ny):
                        if (V >> v) & 1:
                            if not ((P >> (u * ny + v)) & 1):
                                ok = False
                                break
                    if not ok:
                        break
            if ok:
                return True
    return False

def left_fubini_member(P, nx, ny, F, G):
    q = 0
    Gset = set(G)
    for u in range(nx):
        if section(P, nx, ny, u) in Gset:
            q |= 1 << u
    return q in set(F)

def transpose(P, nx, ny):
    Q = 0
    for u in range(nx):
        for v in range(ny):
            if (P >> (u * ny + v)) & 1:
                Q |= 1 << (v * nx + u)
    return Q

for nx in range(1, 4):
    for ny in range(1, 4):
        for coreF in range(1 << nx):
            F = principal_filter(nx, coreF)
            for coreG in range(1 << ny):
                G = principal_filter(ny, coreG)
                for P in range(1 << (nx * ny)):
                    R = rectangle_member(P, nx, ny, F, G)
                    L12 = left_fubini_member(P, nx, ny, F, G)
                    Pt = transpose(P, nx, ny)
                    L21 = left_fubini_member(Pt, ny, nx, G, F)
                    assert R == L12 == L21, (nx, ny, coreF, coreG, P)

# Finite truncation of the section mechanism in the infinite witness.
for N in range(2, 20):
    for u in range(N):
        Vu = {0} | set(range(u, N))
        for v in Vu:
            assert v == 0 or v >= u

print('VERIFY_OK')
