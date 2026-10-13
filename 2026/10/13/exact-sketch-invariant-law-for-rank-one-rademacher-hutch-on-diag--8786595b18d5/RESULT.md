# Exact sketch-invariant law for rank-one Rademacher Hutch++ on diagonal matrices
## Finding

The original Hutch++ algorithm uses a Rademacher matrix sketch to construct an orthogonal subspace, evaluates the trace on that subspace exactly, then estimates the residual trace by independent Rademacher probes. At its smallest allowed matrix-vector budget, three products, the sketch has one column.

For that natural budget we prove an **exact entire output distribution** on *every* positive diagonal spectrum. Unexpectedly, although the subspace itself depends on the sketch signs, the estimator's conditional distribution does not depend on those signs at all.

Let
\[
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),\quad n\ge2,\quad \lambda_i>0,
\]
with
\[
S_2=\sum_{i=1}^{n}\lambda_i^2,\qquad
S_3=\sum_{i=1}^{n}\lambda_i^3,\qquad
\mu=\frac{S_3}{S_2}.
\]
Sample an independent-sign sketch \(s\in\{\pm1\}^n\), take \(q=As/\|As\|_2\), and use \(\ell\ge1\) independent fair sign probes \(\xi_a\) on the deflated matrix:
\[
\widehat T
=q^\top A q+
\frac1\ell\sum_{a=1}^{\ell}
\xi_a^\top(I-qq^\top)A(I-qq^\top)\xi_a.
\]
The case \(\ell=1\) is exactly the published three-query Hutch++; allowing more probes only repeats its stochastic second phase at the same rank-one sketch.

Let \(z_{ia}\) be independent uniform signs, and set
\[
U_a=\sum_i\lambda_i z_{ia},\qquad V_a=\sum_i\lambda_i^2 z_{ia}.
\]
For **every fixed realization** of the sketch signs, the conditional law is
\[
\boxed{
\widehat T\ \overset{d}{=}
\sum_i\lambda_i+\mu
-\frac{2}{\ell S_2}\sum_{a=1}^{\ell}U_aV_a
+\frac{S_3}{\ell S_2^2}\sum_{a=1}^{\ell}U_a^2.
}
\]
Thus sketch randomness does not mix different output distributions, even for nonuniform diagonal spectra. In particular, \(\widehat T\) is unbiased and
\[
\boxed{
\operatorname{Var}(\widehat T)
=\frac4\ell\sum_{1\le i<j\le n}
\left(\frac{\lambda_i\lambda_j}{S_2}\right)^2
(\mu-\lambda_i-\lambda_j)^2
>0.
}
\]
This holds for every strictly positive diagonal spectrum, although the ordinary Rademacher Hutchinson estimator of the same matrix equals \(\operatorname{tr}A\) **without any randomness**.

On the flat spectrum \(A=\lambda I_n\), with \(\lambda>0\), the full law simplifies to
\[
\boxed{
\widehat T\ \overset{d}{=}
\lambda(n+1)-\frac{\lambda}{n\ell}
\sum_{a=1}^{\ell}\left(\sum_{i=1}^{n}z_{ia}\right)^2
},\qquad
\boxed{
\operatorname{Var}(\widehat T)=\frac{2\lambda^2(n-1)}{n\ell}.
}
\]
For \(n=2\) and the published \(\ell=1\) version, \(\widehat T\) takes \(\lambda\) or \(3\lambda\), each with probability \(1/2\). The target is \(2\lambda\), so the **absolute error is \(\lambda\) on every run**. This is a concrete resolution-dependent precision obstruction at the minimum Hutch++ budget, rather than simply a variance bound.

The low-budget effect persists for growing dimension. At any fixed number \(\ell\) of residual probes and fixed \(\lambda>0\), the central limit theorem for independent fair signs gives the nondegenerate limiting **absolute** error law
\[
\boxed{
\frac{\widehat T-n\lambda}{\lambda}
\ \Longrightarrow\ 1-\frac{\chi^2_{\ell}}{\ell}
}\qquad(n\to\infty).
\]
In particular the absolute error variance tends to \(2\lambda^2/\ell\), although the relative error converges to zero as the trace grows like \(n\lambda\). This quantifies the finite-query regime in large dimension, not merely a small-matrix anomaly.

## Assumptions and scope

The matrix is real diagonal positive definite in the coordinate system where Rademacher signs are sampled. This basis assumption matters: a general orthogonal similarity preserves eigenvalues but not the law of a Rademacher quadratic form.

