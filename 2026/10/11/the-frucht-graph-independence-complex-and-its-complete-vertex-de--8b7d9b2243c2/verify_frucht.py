"""Finite Morse certificates for the Frucht-graph independence complexes.

Python 3 standard library; run: python verify_frucht.py
"""
from collections import Counter, deque

EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
NEIGHBORS = [set() for _ in range(12)]
for u,v in EDGES:
    NEIGHBORS[u].add(v); NEIGHBORS[v].add(u)
assert len(EDGES)==18 and all(len(a)==3 for a in NEIGHBORS)
FULL_ORDER=[7,10,0,2,1,5,11,4,9,8,3,6]
DEL_ORDER={
0:[9,5,8,1,7,2,3,0,6,10,4],1:[10,1,9,6,3,4,7,8,5,0,2],
2:list(range(11)),3:list(range(11)),4:list(range(11)),
5:[0,4,7,5,2,1,10,6,9,8,3],6:list(range(11)),7:list(range(11)),
8:list(range(11)),9:[10,6,5,1,7,0,3,4,2,9,8],10:list(range(11)),
11:[3,6,7,8,9,2,4,10,1,5,0]}
LINK_ORDER={
0:list(range(8)),1:list(range(8)),2:[0,7,5,4,6,2,3,1],
3:list(range(8)),4:[3,2,5,1,7,4,0,6],5:list(range(8)),
6:[1,3,0,4,6,2,5,7],7:[1,2,7,5,0,4,3,6],
8:list(range(8)),9:list(range(8)),10:[2,7,0,4,5,3,1,6],
11:[1,2,3,6,0,7,4,5]}
EXPECTED_DEL={0:2,1:2,2:4,3:3,4:3,5:2,6:3,7:2,8:4,9:2,10:2,11:3}
EXPECTED_LINK={0:('sphere',1),1:('sphere',1),2:('sphere',2),
3:('collapsible',0),4:('collapsible',0),5:('sphere',1),
6:('collapsible',0),7:('sphere',1),8:('sphere',2),
9:('sphere',1),10:('sphere',1),11:('collapsible',0)}


def faces_on(nodes):
    nodes=list(nodes); local={x:i for i,x in enumerate(nodes)}
    adj=[sum(1<<local[v] for v in NEIGHBORS[u] if v in local) for u in nodes]
    faces=[0]
    for i in range(len(nodes)):
        faces += [s|(1<<i) for s in faces if not (s & adj[i])]
    assert len(faces)==len(set(faces))
    return set(faces)


def certificate(nodes,order,kind,vertex=None):
    faces=faces_on(nodes)
    assert set(order)==set(range(len(nodes))) and len(order)==len(nodes)
    available=set(faces); matches={}
    for i in order:
        bit=1<<i
        for lower in sorted(tuple(available)):
            upper=lower|bit
            if not lower&bit and upper in available:
                available.remove(lower);available.remove(upper)
                matches[lower]=upper
    assert len(matches)*2+len(available)==len(faces)
    # The augmented empty face is paired to one 0-face. Remove its pair
    # before checking the usual nonaugmented discrete Morse orientation.
    if 0 in matches:
        matched_vertex=matches.pop(0)
        assert matched_vertex.bit_count()==1
        available.add(matched_vertex)
    assert 0 not in available
    counts=Counter(f.bit_count()-1 for f in available)
    assert counts.get(0)==1
    if kind=='full':
        assert len(faces)==169 and counts=={0:1,2:3}
    elif kind=='deletion':
        assert counts=={0:1,2:EXPECTED_DEL[vertex]}
    elif kind=='link':
        typ,k=EXPECTED_LINK[vertex]
        assert counts==({0:1,k:1} if typ=='sphere' else {0:1})
    # Hasse orientation: matched edges upward, unmatched downward.
    nonempty=faces-{0}
    indeg={x:0 for x in nonempty}
    arrows={x:[] for x in nonempty}
    incidences=0
    for big in nonempty:
        t=big
        while t:
            # Delete current bit directly, without changing big.
            low=big^(t&-t)
            t-=t&-t
            if low==0:continue
            if matches.get(low)==big:
                src,dst=low,big
            else:src,dst=big,low
            arrows[src].append(dst); indeg[dst]+=1;incidences+=1
    queue=deque(x for x,d in indeg.items() if not d)
    removed=0
    while queue:
        x=queue.popleft();removed+=1
        for y in arrows[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert removed==len(nonempty), ('cyclic Morse orientation',kind,vertex)
    # To prove actual simplicial collapsibility for candidate link cases,
    # exhaustively remove elementary free-face/coface pairs.
    if kind=='link' and EXPECTED_LINK[vertex][0]=='collapsible':
        remain=set(nonempty)
        while len(remain)>1:
            maximal={x for x in remain if not any(y!=x and x&y==x for y in remain)}
            free=None
            for upper in sorted(maximal):
                for bit in range(upper.bit_length()):
                    lower=upper^(1<<bit)
                    if lower==0 or lower not in remain:continue
                    if sum(1 for y in maximal if lower&y==lower)==1:
                        free=(lower,upper);break
                if free:break
            assert free is not None,('no free face',vertex,len(remain))
            remain.difference_update(free)
        assert len(remain)==1 and next(iter(remain)).bit_count()==1
    print(kind,vertex,'faces',len(faces)-1,'incidences',incidences,
          'Morse pairs',len(matches),'critical',dict(sorted(counts.items())))
    return counts

def main():
    full=certificate(range(12),FULL_ORDER,'full')
    counts={}
    for v in range(12):
        d=certificate([i for i in range(12) if i!=v],DEL_ORDER[v], 'deletion',v)
        l=certificate([i for i in range(12) if i!=v and i not in NEIGHBORS[v]],
                      LINK_ORDER[v],'link',v)
        counts[v]=(d,l)
    assert set(v for v,(d,l) in counts.items() if EXPECTED_LINK[v][0]=='collapsible')=={3,4,6,11}
    print('FRUCHT_MORSE_CERTIFICATE_OK')
if __name__=='__main__':main()
