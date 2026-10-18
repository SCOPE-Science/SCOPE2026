# Coordinate and determinantal strata of the first codimension-two restricted nullcone

## Finding

Let \(p\ge3\) be a prime and set \(n=p+2\). The restricted Lie algebra \(\mathfrak u_n(k)\) of strictly upper-triangular matrices over an algebraically closed field \(k\) of characteristic \(p\) has restricted power \(X^{[p]}=X^p\). Write \(a_i=X_{i,i+1}\) for \(1\le i\le p+1\) and \(b_i=X_{i,i+2}\) for \(1\le i\le p\). All other strictly upper-triangular entries are free in the locus below.

**Theorem.** The reduced algebraic set
\[
\mathcal N_p=\{X\in\mathfrak u_n(k): X^p=0\}_{\mathrm{red}}
\]
has the following *complete* list of irreducible components:

\[
P_{ij}=V(a_i,a_j),\qquad 1\le i<j\le p+1,\quad j-i\ge2,
\]
\[
Q_k=V\!\left(a_k,\ a_{k+1}b_{k-1}+a_{k-1}b_k\right),
\qquad 2\le k\le p.
\]

Each \(P_{ij}\) is a linear coordinate subspace; each \(Q_k\) is a product of a rank-one \(2\times2\) determinantal quadratic cone with an affine space, after a sign change in one coordinate. All components are geometrically irreducible of codimension two in \(\mathfrak u_n\). Their total number is
\[
\frac{(p-1)(p+2)}2.
\]

Over every finite field \(\mathbb F_q\) of cardinality \(q=p^f\), writing \(N=\binom{p+2}{2}\), the exact point count is
\[
\boxed{\ \#\{X\in\mathfrak u_n(\mathbb F_q):X^p=0\}
=q^{N-p-2}\left(q^{p+2}-(q-1)^p(q^2+pq+1)\right).\ }
\]

The first deviation from the automatic condition \(X^p=0\) arises at size \(p+1\), where one top-right monomial gives a union of coordinate hyperplanes. At size \(p+2\), the restricted nullcone first has codimension two, with nonlinear determinantal components.

## Assumptions and scope

The prime satisfies \(p\ge3\). The geometric assertion holds after algebraic closure for every field of characteristic \(p\); the finite-field count holds for every power \(q=p^f\) with \(f\ge1\). The ambient Lie algebra is the nilradical of the standard Borel subalgebra of \(\mathfrak{gl}_{p+2}\), with the standard matrix restricted-power operation. The components refer to the *reduced* zero set of the entries of \(X^p\), not to the potentially nonreduced affine scheme cut out by those equations. Matrix entries at distance three or more above the diagonal are unconstrained.

## Proof

**Step 1: all equations.** A nonzero contribution to the \((i,j)\) entry of \(X^p\) is a directed increasing path of length \(p\) from \(i\) to \(j\). Since \(j-i\le p+1\), every step has length one except possibly one step of length two. Consequently, the only potentially nonzero entries are
\[
(X^p)_{1,p+1}=\prod_{i=1}^{p}a_i,\qquad
(X^p)_{2,p+2}=\prod_{i=2}^{p+1}a_i,
\]
\[
(X^p)_{1,p+2}=
\sum_{j=1}^{p} b_j\prod_{\substack{1\le i\le p+1\\i\notin\{j,j+1\}}}a_i.
\tag{1}
\]
No coefficient cancellation or characteristic-specific simplification is used in these path formulas.

**Step 2: the union is exact.** The simultaneous vanishing of the first two products forces either a zero at one of the interior positions \(2,\ldots,p\), or zeros at both endpoints. If at least two first-superdiagonal positions vanish and some two of them are nonadjacent, every summand in equation (1) contains a zero. This gives some component \(P_{ij}\). If exactly one position vanishes, it must be an interior index \(k\). Then equation (1), after factoring the nonzero remaining \(a\)-entries, becomes exactly
\[
a_{k+1}b_{k-1}+a_{k-1}b_k=0,
\]
so the matrix lies on \(Q_k\). The only remaining case consists of exactly two adjacent zero positions \(i,i+1\). Equation (1) then has precisely one potentially nonzero summand, proportional to \(b_i\); its vanishing puts the point on \(Q_i\) for \(2\le i\le p-1\), on \(Q_2\) when \(i=1\), or on \(Q_p\) when \(i=p\). Conversely, each displayed component makes all three expressions in (1) vanish. The union therefore equals the full geometric zero set over every field extension.

