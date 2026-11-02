# Spectral-share majorization for one-column randomized SVD in finite and infinite rank

## Finding

For a single isotropic sketch column expressed in the right singular basis of a real Hilbert--Schmidt operator, random positive exchangeable squared coordinate amplitudes can only **flatten**, in expectation, the allocation of sketch energy across descending singular modes relative to a constant-amplitude (Rademacher-sign) sketch. This holds simultaneously at every singular-value cutoff, including countably infinite spectra, not merely for the total approximation error.

Write \(\lambda_1\ge\lambda_2\ge\cdots>0\), \(S=\sum_j\lambda_j\), and let \(p_j\) be the fraction of squared sketch norm in output singular mode \(j\). Then, for every positive integer \(k\) strictly smaller than the rank,
\[\boxed{\sum_{j=1}^k\mathbb E p_j\le\frac{\sum_{j=1}^k\lambda_j}{S}.}\]
The left side is ordered decreasingly. Equivalently, the expected spectral-share distribution is dominated in the majorization order by the normalized squared singular values. The conclusion implies simultaneous inequalities for all bounded nondecreasing spectral rewards, and an exact nonnegative pairwise formula for the expected squared Hilbert--Schmidt residual in excess of the constant-amplitude benchmark.

## Assumptions and scope

Let \(A:\mathcal H\to\mathcal K\) be a nonzero Hilbert--Schmidt operator between real separable Hilbert spaces. Choose a singular-value expansion \(Av_j=\sqrt{\lambda_j}u_j\), where the index set is finite or countably infinite and \(\lambda_1\ge\lambda_2\ge\cdots>0\). We require \(S=\sum_j\lambda_j<\infty\).

Let \((X_j)\) be a strictly positive exchangeable finite vector or countably infinite sequence, normalized by \(\mathbb E X_j=1\). Independently, let \((\epsilon_j)\) be independent equiprobable signs. The formal isotropic input sketch assigns coefficient \(\omega_j=\epsilon_j\sqrt{X_j}\) to \(v_j\). In infinite dimension this input need not be an element of \(\mathcal H\); the output series
\[y=\sum_j\sqrt{\lambda_j}\,\omega_j u_j\]
is well-defined in \(L^2(\mathcal K)\), since \(\mathbb E\|y\|^2=S\). The signs make distinct coefficients uncorrelated and each coordinate have variance one. Let \(P_y\) be the orthogonal projector onto the almost surely nonzero vector \(y\), and let \(\widehat A=P_y A\).

Put \(T=\sum_j\lambda_jX_j>0\), \(p_j=\lambda_jX_j/T\), \(q_j=\lambda_j/S\), and \(r_j=\mathbb E(X_j/T)\). All quantities are finite where needed: \(0\le p_j\le1\), \(\sum_jp_j=1\) almost surely, and \(r_j\le1/\lambda_j\). Exchangeability, rather than independence of amplitudes, is essential; independent signs are used to construct an isotropic sketch. For the uniqueness corollary only, the input coordinates are additionally assumed independent, identically distributed, centered, unit variance, and almost surely nonzero.

## Proof

**1. Projected energy.** By the singular-value decomposition, orthogonality, and the rank-one projection formula,
\[\|A-P_yA\|_{HS}^2=S-\|P_yA\|_{HS}^2
=S-\frac{\sum_j\lambda_j^2X_j}{T}
=S-\sum_j\lambda_jp_j.\]
This identity is exact even in infinite rank: \(\sum_j\lambda_j^2X_j\le\lambda_1T\) almost surely. For constant amplitudes \(X_j=1\), the squared residual equals \(R_0=S-(\sum_j\lambda_j^2)/S\).

**2. Pairwise swap identity.** Fix indices \(i<j\), write \(a=\lambda_i\ge b=\lambda_j\), \(x=X_i\), \(z=X_j\), and \(C=\sum_{m\ne i,j}\lambda_mX_m\). Set \(T=ax+bz+C\) and \(T^{ij}=az+bx+C\). Exchangeability gives the same law after interchanging \(x\) and \(z\). Hence
\[r_j-r_i
=\frac12\,\mathbb E\left[(z-x)\left(\frac1T-\frac1{T^{ij}}\right)\right]
=\frac{a-b}{2}\,\mathbb E\frac{(x-z)^2}{TT^{ij}}\ge0.\]
The denominators are strictly positive. Every expectation displayed is finite since the individual quantities \(X_i/T\) are bounded by \(1/\lambda_i\). Thus \(r_1\le r_2\le\cdots\).

The expected shares are also ordered. Applying the same swap symmetrization,
\[\mathbb E(p_i-p_j)=\frac{a-b}{2}\,\mathbb E\frac{2(a+b)xz+C(x+z)}{TT^{ij}}\ge0.\]
Consequently \(\bar p_j=\mathbb E p_j\) is decreasing and \(\sum_j\bar p_j=1\).

**3. Every-prefix majorization.** Let \(S_k=\sum_{j\le k}\lambda_j\). Since \(r_j\) is nondecreasing and the weights \(\lambda_j\) are positive,
\[\frac{\sum_{j\le k}\lambda_j r_j}{S_k}
\le \frac{\sum_j\lambda_jr_j}{S}
=\frac1S.\]
For countably infinite rank, the same inequality follows by splitting the full weighted mean into the initial block and its complement, whose entries are at least the block entries. Since \(\bar p_j=\lambda_jr_j\), this is precisely the displayed prefix theorem. As both \(\bar p\) and \(q\) have mass one and are decreasing, this is the majorization relation \(q\succeq\bar p\). Summation by parts, followed by bounded convergence for the infinite case, yields
\[\mathbb E\sum_j f(\lambda_j)p_j\le\sum_j f(\lambda_j)q_j\]
for each bounded nondecreasing real function \(f\). No continuity assumption on \(f\) is needed.

