"""Exact directional illumination spectrum of equal-depth icosahedral truncations.

Only Python's standard library is required. Coefficients (a,b) mean a+b*phi,
where phi^2=phi+1. No floating-point comparisons occur.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import csv

ZERO = (0, 0)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def negate(a):
    return (-a[0], -a[1])

def mul(a, b):
    return (a[0]*b[0]+a[1]*b[1],
            a[0]*b[1]+a[1]*b[0]+a[1]*b[1])

def sign(a):
    """Exact sign of a[0]+a[1]*(1+sqrt(5))/2."""
    x, y = a
    q = 2*x+y
    if y == 0:
        return (x > 0) - (x < 0)
    if q == 0:
        return (y > 0) - (y < 0)
    if (q > 0) == (y > 0):
        return (q > 0) - (q < 0)
    if 5*y*y > q*q:
        return (y > 0) - (y < 0)
    return (q > 0) - (q < 0)

def dot(v, w):
    ans = ZERO
    for a,b in zip(v,w):
        ans = add(ans, mul(a,b))
    return ans

def vecsub(a,b):
    return [sub(x,y) for x,y in zip(a,b)]

def cross(a,b):
    return [sub(mul(a[1],b[2]), mul(a[2],b[1])),
            sub(mul(a[2],b[0]), mul(a[0],b[2])),
            sub(mul(a[0],b[1]), mul(a[1],b[0]))]

def icosahedron():
    v = []
    for x,y in product((-1,1), repeat=2):
        c=(x,0); d=(0,y)
        v.extend(([ZERO,c,d], [c,d,ZERO], [d,ZERO,c]))
    assert len(v)==12 and len({tuple(vv) for vv in v})==12
    norms={dot(w,w) for w in v}
    assert norms=={(2,1)}  # 1+phi^2=2+phi
    edges=[]
    for i,j in combinations(range(12),2):
        delta=vecsub(v[i],v[j])
        if dot(delta,delta)==(4,0):
            edges.append((i,j))
    assert len(edges)==30
    edge_set=set(edges)
    faces=[t for t in combinations(range(12),3)
           if all(e in edge_set for e in combinations(t,2))]
    assert len(faces)==20
    assert all(sum(e[0]==i or e[1]==i for e in edges)==5 for i in range(12))
    assert all(sum(i in f and j in f for f in faces)==2 for i,j in edges)
    return v,edges,faces

def data():
    vertices,edges,faces=icosahedron()
    normals=vertices + [[add(add(vertices[i][k],vertices[j][k]),vertices[l][k])
                           for k in range(3)] for i,j,l in faces]
    assert len(normals)==32 and all(any(t!=ZERO for t in n) for n in normals)
    # Every normal has its opposite, hence 16 distinct great circles.
    assert all(sum(tuple(v)==tuple(negate(x) for x in n) for v in normals)==1
               for n in normals)
    triples=[]; directed=[]
    for i,j in edges:
        f=[12+p for p,face in enumerate(faces) if i in face and j in face]
        assert len(f)==2
        triples.extend(((i,f[0],f[1]),(j,f[0],f[1])))
        directed.extend(((i,j),(j,i)))
    assert len(triples)==len(directed)==60
    # Independently reconstruct the 32 supporting facets and their incidence
    # at the regular one-third truncation, with coordinates scaled by 3.
    tpoints=[[add(mul((2,0),x),y) for x,y in zip(vertices[i],vertices[j])]
             for i,j in directed]
    incident=[set() for _ in range(60)]
    for f,n in enumerate(normals):
        values=[dot(n,p) for p in tpoints]
        top=values[0]
        for z in values[1:]:
            if sign(sub(z,top))>0:
                top=z
        face_verts=[h for h,z in enumerate(values) if z==top]
        assert len(face_verts)==(5 if f<12 else 6),(f,len(face_verts))
        x,y,z=(tpoints[h] for h in face_verts[:3])
        assert any(t!=ZERO for t in cross(vecsub(y,x),vecsub(z,x)))
        for h in face_verts:
            incident[h].add(f)
    assert all(incident[h]==set(triples[h]) for h in range(60))
    return normals,triples

def lit(signs,triples):
    return sum(all(signs[k]<0 for k in q) for q in triples)

def exact_cells(normals,triples):
    """All open chambers of the arrangement from 32 signed facet normals.

    Every chamber touches an intersection ray of two distinct normal planes.
    At such a ray u, each incident plane n gives two tangent half-rays
    +/-cross(u,n), each with two sides +/-n. Infinitesimal nested
    perturbations exhaust all local sectors, using lexicographic exact signs.
    """
    cells={}
    for i,j in combinations(range(len(normals)),2):
        c=cross(normals[i],normals[j])
        if all(x==ZERO for x in c):
            continue
        for u in (c,[negate(x) for x in c]):
            zero_signs=[sign(dot(n,u)) for n in normals]
            incident=[k for k,s in enumerate(zero_signs) if s==0]
            for k in incident:
                tangent=cross(u,normals[k])
                assert any(x!=ZERO for x in tangent)
                first=[sign(dot(n,tangent)) if zero_signs[a]==0 else 0
                       for a,n in enumerate(normals)]
                second=[sign(dot(n,normals[k]))
                        if zero_signs[a]==0 and first[a]==0 else 0
                        for a,n in enumerate(normals)]
                for h in (-1,1):
                    for side in (-1,1):
                        signs=tuple(zero_signs[a] or h*first[a] or side*second[a]
                                    for a in range(len(normals)))
                        assert all(x!=0 for x in signs)
                        cells[signs]=lit(signs,triples)
    return cells

def main():
    normals,triples=data()
    cells=exact_cells(normals,triples)
    distribution=Counter(cells.values())
    assert len(cells)==152
    assert distribution==Counter({20:132,21:20}),distribution
    for u,expected in (((1,1,1),21),((-2,0,1),20)):
        s=[sign(dot(n,[(a,0) for a in u])) for n in normals]
        assert all(s) and lit(s,triples)==expected,(u,lit(s,triples))
    table=sorted((''.join('+' if s>0 else '-' for s in signs),v)
                 for signs,v in cells.items())
    certificate=Path(__file__).with_name('cells.csv')
    if certificate.exists():
        with certificate.open(newline='',encoding='utf-8') as f:
            r=csv.reader(f)
            assert next(r)==['normal_signs','lit_vertices']
            assert [(row[0],int(row[1])) for row in r]==table
    else:
        raise FileNotFoundError('Required self-contained cells.csv certificate')
    print('EXACT_OK normals=32 great_circles=16 cells=152 spectrum_20=132 spectrum_21=20 max=21 fractional=20/7')

if __name__=='__main__':
    main()
