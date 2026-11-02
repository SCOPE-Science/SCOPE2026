# Quadratic dual-end escape and an inverse-square law in critical-cusp Bernoulli maps

## Finding
For \(1<\theta_0<\theta_1<2\) and \(p\in[0,1]\), choose at each iteration independently the interval map
\[
 f_\theta(\tfrac12\pm t)=1-\theta t-2K_\theta\sqrt t,\qquad
 K_\theta=\frac{1-\theta/2}{\sqrt2},\quad0\le t\le\tfrac12,
\]
with probabilities \(1-p,p\) for \(\theta_0,\theta_1\). Let \(\mathcal L_p=(1-p)\mathcal L_{\theta_0}+p\mathcal L_{\theta_1}\) be the annealed Perron–Frobenius operator, and let \(h_p\) be its unique normalized nonnegative stationary density. Put
\[
 A_p=\frac{1-p}{K_{\theta_0}^{2}}+\frac{p}{K_{\theta_1}^{2}},\qquad
 B_p=\frac{1-p}{(1+\theta_0/2)^2}+\frac{p}{(1+\theta_1/2)^2}.
\]
Then \(0<B_p<1\), \(h_p(1/2)>0\), and the endpoint traces satisfy the exact identities
\[
 h_p(0)=h_p(1)=0,\quad
 h_p'(1)=-A_p h_p(1/2),\quad
 h_p'(0)=\frac{A_pB_p}{1-B_p}h_p(1/2).
\]
For each \(e\in\{0,1\}\) and \(\varepsilon>0\), remove trajectories immediately on entering \(H_{0,\varepsilon}=[0,\varepsilon]\) or \(H_{1,\varepsilon}=[1-\varepsilon,1]\), respectively. Let \(\lambda_{e,\varepsilon}\in(0,1)\) denote the leading eigenvalue of the corresponding killed annealed transfer operator \(\mathcal P_{e,\varepsilon}=\mathcal L_p(\mathbf1_{[0,1]\setminus H_{e,\varepsilon}}\cdot)\), and \(r_{e,\varepsilon}=-\log\lambda_{e,\varepsilon}\) its exponential escape rate. For every fixed permitted \(\theta_0,\theta_1,p\), these eigenvalues exist and are simple for all sufficiently small positive \(\varepsilon\), and
\[
 \boxed{\lim_{\varepsilon\downarrow0}\frac{r_{1,\varepsilon}}{\varepsilon^2}
       =\frac{A_p h_p(1/2)}2,\qquad
 \lim_{\varepsilon\downarrow0}\frac{r_{0,\varepsilon}}{\varepsilon^2}
       =\frac{A_pB_p h_p(1/2)}2,\qquad
 \lim_{\varepsilon\downarrow0}\frac{r_{0,\varepsilon}}{r_{1,\varepsilon}}=B_p.}
\]
The dimension-two local endpoint masses are
\[
 \mu_p(H_{1,\varepsilon})\sim \frac{A_ph_p(1/2)}2\varepsilon^2,\qquad
 \mu_p(H_{0,\varepsilon})\sim\frac{A_pB_ph_p(1/2)}{2(1-B_p)}\varepsilon^2,
\]
where \(d\mu_p=h_p\,dx\). The corresponding normalized escape factors, often called extremal indices, are exactly \(1\) at the nonperiodic endpoint \(1\) and \(1-B_p\) at the repelling fixed endpoint \(0\). The inverse **square**, rather than inverse first power, arises from the vanishing stationary density.

Since \(\theta_0<\theta_1\), the limiting ratio is strictly decreasing and affine in \(p\). Thus its observation identifies the Bernoulli mixing weight through
\[
 p=\frac{B_p-(1+\theta_0/2)^{-2}}{(1+\theta_1/2)^{-2}-(1+\theta_0/2)^{-2}}.
\]

In particular, choosing \(\theta_0=3/2\), \(\theta_1=7/4\) and \(p=2/3\) yields
\[
 A_p=96,\quad B_p=\frac{9872}{33075},\quad
 \lim_{\varepsilon\downarrow0}\frac{r_{0,\varepsilon}}{r_{1,\varepsilon}}=\frac{9872}{33075}.
\]

## Assumptions and scope
The parameter inequalities \(1<\theta_0<\theta_1<2\) are strict and fixed. Probability \(p\) may equal zero or one. The maps are applied independently at each time, and escape means first entry into the closed endpoint hole, before the next map application. The rate is **annealed**, i.e. the logarithm of the leading eigenvalue of the averaged killed transfer operator, not a quenched almost-sure Lyapunov exponent. Endpoint inclusions have zero effect on the absolutely continuous measures. No uniform-in-\(\theta\) assertion is made as the parameters approach the excluded boundaries.

