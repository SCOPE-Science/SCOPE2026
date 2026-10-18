# Complete central-section polygon types of the regular icosidodecahedron

## Finding

**Theorem.** Consider the regular icosidodecahedron \(P\) centered at the origin, realized as the convex hull of the thirty edge midpoints of a regular icosahedron. For every nonzero \(u\in\mathbb R^3\), let \(S_u=P\cap u^\perp\) and let \(n(u)\) be the number of vertices of this planar convex polygon.

The fifteen antipodal vertex pairs \(\{\pm v\}\) of \(P\) define fifteen great circles on the sphere of plane normals, given by \(u\cdot v=0\). These circles form an arrangement with **120 triangular chambers**, **180 arcs**, and **62 intersection points** (equivalently 31 unoriented axes). The number \(n(u)\) is completely characterized as follows:

| Normal stratum | Number of unoriented axial directions | Number of section vertices |
|---|---:|---:|
| No mirror great circle | continuous: 120 open spherical chambers | 12 |
| Exactly one mirror great circle | continuous: open mirror arcs | 10 |
| Intersection of exactly two mirror great circles (twofold axis) | 15 | 8 |
| Intersection of exactly three mirror great circles (threefold axis) | 10 | 6 |
| Intersection of exactly five mirror great circles (fivefold axis) | 6 | 10 |

There are no other possibilities. Consequently, under Haar-uniform direction \(u\in S^2\), the section has twelve vertices with probability one. Nevertheless, the complete singular stratification is nonconstant: six-, eight-, and ten-sided sections arise in precisely the stated families of normal directions. The same polygon-count classification holds for any common positive scaling or rigid rotation of \(P\).

## Assumptions and scope

Take \(\varphi=(1+\sqrt5)/2\). Let \(I\) be the twelve points given by cyclic coordinate permutations of \((0,\pm1,\pm\varphi)\). Two vertices of \(I\) are adjacent exactly when their squared Euclidean distance is \(4\). There are thirty such icosahedral edges. If \(E_I\) is this set, define

\[
P=\operatorname{conv}\{(a+b)/2:\{a,b\}\in E_I\}.
\]

This is the edge-length-one regular icosidodecahedron: it has thirty vertices, sixty edges, twenty triangular facets, twelve pentagonal facets, and a center of inversion. A *normal direction* is oriented on \(S^2\); changing \(u\) to \(-u\) does not change the plane, so axial counts in the table identify antipodal directions. The central section is two-dimensional for every \(u\ne0\), and its vertices are counted without multiplicity, including vertices inherited from \(P\) if the plane passes through them.

## Proof

**1. Exact face graph.** Form all midpoints of icosahedral edges. The midpoint triples in each of twenty icosahedral faces lie on supporting planes of \(P\), giving twenty triangles. For each of the twelve icosahedral vertices, its five incident edge midpoints lie in a second supporting plane, giving a pentagon. Every one of these face planes has the asserted midpoint set as its exact contact set, as checked by inequalities in \(\mathbb Q(\sqrt5)\). They give thirty vertices, thirty-two facets and sixty edges, with each edge incident to one triangle and one pentagon. Every vertex has degree four. The executable certificate independently reconstructs and checks these supporting planes, contact sets and incidences.

**2. Intersections are controlled by the edge-sign vector.** For \(u\ne0\), write \(\sigma_u(v)=\operatorname{sgn}(u\cdot v)\) on vertices of \(P\). An edge with opposite nonzero endpoint signs meets \(u^\perp\) at one section vertex. Every original polytope vertex with sign zero is also a section vertex. There are no others. Therefore

\[
n(u)=\#\{ab\in E(P):\sigma_u(a)\sigma_u(b)<0\}
+\#\{v\in V(P):\sigma_u(v)=0\}.
\]

To justify the formula, a vertex of a polytope section arises either where a polytope edge crosses the plane strictly or at a polytope vertex already lying in the plane. Conversely, each strict crossing is a section vertex and each inherited polytope vertex remains extreme in the section. A whole polytope edge **may** lie inside the section plane: then both endpoints are counted as inherited vertices, not as strict edge crossings. Distinct strict edge crossings cannot coincide, and no inherited vertex coincides with a strict crossing. This formula therefore applies also at exceptional normals, including central equatorial cuts following existing polytope edges.

**3. Fifteen reflection mirrors and all generic sections.** The thirty midpoint vertices are organized in fifteen opposite pairs. The fifteen hyperplanes \(v^\perp\), for one \(v\) per pair, are exactly the directions where the vertex-sign vector may change. Each reflection through such a hyperplane preserves all thirty vertices: direct substitution into \(x\mapsto x-2(x\cdot v)v/(v\cdot v)\) verifies this in \(\mathbb Q(\sqrt5)\). Thus the reflection preserves \(P\), its edge graph, and \(n(u)\). The reflections act transitively on the chambers of their mirror arrangement: any two chambers can be joined by a generic path crossing mirrors transversely one at a time, and reflection in each crossed mirror exchanges adjacent chambers. The count \(n(u)\) is constant on every chamber by the sign formula. At \(u=(1,2,4)\) an exact enumeration gives twelve strict edge crossings and no on-plane vertices. Therefore **every generic section is a dodecagon**.

**4. Generic points on a single mirror.** Fix \(u\) orthogonal to precisely one antipodal vertex pair, \(\{v,-v\}\). Upon a small perturbation of \(u\), those two vertices acquire opposite signs; every other sign stays constant. Since each of \(v,-v\) has degree four and the polytope graph is centrally symmetric, the combined number of strict crossings on their eight incident edges on either nearby generic side is exactly four, regardless of the neighboring signs. At the mirror, those strict crossings vanish and exactly the two vertices \(v,-v\) are counted instead. The remaining edge intersections are unchanged. Thus \(n(u)=12-4+2=10\) on every open mirror arc.

