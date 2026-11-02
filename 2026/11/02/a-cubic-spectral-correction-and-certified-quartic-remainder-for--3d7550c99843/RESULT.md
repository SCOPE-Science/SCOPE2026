# A cubic spectral correction and certified quartic remainder for diffuse spherical hard-edge coefficients

## Finding

Let \(n\ge2\), let \(H\) be any real positive semidefinite \(n\times n\) matrix with \(\operatorname{tr}H=1\), and let \(U\) be Haar-uniform on the unit sphere in \(\mathbb R^n\). Define
\[
\vartheta_n(H)=\mathbb E\sqrt{nU^{\mathsf T}HU},\qquad
A_j(H)=\operatorname{tr}\bigl(H-I_n/n\bigr)^j\quad(j=2,3,4).
\]
Set
\[
Q_n(H)=\frac{n}{4(n+2)}A_2(H)-\frac{n^2}{2(n+2)(n+4)}A_3(H).
\]
**Theorem (finite-dimensional spectral expansion with signed remainder).** For every such \(n,H\), including singular matrices,
\[
0\le 1-\vartheta_n(H)-Q_n(H)
\le\frac{5n^3}{16(n+2)(n+4)(n+6)}
\bigl(12A_2(H)^2+48A_4(H)\bigr).
\tag{1}
\]
The left-hand remainder has the exact nonnegative representation
\[
1-\vartheta_n(H)-Q_n(H)
=\mathbb E\left[\frac{(X-1)^4\bigl(X+4\sqrt X+5\bigr)}{16(1+\sqrt X)^4}\right],
\quad X=nU^{\mathsf T}HU.
\tag{2}
\]
Consequently, along **every** sequence of trace-one positive semidefinite matrices \(H_n\) with \(A_2(H_n)>0\) and \(\operatorname{tr}(H_n^2)\to0\),
\[
\frac{1-\vartheta_n(H_n)}{\frac{n}{4(n+2)}A_2(H_n)}\longrightarrow1.
\tag{3}
\]
For \(H_n=I_n/n\) the deficit vanishes identically. The coefficient \(1/4\) in (3), relative to the centered spectral square sum, is sharp even for strictly positive definite two-band inverse profiles.

There is genuine cubic spectral discrimination beyond purity: when \(n\ge3\), the positive definite eigenvalue lists
\[
\bigl(1/n+2\delta,1/n-\delta,1/n-\delta,1/n,\ldots,1/n\bigr)
\quad\text{and}\quad
\bigl(1/n-2\delta,1/n+\delta,1/n+\delta,1/n,\ldots,1/n\bigr)
\]
for \(0<\delta<1/(2n)\) have equal \(A_2=6\delta^2\), but their deficits differ by
\[
-\frac{6n^2}{(n+2)(n+4)}\delta^3+O_n(\delta^4)
\]
(first profile minus second). Thus equal spectral purity does not determine the first correction beyond the quadratic order.

## Assumptions and scope

The only assumptions for (1)–(2) are \(n\ge2\), positive semidefiniteness, and unit trace. No invertibility, random-matrix entry law, rank bound, spectral gap, or dimension-asymptotic hypothesis is used. The precise limiting statement (3) requires the effective spectral rank \(1/\operatorname{tr}(H_n^2)\) to diverge, and excludes exactly isotropic terms from the displayed ratio because its denominator is zero. All terms in (1) are deterministic functions of the eigenvalues. The relationship to random matrix hard-edge probabilities uses the already-established theorem cited below, rather than a new universality theorem.

## Proof

**Step 1: exact central moments.** Diagonalize \(H\), write its eigenvalues as \(\lambda_i\), and put \(a_i=\lambda_i-1/n\), so \(\sum_i a_i=0\) and \(A_j=\sum_i a_i^j\). With \(Y=X-1\),
\[
Y=n\sum_{i=1}^n a_iU_i^2.
\]
For an independent standard Gaussian vector \(G\), the polar decomposition \(G=RU\) has independent \(R\) and \(U\). Gaussian moment-generating functions give, using \(\sum_i a_i=0\),
\[
\mathbb E\Big(\sum_i a_iG_i^2\Big)^2=2A_2,\quad
\mathbb E\Big(\sum_i a_iG_i^2\Big)^3=8A_3,\quad
\mathbb E\Big(\sum_i a_iG_i^2\Big)^4=12A_2^2+48A_4.
\]
Since \(\mathbb E R^{2j}=n(n+2)\cdots(n+2j-2)\), division by the independent radial moments gives
\[
\mathbb EY=0,\quad
\mathbb EY^2=\frac{2n}{n+2}A_2=:v,\quad
\mathbb EY^3=\frac{8n^2}{(n+2)(n+4)}A_3,
\]
\[
\mathbb EY^4=\frac{n^3(12A_2^2+48A_4)}{(n+2)(n+4)(n+6)}.
\tag{4}
\]
These formulas remain valid for zero eigenvalues, since they are polynomial identities.

**Step 2: an identity valid at the square-root singularity.** For every real \(x\ge0\), direct factorization with \(r=\sqrt x\), \(y=x-1\), gives
\[
1-\sqrt x=-\frac y2+\frac{y^2}8-\frac{y^3}{16}
+\frac{y^4(r^2+4r+5)}{16(1+r)^4}.
\tag{5}
\]
The last kernel is nonnegative. Its multiplier \((r^2+4r+5)/(16(1+r)^4)\) is decreasing for \(r\ge0\), because its derivative has the sign of \(-2r^2-10r-16\). Hence the multiplier belongs to \((0,5/16]\). Taking expectations in (5), applying \(\mathbb EY=0\), and substituting (4) yields (1) and (2). Notice that no Taylor theorem with a potentially divergent fourth derivative at \(x=0\) is invoked.

