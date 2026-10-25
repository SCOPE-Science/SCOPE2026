# Sharp negative-Ritz risk and universal inverse tails for one-dimensional Gaussian-sketched harmonic Arnoldi

## Finding
Let \(A\) be a real symmetric positive-definite matrix with spectrum in \([\mu,L]\), \(0<\mu<L\), and let \(b\ne0\). With an \(s\times n\) independent standard-real-Gaussian sketch \(S\), \(s\ge1\), the one-dimensional *sketched harmonic* Ritz value is the generalized eigenvalue
\[
 H=\frac{(SAb)^{\mathsf T}(SAb)}{(SAb)^{\mathsf T}(Sb)}.
\]
If \(b\) is not an eigenvector, define
\[
 \alpha=\frac{b^{\mathsf T}Ab}{\|Ab\|^2},\qquad
 \beta=\sqrt{\frac{\|b\|^2}{\|Ab\|^2}-\alpha^2}>0.
\]
With \(T_s\) having Student's \(t\)-law with \(s\) degrees of freedom,
\[
 H\ \stackrel{d}=\ \left(\alpha+\frac{\beta}{\sqrt{s}}T_s\right)^{-1}.
\]
In particular, \(\mathbb E|H|^p<\infty\) **if and only if** \(0<p<1\), for every finite \(s\); all first and higher absolute moments diverge. The exact large-magnitude tail is
\[
 \lim_{z\to\infty}z\Pr(|H|>z)
 =\frac{2\sqrt{s}}{\beta}f_{t_s}\!\left(-\frac{\sqrt{s}\alpha}{\beta}\right)>0.
\]
The probability of a negative sketched harmonic Ritz value obeys the **sharp**, spectrum-only bound
\[
 \Pr(H<0)=F_{t_s}\!\left(-\frac{\sqrt{s}\alpha}{\beta}\right)
 \le F_{t_s}\!\left(-\frac{2\sqrt{s\mu L}}{L-\mu}\right).
\]
Equality is attained in dimension two with \(A=\operatorname{diag}(\mu,L)\) and \(b\) proportional to \((\sqrt{L/\mu},1)^{\mathsf T}\). Consequently, at fixed condition number \(\kappa=L/\mu\), the sharp negative-eigenvalue risk is \(F_{t_s}(-2\sqrt{s\kappa}/(\kappa-1))\). An eigenvector start instead has \(\beta=0\) and \(H\) equal to its positive eigenvalue deterministically.

## Assumptions and scope
Everything is in exact real arithmetic. The sketch is a finite \(s\times n\) matrix with independent standard normal entries, no rejection/embedding-conditioning step; the pencil is evaluated wherever its denominator is nonzero, which occurs almost surely. The generalized sketched-harmonic pencil is \(F=(SAb)^{\mathsf T}(SAb)\), \(G=(SAb)^{\mathsf T}(Sb)\) on the one-vector Krylov basis. The sketch has any finite positive row count \(s\). The two endpoints \(\mu,L\) are permitted spectral bounds; equality in the sharp bound uses both as actual eigenvalues.

## Proof
Write \(u=Ab\), \(v=b\). Each row of \((Su,Sv)\) is a jointly Gaussian vector. Orthogonal Gaussian regression gives
\[
 Sv=\alpha Su+\sqrt{\|v\|^2-\alpha^2\|u\|^2}\,Z,
\]
where the entries of \(Z\) are independent standard normals independent of \(Su\). Thus, denoting \(R=\|Su\|/\|u\|\), we have \(R^2\sim\chi_s^2\), and, conditionally on \(Su\), its unit-direction dot product with \(Z\) is an independent standard normal \(N\). Consequently
\[
 \frac{(Su)^{\mathsf T}(Sv)}{\|Su\|^2}
 =\alpha+\beta\frac{N}{R}
 =\alpha+\frac\beta{\sqrt s}T_s,
\]
proving the exact distribution. The Student density is smooth and strictly positive at every finite real argument. Hence the density of the reciprocal denominator at zero is \((\sqrt s/\beta)f_{t_s}(-\sqrt s\alpha/\beta)>0\). Integrating it over \((-1/z,1/z)\) proves the tail constant. The tail-integration identity \(\mathbb E|H|^p=p\int_0^\infty z^{p-1}\Pr(|H|>z)\,dz\) proves the stated complete moment cutoff. The negative probability equals the displayed Student lower-tail probability because the squared-norm numerator is positive almost surely.

