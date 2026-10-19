# Correlation phase boundary and sharp high-anisotropy crossover for one-probe Gaussian range finding

## Finding
For every real \(a>b>0\), \(c_1,c_2>0\), and \(-1\leq\rho\leq1\), set
\[
A=\operatorname{diag}(a,b),\qquad
C_\rho=\begin{pmatrix}c_1&\rho\sqrt{c_1c_2}\\\rho\sqrt{c_1c_2}&c_2\end{pmatrix}.
\]
Draw one zero-mean Gaussian probe \(g\) with covariance \(C_\rho\), form \(z=Ag\) and its rank-one orthogonal projector \(P_z=zz^{\mathsf T}/(z^{\mathsf T}z)\), and approximate \(A\) by \(P_z A\). With \(d=ab\sqrt{c_1c_2}\sqrt{1-\rho^2}\), the **expected squared Frobenius error** is exactly
\[
\mathcal R(\rho):=\mathbb E\|(I-P_z)A\|_F^2
=\frac{a^2b^2(c_1+c_2)+(a^2+b^2)d}{a^2c_1+b^2c_2+2d}.
\tag{1}
\]
At fixed marginal probe variances, correlation magnitude \(|\rho|\) strictly improves, strictly worsens, or does not change expected performance according as \(a^2c_1>b^2c_2\), \(a^2c_1<b^2c_2\), or \(a^2c_1=b^2c_2\). Equivalently, the minimum over \(|\rho|\leq1\) is attained only at \(|\rho|=1\) in the first case, only at \(\rho=0\) in the second case, and at every \(\rho\) in the balanced case. For \(|\rho|<1\), the first two improvements are strict; the singular endpoints are valid by continuity and by the Gaussian definition below.

In the standardized case \(c_1=c_2=b=1\), writing \(a=\kappa>1\), \(\delta=\sqrt{1-\rho^2}\), equation (1) simplifies to
\[
\mathcal R_\kappa(\rho)
=\frac{2\kappa^2+(\kappa^2+1)\kappa\delta}
{\kappa^2+1+2\kappa\delta}
=\kappa\delta+\frac{2\kappa^2\rho^2}{\kappa^2+1+2\kappa\delta}.
\tag{2}
\]
Thus uncorrelated sampling has \(\mathcal R_\kappa(0)=\kappa\), while maximally correlated sampling has \(\mathcal R_\kappa(\pm1)=2\kappa^2/(\kappa^2+1)\). For every sequence \(\kappa\to\infty\), the errors \(\mathcal R_\kappa(\rho_\kappa)\) remain bounded **if and only if** \(\kappa\sqrt{1-\rho_\kappa^2}=O(1)\). In the critical regime \(\kappa\sqrt{1-\rho_\kappa^2}\to\tau\in[0,\infty)\),
\[
\mathcal R_\kappa(\rho_\kappa)\longrightarrow 2+\tau.
\tag{3}
\]

## Assumptions and scope
The matrix \(A\) is a real \(2\times2\) diagonal matrix of positive, unequal singular values; the sketch consists of exactly **one** real Gaussian vector, without oversampling, power iterations, or post-sketch regularization. Gaussian covariance \(C_\rho\) is positive definite for \(|\rho|<1\). At \(|\rho|=1\), it has rank one but \(z\ne0\) almost surely because both marginal variances are positive; the projection is therefore well-defined almost surely. The loss is \(\mathbb E\|(I-P_z)A\|_F^2\), not \((\mathbb E\|(I-P_z)A\|_F)^2\) and not a nuclear or spectral approximation error. The sign of \(\rho\) is immaterial for the diagonal \(A\) and this loss. No claim is made for non-Gaussian probes or higher dimensional matrices.

## Proof
**Step 1: an exact planar Gaussian projector moment.** Let \(z\sim N(0,K)\) in \(\mathbb R^2\) with \(K\) positive definite. Orthogonally diagonalize \(K\), with eigenvalues \(\lambda_1,\lambda_2>0\). Polar decomposition of two independent standard Gaussian coordinates gives a uniformly distributed angle \(\theta\) and
\[
\mathbb E\frac{z_1^2}{z_1^2+z_2^2}
=\frac{2}{\pi}\int_0^{\pi/2}\frac{\lambda_1\cos^2\theta}{\lambda_1\cos^2\theta+\lambda_2\sin^2\theta}\,d\theta
=\frac{\sqrt{\lambda_1}}{\sqrt{\lambda_1}+\sqrt{\lambda_2}}.
\]
The last integral follows on putting \(t=\tan\theta\), partially fractioning \(\lambda_1/[(1+t^2)(\lambda_1+\lambda_2t^2)]\), and integrating over \(t\in[0,\infty)\). The expected off-diagonal entries vanish by odd symmetry. Transforming back to the original basis yields
\[
\mathbb E P_z=\frac{K^{1/2}}{\operatorname{tr}K^{1/2}}.
\tag{4}
\]
For every positive definite real \(2\times2\) matrix, its characteristic equation gives
\[
\frac{K^{1/2}}{\operatorname{tr}K^{1/2}}
=\frac{K+\sqrt{\det K}\,I_2}{\operatorname{tr}K+2\sqrt{\det K}}.
\tag{5}
\]
Indeed, if \(s=\sqrt{\det K}\), Cayley–Hamilton implies \((K+sI)^2=(\operatorname{tr}K+2s)K\); taking traces of the resulting positive square root proves (5). Both identities extend continuously to positive-semidefinite rank-one \(K\ne0\), for which \(z\) is confined to its nonzero range.

