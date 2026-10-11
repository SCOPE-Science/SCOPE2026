# Minimum normal projective planes in the \(24\)-cell quotient triangulation of \(\mathbb{RP}^3\)
## Finding
Let \(K={}^3 12^{13}_{2}\) be the Köhler--Lutz twelve-vertex vertex-transitive triangulation of \(\mathbb{RP}^3\). The source identifies \(K\) with the antipodal quotient of the boundary of the \(24\)-cell, gives face vector \((12,60,96,48)\), and gives a vertex-transitive automorphism group of order \(24\).

For an embedded normal projective plane \(S\subset K\), define its edge weight to be the total number of intersections of \(S\) with the edges of \(K\), counted with multiplicity. Then every such \(S\) has edge weight at least \(21\), and exactly \(60\) normal projective planes have edge weight \(21\).

Equivalently, if \(\alpha\) is the unique nonzero element of \(H^1(K;\mathbf F_2)\) and
\[
w(\alpha)=\min\{\lvert\operatorname{supp}z\rvert:z\in Z^1(K;\mathbf F_2),\ [z]=\alpha\},
\]
then \(w(\alpha)=21\), with exactly \(60\) minimizing cocycles. Under the published simplicial automorphism group these minima form three orbits of sizes \(12\), \(24\), and \(24\). One \(24\)-element orbit has canonical normal representatives made of \(18\) normal triangles and \(11\) normal quadrilaterals. The \(12\)-element orbit and the other \(24\)-element orbit have \(20\) normal triangles and \(10\) normal quadrilaterals.

The complete support-weight distribution in the nonzero cohomology coset is
\[
60t^{21}+132t^{23}+144t^{25}+240t^{27}+360t^{29}+408t^{31}+400t^{33}+240t^{35}+60t^{37}+4t^{39}.
\]

## Assumptions and scope
The simplicial complex is the labeled complex \({}^3 12^{13}_{2}\) in Köhler--Lutz. It is reconstructed only from the three published facet-orbit representatives \(1235_{24}\), \(12510_{12}\), and \(121011_{12}\), together with the published generators of the action \(12^{13}\). Their orbits give exactly \(48\) tetrahedra, \(96\) triangles, and \(60\) edges.

The normal-surface statement concerns embedded normal surfaces with respect to this fixed triangulation. Edge weight counts normal vertices, so repeated intersections of an edge are counted repeatedly.

## Proof
Over \(\mathbf F_2\), a simplicial one-cochain is a cocycle precisely when its values sum to zero around every triangular face. On the \(60\) edges of \(K\), the \(96\) triangle equations have rank \(48\), hence \(\dim Z^1=12\). Vertex coboundaries have rank \(11\). Therefore
\[
\dim_{\mathbf F_2}H^1(K;\mathbf F_2)=1.
\]
Fixing the value of a vertex potential at vertex \(1\) to be zero makes every coboundary unique, so the unique nonzero cohomology class has exactly \(2^{11}=2048\) cocycle representatives. Exhaustive exact enumeration of this entire coset gives the displayed weight distribution. Its least weight is \(21\), attained \(60\) times.

For any one-cocycle \(z\), its restriction to a tetrahedron is a coboundary because a tetrahedron is contractible. Hence the nonzero edges in that tetrahedron form either no cut, a \(1\mid3\) cut, or a \(2\mid2\) cut. These are exactly the edge patterns met by, respectively, no normal disk, one normal triangle, or one normal quadrilateral. Thus a cocycle canonically determines a closed embedded normal surface meeting each supported edge once. For every one of the \(60\) weight-\(21\) cocycles, the disk-adjacency graph is connected and the normal cell structure has Euler characteristic \(1\). A connected closed surface with Euler characteristic \(1\) is \(\mathbb{RP}^2\). Hence all \(60\) minima produce embedded normal projective planes.

Conversely, let \(S\subset K\) be any embedded normal projective plane. Parity of intersection with each edge gives a simplicial one-cocycle \(z_S\): every normal arc in a triangular face contributes two endpoints, so the cocycle equation holds on each triangle. Since \(S\) represents the nonzero class in \(H_2(\mathbb{RP}^3;\mathbf F_2)\), the dual class \([z_S]\) is nonzero. Therefore \(\lvert\operatorname{supp}z_S\rvert\ge21\). The total edge weight of \(S\) is at least \(\lvert\operatorname{supp}z_S\rvert\), proving the lower bound \(21\). Equality forces every supported edge to be met exactly once and every unsupported edge zero times, so \(S\) is exactly the canonical normal surface of a weight-\(21\) cocycle. Thus there are exactly \(60\) minimum normal projective planes.

Finally, the four published permutations generate a group of order \(24\) and preserve the reconstructed facet set. Acting on the \(60\) minimum cocycles gives orbit sizes \(12,24,24\). Direct normal-disk counts give \((18,11)\) for one \(24\)-orbit and \((20,10)\) for the other two orbits.

## Verification
The standalone checker `artifacts/verify.py` uses only the Python standard library. It reconstructs the triangulation from the published group generators and facet-orbit representatives, verifies the face vector, performs exact binary row reduction, exhausts all \(2048\) representatives of the nonzero cohomology class, verifies the complete weight enumerator, generates the order-\(24\) action, computes all minimizer orbits, constructs the canonical normal disks, checks connectedness, and recomputes Euler characteristic for every minimizer.

A replay prints `VERIFY_OK` together with the ranks, coset size, weight enumerator, orbit sizes, and normal-disk profiles recorded above.

## Relationship to prior work
Köhler--Lutz determine the exact triangulation, its topology, face data, facet orbits, and symmetry action. Their full text contains no occurrence of “cocycle,” “cohomology,” “systole,” or “normal surface,” and it does not state a minimum normal projective-plane weight or a cocycle weight enumerator.

General normal-surface theory explains the standard passage from a mod-two cohomology class to its canonical normal representative. The new content here is the exact optimum and complete minimizer structure for this particular highly symmetric \(24\)-cell quotient triangulation.

A previously known exact computation for this same labeled complex gives its shortest nonzero primal homology cycles. That information does not imply the minimum support of a cohomology cocycle, the normal-surface edge weight, the number of minimizing projective planes, or their symmetry-orbit and triangle/quadrilateral profiles.

## Limitations
The result is specific to the fixed triangulation \(K\); it is not an invariant of \(\mathbb{RP}^3\) independent of triangulation. The exhaustive computation concerns binary simplicial one-cocycles and the canonical normal surfaces they define. The lower-bound argument applies to arbitrary embedded normal projective planes in this triangulation, but no claim is made about non-normal representatives before normalization or about other triangulations of \(\mathbb{RP}^3\).

The literature comparison cannot rule out every obscure or unindexed historical computation under a different normal-surface or coding-theoretic terminology.

## References
1. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:math/0506520v1, 24 June 2005. The exact \(\mathbb{RP}^3\) row is \({}^3 12^{13}_{2}\); the paper also lists the generators of the action \(12^{13}\).