For sharpness, define weights \(w_i=\lambda_i^2 b_i^2/\|Ab\|^2\) in an eigenbasis of \(A\). The positive random variable taking values \(q_i=1/\lambda_i\in[a,c]\), with \(a=1/L\) and \(c=1/\mu\), has mean \(\alpha\) and variance \(\beta^2\). Since \((q-a)(c-q)\ge0\), averaging yields
\[
 \beta^2\le(\alpha-a)(c-\alpha),\qquad
 \frac{\beta^2}{\alpha^2}\le\frac{(c-a)^2}{4ac}=
 \frac{(L-\mu)^2}{4\mu L}.
\]
The middle maximum follows by differentiating over \(\alpha\in[a,c]\), attaining \(\alpha=2ac/(a+c)\). Equality requires endpoint-only support with probabilities \(\Pr(q=c)=a/(a+c)=\mu/(\mu+L)\) and \(\Pr(q=a)=c/(a+c)=L/(\mu+L)\). Choosing the displayed two-dimensional \(b\) realizes exactly those \(\lambda_i^2 b_i^2\)-weights. Since the Student lower tail is strictly increasing and the argument is negative, maximizing \(\beta/\alpha\) gives the claimed sharp probability.

## Verification
The accompanying `verify.py` independently evaluates the one-dimensional generalized Ritz pencil on Gaussian sketches with different row counts and spectral conditions and checks the predicted Student-law negativity frequencies against fixed-seed simulations. It also checks the exact spectral extremizer identities. These finite tests only corroborate the analytic derivation; no finite simulation proves an infinite-moment assertion. Run `python verify.py` with the dependencies in `requirements.txt`.

## Relationship to prior work
Güttel, Liu and Nyman (2026) introduce sketched harmonic Arnoldi for matrix functions, including the generalized pencil \((SAB)^*(SAB)\) against \((SAB)^*(SB)\), and study convergence subject to sketch-quality hypotheses. That positive-real spectral control under a sufficiently accurate subspace embedding is compatible with the rare poor sketches quantified here. Standard Gaussian regression and the Student ratio distribution are background facts, and the bounded-support coefficient-of-variation inequality is elementary; they are not independently claimed as new. The contribution is their joint, sharp application to the rank-one sketched harmonic Ritz pencil, including the moment cutoff and optimally realized condition-number risk. Available source access did not permit a page-by-page check of the complete motivating preprint, so historical priority remains uncertain.

## Limitations
This is a one-dimensional *real-Gaussian* sketched-harmonic pencil with no conditioning on successful subspace embedding. It is not a claim about higher Krylov dimensions, finite precision, the convergence of a restarted matrix-function algorithm, complex sketches, or realizations filtered by an embedding test. An eigenvector start has no heavy tail. The theorem predicts rare-event behavior, not that typical large sketches fail. The closest 2026 primary preprint was available through its abstract and a detailed public methodological account rather than the entire original paper; further source comparison and independent audit remain outstanding.

## References
1. S. Güttel, J. Liu, L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions* (first posted July 11, 2026), arXiv:2607.10354, https://arxiv.org/abs/2607.10354.
2. V. Simoncini, *Stabilized Krylov Subspace Recurrences via Randomized Sketching*, Numerical Linear Algebra with Applications (2025), DOI:10.1002/nla.70022.
3. The Student distribution, conditional multivariate-normal regression, and the elementary bounded-support variance inequality are classical probability facts used here as tools.
