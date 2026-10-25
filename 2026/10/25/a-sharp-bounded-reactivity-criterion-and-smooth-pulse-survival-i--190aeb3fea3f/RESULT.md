# A sharp bounded-reactivity criterion and smooth pulse survival in confined Brownian reaction

## Finding

Let a particle undergo reflected Brownian diffusion with diffusion coefficient \(D=1\) on \([0,1]\), initialized from the uniform equilibrium distribution. The endpoint \(0\) is partially reactive, with deterministic nonnegative surface reactivity \(\kappa(t)\). Its accumulated reaction hazard is the Stieltjes integral \(H_t=\int_0^t\kappa(s)\,d\ell_s\), where \(\ell\) is boundary local time at \(0\). With an independent unit-rate exponential reaction threshold, the survival probability is \(S(t)=\mathbb E[e^{-H_t}]\). Put \(A(t)=\int_0^t\kappa(s)\,ds\).

**Sharp local-time covariance bound.** For every nonnegative locally bounded Borel reactivity, and every finite \(t>0\),
\[
\mathbb E[H_t]=A(t),\qquad
\operatorname{Var}(H_t)\le\frac23\int_0^t\kappa(s)^2\,ds.
\]
The universal constant \(2/3\) is optimal: for constant reactivity \(\kappa=1\), \(\operatorname{Var}(H_t)/t\to2/3\) as \(t\to\infty\).

**Complete bounded-reactivity classification.** If \(0\le\kappa(t)\le K<\infty\) for all \(t\ge0\), then
\[
S(\infty):=\lim_{t\to\infty}S(t)>0
\quad\Longleftrightarrow\quad
\int_0^\infty\kappa(t)\,dt<\infty.
\]
If \(A(t)\to\infty\), then \(H_t/A(t)\to1\) both in \(L^2\) and almost surely. For \(A(t)>0\) one has the nonasymptotic bound
\[
S(t)\le e^{-A(t)/2}+\frac{8K}{3A(t)}.
\]
In fact, for any locally bounded nonnegative reactivity, not necessarily uniformly bounded, finite total reactivity \(\int_0^\infty\kappa<\infty\) still implies \(S(\infty)>0\).

**Failure without a uniform bound.** There exists a nonnegative \(C^\infty\) reactivity \(\kappa\), bounded on every finite time interval, such that
\[
\int_0^\infty\kappa(t)\,dt=\infty,
\qquad H_\infty<\infty\quad\text{almost surely},
\qquad 0<S(\infty)<1.
\]
Thus infinite total nominal reactivity does *not* force eventual reaction if the surface is activated in increasingly narrow, increasingly intense pulses. Moreover, this example has \(\mathbb E[H_\infty]=\infty\) even though \(H_\infty\) is almost surely finite.

## Assumptions and scope

The unreacted reflected process \(X\) is the unique standard reflected Brownian motion on the closed unit interval, with generator \(\partial_{xx}\), Neumann reflection at both endpoints, and invariant initial law \(X_0\sim\mathrm{Uniform}[0,1]\). Equivalently, \(dX_t=\sqrt2\,dB_t+d\ell_t-d\widetilde\ell_t\), with inward endpoint regulators. The reactivity \(\kappa:[0,\infty)\to[0,\infty)\) is deterministic, Borel measurable, and locally bounded; for the bounded-reactivity classification it also has a finite uniform upper bound \(K\). The boundary local time is normalized by
\[
\ell_t=\lim_{a\downarrow0}\frac1a\int_0^t\mathbf1_{[0,a)}(X_s)\,ds,
\]
where the limit is the usual continuous boundary-local-time version. This normalization gives \(\mathbb E[\ell_t]=t\) at equilibrium. The killing clock is an independent unit-mean exponential variable \(E\), with reaction occurring when \(H_t>E\). No spatially varying reactivity, interior absorption, moving boundary, or nonstationary initial distribution is asserted.

## Proof

