# A totally skewed stable-fluctuation window for Pareto-reset scaled Brownian absolute area

## Finding
For fully renewed scaled Brownian motion interrupted at independent Pareto reset times, the centered accumulated absolute area has an explicit, non-Gaussian stable fluctuation limit throughout the parameter band described below. The stable index is \(q=\alpha/(1+\beta/2)\); its positive-jump Lévy intensity is determined by a fractional absolute-Brownian-area moment. In particular, for ordinary Brownian motion with \(\beta=1\), the interval \(2<\alpha<3\) exhibits non-Gaussian stable fluctuations even though this lies above the mean-square ergodicity threshold \(\alpha=2\) described for the model in the motivating literature.

## Assumptions and scope
Fix \(K,t_0>0\), \(0<\beta<2\), set \(p=1+\beta/2\), and choose \(p<\alpha<2p\). Independently for each cycle, draw \(S\) with \(\Pr(S>s)=(1+s/t_0)^{-\alpha}\) for \(s\ge0\), and standard Brownian motion \(B\). During that cycle reset both position and the intrinsic clock, and let \(X(u)=\sqrt{2K}B(u^\beta)\), \(0\le u<S\). Concatenate independent cycles from time zero. Define the total absolute area \(A(T)=\int_0^T|X(t)|\,dt\), with the variable \(t\) referring to global time after the reset concatenation.

Define the positive unit-cycle random variable and exponent
\[
Z=\sqrt{2K}\int_0^1|B(u^\beta)|\,du,\qquad q=\frac{\alpha}{p}\in(1,2).
\]
The deterministic area rate is
\[
\mu=2\sqrt{\frac K\pi}\,(\alpha-1)t_0^{p-1}
\frac{\Gamma(p)\Gamma(\alpha-p)}{\Gamma(\alpha)}.
\]
Then, as \(T\to\infty\),
\[
\frac{A(T)-\mu T}{T^{1/q}}\ \Longrightarrow\ \mathcal S_q,
\]
where \(\mathcal S_q\) is the nondegenerate centered, spectrally positive stable random variable with Lévy measure
\[
\nu(dy)=q\,c_*\,y^{-q-1}\mathbf1_{y>0}\,dy,\qquad
c_*=(\alpha-1)t_0^{\alpha-1}\,\mathbb E[Z^q]>0.
\]
Equivalently its characteristic function is
\[
\mathbb E e^{i\theta\mathcal S_q}=
\exp\!\left\{q c_*\int_0^\infty
(e^{i\theta y}-1-i\theta y)y^{-q-1}\,dy\right\},\quad\theta\in\mathbb R.
\]
The integral converges absolutely at both ends because \(1<q<2\). All fractional moments in the coefficient are mathematically defined by the displayed Brownian functional and finite; no closed-form expression for the general \(q\)-moment is asserted.

For \(\beta=1\), \(\alpha=5/2\), and \(t_0=K=1\), the law has \(q=5/3\) and \(\mu=2/\sqrt\pi\).

## Proof
**Cycle scaling and rate.** Brownian scaling implies that the complete-cycle reward \(R=\int_0^S|X(u)|\,du\) has joint distribution with its length \(S\) equal to \((S^pZ,S)\), where \(Z\) is independent of \(S\). This can be realized by drawing an independent scaled unit Brownian path for each cycle. In particular \(\mathbb E Z=2\sqrt{K/\pi}/p\) and \(Z\le\sqrt{2K}\sup_{0\le u\le1}|B(u)|\), so \(Z\) has moments of every positive order. For \(k<\alpha\), direct integration of the Pareto density gives \(\mathbb ES^k=t_0^k\Gamma(k+1)\Gamma(\alpha-k)/\Gamma(\alpha)\). Since \(\alpha>p\), the renewal-reward rate \(\mathbb ER/\mathbb ES\) equals the stated \(\mu\), with \(\mathbb ES=t_0/(\alpha-1)\).