## Proof
**(1) Regular stationary law and its positivity.** Every map has two increasing/decreasing full branches and minimum derivative magnitude \(\Lambda_\theta=1+\theta/2>1\). Its explicit inverse branches are
\[
 u_\theta(y)=\frac{\sqrt{K_\theta^2+\theta(1-y)}-K_\theta}{\theta},\quad
 g_{\theta,\pm}(y)=\tfrac12\pm u_\theta(y)^2,\quad
 w_\theta(y)=\frac{u_\theta(y)}{K_\theta+\theta u_\theta(y)},
\]
and \(\mathcal L_\theta\phi(y)=w_\theta(y)[\phi(g_{\theta,-}(y))+\phi(g_{\theta,+}(y))]\). The critical-cusp cancellation in [1, Section 3] supplies a second-derivative Lasota–Yorke bound on \(W^{2,1}([0,1])\), with high-order contraction \(\Lambda_\theta^{-2}<1\). Taking a convex combination gives such a bound for \(\mathcal L_p\), with its contracting coefficient bounded uniformly by \(\max_j\Lambda_{\theta_j}^{-2}<1\). Interpolation and compact embedding give quasicompactness.

Both individual full-branch systems are topologically exact: cylinder diameters decrease geometrically because every inverse branch contracts by at most \(\Lambda_\theta^{-1}\). For \(0<p<1\), the strictly positive weight of either fixed-map word implies that any nonzero nonnegative periodic density has full essential support after sufficiently many transfer steps. The standard positive-operator peripheral decomposition then excludes distinct cyclic densities; hence the nonnegative stationary density is unique and the eigenvalue \(1\) is simple and the only peripheral eigenvalue. The endpoints \(p=0,1\) follow by the same deterministic full-branch argument. Markov \(L^1\) contraction excludes a Jordan block at \(1\). Thus \(h_p\in W^{2,1}\subset C^1\) exists, with a spectral gap. If \(h_p(1/2)=0\), stationarity and positivity of all inverse-branch weights for \(y<1\) force \(h_p\) to vanish on the dense backward orbit of \(1/2\) under any map assigned positive probability, contradicting \(\int h_p=1\). Hence \(h_p(1/2)>0\).

