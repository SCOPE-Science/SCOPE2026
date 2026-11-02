# Exact mean-resolvent calibration and opposite averaging-variance trends in scalar proximal sampling

## Finding

A one-component stochastic proximal step on a finite sum of scalar quadratics can have exactly the **full deterministic proximal map as its conditional expectation** if its component-sampling probabilities depend on the step size. Although the stationary iterate is unbiased for the true minimizer, its **time-averaging precision** can depend oppositely on the step size for different numbers of components. With two components the asymptotic variance coefficient never decreases; with three, a natural symmetric-offset family makes it strictly decrease for every step size.

Specifically, with the notation below, the unique calibration for all component centers is
\[
p_i=\frac{1+\eta a_i}{n+\eta S},\qquad
\mathbb E\big[\operatorname{prox}_{\eta f_I}(x)\big]=\operatorname{prox}_{\eta F}(x).
\]
The entire stationary covariance sequence and the exact long-run variance coefficient are
\[
\operatorname{Var}(X_0)=\frac{\eta T}{S+U},\qquad
\operatorname{Cov}(X_0,X_k)=\frac{\eta T}{S+U}R^k,\qquad
\Gamma=\frac{(2n+\eta S)T}{S(S+U)},
\]
where \(R=n/(n+\eta S)\). Here stationarity is assumed for covariance and averaging formulas.

## Assumptions and scope

Let \(n\ge2\) be an integer, \(a_i>0\) and \(c_i\in\mathbb R\) for \(1\le i\le n\), and \(\eta>0\). Define
\[
f_i(x)=\tfrac12 a_i(x-c_i)^2,\quad F(x)=\frac1n\sum_{i=1}^{n}f_i(x),\quad S=\sum_i a_i,\quad m=\frac{\sum_i a_i c_i}{S}.
\]
Independently at each iteration, sample \(I_{k+1}\) with the fixed positive probabilities \(p_i=(1+\eta a_i)/(n+\eta S)\), independently of the current state, and update \(X_{k+1}=\operatorname{prox}_{\eta f_{I_{k+1}}}(X_k)\). The proximal parameter \(\eta\) is held constant. Write
\[
T=\sum_i\frac{a_i^2(c_i-m)^2}{1+\eta a_i},\quad
U=\sum_i\frac{a_i}{1+\eta a_i},\quad
R=\frac{n}{n+\eta S}.
\]
The stationary law is reached in distribution from every deterministic initial condition. The statements about \(\operatorname{Cov}\) and \(\Gamma\) refer to a stationary version indexed by nonnegative integers. For all-center uniqueness, the same probability vector must satisfy the mean-map identity for **every** possible center vector at fixed positive curvatures and step size.

## Proof

**Exact calibration and uniqueness.** For every \(i\), direct minimization gives
\[
T_i(x):=\operatorname{prox}_{\eta f_i}(x)
=\frac{x+\eta a_i c_i}{1+\eta a_i}.
\]
Substituting the proposed probabilities yields
\[
\sum_i p_iT_i(x)=\frac{nx+\eta\sum_i a_i c_i}{n+\eta S}
=\operatorname{prox}_{\eta F}(x).
\]
Conversely, equality for all center vectors requires the coefficient of each \(c_i\) to agree: \(p_i\eta a_i/(1+\eta a_i)=\eta a_i/(n+\eta S)\). Since \(a_i,\eta>0\), this uniquely determines every \(p_i\). Uniqueness is **not** asserted if centers are fixed in advance.

**Stationarity, mean, and moments.** Each \(T_i\) is a strict contraction with ratio \(r_i=(1+\eta a_i)^{-1}\). Since the finite set of maps has a common contraction bound smaller than one and sends the compact convex hull of the centers to itself, backward iteration gives a unique compactly supported stationary law, attracting all deterministic starts in Wasserstein distance. The expected map fixes \(m\), so its stationary mean is \(m\).

