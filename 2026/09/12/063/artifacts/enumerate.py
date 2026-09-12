"""Exhaustive enumeration of 10-fold symmetric rotation systems of K(4,10).

Setup: A={0,1,2,3}, B=Z_10. g(b_i)=b_{i+1}, g(a_j)=a_{phi(j)}.
Symmetric rotation systems determined by rotB[0] (6 cyclic orders) and,
per phi-orbit of length k on A, a cyclic order L of Z_10 with L+k == L
cyclically (consistency around the orbit).
"""
import itertools, json, sys

def canonical_starts_zero(n=10):
    rest = list(range(1, n))
    for p in itertools.permutations(rest):
        yield (0,) + tuple(p)

def shift(L, s, mod=10):
    return tuple((x + s) % mod for x in L)

def is_shift_invariant(L, k):
    """Check shift(L,k) equals L up to rotation, O(n)."""
    n = len(L)
    S = shift(L, k)
    # find rotation offset: position in S of L[0]
    r = S.index(L[0])
    for i in range(n):
        if S[(r + i) % n] != L[i]:
            return False
    return True

def invariant_orders(k):
    return [L for L in canonical_starts_zero() if is_shift_invariant(L, k)]

def face_data(rotA, rotB):
    na, nb = len(rotA), len(rotB)
    nxtA = []
    for j in range(na):
        L = rotA[j]; n = len(L); d = {}
        for t, b in enumerate(L):
            d[b] = L[(t + 1) % n]
        nxtA.append(d)
    nxtB = []
    for i in range(nb):
        L = rotB[i]; n = len(L); d = {}
        for t, a in enumerate(L):
            d[a] = L[(t + 1) % n]
        nxtB.append(d)
    seen = set(); faces = []
    for j in range(na):
        for b in range(nb):
            if (0, j, b) in seen:
                continue
            cur = (0, j, b); cyc = []
            while cur not in seen:
                seen.add(cur); cyc.append(cur)
                if cur[0] == 0:
                    _, j2, b2 = cur
                    j3 = nxtB[b2][j2]
                    cur = (1, b2, j3)
                else:
                    _, b2, j2 = cur
                    b3 = nxtA[j2][b2]
                    cur = (0, j2, b3)
            faces.append(cyc)
    return faces

def same_cyclic(A, B):
    n = len(A)
    return any(all(A[(r + t) % n] == B[t] for t in range(n)) for r in range(n))

def check_symmetric(rotA, rotB, phi):
    # g orientation-preserving: rotB[i+1] = phi(rotB[i]); rotA[phi(j)] = shift(rotA[j],1)
    # rotation systems are cyclic orders -> compare up to rotation
    for i in range(10):
        if not same_cyclic(tuple(phi[a] for a in rotB[i]), tuple(rotB[(i + 1) % 10])):
            return False
    for j in range(4):
        if not same_cyclic(shift(rotA[j], 1), tuple(rotA[phi[j]])):
            return False
    return True

def phi_reps():
    ident = [0, 1, 2, 3]
    trans = [1, 0, 2, 3]          # (01)
    doub = [1, 0, 3, 2]           # (01)(23)
    three = [1, 2, 0, 3]          # (012)
    four = [1, 2, 3, 0]           # (0123)
    return {'id': ident, 'transposition': trans, 'double-transposition': doub,
            '3-cycle': three, '4-cycle': four}

def orbits(phi):
    seen = []; out = []
    for j in range(4):
        if any(j in o for o in out):
            continue
        o = [j]; k = phi[j]
        while k != j:
            o.append(k); k = phi[k]
        out.append(o)
    return out

def b0_orders_valid(phi):
    out = []
    for p in itertools.permutations([1, 2, 3]):
        b0 = (0,) + tuple(p)
        cur = b0
        for _ in range(10):
            cur = tuple(phi[a] for a in cur)
        # closure: phi^10(b0) must equal b0 as cyclic order
        if same_cyclic(cur, b0):
            out.append(b0)
    return out

def main():
    inv = {}
    for k in (1, 2, 3, 4):
        inv[k] = invariant_orders(k)
        print(f'k={k}: {len(inv[k])} invariant cyclic orders', flush=True)
    report = {}
    total_checked = 0
    for name, phi in phi_reps().items():
        orbs = orbits(phi)
        per_orbit = [inv[len(o)] for o in orbs]
        ncomb = 6
        for p in per_orbit:
            ncomb *= len(p)
        quad_examples = []
        n_min_genus = 0
        b0list = b0_orders_valid(phi)
        for b0 in b0list:
            rotB = [None] * 10
            rotB[0] = list(b0)
            for i in range(1, 10):
                rotB[i] = [phi[a] for a in rotB[i - 1]]
            for combo in itertools.product(*per_orbit):
                rotA = [None] * 4
                for (o, L) in zip(orbs, combo):
                    for t, j in enumerate(o):
                        rotA[j] = list(shift(L, t))
                assert check_symmetric(rotA, rotB, phi), 'symmetry broken!'
                total_checked += 1
                faces = face_data(rotA, rotB)
                F = len(faces)
                # states per face == darts per face == boundary length; quad <=> 4
                if F == 20 and all(len(f) == 4 for f in faces):
                    n_min_genus += 1
                    if len(quad_examples) < 3:
                        quad_examples.append(
                            {'rotA': [list(r) for r in rotA],
                             'rotB': [list(r) for r in rotB]})
        report[name] = {'phi': phi, 'orbits': orbs, 'combos': ncomb,
                        'n_b0': len(b0list), 'min_genus_count': n_min_genus,
                        'examples': quad_examples}
        print(f'{name}: n_b0={len(b0list)} combos={ncomb} min-genus={n_min_genus}', flush=True)
    print(f'TOTAL checked: {total_checked}', flush=True)
    with open('output/artifacts/enumeration_10cycle.json', 'w') as f:
        json.dump(report, f)
    # summary for log
    with open('output/artifacts/enumeration_10cycle_summary.txt', 'w') as f:
        for name, r in report.items():
            f.write(f"{name}: combos={r['combos']} min-genus={r['min_genus_count']}\n")
        f.write(f'TOTAL checked: {total_checked}\n')

if __name__ == '__main__':
    main()
