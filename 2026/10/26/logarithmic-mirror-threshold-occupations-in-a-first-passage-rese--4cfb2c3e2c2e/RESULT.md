# Logarithmic mirror-threshold occupations in a first-passage resetting Brownian gas

## Finding

Fix a real threshold \(L>0\), diffusivity \(D>0\), and an integer \(N\geq3\). Consider \(N\) independent one-dimensional Brownian motions with generator \(D\partial_{xx}\), all reset simultaneously to zero whenever any particle first reaches \(+L\). Let \((X_1,\ldots,X_N)\) have the unique stationary distribution and define the opposite-threshold occupation count
\[
K_N=\#\{i:X_i<-L\}.
\]
Let \(A_N>0\) be the stationary age since the latest collective reset, and define the dimensionless trigger-proximity variable
\[
Z_N=N\operatorname{erfc}\!\left(\frac{L}{\sqrt{4DA_N}}\right).
\]
For every fixed integer \(k\ge1\) and every bounded continuous function \(f:[0,\infty)\to\mathbb R\),
\[
\boxed{\displaystyle
\lim_{N\to\infty}(\log N)\,\mathbb E\big[f(Z_N)\,\mathbf 1_{\{K_N=k\}}\big]
=\frac1{2^k k!}\int_0^\infty f(z)z^{k-1}e^{-3z/2}\,dz.}
\]
Consequently,
\[
\boxed{\displaystyle
\lim_{N\to\infty}(\log N)\,\mathbb P(K_N=k)=\frac1{k3^k},\qquad
\lim_{N\to\infty}(\log N)\,\mathbb P(K_N\ge1)=\log\frac32.}
\]
Conditionally on the rare event \(K_N\ge1\), the count has the logarithmic-series limit
\[
\boxed{\displaystyle
\mathbb P(K_N=k\mid K_N\ge1)\longrightarrow
\frac{1}{k3^k\log(3/2)},\quad k\ge1.}
\]
For each fixed \(k\ge1\), the trigger-proximity variable conditional on \(K_N=k\) converges in distribution to a Gamma law of shape \(k\) and rate \(3/2\). These are statements about stationary *instantaneous positions*, not prior excursions' running minima or their entire path occupation.

## Assumptions and scope

The Brownian paths and successive reset cycles are independent and fresh. Every particle has the same \(D\), the same reset trigger \(+L\), and zero starting location after reset. The stationary law exists for \(N>2\). No drift, state-dependent diffusivity, extra resetting, interaction between particles or observation noise is assumed. The limit is \(N\to\infty\) with \(L,D\) fixed and \(k\ge1\) fixed. The threshold \(-L\) is physically distinguished as the mirror of the reset trigger, not an arbitrary spatial slice; it is the endpoint of the leading-order limiting support for the most negative positions derived previously.

## Proof

**1. Exact stationary count-and-age law.** Put \(a=L^2/(4D)\), \(u=\sqrt{a/t}\), \(p(t)=\operatorname{erfc}(u)\) and \(S(t)=\operatorname{erf}(u)=1-p(t)\). For a fresh unconstrained Brownian particle started at zero, the reflection principle gives survival below \(+L\) until time \(t\) with probability \(S(t)\). The killed density is
\[
G(x,t)=\frac{e^{-x^2/(4Dt)}-e^{-(x-2L)^2/(4Dt)}}{\sqrt{4\pi Dt}}\,\mathbf 1_{\{x<L\}}.
\]
Its mass below the mirror level \(-L\) is exactly
\[
q(t)=\int_{-\infty}^{-L}G(x,t)\,dx
=\frac{\operatorname{erfc}(u)-\operatorname{erfc}(3u)}2.
\]
Indeed the two Gaussian tails are those at \(-L\) and \(-3L\); the second comes from the absorbed-path image. The cycle lifetime is the minimum of the \(N\) independent individual hitting times. Its survival is \(S(t)^N\), and its finite mean is
\[
\mu_N=\int_0^\infty S(t)^Ndt<\infty\quad (N>2),
\]
since \(S(t)=O(t^{-1/2})\) as \(t\to\infty\). Renewal-reward theory, or the known exact stationary renewal density, yields
\[
\mathbb P(K_N=k,A_N\in dt)=\frac{1}{\mu_N}\binom Nk q(t)^k [S(t)-q(t)]^{N-k}dt,
\quad k=0,\ldots,N.
\]
This is a nonnegative finite-time *subprobability* calculation with mass \(S(t)^N\); no independence of the unconditional stationary particle locations is asserted. More generally,
\[
\mathbb E[f(Z_N)\mathbf 1_{\{K_N=k\}}]
=\frac a{\mu_N}\int_0^\infty \frac{dy}{y^2}
\binom Nk q_y^k(S_y-q_y)^{N-k}
 f(Np_y),
\]
where \(y=a/t\), \(p_y=\operatorname{erfc}(\sqrt y)\), \(S_y=1-p_y\), \(q_y=[p_y-\operatorname{erfc}(3\sqrt y)]/2\). The integral is well defined also at the endpoints because of the positive killed density.