The sketch is a **single** Rademacher column. This is the smallest budget of the original three-part Hutch++ method, which uses three matrix-vector products: \(As\), \(Aq\), and one product on the projected residual probe. For \(\ell>1\), the first two products are retained and only the number of independent residual probes changes.

All signs are independent, each taking \(+1\) or \(-1\) with equal probability. Arithmetic is exact; roundoff and approximate matrix-vector products are not analyzed. The result is a law and variance calculation, not a statement about Hutch++'s asymptotic high-query complexity.

## Proof

Write \(D_s=\operatorname{diag}(s_1,\ldots,s_n)\) and \(p=(\lambda_1,\ldots,\lambda_n)^\top/\sqrt{S_2}\). Because every sketch coordinate is a sign,
\[
q=D_sp,\qquad q^\top A q=\frac{S_3}{S_2}=\mu.
\]
Furthermore \(D_sA=AD_s\) and \(D_s^2=I\). Thus the random deflated matrix is a **sign conjugate** of a fixed matrix:
\[
(I-qq^\top)A(I-qq^\top)
=D_s (I-pp^\top)A(I-pp^\top)D_s.
\]
Conditional on any sketch \(s\), each \(D_s\xi_a\) is again a vector of independent fair signs. Hence the entire conditional output law is the same for every sketch, not merely the first two moments.

Put \(B_0=(I-pp^\top)A(I-pp^\top)\). Expanding the rank-one projections gives
\[
B_0=A-pp^\top A-App^\top+\mu pp^\top.
\]
For a sign vector \(z\), the identity \(z_i^2=1\) gives
\[
z^\top B_0z
=\sum_i\lambda_i
-\frac{2}{S_2}
\Big(\sum_i\lambda_i z_i\Big)
\Big(\sum_i\lambda_i^2z_i\Big)
+\frac{S_3}{S_2^2}
\Big(\sum_i\lambda_i z_i\Big)^2.
\]
Adding \(q^\top A q=\mu\) and averaging the \(\ell\) probes proves the displayed full distribution law.

Since \(\mathbb E(U_aV_a)=S_3\) and \(\mathbb E(U_a^2)=S_2\), its expectation equals \(\sum_i\lambda_i\).

For \(i\ne j\), the off-diagonal entries of the fixed residual matrix are
\[
(B_0)_{ij}=
\frac{\lambda_i\lambda_j}{S_2}
(\mu-\lambda_i-\lambda_j).
\]
For any real symmetric matrix \(B\), a fair-sign quadratic form has exact variance
\[
\operatorname{Var}(z^\top Bz)=4\sum_{i<j}B_{ij}^2,
\]
since the unordered-pair products \(z_iz_j\) are centered and mutually orthogonal in \(L^2\). Independent averaging divides the variance by \(\ell\), which proves the formula.

It is strictly positive: choose any index \(i\) where \(\lambda_i=\max_j\lambda_j\), and another index \(j\ne i\). Because \(\mu\) is a positive-weight average of the \(\lambda_j\) with weights proportional to \(\lambda_j^2\),
\[
\mu\le\lambda_i<\lambda_i+\lambda_j.
\]
Consequently \((B_0)_{ij}\ne0\). In contrast, for ordinary Hutchinson on diagonal \(A\), every sign vector satisfies \(z^\top Az=\sum_i\lambda_i\).

For the isotropic specialization \(\lambda_i=\lambda\), we have \(S_2=n\lambda^2\), \(S_3=n\lambda^3\), \(\mu=\lambda\), and \(V_a=\lambda U_a\). The full law then becomes
\[
\widehat T\overset{d}{=}\lambda(n+1)-\frac{\lambda}{n\ell}\sum_a\big(\sum_i z_{ia}\big)^2.
\]
Writing \(W=\sum_{i=1}^{n}z_i\), independence yields
\[
\mathbb EW^2=n,\qquad
\mathbb EW^4=3n^2-2n,\qquad
\operatorname{Var}(W^2)=2n(n-1).
\]
This proves the isotropic variance formula for every integer \(n\ge2\), not merely by numerical extrapolation. For \(n=2\), \(W^2\) is \(0\) or \(4\) with equal probability, giving the claimed two-point law.

