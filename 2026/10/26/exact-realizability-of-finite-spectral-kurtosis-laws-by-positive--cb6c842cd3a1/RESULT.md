# Exact realizability of finite spectral kurtosis laws by positive Markov-switching diffusivities

## Finding

Fix any positive mean diffusivity \(\mu>0\). Let \(K(z)=2(z-1+e^{-z})/z^2\) for \(z>0\), with \(K(0)=1\). For scalar Brownian motion with **strictly positive diffusivity** modulated by a stationary, irreducible, reversible, finite-state continuous-time Markov chain independent of the driving Brownian motion, the normalized displacement excess kurtosis
\[
\alpha(t)=\frac{\mathbb E[X_t^4]}{3(\mathbb E[X_t^2])^2}-1,\qquad t>0,
\]
is **exactly** a finite nonnegative combination
\[
\alpha(t)=\frac{1}{\mu^2}\sum_{j=1}^{m}w_j K(\lambda_jt),
\quad \lambda_j>0,\quad w_j>0,
\]
with distinct observable relaxation rates \(\lambda_j\); the empty sum is allowed. Conversely, **every** finite choice of distinct rates and positive weights, with no upper restriction on weights at prescribed \(\mu\), is realizable by such a system with at most \(2^m\) states and a strictly positive diffusivity at every state. The entire observed curve uniquely identifies its active rates and normalized weights; it does not identify the switching microphysics. This is a classification of kurtosis time curves, not of the full displacement laws.

## Assumptions and scope

