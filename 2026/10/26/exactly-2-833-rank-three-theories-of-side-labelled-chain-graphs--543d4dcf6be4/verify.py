#!/usr/bin/env python3
"""Independent replay of a finite rank-three classification certificate.

Input: certificate.json in the same directory. Uses only Python standard library.
The proof also requires the elementary EF preservation and chain-word lemmas
written in RESULT.md; computation alone does not establish either lemma.
"""
import json
from pathlib import Path
from collections import deque, Counter
from functools import lru_cache
from itertools import product

HERE=Path(__file__).resolve().parent

def graph(word):
    """A new 0-vertex is in part A and isolated; a new 1-vertex in B
    is adjacent to all existing A vertices. """
    sides=[]; rows=[]
    for digit in word:
        i=len(rows)
        if digit=='0':
            rows.append(0); sides.append(0)
        elif digit=='1':
            r=0
            for j in range(i):
                if sides[j]==0:
                    rows[j]|=1<<i
                    r|=1<<j
            rows.append(r);sides.append(1)
        else:raise ValueError('bad word')
    return tuple(rows),tuple(sides)

def type3(word):
    """Three-round Hintikka invariant for graph with unary A/B.
    For a marked a, record the complete set of one-step extensions
    of every ordered pair (a,b); its own pair (a,a) is special.
    """
    rows,sides=graph(word);n=len(rows)
    vs=set()
    for a in range(n):
        ra=rows[a]
        mask_a=0
        for c in range(n):
            if c!=a:mask_a |= 1<<(2*sides[c]+((ra>>c)&1))
        out=set()
        for b in range(n):
            if b==a:continue
            rb=rows[b];mask=0
            for c in range(n):
                if c==a or c==b:continue
                mask|=1<<(4*sides[c]+2*((ra>>c)&1)+((rb>>c)&1))
            out.add((sides[b],(ra>>b)&1,mask))
        vs.add(((sides[a],mask_a),tuple(sorted(out))))
    return tuple(sorted(vs))

def independent_type3(word):
    """Generic finite-structure Hintikka recursion from atomic diagrams.
    This function does not use the specialized pair-mask formula.
    """
    rows,sides=graph(word);n=len(rows)
    @lru_cache(None)
    def t(seq,remaining):
        atoms=(tuple(sides[v] for v in seq),
               tuple((i,j) for i in range(len(seq)) for j in range(i+1,len(seq)) if seq[i]==seq[j]),
               tuple((i,j) for i in range(len(seq)) for j in range(i+1,len(seq)) if (rows[seq[i]]>>seq[j])&1))
        if remaining==0:return atoms
        return (atoms,frozenset(t(seq+(v,),remaining-1) for v in range(n)))
    return t((),3)

def generate():
    words=['']; typ_to_id={type3(''):0};trans=[]
    head=0
    while head<len(words):
        w=words[head];sub=[]
        for digit in '01':
            nw=w+digit;tp=type3(nw)
            if tp not in typ_to_id:
                typ_to_id[tp]=len(words);words.append(nw)
            sub.append(typ_to_id[tp])
        trans.append(sub);head+=1
    return {'schema_version':1,'signature':'unary A, unary B, undirected simple cross-edge E',
            'words':words,'transitions':trans}

def verify():
    c=json.loads((HERE/'certificate.json').read_text('utf-8'))
    assert c['schema_version']==1
    words=c['words']; trans=c['transitions']
    assert len(words)==2833==len(trans)
    assert words[0]=='' and len(set(words))==len(words)
    assert all(len(w)<=21 for w in words)
    assert Counter(map(len,words))[21]==2
    lookup={type3(w):i for i,w in enumerate(words)}
    assert len(lookup)==len(words),'two representatives share a complete rank-three type'
    for i,w in enumerate(words):
        assert len(trans[i])==2
        for j,d in enumerate('01'):
            assert trans[i][j]==lookup[type3(w+d)], (i,d)
    dist=[None]*len(words);dist[0]=0;queue=deque([0])
    while queue:
        i=queue.popleft()
        for j in trans[i]:
            if dist[j] is None: dist[j]=dist[i]+1;queue.append(j)
    assert all(dist[i]==len(words[i]) for i in range(len(words)))
    assert all(d is not None for d in dist)
    # A completely different implementation of the Hintikka rank-three recursion.
    test_idx={i for i,w in enumerate(words) if len(w)<=7}
    test_idx.update(range(0,len(words),43))
    test_idx.update(i for i,w in enumerate(words) if len(w)>=20)
    independent={}
    for i in sorted(test_idx):
        tp=independent_type3(words[i])
        assert tp not in independent,(i,independent.get(tp))
        independent[tp]=i
    # Check that short input words not retained as representatives land in
    # the claimed state and both implementations give an equivalent type.
    for k in range(0,12):
        for tup in product('01',repeat=k):
            w=''.join(tup);state=0
            for ch in w:state=trans[state][int(ch)]
            assert type3(w)==type3(words[state])
    for k in range(0,7):
        for tup in product('01',repeat=k):
            w=''.join(tup);state=0
            for ch in w:state=trans[state][int(ch)]
            assert independent_type3(w)==independent_type3(words[state])
    cnt=Counter(len(w) for w in words)
    print('VERIFY_OK')
    print('states',len(words),'transitions',2*len(words),'maximum minimum representative order',max(cnt))
    print('states at 21',cnt[21],'witnesses',[w for w in words if len(w)==21])
    print('minimal-order histogram',str(dict(sorted(cnt.items()))))
    print('independent generic Hintikka representatives checked',len(test_idx))
    print('all input words of length <= 11: specialized oracle and transitions agree')
    print('all input words of length <= 6: generic oracle and transitions agree')

if __name__=='__main__':
    verify()
