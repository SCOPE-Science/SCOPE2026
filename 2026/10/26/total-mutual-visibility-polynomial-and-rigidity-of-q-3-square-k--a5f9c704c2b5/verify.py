#!/usr/bin/env python3
"""Independent finite checks of a Hamming-graph visibility enumerator."""
from collections import Counter, deque
from itertools import product
from math import comb
from random import Random


def expected_coefficients(n):
    c = Counter()
    for k in range(n+1):
        c[k] += 2*comb(n,k)*4**k
    c[0] -= 1
    for a in range(1,n+1):
        for b in range(1,n+1):
            c[a+b] += 4*comb(n,a)*comb(n,b)
    c[2] += 12*n
    for b in range(2,n+1):
        c[b+1] += 24*n*comb(n-1,b-1)
    c[4] += 12*comb(n,2)
    return [c[k] for k in range(2*n+1)]


def hamming(vertices, i, j):
    return sum(a != b for a,b in zip(vertices[i],vertices[j]))


def enumerate_distance_two_avoiding(n):
    vertices = list(product(range(2), repeat=3))
    vertices = [v+(c,) for c in range(n) for v in vertices]
    size = len(vertices)
    forbidden = [0]*size
    for i in range(size):
        for j in range(size):
            if i != j and hamming(vertices,i,j) == 2:
                forbidden[i] |= 1<<j
    count = Counter()
    def visit(avail, used):
        if not avail:
            count[used] += 1
            return
        bit = avail & (-avail)
        idx = bit.bit_length()-1
        rest = avail ^ bit
        visit(rest, used)
        visit(rest & ~forbidden[idx], used+1)
    visit((1<<size)-1,0)
    return vertices,count


def total_visible_direct(vertices, selected):
    size=len(vertices)
    neighbors=[[j for j in range(size) if hamming(vertices,i,j)==1] for i in range(size)]
    for u in range(size):
        for v in range(u+1,size):
            shortest=hamming(vertices,u,v)
            # BFS: selected vertices cannot appear internally.
            q=deque([(u,0)])
            visited={u}
            got=False
            while q:
                x,d=q.popleft()
                if x==v:
                    got=(d==shortest)
                    break
                if d>=shortest: continue
                for y in neighbors[x]:
                    if y not in visited and (y==v or y not in selected):
                        visited.add(y)
                        q.append((y,d+1))
            if not got: return False
    return True


def run():
    for n in range(1,7):
        vertices,counts=enumerate_distance_two_avoiding(n)
        actual=[counts[k] for k in range(2*n+1)]
        predicted=expected_coefficients(n)
        assert actual==predicted,(n,actual,predicted)
        assert max(k for k,v in counts.items() if v)==2*n
        if n>=3:
            assert counts[2*n]==4
            for k in range(n+2,2*n+1):
                assert counts[k]==4*comb(2*n,k)
        if n==2:
            assert counts[4]==16
        print('ENUM_OK',n,sum(actual),actual)
    rng=Random(731048)
    for n in (1,2,3):
        vertices=[v+(c,) for c in range(n) for v in product(range(2),repeat=3)]
        for _ in range(72):
            selected={i for i in range(len(vertices)) if rng.randrange(4)==0}
            no_two=not any(hamming(vertices,i,j)==2 for i in selected for j in selected if i<j)
            assert total_visible_direct(vertices,selected)==no_two
    print('VERIFY_OK all polynomial coefficients and sampled direct geodesics')

if __name__=='__main__': run()
