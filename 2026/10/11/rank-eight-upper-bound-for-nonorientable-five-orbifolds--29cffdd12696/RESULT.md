# Rank-eight upper bound for nonorientable five-orbifolds
## Finding
Let \(X\) be a connected closed smooth five-orbifold whose stabilizers have order at most two, and let \(M=|X|\) be its coarse space. Then
\[
H^5(M;\mathbb Z)\cong \mathbb Z^{a}\oplus(\mathbb Z/2)^{b}
\]
for some \(a,b\ge 0\). Consequently the exponent \(e_5(M)\) of the \(2\)-primary torsion subgroup of \(H^5(M;\mathbb Z)\) is at most \(2\).

Becerra--Lupercio Proposition 8.7 then gives a complex regular bundle of rank
\[
4\gcd(4,e_5(M))\le 8.
\]
Thus every connected closed smooth five-orbifold with stabilizers of order at most two admits a complex regular bundle of rank at most \(8\).

Let \(B\) denote the sharp uniform rank bound among connected closed nonorientable smooth five-orbifolds having both stabilizer types \(1\) and \(\mu_2\). Then
\[
4\le B\le 8.
\]
The upper bound is the preceding theorem. For the lower bound, start with the source's connected oriented effective five-orbifold \(\mathcal O\), which has both stabilizer types and minimum regular rank \(4\), and take a connected sum at a free point with the ordinary nonorientable manifold \(\mathbb{RP}^4\times S^1\). Choosing the free ball disjoint from the source's mapping-torus suborbifold preserves that suborbifold, so rank \(2\) remains impossible. The source's rank-\(4\) bundle is trivial on the removed ball and glues to the trivial rank-\(4\) bundle on the punctured manifold, so rank \(4\) is attained on the connected sum.

## Assumptions and scope
"Closed" means compact and without an imposed manifold boundary, in the smooth-orbifold setting used by Becerra--Lupercio. Stabilizers are either trivial or \(\mu_2\). The top-cohomology statement concerns the ordinary integral cohomology of the coarse space.

The proof allows codimension-one reflection strata. Such strata create one-sided codimension-one faces in a good coarse triangulation; they do not invalidate the argument and in fact can only kill top cohomology generators.

The conclusion is an upper bound. It does not decide whether a nonorientable smooth five-orbifold with both stabilizer types can require rank \(8\).

## Proof
Becerra--Lupercio Lemma 7.2 gives a finite triangulation \(Z\) of \(M\), subordinate to the isotropy stratification, whose lifts triangulate the local orbifold charts. In particular \(Z\) is pure of dimension \(5\).

Write \(C^5(Z;\mathbb Z)\) with one generator \(x_\sigma\) for each \(5\)-simplex \(\sigma\). Since \(Z\) has no \(6\)-simplices,
\[
H^5(M;\mathbb Z)=C^5(Z;\mathbb Z)/\operatorname{im}\delta^4.
\]

Consider a \(4\)-simplex \(\tau\). Its interior lies in a single isotropy stratum. In a local effective chart there are only two possibilities relevant in codimension one.