For fixed \(\ell\), each \(n^{-1/2}\sum_i z_{ia}\) converges in distribution to a standard normal random variable as \(n\to\infty\), and the \(\ell\) coordinates remain independent. Applying the continuous mapping theorem to the sum of their squares proves the centered chi-square limit. The exact finite-dimensional variance formula independently gives its limiting variance \(2\lambda^2/\ell\); this is not inferred from weak convergence alone.

## Verification

The included standalone `verify.py` uses exact rational arithmetic to evaluate all sign-sketch and all sign-probe combinations for several nonuniform positive diagonal spectra, compares the full multisets of estimates across sketch realizations, and checks the mean, variance, and weighted-walk identity against the closed forms. It also checks \(\ell=2\) via the full two-probe product distribution on small matrices.

These exhaustive **finite** tests guard the derivation; the analytic proof above handles every permitted dimension and positive diagonal spectrum.

## Relationship to prior work

Meyer, Musco, Musco, and Woodruff introduced Hutch++ with independent Rademacher sketch and residual matrices. Their later variance section analyzes a Gaussian-sketch variant and gives general PSD variance bounds, but it does not supply a rank-one **all-diagonal-spectrum output distribution** or show that sign-sketch randomness is canceled exactly by conjugation.

Persson, Cortinovis, and Kressner restate Hutch++ with Gaussian or Rademacher choices and motivate adaptive allocation when spectral mass is flat. Their paper's **primary MSC 65C05** matches the present trace-estimation subject. Its numerical and Gaussian variance theory does not calculate this exact sign-sketch law.

Gambhir, Stathopoulos, and Orginos already showed that *spectral SVD deflation* can increase Hutchinson variance for Hermitian matrices; in a random-unitary singular-vector model they derived expected variance formulas. The general phenomenon that deflation may harm a sign-probe estimator is therefore **prior**. Their model uses a singular-vector deflation subspace and random unitary coordinates, not the single-column data-dependent **Rademacher** sketch on arbitrary fixed positive diagonal spectra. Their theorem does not imply the sketch-conditional distributional invariance or the bivariate weighted-sign-sum law proved here.

Modern practitioner guidance also observes qualitatively that Rademacher Hutchinson is exact on diagonal matrices and that Hutch++ may add overhead; this observation is **not** claimed as new. The contribution here is the exact full finite-sample law, a variance strictly positive for every positive diagonal spectrum, and a low-budget two-point error law for the algorithm as printed.

Focused searches of published mathematical results for the sign-sketch covariance, rank-one Hutch++ diagonal laws, weighted-sign-sum characterizations, and the isotropic three-query distribution did not locate an implication-equivalent result. Search absence is not a proof of uniqueness.

## Limitations

No claim is made about the recommended large-query regime, general non-diagonal matrices, Gaussian sketches, or non-diagonal coordinate bases. The rank-one result is a sharp low-budget calibration, not an assertion that Hutch++ is generally less accurate than Hutchinson.

Although the exact law gives all distributional properties in principle, no claim is made that every resulting discrete probability is computationally cheap for large arbitrary spectra. The formula is precise, and the support may have exponentially many atoms.

The positive variance on diagonal inputs was anticipated qualitatively by prior trace-estimation discussions; the novel content is the exact sketch-invariant spectral law and its consequences, not the broad warning that deflation can increase variance. Independent assessment of novelty remains outstanding.

## References

1. R. A. Meyer, C. Musco, C. Musco, and D. P. Woodruff, “Hutch++: Optimal Stochastic Trace Estimation,” arXiv:2010.09649, first public version 2020-10-19; SOSA 2021, DOI:10.1137/1.9781611976496.16. Algorithm 1 and variance analysis, §§1 and 5.
2. D. Persson, A. Cortinovis, and D. Kressner, “Improved variants of the Hutch++ algorithm for trace estimation,” arXiv:2109.10659, first public version 2021-09-22; SIAM J. Matrix Anal. Appl. 43 (2022), DOI:10.1137/21M1447623. Primary MSC 65C05; Algorithm 1 and §1.1.
3. A. S. Gambhir, A. Stathopoulos, and K. Orginos, “Deflation as a method of variance reduction for estimating the trace of a matrix inverse,” arXiv:1603.05988, 2016; SIAM J. Sci. Comput. 39 (2017), DOI:10.1137/16M1066361, Theorem 2.6 and discussion of variance increases under spectral deflation.
4. “Trace estimation,” hessian-eigenthings documentation, https://noahgolmant.com/pytorch-hessian-eigenthings/concepts/trace-estimation/ (qualitative discussion of diagonal-Rademacher trace estimation).
