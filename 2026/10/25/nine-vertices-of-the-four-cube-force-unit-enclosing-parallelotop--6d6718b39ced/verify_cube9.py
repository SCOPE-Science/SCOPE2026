"""Standard-library exact verifier for the four-cube nine-vertex width-polar certificate.
Run from a directory containing cube9_width_polars.json:
    python verify_cube9.py
No numeric optimization, floating-point arithmetic, or third-party modules are used.
"""
import json
from itertools import combinations,permutations
from math import comb
from pathlib import Path


def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def det4(a):
    return sum((-1)**i*a[0][i]*det3([[a[r][c] for c in range(4) if c!=i] for r in range(1,4)][0],
                                       [[a[r][c] for c in range(4) if c!=i] for r in range(1,4)][1],
                                       [[a[r][c] for c in range(4) if c!=i] for r in range(1,4)][2]) for i in range(4))


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def cross4(a,b,c):
    return tuple((-1)**i*det3([a[j] for j in range(4) if j!=i],
                              [b[j] for j in range(4) if j!=i],
                              [c[j] for j in range(4) if j!=i]) for i in range(4))


def vector_difference(a,b):return tuple(x-y for x,y in zip(a,b))


def main():
    cert=json.loads((Path(__file__).parent/'cube9_width_polars.json').read_text('utf-8'))
    assert cert['schema']==1 and cert['dimension']==4 and cert['cardinality']==9
    entries=cert['orbit_representatives']
    corners=range(16)
    maps=[]
    for perm in permutations(range(4)):
        p=tuple(sum(((x>>i)&1)<<perm[i] for i in range(4)) for x in corners)
        for flip in corners:maps.append(tuple(v^flip for v in p))
    assert len(maps)==384 and len(set(maps))==384
    unseen=set(combinations(corners,9));total_orbit=0
    total_det=0;total_facets=0;total_vertices=0;max_vertices=0;max_sc=0
    equality_cases=0
    for entry in entries:
        S=tuple(entry['S']);D=entry['scale'];V=[tuple(v) for v in entry['vertices']]
        assert len(S)==9 and all(isinstance(x,int) for x in S) and S==min(unseen)
        assert D>0 and isinstance(D,int) and len(V)==len(set(V)) and len(V)>=5
        orbit={tuple(sorted(m[v] for v in S)) for m in maps}
        assert orbit <= unseen
        unseen.difference_update(orbit);total_orbit+=len(orbit)
        points=[tuple((v>>i)&1 for i in range(4)) for v in S]
        ds={vector_difference(a,b) for a in points for b in points if a!=b}
        assert all((0,)*4!=v for v in ds)
        # Exact feasibility of all listed rational candidate vertices.
        for v in V:
            assert len(v)==4 and all(isinstance(x,int) for x in v)
            assert all(dot(d,v)<=D for d in ds)
        # A point of each sign of each basis coordinate lies in S-S;
        # in particular W_S={y:d*y<=1} is bounded and full-dimensional.
        assert all(tuple((1 if j==i else 0) for j in range(4)) in ds for i in range(4))
        assert all(tuple((-1 if j==i else 0) for j in range(4)) in ds for i in range(4))
        # All supporting 3-dimensional hyperplanes of conv(V) pass through
        # four affinely independent candidate vertices. Each must be one
        # of the defining width inequalities. This proves conv(V)=W_S
        # without using vertex enumeration or trusting certificate generation.
        nfac=0;nondegenerate=False
        for aa,bb,cc,dd in combinations(V,4):
            u=vector_difference(bb,aa)
            v=vector_difference(cc,aa)
            w=vector_difference(dd,aa)
            normal=cross4(u,v,w)
            if normal==(0,0,0,0):continue
            vals=[dot(normal,vector_difference(x,aa)) for x in V]
            if min(vals)<0<max(vals):continue
            if max(vals)>0:normal=tuple(-z for z in normal)
            h=dot(normal,aa)
            assert h>0, 'origin must be strictly interior to conv(V)'
            assert any(all(normal[j]*D==h*d[j] for j in range(4)) for d in ds), 'missing facet inequality'
            nfac+=1
        # A full-dimensional witness (five affinely independent vertices).
        for a,b,c,d,e in combinations(V,5):
            if det4([vector_difference(b,a),vector_difference(c,a),vector_difference(d,a),vector_difference(e,a)]):
                nondegenerate=True;break
        assert nondegenerate and nfac>0
        # Multi-affinity: maximal absolute determinant of arbitrary rows
        # in W_S is attained at a tuple of its vertices. Repetitions vanish.
        orbit_best=0
        for rows in combinations(V,4):
            z=abs(det4(rows)); assert z<=D**4
            orbit_best=max(orbit_best,z)
            total_det+=1
        assert orbit_best==D**4
        equality_cases+=1
        max_sc=max(max_sc,D)
        max_vertices=max(max_vertices,len(V))
        total_vertices+=len(V);total_facets+=nfac
    assert not unseen and total_orbit==comb(16,9) and len(entries)==56
    assert equality_cases==56
    print('FOUR_CUBE_NINE_VERTEX_VOLUME_OK',f'orbits={len(entries)}',f'subsets={total_orbit}',
          f'certified_vertices={total_vertices}',f'max_vertices={max_vertices}',
          f'facet_tests={total_facets}',f'determinant_tests={total_det}',f'max_scale={max_sc}',
          'max_det=1',flush=True)

if __name__=='__main__':main()
