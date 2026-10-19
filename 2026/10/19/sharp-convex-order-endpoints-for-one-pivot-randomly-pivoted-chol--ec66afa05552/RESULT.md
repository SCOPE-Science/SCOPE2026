# Sharp convex-order endpoints for one-pivot randomly pivoted Cholesky

## Finding

The trace decrease in **one** diagonal-proportional randomly pivoted Cholesky step admits a complete, sharp stochastic-risk envelope on every fixed real-symmetric or complex-Hermitian positive-semidefinite spectral orbit. Let \(A\) be a nonzero \(n\times n\) positive-semidefinite matrix with eigenvalues \(\lambda_1,\ldots,\lambda_n\ge0\), set \(S=\sum_j\lambda_j\), and put
\[
q=\frac{\sum_j\lambda_j^2}{S}.
\]
Sample index \(I\) with probability \(A_{ii}/S\) and form the one-pivot Nyström approximation \(\widehat A=Ae_Ie_I^*A/A_{II}\). Its trace gain is \(G_A=\operatorname{tr}\widehat A\). Let \(\Lambda\) have the **size-biased spectral law** \(\Pr\{\Lambda=\lambda_j\}=\lambda_j/S\), combining repeated values if needed. For every finite convex function \(\varphi\) on \([0,\max_j\lambda_j]\),
\[
\boxed{\varphi(q)\le \mathbb E\varphi(G_A)\le
\frac1S\sum_{j=1}^n\lambda_j\varphi(\lambda_j).}
\]
Both bounds are **simultaneously attained for every convex \(\varphi\)** among matrices with the specified eigenvalues: an eigenbasis attains the right-hand side, while a real orthogonal change of basis (respectively a unitary change of basis) can make \(G_A=q\) for *every pivot of positive probability*, attaining the left-hand side. Equivalently, \(q\preceq_{\mathrm{cx}}G_A\preceq_{\mathrm{cx}}\Lambda\).

Consequently the **entire attainable variance interval** under orthogonal or unitary changes of basis is
\[
\boxed{0\le\operatorname{Var}(G_A)=\operatorname{Var}(\operatorname{tr}(A-\widehat A))\le
\frac{\sum_j\lambda_j^3}{S}-\left(\frac{\sum_j\lambda_j^2}{S}\right)^2.}
\]
The maximum is zero precisely when all strictly positive eigenvalues are equal. The gain is deterministic for a given matrix precisely when
\[
\operatorname{diag}(A^2-qA)=0.
\]
The expected one-step residual trace, \(S-q\), is spectral and is the same at both endpoints; the stochastic dispersion need not be.

## Assumptions and scope

All matrices are finite-dimensional, real symmetric or complex Hermitian, positive semidefinite and nonzero. Indexing uses \(1\le i\le n\). If \(A_{ii}=0\), positive semidefiniteness implies \(Ae_i=0\); that index has zero sampling probability and its rank-one quotient is never evaluated. Sampling probabilities are **exactly** proportional to the diagonal before the first update, and computations are in exact arithmetic. The approximation uses one column, not a block or a second adaptive pivot. For fixed eigenvalues, “change of basis” means varying \(A=U\operatorname{diag}(\lambda)U^*\) through real orthogonal \(U\) or complex unitary \(U\), as appropriate. The convex-order bounds concern this stochastic trace gain, not a pathwise order between residual matrices.

## Proof

**1. Exact one-pivot trace gain.** Put \(a_i=A_{ii}\), \(b_i=(A^2)_{ii}=\|Ae_i\|_2^2\), and \(p_i=a_i/S\). For every sampled \(i\), the rank-one update is \(Ae_ie_i^*A/a_i\), so
\[
G_A\mid(I=i)=g_i:=\frac{b_i}{a_i},\qquad
\mathbb EG_A=\sum_{i:a_i>0}\frac{a_i}{S}\frac{b_i}{a_i}
=\frac{\operatorname{tr}(A^2)}{S}=q.
\]
The last expectation coincides with the established one-step expected-residual identity in Chen–Epperly–Tropp–Webber, but says nothing by itself about the distribution.

**2. A size-biased spectral martingale coupling.** Write \(A=U\operatorname{diag}(\lambda)U^*\) and \(w_{ij}=|U_{ij}|^2\). Select an auxiliary spectral index \(J\) with \(\Pr(J=j)=\lambda_j/S\); conditional on \(J=j\), select \(I\) with \(\Pr(I=i\mid J=j)=w_{ij}\). Because every column of \(U\) has squared entries summing to one, this is a probability coupling. Its index marginal is
\[
\Pr(I=i)=\sum_j\frac{\lambda_j}{S}w_{ij}=\frac{a_i}{S},
\]
and on every index of positive marginal mass,
\[
\mathbb E[\lambda_J\mid I=i]
=\frac{\sum_j\lambda_j^2w_{ij}}{\sum_j\lambda_jw_{ij}}
=\frac{(A^2)_{ii}}{A_{ii}}=g_i.
\]
Thus \(G_A\) has the law of \(\mathbb E[\Lambda\mid I]\). Conditional Jensen yields \(\mathbb E\varphi(G_A)\le\mathbb E\varphi(\Lambda)\); unconditional Jensen and \(\mathbb EG_A=q\) yield the other inequality. This proves the stated convex ordering for **every** convex \(\varphi\), including nonsmooth functions.

