# An irreducible snapshot inference floor in a collectively switched harmonic Brownian gas

## Finding
Consider a stationary population of \(N\geq 1\) noninteracting Brownian particles driven by a **common** two-state switching trap. The physically relevant question is whether simultaneous particle positions reveal the trap's **instantaneous** binary state. Let \(R_N\) denote the minimum possible probability of misclassification from one population snapshot when the model parameters are known and both state errors have unit cost.

For every choice of strictly positive parameters specified below, the result is the exact finite-\(N\) expression (4) and the sharp expansion
\[
\boxed{R_N=R_\infty+\frac{D}{\gamma\ell^2 N}\frac{2^{2-A-B}}{B(A,B)}+o(N^{-1}),\qquad R_\infty>0.}
\tag{1}
\]
Here \(A=\alpha/\gamma\), \(B=\beta/\gamma\), and the irreducible infinite-population error is
\[
\boxed{R_\infty=\frac{B_{1/2}(A+1,B)+B(A,B+1)-B_{1/2}(A,B+1)}{B(A,B)}.}
\tag{2}
\]
The beta-Dirichlet stationary mixing law and its state-conditioned version are **prior results**, not the novelty claim. The claim is the exact **population-snapshot optimal binary inference risk**, its strict positive infinite-population floor, and the evaluated sharp \(N^{-1}\) approach. In the symmetric switching family the risk has an additional elementary formula valid for every \(N\), stated in (5).

## Assumptions and scope
Let \(\gamma,D,\ell,\alpha,\beta>0\). A stationary continuous-time Markov chain \(S_t\in\{0,1\}\) changes from \(0\) to \(1\) at rate \(\alpha\), and from \(1\) to \(0\) at rate \(\beta\). Given this **shared** environment, let \(B^i\) be independent two-sided standard Brownian motions, independent of \(S\), and define each particle by its unique stationary solution
\[
 dX_t^i=-\gamma(X_t^i-\ell S_t)\,dt+\sqrt{2D}\,dB_t^i,\qquad i=1,\ldots,N.
\]
Only \(X_0^1,\ldots,X_0^N\) are observed: neither \(S_0\), the environmental history, nor earlier/later snapshots are observed. Parameters are known. The infimum defining \(R_N\) ranges over all measurable binary rules on this observation vector, with stationary prior on the binary state. It is not an online filtering or trajectory-reconstruction claim.

Write \(\sigma^2=D/\gamma\), \(A=\alpha/\gamma\), \(B=\beta/\gamma\), and let \(f(u)=u^{A-1}(1-u)^{B-1}/B(A,B)\), \(0<u<1\), be a beta density. Here \(B(a,b)\) and \(B_x(a,b)\) denote the complete and unregularized lower incomplete beta integrals. Let \(\phi_\delta\) be the centered Gaussian density of variance \(\delta^2\), \(\Phi\) the standard-normal distribution function, and \(\varphi\) its density.

## Proof
**1. Conditional Gaussian reduction and established stationary mixing law.** The stationary stochastic convolution gives
\[
 X_0^i=\ell U+\sigma Z_i,\qquad U=\gamma\int_{-\infty}^0e^{\gamma s}S_s\,ds,\tag{3}
\]
where the \(Z_i\) are independent standard normals, independent of \((U,S_0)\). The pair \((U,S)\) is a piecewise-deterministic process: between switches \(\dot U=\gamma(S-U)\). Its stationary forward equations have the zero-total-flux solution \(p_1(u)=uf(u)\), \(p_0(u)=(1-u)f(u)\). Indeed, with \(p=p_0+p_1\), zero flux is \(-\gamma up_0+\gamma(1-u)p_1=0\); substituting \(p_1=up\) in the state-\(1\) equation yields \(\partial_u[u(1-u)p]=(A-(A+B)u)p\). Its normalized solution is the beta density \(f\). Uniqueness follows from contractive drift, irreducible switching, and the compact invariant interval. This beta-Dirichlet joint law is also contained in Herbach's stationary PDMP construction (Proposition 4.4), and is used here as a starting point, not asserted as new.