**(2) Exact endpoint identities.** Since \(u_\theta(1)=0\), one has \(h_p(1)=0\). At \(y=0\), \(g_{\theta,-}(0)=0\), \(g_{\theta,+}(0)=1\) and \(w_\theta(0)=\Lambda_\theta^{-1}\). Stationarity gives \(h_p(0)=h_p(0)\sum_jp_j\Lambda_{\theta_j}^{-1}\); the sum is less than one, so \(h_p(0)=0\). As \(y\uparrow1\), the inverse formula gives
\[
 u_\theta(y)=\frac{1-y}{2K_\theta}+O((1-y)^2),\qquad
 \mathcal L_\theta h_p(y)=\frac{h_p(1/2)}{K_\theta^2}(1-y)+o(1-y).
\]
Differentiation of the same transfer identity at \(y=0\) (the terms involving \(w_\theta'(0)[h_p(0)+h_p(1)]\) vanish) gives
\[
 h_p'(0)=\sum_j p_j\Lambda_{\theta_j}^{-2}[h_p'(0)-h_p'(1)]
         =B_p[h_p'(0)-h_p'(1)].
\]
The derivative at \(1\) is \(-A_ph_p(1/2)\); solving yields the two asserted derivative identities. Integration of their first-order Taylor expansions gives the stated endpoint masses.

**(3) Spectral small-hole hypotheses.** The inverse branches above are smooth on \([0,1]\), contract uniformly, and have inverse derivative weights of bounded variation. The expanding full-branch BV Lasota–Yorke argument applied to finite random words (with uniform expansion \(\min_j\Lambda_{\theta_j}>1\)) yields a spectral gap for \(\mathcal L_p\) on BV. Deleting a single sufficiently short endpoint interval introduces at most one cut per branch at each step; the same finite-cylinder variation estimates give uniform BV Lasota–Yorke bounds for \(\mathcal P_{e,\varepsilon}\). The weak norm perturbation is at most \(C\varepsilon\), because
\[
 \|\mathcal L_p(\phi\mathbf1_{H_{e,\varepsilon}})\|_1
 \le\int_{H_{e,\varepsilon}}|\phi|\le C\varepsilon\|\phi\|_{BV}.
\]
Thus standard spectral stability [2, Sections 2–3] supplies a simple leading eigenvalue tending to \(1\) and uniform separation from the remaining spectrum. Moreover, writing \(\Delta_{e,\varepsilon}=\mu_p(H_{e,\varepsilon})\), one has \(\Delta_{e,\varepsilon}\asymp\varepsilon^2\), while
\[
 \|\mathcal L_p(h_p\mathbf1_{H_{e,\varepsilon}})\|_{BV}=O(\varepsilon).
\]
Indeed \(h_p\) is \(C^1\) and vanishes linearly at the relevant endpoint, and the image of each hole under either branch has length \(O(\varepsilon)\), with transferred amplitude and total variation \(O(\varepsilon)\). Since the hole functional has BV dual norm \(O(\varepsilon)\), the product is \(O(\varepsilon^2)=O(\Delta_{e,\varepsilon})\). This verifies the nonstandard vanishing-density smallness assumption (A6) of [2, Theorem 2.1], rather than applying the positive-density periodic formula outside its hypotheses.

**(4) Cluster returns and exact rates.** In that theorem the normalized finite-return terms are the conditional stationary measures of starting in the hole, surviving the intervening steps, and returning at the next prescribed step. The endpoint \(1\) is not periodic: each map sends \(1\) to \(0\), while every map fixes and uniformly repels \(0\). Hence for every fixed finite return time, the return intersection for \(H_{1,\varepsilon}\) is empty once \(\varepsilon\) is sufficiently small. All its return coefficients vanish.

At the fixed endpoint \(0\), only the immediate return contributes. For each \(\theta_j\), local inversion of \(f_{\theta_j}(x)=\Lambda_{\theta_j}x+O(x^2)\) gives
\[
 \frac{\mu_p(H_{0,\varepsilon}\cap f_{\theta_j}^{-1}H_{0,\varepsilon})}
 {\mu_p(H_{0,\varepsilon})}
 \longrightarrow\Lambda_{\theta_j}^{-2},
\]
because \(h_p(x)\sim h_p'(0)x\). Averaging over the independent map choice yields the immediate-return coefficient \(B_p\). Every later fixed-time first return coefficient is zero: for all sufficiently small starting points, a fixed finite sequence of maps remains in the uniformly repelling neighborhood of \(0\), so a trajectory that first exits a small endpoint hole cannot re-enter it within that sequence. The perturbative rare-event identity [2, Theorem 2.1] consequently gives
\[
 \frac{1-\lambda_{1,\varepsilon}}{\Delta_{1,\varepsilon}}\to1,\qquad
 \frac{1-\lambda_{0,\varepsilon}}{\Delta_{0,\varepsilon}}\to1-B_p.
\]
Multiplying by the mass expansions and using \(-\log(1-z)\sim z\) proves all three escape-rate formulas.

## Verification
`CHECK.py` evaluates the exact rational inverse-square expression, reconstructs the inverse branches from the defining maps, iterates the annealed transfer operator on a uniform grid, and numerically estimates the leading eigenvalues of both killed operators. For the two-map mixture \(\theta_0=3/2\), \(\theta_1=7/4\), \(p=2/3\), the observed ratios at hole sizes \(0.006,0.003,0.0015\) are approximately \(0.34776,0.32930,0.31622\), moving toward the exact limit \(9872/33075\approx0.29847\). These finite-grid diagnostics are **not** a proof of the limiting theorem. The proof uses endpoint expansions and the rare-event spectral identity.

## Relationship to prior work
Oltiboev and Vafoyev [1] introduce the critical square-root cusp map and prove \(W^{2,1}\) regularity, a deterministic spectral gap, and a small-probability Bernoulli analytic response. Their analysis contains no small-hole escape theorem. Keller and Liverani [2] prove the general spectral escape formula and work out the generalized cusp map at its nonperiodic right endpoint; this is an essential tool here. Their displayed periodic-point derivative formula presumes the usual nonvanishing-density scaling and does not compute the zero-density fixed-endpoint factor in this random family. Bahsoun and Vaienti [3] address random holes and metastability for expanding maps, rather than the present fixed holes with a Bernoulli choice of cusp maps and the explicit two-end ratio. Haydn and Yang [4] establish broad local escape-rate laws for mixing systems; their explicit interval-map periodic-point derivative evaluation uses a positive invariant density at the periodic point and does not evaluate the vanishing-density coefficient here. The present result is the coupled pair of endpoint mass/escape asymptotics and the exact \(p\)-dependent inverse-square ratio; the general spectral perturbation framework is not claimed as new.

## Limitations
The limit is for each fixed expanding parameter pair and Bernoulli weight, not uniform as \(\theta\to2\), where the cusp coefficient vanishes, or as \(\theta\to1\). Only small endpoint holes are classified; interior holes, overlapping holes, finite-size error constants, quenched escape exponents, and full hitting-time laws are not addressed. The positive normalizing factor \(h_p(1/2)\) is not given in closed form, although it cancels in the escape-rate ratio. Priority comparisons with the broader rare-events literature remain subject to independent review.

## References
[1] D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, *ACTA NUUz*, 2(2.3) (issue publicly dated October 6, 2026), 178–183; arXiv:2610.23180v1 (posted October 16, 2026), especially Sections 3, 4, and 6. https://arxiv.org/abs/2610.23180

[2] G. Keller and C. Liverani, *Rare events, escape rates and quasistationarity: some exact formulae*, arXiv:0810.2229 (first posted October 13, 2008), especially Theorem 2.1 and Section 3.1. https://arxiv.org/abs/0810.2229

[3] W. Bahsoun and S. Vaienti, *Escape Rates Formulae and Metastability for Randomly Perturbed Maps*, arXiv:1206.3654 (first posted June 16, 2012), especially Sections 2 and 3. https://arxiv.org/abs/1206.3654

[4] N. Haydn and F. Yang, *Local Escape Rates for φ-Mixing Dynamical Systems*, arXiv:1806.07148 (first posted June 19, 2018), especially Theorem 1 and Section 6.3. https://arxiv.org/abs/1806.07148
