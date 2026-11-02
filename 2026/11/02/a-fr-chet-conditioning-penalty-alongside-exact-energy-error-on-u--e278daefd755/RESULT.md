# A Fréchet conditioning penalty alongside exact energy error on uniform random finite-element meshes

## Finding
For every integer \(n\ge 3\), choose \(n-1\) independent uniform points in \((0,1)\), order them, and add the endpoints. Let \(u_n\) be the continuous, nodal piecewise-affine Galerkin solution of \(-u''=1\) on \((0,1)\), with homogeneous Dirichlet boundary conditions and exact integration. Let \(K_n\) be the unscaled, \((n-1)\)-by-\((n-1)\) stiffness matrix in the usual nodal basis; let \(\kappa_n=\lambda_{\max}(K_n)/\lambda_{\min}(K_n)\). Write \(\mathcal E_n=\int_0^1|u'-u_n'|^2\,dt\).

Then the exact finite-sample laws are
\[
\mathbb E\mathcal E_n=\frac1{2(n+1)(n+2)},\qquad
\operatorname{Var}(\mathcal E_n)=\frac{(n-1)(5n+11)}{2(n+1)^2(n+2)^2(n+3)(n+4)(n+5)},
\]
and, for every \(q>0\),
\[
\mathbb E\kappa_n^q<\infty\quad\Longleftrightarrow\quad 0<q<1.
\]
In particular, the expected condition number is infinite for each fixed \(n\ge3\), despite finite and small energy error. As \(n\to\infty\),
\[
 n^2\mathcal E_n\xrightarrow{\mathbb P}\tfrac12,\qquad
 \sqrt n\bigl(n^2\mathcal E_n-\tfrac12\bigr)\Longrightarrow N(0,\tfrac52),\qquad
 \frac{\kappa_n}{n^3}\Longrightarrow\frac{2}{\pi^2Z},
\]
where \(Z\) has the unit-rate exponential distribution. Thus the limiting condition-number distribution has CDF \(\exp[-2/(\pi^2t)]\) for \(t>0\) (Fréchet shape one). For a deterministic uniform mesh with the same \(n\) elements, the energy error is \(1/(12n^2)\) and the stiffness condition number is \(\cot^2(\pi/(2n))\sim4n^2/\pi^2\): random unguarded knots have a factor-six *expected energy-error* penalty asymptotically and an extra factor of \(n\) in the typical stiffness conditioning scale.

## Assumptions and scope
The load is exactly one, the diffusion coefficient is exactly one, the domain is \((0,1)\), the trial and test functions are ordinary continuous piecewise linear functions with zero boundary values, and all element integrals are exact. There are \(n\) elements and \(n-1\) free nodal degrees of freedom. Knots are order statistics of independent \(U(0,1)\) samples, **not** bounded perturbations of quasi-uniform meshes. The condition number is the Euclidean spectral condition number of the **unpreconditioned nodal matrix**; mass scaling, Jacobi scaling, iterative errors, and floating-point effects are not asserted. For \(n=2\), the one-by-one stiffness condition number is identically one, and for \(n=1\) there is no free stiffness system; the error identities hold for \(n\ge1\).

