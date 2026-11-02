# Exact joint directional-width and central-section law of the regular icosahedron

## Finding

Let \(P\subset\mathbb R^3\) be a regular icosahedron of circumradius \(R\), and let \(U\) be Haar-uniform on the unit sphere. Denote by \(N\) the number of edges of the central section \(P\cap U^\perp\), and let the normalized width in its normal direction be
\[
Z=\frac{\max_{v\in P}\langle U,v\rangle-\min_{v\in P}\langle U,v\rangle}{2R}.
\]
Set
\[
a=\arcsin(1/\sqrt5),\qquad b=\arccos\sqrt{(1+1/\sqrt5)/2},\qquad B(h)=\arctan\!\left(\frac{\tan h}{\cos(\pi/5)}\right).
\]
For \(\cos B(h)\le z\le\cos h\), put
\[
L(z,h)=2\left[\arccos\!\left(\frac{\sin h}{\sqrt{1-z^2}}\right)-z\arccos\!\left(\frac{z\tan h}{\sqrt{1-z^2}}\right)\right].
\]
Define the following explicit elementary function for either \(h=a\) or \(h=b\):
\[
C_h(z)=\begin{cases}
0,&z\ge1,\\
2\pi(1-z),&\cos h\le z<1,\\
2\pi(1-z)-5L(z,h),&\cos B(h)<z<\cos h,\\
2\pi(1-\cos B(h))-5L(\cos B(h),h),&z\le\cos B(h).
\end{cases}
\]
The **complete joint law**, expressed as joint survival functions valid for every real \(z\), is
\[
\boxed{\Pr(N=10,\ Z\ge z)=\frac3\pi C_a(z),\qquad
\Pr(N=12,\ Z\ge z)=\frac3\pi\bigl(C_b(z)-C_a(z)\bigr).}
\]
All other generic section sizes have probability zero. In particular,
\[
\Pr(N=12)=\frac{15}{\pi}\arccos(1/\sqrt5)-5\approx0.2862457352435,
\]
and \(\Pr(N=10)\approx0.7137542647565\). The support of \(Z\) is exactly
\[
\left[\sqrt{(5+2\sqrt5)/15},\ 1\right].
\]
The joint law has **sharp type-separated ends**. Almost surely, \(Z<\sqrt{(1+1/\sqrt5)/2}\) implies \(N=12\), while \(Z>2/\sqrt5\) implies \(N=10\). On the intervening open width interval, both types occur with positive joint density.

## Assumptions and scope

The icosahedron is Euclidean, regular and centered. Its scale does not matter because width is divided by \(2R\). The plane \(U^\perp\) passes through the center, and the *same* normal \(U\) determines both the central-section size and directional width. The distribution on normal directions is normalized surface area on \(S^2\); the exceptional normals for which a section passes through a vertex or the width has multiple distinct supporting vertices form a null set.

## Proof

**1. Exact vertex and edge geometry.** Write \(\varphi=(1+\sqrt5)/2\). We may take the vertices to be all sign choices of the three coordinate families
\[
(0,\pm1,\pm\varphi),\qquad(\pm1,\pm\varphi,0),\qquad(\pm\varphi,0,\pm1).
\]
Every vertex has squared radius \(R^2=1+\varphi^2\), and two vertices are joined by an edge precisely when their squared Euclidean distance equals \(4\). The resulting graph has \(30\) edges and \(20\) triangular facets. Neighboring unit vertex directions have dot product \(1/\sqrt5\).

**2. Exhaustive central-section type partition.** The \(12\) vertices form six antipodal pairs, whose perpendicular great circles are distinct and in general position: every triple of representative vertex vectors has nonzero determinant. Six such great circles have exactly \(6(6-1)+2=32\) connected sign chambers. An exact sign calculation produces \(32\) distinct representative chambers: the \(12\) vertex rays and \(20\) outward facet-normal rays. At vertex rays the crossing-edge count is \(10\); at facet rays it is \(12\). A generic central section has one vertex for each crossed edge, hence precisely these two section types occur, and the displayed representatives exhaust the arrangement. These tests are implemented with exact arithmetic in \(\mathbb Q(\sqrt5)\) in the accompanying program.

**3. Two nested regular spherical pentagons.** For each icosahedron vertex direction \(q\), consider its spherical Voronoi cell \(Q_q\): the set of unit directions \(u\) maximizing \(u\cdot v\) over the twelve normalized vertices at \(v=q\). The five neighboring vertices give the five supporting Voronoi bisectors; \(Q_q\) is a regular spherical pentagon of inradius \(b\), with area \(4\pi/12=\pi/3\). Inside \(Q_q\), the width is \(Z=u\cdot q\).

