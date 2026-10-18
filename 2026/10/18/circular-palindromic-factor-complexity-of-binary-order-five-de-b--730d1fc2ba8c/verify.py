#!/usr/bin/env python3
"""Exact enumeration of circular palindromic factors of order-five binary de Bruijn cycles.
No external dependencies. Two distinct cycle generators and two palindrome algorithms.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv

ORDER=5
L=1<<ORDER
V=L//2

def normal(w):
    k=(w+w).find('0'*ORDER)
    assert 0<=k<L and (w+w).count('0'*ORDER)>0
    return w[k:]+w[:k]

def generate_euler():
    used=[False]*L
    used[0]=True
    path=[0]
    result=set()
    def visit(vertex):
        if len(path)==L:
            if vertex==0:
                s=''.join(str(edge%2) for edge in path)
                result.add(normal(s))
            return
        for edge in (2*vertex,2*vertex+1):
            if not used[edge]:
                used[edge]=True
                path.append(edge)
                visit(edge%V)
                path.pop()
                used[edge]=False
    visit(0)
    return result

def generate_pairings():
    result=set()
    for bits in range(1<<V):
        seen=set()
        edge=0
        trail=[]
        while edge not in seen:
            seen.add(edge)
            trail.append(edge)
            v=edge%V
            bit=(bits>>v)&1
            outgoing_choice=bit if edge==v else bit^1
            edge=2*v+outgoing_choice
        if len(seen)==L and edge==0:
            word=''.join(str(e%2) for e in trail)
            result.add(normal(word))
    return result

def palindromes_direct(w):
    ww=w+w
    return {ww[i:i+k] for i in range(L) for k in range(1,L+1)
            if ww[i:i+k]==ww[i:i+k][::-1]}

def palindromes_centers(w):
    p=set()
    for c in range(L):
        # Odd center c.
        r=0
        while 2*r+1<=L and w[(c-r)%L]==w[(c+r)%L]:
            p.add(''.join(w[j%L] for j in range(c-r,c+r+1)))
            r+=1
        # Even center between c-1 and c.
        r=1
        while 2*r<=L and w[(c-r)%L]==w[(c+r-1)%L]:
            p.add(''.join(w[j%L] for j in range(c-r,c+r)))
            r+=1
    return p

def orbit(w):
    rev=w[::-1]
    comp=''.join('1' if a=='0' else '0' for a in w)
    return {normal(u) for u in (w,rev,comp,comp[::-1])}

def main():
    A=generate_euler()
    B=generate_pairings()
    assert len(A)==len(B)==2048 and A==B
    assert all(len({(w+w)[i:i+ORDER] for i in range(L)})==L for w in A)
    histogram=Counter()
    profiles=Counter()
    orbitcounts=Counter()
    concrete={}
    for w in sorted(A):
        p1=palindromes_direct(w)
        p2=palindromes_centers(w)
        assert p1==p2, w
        # Every length through 5 has all possible binary palindromes.
        for k in range(1,6):
            assert sum(len(p)==k for p in p1)==2**((k+1)//2)
        n=len(p1)
        histogram[n]+=1
        concrete.setdefault(n,w)
        profiles[tuple(sum(len(p)==j for p in p1) for j in range(1,L+1))]+=1
    seen=set()
    for w in A:
        if w in seen: continue
        o=orbit(w)
        assert o<=A
        seen.update(o)
        n=len(palindromes_direct(w))
        for x in o:
            assert len(palindromes_direct(x))==n
        orbitcounts[(n,len(o))]+=1
    assert seen==A
    assert histogram=={22:32,23:32,24:200,27:192,28:920,29:544,30:128},histogram
    assert len(profiles)==51
    assert orbitcounts=={(22,2):4,(22,4):6,(23,4):8,(24,2):6,(24,4):47,(27,4):48,(28,2):14,(28,4):223,(29,4):136,(30,2):8,(30,4):28}
    assert sum(o*q for (n,o),q in orbitcounts.items())==2048
    folder=Path(__file__).resolve().parent
    with (folder/'spectrum.csv').open(newline='',encoding='utf-8') as fh:
        recorded=list(csv.DictReader(fh))
    assert len(recorded)==7
    for row in recorded:
        k=int(row['palindromic_factor_count'])
        assert int(row['cycles'])==histogram[k]
        assert int(row['symmetry_orbits_size2'])==orbitcounts.get((k,2),0)
        assert int(row['symmetry_orbits_size4'])==orbitcounts.get((k,4),0)
    with (folder/'profiles.csv').open(newline='',encoding='utf-8') as fh:
        recorded_profiles=list(csv.DictReader(fh))
    assert len(recorded_profiles)==len(profiles)==51
    for row in recorded_profiles:
        key=tuple(int(row['p%02d'%i]) for i in range(1,33))
        assert int(row['cycles'])==profiles[key]
    assert len({tuple(int(row['p%02d'%i]) for i in range(1,33)) for row in recorded_profiles})==51
    mean=Fraction(sum(k*v for k,v in histogram.items()),2048)
    var=Fraction(sum(k*k*v for k,v in histogram.items()),2048)-mean*mean
    print('VERIFY_OK DFS_cycle_count=2048 local_pairing_assignments=65536 same_cycle_sets=True direct_palindrome_vs_center_expansion=True cycle_count=2048 profile_count=51 palindrome_spectrum='+','.join('%d:%d'%x for x in sorted(histogram.items()))+' mean='+str(mean)+' variance='+str(var)+' symmetry_orbits='+str(sum(orbitcounts.values())))
    print('ORBIT_COUNTS',sorted(orbitcounts.items()))
    print('REPRESENTATIVES', sorted(concrete.items()))
    return histogram,orbitcounts,profiles
if __name__=='__main__':main()