**1. Exact time-weighted covariance.** The Neumann heat kernel for the reflected diffusion is
\[
p_u(x,y)=1+2\sum_{m\ge1}e^{-m^2\pi^2u}\cos(m\pi x)\cos(m\pi y),\qquad u>0.
\]
Write \(h(u)=p_u(0,0)-1=2\sum_{m\ge1}e^{-m^2\pi^2u}\ge0\). Stationarity, the Markov property, and occupation-density approximation of local time give, for nonnegative locally bounded \(\kappa\),
\[
\mathbb E[H_t]=A(t),\quad
\operatorname{Var}(H_t)=2\int_{0\le s<u\le t}\kappa(s)\kappa(u)h(u-s)\,ds\,du.
\]
Indeed, the off-diagonal second moment is the boundary-to-boundary transition density; the diagonal contributes no mass because local time is continuous. The short-time singularity of \(p_u(0,0)\) is of order \(u^{-1/2}\), so the two-time integrals are finite on compact time intervals and justify the boundary-layer limit. The function \(h(|u|)\), considered on the real line, satisfies
\[
\int_{-\infty}^{\infty}h(|u|)\,du
=4\sum_{m\ge1}\frac1{m^2\pi^2}=\frac23.
\]
Thus the variance is the quadratic convolution form of \(\kappa\mathbf1_{[0,t]}\) with the nonnegative even kernel \(h(|u|)\). Young's inequality and Cauchy--Schwarz give
\[
\operatorname{Var}(H_t)\le\|h(|\cdot|)\|_{L^1(\mathbb R)}\|\kappa\mathbf1_{[0,t]}\|_{L^2}^2
=\frac23\int_0^t\kappa(s)^2\,ds.
\]
For \(\kappa\equiv1\), the exact expression is \(2\int_0^t(t-u)h(u)\,du\); division by \(t\) and dominated convergence show that its limit is \(2\int_0^\infty h(u)du=2/3\). Hence the coefficient is sharp.

**2. Total-reactivity criterion under bounded forcing.** If \(A(\infty)<\infty\), monotone convergence and the first-moment identity yield \(\mathbb E H_\infty=A(\infty)<\infty\). Therefore \(H_\infty<\infty\) almost surely, and \(S(\infty)=\mathbb E[e^{-H_\infty}]>0\). This direction requires no uniform bound on \(\kappa\).

Now suppose \(\kappa\le K\) and \(A(t)\to\infty\). Then \(\kappa^2\le K\kappa\) implies
\[
\mathbb E\left[\left(\frac{H_t}{A(t)}-1\right)^2\right]
\le\frac{2K}{3A(t)}\longrightarrow0.
\]
To prove almost-sure, not merely in-probability, convergence, choose increasing times \(t_n\to\infty\) such that \(A(t_n)=n^2\). Continuity and divergence of \(A\) ensure their existence, allowing flat portions of \(A\). Chebyshev yields, for each \(\delta>0\),
\[
\sum_{n\ge1}\mathbb P\left(\left|\frac{H_{t_n}}{n^2}-1\right|>\delta\right)
\le\frac{2K}{3\delta^2}\sum_{n\ge1}n^{-2}<\infty.
\]
Borel--Cantelli and a countable sequence of \(\delta\)'s establish \(H_{t_n}/n^2\to1\) almost surely. Because both \(H\) and \(A\) are nondecreasing, for \(t_n\le t\le t_{n+1}\),
\[
\frac{H_{t_n}}{(n+1)^2}\le\frac{H_t}{A(t)}\le\frac{H_{t_{n+1}}}{n^2}.
\]
Both bounds approach one, proving the full almost-sure ratio law and \(H_\infty=\infty\). Hence \(S(t)\downarrow0\) by dominated convergence. For the claimed finite-time estimate, split the expectation on \(H_t\ge A(t)/2\) and its complement and apply Chebyshev:
\[
S(t)\le e^{-A(t)/2}+\mathbb P(H_t<A(t)/2)
\le e^{-A(t)/2}+4\frac{\operatorname{Var}(H_t)}{A(t)^2}
\le e^{-A(t)/2}+\frac{8K}{3A(t)}.
\]

**3. Smooth counterexample.** Fix any nonnegative, nonzero \(\varphi\in C_c^\infty((0,1))\) normalized by \(\int_0^1\varphi(u)du=1\). Put \(\varepsilon_n=2^{-4n}\) for integers \(n\ge1\), and define
\[
\kappa(t)=\sum_{n\ge1}\varepsilon_n^{-1}
\varphi\!\left(\frac{t-n}{\varepsilon_n}\right).
\]
The pulses have disjoint supports in \((n,n+\varepsilon_n)\), so the sum is locally finite, smooth and nonnegative. Each pulse has time integral exactly one, hence \(A(\infty)=\infty\).

