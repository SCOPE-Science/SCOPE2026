# Independent mathematical audit

## correctness

PASS

The vertex model consists of two poles and two staggered five-cycles: 12 vertices, degree five, 30 edges. The two-independent face condition (every induced connected component has at most two vertices) is equivalent to excluding connected induced triples. Independent reconstruction by breadth-first component counting over all 2^12=4096 masks gave exactly 324 faces including empty, with count by size [1,12,66,140,105], 105 and only 105 four-vertex maximal facets, and 80 forbidden connected triples. The fetched full explicit 105-mask shelling.json was independently checked against the exact facet set. For each of its 104 noninitial facets, enumerated all prior-intersection faces, confirmed that all maximal intersection faces have exactly three vertices (nonempty pure codimension-one intersection), and verified the unique minimal newly introduced restriction face. No failures; entire complex covered; 20 restriction faces equal their full tetrahedron. Standard pure shellability yields the integral homotopy type wedge_{20} S^3; h-vector [1,8,36,40,20] and reduced Euler characteristic -20 agree. This is an exhaustive finite certificate checked independently, not merely a log or a Betti calculation.

## originality

PASS

The theorem is the explicit primal Ind_2 of the icosahedral graph, with a complete 105-facet shelling. Previously inspected higher-independence shellability theorems constrain block/tree-like graph classes rather than this 5-regular nonchordal graph; other icosahedral neighborhood, cut, matching and ordinary independence complexes are different functors.

## value

PASS

The regular icosahedron is a canonical small, highly symmetric, 5-regular, nonchordal graph outside the standard block/tree shellability classes. Classifying its natural induced-component-at-most-two complex by a full shelling gives an integral wedge homotopy type and a reusable explicit finite certificate, rather than a routine Euler-characteristic or mod-two Betti computation. The exact dimension, facet count and sphere number are natural invariants researchers can use when testing stronger shellability criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
