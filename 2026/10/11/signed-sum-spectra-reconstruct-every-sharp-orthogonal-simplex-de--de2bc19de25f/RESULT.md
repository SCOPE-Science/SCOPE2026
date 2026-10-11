# Signed-sum spectra reconstruct every sharp orthogonal-simplex decomposition

## Finding

Let \(u_1,\ldots,u_n\in\mathbb R^d\) be unit vectors with \(n\ge d\), and assume the configuration is sharp for the recent large-signed-sum theorem:
\[
\max_{\varepsilon\in\{-1,1\}^n}
\left\|\sum_{j=1}^n\varepsilon_j u_j\right\|^2=2n-d.
\]
Then the multiset
\[
\mathcal S(U)=
\left\{
\left\|\sum_{j=1}^n\varepsilon_j u_j\right\|^2:
\varepsilon\in\{-1,1\}^n
\right\}
\]
with multiplicity is a complete invariant of the sharp configuration up to permutation of the vectors, independent sign changes, and orthogonal transformations.

More explicitly, the equality classification of Jiang--Lim--Parvatikar gives, after switching and permutation, an orthogonal decomposition into an orthonormal remainder of dimension \(r\) and \(m=n-d\) centered regular-simplex blocks of positive even dimensions \(k_1,\ldots,k_m\), with
\[
r+\sum_{i=1}^m k_i=d.
\]
If \(T=2n-d\) and
\[
D(\varepsilon)=T-
\left\|\sum_{j=1}^n\varepsilon_j u_j\right\|^2,
\]
then the defect multiset has the exact convolution factorization
\[
\sum_{\varepsilon}\delta_{D(\varepsilon)}
=
2^r\delta_0*\nu_{k_1}*\cdots*\nu_{k_m},
\]
where, for every positive even \(k\),
\[
\nu_k=
\sum_{t=0}^{k/2}
2\binom{k+1}{k/2-t}
\delta_{4t(t+1)/k}.
\]

