# Sharp dimension-free entropy-production fluctuation frontier for Gaussian endpoints

## Finding

Let \(P\) and \(Q\) be nondegenerate Gaussian probability laws of the same finite dimension \(d\ge 1\). Write
\[
K=D_{\mathrm{KL}}(P\Vert Q),\qquad V=\operatorname{Var}_{P}\!\left(\log\frac{p(X)}{q(X)}\right).
\]
For every \(K>0\), let \(u_-(K)\in(0,1)\) and \(u_+(K)>1\) be the unique solutions of
\[
u-1-\log u=2K.
\]
Then the exact, dimension-independent attainable range at fixed \(K\) is
\[
\boxed{\frac{(1-u_-(K))^2}{2}\ \leq V\leq\ \frac{(u_+(K)-1)^2}{2}.}
\]
Every number in this closed interval is attained in **every** dimension \(d\ge1\). Equality at either boundary, for \(K>0\), is possible only when the Gaussian means coincide and all but one eigenvalue of the relative precision \(\Sigma_P^{1/2}\Sigma_Q^{-1}\Sigma_P^{1/2}\) equal one; its exceptional eigenvalue equals \(u_-(K)\) or \(u_+(K)\), respectively. Conversely, these conditions attain the respective boundaries. For \(K=0\), necessarily \(P=Q\) and \(V=0\).

The roots have the real Lambert-function description
\[
u_-(K)=-W_0(-e^{-1-2K}),\qquad u_+(K)=-W_{-1}(-e^{-1-2K}).
\]
For example, at \(K=1\), the complete attainable variance interval is approximately \([0.4489074056,6.1433589719]\). At \(K=8\), it is approximately \([0.4999999586,180.4146550572]\): fixing the mean mismatch does not fix, or even approximately determine, fluctuation strength.

## Assumptions and scope

Let \(P=N(\mu,\Sigma_P)\), \(Q=N(\nu,\Sigma_Q)\) on \(\mathbb R^d\), where \(d\in\mathbb N\), \(d\ge1\), \(\mu,\nu\in\mathbb R^d\), and both covariance matrices are real symmetric positive definite. Densities are normalized relative to Lebesgue measure and logarithms are natural. No bounds are imposed on covariance condition numbers, but they must be strictly positive definite. Relative entropy variance uses expectation and variance under \(P\), not \(Q\). The optimization is over all such Gaussian pairs with the prescribed \(K\).

A thermodynamic interpretation is available in the exact-score-field, infinite-forward-time regime of Ding, Quan and Tu [1], where the time-asymmetry entropy production satisfies \(\Delta s_{\mathrm{ta}}=k_B\log(p(X)/q(X))\), \(X\sim P\). Therefore the physically dimensioned bounds are obtained by multiplying \(K\) by \(k_B\) for the mean, and the displayed variance endpoints by \(k_B^2\). This interpretation is conditional on the hypotheses of [1]; it is not asserted for arbitrary finite-time or imperfectly trained diffusion models.

## Proof

**Step 1: Gaussian reduction and exact moments.** Affine changes of the common observation coordinate preserve the likelihood ratio, the relative entropy and its variance. Whiten \(P\) to \(N(0,I_d)\) and orthogonally diagonalize the whitened precision of \(Q\). Write its eigenvalues \(u_1,\ldots,u_d>0\) and the coordinates of the transformed mean of \(Q\) as \(m_1,\ldots,m_d\). Under \(P\), the coordinates \(Z_i\) are independent standard normals, and the log density ratio, up to a nonrandom constant, is
\[
\sum_{i=1}^d\left[\frac{u_i-1}{2}Z_i^2-u_im_iZ_i\right].
\]
The Gaussian identities \(\operatorname{Var}(Z_i^2)=2\), \(\operatorname{Var}(Z_i)=1\), and \(\operatorname{Cov}(Z_i,Z_i^2)=0\) imply, with \(h(u)=u-1-\log u\),
\[
K=\sum_{i=1}^d k_i,\quad k_i=\frac{h(u_i)+u_im_i^2}{2}\ge0;
\qquad V=\sum_{i=1}^d v_i,\quad v_i=\frac{(u_i-1)^2}{2}+u_i^2m_i^2.
\]
The inequality \(h(u)\ge0\), with equality precisely at \(u=1\), proves \(k_i\ge0\) and that \(k_i=0\) means \(u_i=1\), \(m_i=0\).

**Step 2: Exact one-coordinate interval.** Fix \(k>0\) and one coordinate. Feasibility is precisely
\[
h(u)\le2k,\qquad m^2=\frac{2k-h(u)}{u},
\]
so \(u\) varies through the compact interval \([u_-(k),u_+(k)]\). Eliminating the mean gives
\[
v(u;k)=\frac{(u-1)^2}{2}+u(2k-h(u))
=\frac{1-u^2}{2}+2ku+u\log u.
\]
Differentiation at fixed \(k\) yields
\[
\frac{\partial v}{\partial u}=2k-h(u)\ge0,
\]
strictly inside the interval. Thus the full one-coordinate range is exactly
\[
[f_-(k),f_+(k)],\qquad f_\pm(k)=\frac{(u_\pm(k)-1)^2}{2}.
\]
The endpoints require \(m=0\). Every interior variance is attained by a real mean chosen using the displayed expression for \(m^2\); both signs work.

