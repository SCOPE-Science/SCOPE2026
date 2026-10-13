# Degree-weighted critical regularity for Kirchhoff vertex noise on metric graphs

## Finding
Let \(\Gamma\) be a finite connected compact metric graph with at least one edge, positive edge lengths, and standard continuity and Kirchhoff conditions. Write \(H=I-\Delta_\Gamma\), where \(-\Delta_\Gamma\) is the nonnegative Kirchhoff Laplacian. At the vertices introduce additive real Brownian flux noise with a fixed, nonzero, symmetric positive-semidefinite covariance matrix \(Q\). Denote its zero-initial-data stochastic heat convolution by \(X_t\) (defined precisely below), and put
\[
\mathcal S_\Gamma(Q)=\sum_{v\in V(\Gamma)}\frac{Q_{vv}}{\deg(v)}>0.
\]
For every fixed \(t>0\), and every real \(\alpha\), the fractional-domain membership is **sharp**:
\[
\mathbb P\bigl(X_t\in D(H^\alpha)\bigr)=
\begin{cases}1,&\alpha<\tfrac14,\\0,&\alpha\geq\tfrac14.\end{cases}
\]
If \(P_\Lambda=\mathbf{1}_{[1,\Lambda]}(H)\), the cutoff energy has an exact logarithmic coefficient,
\[
\mathbb E\|H^{1/4}P_\Lambda X_t\|_{L^2(\Gamma)}^2
=\frac{\mathcal S_\Gamma(Q)}{2\pi}\log\Lambda+o(\log\Lambda)
\quad(\Lambda\to\infty).
\]
For every \(\alpha>1/4\), the stronger power-law divergence holds:
\[
\mathbb E\|H^\alpha P_\Lambda X_t\|^2
\sim\frac{\mathcal S_\Gamma(Q)}{\pi(4\alpha-1)}\Lambda^{2\alpha-1/2}.
\]
The same invariant determines the initial stochastic energy:
\[
\mathbb E\|X_t\|^2
=\frac{\mathcal S_\Gamma(Q)}2\operatorname{erf}(\sqrt{2t})
+O(e^{-c/t}),\qquad t\downarrow0,
\]
where \(c>0\) can depend on the metric graph. In particular \(\mathbb E\|X_t\|^2\sim\mathcal S_\Gamma(Q)\sqrt{2t/\pi}\). Correlations between distinct vertices do not change these leading coefficients.

## Assumptions and scope
The graph has finitely many distinct vertices and finitely many compact edges, each of strictly positive length. For simplicity loops and parallel edges are excluded; the heat-kernel proof also applies when degrees count incident edge ends. The Laplacian has Kirchhoff–Neumann matching at every vertex, with no potential or nonstandard coupling. The covariance \(Q=(Q_{vw})\) is real, constant in time, symmetric, positive semidefinite and nonzero; rank-deficient and correlated noise is allowed. Brownian motion \(W\) has \(\mathbb E[dW_v(t)dW_w(t)]=Q_{vw}\,dt\).

Let \((\mu_j,\varphi_j)\) be the eigenpairs of \(H\) with eigenvalues listed with multiplicity and a real orthonormal basis of \(L^2(\Gamma)\). For each \(j\) define \(b_j=(\varphi_j(v))_{v\in V}\) and \(a_j=b_j^\top Qb_j\geq0\). The white-flux stochastic convolution means the \(L^2(\Gamma)\)-valued Gaussian series with coordinates
\[
\langle X_t,\varphi_j\rangle=\int_0^t e^{-(t-s)\mu_j}\sum_v\varphi_j(v)\,dW_v(s).
\]
Equivalently, \(X_t=\int_0^t e^{-(t-s)H}B\,dW(s)\), where \(B\) is the distributional vertex trace adjoint, \(\langle Bf,\psi\rangle=\sum_v f_v\psi(v)\); the sign of the flux convention is immaterial for the covariance. This is an additive linear Kirchhoff flux-noise model, not independent noise in edge interiors or random continuity constraints. Domain \(D(H^\alpha)\) is equipped with the spectral graph norm; \(H\geq I\) makes negative powers harmless.