**Power tail and asymmetry.** Pareto regular variation and independence, together with the finite \((q+\varepsilon)\)-moment of \(Z\), give by the product-tail theorem
\[
\Pr(R>x)\sim t_0^\alpha\mathbb E[Z^q]x^{-q}.
\]
Set \(Y=R-\mu S\). Because \(p>1\), one has \(\alpha>q\). The negative tail satisfies \(\Pr(Y<-x)\le\Pr(S>x/\mu)=O(x^{-\alpha})=o(x^{-q})\). For each fixed \(\varepsilon>0\),
\[
\Pr(R>(1+\varepsilon)x)-\Pr(\mu S>\varepsilon x)
\le\Pr(Y>x)\le\Pr(R>x).
\]
Letting \(\varepsilon\downarrow0\) yields the same regularly varying right tail for \(Y\) as for \(R\); also \(\mathbb EY=0\). The classical stable-domain-of-attraction theorem for independent centered variables therefore gives an index-\(q\) spectrally positive Lévy limit for partial sums of \(Y\), with right-tail constant \(t_0^\alpha\mathbb E Z^q\).

**Random cycle count and final fragment.** Let \(N(T)\) count complete cycles by global time \(T\), and \(D(T)\) be the age of the unfinished cycle. The strong renewal law gives \(N(T)/T\to1/\mathbb ES\) almost surely. The stable functional limit for centered \(Y\)-sums, combined with the deterministic uniform clock law and the random-time-change theorem, gives
\[
T^{-1/q}\sum_{j=1}^{N(T)}Y_j\Longrightarrow\mathcal S_q
\]
with the intensity constant \(c_*=t_0^\alpha\mathbb EZ^q/\mathbb ES\). This random-index argument does not require independence between \(N(T)\) and the rewards, because it uses joint functional convergence and the asymptotically deterministic clock. Since \(\mathbb ES<\infty\) and the cycle law is nonarithmetic, the renewal-age distribution \(D(T)\) is tight. The unfinished-cycle contribution \(\int_0^{D(T)}|X(u)|\,du\) is tight as well, by Brownian continuity and tightness of \(D(T)\). Finally,
\[
A(T)-\mu T=\sum_{j=1}^{N(T)}(R_j-\mu S_j)
+\int_0^{D(T)}|X(u)|\,du-\mu D(T).
\]
The last two terms are \(O_{\mathbb P}(1)=o_{\mathbb P}(T^{1/q})\), proving the asserted limit, including its Lévy measure and centering.

## Verification
The accompanying `verify.py` reproduces 25 independent deterministic parameter-domain, Pareto-moment, Brownian-area-mean, renewal-rate, and regularly varying-tail checks. Its output is `PASS 25 deterministic independent numerical identities; stable convergence is analytic`. The limiting-law theorem is proved by the preceding renewal and stable-domain argument, not by numerical simulation. To reproduce: `python verify.py` (requires SciPy).

## Relationship to prior work
Méndez and Cristín, arXiv:2610.19985 (first public 2026-10-14), analyze lower-order moments and ergodic regimes of absolute areas of reset scaled Brownian motion under Poisson and heavy-tailed waiting laws. Méndez and Flaquer-Galmés, arXiv:2507.05955, formulate general-reset functional moments and study a distinct half-occupation observable. Zamparo, arXiv:2207.07521, proves general renewal-reward central limit and large-deviation principles, and treats Brownian additive functionals. These results supply the relevant physical model and probabilistic framework; the specific non-Gaussian stable window, its exponent, positive Lévy measure, and mean-square-ergodic-side example are the focus here. Classical product-tail and stable-sum theorems are used as established lemmas, not claimed as novel.

## Limitations
The claim assumes independent renewal of the Brownian path and intrinsic diffusion clock at every reset; resetting position alone while retaining a time-dependent global diffusivity is a different process. It is restricted to \(0<\beta<2\) and the open range \(1+\beta/2<\alpha<2+\beta\), excluding both critical endpoints, the finite-variance central-limit range, and the infinite-mean-reward range. The claim does not assert a closed formula for \(\mathbb E Z^q\), an error rate, or independent certification. The motivating paper's full text was not available for a full claim-by-claim comparison; overlap with a result outside its available abstract cannot be excluded.

## References
- V. Méndez and J. Cristín, *Absolute area under a scaled Brownian motion with resetting*, arXiv:2610.19985 (2026), https://arxiv.org/abs/2610.19985.
- V. Méndez and R. Flaquer-Galmés, *Statistical properties of stochastic functionals under general resetting*, arXiv:2507.05955 (2025), https://arxiv.org/abs/2507.05955.
- M. Zamparo, *Statistical fluctuations under resetting: rigorous results*, arXiv:2207.07521, J. Phys. A 55 (2022) 484001, https://arxiv.org/abs/2207.07521.
- F. den Hollander, S. N. Majumdar, J. M. Meylahn and H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, J. Phys. A 52 (2019) 175001, https://doi.org/10.1088/1751-8121/ab0efd.
