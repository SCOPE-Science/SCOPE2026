# Complete Vietoris–Rips filtration of the Euclidean cuboctahedron
## Finding
Let \(C=\{(x_1,x_2,x_3)\in\{0,\pm1\}^3:\text{ exactly one coordinate is }0\}\), equipped with the Euclidean metric, and let \(\operatorname{VR}_{\le r}(C)\) denote the inclusive Vietoris--Rips complex. Then
\[
\operatorname{VR}_{\le r}(C)\simeq
\begin{cases}
\bigvee^{11}S^0,&0\le r<\sqrt2,\\
\bigvee^{5}S^1,&\sqrt2\le r<2,\\
S^2,&2\le r<\sqrt6,\\
S^5,&\sqrt6\le r<2\sqrt2,\\
\ast,&r\ge2\sqrt2.
\end{cases}
\]
Equivalently, apart from the degree-zero component structure, the persistent homology has five degree-one intervals \([\sqrt2,2)\), one degree-two interval \([2,\sqrt6)\), and one degree-five interval \([\sqrt6,2\sqrt2)\), over any coefficient field.

## Assumptions and scope
The point set is the standard cuboctahedron of edge length \(\sqrt2\). The convention is inclusive: a finite subset spans a simplex exactly when every pair has distance at most \(r\). The claim concerns the finite Euclidean metric on these twelve vertices, not the intrinsic surface metric on the polyhedron.

## Proof
Every vertex has squared norm \(2\), so for distinct vertices \(p,q\in C\),
\[
\lVert p-q\rVert^2=4-2\langle p,q\rangle.
\]
The possible nonzero squared distances are exactly \(2,4,6,8\); hence the complex changes only at \(\sqrt2,2,\sqrt6,2\sqrt2\).

For \(r<\sqrt2\), there are twelve isolated vertices, giving \(\bigvee^{11}S^0\).

At \(r=\sqrt2\), the maximal simplices are exactly the eight triangular faces of the cuboctahedron. Index them by sign vectors \(s\in\{\pm1\}^3\): the triangle \(T_s\) consists of the three vertices whose nonzero coordinates agree with \(s\). Two such triangles intersect exactly when their sign vectors differ in one coordinate, and then the intersection is a single vertex. Thus the nerve is the cube graph \(Q_3\). Since all nonempty finite intersections are simplices, the nerve lemma gives
\[
\operatorname{VR}_{\le\sqrt2}(C)\simeq Q_3\simeq\bigvee^5S^1.
\]

At \(r=2\), the maximal simplices are exactly the eight triangular-face vertex sets and the six square-face vertex sets; each square now spans a tetrahedron. Cover this abstract complex by those fourteen simplices. The boundary of the geometric cuboctahedron is covered by the corresponding fourteen polygonal faces. These two covers have the same nonempty intersection pattern, and every nonempty intersection is contractible. After an arbitrarily small open-star thickening, the nerve lemma applies to both covers, so
\[
\operatorname{VR}_{\le2}(C)\simeq \partial(\text{cuboctahedron})\cong S^2.
\]

At \(r=\sqrt6\), the only missing edges join antipodal pairs \(\{p,-p\}\). There are six such pairs. Therefore the complex is the join of six two-point discrete spaces,
\[
(S^0)^{\ast6}\cong S^5.
\]
At \(r=2\sqrt2\), all pairwise distances are allowed and the complex is the full simplex on twelve vertices, hence contractible. Constancy on the open intervals between the four distance values proves the stated filtration.

## Verification
The accompanying verifier independently reconstructs the twelve coordinates, all pairwise squared distances, every simplex at squared thresholds \(2,4,6,8\), and every maximal simplex. At the first three nontrivial thresholds it also constructs an acyclic discrete-Morse matching and independently computes mod-two boundary ranks.

At squared threshold \(2\), it finds face vector \((12,24,8)\), Betti vector \((1,5,0)\), and critical-cell counts one in degree \(0\) and five in degree \(1\). At threshold \(4\), it finds \((12,36,32,6)\), Betti vector \((1,0,1,0)\), and one critical cell in degrees \(0\) and \(2\). At threshold \(6\), it finds \((12,60,160,240,192,64)\), Betti vector \((1,0,0,0,0,1)\), and one critical cell in degrees \(0\) and \(5\). At threshold \(8\), it verifies the full simplex. Running `python3 verify_cuboctahedron_rips.py` terminates with `VERIFY_OK`.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine Vietoris--Rips complexes for the vertex sets of the five Platonic solids and explicitly identify Archimedean solids as a conceivable generalization. The cuboctahedron is Archimedean rather than Platonic, so their theorem does not include the present filtration. Exact searches for the cuboctahedron, its description as the line graph of the cube, and rectified-cube/rectified-octahedron aliases did not locate a checked source stating the five-stage homotopy classification above.

The closely related thesis *On Vietoris-Rips Complexes of the 2-Sphere* was checked at the repository metadata and abstract level. Its abstract describes Platonic solids and higher-dimensional regular polytopes, but the full thesis text was not available in machine-readable form during this check; it therefore remains a residual originality risk rather than evidence of absence.

## Limitations
The theorem is specific to the twelve vertices with Euclidean chordal distance. It does not describe Vietoris--Rips complexes of the entire cuboctahedral surface, intrinsic geodesic distance, or noisy samples. The literature search cannot exclude an unindexed or differently phrased prior computation, and the full thesis noted above was not text-inspected.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388; *Innovations in Incidence Geometry* 21 (2024), 17--31, DOI 10.2140/iig.2024.21.17.
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral thesis, Justus Liebig University Giessen, DOI 10.22029/jlupub-17950.
