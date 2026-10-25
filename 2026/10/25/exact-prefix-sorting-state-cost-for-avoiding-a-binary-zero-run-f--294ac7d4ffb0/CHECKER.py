#!/usr/bin/env python3
"""Reproducible finite stress tests for forbidden-factor prefix-sorting automata.

All assertions use exact finite strings and integer state identifiers. The theorem
for unbounded r follows from the mathematical proof, not from these tests.
"""
from itertools import product

def construct(r):
    A = [('A', j) for j in range(r+1)]
    B = [('B', j) for j in range(r)]
    order = A + B[::-1]
    edges = {}
    for j in range(r+1):
        edges[(('A',j),'0')] = ('A', min(j+1,r))
        if j < r:
            edges[(('A',j),'1')] = ('B',0)
    for j in range(r):
        edges[(('B',j),'0')] = ('B',j+1) if j+1<r else ('A',r)
        edges[(('B',j),'1')] = ('B',0)
    return order, edges

def step(word, edges):
    state=('A',0)
    for c in word:
        state=edges.get((state,c))
        if state is None:
            return None
    return state

def colexkey(w):
    return w[::-1]

def test(r):
    states, edges=construct(r)
    ix={state:i for i,state in enumerate(states)}
    assert len(states)==2*r+1
    for (u,a),v in edges.items():
        assert u in ix and v in ix
    for (u,a),v in edges.items():
        for (w,b),z in edges.items():
            if a<b:
                assert ix[v]<ix[z],(r,u,a,v,w,b,z)
            if a==b and ix[u]<ix[w]:
                assert ix[v]<=ix[z],(r,u,a,v,w,b,z)
    # Check language correctness, completion and state-fiber formula.
    nmax=min(2*r+5,14)
    for n in range(nmax+1):
        for bits in product('01',repeat=n):
            w=''.join(bits)
            st=step(w,edges)
            accepted=('0'*r+'1' not in w)
            assert (st is not None)==accepted,(r,w,st,accepted)
            if accepted:
                if st[0]=='A' and st[1]<r:
                    assert w=='0'*st[1]
                elif st==('A',r):
                    assert w.endswith('0'*r)
                else:
                    assert st[0]=='B' and w.endswith('1'+'0'*st[1])
    # Co-lex right-convexity obstruction of a minimal-DFA class.
    for j in range(r):
        u='0'*j; middle='0'*(j+1); v='1'+'0'*j
        assert colexkey(u)<colexkey(middle)<colexkey(v)
        assert step(u,edges)==('A',j)
        assert step(v,edges)==('B',j)
    # Right-language separators for ordinary DFA states.
    for i in range(r+1):
        for j in range(i+1,r+1):
            suffix='0'*(r-j)+'1'
            assert '0'*r+'1' in '0'*j+suffix
            assert '0'*r+'1' not in '0'*i+suffix
    return 2**(nmax+1)-1

if __name__=='__main__':
    total=0
    for r in range(1,11):
        examined=test(r)
        total+=examined
        print(f'r={r}: Wheeler states={2*r+1}, ordinary states={r+1}, accepted-word checks={examined}, edges and obstruction=OK')
    print('VERIFY_OK total checked words:',total)
