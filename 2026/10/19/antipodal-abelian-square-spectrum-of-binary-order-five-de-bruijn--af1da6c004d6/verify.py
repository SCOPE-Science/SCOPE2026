#!/usr/bin/env python3
"""Independent exhaustive enumeration of full-period balanced cuts in order-five binary de Bruijn cycles."""
from collections import Counter,defaultdict
from fractions import Fraction

N=32
NEXT=[((2*v+b)&15) for v in range(16) for b in range(2)]

def canon(w):
    w=tuple(w)
    ww=w+w
    ix=[i for i in range(N) if ww[i:i+5]==(0,0,0,0,0)]
    assert len(ix)==1
    cut=(ix[0]+4)%N
    return w[cut:]+w[:cut]

def valid(w):
    if len(w)!=32 or sum(w)!=16:return False
    ww=w+w
    return {tuple(ww[i:i+5]) for i in range(32)}== {tuple((e>>j)&1 for j in (4,3,2,1,0)) for e in range(32)}

def score(w):
    ww=w+w
    pref=[0]
    for t in ww: pref.append(pref[-1]+t)
    return sum(pref[i+16]-pref[i]==8 for i in range(32))

def score_direct(w):
    return sum(sum(w[(i+j)%32] for j in range(16))==sum(w[(i+j)%32] for j in range(16,32)) for i in range(32))

def dfs_engine():
    found={}
    def visit(v,used,bits):
        if len(bits)==32:
            if v==0:
                w=tuple(bits)
                assert valid(w)
                assert w not in found
                found[w]=score(w)
            return
        for b in (0,1):
            e=2*v+b
            if not (used>>e)&1:
                visit(NEXT[e],used|(1<<e),bits+(b,))
    visit(0,1,(0,))
    return found

def pair_engine():
    found={}
    for assignment in range(65536):
        def successor(e):
            v=e&15
            b=((assignment>>v)&1) ^ ((e>>4)&1)
            return 2*v+b
        e=0
        bits=[]
        mask=0
        for _ in range(32):
            if mask>>e &1:break
            mask|=1<<e
            bits.append(e&1)
            e=successor(e)
        if e!=0 or mask != (1<<32)-1:continue
        w=tuple(bits)
        assert valid(w)
        assert w not in found
        found[w]=score_direct(w)
    return found

def symmetry_groups(found):
    orbits=[]
    unvisited=set(found)
    while unvisited:
        w=next(iter(unvisited))
        group={w,canon(tuple(1-x for x in w)),canon(w[::-1]),canon(tuple(1-x for x in w[::-1]))}
        # All cycle representatives use the same unique distinguished edge.
        assert group<=unvisited or group<=set(found)
        assert len({found[x] for x in group})==1
        unvisited-=group
        orbits.append((len(group),found[w],w))
    return orbits

def main():
    a=dfs_engine()
    b=pair_engine()
    assert len(a)==len(b)==2048 and a==b
    spectrum=Counter(a.values())
    assert all(v>0 and v%2==0 for v in spectrum)
    orbits=symmetry_groups(a)
    assert sum(length for length,_,_ in orbits)==2048
    print('spectrum:', sorted(spectrum.items()))
    print('orbit spectrum:',sorted(Counter((score,length) for length,score,_ in orbits).items()))
    mean=Fraction(sum(s*count for s,count in spectrum.items()),len(a))
    var=Fraction(sum((s-mean)**2*count for s,count in spectrum.items()),len(a))
    print('mean:',mean,'variance:',var,'orbitcount:',len(orbits))
    print('minimum example:', ''.join(map(str,next(w for w,s in a.items() if s==min(spectrum)))))
    print('maximum example:', ''.join(map(str,next(w for w,s in a.items() if s==max(spectrum)))))
    print('HALF_PERIOD_ABELIAN_DB5_PASS words=2048 switches=65536 orbits='+str(len(orbits)))

if __name__=='__main__':main()