**Step 3: Allocation over all coordinates.** Implicitly differentiating \(h(u_\pm(k))=2k\) gives \(u_\pm'(k)=2u_\pm/(u_\pm-1)\). Consequently
\[
f_\pm'(k)=2u_\pm(k),\qquad
f_\pm''(k)=\frac{4u_\pm(k)}{u_\pm(k)-1}.
\]
Hence \(f_-\) is strictly concave and increasing, while \(f_+\) is strictly convex and increasing for positive \(k\); both extend continuously by \(f_\pm(0)=0\). For nonnegative \(a,b\), these properties yield
\[
f_-(a)+f_-(b)\ge f_-(a+b),\qquad
f_+(a)+f_+(b)\le f_+(a+b),
\]
with strictness when both \(a,b>0\). The inequalities follow also by integrating the decreasing/increasing first derivatives from zero. Applying them repeatedly to the nonnegative \(k_i\), and using Step 2, proves
\[
f_-(K)\le\sum_i f_-(k_i)\le\sum_i v_i\le\sum_i f_+(k_i)\le f_+(K).
\]
If equality holds and \(K>0\), exactly one \(k_i\) can be positive (by strict concavity/convexity), and the associated mean must be zero (Step 2). All remaining coordinates have \(u_i=1\) and \(m_i=0\). This proves both necessary and sufficient equality conditions, independently of dimension and of the original covariance eigenbasis.

**Step 4: No gaps in the attainable range.** Fix the given \(K>0\). Set all but one whitened coordinate to \(u_i=1\), \(m_i=0\). Let the remaining precision eigenvalue vary continuously between \(u_-(K)\) and \(u_+(K)\), choosing \(m^2=[2K-h(u)]/u\ge0\). The entropy stays exactly \(K\), while the variance is the continuous, strictly increasing function \(v(u;K)\) from Step 2. Its image is the entire interval \([f_-(K),f_+(K)]\). For \(K=0\), the zero-sum formula forces every \(k_i=0\), hence \(P=Q\) and \(V=0\). This completes the proof.

## Verification

A standalone checker, `verify.py`, reproduces the implicit roots, the frontier, the one-coordinate interpolation, and the exact multivariate moment formula. It performs 1,585 numerical assertions with deterministic sampling, including independent sample-based evaluations of Gaussian log-density ratios in dimensions one through four. These tests are supporting consistency checks; Steps 1–4 constitute the proof for arbitrary positive-definite covariance matrices and every finite dimension. The script is run with `python verify.py` after installing the ordinary dependencies in `requirements.txt`. Its output includes the numerical intervals above. The checker is not a claim of exhaustive numerical enumeration.

## Relationship to prior work

Ding, Quan and Tu [1], Section 3.3, equations (39)–(40) and Supplement III–IV, identify the terminal relative entropy and relative entropy variance as the mean and variance of time-asymmetry entropy production in the precise exact-score, infinite-time regime. They motivate fixed-mean fluctuation comparisons, but their paper and supplementary variance theorem do not state the above sharp, dimension-free Gaussian feasible interval, its equality conditions or complete attainability.

Zhang et al. [2], Section 4 and supplemental proofs, established dimension-independent, Lambert-function bounds on **reverse relative entropy** given forward relative entropy for Gaussian pairs, including rank-one covariance extremizers. That is a closely related but distinct optimization: the objective is \(D_{\mathrm{KL}}(Q\Vert P)\), not \(\operatorname{Var}_P\log(p/q)\). Their theorem does not directly give the displayed extrema or complete variance range at fixed forward entropy. The spectral-allocation technique is classical, and overlap with general Gaussian divergence calculus is a residual originality risk; no novelty is claimed for Lambert functions, the Gaussian KL formula or Gaussian whitening separately.

The standard explicit Gaussian relative entropy formula and the terminology of relative entropy variance are established prior knowledge [2,3]. The distinct assessed claim is the complete fixed-forward-entropy interval for **log-likelihood-ratio variance**, with sharp equality rigidity and one-mode attainability, together with its conditional physical interpretation.

## Limitations

The theorem is about full-rank Gaussian pairs and the endpoint likelihood-ratio law, not mixtures, heavy-tailed distributions, singular covariance matrices or complete time-resolved path entropy production. It gives possible population variances rather than finite-sample confidence bounds. The endpoints can demand very small or very large relative covariance eigenvalues; no uniform conditioning or implementability guarantee is implied. Every statement about thermodynamic entropy production beyond the mathematical \((K,V)\) relationship requires the explicit assumptions of [1]. Independent peer audit has not been performed.

## References

[1] X. Ding, H. T. Quan and Y. Tu, *Stochastic Thermodynamics of Score Matching in Diffusion Models*, arXiv:2606.17252v1, first posted 2026-06-15. https://arxiv.org/html/2606.17252v1 (main Sections 3.3, 4.1, Supplement III–IV).

[2] Y. Zhang, J. Pan, K. Li et al., *On the Properties of Kullback-Leibler Divergence Between Multivariate Gaussian Distributions*, NeurIPS 36 (2023). https://proceedings.neurips.cc/paper_files/paper/2023/file/b5b4d92374323c53c24bbbc8ee0e715c-Paper-Conference.pdf and https://proceedings.neurips.cc/paper_files/paper/2023/file/b5b4d92374323c53c24bbbc8ee0e715c-Supplemental-Conference.pdf.

[3] *Kullback–Leibler divergence for the multivariate normal distribution*, The Book of Statistical Proofs. https://statproofbook.github.io/P/mvn-kl.html.