**3. Simultaneous sharpness.** In an eigenbasis, \(I=j\) has probability \(\lambda_j/S\) and \(g_j=\lambda_j\) whenever \(\lambda_j>0\); hence \(G_A\) has exactly the law of \(\Lambda\). To attain the other endpoint, define \(B=A^2-qA\). This is Hermitian with \(\operatorname{tr}B=0\). Every finite-dimensional trace-zero Hermitian matrix admits an orthonormal basis in which all diagonal entries vanish: if \(B\ne0\), it has a positive and a negative eigenvalue, and a suitable real linear combination of corresponding unit eigenvectors has zero quadratic form; compress \(B\) to that vector's orthogonal complement, whose trace is still zero, and continue inductively. If \(B\) is real symmetric, all vectors and changes of basis can be chosen real. Applying this construction to \(B\) yields a basis with \(b_i=q a_i\) for every \(i\); hence \(g_i=q\) for all sampled indices. Both endpoints are therefore attainable without assumptions on eigenvalue multiplicity or rank.

**4. Exact variance and every intermediate variance.** Taking \(\varphi(x)=x^2\) and subtracting \(q^2\) yields the sharp upper variance \(\sum_j\lambda_j^3/S-q^2\) and the attained lower value zero. The upper bound vanishes exactly if the size-biased law of \(\Lambda\) is concentrated at one value, that is, all positive \(\lambda_j\) are equal. Since \(G_A\) is constant exactly when \(b_i=qa_i\) at every positive-probability index, and zero-diagonal indices of a positive-semidefinite matrix have \(a_i=b_i=0\), the displayed diagonal condition is necessary and sufficient.

For completeness, the variance is continuous along a change of basis even when some \(a_i\) vanishes: \(0\le b_i\le\lambda_{\max}a_i\) implies \(0\le b_i^2/a_i\le\lambda_{\max}^2a_i\), with the ratio interpreted as zero when \(a_i=0\). The unitary orbit is connected. The real orthogonal orbit is likewise connected as a set because changing the sign of one eigenvector preserves \(U\operatorname{diag}(\lambda)U^{\mathsf T}\) and allows either determinant sign; \(\mathrm{SO}(n)\) is path connected for \(n\ge2\). Continuity and attainment of both endpoints therefore give **every** intermediate variance. The \(n=1\) case has the singleton variance interval \(\{0\}\).

## Verification

For a two-dimensional exact illustration, take \(A_0=\operatorname{diag}(1,4)\). The gain equals \(1\) with probability \(1/5\) and \(4\) with probability \(4/5\), so \(q=17/5\), residual-trace expectation is \(8/5\), and gain/residual-trace variance is \(36/25\). Rotating by \(45^\circ\) gives \(A_1=\frac12\begin{pmatrix}5&-3\\-3&5\end{pmatrix}\); either pivot has gain \(17/5\), and hence residual trace is **always** \(8/5\). The spectra and expected errors coincide, but the variances are the exact opposite endpoints.

The standalone `verify.py` evaluates the actual one-pivot Schur complements, the conditional-Jensen inequalities for multiple convex test functions, the spectral variance extremum, and the constructive trace-zero-diagonal real basis on random matrices in dimensions \(2\) through \(8\), including rank-deficient and repeated-spectrum cases. Its recorded output is in `verification_output.txt`. These finite tests support the formulas but **do not establish** the dimension-uniform or all-convex-function conclusions; those follow from Steps 1–4.

## Relationship to prior work

Chen, Epperly, Tropp and Webber introduce the diagonal-proportional RPCholesky rule and obtain the exact expected residual map \(\Phi(A)=A-A^2/\operatorname{tr}A\) and multi-step expected trace guarantees. The mean \(q\) in Step 1 is therefore **not claimed as new**. Steinerberger examines a different diagonal-power pivot rule and expected Schatten-norm progress; the pointwise Cauchy–Schwarz inequality used there, \((A^2)_{ii}^2\le A_{ii}(A^3)_{ii}\), also yields the upper variance inequality after summation. Neither that elementary upper inequality nor the spectral mean is claimed as individually new. Epperly, Tropp and Webber develop accelerated sampling with the same RPCholesky law. The present assertion is instead the sharp **entire convex-order risk envelope for a fixed spectrum**, with both real/complex attainable endpoints and a precise zero-variance basis condition. None of the inspected pertinent results implies these distributional extremal statements merely from its expectation or convergence inequalities.

The proof uses classical conditional Jensen and the elementary trace-zero diagonalization principle. Possible alternative formulations in literature on martingale convex order, spectral majorization or one-step pivot concentration remain a residual novelty risk; this statement does not assert that those general mathematical principles are new.

## Limitations

Only the first exact Cholesky/Nyström pivot is analyzed; no inference is made about joint laws or convex order after multiple adaptive pivots. The theorem compares conjugate matrices with identical spectra, not a single fixed kernel matrix under physically available data reorderings. Constructing a zero-variance basis generally requires matrix-wide spectral information and may destroy sparsity or entry-access advantages; it is **not** an inexpensive algorithmic preprocessing guarantee. Convex order controls expectations of convex losses, not pointwise matrix order or ordinary stochastic tail dominance. Finite floating-point tests do not verify all convex functions or all dimensions.

## References

1. Y. Chen, E. N. Epperly, J. A. Tropp, R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503, initially public 2022-07-13; especially Algorithm 1 and Eq. (5.3), https://arxiv.org/abs/2207.06503.
2. S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, arXiv:2404.11487, 2024-04-17; Sections 1–2, https://arxiv.org/abs/2404.11487.
3. E. N. Epperly, J. A. Tropp, R. J. Webber, *Embrace rejection: Kernel matrix approximation by accelerated randomly pivoted Cholesky*, arXiv:2410.03969, initially public 2024-10-04; Sections 1–2, https://arxiv.org/abs/2410.03969.
