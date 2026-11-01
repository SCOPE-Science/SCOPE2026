#!/usr/bin/env python3
"""Exact finite verification for the ordinary matching complex of a 3-by-8 grid.

No nonstandard dependencies. Run with Python >= 3.9: python verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import comb

WIDTH = 8
EXPECTED_F = (37, 584, 5161, 28191, 99183, 227262, 335396, 308330, 165871, 46801, 5580, 153)

def grid_edges(width):
    return tuple(e for r in range(3) for c in range(width) for e in ([(r*width+c,(r+1)*width+c)] if r<2 else []) + ([(r*width+c,r*width+c+1)] if c<width-1 else []))

def build_faces(edges):
    vertex_masks = tuple((1<<a)|(1<<b) for a,b in edges)
    faces = []
    def visit(i, occupied, mask):
        if i==len(edges):
            if mask: faces.append(mask)
            return
        visit(i+1, occupied, mask)
        if not (occupied & vertex_masks[i]):
            visit(i+1, occupied | vertex_masks[i], mask | (1<<i))
    visit(0,0,0)
    return faces

def boundary(face):
    offset=0
    bits=face
    while bits:
        v=bits & -bits
        yield face^v, -1 if offset%2 else 1
        bits^=v
        offset+=1

def greedy_matching(faces, edge_count):
    remaining=set(faces)
    pairs=[]
    for pivot in range(edge_count):
        bit=1<<pivot
        local=[]
        for f in remaining:
            if not (f&bit) and (f|bit) in remaining:
                local.append((f,f|bit))
        for low,high in local:
            remaining.remove(low)
            remaining.remove(high)
        pairs.extend(local)
    return pairs, remaining

def verify_acyclic(faces, pairs):
    lower_to_upper=dict(pairs)
    indeg={f:0 for f in faces}
    incidence_count=0
    for upper in faces:
        for lower,_ in boundary(upper):
            if not lower: continue
            incidence_count+=1
            if lower_to_upper.get(lower)==upper:
                indeg[upper]+=1
            else:
                indeg[lower]+=1
    queue=deque(f for f,d in indeg.items() if d==0)
    processed=0
    while queue:
        face=queue.popleft()
        processed+=1
        matched_upper=lower_to_upper.get(face)
        if matched_upper is not None:
            indeg[matched_upper]-=1
            if indeg[matched_upper]==0:queue.append(matched_upper)
        for lower,_ in boundary(face):
            if lower and lower_to_upper.get(lower)!=face:
                indeg[lower]-=1
                if indeg[lower]==0:queue.append(lower)
    assert processed==len(faces), (processed,len(faces),'cycle in reversed Hasse graph')
    return incidence_count

def critical_boundary(pairs, critical):
    crit_low=sorted(f for f in critical if f.bit_count()==8)
    crit_high=sorted(f for f in critical if f.bit_count()==9)
    lowidx={f:i for i,f in enumerate(crit_low)}
    matched={low:(high,next(s for f,s in boundary(high) if f==low))
             for low,high in pairs if low.bit_count()==8 and high.bit_count()==9}
    @lru_cache(None)
    def expand(face):
        if face in lowidx:return ((lowidx[face],1),)
        if face not in matched:return ()
        upper,inc=matched[face]
        result=defaultdict(int)
        for other,sgn in boundary(upper):
            if other==face:continue
            for key,value in expand(other):result[key]-=inc*sgn*value
        return tuple(sorted((k,v) for k,v in result.items() if v))
    mat=[[0]*len(crit_high) for _ in crit_low]
    for col,high in enumerate(crit_high):
        for low,sgn in boundary(high):
            for row,value in expand(low):mat[row][col]+=sgn*value
    return mat,crit_low,crit_high,expand.cache_info()

def unimodular_unit_reduction(matrix):
    a=[r[:] for r in matrix]
    rows=len(a); cols=len(a[0])
    pivots=[]
    for k in range(cols):
        candidate=next(((i,j) for i in range(k,rows) for j in range(k,cols) if abs(a[i][j])==1),None)
        assert candidate is not None, ('no unit pivot',k)
        i,j=candidate
        a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        if a[k][k]==-1:a[k]=[-x for x in a[k]]
        for i in range(k+1,rows):
            z=a[i][k]
            if z:
                for j in range(k,cols):a[i][j]-=z*a[k][j]
        for j in range(k+1,cols):
            z=a[k][j]
            if z:
                for i in range(k,rows):a[i][j]-=z*a[i][k]
        pivots.append((k,1))
    assert all(a[i][j]==(1 if i==j else 0) for i in range(rows) for j in range(cols))
    return len(pivots)

def independent_matching_counts(width):
    # Monomer/dimer transfer independent of the face enumeration and edge sorting.
    # Store used vertices at the current column, and track matched edges by number.
    dp={(0,0):1}
    for col in range(width):
        nex=defaultdict(int)
        def fill(occupied, outgoing, position, weight, ways):
            if position==3:
                nex[(outgoing,weight)]+=ways
                return
            bit=1<<position
            if occupied&bit:
                fill(occupied,outgoing,position+1,weight,ways)
                return
            fill(occupied|bit,outgoing,position+1,weight,ways)
            if position<2 and not (occupied & (bit<<1)):
                fill(occupied|bit|(bit<<1),outgoing,position+1,weight+1,ways)
            if col<width-1:
                fill(occupied|bit,outgoing|bit,position+1,weight+1,ways)
        for (incoming,weight),ways in dp.items():fill(incoming,0,0,weight,ways)
        dp=nex
    counts=Counter()
    for (outgoing,weight),ways in dp.items():
        assert outgoing==0
        counts[weight]+=ways
    return counts

def main():
    edges=grid_edges(WIDTH)
    assert len(edges)==37 and len(set(edges))==37
    faces=build_faces(edges)
    assert len(faces)==1222549
    counts=Counter(f.bit_count() for f in faces)
    assert tuple(counts[k] for k in range(1,13))==EXPECTED_F
    transfer=independent_matching_counts(WIDTH)
    assert transfer[0]==1 and tuple(transfer[k] for k in range(1,13))==EXPECTED_F
    pairs,crit=greedy_matching(faces,len(edges))
    critical_dims=Counter(f.bit_count()-1 for f in crit)
    assert dict(critical_dims)=={0:1,7:112,8:18}
    assert len(pairs)==611209 and len(crit)==131
    assert 2*len(pairs)+len(crit)==len(faces)
    incidences=verify_acyclic(faces,pairs)
    assert incidences==8827379 # excluding the 37 vertices' empty faces
    mat,cl,ch,stats=critical_boundary(pairs,crit)
    assert len(cl)==112 and len(ch)==18
    nonzero=sum(v!=0 for row in mat for v in row)
    assert nonzero==182 and max(abs(v) for row in mat for v in row)==1
    pivots=unimodular_unit_reduction(mat)
    assert pivots==18
    reduced_euler=sum((-1)**i*EXPECTED_F[i] for i in range(len(EXPECTED_F)))-1
    assert reduced_euler==-94
    print('VERIFY_OK edges=37 faces=1222549 f_vector='+str(EXPECTED_F))
    print('VERIFY_OK transfer_counts=agreement pairs=611209 critical=(1_0,112_7,18_8)')
    print('VERIFY_OK hasse_incidences='+str(incidences)+' dag_vertices=1222549')
    print('VERIFY_OK integer_morse_differential=112x18 nonzero=182 unit_pivots=18')
    print('VERIFY_OK homotopy=vee_94_S7 reduced_euler=-94')

if __name__=='__main__':main()
