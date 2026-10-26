# A normalized capped exponential Milstein method preserving positivity, martingales, and all coarse-step moments

## Finding
Consider the driftless Itô equation
\[
 dX_t=g(X_t)\,dB_t,\qquad g(x)=\frac{x^2}{1+x},\quad X_0=x_0>0.
\]
For \(h>0\), define, for \(x\ge0\) and \(z\in\mathbb R\),
\[
 f(x)=\frac{x}{1+x},\quad a(x)=\frac{x^2}{(1+x)^3},\quad C(z)=\min\{z^2,1\},
\]
\[
 Q_h(x,z)=\exp\left(f(x)z+\tfrac12a(x)(C(z)-h)-\tfrac12f(x)^2h\right),
\qquad M_h(x)=\mathbb E\,Q_h(x,\sqrt h Z),\ Z\sim N(0,1).
\]
The Gaussian expectation defining \(M_h(x)\) is an ordinary **one-dimensional finite integral**, determined solely by the current state and step size. Define the numerical scheme
\[
 Y_{n+1}=Y_n\frac{Q_h(Y_n,\Delta B_n)}{M_h(Y_n)},\qquad Y_0=x_0,
\quad\Delta B_n=B_{(n+1)h}-B_{nh}.
\]

**Theorem.** For every \(h>0\), every positive integer \(n\), and every finite real \(q\ge1\), the iterate is strictly positive almost surely, obeys \(\mathbb E[Y_n]=x_0\), and has \(\mathbb E[Y_n^q]<\infty\). Thus \((Y_n)\) is a genuine nonnegative discrete-time martingale, not merely a local martingale. For every fixed \(T>0\), every \(N\ge1\), and \(h=T/N\),
\[
 \max_{0\le n\le N}\left(\mathbb E|Y_n-X_{nh}|^2\right)^{1/2}\le C_{T,x_0}h.
\]
The normalization is part of the *mathematical* scheme: replacing \(M_h\) by approximate quadrature would generally sacrifice exact martingale preservation.

For comparison, the uncapped, unnormalized exponential Milstein step of Bréhier and Cohen applied to this same equation has an infinite one-step \(q\)-moment at the state \(x=2\) whenever \(h\ge27/(4q)\); this known obstruction motivates the coupled cap and normalization but is **not** asserted as a new discovery here.

## Assumptions and scope
The driving motion is a standard real Brownian motion, and increments are independent with law \(N(0,h)\). Initial condition \(x_0>0\) is deterministic. The expectation defining \(M_h\) is exact. No timestep restriction is imposed for positivity, martingality, or finiteness of discrete moments. Convergence is asserted on each fixed finite time interval as \(h\to0\), not uniformly over infinite times, and only for the stated scalar diffusion. Classification: MSC2020 **65C30**.