## Proof
**Ritz interpolation and Dirichlet-spacing error.** Put \(t_0=0<t_1<\cdots<t_n=1\), and \(h_j=t_j-t_{j-1}\). The exact solution is \(u(t)=t(1-t)/2\). The nodal interpolant \(I_nu\) satisfies \(\int_0^1(u'-(I_nu)')v_n'=0\) for every piecewise-affine \(v_n\), since each element derivative of \(v_n\) is constant and each element derivative of \(I_nu\) equals the integral average of \(u'\). Hence \(u_n=I_nu\). On a cell of length \(h_j\), the derivative difference is the centered affine function with slope \(-1\), giving exactly
\[\mathcal E_n=\frac1{12}\sum_{j=1}^n h_j^3.\]
The spacing vector is Dirichlet with \(n\) unit parameters. Its monomial-moment identity, directly from the uniform density on the spacing simplex, is \(\mathbb E\prod_j h_j^{a_j}=\prod_j a_j!/(n)_{\sum a_j}\) for nonnegative integers \(a_j\), where \((n)_k=n(n+1)\cdots(n+k-1)\). Thus \(\mathbb E\sum h_j^3=6/[(n+1)(n+2)]\) and \(\mathbb E(\sum h_j^3)^2=36n(n+19)/(n)_6\). Subtracting the squared mean and dividing by \(144\) gives the claimed variance. Equivalently, writing \(h_j=Y_j/T_n\) for independent unit exponentials \(Y_j\) and \(T_n=\sum_jY_j\),
\[
 n^2\mathcal E_n=\frac{\overline{Y^3}_n}{12\bar Y_n^3}.
\]
The law of large numbers gives limit \(6/12=1/2\). The bivariate central limit theorem and delta method give asymptotic variance \(\operatorname{Var}(Y^3-18Y)/144=(720-36+324-648)/144=5/2\), proving the displayed CLT.

