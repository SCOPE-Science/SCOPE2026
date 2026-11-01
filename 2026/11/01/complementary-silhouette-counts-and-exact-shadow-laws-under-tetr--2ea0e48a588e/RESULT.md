# Complementary silhouette counts and exact shadow laws under tetrahedral vertex truncations

## Finding
Let \(T=\operatorname{conv}(v_0,v_1,v_2,v_3)\subset\mathbb R^3\) be an arbitrary nondegenerate tetrahedron. Denote by \(F_i\) the facet opposite \(v_i\), with outward unit normal \(n_i\). For every subset \(S\subseteq\{0,1,2,3\}\), cut off each vertex \(v_i\) with \(i\in S\) by a plane parallel to \(F_i\), leaving a polytope \(T_S\); allow independently chosen truncation depths, subject to the disjointness assumptions stated below.

For a unit viewing direction \(u\), let \(N_S(u)\) be the number of vertices of the orthogonal planar shadow of \(T_S\). For every generic \(u\), put \(s_i(u)=\operatorname{sgn}(n_i\cdot u)\). Then the exact silhouette count is
\[
\boxed{N_S(u)=\sum_{0\le i<j\le3}{\bf1}_{\{s_i\ne s_j\}}
+\sum_{i\in S}\sum_{j\ne i}{\bf1}_{\{s_i=s_j\}}.}\tag{1}
\]
The formula is independent of truncation depth. A pointwise complementary-pair law follows:
\[
\boxed{N_S(u)+N_{S^c}(u)=12\qquad\text{for every generic }u.}\tag{2}
\]
Thus two complementary truncations viewed along the *same* line have perfectly anticorrelated shadow-vertex counts; their sum is identically twelve, for every tetrahedral shape and all admissible depths.

For a regular tetrahedron and a Haar-uniform random viewing line, the entire five-stage distribution depends only on the number \(r=|S|\) of truncated vertices and not on which vertices or on their depths. Put
\[
p=\frac6\pi\arccos\left(\frac13\right)-2
=0.3509593121836436\ldots.
\tag{3}
\]
The exact distributions, with every unlisted probability zero, are

| Number of truncated vertices | Shadow vertex count and probability |
| --- | --- |
| \(r=0\) | \(\Pr(N=3)=p\), \(\Pr(N=4)=1-p\) |
| \(r=1\) | \(\Pr(N=3)=p/4\), \(\Pr(N=5)=1-p/4\) |
| \(r=2\) | \(\Pr(N=5)=p/2\), \(\Pr(N=6)=1-p\), \(\Pr(N=7)=p/2\) |
| \(r=3\) | \(\Pr(N=7)=1-p/4\), \(\Pr(N=9)=p/4\) |
| \(r=4\) | \(\Pr(N=8)=1-p\), \(\Pr(N=9)=p\) |

The first row is the classical untruncated-tetrahedron distribution and is prior work. The new contributions are the all-shape same-direction complement (2), the exact transfer formula (1), and the complete partial-truncation laws in the remaining four rows. In particular, every four-corner truncation has **only octagonal or nonagonal generic shadows**, and the nonagon probability equals the triangular-shadow probability of its original tetrahedron.

## Assumptions and scope
Write the point on each edge incident to \(v_i\) at truncation fraction \(t_i\in(0,1)\) from \(v_i\), and put \(t_i=0\) for \(i\notin S\). The truncating plane opposite \(F_i\) is the barycentric plane \(\lambda_i=1-t_i\), retaining the part \(\lambda_i\le1-t_i\). Require \(t_i+t_j<1\) for all distinct \(i,j\). This ensures that all selected cuts are disjoint, the original six facet-to-facet edges persist with positive length, and no two new triangular facets meet along an edge.

The viewing direction \(u\) is any unit vector for which \(n_i\cdot u\ne0\) for all four indices and which avoids the finite further set of projection degeneracies. The exceptional set has zero spherical area; it may change the naive count if polygon vertices overlap. An unoriented line is represented by either \(u\) or \(-u\); both yield the same count. In the regular case the viewing line is uniformly distributed on the real projective plane, equivalently a uniformly random unit \(u\in S^2\).

Neither perpendicularity of the truncation planes to any edge nor equal cut depths is assumed. Equation (2) couples two independently chosen depth vectors for the complementary cut sets, provided each satisfies the disjointness condition; it compares the shadows along the same viewing direction. In particular it does not assert the sum for two independent random viewing directions.

