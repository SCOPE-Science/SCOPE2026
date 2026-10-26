#!/usr/bin/env python3
"""Exhaustive finite-field checker for weight-zero RB maps on k[t]/(t^3).

Validates both all 3x3 matrices and isomorphism-orbit predictions for
q = 2, 3, 4. For q=5 validates all predicted maps and their orbits.
No external dependencies.
"""
from collections import Counter
from itertools import product

def make_field(q):
    assert q in (2,3,4,5)
    if q == 4:
        add = [[a ^ b for b in range(4)] for a in range(4)]
        def times(a,b):
            z=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1:
                        z ^= 1 << (i+j)
            if z&4: z ^= 7  # x^2 = x+1 in GF(4)
            return z
        mult = [[times(a,b) for b in range(4)] for a in range(4)]
    else:
        add = [[(a+b)%q for b in range(q)] for a in range(q)]
        mult = [[(a*b)%q for b in range(q)] for a in range(q)]
    return add, mult

def add_vector(v,w,A): return tuple(A[a][b] for a,b in zip(v,w))

def multiply(v,w,A,M):
    return tuple(
        sum_field([M[v[i]][w[j]] for i in range(3) for j in range(3) if i+j==k],A)
        for k in range(3)
    )

def sum_field(items,A):
    s=0
    for x in items: s=A[s][x]
    return s

def map_apply(P,v,A,M):
    return tuple(sum_field([M[v[j]][P[j][i]] for j in range(3)],A) for i in range(3))

def is_rb(P,A,M):
    for i in range(3):
        for j in range(i,3):
            left=multiply(P[i],P[j],A,M)
            term1=tuple((P[i][k-j] if k>=j else 0) for k in range(3))
            term2=tuple((P[j][k-i] if k>=i else 0) for k in range(3))
            rhs=map_apply(P,add_vector(term1,term2,A),A,M)
            if left!=rhs: return False
    return True

def candidate(q,A,M):
    return {((0,a,b),(0,0,c),(0,0,0))
            for a,b,c in product(range(q),repeat=3)
            if M[a][a]==M[sum_field([a,a],A)][c]}

def conjugate(P,u,v,A,M,q):
    # phi(t)=u t + v t^2, invertible iff u != 0.
    # For classified P, P(1)=a t+b t^2 and P(t)=c t^2.
    a,b,c=P[0][1],P[0][2],P[1][2]
    au=M[a][u]
    bnew=A[M[a][v]][M[b][M[u][u]]]
    cnew=M[c][u]
    return ((0,au,bnew),(0,0,cnew),(0,0,0))

def orbit_count(candidates,q,A,M):
    unseen=set(candidates); n=0; sizes=[]
    while unseen:
        one=next(iter(unseen))
        orbit={conjugate(one,u,v,A,M,q) for u in range(1,q) for v in range(q)}
        assert orbit.issubset(candidates)
        unseen.difference_update(orbit)
        n+=1; sizes.append(len(orbit))
    return n,Counter(sizes)

def check(q,full):
    A,M=make_field(q)
    candidates=candidate(q,A,M)
    expected_count=q*q if q%2==0 else q*(2*q-1)
    assert len(candidates)==expected_count,(q,len(candidates),expected_count)
    if full:
        actual=set()
        for entries in product(range(q),repeat=9):
            P=tuple(tuple(entries[3*i+j] for j in range(3)) for i in range(3))
            if is_rb(P,A,M): actual.add(P)
        assert actual==candidates,(q,len(actual),len(candidates))
    else:
        assert all(is_rb(P,A,M) for P in candidates)
    n,sizes=orbit_count(candidates,q,A,M)
    predicted=q+2 if q%2==0 else q+4
    assert n==predicted,(q,n,predicted)
    print(f'q={q} all_matrices={full} operators={len(candidates)} orbits={n} orbit_size_histogram={dict(sorted(sizes.items()))}')

if __name__=='__main__':
    for q,full in ((2,True),(3,True),(4,True),(5,False)):
        check(q,full)
    print('VERIFY_OK')
