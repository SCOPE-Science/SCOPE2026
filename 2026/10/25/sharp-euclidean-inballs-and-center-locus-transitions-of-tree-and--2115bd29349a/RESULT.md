# Sharp Euclidean inballs and center-locus transitions of tree and cycle in-in zonotopes

## Finding
For a finite connected simple graph \(G=(V,E)\), let the *unit in-in zonotope* be
\[
I(G)=\sum_{v\in V}[-e_v,e_v]+\sum_{\{v,w\}\in E}[-(e_v-e_w),e_v-e_w]\subset\mathbb R^V.
\]
All distances use the **ambient standard Euclidean metric** on \(\mathbb R^V\). Write \(r(G)\) for its maximum inscribed-ball radius and \(\mathcal C(G)\) for the set of centers of balls having that radius. For \(S\subseteq V\), let \(\delta_G(S)\) be its crossing-edge set. The exact cut formula is
\[
\boxed{r(G)=\min_{\varnothing\ne S\subseteq V}\frac{|S|+|\delta_G(S)|}{\sqrt{|S|}}.}\tag{1}
\]
The minimizing sets are connected. The complete center locus is the polytope
\[
\boxed{\mathcal C(G)=\left\{c\in\mathbb R^V:\left|\sum_{v\in S}c_v\right|\le |S|+|\delta_G(S)|-r(G)\sqrt{|S|}\ \text{for every nonempty connected }S\subseteq V\right\}.}\tag{2}
\]

For every tree \(T\) on \(n\ge1\) vertices, let \(L\) be its number of leaves, with \(L=0\) for \(n=1\). Then
\[
\boxed{r(T)=\min\{\sqrt n,2\},\qquad
\dim\mathcal C(T)=\begin{cases}n-1,&1\le n\le3,\\n-L-1,&n=4,\\n-L,&n\ge5.\end{cases}}\tag{3}
\]
The numbers of facets tangent to the maximal ball centered at the origin are respectively \(2\), \(2(L+1)\), and \(2L\) in these three cases. For the star \(K_{1,n-1}\) with \(n\ge4\), placing its hub first,
\[
\boxed{\mathcal C(K_{1,n-1})=\{(t,0,\ldots,0):|t|\le n-2\sqrt n\}.}\tag{4}
\]

For every cycle \(C_n\), \(n\ge3\),
\[
\boxed{r(C_n)=\min\{\sqrt n,2\sqrt2\},\qquad
\dim\mathcal C(C_n)=\begin{cases}n-1,&3\le n\le7,\\1,&n=8,\\0,&n\ge9\text{ odd},\\1,&n\ge10\text{ even}.\end{cases}}\tag{5}
\]
The corresponding tangent-facet counts are \(2\) for \(3\le n\le7\), \(2n+2\) for \(n=8\), and \(2n\) for \(n\ge9\). For every even \(n\ge8\), indexing vertices cyclically by \(i=0,\ldots,n-1\),
\[
\boxed{\mathcal C(C_n)=\{c_i=(-1)^i t:\ |t|\le5-2\sqrt6\}.}\tag{6}
\]
For every odd \(n\ge9\), the origin is the unique incenter.

## Assumptions and scope
Every edge and coordinate segment in \(I(G)\) has half-length one (unit coefficients in the Minkowski sum); all graphs are finite, undirected, connected, and simple. The normalization is exactly the full-dimensional cube-plus-graphical-zonotope realization above, not the symmetric edge polytope \(\operatorname{conv}\{\pm(e_v-e_w)\}\) or the graphical zonotope confined to the zero-sum hyperplane. The graph \(C_3\) is the usual triangle. The tree case includes the single-vertex interval. The incenter set's dimension is affine dimension in ambient coordinates, and tangent facets refer to the origin-centered maximal ball, not all facets tangent at all possible centers.

## Proof
**1. Support function and cut minimization.** The support function is
\[
h_{I(G)}(u)=\sum_{v\in V}|u_v|+\sum_{\{v,w\}\in E}|u_v-u_w|.\tag{7}
\]
The body is full-dimensional and centrally symmetric. If a ball \(B(c,\rho)\) lies inside it, so does \(B(-c,\rho)\), and convexity of their midpoint gives \(B(0,\rho)\subset I(G)\). Hence \(r(G)=\inf_{u\ne0}h_{I(G)}(u)/\|u\|_2\).

