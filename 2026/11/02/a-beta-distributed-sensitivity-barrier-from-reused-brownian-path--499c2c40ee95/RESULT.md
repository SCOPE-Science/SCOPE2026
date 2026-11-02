# A Beta-distributed sensitivity barrier from reused Brownian paths

## Finding

In an exactly rank-one derivative-informed dimension-reduction problem, reusing a pool of \(\ell\) Brownian paths across arbitrarily many outer drift samples can confine the estimated sensitivity eigenspace to a random \(\ell\)-plane. For the explicit scalar-threshold observable below, this gives an exact Beta-distributed alignment barrier and an exact positive lower bound on the best one-dimensional surrogate error. In the one-path case, the centered martingale control-variate estimator is independent of every outer drift sample.

Let \(d\geq2\), \(1\leq\ell<d\), and \(m\geq1\). Let \(e_d\) denote the final coordinate unit vector. Consider the constant-drift diffusion on \([0,1]\)
\[
\mathrm dX_t^u=u\,\mathrm dt+\mathrm dW_t,\qquad X_0^u=0,\qquad u\in\mathbb R^d,
\]
with a standard \(d\)-dimensional Brownian motion. The bounded terminal observable is \(H(X^u)=\mathbf1_{\{X^u_{1,d}>0\}}\) and \(F(u)=\mathbb E[H(X^u)]\). The drift prior is \(U\sim N(0,I_d)\).

Draw \(Z_1,\dots,Z_\ell\) independently from \(N(0,I_d)\), and **reuse these same vectors for every outer draw** \(U^{(1)},\dots,U^{(m)}\), which are independently sampled from the prior. Define the centered score estimator and its outer-product matrix by
\[
\widehat g_\ell(u)=\frac1\ell\sum_{i=1}^\ell
\left(\mathbf1_{\{u_d+Z_{i,d}>0\}}-\frac12\right)Z_i,
\qquad
\widehat K_{\ell,m}=\frac1m\sum_{j=1}^m
\widehat g_\ell(U^{(j)})\widehat g_\ell(U^{(j)})^\top.
\]
The exact sensitivity matrix is
\[
K=\mathbb E_U[\nabla F(U)\nabla F(U)^\top]
=\frac{1}{2\pi\sqrt3}\,e_de_d^\top.
\]
Set \(S_\ell=\operatorname{span}(Z_1,\dots,Z_\ell)\) and \(P_\ell=\|\Pi_{S_\ell}e_d\|^2\). With probability one, \(\widehat K_{\ell,m}\ne0\) and every unit eigenvector \(v\) for a positive eigenvalue of \(\widehat K_{\ell,m}\) obeys
\[
|v^\top e_d|^2\le P_\ell,
\qquad P_\ell\sim\operatorname{Beta}\!\left(\frac\ell2,\frac{d-\ell}2\right),
\qquad \mathbb E[P_\ell]=\frac\ell d.
\]
In particular, \(\mathbb E[\sin^2\angle(v,e_d)]\ge1-\ell/d\) for every number \(m\) of outer samples, with the expectation over all training randomness.

Let \(U^*\sim N(0,I_d)\) be a **fresh**, independent drift. The smallest possible mean-square prediction error among all one-dimensional ridge predictors whose direction lies in the shared-path span is exactly
\[
\begin{aligned}
\mathcal R(S_\ell)
&=\inf_{\substack{v\in S_\ell,\;\|v\|=1\\h\in L^2(N(0,1))}}
\mathbb E_{U^*}\!\left[(F(U^*)-h(v^\top U^*))^2\mid S_\ell\right]\\
&=\frac1{12}-\frac1{2\pi}\arcsin\!\left(\frac{P_\ell}{2}\right)
\ge\frac{1-P_\ell}{12}>0\quad\text{almost surely},
\end{aligned}
\]
so \(\mathbb E[\mathcal R(S_\ell)]\ge(1-\ell/d)/12\). The exact first equality is attained by the normalized projection of \(e_d\) onto \(S_\ell\) and its Gaussian conditional-expectation predictor. The linear lower bound need not be attained. For \(\ell=1\), the estimated matrix itself is the deterministic function of the reused draw
\[
\widehat K_{1,m}=\frac14Z_1Z_1^\top
\quad\text{for every }m\ge1,
\]
and its unique positive-eigenvalue eigendirection realizes \(\mathcal R(S_1)\), regardless of the outer samples.

## Assumptions and scope

The state dimension and parameter dimension are the same \(d\), the diffusion matrix is the identity, the drift is spatially constant, the observation horizon is one, and the payoff is the final-coordinate threshold at zero. The drift prior is isotropic Gaussian. All Brownian endpoint vectors are independent of one another and of the outer drift samples, but are **not** regenerated across outer samples. The scalar score control coefficient is fixed at \(-1/2\). Gaussian conditional-expectation risks always refer to a new, independent input \(U^*\), not a training sample. All eigenvectors asserted above correspond to positive eigenvalues; zero-eigenvalue nullspace vectors are excluded.

