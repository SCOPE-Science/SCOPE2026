# Euler characteristics of the subdiscriminant filtration of projective matrix space
## Finding
For integers \(n\ge2\) and \(1\le r\le n\), let
\[
X_{n,r}
=
\left\{
[A]\in\mathbb P\operatorname{Mat}_n(\mathbb C):
A\text{ has at most }r\text{ distinct eigenvalues}
\right\},
\]
and put
\[
X_{n,0}=\varnothing.
\]
Let
\[
{n\brace b}
\]
denote the Stirling number of the second kind, and define
\[
q_1=1,
\qquad
q_b=(-1)^{b-2}(b-2)!
\quad(b\ge2).
\]
Then
\[
\boxed{
\chi_{\mathrm{top}}(X_{n,r})
=
n(n-1)+\sum_{b=1}^{r}{n\brace b}q_b.
}
\]

If
\[
E_{n,r}=X_{n,r}\setminus X_{n,r-1}
\]
is the locally closed projective-matrix stratum with exactly \(r\) distinct eigenvalues, then
\[
\boxed{
\chi_c(E_{n,1})=n(n-1)+1,
}
\]
and, for \(2\le r\le n\),
\[
\boxed{
\chi_c(E_{n,r})
=
{n\brace r}(-1)^{r-2}(r-2)!.
}
\]

For \(r=n\), the formula recovers
\[
\chi_{\mathrm{top}}\!\left(\mathbb P^{n^2-1}\right)=n^2
\]
and therefore yields the identity
\[
\sum_{b=1}^{n}{n\brace b}q_b=n.
\]

## Assumptions and scope
The base field is \(\mathbb C\). Distinct eigenvalues are counted without multiplicity. The condition of having at most \(r\) distinct eigenvalues is Zariski closed for \(r<n\); in the subdiscriminant notation of the archival source it is the variety \(\mathcal L_k\) with
\[
k=n-r-1.
\]
For \(r=n\), the variety is the full projective matrix space.

The theorem concerns ordinary topological Euler characteristic of the closed projective levels and compactly supported Euler characteristic of their exact-eigenvalue differences. It does not assert a formula for individual Betti numbers or intersection cohomology.

## Proof
Choose diagonal conjugation weights
\[
w_i=2^{i-1}
\qquad(1\le i\le n).
\]
Conjugation by
\[
\operatorname{diag}(t^{w_1},\ldots,t^{w_n})
\]
defines an algebraic \(\mathbb C^*\)-action preserving the number of distinct eigenvalues, hence preserving every \(X_{n,r}\).

The weight on the matrix coordinate \(E_{ij}\) is
\[
w_i-w_j.
\]
All ordered differences with \(i\ne j\) are nonzero and pairwise distinct. Indeed, for a positive difference the \(2\)-adic valuation determines the smaller exponent and the remaining odd factor determines the gap between exponents; negative differences reduce to the positive case after changing sign.

Consequently the fixed locus in the ambient projective matrix space is the disjoint union of the diagonal projective space
\[
\mathbb P^{n-1}
\]
and the \(n(n-1)\) isolated off-diagonal matrix-unit points
\[
[E_{ij}],\qquad i\ne j.
\]
Every off-diagonal matrix unit is nilpotent, hence has the single eigenvalue \(0\). Thus all \(n(n-1)\) isolated points belong to every \(X_{n,r}\) with \(r\ge1\).

It remains to count the Euler characteristic of the diagonal fixed part. A diagonal projective point has exactly as many distinct eigenvalues as its diagonal coordinates have distinct values. Fix a set partition \(\pi\) of \(\{1,\ldots,n\}\) into \(b\) blocks and impose that two coordinates are equal exactly when their indices lie in the same block. After labeling the blocks, the resulting projective stratum is
\[
\operatorname{Conf}_b(\mathbb C)/\mathbb C^*,
\]
where \(\operatorname{Conf}_b(\mathbb C)\) is the ordered configuration space of \(b\) distinct complex numbers and \(\mathbb C^*\) acts by simultaneous scaling.

For \(b=1\), this quotient is a point, so its Euler characteristic is \(q_1=1\). For \(b\ge2\), write the distinct block values as
\[
(\lambda_1,\ldots,\lambda_b).
\]
Since \(\lambda_2-\lambda_1\ne0\), every scaling orbit has a unique representative after normalizing this difference to \(1\). The quotient is therefore algebraically isomorphic to
\[
\mathbb C\times
\operatorname{Conf}_{b-2}\!\left(\mathbb C\setminus\{0,1\}\right).
\]

