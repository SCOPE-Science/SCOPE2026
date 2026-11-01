"""Standalone geometric checks for the recursive self-volume calculation.

Requires numpy and scipy. Numerical convex-hull computations corroborate,
but do not replace, the exact formulas in RESULT.md.
"""
import itertools
import math
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull

TOL=2e-9

def near(x,y):
    assert abs(float(x)-float(y)) < TOL*max(1.0,abs(float(y))), (x,y)

def hull_section(points, normal):
    """Points in full ambient Euclidean coordinates; section at n dot x=0."""
    points=np.asarray(points,dtype=float)
    norm=np.asarray(normal,dtype=float)
    n=norm/np.linalg.norm(norm)
    sections=[]
    for p,q in itertools.combinations(points,2):
        s=float(n@p);t=float(n@q)
        if s*t < -1e-14:
            sections.append((p*t-q*s)/(t-s))
        elif abs(s)<1e-14:
            sections.append(p)
        elif abs(t)<1e-14:
            sections.append(q)
    sections=np.array(sections)
    basis=null_space(n[None,:])
    projected=sections@basis
    hull=ConvexHull(projected)
    return projected[hull.vertices], hull.volume

def normed_polygon_perimeter(vertices):
    # vertices should be CCW. Cartesian formula for centrally symmetric convex polygon.
    vertices=np.asarray(vertices)
    hull=ConvexHull(vertices)
    a=hull.equations[:,:2]
    b=hull.equations[:,2]
    assert (b<-0.0001).all()
    per=0.
    poly=vertices[hull.vertices]
    for k in range(len(poly)):
        delta=poly[(k+1)%len(poly)]-poly[k]
        per+=np.max(-a@delta/b)
    return per

# The root-polytope/cuboctahedron in the sum-zero subspace of R^4.
eye=np.eye(4)
vertices=np.array([(eye[i]-eye[j])/2 for i in range(4) for j in range(4) if i!=j]);
assert len(vertices)==12
E=null_space(np.ones((1,4)))
three=vertices@E
hull=ConvexHull(three)
near(hull.volume, 5/6)
# Group triangulated Qhull simplices into their geometric supporting facets.
facets={}
rawnormals={}
for simp,eq in zip(hull.simplices,hull.equations):
    key=tuple(np.round(eq, 8))
    facets.setdefault(key,[]).append(simp)
    rawnormals[key]=eq[:3]
assert len(facets)==14, len(facets)
sum_terms=0
counts={3:0,4:0}
for key, triangles in facets.items():
    all_indices=sorted(set(int(i) for tri in triangles for i in tri))
    count=len(all_indices)
    assert count in (3,4)
    counts[count]+=1
    # Surface area from a triangulation, no conceptual restriction to regular faces.
    area=sum(np.linalg.norm(np.cross(three[b]-three[a],three[c]-three[a]))/2 for a,b,c in triangles)
    n=rawnormals[key]/np.linalg.norm(rawnormals[key])
    section,section_area=hull_section(three,n)
    per=normed_polygon_perimeter(section)
    vol2=per/2
    if count==3:
        near(area,math.sqrt(3)/8)
        near(section_area,3*math.sqrt(3)/4)
        near(per,6)
        near(vol2,3)
    else:
        near(area,1/2)
        near(section_area,1)
        near(per,8)
        near(vol2,4)
    sum_terms+=area*vol2/section_area
assert counts=={3:8,4:6},counts
V3=sum_terms/3
near(V3,16/3)

# The four-cross-polytope: unit coordinate vertices, 16 regular-tetrahedral facets.
verts4=np.concatenate([eye,-eye],axis=0)
h4=ConvexHull(verts4)
near(h4.volume,2/3)
assert len(h4.simplices)==16
vol4=0
for facet, equation in zip(h4.simplices,h4.equations):
    a,b,c,d=verts4[facet]
    gram=np.stack([b-a,c-a,d-a])
    facet_area=np.sqrt(np.linalg.det(gram@gram.T))/6
    near(facet_area,1/3)
    normal=equation[:4]/np.linalg.norm(equation[:4])
    section,s_area=hull_section(verts4,normal)
    near(s_area,5/6)
    vol4+=facet_area*V3/s_area
vol4/=4
near(vol4,128/15)

print('cuboctahedron_facets',counts)
print('cuboctahedron_ordinary_volume',hull.volume)
print('cuboctahedron_recursive_self_volume',V3)
print('four_crosspolytope_facets',len(h4.simplices))
print('four_crosspolytope_ordinary_volume',h4.volume)
print('four_crosspolytope_recursive_self_volume',vol4)
print('OK')
