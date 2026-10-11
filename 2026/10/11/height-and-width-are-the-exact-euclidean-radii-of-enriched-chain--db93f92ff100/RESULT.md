# Height and width are the exact Euclidean radii of enriched chain polytopes
## Finding
Let \(P\) be a nonempty finite poset. Write
\[
h(P)=\max\{|C|:C\subseteq P\text{ is a chain}\},
\qquad
w(P)=\max\{|A|:A\subseteq P\text{ is an antichain}\}.
\]
Its enriched chain polytope is
\[
\mathcal C^{(e)}(P)
=
\operatorname{conv}
\left\{
x\in\{-1,0,1\}^{P}:
\operatorname{supp}(x)\text{ is an antichain}
\right\}
\subseteq\mathbb R^{P}.
\]

With the standard Euclidean metric,
\[
\boxed{
r_{\mathrm{in}}\!\left(\mathcal C^{(e)}(P)\right)
=
\frac1{\sqrt{h(P)}}
}
\tag{1}
\]
and
\[
\boxed{
R_{\mathrm{out}}\!\left(\mathcal C^{(e)}(P)\right)
=
\sqrt{w(P)}.
}
\tag{2}
\]

If \(r_*=1/\sqrt{h(P)}\), the complete set of centers of largest inscribed Euclidean balls is
\[
\boxed{
\left\{
c\in\mathbb R^{P}:
\sum_{v\in C}|c_v|
\le
1-\sqrt{\frac{|C|}{h(P)}}
\quad
\text{for every maximal chain }C
\right\}.
}
\tag{3}
\]
In particular, the origin is always an incenter, and it is the unique incenter if and only if every element of \(P\) belongs to a chain of cardinality \(h(P)\).

Let \(L_h(P)\) be the number of maximal chains having cardinality \(h(P)\). The centered largest ball is tangent to exactly
\[
\boxed{
2^{h(P)}L_h(P)
}
\tag{4}
\]
facets: precisely the facets indexed by a longest maximal chain together with an arbitrary sign pattern on that chain.

The circumcenter is uniquely the origin. Its minimum enclosing sphere meets the polytope exactly at the signed characteristic vectors of maximum antichains. If \(A_w(P)\) is the number of antichains of cardinality \(w(P)\), then the outer contact set has exactly
\[
\boxed{
2^{w(P)}A_w(P)
}
\tag{5}
\]
points.

Thus the two fundamental order invariants are recovered directly from the canonical Euclidean geometry:
\[
\boxed{
h(P)=r_{\mathrm{in}}^{-2},
\qquad
w(P)=R_{\mathrm{out}}^2,
\qquad
\frac{R_{\mathrm{out}}}{r_{\mathrm{in}}}
=
\sqrt{h(P)w(P)}.
}
\tag{6}
\]

## Assumptions and scope
Chains and antichains are counted by cardinality. A maximal chain means inclusion-maximal as a chain, while a longest chain means a chain of cardinality \(h(P)\). Every longest chain is maximal, but maximal chains can have smaller cardinality when \(P\) is not pure.

The enriched chain polytope is the centrally symmetric poset polytope introduced in the literature and also called the unconditional chain polytope. No purity, grading, connectedness, or natural labeling assumption is required.

The metric is the standard Euclidean metric on \(\mathbb R^{P}\). The result is therefore about this canonical realization and is not invariant under arbitrary affine transformations.

## Proof
A facet description proved in the enriched-poset-polytope literature says that every facet of \(\mathcal C^{(e)}(P)\) has the form
\[
\sum_{v\in C}\varepsilon_v x_v\le1,
\tag{7}
\]
where \(C\) is a maximal chain and each
\[
\varepsilon_v\in\{-1,1\}.
\]
Moreover every inequality in (7) is facet-defining.

For a fixed maximal chain \(C\), the Euclidean norm of the normal in (7) is
\[
\sqrt{|C|}.
\tag{8}
\]
Hence a Euclidean ball of radius \(r\) centered at \(c\) lies in every signed facet halfspace associated with \(C\) if and only if
\[
\sum_{v\in C}\varepsilon_v c_v+r\sqrt{|C|}\le1
\]
for every sign pattern. Maximizing over all sign patterns gives the equivalent condition
\[
\sum_{v\in C}|c_v|+r\sqrt{|C|}\le1.
\tag{9}
\]

Let \(C_*\) be any longest chain, so \(|C_*|=h(P)\). Equation (9) implies for every inscribed ball
\[
r\sqrt{h(P)}
\le
1-\sum_{v\in C_*}|c_v|
\le1.
\]
Therefore
\[
r\le\frac1{\sqrt{h(P)}}.
\tag{10}
\]
At \(c=0\), all inequalities (9) hold with
\[
r=\frac1{\sqrt{h(P)}}
\]
because every maximal chain has cardinality at most \(h(P)\). This proves (1).

Substituting the optimal radius into (9) gives exactly (3). If every element lies on a longest chain, every coordinate of an incenter is forced to vanish by the zero right-hand side for those longest chains, so the origin is the unique incenter.

