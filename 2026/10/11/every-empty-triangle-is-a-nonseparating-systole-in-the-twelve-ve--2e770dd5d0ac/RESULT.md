# Every empty triangle is a nonseparating systole in the twelve-vertex genus-six surface
## Finding
Let \(K\) be surface number \(58\) in the Altshuler--Bokowski--Schuchert classification of orientable neighborly twelve-vertex surfaces. The published classification identifies these surfaces as genus \(6\), and the exact `GenusSix` model has
\[
f(K)=(12,66,44),\qquad \dim_{\mathbf F_2}H_1(K;\mathbf F_2)=12.
\]
Its one-skeleton is the complete graph \(K_{12}\).

Among the \(\binom{12}{3}=220\) vertex triples, \(44\) are triangular faces and the other \(176\) are empty triangles. Every one of the \(176\) empty triangles represents a nonzero mod-two homology class. Since \(K\) is a closed orientable surface, a simple closed curve is zero in \(H_1(-;\mathbf F_2)\) exactly when it separates. Thus every empty triangle is nonseparating. Because no simple loop has fewer than three edges, all \(176\) are combinatorial one-systoles.

The \(176\) triangular systoles represent exactly \(110\) distinct nonzero classes. Their shortest-representative multiplicities are
\[
1^{\times56},\qquad 2^{\times48},\qquad 4^{\times6}.
\]
There is no class with exactly three triangular representatives, and four is the maximum triangular multiplicity.

The full simplicial automorphism group has order \(12\). Its action on the \(110\) triangular homology classes has orbit profile
\[
(12,1)^{\times4},\ (4,1)^{\times2},\ (12,2)^{\times3},\ (6,2)^{\times2},\ (6,4)^{\times1},
\]
where each pair records orbit size and number of triangular representatives per class. In particular, the six classes with four triangular representatives form one symmetry orbit.

## Assumptions and scope
The triangulation is the exact twelve-vertex facet presentation used by the SageMath `GenusSix` example:
\[
014,018,023,027,036,049,056,05b,07a,08a,09b,
\]
\[
125,126,137,139,147,15a,16b,18b,19a,23b,248,
\]
\[
24a,258,269,279,2ab,345,34b,35a,367,389,38a,
\]
\[
459,46a,46b,478,568,579,57b,67a,689,78b,9ab,
\]
with \(a=10\) and \(b=11\).

An empty triangle is a three-vertex clique whose triangle is not a face. Cycle length is ordinary edge length in the complete one-skeleton. Homology is over \(\mathbf F_2\). The statement concerns this maximally symmetric member of the 59 orientable neighborly twelve-vertex genus-six surfaces, not the other 58 members.

## Proof
The displayed facet list has \(44\) triangles and all \(66\) possible edges. Every edge lies in exactly two triangular faces, and
\[
12-66+44=-10=2-2\cdot6,
\]
consistent with the published orientable genus-six identification.

Write the \(66\) edges as a basis of \(C_1(K;\mathbf F_2)\). The \(44\) facial triangle boundaries have rank \(43\). The graph cycle space of \(K_{12}\) has dimension
\[
66-12+1=55,
\]
so
\[
\dim_{\mathbf F_2}H_1(K;\mathbf F_2)=55-43=12.
\]

Every three-vertex subset is a graph cycle. Reducing the boundary vector of each of the \(176\) nonfacial triangles modulo the row space of the \(44\) facial boundaries gives a nonzero vector. Grouping equal reduced vectors gives exactly \(110\) classes, with multiplicity distribution
\[
56\cdot1+48\cdot2+6\cdot4=176.
\]
This is exhaustive because all \(220\) three-vertex subsets were tested.

For the automorphism calculation, note that the link of every vertex is an eleven-cycle. Any simplicial automorphism is determined by the image of vertex \(0\) together with an isomorphism from the link cycle at \(0\) to the link cycle at that image. Therefore there are only
\[
12\cdot22=264
\]
possible link-compatible vertex permutations to test. Exact facet preservation leaves precisely \(12\), proving the full automorphism-group order without assuming it from the literature.

Applying these twelve automorphisms to the reduced homology classes gives the stated class-orbit profile. The six multiplicity-four classes form one orbit of size six.

Finally, on a closed orientable surface, an embedded simple closed curve is separating if and only if its mod-two homology class vanishes. Each empty triangle is an embedded simple three-cycle and has nonzero class, so every one is nonseparating. Since simple cycles have length at least three, they are all systolic.

## Verification
The standalone `verify.py` uses only the Python standard library. It rebuilds the full edge set and all local incidences, performs exact bit-vector row reduction over \(\mathbf F_2\), checks every vertex triple, enumerates the full automorphism group through link-cycle maps, and computes every class orbit.

Its exact successful output is:

`VERIFY_OK f=12,66,44 chi=-10 genus=6 H1_F2_dim=12 missing3=176 all_missing3_nonzero=yes triangular_classes=110 multiplicities=1:56,2:48,4:6 aut=12 support_orbits=4,4,12,12,12,12,12,12,12,12,12,12,12,12,12,12 class_orbits=(12,1)x4,(4,1)x2,(12,2)x3,(6,2)x2,(6,4)x1 quadruple_classes_one_orbit=yes`

The finite computation proves the complete triangular homology census and all symmetry counts. The only external topological input used for the separating/nonseparating wording is the standard mod-two separation criterion for simple closed curves on closed orientable surfaces.

## Relationship to prior work
Altshuler, Bokowski, and Schuchert classified all \(59\) orientable neighborly twelve-vertex genus-six surfaces. The exact model used here appears as their surface \(58\), which later exact documentation identifies as the unique member with the largest simplicial symmetry group, of order \(12\). Ellingham and Stephens independently summarize the complete 59-surface classification in their work on triangular complete-graph embeddings. These are strong prior results on the object, its classification, and its symmetry.

The new statement is not the existence of the triangulation or the order of its automorphism group. It is the complete homological classification of all empty triangles: none separates, the \(176\) supports collapse to exactly \(110\) mod-two classes with multiplicity profile \(56,48,6\), and the exceptional six multiplicity-four classes form one full symmetry orbit. The inspected classification summaries and exact-object documentation do not state these inclusion-sensitive homology data.

## Limitations
The result only classifies length-three representatives. It does not give the complete minimum-length spectrum for all \(4095\) nonzero classes of \(H_1(K;\mathbf F_2)\), nor does it classify integral homology classes or analogous spectra for the other \(58\) neighborly genus-six surfaces.

The 1996 primary classification was located with month-level publication information but no verified calendar day in the inspected route. To avoid inventing a day, `first_public_date` records the earliest day-resolved public source inspected that independently confirms the 59 orientable twelve-vertex classification, namely 2005-05-19. The older 1996 source remains the primary historical reference.

## References
1. A. Altshuler, J. Bokowski, and P. Schuchert, *Neighborly 2-Manifolds with 12 Vertices*, Journal of Combinatorial Theory, Series A 75 (1996), 148--162, DOI `10.1006/jcta.1996.0069`.
2. M. N. Ellingham and C. Stephens, *Triangular embeddings of complete graphs (neighborly maps) with 12 and 13 vertices*, Journal of Combinatorial Designs 13 (2005), 336--344, DOI `10.1002/jcd.20048`, first published 2005-05-19.
3. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:`math/0506372v1`, submitted 2005-06-18, MSC `57Q15`.
4. SageMath, `GenusSix()` in `simplicial_complex_examples.py`, exact facet presentation and symmetry/homology cross-check.
