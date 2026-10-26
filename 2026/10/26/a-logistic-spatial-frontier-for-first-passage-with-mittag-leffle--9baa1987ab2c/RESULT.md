# A logistic spatial frontier for first passage with Mittag–Leffler diffusivity

## Finding

For the Brownian diffusion with independently refreshed, positive Mittag–Leffler diffusivities defined below, a spatial target at distance \(\exp(b/\alpha)\) has a nondegenerate integer-valued first-passage limit as \(\alpha\downarrow0\). More strongly, all finitely many logarithmic target distances converge *jointly* to one increasing pure-jump process. This process is determined by independent standard logistic variables and has independent increments, despite the first-passage times at different targets sharing the same driving Brownian motion and environment.

For every integer \(q\ge1\) and real \(b_1,\ldots,b_q\),
\[
\left(\frac{T_\alpha(e^{b_i/\alpha})}{h}\right)_{i=1}^{q}
\ \xrightarrow[\alpha\downarrow0]{\mathrm{law}}\
(K_{b_i})_{i=1}^{q},
\qquad
K_b=\min\{j\ge0:Y_j>2b\},
\]
where \((Y_j)_{j\ge0}\) are independent standard logistic random variables with \(\mathbb P(Y_j\le y)=(1+e^{-y})^{-1}\).

Put \(u_b=(1+e^{-2b})^{-1}\). Then
\[
\mathbb P(K_b=k)=(1-u_b)u_b^k\quad(k=0,1,\ldots),
\qquad \mathbb EK_b=e^{2b},
\qquad \operatorname{Var}(K_b)=e^{2b}(1+e^{2b}).
\]
For \(b\le c\) and nonnegative integers \(k,\ell\),
\[
\mathbb P(K_b\ge k,K_c\ge\ell)
=u_b^k u_c^{(\ell-k)_+}.
\]
The process \((K_b)_{b\in\mathbb R}\) has independent increments. Its increment law is explicit: with \(u=u_b<v=u_c\),
\[
\mathbb P(K_c-K_b=0)=\frac{1-v}{1-u},\qquad
\mathbb P(K_c-K_b=d)=\frac{v-u}{1-u}(1-v)v^{d-1}\quad(d\ge1).
\]
Equivalently, in the coordinate \(u\in(0,1)\), \(K(u)=\min\{j\ge0:U_j>u\}\) for independent \(U_j\sim\mathrm{Uniform}(0,1)\), and its finite-dimensional laws coincide with
\[
K(u)=\sum_{d=1}^{\infty}dN_d(u),
\]
where the independent inhomogeneous Poisson counting processes \(N_d\) have intensity \(u^{d-1}\,du\) for \(0<u<1\). In particular, the sum is almost surely finite at each fixed \(u<1\).

The logarithmic target scale is sharp in probability: if \(x_\alpha>0\) and \(\alpha\log x_\alpha\to b\in\mathbb R\), the same one-target limit holds; if \(\alpha\log x_\alpha\to-\infty\), then \(T_\alpha(x_\alpha)/h\to0\) in probability; if \(\alpha\log x_\alpha\to+\infty\), it diverges to infinity in probability.

## Assumptions and scope

Fix \(h>0\). Independently sample positive random variables \((\lambda_{\alpha,j})_{j\ge0}\), with the first-type Mittag–Leffler law of parameter \(0<\alpha<1\), normalized by
\[
\mathbb E[e^{-s\lambda_{\alpha,j}}]=\frac{1}{1+s^\alpha},\qquad s\ge0.
\]
For each \(\alpha\), let \(W\) be standard one-dimensional Brownian motion, independent of all the rates, and use the same realization of \(W\) and the rates for *all* spatial targets. Define the integrated rate and physical-time diffusion by
\[
A_\alpha(t)=\int_0^t\lambda_{\alpha,\lfloor s/h\rfloor}\,ds,
\qquad X_\alpha(t)=W_{2A_\alpha(t)},
\qquad T_\alpha(x)=\inf\{t\ge0:X_\alpha(t)=-x\}.
\]
The diffusivity is constant within each interval \([jh,(j+1)h)\). This is a continuous-space Brownian analogue of periodically refreshed stochastic jump rates, not an assertion that a lattice jump process has an identical finite-\(\alpha\) distribution.

The weak convergence concerns finite-dimensional distributions indexed by fixed logarithmic distances, not a path-space convergence theorem. For the joint limit, all targets are hit in the same environment and by the same Brownian trajectory. Only marginal *limit-process* expectations are claimed; interchange of expectations through the \(\alpha\downarrow0\) limit is not asserted.

## Proof

