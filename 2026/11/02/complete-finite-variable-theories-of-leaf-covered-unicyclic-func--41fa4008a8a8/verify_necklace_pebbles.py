#!/usr/bin/env python3
"""Exact unrestricted-depth k-variable type refinement on finite test graphs.
Colors all k-tuples by atomic type, then by substitution-possible color sets.
A stable partition is the greatest fixed point of the k-pebble game.
"""
from itertools import product


def graph(word):
    m=len(word);n=m+sum(word)
    E=[[False]*n for _ in range(n)]
    u=m
    for i,b in enumerate(word):
        E[i][(i+1)%m]=True
        for _ in range(b):E[u][i]=True;u+=1
    return E


def types(words,k,max_rounds=60):
    graphs=[graph(word) for word in words]
    tuples=[list(product(range(len(E)),repeat=k)) for E in graphs]
    maps=[{p:i for i,p in enumerate(tt)} for tt in tuples]
    def canon(signatures):
        names={}; cc=[]
        for row in signatures:
            new=[]
            for sig in row:
                if sig not in names:names[sig]=len(names)
                new.append(names[sig])
            cc.append(new)
        return cc
    colors=canon([[tuple([t[i]==t[j] for i in range(k) for j in range(i+1,k)]+
                         [E[t[i]][t[j]] for i in range(k) for j in range(k)])
                    for t in tt] for E,tt in zip(graphs,tuples)])
    for round_number in range(max_rounds):
        signatures=[]
        for E,tt,ix,cc in zip(graphs,tuples,maps,colors):
            n=len(E); row=[]
            for t,c in zip(tt,cc):
                available=tuple(tuple(sorted({cc[ix[t[:j]+(w,)+t[j+1:]]] for w in range(n)}))
                                for j in range(k))
                row.append((c,available))
            signatures.append(row)
        refined=canon(signatures)
        if refined==colors:break
        colors=refined
    else:raise RuntimeError('type refinement did not stabilize')
    return [frozenset(cc) for cc in colors],round_number


def predicted(w,k):
    if k==1:
        return ('loop' if len(w)==1 else 'nonloop')
    if k==2:
        n=len(w)
        return ('one-one' if w[0]==1 else 'one-many') if n==1 else ('two' if n==2 else 'three' if n==3 else 'long')
    v=tuple(min(x,k) for x in w)
    return min(v[j:]+v[:j] for j in range(len(v)))


def check_set(words,k):
    cc,rounds=types(words,k)
    pred=[predicted(w,k) for w in words]
    for i in range(len(words)):
        for j in range(i):
            assert (cc[i]==cc[j])==(pred[i]==pred[j]),(k,words[i],words[j])
    return rounds,len(set(cc))


def main():
    words=[list(t) for l in range(1,7) for t in product((1,2),repeat=l)]
    words.extend([[1,3],[3,1],[2,3],[3,2],[1,1,3],[1,3,1],[3,1,1],[1,3,3],[3,1,3]])
    rounds,classes=check_set(words,2)
    print('FO^2: words',len(words),'stable rounds',rounds,'classes',classes,'PASS')
    words=[list(t) for l in range(1,4) for t in product((1,2,3),repeat=l)]
    words += [[1,2,4],[1,2,3],[1,3,2],[1,3,4],[1,3,3],[1,4,1],[1,3,1],
              [1,2,2,1],[1,2,3,1],[2,1,2,3],[1,3,2,1],[2,2,2,2],[2,3,3,3]]
    rounds,classes=check_set(words,3)
    print('FO^3: words',len(words),'stable rounds',rounds,'classes',classes,'PASS')
    # Targeted four-pebble threshold, rotation, orientation, and neighbor checks.
    pairs=[([1,3],[1,4],False),([1,4],[1,5],True),([2,4],[4,2],True),
           ([1,2],[1,3],False),([1,3,4],[1,3,5],True),
           ([1,3,4],[1,4,3],False),([4],[5],True),([3],[4],False)]
    for a,b,expect in pairs:
        colors,_=types([a,b],4)
        assert (colors[0]==colors[1])==expect,(a,b,expect)
    print('FO^4: targeted pairwise refinements',len(pairs),'PASS')

if __name__=='__main__':main()