Conversely, suppose some \(p\in P\) belongs to no longest chain. Every maximal chain containing \(p\) then has cardinality strictly smaller than \(h(P)\). Since there are finitely many such chains,
\[
\eta=
\min_{C\ni p}
\left(
1-\sqrt{\frac{|C|}{h(P)}}
\right)
\]
is positive. For any \(t\) with
\[
0<|t|\le\eta,
\]
the vector \(c=t e_p\) satisfies (3). Hence the incenter is nonunique. This proves the uniqueness criterion.

At the centered optimal ball, equality in a facet distance occurs precisely when
\[
\frac1{\sqrt{|C|}}
=
\frac1{\sqrt{h(P)}},
\]
namely when \(|C|=h(P)\). Each longest maximal chain has \(2^{h(P)}\) sign patterns, and distinct chain/sign pairs give distinct facet hyperplanes. This proves (4).

For the circumradius, every generating point of \(\mathcal C^{(e)}(P)\) is a signed characteristic vector of an antichain \(A\), so its squared Euclidean norm is
\[
|A|\le w(P).
\tag{11}
\]
By convexity, the entire polytope is contained in the centered ball of radius \(\sqrt{w(P)}\). A maximum antichain produces a generating point of norm exactly \(\sqrt{w(P)}\), proving that the centered radius cannot be smaller.

The global minimum enclosing radius also cannot be smaller: the polytope is centrally symmetric, so with every such outer point \(v\) it contains \(-v\), and any ball containing both has radius at least half their distance,
\[
\frac{\|v-(-v)\|}{2}
=
\|v\|
=
\sqrt{w(P)}.
\]
This proves (2).

The circumcenter is unique. If a radius-\(\sqrt{w(P)}\) ball centered at \(c\) contains both \(v\) and \(-v\), then
\[
\|v-c\|^2\le w(P),
\qquad
\|-v-c\|^2\le w(P).
\]
Adding gives
\[
2w(P)+2\|c\|^2\le2w(P),
\]
so \(c=0\).

Finally, if a convex combination of signed antichain vectors has norm \(\sqrt{w(P)}\), equality must hold in both
\[
\left\|\sum_j\lambda_jv_j\right\|
\le
\sum_j\lambda_j\|v_j\|
\le
\sqrt{w(P)}.
\]
Strict convexity of the Euclidean norm forces every participating vector to be the same signed characteristic vector of a maximum antichain. Thus the complete outer contact set is exactly the set stated in (5). Equation (6) follows immediately from (1) and (2).

## Verification
The proof is symbolic and holds for every finite poset. It uses two exact structural inputs from the literature: the signed-antichain vertex/generator description and the signed maximal-chain facet description.

The accompanying `verify.py` independently enumerates several finite posets of different shapes, including chains, antichains, pure and nonpure examples. It reconstructs all antichains and maximal chains from the order relation, verifies every signed-antichain generator against every signed maximal-chain inequality, checks the predicted inner and outer squared radii, and checks the incenter-uniqueness criterion by whether longest chains cover the ground set.

These computations are corroborative only; they are not used to prove the all-poset theorem.

## Relationship to prior work
Okada and Tsuchiya define the enriched chain polytope as the convex hull of signed antichain vectors and develop the enriched transfer map and unimodular triangulations. Their article has primary classification \(52B12\) and provides the middle-period literature anchor for this result.

Ohsugi and Tsuchiya give the complete facet representation used in (7): maximal chains, with every possible sign pattern, define all facets. That facet theorem makes the Euclidean inradius problem finite but does not state the optimization in (1), the complete incenter locus (3), or the contact count (4).

Kohl, Olsen, and Sanyal study the same objects under the name unconditional chain polytopes in a broader theory of unconditional reflexive polytopes. Their full text confirms that the vertices are signed characteristic vectors of inclusion-maximal antichains. It discusses triangulations, reflexivity, and volume-type questions, but no Euclidean radius theorem was located.

Targeted published-result and literature searches used both names of the object and searched for inradius, circumradius, height, width, longest-chain, maximum-antichain, and the characteristic square-root formulas. No statement was located that implies the combined radius formulas, complete incenter set, and equality/contact classifications above.

## Limitations
The result concerns the canonical enriched chain polytope in its standard coordinates. Euclidean radii change under nonorthogonal affine transformations.

The complete incenter description can have positive dimension for nonpure posets; no simpler combinatorial formula for that dimension is claimed here.

The originality assessment cannot exclude a differently phrased observation in older poset-polytope or unconditional-convexity literature. In particular, the numerical formulas are short consequences once both the full facet and signed-antichain descriptions are simultaneously in hand. The contribution claimed here is the exact metric classification, equality structure, and recovery of height and width, not a new facet theorem.

## References
1. Soichi Okada and Akiyoshi Tsuchiya, *Two Enriched Poset Polytopes*, arXiv:2003.12271, first public version 2020-03-27; Annals of Combinatorics 28 (2024), 257--282, DOI 10.1007/s00026-023-00679-7.
2. Hidefumi Ohsugi and Akiyoshi Tsuchiya, *Enriched Order Polytopes and Enriched Hibi Rings*, arXiv:1903.00909; European Journal of Mathematics 7 (2021), 48--68, DOI 10.1007/s40879-020-00403-2.
3. Florian Kohl, McCabe Olsen, and Raman Sanyal, *Unconditional Reflexive Polytopes*, Discrete & Computational Geometry 64 (2020), 427--452, DOI 10.1007/s00454-020-00199-8.
