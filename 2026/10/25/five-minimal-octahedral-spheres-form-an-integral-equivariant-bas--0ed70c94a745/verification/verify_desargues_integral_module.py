#!/usr/bin/env python3
"""Exact standalone finite certificate for Desargues independence homology.

Requires only Python 3 standard library. Face order and orientations are fixed here.
"""
import collections
import itertools
import json
from pathlib import Path

FIVE=tuple(range(5))
LABELS=list(itertools.combinations(FIVE,2))+list(itertools.combinations(FIVE,3))
LABEL_TO_VERTEX={lab:i for i,lab in enumerate(LABELS)}
EDGES=sorted((i,j) for i in range(10) for j in range(10,20)
             if set(LABELS[i]) <= set(LABELS[j]))
assert len(EDGES)==30
adj=[0]*20
for u,v in EDGES:
    adj[u]|=1<<v
    adj[v]|=1<<u

# Face order: ascending vertex insertion, with descending face cardinality updates.
faces=[[0]]
for v in range(20):
    faces.append([])
    for cardinality in range(v,-1,-1):
        faces[cardinality+1].extend(face|(1<<v)
                                    for face in faces[cardinality]
                                    if (adj[v]&face)==0)
faces=faces[:11]
assert tuple(len(group) for group in faces)==(1,20,160,660,1510,1924,1320,480,115,20,2)
index=[{face:i for i,face in enumerate(group)} for group in faces]

def vertex_indices(mask):
    return [i for i in range(20) if mask>>i&1]

def boundary(cardinality):
    return [{index[cardinality-1][mask^(1<<v)]:(-1)**position
             for position,v in enumerate(vertex_indices(mask))}
            for mask in faces[cardinality]]

def compose_zero(upper,lower):
    for col in upper:
        acc=collections.defaultdict(int)
        for mid,coefficient in col.items():
            for row,coeff2 in lower[mid].items():
                acc[row]+=coefficient*coeff2
        assert all(v==0 for v in acc.values())

def mod_rank(columns,p):
    pivots={}
    for column in columns:
        col={row:coef%p for row,coef in column.items() if coef%p}
        while col:
            row=min(col)
            coefficient=col[row]
            if row not in pivots:
                inverse=pow(coefficient,-1,p)
                pivots[row]={i:(v*inverse)%p for i,v in col.items()}
                break
            for i,v in pivots[row].items():
                new=(col.get(i,0)-coefficient*v)%p
                if new:col[i]=new
                else:col.pop(i,None)
    return len(pivots)

def compatible(e,f):
    return all(x!=y and not (adj[x]>>y&1) for x in e for y in f)

neighbors={i:{j for j in range(i+1,30) if compatible(e,EDGES[j])}
           for i,e in enumerate(EDGES)}
matchings=[(i,) for i in range(30)]
matching_counts=[len(matchings)]
for size in range(2,8):
    matchings=[t+(j,) for t in matchings
               for j in neighbors[t[-1]]
               if all(j in neighbors[h] for h in t)]
    matching_counts.append(len(matchings))
    if not matchings:
        break
assert matching_counts==(30,255,700,615,42,5,0) or matching_counts==[30,255,700,615,42,5,0]
# Rebuild the five size-six matchings, since size seven is empty.
matchings=[(i,) for i in range(30)]
for size in range(2,7):
    matchings=[t+(j,) for t in matchings
               for j in neighbors[t[-1]] if all(j in neighbors[h] for h in t)]
assert len(matchings)==5
canonical=[]
for excluded in FIVE:
    seq=[]
    for two in itertools.combinations((q for q in FIVE if q!=excluded),2):
        a=LABEL_TO_VERTEX[two]
        b=LABEL_TO_VERTEX[tuple(sorted(two+(excluded,)))]
        seq.append(EDGES.index((a,b)))
    canonical.append(tuple(sorted(seq)))
assert sorted(matchings)==sorted(canonical)

def sphere_cycle(edge_numbers):
    coefficient=collections.defaultdict(int)
    pairs=[EDGES[e] for e in edge_numbers]
    for orientation in range(64):
        vertices=[pair[orientation>>j&1] for j,pair in enumerate(pairs)]
        inversions=sum(a>b for j,a in enumerate(vertices)
                            for b in vertices[j+1:])
        face=sum(1<<v for v in vertices)
        coefficient[index[6][face]]+=(-1)**(inversions+orientation.bit_count())
    return {j:v for j,v in coefficient.items() if v}

spheres=[sphere_cycle(x) for x in canonical]
assert all(len(z)==64 and set(z.values())<={-1,1} for z in spheres)

def check_cycles(lower):
    for z in spheres:
        acc=collections.defaultdict(int)
        for j,v in z.items():
            for i,w in lower[j].items():acc[i]+=v*w
        assert all(x==0 for x in acc.values())

