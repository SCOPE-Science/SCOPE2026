#!/usr/bin/env python3
"""Reproduce the length-resolved indistinguishability classification over S_3.
No external packages. Word alphabet is 0,1; group permutations act on 0,1,2.
"""
from itertools import permutations, product
from pathlib import Path

EXPECTED = [1,2,4,8,15,26,41,60,84,108,133,148,159,162]

def step(state, n, letter):
    r,t,u,v=state  # count(0) mod 6 and three mod-3 affine coefficients
    if letter == 0 or letter == '0':
        return ((r+1)%6,(t+(1 if (n-r)%2==0 else -1))%3,u,
                (v+(1 if n%2==0 else -1))%3)
    return (r,t,(u+(1 if r%2==0 else -1))%3,v)

def signature(word):
    state=(0,0,0,0)
    for i,c in enumerate(word): state=step(state,i,c)
    return state

def compressed_census():
    frontier={(0,0,0,0):''}
    result=[len(frontier)]
    representatives={0:dict(frontier)}
    for n in range(1,14):
        nxt={}
        for state, w in sorted(frontier.items()):
            for c in (0,1):
                t=step(state,n-1,c)
                nw=w+str(c)
                if t not in nxt or nw<nxt[t]: nxt[t]=nw
        frontier=nxt
        representatives[n]=dict(frontier)
        result.append(len(frontier))
    assert result==EXPECTED,(result,EXPECTED)
    assert set(frontier)==set(product(range(6),range(3),range(3),range(3)))
    assert len(representatives[12])==159
    return result,representatives

def raw_permutation_signature(w, perms, table, assignments):
    out=[]
    for j,k in assignments:
        p=0  # identity is lexicographically first permutation
        for c in w: p=table[p][j if c=='0' else k]
        out.append(p)
    return tuple(out)

def independent_census(rep):
    perms=list(permutations(range(3)))
    table=[]
    for a in perms:
        table.append([perms.index(tuple(a[b[i]] for i in range(3))) for b in perms])
    assignments=list(product(range(6),repeat=2))
    words=['']
    raw_counts=[]
    for n in range(14):
        signatures={}
        comp_to_raw={}
        raw_to_comp={}
        for w in words:
            c=signature(w)
            x=raw_permutation_signature(w,perms,table,assignments)
            assert c not in comp_to_raw or comp_to_raw[c]==x
            assert x not in raw_to_comp or raw_to_comp[x]==c
            comp_to_raw[c]=x
            raw_to_comp[x]=c
            signatures.setdefault(x,w)
        assert len(signatures)==EXPECTED[n],(n,len(signatures))
        assert len(comp_to_raw)==EXPECTED[n]
        raw_counts.append(len(signatures))
        words=[w+s for w in words for s in '01']
    return raw_counts

def validate_certificate(reps, certificate):
    lines=Path(certificate).read_text(encoding='utf-8').splitlines()
    assert lines[0]=='r\tt\tu\tv\tword'
    rows={}
    for line in lines[1:]:
        a,b,c,d,w=line.split('\t')
        state=(int(a),int(b),int(c),int(d))
        assert len(w)==13 and set(w)<={'0','1'}
        assert signature(w)==state
        assert state not in rows
        rows[state]=w
    assert len(rows)==162
    assert rows==reps[13]

if __name__=='__main__':
    result,reps=compressed_census()
    assert independent_census(reps)==result
    validate_certificate(reps,Path(__file__).with_name('CERTIFICATE.tsv'))
    # A letter operation is a permutation of the full 162-state signature universe.
    universe=set(product(range(6),range(3),range(3),range(3)))
    for parity in (0,1):
        for c in (0,1):
            assert {step(x,parity,c) for x in universe}==universe
    print('counts(n=0..13):',result)
    print('full signatures first attained at n=13:',len(reps[13]))
    print('all transitions bijective; counts=162 for every n>=13')
    print('certificate: 162 distinct full-length witnesses verified')
    print('independent raw S3^36 evaluation: passed')
