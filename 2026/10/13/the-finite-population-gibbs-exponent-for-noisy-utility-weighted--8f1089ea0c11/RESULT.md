# The finite-population Gibbs exponent for noisy utility-weighted opinion averaging

## Finding

**Theorem (fixed-population, weak-noise limit).** Fix an integer \(N\geq2\), a learning rate \(0<\mu<1\), and a confidence radius \(\varepsilon>0\). Let \(U:\mathbb R\to(0,\infty)\) be a \(C^3\) utility with bounded first, second, and third derivatives of \(\ell=\log U\). At each microscopic step select an unordered pair of distinct agents uniformly and independently. If their opinions are less than \(\varepsilon\) apart, update **only** those two agents by
\[
 x_i^+=x_i+2\mu\frac{U(x_j)}{U(x_i)+U(x_j)}(x_j-x_i)+\Delta\xi_i,\qquad
 x_j^+=x_j+2\mu\frac{U(x_i)}{U(x_i)+U(x_j)}(x_i-x_j)+\Delta\xi_j,
\]
where fresh \(\xi_i,\xi_j\) are independent standard Gaussians, independent also of the selected pair and all previous steps. If the pair fails the confidence test, no update takes place. Initialize at \(x_i(0)=x_0+\Delta z_i\), for fixed real \(z_i\) with \(\sum_i z_i=0\). With \(X_k=N^{-1}\sum_i x_i(k)\), linearly interpolate \(X_k\) at accelerated times \(s=k\Delta^2/N\), obtaining \(Z^\Delta_s\).

