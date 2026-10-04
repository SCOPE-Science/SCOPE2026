#!/usr/bin/env python3
"""Replay checks for the cyclic path-chain parity theorem."""
from fractions import Fraction


def graph(m):
    V = ['s','t'] + [('a',i) for i in range(m)] + [('b',i) for i in range(m)] + [('c',i) for i in range(m)]
    E=set()
    for i in range(m):
        E.update({
            ('s',('a',i)), (('c',i),'t'),
            (('a',i),('b',i)), (('a',i),('b',(i+1)%m)),
            (('b',i),('c',i)), (('b',i),('c',(i+1)%m)),
            (('a',i),('c',i)), (('a',i),('c',(i+2)%m)),
        })
    return V,E

def allowed_paths(V,E,n):
    out={v:[] for v in V}
    for a,b in E: out[a].append(b)
    P=[(v,) for v in V]
    for _ in range(n): P=[p+(w,) for p in P for w in out[p[-1]]]
    return P

def is_allowed(q,E):
    return all((q[i],q[i+1]) in E for i in range(len(q)-1))

def constraint_matrix(m):
    V,E=graph(m); P=allowed_paths(V,E,4)
    rows={}; triples=[]
    for j,p in enumerate(P):
        for k in range(5):
            q=p[:k]+p[k+1:]
            if any(q[i]==q[i+1] for i in range(len(q)-1)):
                continue
            if not is_allowed(q,E):
                r=rows.setdefault(q,len(rows))
                triples.append((r,j,-1 if k%2 else 1))
    M=[[0]*len(P) for _ in range(len(rows))]
    for r,j,x in triples: M[r][j]+=x
    return P,rows,M

def rank_mod(M,p):
    if not M: return 0
    A=[[x%p for x in row] for row in M]
    r=0; n=len(A[0])
    for c in range(n):
        k=next((i for i in range(r,len(A)) if A[i][c]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(n)]
        r+=1
    return r

def expected_paths(m):
    A=[]
    for i in range(m):
        A += [
            ('s',('a',i),('b',i),('c',i),'t'),
            ('s',('a',i),('b',i),('c',(i+1)%m),'t'),
            ('s',('a',i),('b',(i+1)%m),('c',(i+1)%m),'t'),
            ('s',('a',i),('b',(i+1)%m),('c',(i+2)%m),'t'),
        ]
    return set(A)

def check_relation_rows(m, P, rows):
    # The only forbidden boundary terms are the five indexed families in the proof.
    expected=set()
    for i in range(m):
        expected.add(('s',('b',i),('c',i),'t'))
        expected.add(('s',('b',i),('c',(i+1)%m),'t'))
        expected.add(('s',('a',i),('c',(i+1)%m),'t'))
        expected.add(('s',('a',i),('b',i),'t'))
        expected.add(('s',('a',i),('b',(i+1)%m),'t'))
    assert set(rows)==expected

for m in range(3,25):
    P,rows,M=constraint_matrix(m)
    assert len(P)==4*m
    assert set(P)==expected_paths(m)
    assert len(rows)==5*m
    check_relation_rows(m,P,rows)
    d2=len(P)-rank_mod(M,2)
    d3=len(P)-rank_mod(M,3)
    d5=len(P)-rank_mod(M,5)
    assert d2==1
    if m%2:
        assert d3==0 and d5==0
    else:
        assert d3==1 and d5==1
print('CYCLIC_PATH_CHAIN_VERIFY_OK')
