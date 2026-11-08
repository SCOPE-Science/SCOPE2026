# A non-self-averaging Beta limit and a persistent density gap for the noisy voter model on stars

## Finding

Fix a noise rate \(q>0\). On the star \(K_{1,b}\), each vertex at rate one copies the opinion of a uniformly chosen neighbor, and at independent rate \(q\) replaces its opinion by an unbiased binary opinion. In the unique stationary law, let \(H_b\in\{0,1\}\) be the hub opinion and \(Y_b\) the fraction of leaves with opinion one. Put
\[
 c=1+q,\qquad \alpha=\frac{q}{2(1+q)},\qquad
 \theta=\frac{q(q+2)}{2(1+q)^2}.
\]
For every fixed \(q>0\), as the number \(b\) of leaves tends to infinity,
\[
 (H_b,c(Y_b-\alpha))\ \xrightarrow{\mathrm d}\ (H,Z),
 \quad Z\sim\operatorname{Beta}(\theta,\theta),\quad
 \Pr(H=1\mid Z=z)=z.
\]
Consequently the unweighted leaf fraction remains random, rather than self-averaging:
\[
 \lim_{b\to\infty}\operatorname{Var}(Y_b)=
 \frac{1}{4(1+4q+2q^2)}>0.
\]
The degree-weighted opinion density \(S_b=(H_b+Y_b)/2\) also converges in distribution. Its limiting support is precisely
\[
 \left[\frac\alpha2,\frac{1-\alpha}{2}\right]
 \ \cup\ 
 \left[\frac{1+\alpha}{2},1-\frac\alpha2\right],
\]
leaving an open gap of length \(\alpha>0\) for every fixed positive noise rate. In particular, neither a single Gaussian nor a Bernoulli limit describes this star-graph regime.

An additional exact finite-size identity, valid for every \(b\ge2\), is
\[
 \operatorname{Var}(Y_b)=\frac{1+(b-1)\ell_b}{4b},\qquad
 \ell_b=\frac{1+b^{-1}}{1+b^{-1}+4q+2q^2}.
\]

## Assumptions and scope

The graph has one distinguished hub and \(b\ge2\) leaves, with no self-loops. Each vertex has an independent rate-one imitation clock and independent rate-\(q\) reset clock; an imitation chooses one neighbor uniformly, while a reset chooses zero and one with probability \(1/2\) each. Clocks and reset bits are independent. Time is continuous and the stationary distribution is considered before taking \(b\to\infty\), with \(q\) fixed and strictly positive. The unbiased reset makes every finite labeled configuration communicate with every other, so there is a unique stationary law. The limit variable \(H\) is not claimed to be independent of \(Z\).

Write \(K_b=bY_b\). By leaf permutation invariance, the pair \((H_b,K_b)\) is a Markov chain. At state \((h,k)\), its transition rates are
\[
 \begin{array}{c|c}
 (h,k)\to(h,k+1)&(b-k)(h+q/2)\\
 (h,k)\to(h,k-1)&k(1-h+q/2)\\
 (0,k)\to(1,k)&k/b+q/2\\
 (1,k)\to(0,k)&1-k/b+q/2.
 \end{array}
\]
Transitions outside the state space have rate zero.

## Proof

**1. Compact-limit generator.** On \(E=\{0,1\}\times[0,1]\), write \(y=k/b\) and \(a=q/2\), \(c=1+q\). Taylor expansion of the displayed finite-state rates yields, uniformly for functions that are twice continuously differentiable in the second coordinate,
\[
 \mathcal L f(h,y)=(h+a-cy)\,\partial_y f(h,y)
 +\lambda_h(y)\bigl[f(1-h,y)-f(h,y)\bigr],
\]
where \(\lambda_0(y)=y+a\) and \(\lambda_1(y)=1-y+a\). Indeed, the infinitesimal leaf drift is exactly \(h+a-cy\), and the second-order Taylor remainder is bounded by a constant (depending on the test function and \(q\)) divided by \(b\). The hub jump rates have no approximation error. Finite stationary laws on compact \(E\) have weakly convergent subsequences. Stationarity, uniform generator convergence, and continuity of \(\mathcal Lf\) show that any limit obeys \(\int \mathcal Lf\,d\nu=0\) for every such test function.