## Proof
**1. A facet-sign lemma.** Let \(K\subset\mathbb R^3\) be any convex polyhedron and consider a generic orthogonal projection along \(u\). A polyhedron edge common to facets with outward normals \(a\) and \(b\) is on the projected silhouette precisely when \((a\cdot u)(b\cdot u)<0\). Indeed, a neighborhood of the projected edge is a boundary neighborhood exactly when one facet faces toward and the other away from the viewer; when their signs agree, both lie on the same visible or hidden side and their shared edge projects into the interior. For a generic projection, silhouette edges join to form the boundary polygon, and their number equals the number of polygon vertices. This proves the count lemma independently of symmetry or edge length.

**2. Enumerating all edge types under disjoint truncation.** For every unordered pair \(\{i,j\}\), the original facets \(F_i,F_j\) meet along a surviving edge in \(T_S\), contributing \({\bf1}_{\{s_i\ne s_j\}}\). If \(i\in S\), the newly exposed triangle at \(v_i\) has outward normal \(-n_i\), and it meets each of the three original facets \(F_j\) with \(j\ne i\). By the sign lemma, each such edge contributes \({\bf1}_{\{-s_i\ne s_j\}}={\bf1}_{\{s_i=s_j\}}\). The disjointness hypothesis excludes further edge types. Summing over all six original edges and the new cut-to-old edges proves (1).

**3. The complementary law, without symmetry.** Add (1) for \(S\) and \(S^c\). For each unordered pair \(\{i,j\}\), if \(s_i\ne s_j\), its original-facet edge contributes once to each polytope, giving exactly two. If \(s_i=s_j\), the original-facet edge contributes zero in both polytopes, while each endpoint index belongs to exactly one of \(S,S^c\); the two new-to-old facet-edge indicators contribute one each, again giving two. There are six unordered pairs. Hence their total is \(6\cdot2=12\), which proves (2). This argument also proves independence from the chosen admissible cut depths.

**4. Complete sign-chamber enumeration for the regular tetrahedron.** Since the facet areas are positive and \(\sum_iA_in_i=0\), no generic viewing direction makes all four signs equal. Let \(k\in\{1,2,3\}\) be the number of positive facet signs. The original-edge contribution is \(k(4-k)\): it equals three for \(k=1,3\) and four for \(k=2\). The strict sign pattern is determined by the positive-index subset of size \(k\), yielding fourteen possibilities.

For a regular tetrahedron the eight chambers with a singleton sign (\(k=1\) or \(k=3\)) are congruent under tetrahedral rotations and antipodal inversion. Their total probability equals the known triangular-shadow probability \(p\) in (3): each of the four vertex tangent cones has spherical solid angle
\[
\Omega=3\arccos(1/3)-\pi,
\]
and the union of its cone and antipodal cone gives \(\Pr(N_\varnothing=3)=4\Omega/(2\pi)=p\). Thus each singleton-sign pattern has probability \(p/8\). The six balanced (two-plus, two-minus) chambers are congruent under tetrahedral permutations; by normalization each has probability \((1-p)/6\). No sign pattern is omitted.

For a fixed truncated index set \(S\), the number of additional silhouette edges in (1) is exactly the number of ordered incidences \((i,j)\) with \(i\in S\), \(j\ne i\), and \(s_i=s_j\). If \(k=2\), every chosen index has exactly one other index of its sign, so \(N_S=4+r\). If \(k=1\) or \(3\), there is exactly one minority index \(m\); that index has no same-sign partners and each majority index has two. Consequently
\[
N_S=3+2\bigl(r-{\bf1}_{\{m\in S\}}\bigr)
\quad\text{in singleton-sign chambers}.\tag{4}
\]
Each of the four minority indices has total probability \(p/4\) across its positive and negative singleton-sign chambers. Therefore the singleton-sign contribution has \(m\in S\) with probability \(rp/4\) and \(m\notin S\) with probability \((4-r)p/4\), while the balanced contribution has probability \(1-p\) and count \(4+r\). Substituting \(r=0,1,2,3,4\) yields the complete table. This also proves that the table is independent of which \(r\) vertices were cut and independent of the admissible depths.

