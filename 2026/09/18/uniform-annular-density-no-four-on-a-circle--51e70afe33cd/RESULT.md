# Uniform thick-annulus density for extensible no-four-on-a-circle sets

## Main result

Write \([n]=\{1,\ldots,n\}\). A *bad quadruple* is a set of four lattice points that is collinear or concyclic.

**Theorem.** For every fixed \(\eta\in(0,1]\), there are constants \(c_\eta>0\) and \(N_\eta\) and a set \(S\subset\mathbb N^2\) with no bad quadruple such that, for every integer \(n\ge N_\eta\) and every integer \(m\) with
\[
\eta n\le m\le n,
\]
one has
\[
\boxed{\left|S\cap\bigl([n+m]^2\setminus[n]^2\bigr)\right|\ge c_\eta m.}
\]
In particular every sufficiently large doubling square annulus satisfies
\[
\left|S\cap\bigl([2n]^2\setminus[n]^2\bigr)\right|\ge c_\eta n.
\]

This strengthens the prefix-density conclusion \(|S\cap[n]^2|=\Omega(n)\) of Ghosal--Goenka by forcing linear mass in every origin-centred square annulus whose thickness is a fixed positive fraction of its inner radius. Prefix density by itself does not imply such annular density.

## Input from the extensible construction

Ghosal and Goenka independently retain each \(x\in\mathbb N^2\) with probability
\[
p_x=\frac{\alpha}{\|x\|_\infty}
\]
to obtain a random set \(Q\), then delete the point of largest \(\ell_\infty\)-norm from every bad quadruple, with deterministic tie breaking.

Their Lemma 2.2 provides a universal constant \(C\ge1\) such that, on the dyadic box
\[
B_T=[2^T]^2,
\]
the three classes of bad quadruples satisfy bounds that allow the following simultaneous event with positive probability for all sufficiently large \(T\):
\[
Y_T^{\rm lin}\le2C\alpha^4 2^T,\qquad
Y_T^{\rm sym}\le2C\alpha^4 2^T,\qquad
Y_T^{\rm asym}\le2C\alpha^4 2^T.
\]
Their proof obtains this from variance bounds for the collinear and symmetric classes and an expectation bound for the asymmetric class. We use exactly these published estimates; no new estimate for bad quadruples is required.

Choose \(\alpha>0\) so small that
\[
\alpha^3\le\frac{\eta}{192C}.
\]
This is stronger than the smallness condition needed in the source construction.

## Uniform occupancy of thick annuli before deletion

For integers \(n,m\ge1\), put
\[
A_{n,m}=[n+m]^2\setminus[n]^2,
\qquad Z_{n,m}=|Q\cap A_{n,m}|.
\]
There are exactly \(2r-1\) points \(x\in\mathbb N^2\) with \(\|x\|_\infty=r\). Hence
\[
\mu_{n,m}:=\mathbb E Z_{n,m}
=\sum_{r=n+1}^{n+m}(2r-1)\frac{\alpha}{r}
=\alpha\sum_{r=n+1}^{n+m}\left(2-\frac1r\right)
\ge \alpha m.
\]
Since \(Z_{n,m}\) is a sum of independent Bernoulli variables, the standard multiplicative Chernoff bound gives
\[
\mathbb P\left(Z_{n,m}<\frac{\alpha m}{2}\right)
\le
\mathbb P\left(Z_{n,m}<\frac{\mu_{n,m}}2\right)
\le e^{-\mu_{n,m}/8}
\le e^{-\alpha m/8}.
\]
For fixed \(\eta>0\),
\[
\sum_{n=1}^\infty\;
\sum_{\substack{m\in\mathbb N\\ \eta n\le m\le n}}
 e^{-\alpha m/8}
\le
\sum_{n=1}^\infty n e^{-\alpha\eta n/8}<\infty.
\]
By the first Borel--Cantelli lemma, with probability one there is \(N_0\) such that
\[
Z_{n,m}\ge\frac{\alpha m}{2}
\]
for every \(n\ge N_0\) and every integer \(m\in[\eta n,n]\).

The Ghosal--Goenka dyadic good event has positive probability, so it can be intersected with this probability-one event. Fix a realization \(Q\) in that intersection, and let \(S\) be obtained by their deletion rule.

