# A triangular-cycle neighborhood complex collapses to a torus

## Finding
For every integer \(n\ge5\), let \(G_n=K_3\square C_n\) and form its **open** Lovász neighborhood complex \(\mathcal N(G_n)\): a finite nonempty set of vertices is a simplex precisely when all of its vertices share one graph neighbor (the common neighbor is not required to lie in the set). There is an explicit sequence of exactly \(6n\) elementary simplicial collapses
\[\mathcal N(G_n)\searrow T_n\cong S^1\times S^1,\]
where \(T_n\) is a two-dimensional simplicial torus with face vector \((3n,9n,6n)\). The original complex has face vector \((3n,12n,12n,3n)\). In particular, its integral homology is \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z^2\), \(H_2\cong\mathbb Z\), and zero in higher degrees. There exist primitive classes \(\alpha,\beta\in H^1(\mathcal N(G_n);\mathbb Z)\) with \(\alpha\smile\beta\) a generator of \(H^2\cong\mathbb Z\). This product distinguishes the result from a wedge of circles and spheres.

## Assumptions and scope
All graphs are finite, simple, undirected. Fix an integer \(n\ge5\). Identify the graph's \(3n\) vertices with \(\mathbb Z/n\mathbb Z\times\mathbb Z/3\mathbb Z\), denoting a vertex by \((a,b)\). Two distinct vertices are adjacent if one coordinate agrees and the other coordinates differ by one cyclic step; since the second cyclic coordinate has length three, this is precisely the graph \(K_3\square C_n\). The complex is the ordinary open-neighborhood complex, **not** a closed-neighborhood nerve or a graph-distance Rips complex. An elementary collapse deletes a free face together with its unique codimension-one coface, leaving a simple-homotopy equivalent complex.

## Proof
**Step 1: all maximal simplices.** Set
\[u=(a,b+1),\quad v=(a,b-1),\quad p=(a+1,b),\quad m=(a-1,b),\]
with both coordinates interpreted cyclically as above. The open neighborhood of the graph vertex \((a,b)\) is the four-element set \(F_{a,b}=\{u,v,p,m\}\). Each such set is distinct when \(n\ge5\), so the neighborhood complex is the union of the \(3n\) tetrahedra \(\Delta(F_{a,b})\). The crucial intersection property is that the only common graph neighbor of \(u\) and \(v\) is \((a,b)\): the third vertex in their three-point vertical fiber. Indeed an external-neighbor candidate would have to lie simultaneously in distinct same-level horizontal rows and so cannot be adjacent to both. Consequently, every simplex containing the edge \(\{u,v\}\) is a face of the unique tetrahedron \(F_{a,b}\).

**Step 2: free triangles.** In any order over the \(3n\) pairs \((a,b)\), delete the triangle \(\{u,v,p\}\) together with its unique containing tetrahedron \(F_{a,b}\). The preceding common-neighbor property proves that each designated triangle has just one tetrahedral coface. These deletions are mutually independent: no other tetrahedron contains such a triangle. Exactly \(3n\) elementary collapses have been performed.

**Step 3: free edges.** Each designated edge \(\{u,v\}\) now belongs to only one surviving triangle, namely \(\{u,v,m\}\), because its other incident triangle in the original tetrahedron was deleted in Step 2. Delete the edge together with this triangle. These \(3n\) collapses are again independent. The remaining triangles are exactly
\[\{(a-1,b),(a+1,b),(a,b+1)\},\quad\{(a-1,b),(a+1,b),(a,b-1)\}\]
for all \(a\in\mathbb Z/n\mathbb Z\), \(b\in\mathbb Z/3\mathbb Z\). There are \(6n\) distinct remaining triangles, each of their \(9n\) edges is incident with two triangles, and all \(3n\) vertices remain. The enumeration also gives the original face vector \((3n,12n,12n,3n)\). Thus the collapse count is \(6n\).