The normal-sign chamber around \(q\) is the regular spherical pentagon \(K_q\) given by positive dot products with the five neighbors of \(q\). Their sum is \(\sqrt5\,q\), so positivity also implies \(u\cdot q>0\), fixing the signs of all six antipodal pairs. The five bounding great circles have distance \(a=\arcsin(1/\sqrt5)\) from \(q\). For each neighbor \(w\), the normalized sum \((q+w)/\|q+w\|\) is one vertex of \(K_q\), since its dot products with two other neighbors vanish. The same point is the midpoint of the corresponding side of \(Q_q\). The exact neighbor-incidence calculation proves this for all five neighbors, so \(K_q\subset Q_q\), with its five vertices at the side midpoints of the outer pentagon.

The \(12\) chambers \(K_q\) are precisely those giving decagonal sections. Their complement consists of the \(20\) twelve-sided-section chambers. Thus the intersection of a cap \(u\cdot q\ge z\) with \(K_q\) contributes exactly the joint event \((N=10,Z\ge z)\) inside \(Q_q\), and the annular difference \(Q_q\setminus K_q\) contributes \((N=12,Z\ge z)\).

**4. Exact cap–pentagon area.** A regular spherical pentagon of inradius \(h\) has circumradius \(B(h)\): the spherical right triangle formed by its center, one vertex and the midpoint of an incident edge gives \(\tan B(h)=\tan h/\cos(\pi/5)\). The area of its intersection with a concentric cap of angular radius \(\rho=\arccos z\) is \(C_h(z)\). For \(\rho\le h\), the cap is wholly inside, giving area \(2\pi(1-z)\); for \(\rho\ge B(h)\), the whole pentagon is inside.

In the intermediate range, each of the five sides cuts a spherical segment out of the cap. The five removed segments are disjoint in area until the cap reaches a pentagon vertex. In polar coordinates about the center, one segment has area
\[
2\int_h^{\arccos z}\arccos\!\left(\tan h\cot t\right)\sin t\,dt.
\]
Integration by parts evaluates this integral to \(L(z,h)\). Removing five segments gives the stated piecewise \(C_h(z)\), without any unevaluated integrals. The exact identities \(B(a)=b\), \(\cos B(b)=\sqrt{(5+2\sqrt5)/15}\), and \(C_b(-1)=\pi/3\) locate the thresholds and establish normalization. The inner pentagon has area \(C_a(-1)=2\pi-5\arccos(1/\sqrt5)\) by spherical excess.

**5. Haar aggregation.** The \(12\) congruent outer pentagons partition the sphere. Consequently the probability of any cap–inner-pentagon event equals \(12 C_a(z)/(4\pi)\), and the probability of its annular counterpart equals \(12(C_b(z)-C_a(z))/(4\pi)\). This proves both joint-survival identities and all stated support and type-separation consequences.

## Verification

Run `python verify.py` after installing the two dependencies in `requirements.txt`. It reconstructs the complete icosahedral edge and facet lists and checks every relevant algebraic determinant in \(\mathbb Q(\sqrt5)\). It exhausts all \(32\) sign chambers, checks \(12\) decagon and \(20\) dodecagon representatives, proves neighbor-midtangent containment inequalities exactly, compares the cap formula with a separate numerical polar-angle quadrature, and performs a seeded simulation of \(30{,}000\) orientations as an independent plausibility check. The exact combinatorics and analytical integration—not the numerical quadrature or simulation—prove the theorem for all real \(z\).

## Relationship to prior work

Brandenburg, De Loera and Meroni (2023, Theorem 1.1 and Lemma 2.1) establish general central-section chamber decompositions and show why edge-crossing sets are constant in a chamber; they do not give the evaluated joint law here. The published *Exact Haar polygon-type law for central icosahedron sections* determines the discrete marginal \(N\), not the conditional distribution of the continuous directional width. Earlier joint silhouette–section type calculations likewise concern two discrete polygon counts rather than width. Finch (2011) studies width moments of selected Platonic solids. Abas (2026) gives a general co-area representation for polyhedral width densities and explicit models for other polyhedra, but no icosahedron central-section-type joint law was found in the inspected text. The new content claimed here is the **two-component exact joint distribution** and its sharp type-separated width intervals, not the general chamber method, the width-as-support-function identity, or the separate section marginal.

## Limitations

The result applies to *central* sections and the *same* normal used to measure width. It does not give section polygon areas, independently oriented planes, off-center sections, or a distribution for a deformed icosahedron. Mathematical correctness has received only self-review; no independent audit has been performed. Historical priority remains provisional, including possible specialized literature not found in the inspected searches. The proof of the infinite continuum law is analytic; finite numerical checks only corroborate it.

## References

- M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239, first version 27 April 2023, especially Theorem 1.1, Lemma 2.1 and Section 5. https://arxiv.org/abs/2304.14239
- O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, first version 10 August 2026, especially the polyhedral width co-area formula. https://arxiv.org/abs/2609.26202
- S. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671 (2011). https://arxiv.org/abs/1110.0671
- *Exact Haar polygon-type law for central icosahedron sections*, published mathematical research record. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f