This is a finite-dimensional constant-drift specialization of path-measure score differentiation and derivative-informed sensitivity, not a claim about arbitrary spatially varying drift fields, time-discretization errors, or the finite-element discretization in the motivating source.

## Proof

**1. Exact sensitivity.** The terminal state is \(X_1^u=u+Z\) with \(Z\sim N(0,I_d)\). Writing \(\Phi\) and \(\phi\) for the standard normal distribution and density, respectively, gives \(F(u)=\Phi(u_d)\) and \(\nabla F(u)=\phi(u_d)e_d\). Thus
\[
\mathbb E_U[\phi(U_d)^2]
=\frac1{2\pi}\mathbb E[e^{-U_d^2}]
=\frac1{2\pi\sqrt3}.
\]
The score identity is verified directly: for every coordinate \(k\), \(\partial_{u_k}F(u)=\mathbb E_Z[\mathbf1_{\{u_d+Z_d>0\}}Z_k]\); for \(k\ne d\) this vanishes by independence and for \(k=d\) it is \(\phi(u_d)\). Subtracting \(Z_k/2\) does not alter the mean because \(\mathbb E Z_k=0\).

**2. Fixed-path span.** Every \(\widehat g_\ell(u)\) is a linear combination of the same \(\ell\) vectors \(Z_i\). Therefore \(\operatorname{ran}(\widehat K_{\ell,m})\subseteq S_\ell\), irrespective of the number of outer samples. Since \(\ell<d\), the Gaussian \(d\)-by-\(\ell\) matrix with columns \(Z_i\) has full column rank almost surely. Each coefficient multiplying \(Z_i\) in \(\widehat g_\ell(u)\) is either \(+1/(2\ell)\) or \(-1/(2\ell)\), so every \(\widehat g_\ell(u)\ne0\) almost surely. Hence \(\widehat K_{\ell,m}\ne0\). A positive-eigenvalue eigenvector belongs to its image, thus to \(S_\ell\). For any unit \(v\in S_\ell\), Cauchy–Schwarz gives \(|v^\top e_d|^2\le\|\Pi_{S_\ell}e_d\|^2=P_\ell\).

**3. Exact subspace law.** Rotational invariance of the Gaussian columns implies that \(S_\ell\) is Haar-uniform on the Grassmannian of \(\ell\)-planes in \(\mathbb R^d\). For independent standard normals \(G_1,\dots,G_d\), the projection energy consequently has the same distribution as
\[
\frac{G_1^2+\cdots+G_\ell^2}{G_1^2+\cdots+G_d^2}.
\]
The numerator and complementary sum are independent chi-square variables with \(\ell\) and \(d-\ell\) degrees of freedom. Their ratio yields the asserted Beta distribution, with mean \(\ell/d\). Since both parameters are positive, \(0<P_\ell<1\) almost surely. This proves both alignment bounds.

**4. Exact optimal ridge risk.** Fix a unit \(v\) and write \(c=v^\top e_d\), \(Y=v^\top U^*\), and \(Q=(U^*)_d\). The pair \((Y,Q)\) is jointly standard normal with correlation \(c\); conditionally on \(Y=y\), \(Q\) has distribution \(N(cy,1-c^2)\). Gaussian convolution shows that the optimal square-integrable predictor from \(Y\) is
\[
h_v(Y)=\mathbb E[\Phi(Q)\mid Y]
=\Phi\!\left(\frac{cY}{\sqrt{2-c^2}}\right).
\]
Because \(\Phi(Q)\) is uniform on \((0,1)\), its variance is \(1/12\). The standard bivariate-normal orthant identity
\[
\mathbb P(A\le0,B\le0)=\frac14+\frac{\arcsin\rho}{2\pi}
\]
for centered unit Gaussians of correlation \(\rho\) implies
\[
\operatorname{Var}(h_v(Y))=\frac1{2\pi}\arcsin\!\left(\frac{c^2}{2}\right).
\]
Indeed, introduce two independent standard normals \(V_1,V_2\), independent of \(Y\), and represent \(h_v(Y)^2\) as the probability of the two events \(V_j\le cY/\sqrt{2-c^2}\). The two standardized differences have correlation \(c^2/2\). The conditional-variance identity gives the risk \(1/12-\arcsin(c^2/2)/(2\pi)\). As \(\arcsin\) is increasing, minimizing over \(v\in S_\ell\) means maximizing \(c^2\), which is exactly \(P_\ell\). A normalized projection attains it. Convexity of \(q\mapsto\arcsin(q/2)\) on \([0,1]\), with endpoints \(0\) and \(\pi/6\), gives \(\arcsin(q/2)\le q\pi/6\) and hence the stated lower bound. Taking expectations gives \(\mathbb E[\mathcal R(S_\ell)]\ge (1-\ell/d)/12\).