If the local coarse space is two-sided across \(\tau\), then \(\tau\) is incident to exactly two \(5\)-simplices, say \(\sigma\) and \(\sigma'\). After choosing orientations,
\[
\delta(\tau^*)=\pm x_\sigma\pm x_{\sigma'}.
\]
Thus the corresponding relation identifies the two top generators up to sign.

If the local coarse space is one-sided across \(\tau\), then the effective \(\mu_2\)-action is reflection in the tangent hyperplane of the stratum. The coarse local model is a half-space, \(\tau\) is incident to exactly one \(5\)-simplex \(\sigma\), and
\[
\delta(\tau^*)=\pm x_\sigma.
\]
Thus that top generator is killed.

Form a graph whose vertices are the \(5\)-simplices and whose edges are the two-term relations; mark a vertex whenever a one-term relation occurs in its component. On each connected component, the edge relations express every generator as either \(x\) or \(-x\) for one chosen generator \(x\).

If the component has a marked vertex, then \(x=0\), so that component contributes \(0\). If it has no marked vertex and all sign products around cycles are \(+1\), it contributes \(\mathbb Z\). If some cycle has sign product \(-1\), the propagated relation gives \(x=-x\), hence \(2x=0\). There is no stronger relation: reduction modulo \(2\) sends every generator in the component to \(1\) and annihilates every two-term relation. Hence the contribution is exactly \(\mathbb Z/2\).

Summing over graph components yields
\[
H^5(M;\mathbb Z)\cong \mathbb Z^{a}\oplus(\mathbb Z/2)^{b}.
\]
Therefore \(e_5(M)\le 2\). Proposition 8.7 of the source supplies a regular bundle of rank
\[
4\gcd(4,e_5(M))\le 8.
\]
The same smoothing step used in the source's proof of Theorem E preserves rank and stabilizer representations, so the bundle is smooth.

For the lower side of the nonorientable sharp bound, Becerra--Lupercio Proposition 9.3 constructs a connected oriented effective smooth five-orbifold \(\mathcal O\) with both stabilizer types and minimum regular rank \(4\). Their proof exhibits a mapping-torus suborbifold \(\mathcal T\subset\mathcal O\) on which rank \(2\) is impossible.

Choose a free point of \(\mathcal O\) outside \(\mathcal T\), remove a small ordinary \(5\)-ball, and form the connected sum with \(\mathbb{RP}^4\times S^1\) at an ordinary ball. The result is a closed nonorientable smooth five-orbifold with the same nonfree locus as \(\mathcal O\), hence with both stabilizer types. The suborbifold \(\mathcal T\) remains embedded, so a rank-\(2\) regular bundle would restrict to an impossible rank-\(2\) regular bundle on \(\mathcal T\).

The source's rank-\(4\) regular bundle on \(\mathcal O\) is trivial over the removed ball. Glue its boundary trivialization to the trivial rank-\(4\) bundle on the punctured \(\mathbb{RP}^4\times S^1\). This gives a rank-\(4\) regular bundle on the connected sum. Hence this nonorientable example has minimum regular rank exactly \(4\).

Finally, Corollary 8.5 of the source shows that, in dimension at most five with nonempty \(\mu_2\)-isotropy, the only possible minimum regular ranks are \(2,4,8,16\). The new upper bound removes \(16\) from the smooth five-dimensional case, while the connected-sum example shows that the sharp nonorientable both-stabilizer bound cannot be below \(4\). Thus \(B\in\{4,8\}\).

## Verification
The proof is symbolic and uses no finite experiment as a substitute for a universal argument.

The critical source statements were checked in the open full text: Lemma 7.2 gives the finite good triangulation and complex-of-groups presentation; Proposition 8.7 gives the rank \(4\gcd(4,e_5(M))\); Corollary 8.5 restricts possible minimum ranks to \(2,4,8,16\); Proposition 9.3 gives the smooth rank-\(4\) example with both stabilizer types and its mapping-torus rank-\(2\) obstruction; and Question 10.2 explicitly leaves the nonorientable sharp bound open.

The only new topological input is the signed-incidence calculation of \(H^5\). Every codimension-one simplex in the coarse good triangulation has one or two top-dimensional cofaces. Therefore every row relation in the top coboundary has one or two unit coefficients. The componentwise signed-graph reduction above is exact and shows that top-cohomology torsion can only have order \(2\).

The connected-sum lower-bound construction occurs entirely at free points, where the orbifold is an ordinary manifold. Hence ordinary smooth connected sum applies, the stabilizer data away from the chosen ball are unchanged, and the rank-\(4\) bundle glues across a trivialized sphere boundary.

## Relationship to prior work
Becerra--Lupercio prove the sharp rank \(16\) bound for arbitrary five-dimensional orbispaces with stabilizers of order at most two and the sharp rank \(4\) bound for closed oriented smooth five-orbifolds. Their Proposition 8.7 isolates the coarse top-cohomology exponent \(e_5(M)\) as the remaining obstruction in dimension five. They then ask explicitly for the sharp bound in the closed nonorientable smooth category with both stabilizer types.

The source does not state that coarse top cohomology has only elementary \(2\)-torsion, does not deduce a rank-\(8\) smooth upper bound, and does not reduce Question 10.2 to the alternatives \(4\) and \(8\). The new step is the signed-incidence analysis of the source's good triangulation, including possible one-sided reflection faces.

Targeted exact, alias, and implication searches found no statement giving this rank-\(8\) upper bound or the top-cohomology exponent-\(2\) lemma. Nearby results about orbifold bundles, weighted-projective orbifolds, and isolated \(\mathbb Z/2\)-torsion calculations concern different invariants and do not imply the claim.

## Limitations
The result does not determine whether the sharp nonorientable both-stabilizer bound is \(4\) or \(8\). In particular, it gives no smooth example requiring rank \(8\).

The top-cohomology lemma is specific to the highest cohomological degree of a coarse smooth-orbifold triangulation; it does not assert that lower-degree torsion is elementary \(2\)-torsion.

The regular-bundle conclusion uses the stabilizer restriction to orders at most two and the dimension-five obstruction theorem of Becerra--Lupercio.

## References
1. Enrique Becerra and Ernesto Lupercio, *Regular bundles on orbifolds II: ranks and obstructions*, arXiv:2610.02555v1, 2026.
2. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, for standard simplicial cohomology conventions.