**5. All exceptional axial directions.** Any intersection of mirror great circles corresponds to the projective line spanned by the cross product of two mirror normals. There are \(\binom{15}{2}=105\) pairs. In the exact quadratic field, normalize each nonzero cross product projectively by dividing through its first nonzero coordinate. Sorting these normalized triples yields exactly thirty-one distinct projective axes: fifteen with two incident mirrors, ten with three, and six with five; the pair-count identity \(15\binom22+10\binom32+6\binom52=105\) confirms completeness. For **all** thirty-one representatives, the sign formula gives respectively

\[
\begin{array}{c|c|c|c}
\text{mirrors through axis}&\text{strict crossing edges}&\text{on-plane polytope vertices}&n(u)\\\hline
2&4&4&8\\
3&0&6&6\\
5&0&10&10
\end{array}
\]

These equalities are verified exhaustively using exact field arithmetic by the supplied standalone checker; its short loops and arithmetic are included in full for reproduction, rather than being inferred from floating-point samples. Since a generic normal or a point in exactly one mirror has already been covered, this completes the classification.

**6. Spherical chamber counts.** The thirty-one projective axes produce sixty-two spherical intersection points. At an axis lying in \(m\) mirror great circles, there are \(2m\) outgoing spherical arcs at each of its two antipodal points. Summing half-degrees gives \(E=15\cdot 2\cdot2+10\cdot2\cdot3+6\cdot2\cdot5=180\). Spherical Euler's formula then gives \(F=2-62+180=120\). The chamber containing \((1,2,4)\) has exactly three axial corners, whose mirror multiplicities are respectively two, three, and five, as checked by exact inequalities against all fifteen mirror normals. Reflection-chamber transitivity forces all 120 chambers to be triangles. Their spherical areas are equal under reflection, so each has area \(4\pi/120=\pi/30\). The union of the fifteen great circles has zero spherical area, proving the Haar statement.

## Verification

Run `python3 check_sections.py` with Python 3 and no nonstandard dependencies. It uses exact rational pairs for \(a+b\sqrt5\), with arithmetic signs decided algebraically. It checks the twelve original icosahedron vertices, its thirty edges, the thirty midpoint vertices, the thirty-two exact supporting facets, the sixty edges of \(P\), all fifteen preserving reflections, all 105 pairs of mirrors, the thirty-one projective axes, every exceptional section count, one generic chamber, and one regular point on a mirror. Expected terminal marker: `EXACT_SECTION_CERT_OK`. The loops are finite and exhaustive because all relevant normals occur in open chambers, open mirror arcs, or mirror intersections. No numerical interpolation is used to promote finite experiments into infinite conclusions; constancy on chambers and arcs follows from the sign formula, and transitivity from the reflection action.

## Relationship to prior work

The connection between polygonal sections and polytope intersection complexity is classical; Padrol and Pfeifle (arXiv:1404.2443, publicly available 9 April 2014) give general results for polygons as sections, but do not classify central sections of this solid. Baez (arXiv:2309.15774) describes the icosidodecahedron as a rectified icosahedron and develops higher-dimensional connections without the central polygon-count stratification. The Coxeter reflection arrangement with fifteen mirror circles and 120 triangular fundamental chambers is **not claimed as new**. Similarly, regular decagonal equators of the icosidodecahedron are already illustrated in geometrical references; the contribution assessed here is the unified, all-normal count classification, including every twofold, threefold and fivefold degeneration. The different sixteen-plane icosidodecahedral arrangement studied by Liu (arXiv:1908.01280, Section 1) **explicitly describes** six central decagonal edge-equators and ten six-diagonal equators, so the existence of these individual ten- and six-sided axial cuts is *prior knowledge*. That paper analyzes the topology of its sixteen-plane arrangement rather than the fifteen vertex-normal mirrors and their full central section-vertex count function. The novelty question is therefore restricted to the collective all-orientations classification and the remaining strata; isolated six- and ten-sided equators are not claimed new. Related previous results for **orthogonal projections** of this solid concern a different operation and do not imply the section counts. A recorded icosahedral central-section distribution concerns a different input polytope.

## Limitations

The result concerns only *central* affine-plane sections of one regular solid, and classifies their vertex counts, not side lengths, areas, circumradii, or noncentral section distributions. The 120-chamber reflection structure is classical; no novelty of that arrangement is asserted. Related historical equatorial diagrams, geometric handbooks, and nonindexed teaching references may encode parts or even all of the section-type law; therefore definitive historical priority remains unestablished. The exact checker is reproducibility evidence and was reviewed within the present analysis, not independently certified by another party.

## References

1. Arnau Padrol and Julian Pfeifle, *Polygons as sections of higher-dimensional polytopes*, arXiv:1404.2443, first posted 9 April 2014. https://arxiv.org/abs/1404.2443
2. John C. Baez, *The Icosidodecahedron*, arXiv:2309.15774, first posted 26 September 2023. https://arxiv.org/abs/2309.15774
3. Ye Liu, *Topology of the icosidodecahedral arrangement*, arXiv:1908.01280, first posted August 2019. https://arxiv.org/abs/1908.01280
4. *Icosidodecahedron*, polyhedral reference with documented decagonal equatorial cuts. https://bendwavy.org/klitzing/incmats/id.htm
5. *Disdyakis triacontahedron*, geometric reference on the fifteen classical icosahedral mirror great circles and their 120 fundamental triangular chambers. https://en.wikipedia.org/wiki/Disdyakis_triacontahedron