**Step 2: exact expected loss.** In the theorem, \(K=AC_\rho A\), so
\[
\operatorname{tr}K=a^2c_1+b^2c_2,\quad
\sqrt{\det K}=d,\quad
\operatorname{tr}(A^2K)=a^4c_1+b^4c_2.
\]
Orthogonality and idempotence of \(P_z\) give
\[
\|(I-P_z)A\|_F^2=\operatorname{tr}(A^2)-\operatorname{tr}(A^2P_z).
\]
Substituting (5) yields
\[
\mathcal R(\rho)=a^2+b^2-
\frac{a^4c_1+b^4c_2+d(a^2+b^2)}{a^2c_1+b^2c_2+2d},
\]
which simplifies to equation (1). No integrability issue arises: the squared error is bounded between \(b^2\) and \(a^2\) almost surely.

**Step 3: complete correlation optimization.** Treating the right-hand side of (1) as a function \(R(d)\) on \([0,ab\sqrt{c_1c_2}]\), direct differentiation and exact factorization give
\[
R'(d)=\frac{(a^2-b^2)(a^2c_1-b^2c_2)}{(a^2c_1+b^2c_2+2d)^2}.
\tag{6}
\]
Since \(d\) is strictly decreasing in \(|\rho|\in[0,1]\), the sign in (6) proves all three alternatives, including the unique minimizers and the balanced equality case. Every covariance with the prescribed two diagonal variances and positive-semidefinite constraint occurs for precisely such a \(\rho\).

**Step 4: the sharp singular-anisotropy crossover.** Put \(a=\kappa\), \(b=c_1=c_2=1\) in (1). Elementary algebra yields both forms in (2). The second term in (2) is nonnegative, so bounded error implies bounded \(\kappa\delta\). Conversely, it is at most \(2\kappa^2/(\kappa^2+1)\le2\), proving boundedness whenever \(\kappa\delta\) is bounded. If \(\kappa\delta\to\tau<\infty\), then \(\delta\to0\), \(\rho^2\to1\), and the second term tends to \(2\); this gives (3). Substitution \(\rho=0,\pm1\) gives the stated endpoint values.

## Verification
The complete standalone \(\texttt{verify.py}\) requires only Python's standard library. It checks the rational derivative factorization and squared-error bounds, evaluates the same expectation by an independent uniform-angle quadrature, tests improvement and deterioration examples and the balanced case, checks equation (2), and exercises convergence of the critical scaling (3). The recorded run reports **935 deterministic checks passed**. It does not substitute finite tests for the all-parameter proof, and the critical scaling is established analytically by Step 4. Reproduce using \(\texttt{python3 verify.py}\); the recorded output is in \(\texttt{verification_output.txt}\).

## Relationship to prior work
Scotto Di Perrotolo, Diouane, Gürol, and Vasseur analyze randomized range finding with non-standard Gaussian covariance; their 2024 preprint motivates precise dependence on the covariance, and its Theorems 3.1–3.2 give general **bounds on the unsquared Frobenius error** when the sample count is at least target rank plus two. The present exact squared-error and covariance-correlation optimization instead concern the excluded one-sample regime. Boullé and Townsend likewise analyze covariance-informed Gaussian randomized SVD, with a theorem using at least four oversampling vectors; their results do not provide (1), (6), or (3). Halko, Martinsson, and Tropp supply the classical iid-Gaussian range-finding framework.

An additional exact reduction is worth separating from the claimed extension: for \(B=A^2\), the rank-one Nyström residual of \(B\) with the same probe \(g\) has trace exactly equal to \(\|(I-P_{Ag})A\|_F^2\). Thus existing iid-Gaussian two-eigenvalue Nyström expectation formulas already imply the \(ho=0\), \(c_1=c_2\) specialization. They do not by themselves classify covariance correlations at fixed marginals or establish the coupled \(\kappa,ho\) limit.

The angular central Gaussian law, including its covariance-parametrized directional density, predates these algorithms and is not claimed as new; the planar projector moment is derived here to make the calculation self-contained. The uncorrelated specialization \(\mathcal R_\kappa(0)=\kappa\) is an elementary pre-existing Gaussian-ratio case and is not the proposed novelty. The substantive statements assessed here are the **full fixed-marginal correlation-sign classification** and its **sharp high-anisotropy correlation crossover** for the numerical approximation error.

## Limitations
Only one-probe, diagonal real \(2\times2\) range finding under centered Gaussian sampling is treated. Changing covariance marginals, allowing arbitrary rotated singular bases, increasing sketch rank, measuring a different error, or using postprocessed/regularized approximants can change the optimization. Correlation \(|\rho|=1\) is a singular, rather than full-rank, sketch covariance; the theorem nonetheless includes this exact mathematical endpoint. The high-anisotropy limit is sequential and does not imply a practical floating-point reliability bound. Generic angular Gaussian identities and prior analyses can imply components of the calculation; priority for the *combined correlation design and crossover statement* remains subject to further literature discovery.

## References
1. A. Scotto Di Perrotolo, Y. Diouane, S. Gürol, X. Vasseur, *A general error analysis for randomized low-rank approximation with application to data assimilation*, arXiv:2405.04811, first posted 2024-05-08; revised under the title *A unified error analysis for randomized low-rank approximation with application to data assimilation*. https://arxiv.org/abs/2405.04811 ; HTML of revised version: https://arxiv.org/html/2405.04811v2 .
2. N. Boullé, A. Townsend, *A generalization of the randomized singular value decomposition*, arXiv:2105.13052, 2021. https://arxiv.org/html/2105.13052v3 .
3. N. Halko, P.-G. Martinsson, J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, arXiv:0909.4061, 2009. https://arxiv.org/html/0909.4061v2 .
4. D. E. Tyler, *Statistical analysis for the angular central Gaussian distribution on the sphere*, Biometrika 74 (1987), 579–589. https://doi.org/10.1093/biomet/74.3.579 .
