# Fixed-modulus optimality and a sharp Gaussian tail penalty in one-vector range finding

## Finding

For every integer \(d\ge 3\), every integer \(q\ge0\), and every strictly positive singular-value list of a real matrix whose right singular vectors are the standard coordinate vectors, independent fair signs minimize the **expected squared Frobenius residual** of a one-vector randomized subspace-iteration approximation among **all iid, centered, unit-variance real probes with almost surely nonzero entries**. There is an exact nonnegative pairwise formula for the excess expected residual of every competing probe, with strict inequality unless the singular values are all equal or the entries already have unit absolute value almost surely.

For a one-spike diagonal family, the theorem also yields a sharp asymptotic separation: the excess residual of a one-vector Gaussian sketch decreases as \(L^{-(2q+1)/2}\), whereas that of the sign sketch decreases as \(L^{-(2q+1)}\), with explicit positive constants. Here \(L>1\) is the ratio of the leading squared singular value to each remaining squared singular value and \(q\) is the number of power-iteration rounds. This is a comparison of **expected squared residuals** at equal one-vector sketch size, not a worst-case orientation guarantee.

## Assumptions and scope

Take \(m\ge d\ge3\), \(U\in\mathbb R^{m\times d}\) with \(U^{\mathsf T}U=I_d\), and
\[
 A=U\operatorname{diag}(\sqrt{a_1},\ldots,\sqrt{a_d}),\qquad a_i>0.
\]
Thus the right singular directions coincide with the input-coordinate basis. For a nonnegative integer \(q\), draw one probe \(\xi\in\mathbb R^d\) and form
\[
 Y=(AA^{\mathsf T})^q A\xi,\qquad
 P_Y=\frac{YY^{\mathsf T}}{Y^{\mathsf T}Y},\qquad
 \mathcal R(\xi)=\|A-P_YA\|_F^2.
\]
The entries \(\xi_i\) are iid, \(\mathbb E\xi_i=0\), \(\mathbb E\xi_i^2=1\), and \(\Pr(\xi_i=0)=0\). Hence \(Y\ne0\) almost surely. Define \(b_i=a_i^{2q+1}\), \(B=\sum_i b_i\), \(W_i=\xi_i^2\), \(S=\sum_i b_iW_i\), and for \(i<j\)
\[
 S_{ij}=S+(b_i-b_j)(W_j-W_i).
\]
The last quantity is the positive denominator obtained by swapping \(W_i\) and \(W_j\) while leaving all other coordinates unchanged.

Let \(\mathcal R_\pm\) denote the residual for iid fair Rademacher signs. The exact identity is
\[
\boxed{\mathbb E\mathcal R(\xi)-\mathbb E\mathcal R_\pm
=\frac1{2B}\sum_{i<j}b_i b_j(a_i-a_j)(b_i-b_j)
\mathbb E\!\left[\frac{(W_i-W_j)^2}{S S_{ij}}\right]\ge0.}
\]
The comparison is simultaneous in \(d\), \(q\), and the positive singular spectrum, and has no higher-moment assumptions on the probe. Equality holds precisely when either all \(a_i\) are equal or \(W_i=1\) almost surely. With the stated centering, the latter means iid fair signs. In particular, a Gaussian probe is strictly worse whenever the spectrum is nonflat.

For the spike family \(A=\operatorname{diag}(\sqrt L,1,\ldots,1)\), \(L>1\), the optimal rank-one squared Frobenius error is \(d-1\). Put \(H=L^{2q+1}\) and \(\nu=(d-1)/2\). The exact sign excess is
\[
 \mathbb E\mathcal R_\pm-(d-1)
 =\frac{(L-1)(d-1)}{H+d-1}.
\]
For a standard Gaussian probe let \(T\sim\operatorname{Beta}(1/2,\nu)\). Its exact excess is
\[
 \mathbb E\mathcal R_G-(d-1)
 =(L-1)\mathbb E\left[\frac{1-T}{1+(H-1)T}\right].
\]
At fixed \(d\ge3\), \(L>1\), as \(q\to\infty\),
\[
 \mathbb E\mathcal R_G-(d-1)
 \sim (L-1)\frac{\sqrt\pi\,\Gamma(d/2)}{\Gamma((d-1)/2)}H^{-1/2},
 \qquad
 \mathbb E\mathcal R_\pm-(d-1)
 \sim (L-1)(d-1)H^{-1}.
\]
Consequently their excess-risk ratio grows asymptotically as
\[
 \frac{\mathbb E\mathcal R_G-(d-1)}{\mathbb E\mathcal R_\pm-(d-1)}
 \sim\frac{\sqrt\pi\,\Gamma(d/2)}{(d-1)\Gamma((d-1)/2)}\sqrt H.
\]