Let \(E_n\) be the event that the *unreacted* reflected Brownian motion visits the reactive endpoint \(0\) at some time in \([n,n+\varepsilon_n]\). Since \(X_n\) is uniform and future Brownian increments are independent, the folding construction of reflected Brownian motion from \(x\in[0,1]\) shows that visiting \(0\) during the next \(\varepsilon\) units of time requires \(\sqrt2\sup_{0\le u\le\varepsilon}|B_u|\ge x\). The reflection principle and a Gaussian tail bound yield
\[
\mathbb P(E_n)\le4\int_0^1\exp\!\left(-\frac{x^2}{4\varepsilon_n}\right)dx
\le4\sqrt{\pi\varepsilon_n}.
\]
Consequently \(\sum_n\mathbb P(E_n)<\infty\) since \(\sum_n\sqrt{\varepsilon_n}=\sum_n4^{-n}=1/3\). Borel--Cantelli implies that almost surely only finitely many pulse intervals are ever visited at the reactive endpoint. Local time increases only while \(X_t=0\); therefore its weighted integral is zero on all but finitely many pulses. The finitely many remaining integrals are finite, because each pulse has bounded height and local time is finite on compact intervals. Thus \(H_\infty<\infty\) almost surely and \(S(\infty)>0\), despite \(\mathbb E H_\infty=A(\infty)=\infty\). Since the particle has positive probability of accumulating local time inside a nonzero pulse, \(\mathbb P(H_\infty>0)>0\), so \(S(\infty)<1\).

This completes all asserted statements.

## Verification

The Neumann eigenfunctions, the coefficient \(2/3\), and the occupation-time normalization can be checked independently. In particular, the equilibrium boundary-local-time mean is \(t\), while the constant-reactivity asymptotic variance is \((2/3)t+O(1)\). The folded-Brownian hitting argument provides a rigorous summable bound rather than a simulation of an infinite sequence of pulses. The accompanying `verify.py` computes finite spectral partial sums and checks their certified tail bounds; finite computations are corroboration only and no infinite statement relies on truncation. The analytic proof above establishes every universal quantifier and almost-sure assertion.

## Relationship to prior work

Grebenkov and Ye, *Diffusion-controlled reactions with time-dependent surface reactivity* (arXiv:2610.23017v1, publicly posted 2026-10-16), formulate time-dependent Robin surface reactions through boundary local time and discuss finite-total-reactivity survival and adiabatic long-time classes. Those formulations and sufficient implications are prior work. The present statement is the converse for every uniformly bounded measurable temporal reactivity, with a sharp covariance constant, a quantitative survival bound, and an explicit smooth but unbounded counterexample to extending the converse without its uniform bound. The Neumann heat kernel, boundary local time, spectral return kernels, and covariance calculus are classical tools, not claimed as new individually.

Grebenkov's *Probability distribution of the boundary local time of reflected Brownian motion in Euclidean domains* (arXiv:1909.07677) studies local-time distributions and their spectral background, mainly for non-time-weighted quantities. Grebenkov's *Residence times and other functionals of reflected Brownian motion* (Phys. Rev. E 76, 041139, 2007) covers general local-time functionals. Neither is claimed to have been exhaustively excluded as a possible source of an implicit general variance lemma. The precise novelty claim concerns the combined time-dependent sharp reaction/survival boundary, not the elementary spectral kernel alone.

## Limitations

The analysis is specific to one-dimensional bounded homogeneous reflected Brownian motion, equilibrium initialization, a fixed reactive endpoint, and deterministic temporal reactivity. Its sharp constant is for this normalization and domain; it is not asserted for other geometries or nonstationary starts. The pulse example requires peak heights increasing without bound, though the intensity remains smooth and finite at every fixed time. The upper survival bound need not be asymptotically optimal for individual reactivity profiles. Literature coverage may be incomplete, especially for general time-dependent boundary killing and related weighted additive-functional laws.

## References

1. D. S. Grebenkov and Y. Ye, *Diffusion-controlled reactions with time-dependent surface reactivity*, arXiv:2610.23017v1 (2026), https://arxiv.org/abs/2610.23017.
2. D. S. Grebenkov, *Probability distribution of the boundary local time of reflected Brownian motion in Euclidean domains*, Physical Review E 100, 062110 (2019), arXiv:1909.07677, https://arxiv.org/abs/1909.07677.
3. D. S. Grebenkov, *Residence times and other functionals of reflected Brownian motion*, Physical Review E 76, 041139 (2007), DOI:10.1103/PhysRevE.76.041139.
4. Y. Ye and D. S. Grebenkov, *Correlation between the first-reaction time and the acquired boundary local time*, arXiv:2512.16747 (2025), https://arxiv.org/abs/2512.16747.
