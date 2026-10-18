#!/usr/bin/env python3
"""Reproduce two low off-diagonal magnitude homology groups of crown graphs.

The chain complex uses standard graph distances and integral boundary signs.
Endpoint classes suffice by permutation and bipartition exchange symmetries.
"""
from collections import deque
from itertools import product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def crown_graph(n):
    vertices = tuple(range(2*n))
    adjacency = {v: set() for v in vertices}
    for i in range(n):
        for j in range(n):
            if i != j:
                adjacency[i].add(n+j)
                adjacency[n+j].add(i)
    distance = [[10**9]*(2*n) for _ in vertices]
    for start in vertices:
        distance[start][start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if distance[start][v] > distance[start][u]+1:
                    distance[start][v] = distance[start][u]+1
                    queue.append(v)
    assert max(max(row) for row in distance) == 3
    return distance


def chains(distance, a, b, length, max_degree):
    result = [[] for _ in range(max_degree+1)]
    vertices = range(len(distance))
    def visit(path, used):
        degree = len(path)-1
        if used == length and path[-1] == b:
            result[degree].append(tuple(path))
        if degree >= max_degree or used >= length:
            return
        for nxt in vertices:
            increment = distance[path[-1]][nxt]
            if increment and used + increment <= length:
                visit(path+[nxt], used+increment)
    visit([a],0)
    return result


def boundary_matrix(chains_by_degree, distance, k):
    target_index = {x:i for i,x in enumerate(chains_by_degree[k-1])}
    cols = []
    for path in chains_by_degree[k]:
        column = {}
        for i in range(1,k):
            if distance[path[i-1]][path[i+1]] == distance[path[i-1]][path[i]] + distance[path[i]][path[i+1]]:
                reduced = path[:i]+path[i+1:]
                index = target_index[reduced]
                column[index] = column.get(index,0) + (-1)**i
        cols.append({i:v for i,v in column.items() if v})
    return cols, len(target_index)


def modular_rank(cols, prime):
    pivots = {}
    for c in cols:
        vector = {i:v % prime for i,v in c.items() if v % prime}
        while vector:
            row = min(vector)
            if row not in pivots:
                coefficient = pow(vector[row],-1,prime)
                pivots[row] = {i:(v*coefficient)%prime for i,v in vector.items()}
                break
            factor = vector[row]
            for i, coefficient in pivots[row].items():
                new_coefficient = (vector.get(i,0)-factor*coefficient)%prime
                if new_coefficient:vector[i]=new_coefficient
                elif i in vector:del vector[i]
    return len(pivots)


def smith_data(cols, rows):
    matrix = Matrix.zeros(rows, len(cols))
    for j,column in enumerate(cols):
        for i,v in column.items():matrix[i,j]=v
    diag = smith_normal_form(matrix, domain=ZZ)
    entries = [abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i]]
    return len(entries), sorted(set(entries))


def check(n):
    d = crown_graph(n)
    endpoints = [(0,0), (0,1), (0,n), (0,n+1)]
    expected = {(2,3):(n==3), (3,4):(n==3)}
    report=[]
    for degree,length in [(2,3),(3,4)]:
        for a,b in endpoints:
            ch=chains(d,a,b,length,degree+1)
            lower,lower_rows=boundary_matrix(ch,d,degree)
            upper,upper_rows=boundary_matrix(ch,d,degree+1)
            assert upper_rows == len(ch[degree])
            ranks = [(modular_rank(lower,p),modular_rank(upper,p)) for p in (2,3,5)]
            assert len(set(ranks))==1,(n,degree,length,a,b,ranks)
            low,up = ranks[0]
            betti=len(ch[degree])-low-up
            expected_betti = int(n==3 and a==0 and b==n) if degree==2 else int(n==3 and a==0 and b==1)
            assert betti==expected_betti,(n,degree,length,a,b,betti,expected_betti)
            if n<=4 and ch[degree]:
                r1,inv1=smith_data(lower,lower_rows)
                r2,inv2=smith_data(upper,upper_rows)
                assert (r1,r2)==(low,up)
                assert inv2 in ([],[1]),(n,degree,length,a,b,inv2)
            report.append((degree,length,(a,b),len(ch[degree-1]),len(ch[degree]),len(ch[degree+1]),low,up,betti))
    return report


if __name__=='__main__':
    for n in (3,4,5,6):
        rows=check(n)
        print('CROWN',n,'CHECKED_ENDPOINT_CLASSES',len(rows))
        for k,l,ab,cprev,c,cnext,rprev,rnext,b in rows:
            print(' ',(k,l),ab,'chains', (cprev,c,cnext), 'ranks', (rprev,rnext),'homology_rank',b)
    print('CROWN_MAGNITUDE_LOW_OFF_DIAGONAL_CHECKS_OK')
