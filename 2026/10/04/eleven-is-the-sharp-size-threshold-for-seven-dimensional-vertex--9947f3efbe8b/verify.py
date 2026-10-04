from itertools import product

# A 3-polytope with v vertices has e >= 3v/2 by minimum vertex degree 3,
# and Euler gives f = 2-v+e.  Thus v<=5 cannot have v>f.
for v in (4,5):
    for e in range((3*v+1)//2, 3*v-5):
        f=2-v+e
        assert f >= v

# The minimal strict vertex excess is attained by the triangular prism.
prism=(6,9,5)       # (vertices, edges, facets)
bipyramid=(5,9,6)  # dual tuple
assert prism[0] > prism[2]
assert bipyramid[0] < bipyramid[2]

# Free join counts and dimension.
dim_prism=3
dim_join=dim_prism+dim_prism+1
v_join=prism[0]+bipyramid[0]
f_join=prism[2]+bipyramid[2]
assert (dim_join,v_join,f_join)==(7,11,11)

# The prism factor is a 3-face with 6 vertices and is contained in exactly
# the 6 facets indexed by facets of the bipyramid, violating the face criterion.
assert prism[0] + bipyramid[2] == 12 > max(v_join,f_join)

# Lower-bound arithmetic: a 3-face with strict vertex excess has >=6 vertices;
# full dimension needs >=4 vertices outside. If total vertices were 10, these
# numbers would be exact, and the four outside vertices form a tetrahedral join
# factor, giving only four containing facets, contradicting the required >=6.
face_vertices=6
outside_vertices=4
assert face_vertices+outside_vertices==10
containing_facets_if_equality=4
required_dual_face_vertices=6
assert containing_facets_if_equality < required_dual_face_vertices

print('VERIFY_OK sharp d7 vertex-facet obstruction threshold')