Forgetting the last point gives the standard locally trivial configuration-space fibration. Its successive fibers are copies of \(\mathbb C\) with respectively \(2,3,\ldots,b-1\) points removed. Since
\[
\chi_c\!\left(\mathbb C\setminus\{m\text{ points}\}\right)=1-m,
\]
multiplicativity gives
\[
\chi_c\!\left(
\operatorname{Conf}_{b-2}(\mathbb C\setminus\{0,1\})
\right)
=
(-1)^{b-2}(b-2)!.
\]
Hence a fixed equality partition with \(b\) blocks contributes exactly \(q_b\). There are
\[
{n\brace b}
\]
such partitions.

Thus
\[
\chi_c\!\left(X_{n,r}^{\mathbb C^*}\right)
=
n(n-1)+\sum_{b=1}^{r}{n\brace b}q_b.
\]
For a complex algebraic variety with an algebraic \(\mathbb C^*\)-action, compactly supported Euler characteristic equals that of the fixed locus. Since \(X_{n,r}\) is projective,
\[
\chi_{\mathrm{top}}(X_{n,r})
=
\chi_c(X_{n,r})
=
\chi_c\!\left(X_{n,r}^{\mathbb C^*}\right),
\]
which proves the closed-level formula.

Finally, additivity of \(\chi_c\) for
\[
X_{n,r}=X_{n,r-1}\sqcup E_{n,r}
\]
gives the exact-layer formula immediately.

## Verification
The bundled checker computes Stirling numbers independently by their recurrence and verifies the closed-level and layer identities for
\[
2\le n\le30.
\]
It separately verifies pairwise separation of every ordered off-diagonal weight difference for the powers-of-two cocharacter through
\[
n=30.
\]

As an independent finite-model check of the diagonal stratification, for small prime fields it exhaustively enumerates nonzero diagonal vectors modulo scalar multiplication, groups them by the number of distinct coordinate values, and verifies the finite-field analogue
\[
\#\left(\operatorname{Conf}_b(\mathbb F_p)/\mathbb F_p^*\right)
=
\frac{p(p-1)\cdots(p-b+1)}{p-1}
\quad(b\ge2).
\]
Evaluating the corresponding arrangement counting polynomial at \(p=1\) reproduces \(q_b\). This is a regression check, not a substitute for the complex-algebraic proof above.

The checker also verifies the small values
\[
\chi_{\mathrm{top}}(X_{2,1})=3,
\qquad
\chi_{\mathrm{top}}(X_{3,1})=7,
\qquad
\chi_{\mathrm{top}}(X_{3,2})=10,
\qquad
\chi_{\mathrm{top}}(X_{4,2})=20.
\]

## Relationship to prior work
Domokos defines the full complex matrix varieties \(\mathcal L_k\) of matrices with a bounded number of distinct eigenvalues and proves invariant-theoretic results for their vanishing ideals and subdiscriminants. The same paper identifies their diagonal slices with the coordinate-equality subspace arrangements \(\mathcal D_k\). Its inspected full text does not state an Euler-characteristic or Poincaré-polynomial formula.

Vassiliev studies a filtration by the number of eigenvalues for Hermitian operators and obtains substantially finer cohomological information for that real-Hermitian problem. That parameter space is different: Hermitian operators form a real vector space and their topology is controlled by unitary spectral decompositions. No implication from those results to the projectivized variety of all complex matrices was located.

Targeted searches using “subdiscriminant variety,” “matrices with at most distinct eigenvalues,” “matrix discriminant complement,” “Euler characteristic,” “Poincaré,” and the Stirling-number form of the answer did not locate the formula above. The closest literature found concerns real symmetric or Hermitian matrices, equations and degrees of discriminant loci, or matrix problems unrelated to this projective complex variety.

A previously studied eigenvalue-coincidence filtration comparing a matrix with its northwest cutoff is a different condition: it constrains overlap between two characteristic polynomials rather than the number of roots of one characteristic polynomial. Neither filtration contains the other in a way that implies the theorem here.

## Limitations
Euler characteristic is coarse: the formulas do not determine irreducible components, singularities, ordinary Betti numbers, intersection cohomology, or motives.

The proof uses complex-algebraic torus localization. No assertion is made for real loci, where the topology of repeated-eigenvalue sets is different.

The argument is short once the diagonal equality-partition stratification is combined with localization, so an older unindexed or folklore observation remains a residual originality risk. The related Hermitian literature also shows that much finer topology can exist even when Euler characteristic collapses to a simple expression.

## References
M. Domokos, *Invariant theoretic characterization of subdiscriminants of matrices*, arXiv:1206.2358, first submitted 11 June 2012; *Linear and Multilinear Algebra* 61 (2013), 663--674, DOI 10.1080/03081087.2012.762714.

V. A. Vassiliev, *Spaces of Hermitian operators with simple spectra and their finite-order cohomology*, *Moscow Mathematical Journal* 3 (2003), 1145--1165, DOI 10.17323/1609-4514-2003-3-3-1145-1165.