**2. Trigger-layer scale and cycle normalization.** Set
\[
y_N=\big[\operatorname{erfc}^{-1}(1/N)\big]^2.
\]
The standard complementary-error-function tail gives
\[
p_y=\frac{e^{-y}}{\sqrt{\pi y}}\big(1+O(y^{-1})\big)
\quad(y\to\infty),\qquad y_N\sim\log N.
\]
For each fixed real \(w\), at \(y=y_N+w\),
\[
Np_y\to e^{-w},\quad
Nq_y\to\frac12e^{-w},\quad
N(S_y-q_y-1)\to-\frac32e^{-w}.
\]
The image tail \(\operatorname{erfc}(3\sqrt y)\) is exponentially smaller than \(p_y\) in this layer. Rescale \(y=y_Nv\) in the cycle mean:
\[
\mu_N=a\int_0^\infty y^{-2}S_y^N\,dy
\sim\frac a{y_N}.
\]
For \(v>1\), the factor \(S_{y_Nv}^N\to1\); for \(0<v<1\), it tends to zero. Integrability near \(v=0\) follows by cutting at \(y=1\): on \((0,1)\), \(S_y^N\le S_1^{N-4}S_y^4\) and \(y^{-2}S_y^4\) is bounded; on \([1,(1-\varepsilon)y_N]\), \(S_y^N\) is exponentially small in a positive power of \(N\). The upper tail is dominated by \(y^{-2}\). These estimates justify the limiting step profile and its integral.

**3. Rare-count layer.** For any fixed \(k\ge1\), Stirling's finite-\(k\) binomial relation and the limits in step 2 give, at \(y=y_N+w\),
\[
\binom Nk q_y^k(S_y-q_y)^{N-k}
\longrightarrow \frac{e^{-kw}}{2^k k!}\exp\!\left(-\frac32e^{-w}\right).
\]
For \(w\) outside any fixed bounded window, this integrand admits an integrable dominating envelope: on \(y\ge y_N/2\), Gaussian-tail ratios bound \(Np_y\) above and below by constant multiples of \(e^{-w}\), while the integrand is bounded by a constant multiple of \((Np_y)^k e^{-cNp_y}\); for \(y<y_N/2\), \(S_y^{N-k}\) gives a contribution exponentially small in a positive power of \(N\), using the same \(y\le1\) integrability split as in step 2. The far upper tail has the integrable \(e^{-kw}\) bound. Thus the limiting integral can be taken over the entire real \(w\)-axis even for bounded noncompactly supported \(f\). Since \(y_N^2/y^2\to1\) on the critical layer and \(a/\mu_N\sim y_N\), it follows that
\[
\lim_{N\to\infty}y_N\mathbb E[f(Z_N)\mathbf 1_{\{K_N=k\}}]
=\frac1{2^kk!}\int_{-\infty}^\infty
 f(e^{-w})e^{-kw}e^{-3e^{-w}/2}\,dw.
\]
The change \(z=e^{-w}\) gives the stated integral. Replacing \(y_N\) by \(\log N\) is justified by their ratio tending to one. Evaluating the gamma integral at \(f=1\) produces \(1/(k3^k)\), and division by that positive limit gives the Gamma conditional law.

