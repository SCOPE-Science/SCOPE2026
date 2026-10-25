"""Exact, standalone enumeration of ternary three-mer minimum decycling sets.
Python 3, standard library only. Reads no external files. It also regenerates two CSV certificates.
"""
from itertools import product, permutations
from collections import Counter
from pathlib import Path
import csv

Q=3; K=3; V=Q**K
ALL=(1<<V)-1

def digits(x):
    return (x//9,(x//3)%3,x%3)

def index(t):
    return 9*t[0]+3*t[1]+t[2]

def neighbors(u):
    return tuple((u%9)*3+j for j in range(Q))

def rotate(u):
    return (u%9)*3+u//9

def necklace_cycles():
    seen=set(); out=[]
    for v in range(V):
        if v in seen: continue
        walk=[]; cur=v
        while cur not in seen:
            seen.add(cur);walk.append(cur);cur=rotate(cur)
        assert cur==v
        out.append(tuple(walk))
    return tuple(out)

def short_cycles(length):
    distinct=set()
    for raw in product(range(Q),repeat=length):
        triplets=tuple(index(tuple(raw[(i+j)%length] for j in range(K))) for i in range(length))
        if len(set(triplets))==length:
            distinct.add(sum(1<<v for v in triplets))
    return tuple(sorted(distinct))

def topological_longest_path(removed):
    present=ALL^removed
    indeg=[0]*V
    for u in range(V):
        if present>>u&1:
            for v in neighbors(u):
                if present>>v&1:indeg[v]+=1
    fifo=[v for v in range(V) if present>>v&1 and indeg[v]==0]
    dist=[1]*V;count=0
    while count<len(fifo):
        u=fifo[count];count+=1
        for v in neighbors(u):
            if present>>v&1:
                dist[v]=max(dist[v],dist[u]+1)
                indeg[v]-=1
                if indeg[v]==0:fifo.append(v)
    if count!=present.bit_count(): return None
    return max((dist[v] for v in fifo),default=0)

def symmetry_images(mask):
    out=set()
    for sigma in permutations(range(Q)):
        for reverse in (False,True):
            new=0
            for v in range(V):
                if mask>>v&1:
                    d=digits(v)
                    if reverse:d=d[::-1]
                    new|=1<<index(tuple(sigma[j] for j in d))
            out.add(new)
    return out

def pattern(mask):
    return ' '.join(''.join(map(str,digits(v))) for v in range(V) if mask>>v&1)

def word_mask(word):
    mask=0
    for i in range(len(word)-2):
        mask|=1<<index(word[i:i+3])
    return mask

def main():
    necklaces=necklace_cycles()
    assert len(necklaces)==11
    assert Counter(map(len,necklaces))=={1:3,3:8}
    short2=short_cycles(2)
    short4=short_cycles(4)
    assert len(short2)==3 and len(short4)==18
    classification=Counter(); accepted={}; forbidden=short2+short4
    for transversal in product(*necklaces):
        removed=sum(1<<v for v in transversal)
        assert removed.bit_count()==11
        shortest_obstruction=2 if any(removed&cyc==0 for cyc in short2) else (4 if any(removed&cyc==0 for cyc in short4) else 0)
        long=topological_longest_path(removed)
        if shortest_obstruction==0:
            assert long in (6,7)
            accepted[removed]=long
            classification[('acyclic',long)]+=1
        else:
            assert long is None
            classification[('cyclic',shortest_obstruction)]+=1
    assert sum(classification.values())==6561
    assert classification=={('acyclic',6):60,('acyclic',7):24,('cyclic',2):5436,('cyclic',4):1041}
    remaining=set(accepted);orbits=[]
    while remaining:
        head=min(remaining)
        images=symmetry_images(head)
        assert images<=remaining
        assert len({accepted[x] for x in images})==1
        remaining-=images
        orbits.append((min(images),accepted[head],len(images)))
    orbits.sort(key=lambda o:(o[1],o[0]))
    assert len(orbits)==7
    assert [size for rep,L,size in orbits]==[12]*7
    assert [L for rep,L,size in orbits]==[6]*5+[7]*2
    assert [hex(rep) for rep,L,size in orbits]==['0x40321f9','0x403a1d9','0x403a5c3','0x40b25c3','0x413ae05','0x413283d','0x413a81d']
    # Independent direct enumeration of every ternary word of lengths 8, 9, 10.
    # A surviving directed path with h vertices corresponds to a word length h+2.
    avoid_counts={}
    for length in (8,9,10):
        occ=Counter(word_mask(word) for word in product(range(Q),repeat=length))
        avoid_counts[length]={mask:sum(count for observed,count in occ.items() if observed&mask==0) for mask in accepted}
    for mask,L in accepted.items():
        assert avoid_counts[8][mask]>0
        if L==6:
            assert avoid_counts[9][mask]==0
        else:
            assert avoid_counts[9][mask]>0
        assert avoid_counts[10][mask]==0
    target=Path(__file__).resolve().parent
    with (target/'min_decycling_sets.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f,lineterminator='\n')
        writer.writerow(['mask_hex','removed_three_mers','max_avoiding_windows','shortest_guaranteed_word_length','symmetry_class'])
        reps=[set(symmetry_images(rep)) for rep,L,size in orbits]
        for mask,L in sorted(accepted.items()):
            oi=next(i for i,o in enumerate(reps) if mask in o)
            writer.writerow([hex(mask),pattern(mask),L,L+3,oi+1])
    with (target/'short_cycles.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f,lineterminator='\n')
        writer.writerow(['length','vertex_mask_hex','vertex_three_mers'])
        for length,candidates in ((2,short2),(4,short4)):
            for mask in candidates:
                writer.writerow([length,hex(mask),pattern(mask)])
    print('TERNARY_3MER_MDS_PASS candidates=6561 optimum=11 minima=84 latency9=60 latency10=24 symmetry_orbits=7 short_cycles=3+18')
    for i,(rep,L,size) in enumerate(orbits,1):
        print(f'orbit={i} size={size} shortest_guaranteed_length={L+3} rep={hex(rep)} patterns={pattern(rep)}')

if __name__=='__main__':main()
