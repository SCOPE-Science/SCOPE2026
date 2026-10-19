"""Full automorphism action on minimum zero forcing sets of the Shrikhande graph.

Usage: python scripts/verify_orbits.py [--write-certificate]
The certificate path is relative to this file's package directory.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import csv
import sys
from verify_simulation import graph, closure

POINTS=[(a,b) for a in range(4) for b in range(4)]
INDEX={v:i for i,v in enumerate(POINTS)}
CONN={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
ROOT=Path(__file__).resolve().parent.parent
CERT=ROOT/'certificates'/'shrikhande_minimum_orbits.csv'

def automorphisms():
    matrices=[]
    for a,b,c,d in product(range(4),repeat=4):
        if {((a*x+b*y)%4,(c*x+d*y)%4) for x,y in CONN}==CONN:
            matrices.append((a,b,c,d))
    assert len(matrices)==12
    maps=[]
    for a,b,c,d in matrices:
        for p,q in POINTS:
            m=tuple(INDEX[((a*x+b*y+p)%4,(c*x+d*y+q)%4)]
                    for x,y in POINTS)
            maps.append(m)
    assert len(set(maps))==192
    A=graph('shrikhande')
    for m in maps:
        assert len(set(m))==16
        for x in range(16):
            assert {m[u] for u in A[x]}==set(A[m[x]])
    # Upper bound for the full automorphism group: the six neighbors of vertex 0
    # induce a 6-cycle; the nine other vertices have distinct two-element
    # neighborhoods within that cycle. Thus a stabilizer embeds into D_6.
    root_neigh=set(A[0]); other=[v for v in range(16) if v!=0 and v not in root_neigh]
    assert len(other)==9
    assert len({tuple(sorted(root_neigh.intersection(A[v]))) for v in other})==9
    sub={v:root_neigh.intersection(A[v]) for v in root_neigh}
    assert all(len(sub[v])==2 for v in root_neigh)
    discovered={next(iter(root_neigh))};frontier=list(discovered)
    while frontier:
        v=frontier.pop()
        for u in sub[v]:
            if u not in discovered: discovered.add(u);frontier.append(u)
    assert discovered==root_neigh  # Connected 2-regular local graph: a six-cycle.
    assert len(maps)==16*12
    return maps

def image(mask,p):
    out=0
    while mask:
        one=mask&-mask;mask-=one
        out|=1<<p[one.bit_length()-1]
    return out

def connected_components(mask,A):
    unseen={i for i in range(16) if mask>>i&1};component_sizes=[]
    while unseen:
        start=unseen.pop();stack=[start];c=1
        while stack:
            v=stack.pop()
            for u in A[v]:
                if u in unseen:
                    unseen.remove(u);stack.append(u);c+=1
        component_sizes.append(c)
    return '+'.join(map(str,sorted(component_sizes)))

def rows():
    A=graph('shrikhande');maps=automorphisms()
    white_six={W for W in range(1<<16) if W.bit_count()==6 and
               closure(65535^W,A)[0]==65535}
    assert len(white_six)==3616
    output=[]
    while white_six:
        rep=min(white_six)
        orb={image(rep,p) for p in maps}
        assert orb<=white_six
        white_six-=orb
        e=sum(1 for u in range(16) if (rep>>u)&1
              for v in A[u] if u<v and (rep>>v)&1)
        time=closure(65535^rep,A)[1]
        output.append({'white_mask_hex':f'{rep:04x}',
                       'orbit_size':len(orb),
                       'white_induced_edges':e,
                       'white_components':connected_components(rep,A),
                       'synchronous_rounds':time})
    assert len(output)==23
    assert Counter(int(r['orbit_size']) for r in output)=={192:15,96:7,64:1}
    assert sum(int(r['orbit_size']) for r in output)==3616
    assert Counter({2:sum(int(r['orbit_size']) for r in output if int(r['synchronous_rounds'])==2),
                    3:sum(int(r['orbit_size']) for r in output if int(r['synchronous_rounds'])==3)})=={2:1312,3:2304}
    return output

def main():
    computed=rows()
    if '--write-certificate' in sys.argv:
        CERT.parent.mkdir(parents=True,exist_ok=True)
        with CERT.open('w',encoding='utf-8',newline='') as f:
            wr=csv.DictWriter(f,fieldnames=list(computed[0]))
            wr.writeheader();wr.writerows(computed)
    with CERT.open(encoding='utf-8',newline='') as f:
        recorded=list(csv.DictReader(f))
    assert recorded==[{k:str(v) for k,v in r.items()} for r in computed]
    print('VERIFY_ORBITS_OK affine_automorphisms=192 full_group_order=192')
    print('VERIFY_ORBITS_OK minimum_orbits=23 spectrum=192x15+96x7+64')
    print('VERIFY_ORBITS_OK certificate_complete=23_rows minimum_sets=3616 time_2=1312 time_3=2304')

if __name__=='__main__':main()