For any sign-changing \(u\), its positive part \(u^+\) and (absolute) negative part \(u^-\) have disjoint supports and satisfy \(h(u)=h(u^+)+h(u^-)\) because \(|u_v-u_w|=|u^+_v-u^+_w|+|u^-_v-u^-_w|\). Consequently \(h(u)/\|u\|_2\) strictly exceeds the smaller corresponding nonzero-sign-part quotient; a minimizer has one sign. For \(u\ge0\), the layer-cake and graph-coarea identities, with \(S_s=\{v:u_v>s\}\), yield
\[
u=\int_0^\infty\mathbf1_{S_s}\,ds,\qquad h(u)=\int_0^\infty\bigl(|S_s|+|\delta_G(S_s)|\bigr)\,ds.\tag{8}
\]
Set \(R=\min_{S\ne\emptyset}(|S|+|\delta S|)/\sqrt{|S|}\). Since \(\|\mathbf1_S\|_2=\sqrt{|S|}\), Minkowski's integral inequality gives
\[
h(u)\ge R\int_0^\infty\|\mathbf1_{S_s}\|_2\,ds\ge R\|u\|_2.\tag{9}
\]
Every test direction \(u=\mathbf1_S\) attains exactly its associated cut quotient. This proves (1). Strict convexity of the Euclidean norm in the second inequality also shows every minimizing direction is a scalar signed indicator of one minimizing set. If a minimizing \(S\) had at least two graph-connected components, its cut numerator would be the sum of component numerators, which is strictly greater than \(R\sqrt{|S|}\), since the sum of their square-root sizes exceeds \(\sqrt{|S|}\). Thus every minimizing \(S\) is connected.

**2. Facet and center criterion.** At a support direction \(u\), a coordinate segment is free precisely when \(u_v=0\), and an edge segment is free precisely when \(u_v=u_w\). The direction space of the exposed face therefore has dimension \(n-m\), where \(m\) is the number of graph-connected components among vertices at equal *nonzero* values of \(u\) (each distinct nonzero value defines its own component collection). This is a facet iff \(m=1\). Hence every facet has outward normal a nonzero multiple of \(\pm\mathbf1_S\) for a nonempty connected set \(S\); conversely each such set determines a facet. Its supporting hyperplane is
\[
\pm\sum_{v\in S}x_v=|S|+|\delta_G(S)|.\tag{10}
\]
The ball \(B(c,r)\) lies in this halfspace pair iff \(|\sum_{v\in S}c_v|+r\sqrt{|S|}\le|S|+|\delta S|\), proving (2). At \(c=0\), exactly the minimizing sets in (1) yield tangent facet pairs.

**3. Tree extremizers.** For a connected tree, a proper nonempty \(S\) has \(|\delta S|\ge1\), so with \(k=|S|\),
\[
\frac{k+|\delta S|}{\sqrt k}\ge\sqrt k+\frac1{\sqrt k}\ge2.\tag{11}
\]
Equality holds iff \(k=1\) and \(S\) is a leaf. The full set contributes \(\sqrt n\). This proves the radius and minimizing-set classification, including the tie at \(n=4\). At a maximizing center every active ±facet pair forces \(\sum_{v\in S}c_v=0\); their indicator vectors are linearly independent except for a possible trivial redundancy when all vertices are leaves (impossible for a tree on \(n\ge3\)). For \(n\le3\) the full-set indicator is the only contact and has rank one. For \(n=4\), the full-set indicator and \(L\) leaf indicators have rank \(L+1\). For \(n\ge5\), the \(L\) leaf indicators have rank \(L\). Every non-contact facet inequality is strict at \(c=0\); hence the center locus has nonempty relative interior in exactly these linear equality spaces. Its dimensions are those in (3). For a star with \(n\ge4\), the \(n-1\) leaf coordinates of a center vanish; a connected subset either is a singleton leaf or contains the hub with \(k\) leaves, for which the cut numerator equals \(n\). Equation (2) gives \(|t|\le n-2\sqrt{k+1}\) for \(0\le k\le n-1\). The strongest is \(k=n-1\), yielding (4).

**4. Cycle extremizers.** A proper nonempty cycle subset has at least two crossing edges. Therefore
\[
\frac{k+|\delta S|}{\sqrt k}\ge\sqrt k+\frac2{\sqrt k}\ge2\sqrt2,\tag{12}
\]
with equality iff \(k=2\) and \(S\) is an adjacent pair. The full set gives \(\sqrt n\), establishing both (5)'s radius and the contact counts, with the exact tie at \(n=8\). For \(n\ge9\), equations for all contacting adjacent pairs read \(c_i+c_{i+1}=0\). For an odd cycle they imply \(c=0\). For an even cycle they leave exactly the alternating line. At \(n=8\), the additional full-set contact is automatically satisfied by an alternating vector; for \(3\le n\le7\) only the full-set equation remains. Strict slack at \(c=0\) for every other facet proves all dimensions asserted in (5).