For every finite \(T>0\), as \(\Delta\downarrow0\), \(Z^\Delta\) converges weakly in \(C([0,T])\) to the unique solution of
\[
 \boxed{\quad dZ_s=\frac{N-1}{N(1-\mu)}\ell'(Z_s)\,ds+\sqrt{\frac2N}\,dW_s,\qquad Z_0=x_0.\quad}
\]
In particular, if \(\int_{\mathbb R}U(x)^{(N-1)/(1-\mu)}\,dx<\infty\), the **limiting diffusion** has the unique invariant probability density
\[
 \boxed{\quad p_\infty(x)=\frac{U(x)^{(N-1)/(1-\mu)}}{\int_{\mathbb R}U(u)^{(N-1)/(1-\mu)}\,du}.\quad}
\]
Thus, when population size is fixed before sending microscopic noise to zero, the effective Gibbs exponent is exactly \((N-1)/(1-\mu)\), rather than the large-population approximation \(N/(1-\mu)\). The distinction arises even though the limiting center diffusion coefficient \(1/N\) agrees with the leading approximation.

A neutral-utility identity underlying the theorem is also exact: in the unrestricted-pair model with constant \(U\), the unique stationary distribution of centered disagreements has
\[
 \mathbb E\left[\frac1N\sum_{i=1}^N(x_i-X)^2\right]
 =\frac{(N-1)^2}{N^2}\frac{\Delta^2}{2\mu(1-\mu)}.
\]
Here the center itself need not possess a stationary distribution. The theorem asserts a finite-time weak-noise limit, not interchange of a microscopic stationary limit with \(\Delta\downarrow0\).

## Assumptions and scope

The population size is fixed; no \(N\to\infty\) limit is taken. Time at each microscopic update equals \(1/N\), following the motivating model. Only two selected opinions receive noise. The strict confidence inequality has no effect on the limiting dynamics on a finite accelerated horizon: with probability approaching one, every selected pair is within confidence throughout that horizon. The bound \(\varepsilon>0\) is fixed independently of \(\Delta\).

The smoothness and boundedness hypotheses on \(\ell\) ensure uniform local Taylor estimates and globally Lipschitz limiting drift. The limiting invariant-density assertion is conditional on integrability of the displayed power of \(U\); neither finite-noise stationarity nor a uniform-in-time diffusion approximation is asserted. Finite or infinite confidence thresholds are both represented by the same result, with the unrestricted-pair model providing the comparison process.

For example, with \(N=2\), \(\mu=1/2\), and \(U(x)=(1+x^2)^{-1}\), the limiting invariant density is \(2/[\pi(1+x^2)^2]\). The large-population closure would instead assign exponent \(4\) to \(U\), while the exact fixed-population exponent is \(2\). Both are proper densities but are different.

## Proof

**1. Centered update and exact neutral contraction.** Let \(P=I-\mathbf1\mathbf1^\top/N\), \(Y_k=P x(k)/\Delta\), \(v_{ij}=e_i-e_j\), and \(S(y)=\|y\|_2^2\). Write \(\ell=\log U\) and
\[
 d_{ij}=\frac{U(x_j)-U(x_i)}{U(x_j)+U(x_i)}
 =\tanh\left(\frac{\ell(x_j)-\ell(x_i)}2\right).
\]
During a permitted interaction, with \(A_{ij}=I-\mu v_{ij}v_{ij}^{\top}\) and \(\zeta=\xi_i e_i+\xi_j e_j\), exact algebra gives
\[
 Y_{k+1}=A_{ij}Y_k+\mu d_{ij}(Y_{k,j}-Y_{k,i})P(e_i+e_j)+P\zeta,
\]
and
\[
 X_{k+1}-X_k=\frac{2\mu}{N}d_{ij}(x_j-x_i)+\frac\Delta N(\xi_i+\xi_j).
\]
For constant utility, \(d_{ij}=0\). Because \(Y\) is centered, the pair identity is
\[
 \frac1{\binom N2}\sum_{i<j}(Y_i-Y_j)^2=\frac2{N-1}S(Y).
\]
Also, \(\|A_{ij}Y\|^2=S(Y)-2\mu(1-\mu)(Y_i-Y_j)^2\) and the fresh centered noise has expected squared norm \(2(1-1/N)\). Consequently
\[
 \mathbb E[S(Y_{k+1})\mid Y_k]
 =aS(Y_k)+\frac{2(N-1)}N,\qquad
 a=1-\frac{4\mu(1-\mu)}{N-1}\in[0,1).
\]
The neutral Markov chain contracts synchronously in mean square by factor \(a\), so its invariant law exists and is unique, with finite moments of every fixed order. At stationarity,
\[
 \overline S=\frac{(N-1)^2}{2N\mu(1-\mu)},\qquad
 \overline h=\mathbb E\left[\frac1{\binom N2}\sum_{i<j}(Y_i-Y_j)^2\right]
 =\frac{N-1}{N\mu(1-\mu)}.
\]
Rescaling \(Y=(x-X\mathbf1)/\Delta\) yields the stated **exact** neutral disagreement variance.

**2. Uniform small-noise localization.** The bounded derivative of \(\ell\) gives \(|d_{ij}|\le C\Delta|Y_i-Y_j|\). Hence the nonlinear term in the centered update has norm at most \(C\Delta S(Y)\). Stop the unrestricted-pair process when \(\Delta\|Y\|\) first exceeds a sufficiently small \(r>0\), with \(r<\varepsilon/4\). For its deterministic neutral part,
\[
 \mathbb E_{ij}\|A_{ij}Y\|^4\le S(Y)\,\mathbb E_{ij}\|A_{ij}Y\|^2=aS(Y)^2.
\]
Since \(a<1\), Young's inequality and the finite fourth moments of Gaussian increments show, after choosing \(r\) sufficiently small, that the one-step fourth moment before stopping is at most \(q S(Y)^2+C\) for fixed \(q<1\), uniformly in \(\Delta\). Iteration gives a uniform pre-exit fourth-moment bound. For \(k\le NT/\Delta^2\), Markov's inequality and a union bound on the first exit now give
\[
 \mathbb P\left(\max_{k\le NT/\Delta^2}\Delta\|Y_k\|\ge r\right)
 \le C_T\Delta^2\longrightarrow0.
\]
Indeed, on each pre-exit step an exit requires \(\|Y_{k+1}\|\ge r/\Delta\), and its fourth moment is uniformly bounded. Since every pairwise distance is at most \(2\Delta\|Y\|\), the all-pairs process and the actual confidence-limited process coincide with probability tending to one on the stated horizon. All subsequent estimates may therefore use stopped all-pairs dynamics.

**3. Exact fast-observable averaging.** Set
\[
 h(y)=\frac2{N-1}S(y),\qquad
 c=\frac{4\mu(1-\mu)}{N-1}.
\]
Expanding the exact centered update, and using the fourth-moment bound, gives the conditional identity
\[
 \mathbb E[h(Y_{k+1})-h(Y_k)\mid\mathcal F_k]
 =-c(h(Y_k)-\overline h)+R_k^\Delta,
\]
where \(\mathbb E|R_k^\Delta|\le C\Delta\) uniformly before exit. More explicitly, the error is bounded by \(C\Delta S(Y_k)^{3/2}+C\Delta^2 S(Y_k)^2\). The centered difference between the left side's increment and its conditional mean is a square-integrable martingale increment with uniformly bounded second moment.

For \(f_k=\ell'(X_k)\), the bounded second derivative of \(\ell\) and the exact mean increment imply \(\mathbb E|f_{k+1}-f_k|^2\le C\Delta^2\). Multiply the preceding conditional identity by \(f_k\) and sum. Discrete summation by parts makes the weighted \(h_{k+1}-h_k\) sum a boundary term plus increments \((f_{k+1}-f_k)h_{k+1}\); Cauchy--Schwarz, the fourth-moment bound, and multiplication by \(\Delta^2\) make these terms vanish. The \(R_k^\Delta\) sum contributes \(O(\Delta)\), and Doob's inequality makes the rescaled martingale term vanish, uniformly for at most \(NT/\Delta^2\) steps. Thus
\[
 \sup_{m\le NT/\Delta^2}\left|
 \Delta^2\sum_{k<m}\ell'(X_k)(h(Y_k)-\overline h)
 \right|\xrightarrow{\mathbb P}0.
\]
No unverified Gaussian approximation for the invariant disagreement law is used: only its exact quadratic moment and the preceding martingale averaging identity are needed.

**4. Slow drift and diffusion.** Uniform Taylor expansion about the current mean gives
\[
 d_{ij}=\tfrac12\ell'(X_k)\Delta(Y_{k,j}-Y_{k,i})
 +O(\Delta^2 S(Y_k)),
\]
so the mean update satisfies
\[
 X_{k+1}-X_k
 =\frac{\Delta^2\mu}{N}\ell'(X_k)(Y_{k,j}-Y_{k,i})^2
 +\frac\Delta N(\xi_i+\xi_j)+O(\Delta^3 S(Y_k)^{3/2}).
\]
Conditional averaging over pairs replaces the squared difference by \(h(Y_k)\). The pair-selection fluctuation is another square-integrable martingale whose \(\Delta^2\)-weighted partial sums vanish uniformly on the accelerated horizon. Step 3 replaces \(h(Y_k)\) by \(\overline h\). The sum of Gaussian mean-noise increments has, **exactly**, conditional variance \(2\Delta^2/N^2\) per update, hence converges after the time change \(s=k\Delta^2/N\) to \(\sqrt{2/N}\,W_s\). The drift per unit accelerated time is
\[
 \mu\overline h\,\ell'(x)
 =\frac{N-1}{N(1-\mu)}\ell'(x).
\]
The uniform error bounds, martingale functional central limit theorem, and Lipschitzness of \(\ell'\) imply weak convergence of the interpolated mean to the asserted unique SDE solution.

**5. Limiting stationary density.** The limit generator is \(Lf=b(x)f'(x)+(1/N)f''(x)\), with \(b(x)=(N-1)\ell'(x)/[N(1-\mu)]\). Its zero-current stationary equation is \(p'/p=Nb=(N-1)\ell'/(1-\mu)\). Integration gives exactly \(p\propto U^{(N-1)/(1-\mu)}\). If normalizable, this strictly positive density is invariant; uniform ellipticity and irreducibility of the one-dimensional diffusion give uniqueness. This proves only the invariant law of the **limiting** process, not a stationary law for the original microscopic chain.

## Verification

A standard-library Python verifier, `verify.py`, independently constructs all pairwise averaging matrices and projected pair-noise covariance matrices with exact rational arithmetic. For population sizes \(2\le N\le10\) and five rational learning rates it checks the full neutral covariance balance, pairwise quadratic identity, exact stationary disagreement moment, accelerated drift and diffusion coefficients, and corrected Gibbs exponent. Execute with `python3 verify.py`; expected output:

`VERIFY_OK: 45 exact rational covariance, mixing and inverse-temperature checks`

These finite matrix checks independently validate the algebraic constants but do not establish weak convergence. The latter is supported by the analytic moment, localization, martingale averaging, and functional-CLT proof above.

## Relationship to prior work

Siebenmorgen and Restrepo (2026), Eq. (15) and Supplementary Appendices A--F, derive the large-population/small-cluster approximation \(p\propto U^{N/(1-\mu)}\). Their Appendix A explicitly notes that distinct centered opinions are slightly anticorrelated at finite \(N\) and drops the correction in the drift closure; Appendix F also uses a Gaussian approximation for individual deviations. The present result keeps the exact finite-pair covariance and proves a fixed-\(N\), small-noise limit, resulting in the shifted exponent \((N-1)/(1-\mu)\). It is not a contradiction of their leading large-\(N\) approximation: the relative correction is \(1/N\).

Xing and Johansson (2024) prove concentration of expected final and time-averaged opinions in random-graph gossip **with stubborn agents**, not utility-induced weak-noise diffusion of an unrestricted mean. Acemoğlu, Como, Fagnani, and Ozdaglar (2013) analyze stochastic gossip with stubborn agents and persistent disagreement, and Mathkar and Borkar (2016) analyze nonlinear stochastic-approximation gossip toward deterministic limiting trajectories. General martingale and averaging methods are background techniques, not claimed as new.

## Limitations

The result requires initially near-consensus opinions, fixed \(N\) and fixed \(\mu\in(0,1)\), independent Gaussian noise on the selected pair, and a smooth strictly positive opinion-only utility with bounded derivatives of its logarithm. It concerns convergence on each **finite accelerated time horizon**. It does not establish a uniform approximation as \(T\to\infty\), convergence of finite-noise stationary distributions to the displayed invariant law, metastable switching-time asymptotics, a simultaneous \(N\to\infty\) limit, or a theorem for heterogeneous update rates or utility depending on all opinions. The neutral disagreement moment is exact only for all-pairs interactions with constant utility; in the nonlinear model it appears as the leading local fast-mode moment.

## References

1. A. Siebenmorgen and J. G. Restrepo, *A Utility-Driven Bounded-Confidence Model for Opinion Dynamics*, arXiv:2605.21844v1, first submitted 21 May 2026. https://arxiv.org/html/2605.21844v1 . Relevant: model Eq. (1), mean diffusion Eqs. (5)--(15), Supplementary Appendices A--F.
2. Y. Xing and K. H. Johansson, *Concentration in Gossip Opinion Dynamics over Random Graphs*, arXiv:2301.05352v4 (2024). https://arxiv.org/html/2301.05352v4 . Relevant: Sections 2 and 4, Theorems 9 and 17.
3. D. Acemoğlu, G. Como, F. Fagnani and A. Ozdaglar, *Opinion Fluctuations and Disagreement in Social Networks*, Mathematics of Operations Research 38 (2013), 1--27, arXiv:1009.2653. https://arxiv.org/abs/1009.2653 .
4. A. S. Mathkar and V. S. Borkar, *Nonlinear Gossip*, SIAM J. Control Optim. 54 (2016), 1535--1557, DOI:10.1137/140992588. https://doi.org/10.1137/140992588 .