**1. Singular logarithmic-rate limit.** The Mittag–Leffler rate law has the following exact survival integral (see Levit–Reuveni, supplementary equations S49–S51):
\[
\mathbb P(\lambda_\alpha>x)=\frac{\sin(\pi\alpha)}{\pi\alpha}x^\alpha
\int_0^\infty\frac{\exp(-r^{1/\alpha})}{r^2+2rx^\alpha\cos(\pi\alpha)+x^{2\alpha}}\,dr.
\]
Substitute \(x=e^{y/\alpha}\), so that \(x^\alpha=z=e^y>0\). For sufficiently small \(\alpha\), \(\cos(\pi\alpha)\ge0\), and the integrand is bounded by \((r^2+z^2)^{-1}\), an integrable function on \((0,\infty)\). Moreover \(e^{-r^{1/\alpha}}\to\mathbf1_{r<1}\) for almost every \(r\), and \(\sin(\pi\alpha)/(\pi\alpha)\to1\). Dominated convergence yields
\[
\lim_{\alpha\downarrow0}\mathbb P(\alpha\log\lambda_\alpha>y)
=z\int_0^1\frac{dr}{(r+z)^2}
=\frac1{1+e^y}.
\]
Hence \(\alpha\log\lambda_{\alpha,j}\Rightarrow Y_j\) where \(Y_j\) is standard logistic. Independence of the rate samples gives joint convergence of every finite prefix of the logarithmic rates to independent logistic variables.

**2. Brownian inverse clock.** Let \(H_x=\inf\{s\ge0:W_s=-x\}\). Standard Brownian scaling gives \(H_x\overset{d}=x^2H_1\), with \(0<H_1<\infty\) almost surely. Therefore, whenever \(\alpha\log x_\alpha\to b\),
\[
\alpha\log(H_{x_\alpha}/2)\to 2b\quad\text{in probability}.
\]
The continuous, strictly increasing clock \(2A_\alpha(t)\) tends to infinity almost surely, so \(T_\alpha(x)\) is exactly the time at which \(A_\alpha\) first crosses \(H_x/2\). The factor \(1/2\) and the fixed refresh length \(h\) disappear on multiplication of logarithms by \(\alpha\).

**3. Finite-prefix switching.** Fix finitely many \(b_i\) and an integer \(L\). By a Skorokhod coupling of the finite log-rate vector, and the convergence in probability of all finitely many Brownian log-thresholds, we can work on events with probability arbitrarily close to one on which those logarithms are uniformly close to their respective limits. Since a logistic variable has a continuous distribution, with probability approaching one as \(\eta\downarrow0\), none of \(Y_0,\ldots,Y_{L-1}\) is within \(\eta\) of any \(2b_i\). On such an event, if \(K_{b_i}=k<L\), the rates in refresh blocks \(0,\ldots,k-1\) have logarithmic sizes bounded above by \(2b_i-\eta/2\), and the rate in block \(k\) is bounded below by \(2b_i+\eta/2\). The cumulative integrated rate before time \(kh\) is consequently at most
\[
hL\exp((2b_i-\eta/2)/\alpha),
\]
whereas the Brownian clock threshold is at least \(\exp((2b_i-\eta/4)/\alpha)\) for small enough \(\alpha\). No crossing has occurred by \(kh\). The remainder of the Brownian clock threshold can be traversed within the next block in physical time at most
\[
\exp((2b_i+\eta/4)/\alpha)/\exp((2b_i+\eta/2)/\alpha)
=\exp(-\eta/(4\alpha))\to0.
\]
It follows that \(T_\alpha(e^{b_i/\alpha})/h\to k\) on these good events. Since \(\mathbb P(K_{b_i}\ge L)=u_{b_i}^{L}\), first taking \(L\to\infty\) and then \(\eta\downarrow0\) proves the stated joint finite-dimensional convergence. The same argument allows any finite family with \(\alpha\log x_{\alpha,i}\to b_i\).

**4. Limiting spatial process.** Transform \(Y_j\) to \(U_j=F(Y_j)\), independent uniform random variables. The event \(Y_j>2b\) becomes \(U_j>u_b\). Therefore \(K_b\) is the first index at which a uniform exceeds \(u_b\). Counting failures gives its geometric law and the joint tail: if \(k\le\ell\), all first \(k\) uniforms must be at most \(u_b\), and uniforms with indices \(k,\ldots,\ell-1\) at most \(u_c\). This has probability \(u_b^ku_c^{\ell-k}\); the reverse ordering follows analogously.

At a first exceedance of level \(u\), the crossing uniform is uniform on \((u,1)\), independently of the failed uniforms and all later samples. Conditional on the past threshold process up to level \(u\), the chance that this crossing value also exceeds \(v\) is \((1-v)/(1-u)\). If not, the subsequent uniforms generate an independent waiting time for a success above \(v\), giving the displayed increment law. The strong Markov property for the iid sequence at its first-exceedance index permits iteration across any finite sequence of levels, proving independent increments.

