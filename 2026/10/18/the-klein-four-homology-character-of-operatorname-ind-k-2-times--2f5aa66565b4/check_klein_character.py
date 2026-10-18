"""Finite direct checks of Klein-four Lefschetz characters.

Only Python's standard library is used. The theorem for all q is proved
in RESULT.md; finite enumeration here is an independent diagnostic.
"""
from itertools import product
from math import comb


def beta(q):
    return (q - 1) ** 2 * (q * q - 2) // 2


def expected(q):
    return (beta(q), (q - 1) ** 2, -(q - 1) ** 2, 1 - q)


def direct(q):
    """Enumerate every 2^(2q^2) vertex subset at q=2,3.

    For each invariant independent face, add (-1)^#vertex_orbits to
    the reduced H_3 character, equivalent to the signed chain trace.
    """
    vv = list(product(range(2), range(q), range(q)))
    N = len(vv)
    perms = []
    for mode in range(4):
        images = []
        for a, i, j in vv:
            if mode & 1:
                a = 1 - a
            if mode & 2:
                i, j = j, i
            images.append(vv.index((a, i, j)))
        perms.append(images)
    edge_masks = [0] * N
    for u, (a,i,j) in enumerate(vv):
        for v, (b,k,l) in enumerate(vv):
            if a != b and i != k and j != l:
                edge_masks[u] |= 1 << v
    out = [0] * 4
    valid = 0
    for face in range(1 << N):
        good = True
        f = face
        while f:
            bit = f & -f
            f -= bit
            u = bit.bit_length() - 1
            if edge_masks[u] & face:
                good = False
                break
        if not good:
            continue
        valid += 1
        for mode, perm in enumerate(perms):
            image = 0
            orbit_count = 0
            remaining = face
            while remaining:
                bit = remaining & -remaining
                orbit_count += 1
                index = bit.bit_length() - 1
                k = index
                while True:
                    image |= 1 << k
                    remaining &= ~(1 << k)
                    k = perm[k]
                    if k == index:
                        break
            if image == face:
                out[mode] += (-1) ** orbit_count
    return valid, tuple(out)


def swapped_coordinates_signed_independence(q):
    """Enumerate t-orbit selections using their cross-sheet graph.

    The first and second parts each have q+comb(q,2) orbit-vertices.
    Independent sets of the bipartite quotient are counted at -1 by
    summing over every subset U of the first part: a contribution occurs
    exactly when U dominates every orbit in the opposite part.
    """
    orbits = [(i,i) for i in range(q)] + [(i,j) for i in range(q) for j in range(i+1,q)]
    def verts(pair):
        i,j = pair
        return [(i,j)] if i == j else [(i,j),(j,i)]
    neighbor_masks=[]
    for o in orbits:
        mask=0
        for v,p in enumerate(orbits):
            if any(x!=a and y!=b for x,y in verts(o) for a,b in verts(p)):
                mask|=1<<v
        neighbor_masks.append(mask)
    result=0
    unions=[0]*(1<<len(orbits))
    full=(1<<len(orbits))-1
    for mask in range(1,1<<len(orbits)):
        low=mask&-mask
        unions[mask]=unions[mask^low]|neighbor_masks[low.bit_length()-1]
        if unions[mask]==full:
            result+=(-1)**mask.bit_count()
    return result


def irreducible_multiplicities(q):
    B,s,t,st=expected(q)
    return {(e,d):(B+e*s+d*t+e*d*st)//4 for e in (1,-1) for d in (1,-1)}


if __name__ == '__main__':
    for q in (2,3):
        nfaces,traces=direct(q)
        assert traces == expected(q),(q,traces,expected(q))
        print('direct simplex enumeration q=%d: faces(including empty)=%d, character=%s' % (q,nfaces,traces))
    for q in (2,3,4,5):
        signed=swapped_coordinates_signed_independence(q)
        assert signed==-(q-1)**2,(q,signed)
        print('coordinate-swap orbit inclusion-exclusion q=%d: trace=%d' % (q,signed))
    for q in range(2,101):
        B,s,t,st=expected(q)
        vals=[B+e*s+d*t+e*d*st for e in (1,-1) for d in (1,-1)]
        assert all(v%4==0 and v>=0 for v in vals)
        assert sum(v//4 for v in vals)==B
    for q in (2,3,4,5,6):
        print('q=%d: V4 multiplicities %s' % (q,irreducible_multiplicities(q)))
    print('PASS direct enumeration, independent quotient enumeration, and 2<=q<=100 character arithmetic')