Put \(Z_k=X_k-m\) and \(h_i=a_i(c_i-m)\), with \(\sum_i h_i=0\). Then
\[
Z_{k+1}=r_{I_{k+1}}Z_k+\xi_{I_{k+1}},\qquad
\xi_i=\frac{\eta h_i}{1+\eta a_i}.
\]
Its independent innovation has mean zero, and
\[
\mathbb E r_I=R,\qquad
\mathbb E r_I^2=\frac{1}{n+\eta S}\sum_i\frac1{1+\eta a_i},\qquad
\mathbb E\xi_I^2=\frac{\eta^2T}{n+\eta S}.
\]
Also \(1-\mathbb E r_I^2=\eta(S+U)/(n+\eta S)\); this follows by summing \((1+\eta a_i)-(1+\eta a_i)^{-1}=\eta a_i[1+(1+\eta a_i)^{-1}]\). In the stationary centered variance equation, the mixed term vanishes because \(Z_k\) is independent of the next index and \(\mathbb E Z_k=0\). Hence \(V=\mathbb E\xi_I^2/(1-\mathbb E r_I^2)=\eta T/(S+U)\). Since \(\mathbb E[Z_{k+1}\mid Z_k]=RZ_k\), induction gives \(\operatorname{Cov}(X_0,X_k)=VR^k\). Direct expansion of a stationary mean proves for every integer \(N\ge1\)
\[
\operatorname{Var}\left(\frac1N\sum_{j=0}^{N-1}X_j\right)
=\frac{V}{N^2}\left(N+2\sum_{k=1}^{N-1}(N-k)R^k\right).
\]
The geometric sum yields \(\Gamma=V(1+R)/(1-R)=(2n+\eta S)T/[S(S+U)]\).

**Two components: no decreasing regime.** Let \(n=2\), \(a_1=a\), \(a_2=b\), \(\Delta=c_1-c_2\), and \(g=ab\Delta/(a+b)\). Then \(h_1=g\), \(h_2=-g\). Substituting into the general formula and canceling rational factors gives
\[
V=\frac{\eta g^2}{a+b+\eta ab},\qquad
\Gamma=\frac{g^2[4+\eta(a+b)]}{(a+b)[a+b+\eta ab]}.
\]
Its exact derivative is
\[
\frac{d\Gamma}{d\eta}
=\frac{g^2(a-b)^2}{(a+b)(a+b+\eta ab)^2}\ge0.
\]
Strict inequality holds exactly when both curvatures and centers differ.

**Three components: a strict reversal.** Let \((a_1,a_2,a_3)=(a,b,b)\) and \((c_1,c_2,c_3)=(0,1,-1)\), where \(a,b>0\). Then \(m=0\). Set \(r=a/b\), \(u=b\eta\), and
\[
D_r(u)=r(r+2)u^2+(r^2+6r+2)u+2r+4.
\]
Direct substitution yields
\[
\Gamma_r(u)=\frac{2(1+ru)[6+(r+2)u]}{(r+2)D_r(u)},
\]
and exact differentiation and factorization gives
\[
\Gamma_r'(u)=\frac{2(r-1)\left[r^2(r+2)u^2+4r(r+2)u+4(2r+1)\right]}{(r+2)D_r(u)^2}.
\]
The bracket and denominator are positive for \(r,u>0\). Thus \(0<a<b\) implies strict decrease for **every** \(\eta>0\), while \(a>b\) implies strict increase and \(a=b\) constant. The endpoint values are \(\Gamma_r(0+)=6/(r+2)^2\) and \(\Gamma_r(+\infty)=2/(r+2)\). By contrast, the stationary single-iterate variance in this family is
\[
V_r(u)=\frac{2u(1+ru)}{D_r(u)},\qquad
V_r'(u)=\frac{2[r^2(r+5)u^2+4r(r+2)u+2r+4]}{D_r(u)^2}>0.
\]
The derivative numerator identity follows by collecting terms; all are positive for \(r,u>0\). This shows the reversal is specific to *time-averaging error*, not to stationary single-iterate error.