The factorization is injective. In particular, if \(K=\max_i k_i\) and exactly \(q\) blocks have dimension \(K\), then the two highest signed-sum levels already reveal
\[
\min\{D(\varepsilon):D(\varepsilon)>0\}=\frac{8}{K}
\]
and
\[
\frac{\#\{\varepsilon:D(\varepsilon)=8/K\}}
{\#\{\varepsilon:D(\varepsilon)=0\}}
=
\frac{qK}{K+4}.
\]
After recovering \(K\) and \(q\), canceling the known factor \(\nu_K^{*q}\) and iterating recovers the complete multiset of simplex dimensions. Thus two sharp configurations have the same signed-sum norm spectrum if and only if they are equivalent in the equality classification.

For example, at \((d,n)=(6,8)\), the sharp type with simplex dimensions \((2,2)\) and orthonormal remainder dimension \(2\), and the sharp type with simplex dimensions \((2,4)\) and no orthonormal remainder, have the same sharp maximum \(10\) but are immediately separated by their first defects, respectively \(4\) and \(2\).

## Assumptions and scope

The result concerns only configurations attaining equality in the Jiang--Lim--Parvatikar bound. It does not assert that the signed-sum spectrum classifies arbitrary unit-vector configurations, nor does it address the unresolved regime in which the optimal constant is strictly larger than \(\sqrt{2n-d}\).

The spectrum is a multiset: multiplicities of sign vectors are essential. Switching one input vector merely permutes sign vectors, and orthogonal transformations preserve all norms, so the stated equivalence operations preserve the spectrum.

## Proof

The equality theorem of Jiang--Lim--Parvatikar states that every sharp configuration is, after switching, a mutually orthogonal union of centered regular simplices in positive even dimensions and an orthonormal set. Consider one simplex block of dimension \(k\). It has \(k+1\) unit vertices \(v_0,\ldots,v_k\) satisfying
\[
\langle v_a,v_b\rangle=-\frac1k
\qquad(a\ne b).
\]
For signs \(\eta_0,\ldots,\eta_k\), write
\[
s=\sum_{a=0}^k\eta_a.
\]
The source computation gives
\[
\left\|\sum_{a=0}^k\eta_a v_a\right\|^2
=
\frac{(k+1)^2-s^2}{k}.
\]
Because \(k\) is even, \(k+1\) is odd. Hence \(|s|=2t+1\) for a unique integer \(0\le t\le k/2\). The maximal block value is \(k+2\), obtained at \(t=0\), and the defect from this block maximum is
\[
(k+2)-
\frac{(k+1)^2-(2t+1)^2}{k}
=
\frac{4t(t+1)}{k}.
\]
For a fixed \(t\), the number of sign vectors with \(|s|=2t+1\) is
\[
2\binom{k+1}{k/2-t}.
\]
This proves the formula for \(\nu_k\).

Every signed sum on the orthonormal remainder has the same squared norm \(r\), and its \(2^r\) signings contribute only multiplicity. Orthogonality makes squared norms add across blocks, so defects add. This proves the convolution factorization.

The total multiplicity of the signed-sum spectrum is \(2^n\), so the spectrum itself recovers \(n\). Its largest squared norm is \(T=2n-d\), so it then recovers \(d=2n-T\) as well. It remains to prove that the factorization determines the block dimensions. For any block of dimension \(k\), its least positive defect is obtained at \(t=1\) and equals \(8/k\). Therefore the least positive atom of the full defect measure is \(8/K\), where \(K\) is the largest block dimension.

Let \(M_0\) be the multiplicity of defect zero and \(M_1\) the multiplicity at \(8/K\). A defect of size \(8/K\) can arise only by taking \(t=1\) in exactly one largest block and \(t=0\) everywhere else. If \(q\) blocks have dimension \(K\), then
\[
\frac{M_1}{M_0}
=
q\,
\frac{\binom{K+1}{K/2-1}}{\binom{K+1}{K/2}}
=
\frac{qK}{K+4}.
\]
Thus the spectrum recovers both \(K\) and its multiplicity \(q\).

For a finite defect measure \(\mu\), write its Laplace transform as
\[
L_\mu(s)=\int e^{-sx}\,d\mu(x).
\]
The transform of \(\nu_k\) is a strictly positive finite exponential sum for every real \(s\). Hence, after recovering \(K\) and \(q\), one may divide
\[
L_\mu(s)
\quad\text{by}\quad
L_{\nu_K}(s)^q
\]
for real \(s\). The quotient is exactly the Laplace transform of the residual convolution. Finite measures on \([0,\infty)\) are uniquely determined by their Laplace transforms, so the residual defect measure is determined uniquely. Iterating recovers every simplex-block dimension. Finally,
\[
r=d-\sum_i k_i.
\]

Conversely, equal block dimensions and equal \(r\) give orthogonally congruent centered regular simplices and orthonormal remainders; the source equality classification then gives equivalence after switching and permutation. This proves completeness of the signed-sum spectrum.

## Verification

The proof is exact and analytic. The packaged checker independently constructs the rational defect measures of all admissible sharp block decompositions through ambient dimension \(16\), confirms that no two decomposition types with the same \((n,d)\) have the same spectrum, and checks the first-defect and first-multiplicity formulas.

The finite check is a stress test only. The general theorem rests on the displayed block formula, the smallest-positive-defect argument, and uniqueness of finite measures from their Laplace transforms.

## Relationship to prior work

Jiang, Lim, and Parvatikar prove the sharp bound, classify every equality configuration into mutually orthogonal even-dimensional regular-simplex blocks plus an orthonormal set, and compute the squared norm of a signed sum inside one simplex block. Their paper does not state a convolutional defect spectrum, does not compare spectra of different equality decompositions, and does not prove that the scalar multiset of all signed-sum norms reconstructs the decomposition.

Pinasco independently solves the first linearly dependent case \(n=d+1\). In the model equality configurations he records the same one-simplex signed-sum formula and identifies the maximizing signs by the condition that the sign imbalance has absolute value \(1\). That paper has only one simplex block and does not state the multi-block convolution or the inverse reconstruction theorem.

Targeted searches for signed-sum spectra, maximizing-sign multiplicities, orthogonal simplex-block spectra, and reconstruction of the equality decomposition found no equivalent statement. A nearby published result studies second-order Gram stability of the planar three-vector extremizer; it concerns perturbative stability near a single equilateral block and does not determine or reconstruct the multi-block signed-sum spectrum.

## Limitations

This is a rigidity theorem inside the sharp equality class, not a stability theorem for nearly sharp systems. The inverse step assumes exact spectral multiplicities and exact signed-sum norms; no noise-robust reconstruction estimate is proved. The result also does not determine the unresolved constants for \(n>3d/2\).

The originality assessment is based on the inspected primary texts and targeted statement-level searches; it does not claim exhaustive coverage of every unpublished or unindexed note.

## References

1. Z. Jiang, J. Lim, and S. Parvatikar, *Unbalancing unit vectors*, arXiv:2609.31389v1, 25 September 2026. Primary MSC 52A40; secondary MSC 52A37.
2. D. Pinasco, *Large signed sums of unit vectors: the first linearly dependent case*, arXiv:2609.21101v1, 17 September 2026. Primary MSC 52A40; secondary MSC 52A37.
