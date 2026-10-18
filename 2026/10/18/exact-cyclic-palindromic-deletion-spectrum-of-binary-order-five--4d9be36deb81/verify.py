#!/usr/bin/env python3
"""Exhaustive circular longest-palindromic-subsequence profiles of binary order-5 de Bruijn cycles."""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv

N=32

def pairing_cycles():
    result=set()
    for mask in range(1<<16):
        successor=[0]*32
        for vertex in range(16):
            toggle=(mask>>vertex)&1
            successor[vertex]=2*vertex+toggle
            successor[16+vertex]=2*vertex+1-toggle
        seen=0
        edge=0
        route=[]
        while not (seen>>edge)&1 and len(route)<N:
            seen|=1<<edge
            route.append(edge)
            edge=successor[edge]
        if edge==0 and len(route)==N:
            result.add(''.join(str(e>>4) for e in route))
    assert len(result)==2048
    return result

def euler_cycles():
    result=set()
    # Anchor the distinguished 00000 edge, ensuring one root per cycle.
    path=[0]
    def dfs(vertex,used):
        if len(path)==N:
            if vertex==0:
                result.add(''.join(str(e>>4) for e in path))
            return
        for e in (2*vertex,2*vertex+1):
            if not (used>>e)&1:
                path.append(e)
                dfs(e&15,used|(1<<e))
                path.pop()
    dfs(0,1)
    assert len(result)==2048
    return result

def palindromic_subsequence_dp(word):
    n=len(word)
    d=[[0]*n for _ in range(n)]
    for i in range(n): d[i][i]=1
    for size in range(2,n+1):
        for i in range(n-size+1):
            j=i+size-1
            if word[i]==word[j]:
                d[i][j]=2+(d[i+1][j-1] if size>2 else 0)
            else:
                d[i][j]=max(d[i+1][j],d[i][j-1])
    return d[0][-1]

def lcs_reverse(word):
    n=len(word)
    rev=word[::-1]
    last=[0]*(n+1)
    for a in word:
        now=[0]*(n+1)
        for j,b in enumerate(rev,1):
            now[j]=last[j-1]+1 if a==b else max(now[j-1],last[j])
        last=now
    return last[-1]

def literal_lps(word):
    best=0
    for mask in range(1 << len(word)):
        if mask.bit_count()<=best:
            continue
        subseq=''.join(ch for i,ch in enumerate(word) if (mask >> i) & 1)
        if subseq==subseq[::-1]:
            best=len(subseq)
    return best

def cyclic_invariant(word,method):
    return max(method(word[i:]+word[:i]) for i in range(len(word)))

def rotate_to_zero(word):
    return min(word[i:]+word[:i] for i in range(32))

def symmetries(word):
    return {rotate_to_zero(z) for z in (word,word[::-1],word.translate(str.maketrans('01','10')),word[::-1].translate(str.maketrans('01','10')))}

def run():
    pair=pairing_cycles()
    euler=euler_cycles()
    assert pair==euler
    # Exhaustive short-word reference against literal subsequence enumeration.
    for n in range(1,10):
        for value in range(1 << n):
            word=f'{value:0{n}b}'
            assert literal_lps(word)==palindromic_subsequence_dp(word)==lcs_reverse(word)
    table={}
    samples={}
    for w in sorted(pair):
        assert w.startswith('00000')
        assert len({(w+w)[i:i+5] for i in range(32)})==32
        val=cyclic_invariant(w,palindromic_subsequence_dp)
        other=cyclic_invariant(w,lcs_reverse)
        assert val==other,(w,val,other)
        table[w]=val
        samples.setdefault(val,w)
    hist=Counter(table.values())
    assert hist==Counter({25:76,26:114,27:1380,28:286,29:192})
    assert sum(hist.values())==len(pair)==2048
    mean=Fraction(sum(k*v for k,v in hist.items()),2048)
    var=sum(Fraction(v,2048)*(k-mean)**2 for k,v in hist.items())
    assert mean==Fraction(13925,512)
    assert var==Fraction(178215,262144)
    data_path=Path(__file__).with_name("spectrum.csv")
    with data_path.open(newline="",encoding="utf-8") as f:
        stored=list(csv.DictReader(f))
    assert len(stored)==2048
    assert {r["cycle"]:int(r["cyclic_lps"]) for r in stored}==table
    assert all(int(r["minimum_deletions"])==32-int(r["cyclic_lps"]) for r in stored)
    orbit_counts=defaultdict(lambda:Counter())
    unseen=set(pair)
    while unseen:
        w=min(unseen)
        orb=symmetries(w)
        assert orb<=pair
        assert len({table[x] for x in orb})==1
        unseen-=orb
        orbit_counts[table[w]][len(orb)]+=1
    assert sum(orb*cnt for by_size in orbit_counts.values() for orb,cnt in by_size.items())==2048
    assert sum(by_size[2] for by_size in orbit_counts.values())==32
    assert sum(by_size[4] for by_size in orbit_counts.values())==496
    assert {k:(by_size[2],by_size[4]) for k,by_size in orbit_counts.items()}=={
        25:(4,17),26:(1,28),27:(22,334),28:(5,69),29:(0,48)}
    print('VERIFY_OK cycles=2048 pairings=65536 DFS=2048 independent_LPS_methods=2 brute_binary_words_through_length9=yes de_bruijn_windows_checked=yes rotation_comparisons=65536 histogram='+','.join(f'{k}:{hist[k]}' for k in sorted(hist))+' mean='+str(mean)+' variance='+str(var)+' orbits='+repr(dict(orbit_counts)))
    print('WITNESSES',repr(samples))
    return hist,mean,var,dict(orbit_counts)
if __name__=='__main__':run()