**2. Exactly optimal finite-population rule.** The sample mean is sufficient for \(U\), hence also for \(S_0\), since the Gaussian likelihood factors into a residual factor independent of \(U\) and a factor involving only the sample mean. Normalize the observed mean as \(Y_N=(\ell N)^{-1}\sum_iX_0^i=U+\delta_N Z\), where \(\delta_N^2=D/(\gamma\ell^2N)\). Define
\[
 g_1(y)=\int_0^1u f(u)\phi_{\delta_N}(y-u)\,du,\qquad
 g_0(y)=\int_0^1(1-u) f(u)\phi_{\delta_N}(y-u)\,du.
\]
These are the joint observation/state densities. Thus the exact optimal error is
\[
\boxed{R_N=\int_{\mathbb R}\min\{g_0(y),g_1(y)\}\,dy.}\tag{4}
\]
The posterior odds are strictly increasing in \(y\): their derivative is a positive multiple of the difference of conditional expectations of \(U\) under the \(u f\) and \((1-u)f\) posterior weights, which is strictly positive by monotone likelihood ratio. As \(y\to\pm\infty\), those odds tend to \(\infty\) and \(0\), respectively. Therefore there is exactly one Bayes decision threshold \(y_{\delta_N}\), determined by \(g_1(y_{\delta_N})=g_0(y_{\delta_N})\); decide \(1\) above it. No finite-\(N\) claim is based only on an approximate threshold.

**3. The positive limiting floor.** As \(\delta_N\to0\), the observation reveals \(U\) but not \(S_0\). The established stationary joint law gives \(\mathbb P(S_0=1\mid U=u)=u\). Thus the limiting optimal loss is \(\int_0^1\min(u,1-u)f(u)\,du\), exactly (2). It is strictly between \(0\) and \(1/2\) for every \(A,B>0\). For any finite \(N\), the Gaussian channel strictly loses classification information across the threshold, so \(R_N>R_\infty\).