**Step 3: irreducibility and maximality.** Each \(P_{ij}\) is a linear subspace of codimension two. In the coordinate hyperplane \(a_k=0\), the remaining equation for \(Q_k\) is the determinant of a generic \(2\times2\) matrix after an invertible linear rescaling of coordinates; this polynomial is irreducible over every field. Thus \(Q_k\) is also geometrically irreducible of codimension two. All listed sets are distinct, because each has a different prime defining ideal; since all have the same dimension, none contains another. Their union is the entire reduced zero set, proving the component list and the count \(p(p-1)/2+(p-1)=(p-1)(p+2)/2\).

**Step 4: finite-field enumeration.** Let \(A(q)\) count choices of \((a_1,\ldots,a_{p+1})\in\mathbb F_q^{p+1}\) for which both products in Step 1 vanish. Inclusion-exclusion gives
\[
A(q)=q^{p+1}-2q(q-1)^p+(q-1)^{p+1}.
\]
For almost every such choice, the third equation vanishes identically in the \(p\) variables \(b_i\), leaving \(q^p\) choices. Precisely two disjoint types impose one nonzero linear equation: (i) a *unique* interior zero, giving \((p-1)(q-1)^p\) choices of \(a\); (ii) *exactly two adjacent* zeros, giving \(p(q-1)^{p-1}\) choices. For either exceptional type there are exactly \(q^{p-1}\) choices of \(b\). Thus the number of admissible \((a,b)\) equals
\[
q^p A(q)-(q^p-q^{p-1})\left((p-1)(q-1)^p+p(q-1)^{p-1}\right)
=q^{p-1}\left(q^{p+2}-(q-1)^p(q^2+pq+1)\right).
\]
The other \(N-(2p+1)\) entries contribute a factor \(q^{N-2p-1}\), yielding the asserted formula.

## Verification

Run the standalone companion script `verify_pnull.py` with Python 3. It performs independent matrix-power calculations and component-membership tests, exhaustively over all choices of the first two superdiagonals for characteristic two with field sizes two and four and for characteristic three over the prime field. It also performs fixed-seed randomized full-matrix checks in characteristics two, three and five, allowing arbitrary higher superdiagonals. The exhaustive point totals for \((p,q)=(2,2),(2,4),(3,3)\) are respectively \(28,496,22113\). The first two are **boundary checks outside the theorem's stated prime range**, not part of its originality claim. The script returns `VERIFY_OK`. These finite checks corroborate but do not replace the proof for arbitrary primes and extensions.

## Relationship to prior work

Classical orbital-variety theory already implies, over characteristic zero, the component count attached to the nilpotent partition \((p,2)\) by standard Young tableaux; that numerical count is **not claimed as independently new**. Melnikov studies upper-triangular matrices with square zero over \(\mathbb C\), including the characteristic-zero analogue of the size-four boundary. Boos and Reineke describe orbits of square-zero matrices, and Boos treats parabolic conjugation on varieties of \(x\)-nilpotent matrices over \(\mathbb C\). Those results provide relevant geometric context and broader abstract orbit machinery, but the inspected passages do not state the explicit coordinate/determinantal decomposition in the restricted characteristic-\(p\) family of size \(p+2\), nor its finite-field point-count polynomial. The contribution claimed here is the combination of those explicit reduced equations, the decomposition valid in positive characteristic for all primes \(p\ge3\), and the uniform finite-field point count; the classical tableau count serves as a consistency check rather than a priority claim.

## Limitations

The equations and decomposition are set-theoretic over algebraic closures; no scheme-theoretic radicality or reducedness of the original ideal is asserted. No formula for dimensions larger than \(p+2\), conjugacy orbit counts, or cohomological invariants is claimed. The finite-field formula uses the exact hypothesis \(q=p^f\). The more general classical orbital-variety framework provides partial a priori information; an unlocated positive-characteristic specialization giving all equations and point counts remains a literature-coverage risk.

## References

1. Anna Melnikov, *Description of B-orbit closures of order 2 in upper-triangular matrices*, first available 15 December 2003, arXiv:math/0312290, https://arxiv.org/html/math/0312290v2 (Introduction and §§2–4).
2. Magdalena Boos and Markus Reineke, *B-orbits of 2-nilpotent matrices and generalizations*, first available 12 April 2010, arXiv:1004.1996, https://arxiv.org/html/1004.1996v1 (§§2, 3, 5).
3. Magdalena Boos, *Conjugation on varieties of nilpotent matrices*, first available 23 May 2012, arXiv:1205.5197, https://arxiv.org/html/1205.5197v2 (§§4–6).
