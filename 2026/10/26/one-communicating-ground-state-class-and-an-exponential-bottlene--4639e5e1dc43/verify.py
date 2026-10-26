#!/usr/bin/env python3
"""Finite reproducibility checks for minority dynamics on equal tripartite graphs.

Python 3, standard library only. Mathematical proof covers all positive sizes.
"""
from collections import deque
from itertools import combinations

def count_ones(z, start, m):
    return ((z >> start) & ((1 << m) - 1)).bit_count()

def spins(z,m):
    return tuple(2*count_ones(z,j*m,m)-m for j in range(3))

def energy(z,m):
    u=spins(z,m)
    return (3*m*m+u[0]*u[1]+u[1]*u[2]+u[2]*u[0])//2

def active_vertices(z,m):
    u=spins(z,m)
    for i in range(3):
        outside=u[(i+1)%3]+u[(i+2)%3]
        for j in range(m):
            v=i*m+j
            bit=(z>>v)&1
            if (bit and outside>=0) or (not bit and outside<=0):
                yield v

def ground(z,m):
    u=spins(z,m)
    return any(abs(u[i])==m and u[i]==-u[j] for i,j in combinations(range(3),2))

def drive_to_ground(z,m):
    path=[z]
    for i in range(3):
        u=spins(z,m)
        outside=sum(u[j] for j in range(3) if j!=i)
        target=0 if outside>=0 else 1
        for j in range(m):
            v=i*m+j
            if ((z>>v)&1)!=target:
                assert v in set(active_vertices(z,m))
                new=z^(1<<v)
                assert energy(new,m)<=energy(z,m)
                z=new
                path.append(z)
    assert ground(z,m)
    assert len(path)-1 <=3*m
    return path

def test_size(m):
    N=3*m
    num=1<<N
    L=6*((1<<m)-1)
    lows=set()
    total_flips=0
    for z in range(num):
        g=ground(z,m)
        e=energy(z,m)
        assert (e==m*m)==g
        if g:
            lows.add(z)
        for v in active_vertices(z,m):
            w=z^(1<<v)
            assert energy(w,m)<=e
            if g:
                assert ground(w,m)
                assert v in set(active_vertices(w,m))
            total_flips+=1
        assert drive_to_ground(z,m)[-1] in range(num)
    assert len(lows)==L, (m,len(lows),L)
    # Exactly one communicating ground class; use breadth-first reachability.
    root=next(iter(lows)); reached={root}; q=deque([root])
    while q:
        z=q.popleft()
        for v in active_vertices(z,m):
            w=z^(1<<v)
            if w not in reached:
                reached.add(w);q.append(w)
    assert reached==lows, (m,len(reached),len(lows))
    # Six labelled monochromatic (nonconstant) junctions.
    corners={z for z in lows if all(abs(x)==m for x in spins(z,m))}
    assert len(corners)==6
    if m>=2:
        # Fix group 0 all 0, group 1 all 1, group 2 nonmonochromatic.
        S={((1<<m)-1)<<m | (q << (2*m)) for q in range(1,(1<<m)-1)}
        assert S<=lows and len(S)==(1<<m)-2
        outgoing=sum(sum((z^(1<<v)) not in S for v in active_vertices(z,m)) for z in S)
        assert outgoing==2*m, (m,outgoing)
        assert (outgoing,3*m*L)==(2*m,3*m*L)
    return {'m':m, 'all_states':num, 'ground_states':len(lows),
            'communicating_classes':1, 'junctions':len(corners),
            'active_transitions_checked':total_flips,
            'claimed_ground_states':L}

if __name__=='__main__':
    for m in range(1,6):
        print(test_size(m))
    print('All finite tests passed. General proof is separate.')
