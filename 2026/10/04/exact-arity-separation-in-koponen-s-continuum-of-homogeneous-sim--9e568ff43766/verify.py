from itertools import permutations
from math import factorial

# Koponen's H_n has vertices 0,...,n.  On distinct triples R fails
# exactly at (0,b,b+1) for 1<=b<n and (0,n,1).
def false_triples(n):
    return {(0,b,b+1) for b in range(1,n)} | {(0,n,1)}

def relabel_false(n, p):
    return frozenset((p[a],p[b],p[c]) for (a,b,c) in false_triples(n))

def is_aut(n,p):
    return relabel_false(n,p) == frozenset(false_triples(n))

def embeds(m,n,inj):
    # inj is tuple of length m+1 into 0,...,n.
    Fm=false_triples(m); Fn=false_triples(n)
    for a in range(m+1):
        for b in range(m+1):
            for c in range(m+1):
                if len({a,b,c})<3:
                    continue
                src=(a,b,c) not in Fm
                tgt=(inj[a],inj[b],inj[c]) not in Fn
                if src != tgt:
                    return False
    return True

for n in range(3,8):
    verts=tuple(range(n+1))
    auts=[p for p in permutations(verts) if is_aut(n,p)]
    assert len(auts)==n, (n,len(auts))
    labeled={relabel_false(n,p) for p in permutations(verts)}
    expected=factorial(n+1)//n
    assert len(labeled)==expected, (n,len(labeled),expected)
    # Every automorphism fixes 0; restrictions are the cyclic rotations.
    assert all(p[0]==0 for p in auts)
    print(f'n={n}: |Aut(H_n)|={len(auts)}, labeled copies={len(labeled)}')

# Independent finite check of Koponen's pairwise non-embedding antichain.
for m in range(3,7):
    for n in range(3,8):
        if m==n or m>n:
            continue
        found=False
        # Any embedding must send 0 to 0 because every false triple has first coordinate 0.
        for image_pos in permutations(range(1,n+1),m):
            inj=(0,)+image_pos
            if embeds(m,n,inj):
                found=True
                break
        assert not found, (m,n,inj)
print('finite non-embedding checks: OK')
print('VERIFY_OK')
