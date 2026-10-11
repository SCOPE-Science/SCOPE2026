"""Finite checks of the rational symmetry character for total three-cut ladder complexes.

Execute with Python 3: python verify.py
No external packages are required. The infinite-family argument is in RESULT.md.
"""
from itertools import combinations
from math import comb


def vertices(n):
    return tuple(range(2*n))


def neighbors(n, v, w):
    a, i = divmod(v, n)
    b, j = divmod(w, n)
    return (a == b and abs(i-j) == 1) or (a != b and i == j)


def permutation(n, action):
    out = []
    for v in vertices(n):
        a, i = divmod(v, n)
        if 'S' in action:
            a = 1-a
        if 'R' in action:
            i = n-1-i
        out.append(a*n+i)
    return tuple(out)


def independent_triple(n, selected):
    for u, v, w in combinations(selected, 3):
        if not neighbors(n, u, v) and not neighbors(n, u, w) and not neighbors(n, v, w):
            return True
    return False


def orbit_trace(n, action):
    perm = permutation(n, action)
    pending = set(vertices(n))
    cycles = []
    while pending:
        v = min(pending)
        cyc = []
        cur = v
        while cur not in cyc:
            cyc.append(cur)
            cur = perm[cur]
        assert cur == v
        pending.difference_update(cyc)
        cycles.append(tuple(cyc))
    z = 0
    for q in range(min(4, len(cycles))+1):
        for inds in combinations(range(len(cycles)), q):
            chosen = [v for j in inds for v in cycles[j]]
            if len(chosen) > 4 or independent_triple(n, chosen):
                continue
            z += (-1)**q
    return (-1)**len(cycles)*z


def proposed(n, action):
    dim = comb(n-1, 2)
    flip = -1 if n%2 else 1
    reflection = (n-1)//2
    return {'I':dim, 'S':flip*dim, 'R':reflection, 'SR':flip*reflection}[action]


def all_faces(n):
    allmask = (1 << (2*n))-1
    faces = []
    for mask in range(1 << (2*n)):
        outside = [v for v in vertices(n) if (allmask^mask) & (1<<v)]
        if independent_triple(n, outside):
            faces.append(mask)
    return faces


def signed_simplex_trace(n, action, faces):
    perm = permutation(n, action)
    total = 0
    for mask in faces:
        ls = [i for i in vertices(n) if mask&(1<<i)]
        ls2 = [perm[i] for i in ls]
        if set(ls) != set(ls2):
            continue
        inv = sum(ls2[i] > ls2[j] for i in range(len(ls2)) for j in range(i+1, len(ls2)))
        total += (-1)**(len(ls)-1+inv)
    return total


def rank_gf2(columns):
    piv = {}
    for col in columns:
        x = col
        while x:
            p = x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                break
    return len(piv)


def homology(n, faces):
    layers = {}
    for f in faces:
        layers.setdefault(f.bit_count()-1, []).append(f)
    ranks = {}
    for q in range(0,max(layers)+1):
        lower = {s:i for i,s in enumerate(layers[q-1])}
        cols=[]
        for s in layers.get(q, []):
            c=0
            for v in vertices(n):
                if s&(1<<v):
                    face=s^(1<<v)
                    c ^= 1<<lower[face]
            cols.append(c)
        ranks[q] = rank_gf2(cols)
    betti={q:len(layers[q])-ranks.get(q,0)-ranks.get(q+1,0) for q in range(-1,max(layers)+1)}
    return {q:k for q,k in betti.items() if k}


def main():
    actions=('I','S','R','SR')
    for n in range(3,41):
        for a in actions:
            got=orbit_trace(n,a)
            expected=proposed(n,a)
            assert got==expected,(n,a,got,expected)
        assert (comb(n-1,2)+(n-1)//2)%2==0
    for n in range(3,8):
        fs=all_faces(n)
        assert 0 in fs
        for a in actions:
            got=signed_simplex_trace(n,a,fs)
            expected=proposed(n,a)
            assert got==expected,(n,a,got,expected)
        if n<=6:
            got=homology(n,fs)
            expected={2*n-6:comb(n-1,2)}
            assert got==expected,(n,got,expected)
        print('n',n,'faces',len(fs),'character',tuple(proposed(n,a) for a in actions))
    print('VERIFY_OK')


if __name__=='__main__':
    main()