## Charging the deleted points

Fix sufficiently large \(n\) and \(m\in[\eta n,n]\), and set
\[
T=\left\lceil\log_2(n+m)\right\rceil.
\]
Every point deleted from \(A_{n,m}\) was selected as the maximal-norm point of at least one bad quadruple contained in \([n+m]^2\subseteq B_T\). Assign to each deleted point one such witnessing quadruple. Because a bad quadruple selects only one point for deletion, this assignment is injective. Consequently the number \(D_{n,m}\) of deleted points in \(A_{n,m}\) is at most the total number of bad quadruples of \(Q\) in \(B_T\):
\[
D_{n,m}
\le Y_T^{\rm lin}+Y_T^{\rm sym}+Y_T^{\rm asym}
\le6C\alpha^4 2^T.
\]
Since \(m\le n\),
\[
2^T<2(n+m)\le4n\le\frac{4m}{\eta},
\]
and therefore
\[
D_{n,m}<\frac{24C}{\eta}\alpha^4m
\le\frac{\alpha m}{8},
\]
where the last inequality follows from \(\alpha^3\le\eta/(192C)\).
Thus
\[
|S\cap A_{n,m}|
\ge Z_{n,m}-D_{n,m}
\ge\left(\frac12-\frac18\right)\alpha m
=\frac{3\alpha}{8}m.
\]
The theorem follows, for example with
\[
c_\eta=\frac{3\alpha}{8}.
\]
By construction every bad quadruple of \(Q\) loses a point, so \(S\) contains no four collinear or concyclic points.

## Significance

The source theorem guarantees the correct linear order of growth in every prefix square \([n]^2\). The result above adds a local-in-scale regularity statement: after the same type of deletion, linear mass survives simultaneously in every square shell of relative thickness at least \(\eta\). Thus the extensible construction can be chosen so that its density is not maintained merely by sporadic bursts at separated radii.

The argument isolates a reusable principle. A weighted sampling law with expected shell mass proportional to shell thickness, together with a dyadic \(O(\alpha^4 R)\) bound on deletions up to radius \(R\), yields uniform density on every window of thickness \(\Omega(R)\) after taking \(\alpha\) sufficiently small relative to that thickness ratio.

## Relation to prior work and originality check

Ghosal and Goenka, *The extensible no-four-on-a-circle problem* (arXiv:2609.20447, submitted 17 September 2026), prove that some bad-quadruple-free \(S\subset\mathbb Z^2\) satisfies
\[
|S\cap[n]^2|=\Omega(n).
\]
Their proof introduces dyadic shells to estimate the random construction, but the stated result and its proof conclude a prefix lower bound, not a simultaneous lower bound in every thick square annulus.

The earlier paper of Ghosal, Goenka and Keevash, *On Subsets of Lattice Cubes Avoiding Affine and Spherical Degeneracies* (Discrete & Computational Geometry, 2026), treats finite boxes and establishes linear-size finite no-four-on-a-circle configurations; it does not provide the annular extensible conclusion above.

Targeted searches for combinations of no-four-on-a-circle / extensible constructions with annular density, square annuli, dyadic-shell density, and local density did not reveal a prior statement equivalent to the theorem above. The motivating preprint is extremely recent, so unindexed or contemporaneous parallel work remains a material residual originality risk.

## Limitations

- The annuli are origin-centred square annuli in the \(\ell_\infty\) geometry inherited from \([n]^2\). No translation-uniform lower density is proved.
- The parameter \(\eta>0\) is fixed in advance, and the constructed set and constant may depend on \(\eta\). The theorem does not control arbitrarily thin relative annuli for one fixed construction.
- The constant is not numerically optimized because it depends on the universal constant \(C\) implicit in the source estimates.
- The result is existential and probabilistic; it does not give an efficient deterministic construction.

## References

1. Anubhab Ghosal and Ritesh Goenka, *The extensible no-four-on-a-circle problem*, arXiv:2609.20447, 2026. https://arxiv.org/abs/2609.20447
2. Anubhab Ghosal, Ritesh Goenka, and Peter Keevash, *On Subsets of Lattice Cubes Avoiding Affine and Spherical Degeneracies*, Discrete & Computational Geometry, 2026. https://doi.org/10.1007/s00454-026-00853-7
