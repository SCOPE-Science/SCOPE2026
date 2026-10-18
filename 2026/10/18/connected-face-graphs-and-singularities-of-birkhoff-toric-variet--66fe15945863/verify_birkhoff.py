"""Independent finite face and normal-cone census for Birkhoff toric singular strata.

Requires Python 3 standard library only. Enumerates every intersection of the
coordinate facets of B_3 and B_4 (all 2^(n^2) coordinate patterns), deduplicates
faces, and applies graph-connectivity/dimension formulas.  It does not prove the
infinite family theorem; that proof is included separately in RESULT.md.
"""
from itertools import permutations, combinations
from math import comb


def component_count(edge_mask, n):
    parent = list(range(2 * n))
    def root(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for i in range(n):
        for j in range(n):
            if edge_mask & (1 << (i*n+j)):
                a, b = root(i), root(n+j)
                if a != b:
                    parent[b] = a
    return len({root(a) for a in range(2*n)})


def complete_two_block_masks(n):
    found = set()
    for a in range(1, n):
        for rows in combinations(range(n), a):
            r = set(rows)
            for cols in combinations(range(n), a):
                c = set(cols)
                mask = sum(1 << (i*n+j) for i in range(n) for j in range(n) if ((i in r) == (j in c)))
                found.add(mask)
    return found


def audit_n(n):
    full = (1 << (n*n))-1
    perms = [sum(1 << (i*n+p[i]) for i in range(n)) for p in permutations(range(n))]
    faces = set()
    # Each nonempty face is intersection of active coordinate facets.
    for support in range(full+1):
        face = 0
        for pm in perms:
            if pm & support == pm:
                face |= pm
        if face:
            faces.add(face)
    data = {}
    for face in faces:
        e = face.bit_count()
        c = component_count(face,n)
        dim = e - 2*n+c
        codim = (n-1)**2-dim
        rays = n*n-e
        assert codim >= 0 and rays-codim == c-1, (n,face,e,c,dim,codim,rays)
        data[face] = (c,dim,rays,codim)
    singular = {f for f,t in data.items() if t[0]>1}
    maximal = {f for f in singular if not any(f != g and f & g == f for g in singular)}
    expected = complete_two_block_masks(n)
    assert maximal == expected, (n,len(maximal),len(expected), sorted(maximal ^ expected)[:10])
    assert len(maximal) == (comb(2*n,n)-2)//2
    strata = {}
    for face in maximal:
        a = next((k for k in range(1,n) if data[face][1]==(k-1)**2+(n-k-1)**2), None)
        strata[data[face][1]] = strata.get(data[face][1],0)+1
    print('n',n,'faces',len(faces),'singular_faces',len(singular),'maximal_singular',len(maximal),'dimensions',strata)


def smaller_boundary_checks():
    for n in range(3,8):
        blocks = complete_two_block_masks(n)
        assert len(blocks) == (comb(2*n,n)-2)//2
        for f in blocks:
            c = component_count(f,n)
            assert c==2
            e=f.bit_count()
            d=e-2*n+c
            q=(n-1)**2-d
            assert (n*n-e)-q==1
            ab=(q+1)//2
            assert q==2*ab-1
        print('block_check',n,'components',len(blocks))

if __name__=='__main__':
    audit_n(3)
    audit_n(4)
    smaller_boundary_checks()
    print('VERIFY_OK')