Let \(Y_t\) be a stationary irreducible continuous-time Markov chain on a finite labeled state set \(S\), with generator \(Q\), invariant probability \(\pi(s)>0\), and detailed balance \(\pi(s)Q(s,s')=\pi(s')Q(s',s)\). Let \(d:S\to(0,\infty)\), and set \(D_t=d(Y_t)\) with \(\mu=\sum_s\pi(s)d(s)\). Independently take standard real Brownian motion \(W\), and define \(X_t=\int_0^t\sqrt{2D_u}\,dW_u\). All expectations use the stationary initial law of \(Y\). No fixed upper bound on \(d\) is assumed; imposing one may restrict the attainable weights. Rates are finite and positive; coincident rates are merged. The empty mixture is realized by constant \(d\).

## Proof

**1. Moment reduction.** Write \(A_t=\int_0^t D_s\,ds\). Conditional on the full diffusivity path, \(X_t\) is centered Gaussian with variance \(2A_t\), because \(W\) is independent. Consequently
\[
\mathbb E[X_t^2]=2\mu t,\qquad
\mathbb E[X_t^4]=12\mathbb E[A_t^2],\qquad
\mu^2t^2\alpha(t)=\operatorname{Var}(A_t).
\]
If \(C(u)=\operatorname{Cov}(D_0,D_u)\), stationarity and symmetry of covariance imply
\[
\mu^2t^2\alpha(t)=2\int_0^t(t-u)C(u)\,du. \tag{1}
\]

**2. The necessary positive spectral mixture.** With inner product \(\langle f,g\rangle_\pi=\sum_s\pi(s)f(s)g(s)\), reversibility makes \(Q\) self-adjoint. Since the chain is irreducible, its constants form the simple kernel, and the nonconstant eigenvalues of \(-Q\) are strictly positive. Expand \(f=d-\mu\) into its orthogonal spectral projections. For each distinct positive eigenvalue \(\lambda_j\) with nonzero projection, let \(w_j=\|P_{\lambda_j}f\|_\pi^2>0\). Then
\[
C(u)=\langle f,e^{uQ}f\rangle_\pi=\sum_{j=1}^m w_j e^{-\lambda_ju}.
\]
Substituting in (1), integrating exactly, and noting \(\int_0^t(t-u)e^{-\lambda u}\,du=(\lambda t-1+e^{-\lambda t})/\lambda^2\) gives the asserted \(K\)-mixture.

**3. Constructive sufficiency at an arbitrary prescribed mean.** Start with arbitrary \(m\geq1\), distinct \(\lambda_j>0\), \(w_j>0\), and \(\mu>0\). Choose *any* \(h_j>0\) satisfying \(\sum_jh_j<\mu\). Put
\[
p_j=\frac{h_j^2}{h_j^2+w_j}\in(0,1),\qquad
 a_j=\frac{h_j^2+w_j}{h_j}>0,\qquad
 d_0=\mu-\sum_jh_j>0.
\]
For each \(j\), independently evolve a stationary binary chain \(B_j(t)\in\{0,1\}\), switching from \(0\) to \(1\) at rate \(\lambda_jp_j\) and from \(1\) to \(0\) at rate \(\lambda_j(1-p_j)\). Its invariant \(1\)-probability is \(p_j\), and \(\operatorname{Cov}(B_j(0),B_j(t))=p_j(1-p_j)e^{-\lambda_jt}\). Take the joint chain \(Y=(B_1,\ldots,B_m)\) on \(\{0,1\}^m\), with observable
\[
D_t=d_0+\sum_{j=1}^m a_jB_j(t).
\]
Every state has diffusivity at least \(d_0>0\); all binary flip rates are positive, so the product chain is irreducible, stationary, and reversible. Crucially, \(a_jp_j=h_j\) and \(a_j^2p_j(1-p_j)=w_j\). Therefore \(\mathbb ED_t=d_0+\sum_jh_j=\mu\), while independence eliminates cross covariances and gives \(C(t)=\sum_jw_je^{-\lambda_jt}\). The first two proof steps yield **exactly** the prescribed \(\alpha\) for every \(t>0\). The product generator has other possible eigenvalues, but the linear observable \(d-\mu\) has no projection onto their higher-order tensor-product eigenfunctions, so no unwanted term occurs.

**4. Identification and nonidentification.** Twice differentiating (1), valid for finite exponential sums, recovers
\[
C(t)=\frac{\mu^2}{2}\frac{d^2}{dt^2}\left(t^2\alpha(t)\right).
\]
Finite sums of exponentials with distinct real exponents have unique coefficients and exponents (successively isolate the slowest rate as \(t\to\infty\), then subtract and repeat), hence the full exact curve and \(\mu\) uniquely determine every active \(\lambda_j,w_j\). Nevertheless, the freely chosen positive tuple \((h_j)_j\) ranges over an open simplex and changes, for instance, the minimum realized diffusivity \(d_0\) while preserving \(\mu,C,\alpha\); thus the microscopic chain and state diffusivities are not uniquely identified. Finally \(K(z)=2\int_0^1(1-u)e^{-zu}\,du\) implies each nonzero admissible curve is strictly decreasing and completely monotone, but these forward qualitative facts alone are not the converse construction.

## Verification

The accompanying `verification/verify.py` enumerates several rational-parameter product chains on \(2,4,8\) states, constructs their generators and stationary probabilities with exact rational arithmetic, checks positivity, exact mean, row sums, detailed balance, and verifies that the observable eigenmodes have precisely the prescribed rates, weights, and no extra active modes. It separately checks the resulting covariance exponentials at three positive times. Run with `python3 verification/verify.py` (standard library only). Its printed `EXACT_VERIFY_OK` lines certify the enumerated examples, **not** the general theorem, which follows from the analytic steps above.

## Relationship to prior work

Chubynsky–Slater (first public 2014-04-14) introduced fluctuating diffusivity to explain Brownian mean-square displacement with non-Gaussian displacement statistics; its discrete-time fourth-moment relation already connects displacement non-Gaussianity to diffusivity correlations. Uneyama–Miyaguchi–Akimoto (first public 2014-11-19) derived general time-averaged displacement fluctuations from diffusivity autocorrelation and analyzed binary Markov examples. Miyaguchi–Akimoto–Yamamoto (first public 2016-04-30) treated two-state fluctuating diffusivity. Jensen (first public 2023-11-13) explicitly obtained the **forward** multicomponent Kärger kurtosis spectral formula and log-convexity, so neither the positive spectral expansion nor its monotonicity is claimed here as new. Erland–Greenwood (2007) addresses spectral design of reversible Markov noise. The proposed additional classification is the **converse at fixed positive mean**: arbitrary positive finite relaxation spectra and amplitudes are attainable with no hidden positivity obstruction by an explicit stationary positive Markov diffusivity, paired with uniqueness of the observable spectral data and nonuniqueness of the kinetics.

## Limitations

This theorem assumes a finite-state reversible stationary chain and a Brownian driver independent of it. It does not characterize nonreversible switching, continuous-state or nonstationary diffusivity, experimental finite-sample reconstruction, higher displacement moments, or the full displacement distribution. No uniform upper cap on diffusivity is imposed. Infinite spectral measures are not asserted realizable by finite chains. Full text of the particularly relevant 2023 Jensen article and the 2007 Erland–Greenwood article could not be accessed; their available abstracts and metadata were compared, but possible unobserved inverse-construction statements remain a publication-priority risk. The work has undergone a self-review only; no independent audit or external experimental validation has been performed.

## References

1. M. V. Chubynsky and G. W. Slater, “Diffusing diffusivity”: A model for anomalous and “anomalous yet Brownian” diffusion, arXiv:1404.3573v1 (2014-04-14), https://arxiv.org/abs/1404.3573.
2. T. Uneyama, T. Miyaguchi, and T. Akimoto, Fluctuation Analysis of Time-Averaged Mean-Square Displacement for Langevin Equation with Time-Dependent and Fluctuating Diffusivity, arXiv:1411.5165v1 (2014-11-19), https://arxiv.org/abs/1411.5165.
3. T. Miyaguchi, T. Akimoto, and E. Yamamoto, Langevin equation with fluctuating diffusivity: a two-state model, arXiv:1605.00106v1 (2016-04-30), https://arxiv.org/abs/1605.00106.
4. J. H. Jensen, Diffusional kurtosis time dependence and the water exchange rate for the multi-compartment Kärger model, *Magnetic Resonance in Medicine* **91** (2024), 1122–1135; first published 2023-11-13; DOI:10.1002/mrm.29926.
5. S. Erland and P. E. Greenwood, Constructing 1/omega-alpha noise from reversible Markov chains, *Physical Review E* **76** (2007), 031114; DOI:10.1103/PhysRevE.76.031114.