## Proof

**Step 1: deterministic reduction.** Because \(Y=U\operatorname{diag}(a_i^{q+1/2})\xi\), elementary projector algebra gives
\[
 \mathcal R(\xi)=\sum_i a_i-\frac{\sum_i a_i b_iW_i}{\sum_i b_iW_i}.
\]
The nonconstant quotient is bounded by the smallest and largest \(a_i\), so its expectation always exists. For fair signs \(W_i=1\) deterministically, hence
\[
 \mathbb E\mathcal R_\pm=\sum_i a_i-\frac{\sum_i a_i b_i}{B}.
\]

**Step 2: exchangeability identity.** Set \(\alpha_i=\mathbb E(W_i/S)\). Since \(0\le b_iW_i/S\le1\), every \(\alpha_i\) is finite; also \(\sum_i b_i\alpha_i=1\). For \(i<j\), exchangeability of the iid squared magnitudes and the swap \((W_i,W_j)\mapsto(W_j,W_i)\) give
\[
 \begin{aligned}
 \alpha_j-\alpha_i
 &=\frac12\mathbb E\left[(W_j-W_i)\left(\frac1S-\frac1{S_{ij}}\right)\right]\\
 &=\frac{b_i-b_j}{2}\mathbb E\left[\frac{(W_i-W_j)^2}{S S_{ij}}\right].
 \end{aligned}
\]
All terms are well-defined, including distributions without finite fourth moments, because the first expression is the difference of two finite expectations. Substituting \(\sum_i b_i\alpha_i=1\) into the deterministic reduction and pairing the ordered terms yields
\[
 \mathbb E\mathcal R(\xi)-\mathbb E\mathcal R_\pm
 =\frac1B\sum_{i<j}b_ib_j(a_i-a_j)(\alpha_j-\alpha_i),
\]
which proves the boxed identity. The function \(t\mapsto t^{2q+1}\) is strictly increasing on positive inputs, so \((a_i-a_j)(b_i-b_j)\ge0\). If some \(a_i\ne a_j\) and the iid squared magnitudes are nonconstant, then \(\Pr(W_i\ne W_j)>0\) and that pair has strictly positive contribution. Conversely, if every \(a_i\) is equal the residual is constant, and if \(W_i\equiv1\) the pairwise difference vanishes. The unit-variance and mean-zero hypotheses turn a constant \(W_i\) into a fair sign entry. This proves the precise equality cases.

**Step 3: spike representation.** For the displayed one-spike matrix, let \(V=\sum_{i=2}^d W_i\). The deterministic reduction gives
\[
 \mathcal R(\xi)-(d-1)=(L-1)\frac{V}{H W_1+V}.
\]
Fair signs give \(W_1=1\), \(V=d-1\), proving the exact rational formula. For Gaussian probes, \(W_1\sim\chi_1^2\) and \(V\sim\chi_{d-1}^2\) independently. Their ratio \(T=W_1/(W_1+V)\) has the stated beta distribution, giving the Gaussian integral exactly.