**2. Identification of the joint law.** Under the affine change \(z=c(y-\alpha)\), the limiting drifts for hub states zero and one are \(-cz\) and \(c(1-z)\), respectively. Their attracting fixed points are \(0\) and \(1\); accordingly the invariant interval in the original \(y\)-coordinate is \([\alpha,1-\alpha]\). The transformed hub flip rates are
\[
 \lambda_0(z)=c\theta+z/c,\qquad
 \lambda_1(z)=c\theta+(1-z)/c.
\]
Let \(f_\theta(z)=z^{\theta-1}(1-z)^{\theta-1}/B(\theta,\theta)\) for \(0<z<1\). The proposed joint densities for the hub state are
\[
 \rho_0(z)=(1-z)f_\theta(z),\qquad
 \rho_1(z)=zf_\theta(z).
\]
Their probability flux magnitude is \(J(z)=cz(1-z)f_\theta(z)\). Since \(\theta>0\), both boundary fluxes vanish; moreover
\[
 J'(z)=c\theta(1-2z)f_\theta(z)
 =\lambda_0(z)\rho_0(z)-\lambda_1(z)\rho_1(z).
\]
These are the two stationary transport-plus-switching equations, including their zero-flux boundary conditions. Thus the displayed joint densities define an invariant probability measure for the compact-limit generator. They also give \(\Pr(H=1\mid Z=z)=z\) and \(Z\sim\operatorname{Beta}(\theta,\theta)\).

**3. Uniqueness without an assumed ergodic theorem.** For any probability measure on \(E\) satisfying all the limiting generator identities, set \(v_m=\mathbb E[Y^m]\) and \(w_m=\mathbb E[H Y^m]\), with \(v_0=1\). Testing \(\mathcal L\) on \(y^m\) and \(hy^{m-1}\) gives, for all integers \(m\ge1\),
\[
 c v_m=a v_{m-1}+w_{m-1},
\]
\[
 mc\,w_{m-1}=(m-1)(1+a)w_{m-2}+a v_{m-1}+v_m,
\]
where the term with \(w_{-1}\) is absent at \(m=1\). Eliminating \(w_{m-1}\) yields
\[
 (mc^2-1)v_m=(mc a+a)v_{m-1}+(m-1)(1+a)w_{m-2}.
\]
Because \(c>1\), the coefficient on the left is strictly positive for every \(m\ge1\). The recursion uniquely determines \(v_m\) and \(w_{m-1}\) inductively starting from \(v_0=1\). Since polynomials are dense in continuous functions on \([0,1]\), all the moments uniquely determine both subprobability measures on the hub states. Every weak subsequential limit therefore equals the exhibited measure, proving full stationary weak convergence. The limiting dynamics cannot have stationary mass outside \([\alpha,1-\alpha]\) because this unique invariant law is supported there.

**4. Exact finite-star covariance and variance.** Use spin variables \(\sigma_v=2\eta_v-1\). By opinion-flip symmetry, each stationary spin has mean zero. For distinct leaves \(i,j\), let \(\ell_b=\mathbb E[\sigma_i\sigma_j]\) and \(d_b=\mathbb E[\sigma_h\sigma_i]\). Apply the finite generator to the products \(\sigma_i\sigma_j\) and \(\sigma_h\sigma_i\). Their stationary equations are
\[
 0=2d_b-2(1+q)\ell_b,
\qquad
 0=1+b^{-1}+(1-b^{-1})\ell_b-2(1+q)d_b.
\]
Elimination gives precisely \(\ell_b=(1+b^{-1})/(1+b^{-1}+4q+2q^2)\). Summing leaf variances and covariances establishes the finite-size identity. Its limit is \(1/[4(1+4q+2q^2)]\), independently matching the variance of \(\alpha+Z/c\) since \(\operatorname{Var}(Z)=1/[4(2\theta+1)]\).

