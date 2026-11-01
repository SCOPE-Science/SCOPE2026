#!/usr/bin/env python3
"""Exact finite-locality and integral Morse checks for bidirected K_{2,n} multipath complexes.

No external dependencies. Use Python 3.9 or newer.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

PIVOTS_SIX = (18,9,22,21,7,15,5,19,3,1,12,14,16,0,23,10,6,11,8,17,2,4,13,20)
PIVOTS_FIVE = (6,2,13,18,5,19,8,1,10,3,11,0,7,15,9,14,16,17,4,12)


def all_faces(n):
    # Arc 4*j+2*h: hub h -> leaf j; arc 4*j+2*h+1: leaf j -> hub h.
    arcs = [(h, 2+j) if orient == 0 else (2+j,h)
            for j in range(n) for h in range(2) for orient in range(2)]
    faces = [set() for _ in range(5)]
    faces[0].add(())
    for size in range(1,5):
        for face in combinations(range(4*n),size):
            sources = [arcs[z][0] for z in face]
            targets = [arcs[z][1] for z in face]
            if len(set(sources)) != size or len(set(targets)) != size:
                continue
            successor = dict(zip(sources,targets))
            valid = True
            for v in sources:
                seen = set()
                while v in successor:
                    if v in seen:
                        valid = False
                        break
                    seen.add(v)
                    v = successor[v]
                if not valid:
                    break
            if valid:
                faces[size].add(face)
    return faces


def match(faces,pivots):
    residual = set().union(*faces)
    pairs = []
    for v in pivots:
        # Each optional-pivot interval is disjoint from every other one at this stage.
        stage = [(face,tuple(sorted((*face,v)))) for face in residual if v not in face]
        for low,high in stage:
            if low in residual and high in residual:
                residual.remove(low)
                residual.remove(high)
                pairs.append((low,high))
    return residual,pairs


def assert_acyclic(faces,pairs):
    allf = sorted(set().union(*faces),key=lambda x:(len(x),x))
    index = {face:i for i,face in enumerate(allf)}
    matched = set(pairs)
    adj = [[] for _ in allf]
    indegree = [0]*len(allf)
    def edge(a,b):
        adj[a].append(b)
        indegree[b] += 1
    for size in range(1,5):
        for upper in faces[size]:
            for k in range(size):
                lower = upper[:k]+upper[k+1:]
                if (lower,upper) in matched:
                    edge(index[lower],index[upper])
                else:
                    edge(index[upper],index[lower])
    q=deque(i for i,d in enumerate(indegree) if d==0)
    seen=0
    while q:
        i=q.popleft();seen+=1
        for j in adj[i]:
            indegree[j]-=1
            if indegree[j]==0:
                q.append(j)
    assert seen==len(allf),('directed cycle in Hasse graph',seen,len(allf))
    return sum(len(x) for x in adj)


def face_vector_formula(n):
    return (1,4*n,6*n*n-4*n,4*n*(n-1)**2,n*(n-1)**2*(n-2))


def sphere_count(n):
    return n**4-8*n**3+19*n**2-14*n+1


def top_morse_boundary_five(critical,pairs):
    up = {low:high for low,high in pairs if len(low)==3}
    down = {high:low for low,high in pairs if len(high)==3}
    targets = [face for face in critical if len(face)==3]
    assert len(targets)==1
    target=targets[0]
    @lru_cache(None)
    def reduction(triangle):
        if triangle==target:
            return 1
        if triangle in down:
            return 0
        assert triangle in up,triangle
        upper=up[triangle]
        k=next(k for k in range(4) if upper[:k]+upper[k+1:]==triangle)
        # Algebraic elementary cancellation of an integral unit incidence.
        return -((-1)**k)*sum(((-1)**j)*reduction(upper[:j]+upper[j+1:])
                              for j in range(4) if j!=k)
    entries=[]
    for upper in sorted(face for face in critical if len(face)==4):
        entries.append(sum(((-1)**j)*reduction(upper[:j]+upper[j+1:])
                           for j in range(4)))
    return target, entries


def boundary_rank_mod_p(faces,k,p):
    row={face:j for j,face in enumerate(sorted(faces[k-1]))}
    pivots={}
    for simplex in faces[k]:
        vec={row[simplex[:i]+simplex[i+1:]]:((-1)**i)%p for i in range(k)}
        while vec:
            j=max(vec)
            if j in pivots:
                factor=vec[j]
                for r,c in pivots[j].items():
                    new=(vec.get(r,0)-factor*c)%p
                    if new:vec[r]=new
                    else:vec.pop(r,None)
            else:
                inv=pow(vec[j],-1,p)
                pivots[j]={r:val*inv%p for r,val in vec.items()}
                break
    return len(pivots)


def main():
    for n in (5,6,7,8,9,10):
        faces=all_faces(n)
        assert tuple(map(len,faces))==face_vector_formula(n)
        residual,pairs=match(faces,PIVOTS_FIVE if n==5 else PIVOTS_SIX)
        if n==5:
            assert Counter(map(len,residual))==Counter({3:1,4:32})
            edges=assert_acyclic(faces,pairs)
            triangle,row=top_morse_boundary_five(residual,pairs)
            assert triangle==(2,5,11)
            assert Counter(row)==Counter({2:11,0:11,-2:10})
            assert __import__('math').gcd(*row)==2
            ranks2=[boundary_rank_mod_p(faces,k,2) for k in range(1,5)]
            ranks3=[boundary_rank_mod_p(faces,k,3) for k in range(1,5)]
            assert ranks2==[1,19,111,208]
            assert ranks3==[1,19,111,209]
            print('n=5:',len(pairs),'matched pairs, critical cell dimensions 2:1 and 3:32; signed Morse row',dict(Counter(row)),'Hasse arrows',edges,'field ranks',ranks2,ranks3)
        else:
            assert all(len(face)==4 for face in residual)
            assert len(residual)==sphere_count(n)
            if n in (6,9):
                edges=assert_acyclic(faces,pairs)
                print('n=%s:'%n,len(pairs),'matched pairs,',len(residual),'critical 3-cells; Hasse arrows',edges)
            else:
                print('n=%s:'%n,len(pairs),'matched pairs,',len(residual),'critical 3-cells')
    print('BIDIRECTED_K2N_TORSION_TO_SPHERE_WEDGE_EXACT_OK')

if __name__=='__main__':
    main()