**Step 4: identify the torus, including orientability.** Consider the infinite square lattice \(\mathbb Z^2\) and its parity-even subset \(\Lambda=\{(x,y)\in\mathbb Z^2:x+y\equiv0\pmod2\}\). Join parity-even points with displacements \((2,0)\), \((1,1)\), or \((1,-1)\), and triangulate each rhombic tile by the horizontal length-two diagonal. Equivalently, about every odd-parity center \((x,y)\), take the two triangles whose corners are the points at displacements \((-1,0),(1,0),(0,1)\) or \((-1,0),(1,0),(0,-1)\). This is a face-to-face planar triangulation of \(\mathbb R^2\) (the two triangles form each diamond, and the diamonds tile the plane). Its translation symmetries contain \(\Lambda\).

Reducing lattice coordinates modulo \((n,3)\) identifies its vertices with the \(3n\) vertices of the remaining complex: every residue pair has an even-parity lift, because adding the odd vertical period \(3\) changes parity. The translation kernel is the rank-two sublattice
\[L_n=\Lambda\cap(n\mathbb Z\times3\mathbb Z).\]
For \(n\ge5\), reduction does not identify any vertices of an individual triangle or distinct triangles in the same local tile: all horizontal vertex displacements within a triangle have absolute value at most \(2\), and the vertical ones at most \(1\), while a nonzero kernel vector has horizontal component divisible by \(n\) and vertical component divisible by \(3\). The images are exactly the triangles of Step 3. Therefore \(T_n\) is simplicially the quotient of this parity-even planar triangulation by \(L_n\). A quotient of the oriented plane by a full rank-two lattice of translations is an orientable two-torus, and this triangulation descends without identifications inside simplices. Thus \(T_n\cong\mathbb R^2/L_n\cong S^1\times S^1\).

Every step is an elementary simplicial collapse or a direct geometric identification; no finite-parameter extrapolation is used. The stated integral homology and nonzero cup product now follow from the standard cellular structure and cohomology ring of the torus.

## Verification
A standalone Python standard-library verifier, `verify.py`, rebuilds the \(3n\) original tetrahedral facets, all of their faces, and performs the two explicit phases of free-face collapses. For every \(n\) from \(5\) through \(40\), it checks the initial and final face vectors, each unique coface, connectedness of the final triangle adjacency graph, exactly two triangles per edge, and that each vertex link is one cycle. The recorded exact output is in `verification_output.txt` and ends with `VERIFY_OK_TRIANGULAR_CYCLE_NEIGHBORHOOD_TORUS`. This finite check is independent corroboration of the all-parameter geometric proof above, not a replacement for it.

## Relationship to prior work
The open-neighborhood construction and its topological relevance are standard; see Matsushita's 2012 work on fundamental groups of neighborhood complexes. A related published classification for \(K_m\square C_n\) assumes \(m\ge4\) and gives a mixed-dimensional wedge of spheres and a circle; it does not apply to the exceptional three-point fiber. A separate toroidal-grid neighborhood result assumes no period of Manhattan length less than five; the factor \(C_3\) violates that hypothesis. Unlike a wedge decomposition, the surviving torus here has nontrivial integral first-degree cup multiplication.

## Limitations
The statement is restricted to \(n\ge5\) and the ordinary open-neighborhood construction. It makes no assertion for smaller cyclic lengths, other complete-graph fibers, different graph products, or equivariant actions. Targeted searches and reviewed available papers did not locate an identical previously published statement, but an equivalent unindexed proof or a general theorem not identified in the available literature remains possible. There has been no independent scientific audit.

## References
1. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, initially posted 2012-10-10. Provides the general neighborhood-complex and fundamental-group framework, not the present two-torus collapse.
2. *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, published research record 2026-10-11, identifier `3a53c8927b3c`. Applies to complete-graph factor size at least four.
3. *Toroidal grid neighborhood complexes collapse to one or two tori*, published research record 2026-10-11, identifier `737edf71bc86`. Assumes all nonzero quotient periods have Manhattan length at least five.