**Step 3: uniform diffuse asymptotic and sharpness.** Since \(A_4\le A_2^2\), (4) implies \(\mathbb EY^4\le15v^2\). Cauchy–Schwarz then gives \(|\mathbb EY^3|\le\sqrt{15}v^{3/2}\). Thus (5) and (4) yield the uniform bound
\[
\left|1-\vartheta_n(H)-\frac v8\right|
\le \frac{\sqrt{15}}{16}v^{3/2}+\frac{75}{16}v^2.
\tag{6}
\]
If \(\operatorname{tr}H_n^2\to0\), then \(v\le2\operatorname{tr}H_n^2\to0\). Dividing (6) by \(v/8>0\) proves (3). For explicit sharpness, take even \(n\), with half the eigenvalues equal to \((1+\eta)/n\) and half equal to \((1-\eta)/n\), where \(0<\eta<1\) is fixed. Then \(A_2=\eta^2/n\), \(v=2\eta^2/(n+2)>0\), so (3) applies with a nonzero deficit and forces the universal leading constant to be \(1/4\).

**Step 4: cubic shape discrimination.** In the two listed three-coordinate perturbations, \(A_2\) agrees, while \(A_3=\pm6\delta^3\) and \(A_4=18\delta^4\). The right side of (1) is \(O_n(\delta^4)\). Subtracting the two expansions gives the displayed cubic difference, with the minus sign because the positive \(A_3\) contributes negatively to the deficit. Both spectra remain positive for \(0<\delta<1/(2n)\).

## Verification

The standalone Python 3 verifier `verify.py` checks independently computed rational Dirichlet-sphere moments against all three expressions in (4), including singular spectra, for 180 deterministic finite-dimensional profiles. It also compares the spectral bounds against direct periodic midpoint integration of the circle law in dimension two and verifies the equal-purity/opposite-cubic construction. The recorded run passed 1,478 assertions (`verification_output.txt`). This finite testing neither replaces the all-dimensional proof nor establishes literature originality. Both files are provided with the result.

The decisive algebraic certificate is the exact factorization
\[
1-r+\tfrac12(r^2-1)-\tfrac18(r^2-1)^2+\tfrac1{16}(r^2-1)^3
=\tfrac1{16}(r-1)^4(r^2+4r+5),
\]
which verifies the sign, the boundary \(r=0\), and the normalization of the remainder. The Gaussian moment identities have been independently checked using rational Dirichlet moments, not only simulation.

## Relationship to prior work

Häggblom (2026), Proposition 7.1 and Corollary 1.3, defines precisely \(\vartheta_n(H)\), proves the exact variance \(v\), and establishes only the coarser diffuse bound \(0\le1-\vartheta_n(H)\le v/2\), along with convergence to one if and only if the inverse profile is diffuse. The present theorem does not claim these definitions, universality assertions, or the variance identity. It identifies the precise universal leading loss \(v/8\), the **signed cubic centered spectral correction**, and an explicit globally valid nonnegative quartic remainder, none of which is stated there. In the notation of the cited universality theorem, the hard-edge coefficient can therefore be replaced algebraically by the explicit spectral polynomial, with an additional controlled deterministic coefficient error \(O(v^2)\); this must not be misrepresented as an improved rate for the underlying random-matrix universality remainder.

Gusakova, Spodarev and Zaporozhets (2022) express the first intrinsic volume of an ellipsoid as the same kind of spherical square-root average, and give general integral representations. Those formulas supply a broader exact computational representation of the underlying functional, not the indicated signed moment enclosure. Häggblom's earlier (2026) Gaussian phase-retrieval study contains a related inverse-tail spherical-norm coefficient in a different application; its accessible relevant sections concern Gaussian inverse-tail linearization and trace concentration. Hillier (2001) studies densities of general sphere quadratic forms. These are acknowledged mathematical routes toward the object and remain priority risks for uninspected stronger derivative expansions. Literature searches and mathematical-record comparisons did not uncover a previously stated all-spectrum bound (1).

## Limitations

The advance is a deterministic quantitative refinement of a known random-matrix coefficient, **not** a new least-singular-value universality theorem. Formula (3) gives a relative asymptotic for the coefficient deficit, not automatically a relative second-order expansion for a random-matrix failure probability when the error in the parent universality theorem is larger than the deficit. The bound on the quartic remainder is explicit and uniform but is not claimed optimal. The theorem does not treat non-Haar direction laws or non-positive-semidefinite forms. Independent mathematical and historical-priority verification has not been performed.

## References

1. Christian E. Häggblom, *Ultra-hard-edge universality under deterministic preconditioning*, arXiv:2610.31143v1 (first posted 2026-10-22), especially Theorem 1.1, Corollary 1.3 and Proposition 7.1. https://arxiv.org/abs/2610.31143
2. Anna Gusakova, Evgeny Spodarev and Dmitry Zaporozhets, *Intrinsic volumes of ellipsoids*, arXiv:2206.14002v2, especially the spherical mean-width formula for the first intrinsic volume. https://arxiv.org/abs/2206.14002
3. Christian E. Häggblom, *Gaussian Critical-Threshold Instability in Real Phase Retrieval*, arXiv:2609.28198v1, especially Section 9. https://arxiv.org/abs/2609.28198
4. Grant Hillier, *The density of a quadratic form in a vector uniformly distributed on the n-sphere*, Econometric Theory 17 (2001), 1–28, doi:10.1017/S026646660117101X (abstract examined; full text not obtained).