**Step 4: sharp exponent.** Write \(\mathrm B\) for the Euler beta function. The Gaussian ratio is
\[
 I(H)=\frac1{\mathrm B(1/2,\nu)}
 \int_0^1\frac{t^{-1/2}(1-t)^\nu}{1+(H-1)t}\,dt.
\]
With \(u=Ht\),
\[
 \sqrt H I(H)=\frac1{\mathrm B(1/2,\nu)}
 \int_0^H\frac{u^{-1/2}(1-u/H)^\nu}{1+(1-1/H)u}\,du.
\]
For \(H\ge2\), the integrand, extended as zero above \(H\), is bounded by \(u^{-1/2}/(1+u/2)\), which is integrable on \((0,\infty)\). Dominated convergence gives a limit \(\pi/\mathrm B(1/2,\nu)=\sqrt\pi\,\Gamma(d/2)/\Gamma((d-1)/2)\), strictly positive. The sign expression is rational and has excess asymptotic to \((L-1)(d-1)/H\). Thus both rates and the ratio follow, without inferring them from finite computation.

## Verification

Run `python3 verify.py` with Python 3.9 or later. The standalone dependency-free checker verifies the pairwise identity exactly over 60 finite iid squared-magnitude models, checks strict and equality cases, and checks the one-spike sign formula over dimensions, spectra and power indices. It also independently evaluates five Gaussian beta integrals against direct Gaussian samples and performs four two-coordinate consistency tests. The package replay reports **621 passed exact-rational or numerical check groups**. Its finite cases test the algebra; the preceding proof is necessary for the infinite quantifiers and the asymptotic statements.

An illustrative non-asymptotic case is \(d=3\), \(L=4\), \(q=1\), where \(H=64\). The sign excess is exactly \(1/11\), while the Gaussian excess equals
\[
 3\left(\frac{64}{63}\frac{\arctan\sqrt{63}}{\sqrt{63}}-\frac1{63}\right)
 \approx0.5073886864.
\]
The respective total squared residuals are obtained by adding the optimal rank-one error \(2\). These are formula evaluations, not empirical risk estimates.

## Relationship to prior work

Saibaba and Międlar (2023 preprint; 2025 journal article) develop broad randomized low-rank approximation bounds and investigate non-Gaussian probes, including signs and the subspace-iteration variant. Their analysis emphasizes sample-complexity and qualitative distribution classes rather than an exact distribution-free minimizer for this one-vector, singular-coordinate-aligned class or the sharp one-spike asymptotic ratio. Saibaba (2018) and Diouane et al. (2022) supply different canonical-angle and expected-error bounds. Epperly and Webber (2026) study a stronger worst-case-over-inputs **minimax** formulation for randomized SVD; this does not imply the fixed-input, fixed-orientation iid magnitude comparison here, because the quantifiers and admissible random embeddings differ. The real-valued minimax bound in its Theorem 3.3 also requires more sketch columns than the target rank plus one, so it does not cover this one-column case. The exceptional two-coordinate, no-power comparison is not part of the present novelty claim.

## Limitations

The conclusion depends essentially on the probe coordinates coinciding with the right singular directions. Rotating a matrix while keeping an iid sign probe in the original coordinates changes its law relative to the singular basis; no arbitrary-orientation superiority is asserted. The optimality is only among iid real, centered unit-variance entries with almost surely nonzero magnitudes, for a **single** sketch vector and expected squared Frobenius error. It is not a universal claim for multi-column or dependent embeddings, rank-truncated postprocessing, spectral-norm risk, or all matrix orientations. The sharp Gaussian/sign exponent comparison is for a fixed-dimension, fixed-spike family in the limit of increasing integer power rounds. Literature priority may be affected by general exchangeability or normalized-random-weight inequalities not explicitly marketed as randomized range-finding results. No independent scientific validation has been performed.

## References

1. A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814v1 (first public 2023-08-10), https://arxiv.org/html/2308.05814v1; SIAM Journal on Mathematics of Data Science 7 (2025), 136–162, DOI 10.1137/23M1593255.
2. A. K. Saibaba, *Randomized subspace iteration: Analysis of canonical angles and unitarily invariant norms*, arXiv:1804.02614, https://arxiv.org/abs/1804.02614.
3. Y. Diouane and collaborators, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793, https://arxiv.org/html/2206.08793v2.
4. E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096v2 (2026), https://arxiv.org/html/2605.19096v2.