For an exact numerical witness, choose \(a=1\), \(b=10\), and \(c=(0,1,-1)\). At \(\eta=1/5\), \(\Gamma=1360/1197\), \(V=80/171\); at \(\eta=2\), \(\Gamma=800/819\), \(V=100/117\). The asymptotic averaging coefficient decreases while the stationary variance increases.

## Verification

The included `verify.py` implements symbolic factorizations using SymPy, checks 275 exact-rational random parameter cases for normalization, calibration, stationary second moments, and long-run variance, and performs three independent seeded Monte Carlo trajectory comparisons for means, variances, and lag-one covariances. It reports ten symbolic identity groups, 275 rational cases and three trajectory checks as passing. To reproduce, install dependencies in `requirements.txt` and run `python verify.py` in this package. The analytic derivation above, not finite simulations, proves the universal and limiting claims.

## Relationship to prior work

Traoré et al. [1] define and analyze stochastic proximal point algorithms and variance-reduced versions for finite sums; their plain version samples components uniformly, and the inspected convergence theorems do not specify this step-dependent *mean-resolvent-matching* law or exact stationary time-average variance. Sadiev, Condat and Richtárik [2] treat random resolvents of monotone operators with expected-similarity convergence bounds, including a general sampling law, but their inspected SPPM and correction theorems do not supply the exact all-center calibrating probabilities or the two-versus-three variance-sign classification. Toulis and Airoldi [3] address implicit stochastic gradients and asymptotic estimator variances under a different step-size and estimator framework. Proximal-average theory [4] supplies general convex combinations of proximal mappings as proximal maps of *proximal averages*, but that does not in general identify such an average with \(\operatorname{prox}_{\eta F}\) for the original arithmetic mean; the equality here requires the explicit quadratic calibration. The finite-alphabet random affine second-moment calculations themselves are standard ingredients; the asserted contribution is their motivated joint calibration and sharp minimal-component reversal, not a new general Markov-chain covariance theorem.

## Limitations

This is an exact-arithmetic theorem for scalar positive-curvature quadratics with iid indices and a fixed step size. The conditional mean identity does not imply that individual trajectories follow deterministic proximal point iteration, nor does it imply the stationary law is concentrated at the minimizer. The general variance formulas apply at stationarity; no stationary central limit theorem or nonstationary finite-sample bound is claimed. The uniqueness of probabilities requires **all possible** center choices. The three-component monotonicity classification is for the specified symmetric-offset family, not all three-component problems. Higher dimensions, nonlinear functions, dependent sampling, unknown curvatures, and wall-clock optimality are outside scope. An exhaustive historical priority assessment is not possible; generic affine-recursion and proximal-average theorems could provide alternative routes to parts of the formulas.

## References

[1] C. Traoré, V. Apidopoulos, S. Salzo, S. Villa, *Variance reduction techniques for stochastic proximal point algorithms*, arXiv:2308.09310, first posted 2023-08-18, https://arxiv.org/abs/2308.09310.

[2] A. Sadiev, L. Condat, P. Richtárik, *Stochastic Proximal Point Methods for Monotone Inclusions under Expected Similarity*, arXiv:2405.14255 (2024), https://arxiv.org/abs/2405.14255.

[3] P. Toulis, E. M. Airoldi, *Asymptotic and finite-sample properties of estimators based on stochastic gradients*, arXiv:1408.2923, https://arxiv.org/abs/1408.2923.

[4] H. H. Bauschke, X. Wang, *The Bregman proximal average*, arXiv:2108.11440 (2021), https://arxiv.org/abs/2108.11440.

[5] D. P. Bertsekas, *Incremental proximal methods for large scale convex optimization* (2011), author manuscript, https://web.mit.edu/dimitrib/www/Incremental_Proximal.pdf.
