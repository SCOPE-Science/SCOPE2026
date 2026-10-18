#!/usr/bin/env python3
"""Self-contained exact verification of the Petersen component-size filtration.
Run: python3 verify.py [certificate.json]
All arithmetic is integer, including GF(2) matrix reduction.
"""
import collections
import itertools
import json
import pathlib
import sys

CERT = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).with_name('certificate.json')
obj=json.loads(CERT.read_text(encoding='utf-8'))
vertices=list(itertools.combinations(range(5),2))
assert obj['vertex_labels']==[''.join(str(x) for x in pair) for pair in vertices]
assert len(vertices)==10
adj=[]
for i,a in enumerate(vertices):
    adj.append(sum(1<<j for j,b in enumerate(vertices) if set(a).isdisjoint(b)))
assert all(x.bit_count()==3 for x in adj)
assert sum(x.bit_count() for x in adj)//2==15

def largest_component(mask):
    seen=0
    best=0
    while mask&~seen:
        seed=(mask&~seen)&-(mask&~seen)
        wave=seed
        seen|=seed
        total=0
        while wave:
            low=wave&-wave
            wave-=low
            idx=low.bit_length()-1
            total+=1
            new=adj[idx]&mask&~seen
            wave|=new
            seen|=new
        best=max(best,total)
    return best

level=[largest_component(m) for m in range(1<<10)]
assert level[0]==0
assert max(level)==10
assert all(level[f^(f&-f)]<=level[f] for f in range(1,1<<10))

EXPECTED={
    1:{0:1,2:4},
    2:{0:1,3:1},
    3:{0:1,3:1},
    4:{0:1,3:11},
    5:{0:1,4:61},
    6:{0:1,5:74},
    7:{0:1,6:36},
    8:{0:1,7:9},
    9:{0:1,8:1},
    10:{0:1}
}
EXPECTED_BARS={(2,1,2):4,(3,2,5):1,(3,4,5):10,
               (4,5,6):61,(5,6,7):74,(6,7,8):36,
               (7,8,9):9,(8,9,10):1}
assert [x['r'] for x in obj['records']]==list(range(1,11))

# Every row is certified through a sequence of elementary free-pair removals
# and critical facet removals. The removal order proves acyclicity.
for record in obj['records']:
    r=record['r']
    faces={m for m in range(1,1<<10) if level[m]<=r}
    alive=set(faces)
    critical=[]
    matched=0
    for step in record['steps']:
        if step[0]=='P':
            _,lower,upper=step
            assert lower in alive and upper in alive,(r,step)
            assert (lower&upper)==lower and (upper^lower).bit_count()==1,(r,step)
            current_cofaces=[lower|(1<<i) for i in range(10)
                             if not (lower>>i)&1 and (lower|(1<<i)) in alive]
            assert current_cofaces==[upper],(r,step,current_cofaces)
            alive.remove(lower)
            alive.remove(upper)
            matched+=1
        elif step[0]=='C':
            _,cell=step
            assert cell in alive,(r,step)
            assert not any((cell|(1<<i)) in alive for i in range(10)
                           if not (cell>>i)&1),(r,step)
            critical.append(cell)
            alive.remove(cell)
        else:
            raise AssertionError((r,step))
    assert not alive,(r,len(alive))
    assert 2*matched+len(critical)==len(faces)
    dims=dict(collections.Counter(f.bit_count()-1 for f in critical))
    assert dims==EXPECTED[r],(r,dims)
    print('Morse r=%d faces=%d pairs=%d critical=%s'%(r,len(faces),matched,dims))

# Independently compute the homology dimensions from the complete boundary
# matrices, without using the matching data.
def rank_mod2(columns):
    basis={}
    for col in columns:
        while col:
            pivot=col.bit_length()-1
            if pivot in basis:
                col^=basis[pivot]
            else:
                basis[pivot]=col
                break
    return len(basis)

for r in range(1,11):
    by_dim=collections.defaultdict(list)
    for m in range(1,1<<10):
        if level[m]<=r:
            by_dim[m.bit_count()-1].append(m)
    ranks={}
    for d in range(1,max(by_dim)+1):
        row={m:i for i,m in enumerate(by_dim[d-1])}
        cols=[]
        for face in by_dim[d]:
            boundary=0
            x=face
            while x:
                b=x&-x
                x-=b
                boundary^=1<<row[face^b]
            cols.append(boundary)
        ranks[d]=rank_mod2(cols)
    betti={d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
           for d in by_dim}
    betti[0]-=1
    betti={d:b for d,b in betti.items() if b}
    target={d:c for d,c in EXPECTED[r].items() if d>0}
    assert betti==target,(r,betti,target)
    print('Homology r=%d reduced_F2=%s'%(r,betti))

# Standard sorted boundary-matrix algorithm for persistence over F_2.
# Filter by largest connected component; break ties by face size then mask.
simplices=list(range(1,1<<10))
simplices.sort(key=lambda x:(level[x],x.bit_count(),x))
pos={m:j for j,m in enumerate(simplices)}
basis={}
paired=[]
births=[]
for j,m in enumerate(simplices):
    col=0
    x=m
    while x:
        b=x&-x
        x-=b
        if m^b:
            col^=1<<pos[m^b]
    while col:
        pivot=col.bit_length()-1
        if pivot in basis:
            col^=basis[pivot]
        else:
            basis[pivot]=col
            paired.append((pivot,j))
            break
    if col==0:
        births.append(j)
unpaired=set(births)-{p for p,_ in paired}
assert len(unpaired)==1
assert simplices[next(iter(unpaired))].bit_count()==1
bars=collections.Counter()
for p,j in paired:
    f,g=simplices[p],simplices[j]
    if level[f]<level[g]:
        bars[(f.bit_count()-1,level[f],level[g])]+=1
assert dict(bars)==EXPECTED_BARS,(bars,EXPECTED_BARS)
print('Persistent F2 positive-dimensional barcode:',sorted(bars.items()))
print('All exact checks passed.')
