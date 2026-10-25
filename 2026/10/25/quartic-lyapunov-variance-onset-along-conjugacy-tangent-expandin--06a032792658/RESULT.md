# Quartic Lyapunov-variance onset along conjugacy-tangent expanding maps

## Finding

Let \(d\geq2\) be an integer, let \(\mathbb T=\mathbb R/\mathbb Z\), and take a real \(u\in C^5(\mathbb T)\). Put \(T_d(x)=dx\pmod1\), \(v(x)=d u(x)-u(dx)\), and define the orientation-preserving covering maps
\[
f_\varepsilon(x)=dx+\varepsilon v(x)\pmod1.
\]
For all sufficiently small real \(\varepsilon\), these maps are uniformly expanding. Let \(\mu_\varepsilon\) be the unique measure of maximal entropy and let their **maximal-entropy Lyapunov asymptotic variance** be
\[
\sigma^2(\varepsilon)=\lim_{N\to\infty}\frac1N\int\!\left(\sum_{j=0}^{N-1}\log f_\varepsilon'(f_\varepsilon^j x)-N\int\log f_\varepsilon'\,d\mu_\varepsilon\right)^2d\mu_\varepsilon(x).
\]
Writing
\[
w(x)=u'(dx)\,[d u(x)-u(dx)],\qquad \phi(x)=\frac{w'(x)}d,
\]
and denoting by \(\mathcal V_{T_d}(\phi)\) the Green–Kubo asymptotic variance of \(\phi\) under Lebesgue measure for \(T_d\), one has the **quartic onset formula**
\[
\boxed{\displaystyle\lim_{\varepsilon\to0}\frac{\sigma^2(\varepsilon)}{\varepsilon^4}=\mathcal V_{T_d}(\phi).}
\]
The limit may be zero for special \(u\); the formula alone does not assert strict positivity in every direction.

For the explicit smooth degree-two family
\[
f_\varepsilon(x)=2x+\varepsilon\left[\frac{\sin(4\pi x)}{2\pi}-\frac{\sin(2\pi x)}\pi\right]\pmod1,
\]
which is expanding whenever \(|\varepsilon|<1/4\), the coefficient is strictly positive and **exactly**
\[
\boxed{\displaystyle\lim_{\varepsilon\to0}\frac{\sigma^2(\varepsilon)}{\varepsilon^4}=\frac94.}
\]
In particular, \(\sigma^2(\varepsilon)>0\) for all sufficiently small nonzero \(\varepsilon\): these maps are not smoothly conjugate to the doubling map, despite being tangent at first order to a smooth-conjugacy deformation.

## Assumptions and scope

