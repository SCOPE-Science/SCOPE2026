#!/usr/bin/env python3
"""Finite support checks for pure-edge directed cycles with pendant in-leaves.
No finite enumeration is used as an infinite-classification proof.
"""
from itertools import product, combinations
from math import gcd


def graph(word):
    m=len(word)
    edges=set()
    n=m
    parents=[]
    for i,b in enumerate(word):
        edges.add((i,(i+1)%m))
        for _ in range(b):
            edges.add((n,i)); parents.append(i); n+=1
    return n,edges


def profile(word):
    n,edges=graph(word); m=len(word)
    vertex_types=lambda v: 'core' if v<m else 'leaf'
    ans={}
    for i in range(n):
        p=set((vertex_types(j),i==j,(i,j) in edges,(j,i) in edges,(j,j) in edges) for j in range(n))
        if vertex_types(i) in ans: assert ans[vertex_types(i)]==p
        else: ans[vertex_types(i)]=p
    return frozenset((t,frozenset(s)) for t,s in ans.items())


def theoretical_phase(word):
    m=len(word)
    if m==1: return 'loop-one' if word[0]==1 else 'loop-many'
    return 'double' if m==2 else 'triple' if m==3 else 'long'



def totient(n):
    return sum(gcd(j,n)==1 for j in range(1,n+1))


def necklace_count(length,alphabet):
    return sum(totient(d)*alphabet**(length//d) for d in range(1,length+1) if length%d==0)//length


def key(word):
    return min(tuple(word[i:]+word[:i]) for i in range(len(word)))


def check():
    cnt=0; classes={}
    for length in range(1,7):
        for word in product((1,2,3),repeat=length):
            word=list(word);p=profile(word);phase=theoretical_phase(word)
            if phase in classes: assert classes[phase]==p,(word,phase)
            else: classes[phase]=p
            cnt+=1
    assert len(classes)==5 and len(set(classes.values()))==5
    print('2-variable stationary extension profiles:',cnt,'directed coronas; exactly five profiles: PASS')
    num=0
    for length in range(1,7):
        for k in range(1,6):
            words={key(list(word)) for word in product(range(1,k+1),repeat=length)}
            assert len(words)==necklace_count(length,k)
            num+=1
    print('Necklace orbit counts by Burnside:',num,'independent enumerations: PASS')
    localized=0
    samples = [[1], [2], [3], [4], [5], [1,1], [2,3], [3,2],
               [1,2,3], [3,1,2], [1,4,5], [5,3,1,2], [2,2,2,2]]
    for word in samples:
        length=len(word);n,E=graph(word)
        for root in range(length):
            child=[v for v in range(length,n) if (v,root) in E]
            for r in range(1,5):
                if r==4:
                    witnessed=any(all(any((u,w) in E and (v,w) in E for w in range(n))
                                        for u in old for v in (new,))
                                    for old in combinations(child,3)
                                    for new in range(length,n) if new not in old)
                else:
                    witnessed=any(all((v,root) in E for v in cs)
                                  for cs in combinations(range(length,n),r))
                assert witnessed==(word[root]>=r),(word,root,r)
                localized+=1
    print('Recycled-anchor local child-count witnesses:',localized,'tests: PASS')

if __name__=='__main__':check()
