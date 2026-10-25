#!/usr/bin/env python3
"""Exact, standalone finite certificate checker for two order-four Latin-square complexes.
Standard library only; run `python3 verify.py` beside certificate.json.
The arrays encode cells as 4*row+column and faces as 16-bit integers.
"""
import json
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path

N=4
CELLS=range(N*N)

def symbols(kind):
    if kind=='cyclic': return lambda row,column:(row+column)%N
    if kind=='klein': return lambda row,column:row^column
    raise ValueError(kind)

def faces(kind):
    op=symbols(kind)
    faces=set()
    for k in range(5):
        for subset in combinations(CELLS,k):
            rows={v//4 for v in subset}
            columns={v%4 for v in subset}
            values={op(v//4,v%4) for v in subset}
            if len(rows)==len(columns)==len(values)==k:
                faces.add(sum(1<<v for v in subset))
    return faces

def faces_by_recursion(kind):
    op=symbols(kind)
    out=set()
    def go(next_cell, mask,rows,columns,values):
        out.add(mask)
        for v in range(next_cell,16):
            r,c=divmod(v,4);z=op(r,c)
            if (rows>>r)&1 or (columns>>c)&1 or (values>>z)&1:continue
            go(v+1,mask|(1<<v),rows|(1<<r),columns|(1<<c),values|(1<<z))
    go(0,0,0,0,0)
    return out

def dims(faces):
    hist=Counter(m.bit_count() for m in faces)
    return [hist.get(k,0) for k in range(5)]

def positions(mask):return [v for v in CELLS if mask>>v&1]

def codim_one_cofaces(face,complex_faces):
    return [face|1<<v for v in CELLS if not(face>>v&1) and (face|1<<v) in complex_faces]

def connected(vertices,edges):
    if not vertices:return False
    g=defaultdict(set)
    for a,b in edges:g[a].add(b);g[b].add(a)
    visited={next(iter(vertices))};stack=list(visited)
    while stack:
        for z in g[stack.pop()]:
            if z not in visited:visited.add(z);stack.append(z)
    return visited==set(vertices)

def incidence(tri,edge):
    assert tri.bit_count()==3 and edge.bit_count()==2 and (tri&edge)==edge
    return (-1)**positions(tri).index(next(v for v in positions(tri) if not(edge>>v&1)))

def orientable_surface(cyclic,cert_orientation):
    vertices={m for m in cyclic if m.bit_count()==1}
    edges={m for m in cyclic if m.bit_count()==2}
    triangles={m for m in cyclic if m.bit_count()==3}
    assert len(vertices)==16 and len(edges)==48 and len(triangles)==32
    assert not any(x.bit_count()>3 for x in cyclic)
    assert connected(set(CELLS),[tuple(positions(e)) for e in edges])
    certified={int(t):int(sign) for t,sign in cert_orientation}
    assert len(cert_orientation)==len(certified)==32
    assert set(certified)==triangles and set(certified.values())<= {-1,1}
    for e in edges:
        contained=[t for t in triangles if (t&e)==e]
        assert len(contained)==2
        a,b=contained
        assert certified[a]*incidence(a,e)==-certified[b]*incidence(b,e)
    for v in CELLS:
        adjacent=[x for x in CELLS if x!=v and (1<<v|1<<x) in cyclic]
        link_edges=[]
        for a,b in combinations(adjacent,2):
            if (1<<v|1<<a|1<<b) in cyclic:link_edges.append((a,b))
        degrees=Counter(x for pair in link_edges for x in pair)
        assert len(adjacent)==6 and len(link_edges)==6
        assert set(degrees)==set(adjacent) and set(degrees.values())=={2}
        assert connected(set(adjacent),link_edges)
    assert (len(vertices)-len(edges)+len(triangles))==0
    return (len(vertices),len(edges),len(triangles))

def check_collapses(klein,collapses):
    remaining=set(klein)
    assert len(collapses)==32
    for i,(low,high) in enumerate(collapses):
        assert low in remaining and high in remaining,('absent',i)
        assert high.bit_count()==low.bit_count()+1,('dimension',i)
        assert (low&high)==low,('containment',i)
        assert codim_one_cofaces(low,remaining)==[high],('not free',i)
        remaining.remove(low);remaining.remove(high)
    # Remaining faces form a graph and include all their subfaces.
    assert len(remaining)==len(klein)-64==41
    assert dims(remaining)==[1,16,24,0,0]
    for face in remaining:
        for v in positions(face):assert (face^(1<<v)) in remaining
    edgelist=[tuple(positions(e)) for e in remaining if e.bit_count()==2]
    assert connected(set(CELLS),edgelist)
    return len(edgelist)-16+1

def reduced_squares():
    first=tuple(range(4))
    row_options={r:[p for p in permutations(range(4)) if p[0]==r] for r in range(1,4)}
    out=[]
    for r1 in row_options[1]:
        for r2 in row_options[2]:
            for r3 in row_options[3]:
                square=(first,r1,r2,r3)
                if all(len({square[row][column] for row in range(4)})==4 for column in range(4)):
                    out.append(square)
    assert len(out)==4
    return out

def isotopy(square,kind):
    target=symbols(kind)
    # Source rows and columns are mapped independently to target rows/columns;
    # all 16 positions then uniquely constrain the symbol permutation.
    for rp in permutations(range(4)):
        for cp in permutations(range(4)):
            sm=[None]*4
            ok=True
            for row in range(4):
                for column in range(4):
                    s=square[row][column]
                    wanted=target(rp[row],cp[column])
                    if sm[s] is not None and sm[s]!=wanted:
                        ok=False;break
                    sm[s]=wanted
                if not ok:break
            if ok and len(set(sm))==4:
                assert all(target(rp[r],cp[c])==sm[square[r][c]] for r in range(4) for c in range(4))
                return [list(rp),list(cp),sm]
    return None

def check_order_four_classification():
    classes=Counter(); rows=[]
    for square in reduced_squares():
        is_c=isotopy(square,'cyclic')
        is_v=isotopy(square,'klein')
        assert bool(is_c)!=bool(is_v)
        kind='cyclic' if is_c else 'klein'
        classes[kind]+=1
        rows.append({'square':[list(r) for r in square], 'kind':kind,'isotopy':is_c or is_v})
    assert classes=={'cyclic':3,'klein':1}
    return rows

def check():
    p=Path(__file__).with_name('certificate.json')
    cert=json.loads(p.read_text(encoding='utf-8'))
    assert cert['schema_version']==1 and set(cert)=={'schema_version','orientation','collapses','reduced_isotopies'}
    cyclic,klein=faces('cyclic'),faces('klein')
    assert cyclic==faces_by_recursion('cyclic')
    assert klein==faces_by_recursion('klein')
    assert dims(cyclic)==[1,16,48,32,0]
    assert dims(klein)==[1,16,48,32,8]
    fv=orientable_surface(cyclic,cert['orientation'])
    rank=check_collapses(klein,cert['collapses'])
    assert rank==9
    assert check_order_four_classification()==cert['reduced_isotopies']
    # Fully enumerate both groups' full transversals.
    assert sum(m.bit_count()==4 for m in cyclic)==0
    assert sum(m.bit_count()==4 for m in klein)==8
    print('ORDER4_SQUARES=4 REDUCED_CLASSES=cyclic:3,klein:1')
    print('CYCLIC_FACE_COUNTS=[1,16,48,32,0]')
    print('CYCLIC_CLOSED_CONNECTED_ORIENTED_SURFACE_EULER=0 GENUS=1')
    print('KLEIN_FACE_COUNTS=[1,16,48,32,8]')
    print('KLEIN_ELEMENTARY_COLLAPSES=32 GRAPH_VERTICES=16 GRAPH_EDGES=24 CIRCLE_RANK=9')
    print('FULL_TRANSVERSALS=cyclic:0,klein:8')
    print('VERIFY_OK')

if __name__=='__main__':check()