**4. The total positive-count mass and no lost probability.** Instead of exchanging the infinite sum with a limit, use the exact probability
\[
\mathbb P(K_N\ge1)=\frac a{\mu_N}\int_0^\infty\frac{dy}{y^2}
\left[S_y^N-(S_y-q_y)^N\right].
\]
On the same layer \(y=y_N+w\), its integrand tends to
\(e^{-e^{-w}}-e^{-3e^{-w}/2}\). The difference is integrably dominated: at \(w\to+\infty\), it is \(O(e^{-w})\), and at \(w\to-\infty\), it is bounded by \(e^{-c e^{-w}}\); the noncritical ranges are controlled as above. Hence
\[
\lim_{N\to\infty}y_N\mathbb P(K_N\ge1)
=\int_0^\infty\frac{e^{-z}-e^{-3z/2}}z\,dz
=\log(3/2),
\]
by Frullani's identity. Finally \(\sum_{k\ge1}1/(k3^k)=\log(3/2)\), proving tightness of the conditional count laws and the displayed logarithmic-series distribution.

## Verification

The embedded executable `verify_mirror.py` independently integrates the **exact finite-\(N\)** renewal expressions after the transformation \(y=a/t\), with scale \(a=1\). It uses the killed reflection-principle mass \(q_y\), not the limiting Gamma approximation, and checks renewal normalization, disjoint count masses, logarithmic count scale, and a finite-\(N\) conditional layer-moment comparison. Execution with Python 3 and SciPy passed 35 deterministic numerical comparisons for \(N=10^3,10^4,10^5,10^6,10^8\). For example, \((\log N)\mathbb P(K_N\ge1)\) decreases from approximately \(0.43713\) at \(N=10^3\) to \(0.42211\) at \(N=10^8\), in agreement with the analytical limit \(\log(3/2)\approx0.405465\). This slow approach is expected at logarithmic scale. Finite quadrature does not establish the limit; the proof above does.

To reproduce: extract the embedded file and run `python verify_mirror.py` with a Python 3 environment containing SciPy. Diffusivity and trigger position cancel from the dimensionless asymptotic coefficients by Brownian scaling. The main mathematical statements have no numerical-fit parameters.

## Relationship to prior work

Biroli, Majumdar and Schehr (arXiv:2512.00440v1, revised v2; EPL 153, 31002, 2026) established this threshold-reset Brownian gas, its exact stationary joint law (their eqs. (10)–(13)), the leading large-population stationary scaling, the order statistics and the full counting statistics for a **shrinking symmetric central interval** (their eqs. (36)–(38)). Their fixed-rank extreme law gives a limiting support ending at the mirror boundary; it does **not state** the rare probability that the actual minimum passes strictly *beyond* that endpoint, its logarithmic-series count law, or the conditional trigger-age Gamma profile. Our theorem quantifies precisely that nonuniform endpoint correction, using the known stationary renewal law as a premise. It is therefore not a claim to have discovered the stationary law or the leading extreme density. Biswas, Majumdar and Pal (arXiv:2504.13501) studied threshold-triggered search optimization rather than this stationary opposite-boundary occupation. De Mauro et al. (arXiv:2509.06658) considered exogenous simultaneous non-Poissonian resetting, with a different cycle-age mechanism. A separate fixed-\(N\) far-negative-tail law does not determine the joint \(N\to\infty\) mirror-threshold boundary because its limit is nonuniform.

## Limitations

The result is for fixed, equal thresholds and diffusivities, and an instantaneous position count. It does not determine the full point process of signed extreme positions, the joint limit when \(L,D\) or the inspection threshold depend on \(N\), or the probability that an entire excursion **ever** visited the negative mirror. The source's stationary joint density algebraically determines every finite-\(N\) marginal, so novelty concerns the newly derived *sharp singular large-\(N\) theorem*, not the existence of an exact representation. The numerical verification is illustrative, not an independent proof or audit.

## References

1. M. Biroli, S. N. Majumdar, G. Schehr, *First Passage Resetting Gas*, arXiv:2512.00440v1 (first posted 2025-11-29); revised arXiv:2512.00440v2; EPL **153**, 31002 (2026), DOI:10.1209/0295-5075/ae3f4f. Exact stationary joint density, large-population order statistics, and central full counting statistics.
2. A. Biswas, S. N. Majumdar, A. Pal, *Target Search Optimization by Threshold Resetting*, arXiv:2504.13501v1 (2025). Threshold-triggered collective reset model and search-time optimization.
3. G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658v1 (2025). Exogenous renewal-reset comparison.
4. Standard reflection principle and regenerative stationary occupation formula; their applications here are explicitly derived in the proof.
