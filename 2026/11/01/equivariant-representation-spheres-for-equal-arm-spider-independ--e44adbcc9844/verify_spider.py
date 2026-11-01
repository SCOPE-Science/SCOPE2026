"""Finite, independent face/character checks for equal-arm spider independence complexes.
Run: python3 verify_spider.py.  No network or nonstandard dependencies.
"""
from itertools import permutations
from math import factorial


def graph(m, length):
    # center is 0; arm i consists of indices 1+i*length through (i+1)*length
    n = 1 + m * length
    edges = []
    for a in range(m):
        previous = 0
        for j in range(length):
            v = 1 + a * length + j
            edges.append((previous, v))
            previous = v
    return n, edges


def independent_faces(n, edges):
    nbr = [0] * n
    for u,v in edges:
        nbr[u] |= 1 << v
        nbr[v] |= 1 << u
    faces = [0]
    for v in range(n):
        b = 1 << v
        faces += [f | b for f in faces if not (f & nbr[v])]
    return faces


def permutation_on_graph(m, length, perm):
    p = list(range(1 + m * length))
    for a in range(m):
        for j in range(length):
            p[1 + a*length + j] = 1 + perm[a]*length + j
    return p


def signed_trace(faces, vertex_perm):
    total = -1  # augmented empty face sign
    for f in faces[1:]:
        verts = [v for v in range(len(vertex_perm)) if f >> v & 1]
        img = [vertex_perm[v] for v in verts]
        if set(img) != set(verts):
            continue
        inv = sum(img[i] > img[j] for i in range(len(img)) for j in range(i+1,len(img)))
        total += (-1) ** (len(verts) - 1 + inv)
    return total


def cycles(perm):
    n=len(perm)
    unseen=set(range(n))
    num=0
    while unseen:
        num += 1
        v=next(iter(unseen))
        while v in unseen:
            unseen.remove(v)
            v=perm[v]
    return num


def expected_reduced_trace(m,L,cyc):
    q,r=divmod(L,3)
    if r == 0:
        return 0
    dim = m*q if r==1 else m*(q+1)-1
    dim_fixed = q*cyc if r==1 else (q+1)*cyc-1
    return (-1) ** dim_fixed


def mod2_boundary_rank(columns):
    piv={}
    for x in columns:
        while x:
            b=x.bit_length()-1
            if b not in piv:
                piv[b]=x
                break
            x ^= piv[b]
    return len(piv)


def betti_mod2(faces, n):
    buckets={}
    for f in faces[1:]:
        k=f.bit_count()-1
        buckets.setdefault(k,[]).append(f)
    ranks={}
    for d,fs in buckets.items():
        if d==0:
            ranks[d]=0
            continue
        lower={f:i for i,f in enumerate(buckets[d-1])}
        columns=[]
        for f in fs:
            col=0
            bit=f
            while bit:
                b=bit & -bit
                bit-=b
                col ^= 1 << lower[f ^ b]
            columns.append(col)
        ranks[d]=mod2_boundary_rank(columns)
    return {d:len(fs)-ranks[d]-ranks.get(d+1,0)-(d==0) for d,fs in buckets.items()}


def run():
    characters=0;betti=0;faces_count=0; orbit_fixed=0
    for m,L in ((2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),
                (3,4),(3,5),(3,6),(4,1),(4,2),(4,3),(4,4)):
        n,e=graph(m,L)
        faces=independent_faces(n,e)
        faces_count+=len(faces)
        red=betti_mod2(faces,n)
        q,r=divmod(L,3)
        d=m*q if r==1 else m*(q+1)-1
        for deg,rank in red.items():
            expected=int(r!=0 and deg==d)
            assert rank==expected,(m,L,red,d)
        betti+=1
        for perm in permutations(range(m)):
            cp=cycles(perm)
            p=permutation_on_graph(m,L,perm)
            tr=signed_trace(faces,p)
            assert tr==expected_reduced_trace(m,L,cp),(m,L,perm,tr,expected_reduced_trace(m,L,cp))
            characters+=1
            # The orbit-incidence graph is an actual spider on cp arms:
            orbit_fixed+=1
    print(f'VERIFY_OK {betti} full mod-2 Betti vectors; {characters} oriented Lefschetz characters; {orbit_fixed} orbit-fixed quotient predictions; {faces_count} independent face instances')

if __name__=='__main__':run()