def exact_det_unit_certificate(columns,certificate):
    columns_used=certificate['cols']
    rows_used=certificate['rows']
    n=len(columns_used)
    assert n==388 and len(rows_used)==n
    assert len(set(columns_used))==len(set(rows_used))==388
    assert max(columns_used)<len(columns) and max(rows_used)<len(faces[6])
    local_rows={r:i for i,r in enumerate(rows_used)}
    rows={i:{} for i in range(n)}
    coldata={j:{} for j in range(n)}
    for j,original_col in enumerate(columns_used):
        for global_row,value in columns[original_col].items():
            if global_row in local_rows:
                i=local_rows[global_row]
                rows[i][j]=value
                coldata[j][i]=value
    sign=1
    steps=0
    while rows:
        optimal=None
        selected=None
        for j,c in coldata.items():
            for i,a in c.items():
                if a not in (-1,1):continue
                cost=(len(c)-1)*(len(rows[i])-1)
                if optimal is None or cost<optimal:
                    optimal=cost
                    selected=(i,j,a)
                    if cost==0:break
            if optimal==0:break
        assert selected is not None, 'integer determinant certificate failed: no unit pivot'
        i,j,a=selected
        sign *= a * (-1)**(sum(k<i for k in rows)+sum(k<j for k in coldata))
        row_i=rows[i].copy()
        col_j=coldata[j].copy()
        for k,b in col_j.items():
            if k==i:continue
            for ell,c in row_i.items():
                if ell==j:continue
                new=rows[k].get(ell,0)-b*a*c
                if new:
                    rows[k][ell]=new
                    coldata[ell][k]=new
                else:
                    rows[k].pop(ell,None)
                    coldata[ell].pop(k,None)
            rows[k].pop(j,None)
        for ell in row_i:
            coldata[ell].pop(i,None)
        del rows[i]
        del coldata[j]
        steps+=1
    assert steps==388 and sign==certificate['det'] and abs(sign)==1
    return sign,steps

def map_cycle(chain,transform):
    out=collections.defaultdict(int)
    for i,c in chain.items():
        vertices=vertex_indices(faces[6][i])
        mapped=[transform[v] for v in vertices]
        inv=sum(a>b for j,a in enumerate(mapped) for b in mapped[j+1:])
        mask=sum(1<<v for v in mapped)
        out[index[6][mask]]+=(-1)**inv*c
    return {j:v for j,v in out.items() if v}

def verify_symmetry():
    swap=[LABEL_TO_VERTEX[tuple(v for v in FIVE if v not in a)] for a in LABELS]
    for p in itertools.permutations(FIVE):
        vertex_map=[LABEL_TO_VERTEX[tuple(sorted(p[v] for v in lab))] for lab in LABELS]
        for i,z in enumerate(spheres):
            assert map_cycle(z,vertex_map)==spheres[p[i]]
            assert map_cycle(z,[swap[vertex_map[j]] for j in range(20)])=={
                r:-c for r,c in spheres[p[i]].items()}
    # Each symmetry is realized by a graph automorphism.
    for transform in ([swap]+[[LABEL_TO_VERTEX[tuple(sorted(p[v] for v in lab))]
                                for lab in LABELS]
                                for p in ((1,0,2,3,4),(1,2,3,4,0))]):
        assert {tuple(sorted((transform[a],transform[b]))) for a,b in EDGES}==set(EDGES)
    return 240

def main():
    d5=boundary(5)
    d6=boundary(6)
    d7=boundary(7)
    d8=boundary(8)
    compose_zero(d7,d6)
    compose_zero(d8,d7)
    check_cycles(d6)
    rk5=mod_rank(d6,101)
    rk6=mod_rank(d7,101)
    rk7=mod_rank(d8,101)
    assert (rk5,rk6,rk7)==(932,383,97)
    assert mod_rank(d7+spheres,2)==388
    certificate=json.loads((Path(__file__).parent/'CERTIFICATE.json').read_text('utf-8'))
    determinant,steps=exact_det_unit_certificate(d7+spheres,certificate)
    assert all(i in certificate['cols'] for i in range(480,485))
    symmetries=verify_symmetry()
    print('FACE_CARDINALITY_COUNTS',tuple(len(x) for x in faces))
    print('INDUCED_MATCHINGS_COUNTS_BY_SIZE',matching_counts)
    print('FIVE_12_VERTEX_MINIMAL_OCTAHEDRA',len(spheres),'SUPPORT_FACES_PER_CYCLE',64)
    print('BOUNDARY_RANK_LOWER_BOUNDS_MOD_101',rk5,rk6,rk7)
    print('COMPLEMENTARY_RANK_UPPER_BOUNDS',1320-388,480-97)
    print('AUGMENTED_IMAGE_RANK_AND_UNIT_MINOR',388,determinant,'EXACT_UNIT_PIVOTS',steps)
    print('INTEGRAL_H5_BASIS_RANK',5)
    print('PERMUTATION_AND_COMPLEMENT_ACTIONS_CHECKED',symmetries)
    print('VERIFY_OK_DESARGUES_FIVE_MINIMAL_SPHERES_INTEGRAL_S5_C2_MODULE')

if __name__=='__main__':main()