Its probability-generating function is
\[
\mathbb E[z^{K(u)}]=\frac{1-u}{1-uz}
=\exp\left(\sum_{d\ge1}\frac{u^d}{d}(z^d-1)\right),\qquad |z|\le1.
\]
Because the exponent is the cumulant generating function of independent Poisson jump counts with cumulative rates \(u^d/d\), and the processes in both descriptions have independent increments and start at zero, their finite-dimensional laws agree. In particular \(\operatorname{Cov}(K_b,K_c)=\operatorname{Var}(K_b)\) for \(b\le c\).

**5. Sharpness.** Monotonicity of \(T_\alpha(x)\) in \(x\), under the shared Brownian/environment coupling, gives for \(\alpha\log x_\alpha\to-\infty\) a stochastic upper bound by \(T_\alpha(e^{B/\alpha})\) for every fixed \(B\), eventually. Passing \(\alpha\downarrow0\), then \(B\to-\infty\), forces the ratio to zero in probability because \(\mathbb P(K_B>0)=u_B\to0\). Similarly a lower bound for \(B\to+\infty\) forces divergence in probability, since \(K_B\to\infty\) in probability.

## Verification

The independent standalone program `verify.py` reproduces exact finite-prefix threshold-distribution checks using rational arithmetic, checks the proposed inhomogeneous Poisson generating functions, numerically evaluates the original Mittag–Leffler survival integral at decreasing \(\alpha\), and simulates a single Brownian time-changed first-passage block using a standard positive-stable mixture representation. It produces `verification_output.txt`, which records 154 passed finite assertions.

The program does not establish weak convergence, infinite-dimensional process identities, or uniform integrability; those rely on the proof above. Both programs are Python standard-library only and use fixed random seeds where random sampling is involved.

## Relationship to prior work

Levit and Reuveni (arXiv:2609.26925v1, first posted 2026-09-22) study a *lattice* simple walk with periodically resampled heavy-tailed Mittag–Leffler jump rates. They establish the fixed-parameter mean first-passage transition at \(\alpha=1/2\), fixed-\(\alpha\) large-distance mean scaling, and the singular \(\alpha\downarrow0\) fixed-distance mean. Their supplementary integral is the starting identity in step 1. Their stated results do not identify the joint Brownian logarithmic-distance first-passage limit and its independent-increment spatial law.

Uchida, Washizu and Miyoshi (arXiv:2502.20705) develop general stochastic-diffusivity first-passage formulas. Their time-change framework motivates step 2 but does not state the singular Mittag–Leffler/logarithmic-distance limit. Arutkin and Reuveni (arXiv:2302.07041) study doubly stochastic continuous-time random walks and piecewise-random jump rates; the model and fixed-rate results differ from the simultaneous heavy-tail and exponential-distance limit. Sposini, Chechkin and Metzler (arXiv:1809.09186) derive first-passage formulas for Ornstein–Uhlenbeck-squared diffusing diffusivity, whose stationary rates have exponential rather than Mittag–Leffler heavy tails.

The geometric law and the compound-Poisson expansion individually follow classical probability identities. The claimed contribution is their joint realization as a singular *spatial first-passage field* under the precise stochastic diffusivity model, together with the full sharp distance-scale trichotomy; neither elementary identity alone is asserted as a new general theorem.

## Limitations

This is a Brownian continuum model with iid rates refreshed at deterministic intervals, not a theorem about lattice jumps. Only finite-dimensional weak convergence and convergence in probability in the two outer regimes are proved. In particular, no path-space convergence, finite-\(\alpha\) total-variation bound, prelimit moment convergence, universality beyond the specified Mittag–Leffler law, or claim concerning multiple independent Brownian paths is made. The established limiting means should not be confused with convergence of the prelimit expectations. The limiting additive-process representation concerns spatial logarithmic distance, not physical-time independent increments. Related record-process constructions could constitute historical priority; the novelty comparison cannot exclude every earlier equivalent formulation.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925v1 (first public 2026-09-22), especially Section S2, equations S49–S53 and main equation 6. https://arxiv.org/abs/2609.26925
2. G. Uchida, H. Washizu, and H. Miyoshi, *First passage time properties of diffusion with a broad class of stochastic diffusion coefficients*, arXiv:2502.20705 (first public 2025-02-28), Sections II–III. https://arxiv.org/abs/2502.20705
3. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, arXiv:2302.07041, sections on stochastic rate and piecewise-constant rate. https://arxiv.org/abs/2302.07041
4. V. Sposini, A. V. Chechkin, and R. Metzler, *First passage statistics for diffusing diffusivity*, arXiv:1809.09186, Sections 2–3. https://arxiv.org/abs/1809.09186