For even \(n\ge8\), put \(c_i=(-1)^i t\). Every connected proper set is a contiguous cyclic interval of length \(k\). For even \(k\), its center sum is zero. For odd \(k\), its sum has absolute value \(|t|\), and its boundary has two edges. Thus (2) is exactly the family \(|t|\le k+2-2\sqrt{2k}\) over odd \(1\le k\le n-1\). The \(k=1\) bound is \(3-2\sqrt2\), the \(k=3\) bound is \(5-2\sqrt6\), which is smaller, and for \(k\ge3\) the function \(k+2-2\sqrt{2k}\) is strictly increasing. The full-set constraint is automatic. Therefore the smallest bound is achieved at \(k=3\) and (6) holds, including its strictly positive width.

## Verification
The standalone `verify.py` uses standard Python and exact rational arithmetic for all discrete cut and rank comparisons. It enumerates all labeled trees on up to six vertices, cycles of orders three through fifteen, independently compares support values on thousands of small integer vectors, and checks the proposed tree/cycle contact-space dimensions. It also checks all connected-cut center inequalities for the even-cycle segment endpoints up to order fourteen. It reports:

```text
EXACT_OK labeled_trees=1442 cycles=13 contact_cuts=4225 raw_support_vectors=7768
CENTER_OK all_cut_cycle_segment_checks=21756 star_bounds=117
```

These are corroborations and do not substitute for the all-order proof above; the even-cycle segment endpoint feasibility checks use floating-point square-root comparisons with an explicit tolerance.

## Relationship to prior work
Glew, *Geometry of in-in correlators* (2026), introduced the in-in zonotope and supplied a Minkowski-sum realization, facets indexed by connected subgraphs, and a small-order face-number table. The normalization (7) follows from that known construction; neither the support function alone nor the existing facet description is claimed as new. The contribution is the exact Euclidean cut quotient, sharp tree and cycle thresholds, tangent-facet counts, complete center-locus dimensions, and explicit alternating or star center segments.

He, Li, Su, and Zhu, *Tropical and Stringy Integrals for In-In Correlators* (2026), independently identify the polytope's support function with a vertex-space integral and emphasize its volume/stringy geometry. Its accessible abstract and article overview do not state these inball classifications; its complete primary text was not accessible for this comparison, so differently worded earlier results remain a residual risk.

The published weighted graphical-zonotope inradius formula concerns an edge-only zonotope intrinsic to the zero-sum subspace and has a *centered-cardinality* cut denominator; it does not imply the ambient-metric, cube-plus-edge cut formula (1) or the center loci. The published path/cycle symmetric-edge-polytope formulas concern **convex hulls** of signed edge roots, rather than their Minkowski sum with a full cube. The full text of Padrol, Pilaud and Poullot addresses deformations of graphical zonotopes, not the present metric classification. Earlier literature could contain equivalent formulations under different names; all originality assessments are limited to material actually inspected.

## Limitations
Only unit coefficients, the standard Euclidean metric, and unweighted finite simple connected graphs are classified. No weighted-edge or unequal-coordinate generalization, physical prediction, canonical-form identity, or independent external audit is asserted. Tree and cycle results are proved for every allowed finite order; the checker covers only bounded cases. The general formula (1) is a structural intermediate result, while the tree/cycle phase diagrams and center classifications are the principal new claims.

## References
1. Ross Glew, *Geometry of in-in correlators*, arXiv:2601.18903, first public 2026-01-26; *Physical Review Letters* **137** (2026), 161603, DOI 10.1103/39dm-2rsw.
2. Song He, Xiang Li, Yong-Xiang Su, Fan Zhu, *Tropical and Stringy Integrals for In-In Correlators*, arXiv:2608.19720, first public 2026-08-20.
3. Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first public 2021-11-24.
4. Published published-finding corpus, *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, `2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab`.
5. Published published-finding corpus, *Cycle symmetric edge polytopes have a parity-split exact Euclidean inradius*, `2026/10/11/SCOPE-cycle-symmetric-edge-polytopes-have-a-parity-split-exact-euclide--07f34c5bcbf4`.
6. Published published-finding corpus, *Path symmetric edge polytopes have an exact inradius and a codimension-one incenter family*, `2026/10/11/SCOPE-path-symmetric-edge-polytopes-have-an-exact-inradius-and-a-codim--4fbd84888e21`.