**Smallest stiffness eigenvalue.** A nodal vector \(a\in\mathbb R^{n-1}\) corresponds to its piecewise-affine interpolant \(v_a\), with \(a^\top K_na=\|v_a'\|_{L^2}^2\) and \(\|a\|^2=\sum_{i=1}^{n-1}v_a(t_i)^2\). Let \(F_{n-1}\) be the empirical CDF of the independent uniform interior knots, and \(\delta_{n-1}=\sup_{t\in[0,1]}|F_{n-1}(t)-t|\). Uniform empirical convergence gives \(\delta_{n-1}\to0\) in probability. Integration by parts, Cauchy–Schwarz, and the Dirichlet Poincaré inequality give, uniformly for all such \(v_a\),
\[
\frac1{n-1}\sum_{i=1}^{n-1}v_a(t_i)^2
\le \int_0^1v_a^2+\delta_{n-1}\int_0^1|(v_a^2)'|
\le\bigl(\pi^{-2}+2\delta_{n-1}/\pi\bigr)\int_0^1|v_a'|^2.
\]
Therefore \(\liminf n\lambda_{\min}(K_n)\ge\pi^2\) in probability. For the reverse inequality choose the nodal interpolant of \(\sin(\pi t)\): the maximum spacing tends to zero in probability, so its energy converges to \(\pi^2/2\), while the uniform empirical law gives \(n^{-1}\sum_i\sin^2(\pi t_i)\to1/2\). Hence
\[n\lambda_{\min}(K_n)\xrightarrow{\mathbb P}\pi^2.\]

**Largest stiffness eigenvalue.** The assembled matrix is \(K_n=\sum_{j=1}^n h_j^{-1}b_jb_j^\top\), where \(b_1=e_1\), \(b_n=e_{n-1}\) up to sign, and interior \(b_j=e_{j-1}-e_j\). With \(h_j=Y_j/T_n\), the minimum exponential \(Y_{(1)}\) satisfies \(nY_{(1)}\overset{d}=Z\sim\mathrm{Exp}(1)\), and \(T_n/n\to1\). Fix \(M>0\) and split edges at \(Y_j\le M/n\). The probability that these short edges include an endpoint or two adjacent edges is at most \(2M/n+O(M^2/n)\). With probability approaching \(1-e^{-M}\), at least one such edge exists and all are isolated interior edges. Their rank-one edge matrices then have disjoint supports, so the largest eigenvalue of the short-edge sum is exactly \(2T_n/Y_{(1)}\). The remaining positive-semidefinite weighted path Laplacian has operator norm at most \(4T_nn/M\). Consequently the error after scaling by \(n^2\) is bounded by \(4(T_n/n)/M\). Taking \(n\to\infty\), then \(M\to\infty\), yields
\[\lambda_{\max}(K_n)/n^2\Longrightarrow2/Z.\]
Combining with the smallest-eigenvalue limit by Slutsky yields the claimed \(\kappa_n/n^3\) distribution.

**Finite-sample moment threshold.** For all vectors \(v_a\) with \(v_a(0)=0\), Cauchy–Schwarz gives \(\max_t|v_a(t)|^2\le\int|v_a'|^2\). Consequently \(\lambda_{\min}(K_n)\ge1/(n-1)\), while the edge-sum bound yields \(\lambda_{\max}(K_n)\le4/h_{\min}\). The uniform-simplex spacings obey \(\mathbb P(h_{\min}>s)=(1-ns)^{n-1}\) for \(0\le s\le1/n\), so inverse moments of \(h_{\min}\) exist for \(q<1\). Conversely, fix any **interior** edge, say \(h_2\), and constrain the other spacings to small neighborhoods of a positive configuration while \(h_2\downarrow0\). This event has a density bounded below in the shrinking gap. The Rayleigh quotient for the nodal interpolant of \(\sin(\pi t)\) gives an upper bound on \(\lambda_{\min}\) uniform on that event; the vector supported with opposite signs on the two endpoints of edge \(h_2\) gives \(\lambda_{\max}\ge2/h_2\). Thus \(\kappa_n\ge c/h_2\) on a positive-density family, making every \(q\ge1\) moment diverge. This construction requires \(n\ge3\).

## Verification
The included standalone \(\texttt{verify.py}\) checks 550 exactly rational, nonuniform Galerkin systems against their nodal interpolants and element error identities, 150 exact Dirichlet-moment identities, and a reproducible exploratory spectral experiment on 100 meshes with 250 elements. The finite checks are not proofs of infinite moment divergence or weak convergence; all infinite assertions are established above from elementary analytic bounds, the law of large numbers, the central limit theorem, and extreme spacings.

## Relationship to prior work
Abdulle and Garegnani (arXiv:2103.06204, 2021) formulate random-mesh finite elements, posterior error estimators, and one-dimensional bounds under quasi-uniform or controlled-perturbation assumptions. Their mesh is generated by moving an existing mesh's nodes by controlled \(h^p\) amounts, unlike fully resampled uniform order statistics, and their stated results do not give this finite-sample error law or a Fréchet conditioning law. Kamenski, Huang, and Xu (arXiv:1201.3651, 2012) obtain general deterministic spectral conditioning bounds for arbitrary anisotropic meshes and analyze diagonal preconditioning; those bounds motivate studying mesh nonuniformity but do not specify the limiting random spectrum or joint approximation/conditioning cost for the present sampling law. Flegel (arXiv:1801.05684, 2018) studies localization of *small* Dirichlet eigenvalues for degenerate conductances on higher-dimensional lattices; this is not the extreme large-conductance eigenvalue of the one-dimensional finite-element matrix here. The exponential representation of uniform spacings and general eigenvalue variational inequalities are standard, and are not claimed as inventions.

## Limitations
The statement does not extend automatically to boundedly perturbed quasi-uniform meshes, other diffusion coefficients or right-hand sides, multidimensional elements, nonuniform point densities, or diagonally preconditioned systems. Conditioning is a mathematical spectral statement, not a measured runtime or floating-point failure claim. An earlier equivalent exact derivation in random-conductance or random-mesh literature cannot be completely ruled out without independent priority checking; no source in the inspected texts states the combined exact finite-sample energy moments and normalized Fréchet stiffness-conditioning result.

## References
1. A. Abdulle and G. Garegnani, *A probabilistic finite element method based on random meshes: Error estimators and Bayesian inverse problems*, arXiv:2103.06204, first submitted 2021-03-10, https://arxiv.org/abs/2103.06204.
2. L. Kamenski, W. Huang, and H. Xu, *Conditioning of Finite Element Equations with Arbitrary Anisotropic Meshes*, arXiv:1201.3651, first submitted 2012-01-17, https://arxiv.org/html/1201.3651v3.
3. F. Flegel, *Eigenvector localization in the heavy-tailed random conductance model*, arXiv:1801.05684, first submitted 2018-01-17, https://arxiv.org/abs/1801.05684.