## Proof
**(1) The exact diffusion.** Since \(0\le g'(x)=1-(1+x)^{-2}\le1\), \(g\) is globally Lipschitz on the nonnegative halfline. Extend it by zero on the negative halfline, giving a globally Lipschitz function. The stochastic differential equation has a unique strong solution. Before any proposed first hitting time of zero, Itô's formula gives
\[
 d\log X_t=\frac{X_t}{1+X_t}\,dB_t-\frac12\left(\frac{X_t}{1+X_t}\right)^2dt.
\]
Both coefficients are bounded, precluding a finite-time divergence of \(\log X_t\) to \(-\infty\). Hence the solution is strictly positive. For \(q\ge2\), Itô's formula and \(0\le g(x)\le x\), followed by localization and Gronwall, give \(\sup_{t\le T}\mathbb E X_t^q<\infty\). Therefore the stochastic integral with integrand \(g(X_t)\) is square integrable and \(\mathbb E X_t=x_0\).

**(2) Global positivity, exact conditional expectation and moments.** The functions satisfy \(0\le f\le1\) and \(0\le a\le4/27\). The logarithm of \(Q_h\) is finite for every finite \(z\), and
\[
 Q_h(x,z)\le\exp\left(|z|+\tfrac{2}{27}\right),
\]
so every Gaussian moment of \(Q_h(x,\sqrt hZ)\) exists at every finite \(h\). Jensen's inequality yields
\[
 M_h(x)\ge\exp\left(\tfrac12a(x)\big(\mathbb EC(\sqrt hZ)-h\big)-\tfrac12f(x)^2h\right)
 \ge\exp\left(-\tfrac12\big(4/27+1\big)h\right),
\]
where the last inequality uses \(C\ge0\). In particular \(0<M_h(x)<\infty\) uniformly in \(x\ge0\) for each \(h\). Positivity follows by induction. Conditional independence of \(\Delta B_n\) gives
\[
 \mathbb E\left[Q_h(Y_n,\Delta B_n)/M_h(Y_n)\mid\mathcal F_{nh}\right]=1,
\]
so \(\mathbb E[Y_{n+1}\mid\mathcal F_{nh}]=Y_n\), once integrability is established. For any fixed \(h,q\), the uniform lower bound on \(M_h\), Gaussian exponential moments, and \(Q_h\le e^{|z|+2/27}\) give a uniform constant \(K_{h,q}<\infty\) such that
\[
 \mathbb E\left[(Q_h(x,\sqrt hZ)/M_h(x))^q\right]\le K_{h,q},\qquad x\ge0.
\]
Induction gives \(\mathbb E Y_n^q\le x_0^q K_{h,q}^{n}\) for every finite \(n\). Integrability and the martingale assertion follow.

**(3) Uniform small-step estimates.** For each fixed \(q\ge2\), choose \(h_q>0\) so small that \(q(4/27)h_q<1/2\). Because \(C(z)\le z^2\), the elementary Gaussian quadratic-exponential integral bounds the \(q\)-moment of \(Q_h\) by \(1+O_q(h)\), uniformly over \(x\ge0\) and \(0<h\le h_q\). The preceding Jensen bound gives \(M_h(x)^{-q}\le e^{C_qh}\); hence
\[
 \sup_{x\ge0}\mathbb E\left[(Q_h(x,\sqrt hZ)/M_h(x))^q\right]\le1+C_q h.
\]
This implies \(\sup_{nh\le T}\mathbb E Y_n^q\le x_0^qe^{C_qT}\), uniformly over small \(h\).

For the local expansion, let \(z\sim N(0,h)\). On \(|z|\le1\), \(C(z)=z^2\), so a Taylor expansion in \(z\) and \(h\) gives
\[
 Q_h(x,z)=1+f(x)z+\tfrac12\big(f(x)^2+a(x)\big)(z^2-h)+R_h(x,z),
\]
with \(\sup_{x\ge0}\mathbb E|R_h(x,z)|^2\le Ch^3\) and \(\sup_{x\ge0}|\mathbb E R_h(x,z)|\le Ch^2\). To justify the uniform bounds without restricting to a compact state set: all coefficients \(f,a\) are uniformly bounded, the Taylor remainder is controlled by Gaussian moments of \(|z|^3+h|z|+h^{3/2}\), and the omitted \(|z|>1\) events have Gaussian probability \(O(e^{-c/h})\). On this tail, for sufficiently small \(h\), the exponential moment of the uncapped quadratic factor is finite and a Gaussian weighted Cauchy–Schwarz bound makes the difference exponentially small. These estimates also prove \(\sup_x|M_h(x)-1|\le Ch^2\) because \(\mathbb Ez=\mathbb E(z^2-h)=0\). Thus the normalized factor satisfies
\[
 x\frac{Q_h(x,z)}{M_h(x)}=x+g(x)z+\tfrac12 g(x)g'(x)(z^2-h)+x\rho_h(x,z),
\]
where \(\mathbb E[\rho_h(x,z)]=0\) exactly and \(\sup_x\mathbb E|\rho_h(x,z)|^2\le Ch^3\). Here the coefficient identity is \(x(f^2+a)=g g'\), checked from the displayed rational formulas. Exact zero-mean follows from the normalization and the centered Milstein terms, not from a heuristic Taylor truncation.

**(4) Strong order one.** The coefficient \(g\) and the product \(gg'\) are globally Lipschitz; moreover \(g\) has bounded first and second derivatives and \(|g''(x)g(x)^2|+|g'(x)^2g(x)|\le C(1+x)\). The standard Itô–Taylor expansion, obtained by applying Itô's formula to \(g(X_s)\) inside the stochastic integral and taking one iterated integral, yields
\[
 X_{t+h}=X_t+g(X_t)z+\tfrac12(gg')(X_t)(z^2-h)+\eta_{t,h},
\]
where \(\mathbb E[\eta_{t,h}\mid\mathcal F_t]=0\) and \(\mathbb E[|\eta_{t,h}|^2\mid\mathcal F_t]\le Ch^3(1+X_t^2)\). For completeness, the latter follows from Itô isometry for the two omitted nested stochastic integrals, their integrands' linear-growth bounds, and \(\mathbb E[1+X_s^2\mid\mathcal F_t]\le C(1+X_t^2)\) for \(s\in[t,t+h]\). Couple \(X\) and \(Y\) with the same Brownian increments and write \(e_n=X_{nh}-Y_n\). Subtraction of the two expansions gives \(e_{n+1}=e_n+\delta g_n z+\tfrac12\delta(gg')_n(z^2-h)+\eta_n-Y_n\rho_n\). The last four terms are all conditionally centered. Conditional Itô isometry, Gaussian moments, Lipschitz estimates, Cauchy–Schwarz/Young inequalities for cross terms, and the uniform second moments from steps (1)–(3) give
\[
 \mathbb E|e_{n+1}|^2\le(1+Ch)\mathbb E|e_n|^2+Ch^3.
\]
Since \(e_0=0\), discrete Gronwall gives \(\max_{nh\le T}\mathbb E|e_n|^2\le C_{T,x_0}h^2\), as claimed. No assertion here concerns strong convergence with a numerically approximated normalizer.

**(5) The motivating coarse-step obstruction.** In the uncapped version, the term involving \(a(x)z^2/2\) remains quadratic for every \(z\). At \(x=2\), \(a=4/27\). Multiplying the \(q\)-th power of that factor by the Gaussian density produces an integrand with quadratic exponent coefficient \((qa-1/h)/2\), whose integral diverges whenever \(qah\ge1\), including equality. The new cap removes precisely this quadratic Gaussian-tail obstruction; normalization separately eliminates spurious one-step mean drift.

## Verification
All identities and the Gaussian integrals can be checked with the attached standalone `verify.py` script. It checks the rational coefficient identity, nonnegative boundedness of \(a\) on a grid, quadrature of \(M_h\), exact-in-the-definition normalization, finite coarse-step \(q\)-moments, and finite-step Milstein expansions. Finite checks support the proof but cannot establish the global theorem; the arguments in the preceding section do that.

## Relationship to prior work
Bréhier and Cohen (2026, arXiv:2608.25689v1), equation (26), Proposition 5, Theorem 6 and Proposition 9 establish positivity, small-step strong first order and moment bounds for the **uncapped, unnormalized** exponential integrator. Its Gaussian quadratic integrability condition motivates the tail modification. Their companion preprint (arXiv:2608.25685v1) concerns bounded-domain stochastic splitting schemes, not this infinite-halfline martingale construction. Yi, Hu and Zhao (2020, arXiv:2010.16321) use logarithmic truncation for positivity and convergence; their method is structurally distinct from conditional normalization of this exponential Milstein multiplier. The observation that the original uncapped method can have infinite moments is treated as prior information, not as the claimed advance. The advance asserted here is a **single modified scheme with all four demonstrated properties**. No exhaustive novelty claim is made.

## Limitations
The normalizer \(M_h\) is a definite Gaussian integral rather than an elementary closed form. Finite-precision quadrature normally yields an approximately, not exactly, martingale-preserving implementation. For large \(h\), finite moments may be huge; the theorem is not a uniform-in-step stability estimate. The proof covers one scalar rational diffusion, not all scalar SDEs or multivariate systems. The claim is subject to independent mathematical and literature review; classical normalized exponential integrators may provide related constructions.

## References
1. C.-E. Bréhier and D. Cohen, *Analysis of a first-order explicit positivity preserving scheme for a class of scalar SDEs*, arXiv:2608.25689v1 (first posted 2026-08-26), https://arxiv.org/abs/2608.25689 .
2. C.-E. Bréhier and D. Cohen, *Explicit domain preserving numerical schemes for a class of stochastic differential equations*, arXiv:2608.25685v1 (first posted 2026-08-26), https://arxiv.org/abs/2608.25685 .
3. Y. Yi, Y. Hu and J. Zhao, *Positivity preserving logarithmic Euler-Maruyama type scheme for stochastic differential equations*, arXiv:2010.16321 (first posted 2020-10-30), https://arxiv.org/abs/2010.16321 .