**4. Exact pairwise residual excess.** Since \(\sum_j\lambda_jr_j=1\), the expected captured energy \(F=\sum_j\lambda_j^2r_j\) satisfies
\[SF-\sum_j\lambda_j^2
=\sum_{i<j}\lambda_i\lambda_j(\lambda_i-\lambda_j)(r_i-r_j).\]
Substituting Step 2 and subtracting captured energies from \(S\) gives
\[\boxed{\mathbb E\|A-P_yA\|_{HS}^2-R_0
=\frac1{2S}\sum_{i<j}\lambda_i\lambda_j(\lambda_i-\lambda_j)^2
\mathbb E\frac{(X_i-X_j)^2}{T T^{ij}}.}\]
All terms on the right are nonnegative. In infinite rank the double-sum rearrangement is valid: for example, the sum of absolute values of the corresponding unsymmetrized terms is bounded by \(S\sum_i\lambda_i^2r_i+(\sum_i\lambda_i^2)(\sum_j\lambda_jr_j)\le2S\lambda_1\). Thus the exact pair sum converges; it is not obtained by an unjustified finite truncation.

If at least one pair has \(\lambda_i\ne\lambda_j\) and \(\mathbb P(X_i\ne X_j)>0\), the excess is strictly positive. For independent identically distributed amplitude squares, \(X_i=X_j\) almost surely forces a deterministic common value. Unit second moment makes it one, and independent centered coordinates taking only values of magnitude one are equiprobable signs. Conversely independent Rademacher signs give equality. For dependent exchangeable amplitudes, a common random positive factor gives equality as it cancels in every share.

## Verification

A standalone Python 3 checker (`verify.py`) enumerates every amplitude assignment from \(\{1/4,7/4\}\) for ordered integer spectra across 2–6 modes. It tests the exact expected ordering, every prefix bound, all swap identities, the pairwise excess formula, flat-spectrum equality, common-amplitude equality, and an exchangeable dependent sample-without-replacement law. It also checks a three-mode example using fractions without floating-point error. Run `python3 verify.py` from the package directory; the tests require only the Python standard library.

For \(\lambda=(9,4,1)\) and independent equally likely amplitudes \(X_j\in\{1/4,7/4\}\), the expected shares are exactly
\[\left(\frac{61375257}{105826105},\frac{67777909}{211652210},\frac{21123787}{211652210}\right),\]
compared with the constant-amplitude shares \((9/14,4/14,1/14)\). The constant-amplitude squared residual is \(7\), whereas random amplitudes give \(223734413/30236030\); the exact increase is \(12082203/30236030\). Finite checks illustrate but do not prove the countably infinite statement.

## Relationship to prior work

Lynch-Davies and Webb (2026, arXiv:2610.31333v1) develop a rigorous infinite-dimensional randomized SVD formulation using sketch functionals and bounds for sub-Gaussian sketch distributions. Their Theorem 3.15 is a high-probability approximation bound, not a statement about the expected energy allocated to every singular mode by a single sketch. Their experiments compare Gaussian and Rademacher sketches, but do not supply the every-prefix ordering or pairwise identity above.

Saibaba and Międlar (2023, arXiv:2308.05814) provide nonasymptotic approximation bounds for several non-Gaussian sketch families, based on sample-covariance estimates; these do not give the present exact one-column spectral-share majorization. Halko, Martinsson and Tropp (arXiv:0909.4061) give the standard randomized range-finding algorithm and Gaussian expected-error bounds. Diouane and collaborators (arXiv:2206.08793) treat nonstandard Gaussian covariance and mean in expected-error bounds. The elementary two-mode Rademacher comparison is a special case of the pairwise expression and is not the claimed contribution here; the contribution is a simultaneous all-cutoff theorem with an exact all-pairs formula and a countably infinite Hilbert--Schmidt extension.

## Limitations

The spectral coordinates must be an eigenbasis of \(A^*A\), and squared sketch amplitudes must be positive and exchangeable. Arbitrary rotations of independent Rademacher sketches need not preserve the comparison. The proof addresses one sketch column and expected squared Hilbert--Schmidt residual, not higher-rank subspaces, optimal rank-one approximation in every draw, tail probabilities, or oversampled practical error bounds. The countably infinite claim uses a cylindrical input sketch, not an ordinary random input vector in the Hilbert space. Independent verification and exhaustive historical-priority analysis remain outstanding.

## References

1. M. Lynch-Davies and M. Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD*, arXiv:2610.31333v1, first posted 2026-10-22. https://arxiv.org/abs/2610.31333
2. A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814, 2023. https://arxiv.org/abs/2308.05814
3. N. Halko, P.-G. Martinsson and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, arXiv:0909.4061, 2009. https://arxiv.org/abs/0909.4061
4. Y. Diouane, S. Gürol, A. Scotto Di Perrotolo and X. Vasseur, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793, 2022. https://arxiv.org/abs/2206.08793
