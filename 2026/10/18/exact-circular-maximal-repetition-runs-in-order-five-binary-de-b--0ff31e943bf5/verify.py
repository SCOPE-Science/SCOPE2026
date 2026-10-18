#!/usr/bin/env python3
"""Exhaustive, independently replayable circular-run census for binary B(2,5)."""
import csv
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

N = 32
EXPECTED = {(0,2):16, (1,1):224, (1,2):128, (2,0):768, (2,1):608, (2,2):304}

def canonical(w):
    return min(w[t:]+w[:t] for t in range(len(w)))

def dfs_cycles():
    """All Eulerian edge trails starting at the distinguished five-bit edge 00000."""
    result = set()
    path = [0]
    def visit(vertex, used):
        if used == (1 << 32)-1:
            if vertex == 0:
                bits = ''.join(str(edge & 1) for edge in path)
                assert bits.count('1') == 16
                result.add(canonical(bits))
            return
        for bit in (0,1):
            edge = 2 * vertex + bit
            if not (used >> edge) & 1:
                path.append(edge)
                visit(edge & 15, used | (1 << edge))
                path.pop()
    visit(0, 1)
    return result

def pairing_cycles():
    """Independently enumerate all 2^16 pairings of incident edges."""
    result = set()
    singles = 0
    for mask in range(1 << 16):
        next_edge = [0]*32
        for vertex in range(16):
            flip = (mask >> vertex) & 1
            next_edge[vertex] = 2 * vertex + flip
            next_edge[vertex + 16] = 2 * vertex + (1-flip)
        route = []
        visited = 0
        edge = 0
        while not (visited >> edge) & 1:
            route.append(edge)
            visited |= 1 << edge
            edge = next_edge[edge]
        if len(route)==32 and edge==0:
            singles += 1
            word = ''.join(str(e & 1) for e in route)
            result.add(canonical(word))
    assert singles==2048
    return result

def period_of(s,p):
    return all(s[j]==s[j+p] for j in range(len(s)-p))

def extension_runs(w):
    """Maximal extension of each 2p square, using the periodic infinite word."""
    found=set()
    for start in range(N):
        for p in range(1,5):
            if any(w[(start+j)%N]!=w[(start+j+p)%N] for j in range(p)):
                continue
            length=2*p
            while length < N and w[(start+length)%N]==w[(start+length-p)%N]:
                length+=1
            if w[(start-1)%N]==w[(start+p-1)%N]:
                continue
            factor=''.join(w[(start+j)%N] for j in range(length))
            if not any(period_of(factor,q) for q in range(1,p)):
                found.add((start,length,p))
    return found

def brute_runs(w):
    """Independent interval/period search with two-sided extension tests."""
    found=set()
    for start in range(N):
        for length in range(2,9):
            segment=''.join(w[(start+j)%N] for j in range(length))
            short=[]
            for p in range(1,length//2+1):
                if period_of(segment,p):
                    short.append(p)
            if not short:
                continue
            p=min(short)
            if p>4:
                continue
            left=(w[(start-1)%N]==w[(start+p-1)%N])
            right=(w[(start+length)%N]==w[(start+length-p)%N])
            if not left and not right:
                found.add((start,length,p))
    return found

def valid_cycle(w):
    assert len(w)==32 and set(w)=={'0','1'}
    factors={''.join(w[(i+j)%32] for j in range(5)) for i in range(32)}
    return len(factors)==32

def orbit(w):
    complement=lambda s: ''.join('1' if ch=='0' else '0' for ch in s)
    return {canonical(s) for s in (w, w[::-1],complement(w),complement(w[::-1]))}

def main():
    lhs=dfs_cycles(); rhs=pairing_cycles()
    assert lhs==rhs and len(lhs)==2048
    hist=Counter(); count_hist=Counter(); len2_hist=Counter()
    period_length=Counter(); seen_orbits=set(); orbit_profile=Counter()
    rows=[]
    for w in sorted(lhs):
        assert valid_cycle(w)
        found=extension_runs(w)
        assert found==brute_runs(w), ('RUN_METHOD_MISMATCH',w,found,brute_runs(w))
        profile=[sum(p==j for _,_,p in found) for j in range(1,5)]
        assert profile[:2]==[8,2]
        cell=tuple(profile[2:]); hist[cell]+=1
        count_hist[len(found)]+=1
        lengths2=tuple(sorted(length for _,length,p in found if p==2))
        assert lengths2 in {(4,6),(5,5)}
        len2_hist[lengths2]+=1
        for _,length,p in found:period_length[(p,length)]+=1
        rows.append((w,*profile,len(found),'-'.join(map(str,lengths2))))
        orbit_id=min(orbit(w))
        if orbit_id not in seen_orbits:
            members=orbit(w)
            assert all(x in lhs for x in members)
            seen_orbits.add(orbit_id)
            orbit_profile[(cell,len(members))]+=1
    assert hist==EXPECTED, hist
    assert count_hist==Counter({12:1008,13:736,14:304}), count_hist
    assert len2_hist==Counter({(4,6):1536,(5,5):512})
    assert period_length==Counter({(1,2):8192,(1,3):4096,(1,5):4096,(2,4):1536,(2,5):1024,(2,6):1536,(3,6):1792,(3,7):1920,(4,8):1728})
    assert len(seen_orbits)==528
    assert orbit_profile==Counter({((0,2),2):4,((0,2),4):2,((1,1),4):56,((1,2),4):32,((2,0),2):20,((2,0),4):182,((2,1),2):4,((2,1),4):150,((2,2),2):4,((2,2),4):74})
    count=Fraction(sum(k*v for k,v in count_hist.items()),2048)
    variance=Fraction(sum(k*k*v for k,v in count_hist.items()),2048)-count*count
    assert count==Fraction(405,32) and variance==Fraction(535,1024)
    file=Path(__file__).with_name('profiles.csv')
    with file.open(newline='',encoding='utf-8') as f:
        reader=csv.reader(f)
        header=next(reader)
        assert header==['cycle','runs_p1','runs_p2','runs_p3','runs_p4','total_runs','period2_lengths']
        loaded=[(r[0],*map(int,r[1:6]),r[6]) for r in reader]
    assert loaded==rows
    print('VERIFY_OK cycles=2048 DFS_generator=yes pairing_assignments=65536 pairing_generator=yes')
    print('VERIFY_OK all_five_bit_factors=yes two_independent_cyclic_run_enumerators=yes')
    print('VERIFY_OK cells=' + ','.join(f'{a}-{b}:{hist[a,b]}' for a,b in sorted(hist)))
    print('VERIFY_OK total_runs=12:1008,13:736,14:304 mean=405/32 variance=535/1024')
    print('VERIFY_OK period2_lengths=4+6:1536,5+5:512 symmetry_orbits=528')
    print('VERIFY_OK file_rows=2048 and period_length_incidence_all_exact')

if __name__=='__main__':main()