## Proof
**1. Local heat kernel and positive covariance measure.** For the Kirchhoff heat kernel \(K_s\), the standard metric-graph walk expansion (Borthwick–Harrell–Jones, Proposition 2.1) assigns the trivial path from \(v\) to itself coefficient \(2/\deg(v)\). Because every nontrivial vertex-to-vertex walk has positive length, the finite graph and positive minimum edge length imply, as \(s\downarrow0\),
\[
K_s(v,w)=\frac{\mathbf1_{v=w}}{\deg(v)\sqrt{\pi s}}+O(s^{-1/2}e^{-c_0/s})
\]
for some \(c_0>0\), uniformly across the finitely many vertex pairs. The shifted heat kernel of \(H\) is \(e^{-s}K_s\). Taking its vertex covariance trace gives
\[
F(s):=\sum_j a_j e^{-s\mu_j}
=\sum_{v,w}Q_{vw}e^{-s}K_s(v,w)
=\frac{\mathcal S_\Gamma(Q)e^{-s}}{\sqrt{\pi s}}+O(s^{-1/2}e^{-c_0/s}).
\]
Here \(a_j\geq0\) because \(Q\) is positive semidefinite. Also \(\mathcal S_\Gamma(Q)>0\): a nonzero positive-semidefinite matrix has a positive diagonal entry.

**2. Weighted local Weyl law.** The Karamata Tauberian theorem for the nonnegative discrete measure \(\sum_j a_j\delta_{\mu_j}\), applied to the preceding Laplace-transform asymptotic, gives
\[
N_Q(\Lambda):=\sum_{\mu_j\leq\Lambda}a_j
\sim\frac{2\mathcal S_\Gamma(Q)}\pi\sqrt\Lambda.
\]
Indeed \(\Gamma(3/2)=\sqrt\pi/2\) converts the heat coefficient \(\mathcal S/\sqrt\pi\) into \(2\mathcal S/\pi\). This is basis-independent even at degenerate eigenvalues. The diagonal scalar local Weyl law is already known; the covariance-weighted measure and its use below are the pertinent combination.

**3. Exact Gaussian variances and spectral divergence.** By Itô isometry, for each \(t>0\),
\[
\mathbb E\|H^\alpha P_\Lambda X_t\|^2
=\frac12\sum_{\mu_j\leq\Lambda}a_j\mu_j^{2\alpha-1}\bigl(1-e^{-2t\mu_j}\bigr).
\]
At high energy the exponential term has finite total contribution. Abel/partial summation from the weighted Weyl law yields, at \(\alpha=1/4\), the coefficient \((1/2)\cdot(\mathcal S/\pi)\log\Lambda\). At \(\alpha>1/4\), integrating \(\mu^{2\alpha-1}\) against \(dN_Q(\mu)\) yields the stated \(\mathcal S/[\pi(4\alpha-1)]\) coefficient and exponent. At \(\alpha<1/4\), the same comparison shows finite variance, so \(X_t\in D(H^\alpha)\) almost surely. In particular at \(\alpha=0\), the series defines a genuine \(L^2\)-valued convolution.

**4. Necessity holds almost surely, not merely in mean square.** The subset \(D(H^\alpha)\subset L^2(\Gamma)\) is a measurable linear subspace, defined by convergence of nonnegative partial spectral sums. For a centered Gaussian measure every measurable linear subspace has probability zero or one. If \(X_t\) belonged to this subspace with probability one, its induced centered Gaussian measure on the separable Hilbert space \(D(H^\alpha)\) would have finite squared-norm expectation by Fernique's theorem. This contradicts the divergent Itô series for \(\alpha\geq1/4\). Thus its probability is zero.