**5. Full-truncation transfer for an arbitrary tetrahedron.** For \(S=\{0,1,2,3\}\), (2) gives \(N_S=12-N_\varnothing\). A generic shadow of any tetrahedron has three or four vertices. Hence a fully vertex-truncated nondegenerate tetrahedron has only eight or nine generic silhouette vertices. Moreover, if the original vertex tangent cone solid angles are \(\Omega_i\), the known formula for triangular shadows gives
\[
\Pr(N_S=9)=\frac1{2\pi}\sum_{i=0}^3\Omega_i,\qquad
\Pr(N_S=8)=1-\frac1{2\pi}\sum_{i=0}^3\Omega_i.
\tag{5}
\]
The novelty in (5) is the *truncation transfer* and the pathwise pairing; the solid-angle formula for the untruncated tetrahedron is prior work.

## Verification
The standalone `verify.py` evaluates the sign-count prediction for all sixteen vertex subsets on three geometrically different nondegenerate tetrahedra (regular, asymmetric and flattened) and compares it against independently computed planar convex hulls from the actual truncated vertex coordinates. It checks the complement identity for every subset and direction. All **28,800 projected-convex-hull comparisons** passed.

The checker separately enumerates all fourteen strict four-sign patterns using exact symbolic probability masses \(p/8\) and \((1-p)/6\), verifying the five stated distributions as symbolic identities, not floating-point fitting. Finally it compares the five laws with **250,000 independent Haar-normal samples** for the regular tetrahedron. The executable is `python verify.py`, requiring `numpy`, `scipy`, `sympy`; it emits a line beginning with `PASS:` on success.

These finite tests do not certify infinitely many shapes, directions, or cut depths. The all-shape statements are established by the exact facet-sign and edge-enumeration proof above. The sampler tests the table statistically rather than replacing the spherical-cone calculation.

## Relationship to prior work
Feldman and Klain (2008), *Angles as probabilities*, establish the triangular-shadow probability of an arbitrary untruncated tetrahedron from vertex cone angles. Formula (3), the first row of the table, and the solid-angle portion of (5) use that known result; none is presented as a new discovery.

Published work on orthogonal silhouettes of tetrahedra provides finer area-weighted triangular/quadrilateral shadow moments, again for the **untruncated** tetrahedron; it does not imply (1), the complementary same-direction coupling (2), or the sequence of partial-cut probability laws. This distinction is about statements and implications rather than the presence of the word "tetrahedron" in a title.

Al-Ajmi, Koca and Bait Bu Salasel (2015) examine particular Coxeter-plane projections, including truncated tetrahedral examples. Geometric references also illustrate octagonal and nonagonal projections of a truncated tetrahedron. Such selected views do not give the all-direction classification, tetrahedron-shape generality, depth independence, coupling, or Haar distributions of the present theorem. The 2026 paper *Area-weighted silhouette probabilities of arbitrary tetrahedra* likewise treats untruncated silhouettes and conditional area moments, not the paired truncation law.

## Limitations
All cuts must be parallel to their opposite original faces and pairwise disjoint in the stated edge-fraction sense. Oblique cuts, overlapping cuts, arbitrary non-convex surgeries, and nongeneric directions are not covered by the generic-shadow formula. The five-stage probability table uses regularity of the **original** tetrahedron and Haar-uniform viewing directions; it does not claim the same probabilities for asymmetric original tetrahedra, although the exact count formula and complementary law remain valid for all of them. The theorem concerns combinatorial shadow vertex counts, not the distributions of shadow area or perimeter.

Published specific-view examples of octagonal and nonagonal truncated-tetrahedral shadows are prior art. An unindexed general-polyhedron stereology treatment could already contain the complete transfer law; this remains a residual historical originality risk. Independent review has not been performed.

## References
1. D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459v1 (first public version 19 September 2008), Theorem 1. https://arxiv.org/abs/0809.3459
2. M. Al-Ajmi, M. Koca and H. Bait Bu Salasel, *Projection of Polyhedra onto Coxeter Planes Described with Quaternions*, 2015, DOI: 10.24200/squjs.vol19iss2pp77-90.
3. *The Truncated Tetrahedron*, geometrical projection reference, https://www.qfbox.info/4d/trunctet (projection examples).
4. *Area-weighted silhouette probabilities of arbitrary tetrahedra*, publicly available geometric research manuscript, 2026 (untruncated area-weighted silhouettes).