**5. One reused path and control choice.** With \(\ell=1\), the centered indicator equals \(\pm1/2\) for every drift, except on a probability-zero threshold event. Therefore \(\widehat g_1(u)\widehat g_1(u)^\top=Z_1Z_1^\top/4\) for every \(u\), and averaging over outer samples changes nothing. For completeness, the scalar control coefficient \(-1/2\) uniquely minimizes the mean over the Gaussian drift prior of the conditional total gradient-estimator variance among fixed scalar coefficients: for each coordinate \(k\), symmetry gives \(\mathbb E_{U,Z}[\mathbf1_{\{U_d+Z_d>0\}}Z_k^2]=1/2\). Consequently the coefficient-dependent expected second moment is \(1/2+\beta+\beta^2\), while the squared gradient mean is independent of \(\beta\). This quadratic is uniquely minimized at \(\beta=-1/2\).

## Verification

The complete executable file `verify.py` uses fixed-seed Gaussian experiments and deterministic Gaussian quadrature. It checks the exact one-path matrix identity over several dimensions and outer sample counts, numerical column-span and rank identities, the Beta projection mean in several dimensions, the analytic orthant-risk expression, the linear risk floor, the Gaussian derivative, the control coefficient and the exact sensitivity eigenvalue. Its latest standalone execution completed 10,944 checks successfully. These finite checks do **not** establish the general-dimensional conclusions; Steps 1–5 above provide the proof.

To reproduce: run `python verify.py` with Python 3 and NumPy installed. No hidden input files or simulations are required.

## Relationship to prior work

Zou, Lie and Marzouk (2026) introduce the path-space sensitivity matrix, score-based inner Monte Carlo gradient, scalar martingale control variate and outer-product estimator. Their numerical implementation explicitly reuses Brownian trajectories across outer drift samples (Section 4.1). The present theorem studies a constant-drift terminal-event specialization of this **specific reuse decision**, deriving its finite-inner-span restriction, the exact Grassmannian/Beta alignment law and the optimal downstream one-dimensional prediction risk. The source establishes neither a universal shared-path rank obstruction nor this precise model-specific quantitative bound; its spatially varying drift fields need not have the same restriction.

Holodnak, Ipsen and Smith (2018) study active-subspace eigenvector errors from independent unbiased outer-product samples. Luo, O'Leary-Roseberry, Chen and Ghattas (2026) establish empirical derivative-informed subspace estimation errors and optimal conditional-expectation ridge approximation. Those established theories do not directly give the reuse-induced fixed-score-span phenomenon: the inner path pool is held fixed as the outer sample count grows, and the resulting conditional covariance need not equal the population sensitivity matrix. The Gaussian Beta projection and normal orthant identities are classical; novelty is not claimed for either identity separately.

## Limitations

The obstruction depends on a finite Gaussian path pool shared across outer parameter samples **and** a constant-drift score whose vector equals the Brownian endpoint. For position-dependent score integrands, the score vector may change with the outer parameter even under shared noise, so the span constraint can fail. Regenerating independent paths for every outer draw also removes this particular fixed-span argument. The result concerns one-dimensional approximation and does not claim an analogous sharp error for arbitrary multi-dimensional reduced spaces. The lower bound is for prediction from a single extracted linear coordinate using a fresh Gaussian drift, not for recovery by methods with additional access to the original model. The linear risk bound is conservative relative to the exact arcsine formula. Established random-subspace and Gaussian-conditioning mathematics contributes essential proof ingredients, and an unlocated earlier specialized treatment remains a historical-priority risk. Independent mathematical audit has not been performed.

## References

1. J. Zou, H. C. Lie and Y. Marzouk, *Derivative-Informed Dimension Reduction of Stochastic Differential Equations: A Path-Space Sensitivity Approach*, arXiv:2610.33210v1, first submitted 2026-10-23. https://arxiv.org/html/2610.33210v1
2. J. T. Holodnak, I. C. F. Ipsen and R. C. Smith, *A Probabilistic Subspace Bound with Application to Active Subspaces*, arXiv:1801.00682, 2018. https://arxiv.org/abs/1801.00682
3. D. Luo, T. O'Leary-Roseberry, P. Chen and O. Ghattas, *Dimension Reduction for Derivative-Informed Operator Learning: An Analysis of Approximation Errors*, Journal of Machine Learning Research 27(182), 2026. https://jmlr.org/papers/v27/25-1861.html