All derivatives are taken on real degree-\(d\) lifts and are periodic where appropriate. The invariant probability measures are **measures of maximal entropy**, not the absolutely continuous invariant measures in general. The small-parameter limit is taken at fixed \(d\) and fixed \(u\), with \(u\in C^5\). The variance concerns the observable \(\log f_\varepsilon'\), normalized per iterate, and not the variance of the exponent divided by its period; the latter has the leading asymptotic \(\sigma^2(\varepsilon)/N\) as the period tends to infinity at fixed \(\varepsilon\).

## Proof

**1. Second-order conjugacy defect.** For sufficiently small \(\varepsilon\), \(H_\varepsilon(x)=x+\varepsilon u(x)\) is an orientation-preserving \(C^5\) circle diffeomorphism. Taylor inversion gives, in \(C^2\),
\[
H_\varepsilon^{-1}(x)=x-\varepsilon u(x)+\varepsilon^2u(x)u'(x)+O(\varepsilon^3).
\]
For \(G_\varepsilon=H_\varepsilon\circ f_\varepsilon\circ H_\varepsilon^{-1}\), substitution and the identity \(v=d u-u\circ T_d\) cancel the first-order term. The second-order term is
\[
\begin{aligned}
G_\varepsilon(x)&=dx+\varepsilon^2w(x)+O_{C^2}(\varepsilon^3),\\
w(x)&=u'(dx)v(x).
\end{aligned}
\]
Indeed, before simplification its coefficient is \(d u'u-v'u+u'(dx)(v-du)\), and using \(v'=d u'-d u'(dx)\) reduces this to \(u'(dx)v\). Consequently the normalized logarithmic derivative obeys
\[
\psi_\varepsilon:=\frac{\log G_\varepsilon'-\log d}{\varepsilon^2}\longrightarrow\frac{w'}d=\phi\quad\text{in }C^1(\mathbb T).
\]

**2. Invariance of the variance under smooth conjugacy.** Writing \(y=H_\varepsilon(x)\), the chain rule gives
\[
\log G_\varepsilon'(y)=\log f_\varepsilon'(x)+\log H_\varepsilon'(f_\varepsilon x)-\log H_\varepsilon'(x).
\]
The final two terms form a bounded coboundary. Since \(H_{\varepsilon*}\mu_\varepsilon\) is the maximal-entropy measure of \(G_\varepsilon\), telescoping this coboundary changes length-\(N\) sums by a uniformly bounded quantity. The asymptotic variances coincide and constants do not affect variance. Therefore
\[
\frac{\sigma^2(\varepsilon)}{\varepsilon^4}=\mathcal V_{G_\varepsilon}(\psi_\varepsilon).
\]

**3. Continuity of Green–Kubo variance at the integer covering.** If a uniformly expanding family of degree-\(d\) circle maps \(G_t\to T_d\) in \(C^1\) has observables \(a_t\to a_0\) in \(C^1\), then
\(\mathcal V_{G_t}(a_t)\to\mathcal V_{T_d}(a_0)\), with maximal-entropy measures throughout. To see this without a parameter-dependent unproved spectral assumption, code each map by the full one-sided \(d\)-symbol shift, assigning mass \(d^{-m}\) to each depth-\(m\) cylinder. Uniform expansion gives a common \(\lambda>1\) and a cylinder diameter bound \(C\lambda^{-m}\), uniformly near \(T_d\). For a uniformly Lipschitz observable, its value on a coding sequence differs from the approximation determined by its first \(m\) symbols by at most \(C'\lambda^{-m}\). Taking \(m=\lfloor n/2\rfloor\), independence of the first \(m\) symbols from the tail beginning at \(n\) bounds the lag-\(n\) centered correlation by \(C''\lambda^{-n/2}\), uniformly over the family. At each fixed lag, coding maps and observables converge almost everywhere in symbolic coordinates (the exceptional multiple codings have Bernoulli measure zero). Dominated convergence over lags now proves convergence of the absolutely convergent Green–Kubo series. Applying the lemma to \(G_\varepsilon\) and \(\psi_\varepsilon\) proves the general formula.

**4. Exact coefficient.** Choose \(d=2\) and \(u(x)=-\sin(2\pi x)/(2\pi)\). Then \(v=2u-u(2x)\) gives the displayed map and elementary product-to-sum identities give
\[
w(x)=\frac{\sin(6\pi x)-\sin(2\pi x)}{2\pi}-\frac{\sin(8\pi x)}{4\pi},
\quad
\phi(x)=\frac32\cos(6\pi x)-\frac12\cos(2\pi x)-\cos(8\pi x).
\]
Orthogonality of Fourier modes shows \(\int\phi^2dx=7/4\), \(\int\phi(x)\phi(2x)dx=0\), \(\int\phi(x)\phi(4x)dx=1/4\), and \(\int\phi(x)\phi(2^n x)dx=0\) for all \(n\ge3\). Thus
\[
\mathcal V_{T_2}(\phi)=\frac74+2\cdot\frac14=\frac94.
\]
The positive limit forces \(\sigma^2(\varepsilon)>0\) for sufficiently small nonzero \(\varepsilon\), and smooth conjugacy to the linear map would make the derivative observable a constant plus coboundary and its variance zero. This proves the stated non-conjugacy.

## Verification

The standalone `check.py` uses exact rational arithmetic to verify the nonzero Fourier correlations and the coefficient \(9/4\). It also numerically compares the actual conjugated maps and their logarithmic derivatives against the second-order formulas at \(\varepsilon\in\{0.08,0.04,0.02,0.01\}\), at 137 fixed points on the circle. Run `python3 check.py`; the included `check_output.txt` records the result `CHECKS_PASS`. The rational Fourier calculation independently checks the critical arithmetic; numerical convergence is a finite consistency check, not a proof of the all-parameter asymptotic.

## Relationship to prior work

Drach, Fu, Kaloshin, Li and Liverani (arXiv:2511.15662, first posted 2025-11-19) prove a central limit theorem for periodic Lyapunov exponents of each fixed nonlinearly expanding smooth circle map, and formulate its variance by a Green–Kubo correlation series. Their fixed-map results do not calculate its rate of vanishing when the map approaches an integer covering in a conjugacy-tangent direction. Baladi and Smania (arXiv:0705.3383) investigate linear response tangent to topological classes for piecewise expanding interval maps, a different (SRB expectation) statistic; Erchenko (2019) studies flexible values of mean Lyapunov exponents, not this variance onset. The result here quantifies the higher-order mechanism and gives a concrete exact coefficient for a smooth degree-two family.

## Limitations

The result does not assert a central limit theorem **uniform** in \(\varepsilon\) and period. The general quartic coefficient can vanish, and no higher-order asymptotic is claimed in that case. The coefficient concerns the maximal-entropy measure and need not equal the coefficient for the absolutely continuous invariant measure. A general pressure-analyticity theorem may imply parts of the perturbative mechanism under an alternative formulation; the exact stated curvature formula and trigonometric coefficient have not received independent priority or mathematical audit.

## References

- K. Drach, Z. Fu, V. Kaloshin, Z. Li, C. Liverani, *Normal distribution of Lyapunov exponents of periodic orbits for expanding circle maps*, arXiv:2511.15662v1 (2025-11-19), https://arxiv.org/abs/2511.15662 .
- V. Baladi, D. Smania, *Linear response formula for piecewise expanding unimodal maps*, arXiv:0705.3383 (2007), https://arxiv.org/abs/0705.3383 .
- A. Erchenko, *Flexibility of Lyapunov exponents for expanding circle maps*, Discrete and Continuous Dynamical Systems 39 (2019), 2325–2342, https://doi.org/10.3934/dcds.2019098 .