**5. The degree-weighted gap.** A simple random walk on \(K_{1,b}\) has stationary vertex masses \(1/2\) at the hub and \(1/(2b)\) at each leaf; therefore its stationary-weighted binary density is \(S_b=(H_b+Y_b)/2\). Its limiting joint representation implies that \(S=(H+\alpha+Z/c)/2\). Conditional on \(H=0\), its support is \([\alpha/2,(1-\alpha)/2]\); conditional on \(H=1\), its support is \([(1+\alpha)/2,1-\alpha/2]\). Each interval is filled because \(0<\theta<1/2\) and the densities \(zf_\theta(z)\) and \((1-z)f_\theta(z)\) are strictly positive in their interiors. The two intervals are separated by a gap of length \(\alpha\).

## Verification

A self-contained standard-library Python checker (`verify.py`) solves exact rational stationary equations both for the full labeled spin chain and for the symmetry-lumped chain on nine finite cases: \(b\in\{2,3,4\}\) and \(q\in\{1/2,1,2\}\). It matches all aggregated state probabilities, stationary means, and the exact finite-star variance. It separately checks 212 exact rational stationary-generator and Beta-moment identities over five positive rational noise rates and moments through degree ten. The checker was executed on the packaged source and passed. These finite checks are supporting tests, not the proof of convergence for arbitrary \(b\), which is the compactness-and-moment argument above. Run `python verify.py` with Python 3 and no additional dependencies.

## Relationship to prior work

Pymar and Rivera, *Asymptotic behaviour of the noisy voter model density process* (arXiv:2112.01478, first public December 2, 2021), study the stationary-vertex-weighted density and Gaussian/Bernoulli regimes on general graphs. Their Gaussian sufficient condition explicitly fails for stars. The present joint star limit and its disconnected stationary-weighted support are not implied by their identified regimes.

Caligiuri and Galla, *Noisy voter models in switching environments* (arXiv:2305.19096, first public May 30, 2023), provide general two-state piecewise-deterministic stationary formulas **including state-dependent switching rates**. Those equations encompass the limiting density's algebra once the star-induced limiting generator is independently derived. The generic PDMP stationary formula is **not claimed as new** here. The new model-specific content is the finite-star stationary-to-PDMP convergence, the exact endogenous-hub conditional distribution, the persistent disconnected density support, and the finite-\(b\) covariance identity. Their studied external-influencer dynamics use distinct microscopic assumptions.

Mori, Hisakado, and Nakayama, *A voter model on networks and multivariate beta distribution* (arXiv:1810.05643), work with many voters per network node and multivariate Wright–Fisher diffusion, rather than one noisy hub coupled to individual leaves. Herrerías-Azcué and Galla, *Consensus and diversity in multi-state noisy voter models* (arXiv:1903.09198), study a different multi-opinion population model. Analogous Beta laws for different dynamics do not by themselves determine this finite-star stationary limit.

## Limitations

The result assumes a fixed positive per-vertex noise rate, unbiased binary resets, continuous time, uniform-neighbor imitation, and unweighted stars. It does not cover jointly vanishing noise and growing graph size, biased resets, non-star graphs, or time-dependent transient laws. The density in the limiting Beta formula can be obtained using pre-existing general PDMP formulas after the particular microscopic-to-limit reduction is established; historical novelty of some presentation or special-function identity is not independently certified. The verification script provides exact finite checks, not an independent mathematical audit.

## References

- R. Pymar and N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478 (first public 2021-12-02), https://arxiv.org/abs/2112.01478.
- A. Caligiuri and T. Galla, *Noisy voter models in switching environments*, arXiv:2305.19096 (first public 2023-05-30), https://arxiv.org/abs/2305.19096.
- S. Mori, M. Hisakado, K. Nakayama, *A voter model on networks and multivariate beta distribution*, arXiv:1810.05643 (first public 2018-10-12), https://arxiv.org/abs/1810.05643.
- P. Herrerías-Azcué and T. Galla, *Consensus and diversity in multi-state noisy voter models*, arXiv:1903.09198 (2019), https://arxiv.org/abs/1903.09198.