**5. Small-time energy.** Another application of Itô isometry and Tonelli gives
\[
\mathbb E\|X_t\|^2=\int_0^tF(2s)\,ds.
\]
The zero-length paths contribute exactly
\[
\int_0^t\frac{\mathcal S e^{-2s}}{\sqrt{2\pi s}}\,ds
=\frac{\mathcal S}2\operatorname{erf}(\sqrt{2t}).
\]
The sum of all positive-length paths contributes at most \(O(e^{-c/t})\) after integration (possibly with a smaller \(c>0\)). This proves the claimed expansion. The cross-correlations \(Q_{vw}\) for \(v\ne w\) affect only these exponentially small short-time corrections, although they may affect the finite spectral energy.

## Verification
The standalone `verify.py` checks a positive-definite correlated two-vertex covariance, the exact Neumann-interval vertex weights by parity, the central-vertex factor of an equal-arm star, and the high-frequency logarithmic slope between two spectral cutoffs. Running `python3 verify.py` returns `VERIFY_OK`. The check's graph is the Neumann interval of length \(\pi\), with covariance \(Q=\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}\), so \(\mathcal S=5\) and the predicted logarithmic coefficient is \(5/(2\pi)\). The exact eigenfunction values give the squared-weight sequence \(a_n=2(5+2(-1)^n)/\pi\) for \(n\geq1\), making correlated cancellation explicit.

All uniform-in-graph and all-eigenvalue statements are proved analytically through the heat-kernel path expansion and Tauberian argument; finite tests corroborate normalization only. Standard Gaussian-measure results are invoked for almost-sure non-membership.

## Relationship to prior work
Kovács and Sikolya, arXiv:2207.01944, Theorem 3.8, establish fractional-domain continuous-path regularity below \(\alpha=1/4\) for Kirchhoff vertex noise under a uniform eigenfunction vertex-trace hypothesis. Their theorem does not assert the almost-sure endpoint obstruction or the covariance- and degree-dependent ultraviolet coefficient. Borthwick, Harrell and Jones, arXiv:2204.06619, Proposition 2.1, Proposition 3.1, and Theorem 4.1, establish the required deterministic metric-graph heat-kernel path expansion and local Weyl law; these input facts are **not** new here. Kostrykin, Potthoff and Schrader, arXiv:math-ph/0701009, give earlier heat-kernel walk formulas. The assessed conclusion is their use with the vertex-noise Itô covariance to determine exact regularity, leading coefficient, and short-time stochastic energy for all nonzero correlated vertex covariances.

## Limitations
The theorem is for the linear additive vertex-flux problem with uniform scalar edge diffusion, Kirchhoff matching, and a fixed nonzero positive-semidefinite covariance. It does not cover simultaneously noisy continuity conditions, time-dependent or colored covariance, arbitrary edge potentials, nonlinear stochastic equations, or noncompact networks. Membership is asserted at each fixed \(t>0\), not simultaneously for all times or as a path-continuity statement in every subcritical space. The coefficient depends on normalization of the Laplacian, the semigroup, and Brownian covariance exactly as specified. The asymptotics do not determine the finite constant after removing the critical logarithm. The combination may have an equivalent formulation in literature not retrieved by the searches; the underlying heat-kernel asymptotic is established prior work.

## References
1. M. Kovács and E. Sikolya, *On the parabolic Cauchy problem for quantum graphs with vertex noise*, arXiv:2207.01944, version 2, especially Section 3 and Theorem 3.8. First public preprint: 2022-07-05. https://arxiv.org/pdf/2207.01944
2. D. Borthwick, E. M. Harrell II and K. Jones, *The heat kernel on the diagonal for a compact metric graph*, arXiv:2204.06619, especially Proposition 2.1, Proposition 3.1, and Theorem 4.1. https://arxiv.org/pdf/2204.06619
3. V. Kostrykin, J. Potthoff and R. Schrader, *Heat kernels on metric graphs and a trace formula*, arXiv:math-ph/0701009. https://arxiv.org/pdf/math-ph/0701009
4. Classical Karamata Tauberian theorem for Laplace transforms of positive measures and Fernique's Gaussian integrability theorem (used in their standard forms).
