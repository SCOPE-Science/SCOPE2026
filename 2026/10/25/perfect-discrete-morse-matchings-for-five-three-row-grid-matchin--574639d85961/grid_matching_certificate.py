#!/usr/bin/env python3
"""Exact finite face-poset discrete Morse verification for grid matching complexes.

The two vertices of every grid edge are explicitly constructed. The fixed
lexicographic pivot orders define a complete partial matching of the augmented
face poset. Directed Hasse covers are checked for acyclicity by a full
indegree-topological-sort, not by inspecting Euler characteristics alone.
"""
from collections import Counter, deque

PIVOTS = {
    3: [5,11,0,4,6,1,8,9,7,3,2,10],
    4: [16,5,2,4,0,13,14,6,1,7,9,15,8,12,11,3,10],
    5: [2,20,11,8,21,7,18,15,13,1,16,17,5,19,6,4,3,10,0,14,9,12],
    6: [9,19,24,26,10,0,18,6,11,3,14,1,15,13,7,5,25,12,2,16,20,23,17,8,22,4,21],
    7: [25,19,17,1,22,23,20,21,29,5,28,4,12,10,26,2,7,14,15,18,6,30,24,11,3,16,31,0,8,27,9,13],
}
EXPECT = {3: (131,5), 4:(823,9), 5:(5096,16), 6:(31687,31), 7:(196785,55)}


def grid_edges(n):
    out=[]
    for i in range(3):
        for j in range(n):
            for a,b in ((i+1,j),(i,j+1)):
                if a < 3 and b < n:
                    out.append((i*n+j,a*n+b))
    return out


def enumerate_faces(n):
    edges=grid_edges(n)
    faces={0:0} # face edge-bitmask -> occupied grid-vertex bitmask
    for k,(u,v) in enumerate(edges):
        uv=(1<<u)|(1<<v)
        additions={f|(1<<k):used|uv for f,used in faces.items() if not used&uv}
        faces.update(additions)
    return set(faces),len(edges)


def pivot_matching(faces,order):
    remaining=set(faces)
    paired_lower={}
    for k in order:
        bit=1<<k
        for f in tuple(remaining):
            g=f|bit
            if not f&bit and g in remaining:
                remaining.remove(f)
                remaining.remove(g)
                paired_lower[f]=g
    return paired_lower,remaining


def directed_acyclicity(faces, lower_pairs):
    # Each oriented Hasse edge is either upper->lower, or lower->upper
    # for a matched cover. The complete orientation must be a DAG.
    indegree={f:0 for f in faces}
    cover_count=0
    for upper in faces:
        bits=upper
        while bits:
            bit=bits&-bits;bits-=bit
            lower=upper-bit
            if lower_pairs.get(lower)==upper:
                indegree[upper]+=1
            else:
                indegree[lower]+=1
            cover_count+=1
    ready=deque(x for x,d in indegree.items() if d==0)
    seen=0
    while ready:
        face=ready.popleft()
        seen+=1
        bits=face
        while bits:
            bit=bits&-bits;bits-=bit
            low=face-bit
            if lower_pairs.get(low)!=face:
                indegree[low]-=1
                if indegree[low]==0:ready.append(low)
        top=lower_pairs.get(face)
        if top is not None:
            indegree[top]-=1
            if indegree[top]==0:ready.append(top)
    assert seen==len(faces),(seen,len(faces))
    return cover_count


def main():
    for n in sorted(PIVOTS):
        faces,ecount=enumerate_faces(n)
        assert sorted(PIVOTS[n])==list(range(ecount))
        pairing,crit=pivot_matching(faces,PIVOTS[n])
        assert len(pairing)*2+len(crit)==len(faces)
        assert {x.bit_count()-1 for x in crit}=={n-1}
        assert (len(faces),len(crit))==EXPECT[n]
        # Independently check the signed Euler count using ALL faces.
        augmented_euler=sum((-1)**x.bit_count() for x in faces)
        assert augmented_euler==(-1)**n*len(crit)
        covers=directed_acyclicity(faces,pairing)
        print(f'n={n}: graph_edges={ecount}; faces={len(faces)}; '
              f'Hasse_covers={covers}; matched_pairs={len(pairing)}; '
              f'critical_{n-1}_faces={len(crit)}; DAG=yes; Euler=yes')
    print('CERTIFICATE_OK')

if __name__=='__main__':main()