**4. Sharp finite-size correction.** Extend \(h(u)=(2u-1)f(u)\mathbf1_{(0,1)}(u)\) by zero. The threshold solves \((h*\phi_\delta)(y_\delta)=0\). On a fixed neighborhood of \(1/2\), the beta density is smooth and positive. The local heat-kernel expansion and the implicit-function theorem give
\[
 y_\delta=\frac12-\delta^2\frac{f'(1/2)}{f(1/2)}+O(\delta^4).
\]
The exact excess risk relative to the ideal classifier that observes \(U\) is
\[
\begin{aligned}
R(\delta)-R_\infty={}&\int_0^{1/2}(1-2u)f(u)\Phi\bigl((u-y_\delta)/\delta\bigr)\,du\\
&+\int_{1/2}^1(2u-1)f(u)\Phi\bigl((y_\delta-u)/\delta\bigr)\,du.
\end{aligned}
\]
Set \(u=1/2+\delta z\). Gaussian tails dominate the rescaled integrands uniformly away from the endpoints, and \((y_\delta-1/2)/\delta\to0\). Dominated convergence gives
\[
\frac{R(\delta)-R_\infty}{\delta^2}\longrightarrow 4f(1/2)\int_0^\infty z\Phi(-z)\,dz=f(1/2),
\]
using \(\int_0^\infty z\Phi(-z)dz=1/4\). Substituting \(\delta=\delta_N\) gives (1). The coefficient is exactly \(f(1/2)=2^{2-A-B}/B(A,B)\).

**5. Exactly solvable symmetric benchmark.** When \(\alpha=\beta=\gamma\), the beta law is uniform, the threshold is exactly \(y_\delta=1/2\), and \(R_\infty=1/4\). Put \(H=1/(2\delta_N)\). Direct integration of (4) gives
\[
\boxed{R_N=\frac14+\frac12\Phi(-H)+2\delta_N^2\left[\Phi(H)-\frac12-H\varphi(H)\right].}\tag{5}
\]
In particular \(R_N=1/4+D/(\gamma\ell^2N)+O(e^{-cN})\) for some \(c>0\) when the other parameters are fixed. More generally for symmetric switching \(\alpha=\beta=s\), setting \(q=s/\gamma\) gives the exact plateau
\[
 R_\infty=\frac12-\frac{\Gamma(q+1/2)}{2\sqrt\pi\Gamma(q+1)},
\]
with \(R_\infty=q\log2+O(q^2)\) as \(q\downarrow0\), and \(R_\infty=1/2-(2\sqrt{\pi q})^{-1}+O(q^{-3/2})\) as \(q\to\infty\). These limits quantify the disparity between slowly switching and rapidly switching environments.

## Verification
The accompanying standalone `verify.py` numerically evaluates the exact optimal risk via a threshold determined from the full beta-Gaussian observation likelihood, **not** from the asymptotic threshold. It compares the normalized excess risk to the coefficient in (1) for three beta shapes, checks (5) independently, and checks the symmetric limiting formula and its asymptotic behavior. The proof of the infinite-population statement and the \(N^{-1}\) coefficient is analytic; quadrature over a finite sample of parameters is corroborative only.

## Relationship to prior work
Bressloff, *Global density equations for a population of actively switching particles* (arXiv:2310.03418, first submitted 2023-10-05), develops the population model with a shared Markov environment, its hybrid density formulation, and noise-induced particle correlations; Section 5 also treats an Ornstein–Uhlenbeck particle with Markov-switching drift. Its analyzed observables do not include the one-snapshot binary-state Bayes error, the irreducible infinite-population inference floor, or the sharp \(N^{-1}\) correction.

Herbach, *Stochastic gene expression with a multistate promoter* (arXiv:1804.05740), gives the beta/Dirichlet stationary distribution and the joint density proportional to \(u f(u)\) for its two-state PDMP (Proposition 4.4). These are **strong prior mathematical coverage** of the stationary mixing step, fully credited above. The finite-\(N\) population inference theorem is not a claim of discovering that joint law.

Bäuerle, Gilitschenski, and Hanebeck, *Exact and Approximate Hidden Markov Chain Filters Based on Discrete Observations* (arXiv:1411.0849), derive posterior filtering formulas for noisy time-discrete observations of **time-integrated telegraph paths**. Their inference setting observes a time series, not a single stationary spatial sample from arbitrarily many independent Brownian particles in a common environment; their main formulas do not imply the evaluated \(N^{-1}\) snapshot-error correction without a separate specialization and asymptotic argument. Standard Gaussian-channel Bayes theory and the local small-noise expansion are methodological precedents, not claimed as new in themselves.

## Limitations
The model is linear and noninteracting, and all particles share an identical two-state environment. No claim is made for spatially heterogeneous forcing, temporal sequences of observations, parameter uncertainty, asymmetric decision costs, or correlated thermal noises. The \(o(N^{-1})\) remainder holds at fixed positive model parameters; it is not uniform in extreme switching regimes. The plateau is a limitation of **one simultaneous snapshot**, not of high-frequency time-resolved sensing. A more general inference theorem may imply the result; mathematical correctness does not independently establish publication priority.

## References
1. P. C. Bressloff, *Global density equations for a population of actively switching particles*, arXiv:2310.03418 (first public 2023-10-05), J. Phys. A 57 (2024) 085001. https://arxiv.org/abs/2310.03418.
2. U. Herbach, *Stochastic gene expression with a multistate promoter: breaking down exact distributions*, arXiv:1804.05740 (2018), SIAM J. Appl. Math. https://arxiv.org/abs/1804.05740.
3. N. Bäuerle, I. Gilitschenski and U. D. Hanebeck, *Exact and Approximate Hidden Markov Chain Filters Based on Discrete Observations*, arXiv:1411.0849 (2014), Stat. Risk Model. https://arxiv.org/abs/1411.0849.
