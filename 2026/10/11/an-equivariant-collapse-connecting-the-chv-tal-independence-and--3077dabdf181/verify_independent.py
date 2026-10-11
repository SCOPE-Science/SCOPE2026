#!/usr/bin/env python3
"""Independent face, modular-chain, graph-coloring, and symmetry check (stdlib only)."""
from itertools import combinations

VERTICES = tuple(range(12))
NEIGHBORS = (
    (1,4,6,9), (0,2,5,7), (1,3,6,8), (2,4,7,9),
    (0,3,5,8), (1,4,10,11), (0,2,10,11), (1,3,8,11),
    (2,4,7,10), (0,3,10,11), (5,6,8,9), (5,6,7,9),
)
NB = [set(v) for v in NEIGHBORS]


def face_tuples():
    f={k:[] for k in range(1,5)}
    for k in range(1,5):
        for c in combinations(VERTICES,k):
            if set.intersection(*(NB[x] for x in c)):
                f[k].append(c)
    assert f[1] == [(x,) for x in VERTICES]
    return f


def rank_mod(rows,p):
    if not rows:return 0
    m=[list(map(lambda x:x%p, row)) for row in rows]
    r=0;n=len(m[0])
    for col in range(n):
        pivot=next((i for i in range(r,len(m)) if m[i][col]),None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r]
        z=pow(m[r][col],-1,p)
        m[r]=[(x*z)%p for x in m[r]]
        for i in range(r+1,len(m)):
            if m[i][col]:
                z=m[i][col]
                m[i]=[(x-z*y)%p for x,y in zip(m[i],m[r])]
        r+=1
        if r==len(m):break
    return r


def boundary(faces,k):
    lower=faces[k-1]
    index={s:i for i,s in enumerate(lower)}
    z=[[0]*len(faces[k]) for _ in lower]
    for j,s in enumerate(faces[k]):
        for i in range(len(s)):
            f=s[:i]+s[i+1:]
            z[index[f]][j]=(-1)**i
    return z


def colorable(q):
    colors=[-1]*12
    order=sorted(VERTICES,key=lambda x:(-len(NB[x]),x))
    def rec(i):
        if i==12:return tuple(colors)
        v=order[i]
        for c in range(q):
            if all(colors[w]!=c for w in NB[v]):
                colors[v]=c
                z=rec(i+1)
                if z is not None:return z
        colors[v]=-1
        return None
    return rec(0)


def compose(a,b):return tuple(a[b[i]] for i in VERTICES)

def all_automorphisms():
    # Independent exhaustive backtracking; every pair must preserve adjacency AND nonadjacency.
    result=[]
    mapping={}
    used=set()
    def rec():
        if len(mapping)==12:
            result.append(tuple(mapping[i] for i in VERTICES));return
        # Pick the unassigned vertex most strongly constrained by already mapped edges.
        remaining=[x for x in VERTICES if x not in mapping]
        v=max(remaining,key=lambda x:(sum(x in NB[u] for u in mapping),-x))
        for w in VERTICES:
            if w in used:continue
            if not all((v in NB[u]) == (w in NB[mapping[u]]) for u in mapping):continue
            mapping[v]=w;used.add(w)
            rec()
            used.remove(w);del mapping[v]
    rec()
    return result


def signed_fixed_trace(faces,p):
    out=-1   # reduced alternating trace: empty simplex contributes -1
    for k in range(1,5):
        for s in faces[k]:
            images=[p[i] for i in s]
            if set(images)!=set(s):continue
            inversions=sum(images[a]>images[b] for a in range(k) for b in range(a+1,k))
            out+=(-1)**(k-1+inversions)
    return out


def main():
    assert all(len(x)==4 for x in NB)
    assert all((v in NB[u]) == (u in NB[v]) for u in VERTICES for v in VERTICES)
    assert not any(v in NB[u] and w in NB[v] and u in NB[w] for u,v,w in combinations(VERTICES,3))
    f=face_tuples()
    assert [len(f[k]) for k in range(1,5)] == [12,42,44,12]
    for prime in (2,3,5,101):
        ranks=[rank_mod(boundary(f,k),prime) for k in (2,3,4)]
        assert ranks==[11,31,12],(prime,ranks)
    assert colorable(3) is None
    four=colorable(4)
    assert four is not None
    assert all(four[u]!=four[v] for u in VERTICES for v in NB[u])
    group=all_automorphisms()
    assert len(group)==8,len(group)
    traces=[signed_fixed_trace(f,p) for p in group]
    assert sorted(traces)==[-1,-1,-1,-1,1,1,1,1],traces
    r=(1,5,11,6,0,4,7,10,9,2,3,8)
    s=(0,4,3,2,1,5,9,8,7,6,11,10)
    identity=tuple(VERTICES)
    assert r in group and s in group
    assert compose(compose(compose(r,r),r),r)==identity
    assert compose(s,s)==identity
    assert compose(compose(s,r),s)==compose(compose(r,r),r)
    powers=[identity]
    for k in range(3):powers.append(compose(r,powers[-1]))
    assert len(set(powers))==4 and s not in powers
    assert {compose(p, x) for p in powers for x in (identity,s)} == set(group)
    orbit_sets=[]
    pending=set(VERTICES)
    while pending:
        v=min(pending)
        orbit={p[v] for p in group}
        orbit_sets.append(tuple(sorted(orbit)))
        pending-=orbit
    assert sorted(map(len,orbit_sets)) == [4,8], orbit_sets
    assert signed_fixed_trace(f,r)==-1
    assert signed_fixed_trace(f,s)==-1
    assert signed_fixed_trace(f,compose(r,s))==1
    print('INDEPENDENT_OK f_vector=%s boundary_ranks=[11,31,12] primes=[2,3,5,101]'
        %([len(f[k]) for k in range(1,5)]))
    print('CHROMATIC_OK no_three_coloring four_coloring=%s' % (four,))
    print('SYMMETRY_OK order=8 orbits=%s traces=%s rotations_r=%d reflection_s=%d reflection_rs=%d' % (
        orbit_sets,
        sorted(traces),signed_fixed_trace(f,r),signed_fixed_trace(f,s),
        signed_fixed_trace(f,compose(r,s))))

if __name__ == '__main__':main()
