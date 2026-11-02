# Universal sign criterion for Gaussian quadratic qubit dephasing

## Finding
Consider a pure-dephasing qubit coupled quadratically to a real centered Gaussian environment, with an arbitrary bounded deterministic modulation. The following universal characterization is exact: its reduced qubit maps are completely-positive divisible for **every** Gaussian bath covariance if and only if the modulation has one fixed sign almost everywhere. Equivalently, every genuinely sign-changing modulation admits a finite-correlation stationary Ornstein–Uhlenbeck bath for which the coherence revives strictly. The result separates bath-universal absence of information backflow from decoherence behavior of any one chosen bath.

## Assumptions and scope
Fix a finite horizon \(T>0\), a nonzero real coupling \(\kappa\), and a real \(g\in L^\infty([0,T])\). For every centered, jointly measurable, real Gaussian process \(Z\) with continuous positive-semidefinite covariance \(C(s,t)\) on \([0,T]^2\), let
\[
Q_t=\int_0^t g(u)\bigl(Z_u^2-C(u,u)\bigr)\,du,\qquad F(t)=\mathbb E\exp(i\kappa Q_t).
\]
The corresponding ensemble-averaged random-unitary qubit dynamics leaves populations unchanged and multiplies one off-diagonal matrix entry by \(F(t)\) (the other by its conjugate). In Hamiltonian terms, \(H_u=\kappa g(u)(Z_u^2-C(u,u))\sigma_z/2\); the convention for which off-diagonal entry receives \(F\) is immaterial. Brownian and other physical Gaussian bath realizations are included whenever their covariances meet these conditions.

The theorem asserts that
\[
\left(\forall C\text{ as above},\ \{\Lambda_t\}_{0\le t\le T}\text{ is CP-divisible}\right)
\quad\Longleftrightarrow\quad
\bigl(g\ge0\text{ a.e.}\bigr)\ \text{or}\ \bigl(g\le0\text{ a.e.}\bigr).
\]
If \(g\) changes sign on sets of positive measure, a stationary Ornstein–Uhlenbeck bath with covariance \(C_\varepsilon(s,t)=\sigma^2e^{-\varepsilon|s-t|}\), some finite \(\varepsilon>0\), violates CP-divisibility. This bath has a nonzero finite correlation time, is nondegenerate and mixing. Neither a white-noise limit nor singular quenched noise is required for the counterexample.

## Proof
**Gaussian quadratic representation.** On the real Hilbert space \(\mathcal H=L^2([0,T])\), continuous covariance \(C\) defines a nonnegative trace-class covariance operator \(\mathcal C\): its trace is \(\int_0^T C(u,u)\,du<\infty\). Define \(M_t\) as multiplication by \(g(u)\mathbf1_{[0,t]}(u)\), and set \(B_t=\mathcal C^{1/2}M_t\mathcal C^{1/2}\). Then \(B_t\) is self-adjoint and trace class. A Karhunen–Loève expansion and convergence in quadratic-mean (equivalently the Gaussian quadratic-form determinant identity) give
\[
F(t)=\exp\bigl(-i\kappa\operatorname{tr} B_t\bigr)
\det\bigl(I-2i\kappa B_t\bigr)^{-1/2},
\]
where the square-root branch is continuous from \(\kappa=0\). In particular, for the real eigenvalues \(\lambda_j(B_t)\), counted with multiplicity,
\[
|F(t)|=\prod_j\bigl(1+4\kappa^2\lambda_j(B_t)^2\bigr)^{-1/4}>0.
\]
The last product converges to a strictly positive value because \(\sum_j\lambda_j(B_t)^2<\infty\); the phase from centering does not affect it.

**Sufficiency.** If \(g\ge0\) a.e., then \(0\preceq B_s\preceq B_t\) for \(0\le s\le t\), since their difference is \(\mathcal C^{1/2}M_{(s,t]}\mathcal C^{1/2}\succeq0\). By the min–max principle, each ordered nonnegative eigenvalue of \(B_t\) is nondecreasing. The convergent product above implies that \(|F(t)|\) is nonincreasing. For \(g\le0\) replace \(B_t\) with \(-B_t\). Every \(\Lambda_s\) is invertible as a linear qubit map because \(F(s)\ne0\), and \(\Lambda_t\Lambda_s^{-1}\) is a dephasing channel with off-diagonal multiplier \(F(t)/F(s)\). That intermediate map is completely positive and trace preserving precisely when \(|F(t)/F(s)|\le1\). Thus all intermediates are channels.

**Necessity and the finite-memory witness.** Write \(G(t)=\int_0^t g(u)\,du\). If \(g\) has both signs on sets of positive measure, there exist \(0\le s<t\le T\) with \(|G(t)|<|G(s)|\). Indeed, if \(|G|\) were nondecreasing, continuity and absolute continuity would force \(G\) to keep its sign after first leaving zero, with its derivative of that same sign almost everywhere; on its zero set the derivative is zero almost everywhere. Consequently \(g=G'\) would have a fixed sign almost everywhere, a contradiction.

For the static Gaussian \(Z_u=\xi\), \(\xi\sim N(0,\sigma^2)\), direct evaluation gives
\[
|F(t)|=\bigl(1+4\kappa^2\sigma^4G(t)^2\bigr)^{-1/4}.
\]
At the two selected times this has \(|F(t)|>|F(s)|\). To replace the static witness by a finite-memory bath, couple the stationary processes
\[
Z_u^{(\varepsilon)}=e^{-\varepsilon u}\xi+
\sigma\sqrt{2\varepsilon}\int_0^u e^{-\varepsilon(u-v)}\,dW_v,
\qquad \varepsilon>0,
\]
where \(W\) is independent of \(\xi\). Their covariances are exactly \(\sigma^2e^{-\varepsilon|u-v|}\). On the finite horizon, \(Z^{(\varepsilon)}\to\xi\) in \(L^2(\Omega\times[0,T])\). Uniform second-moment bounds and Cauchy–Schwarz therefore give \(Q_u^{(\varepsilon)}\to(\xi^2-\sigma^2)G(u)\) in \(L^1\) for each \(u\). The characteristic functions, hence their moduli, converge. The strict reversal between \(s\) and \(t\) survives for every sufficiently small **positive** \(\varepsilon\). The associated intermediate qubit map is not completely positive. This proves necessity with a mixing, exponentially correlated Gaussian bath.

## Verification
The standalone file `verify_quadratic_dephasing.py` implements the finite-dimensional version of the determinant formula by symmetrically conjugating weighted covariances, and compares it with direct complex determinants. Its reproducible seeded tests include oscillatory (possibly negative-valued) positive-semidefinite covariances, unequal modulations, and finite-correlation Ornstein–Uhlenbeck echo profiles. Executing it with Python 3 and NumPy completed **518** finite numerical comparisons: **480** Loewner-monotonicity comparisons, **18** echo/static checks, and **20** complex determinant checks. These are independent sanity checks; the all-covariance and all-time quantifiers are proved by the analytic argument above, not inferred from finite tests.

## Relationship to prior work
Cai et al. (2024) derive quadratic and linear decoherence functions for specified fluctuating environments, including nonstationary Ornstein–Uhlenbeck noise. Cywiński (2013) develops quadratic-noise dephasing under dynamical-decoupling sign changes and its noise spectroscopy, and Norris, Paz-Silva, and Viola (2015) provide related non-Gaussian noise-spectroscopy theory. These works supply the motivating physical settings and much of the standard quadratic-Gaussian machinery. The claim here is **not** that squared-Gaussian decoherence, Gaussian characteristic determinants, pulse-induced echo, or the CP-divisibility criterion was previously unknown. Its asserted additional classification concerns an arbitrary bounded deterministic modulation and the universal quantifier over **every** continuous Gaussian covariance, together with a finite-correlation stationary bath witnessing the converse. No general publication-priority guarantee follows from a literature search.

## Limitations
The universal criterion concerns commuting pure dephasing, centered *classical Gaussian* quadratic noise, bounded deterministic modulation, and finite time horizons. It does not assert monotonicity for controls whose sign changes in a fixed chosen bath, nor describe quantum back-action, noncommuting system–bath couplings, or operational multi-time quantum Markovianity beyond CP-divisibility of the reduced maps. The witness requires choosing an adequately slow but strictly positive Ornstein–Uhlenbeck relaxation rate. Related broad results on Gaussian quadratic forms or quantum dephasing may imply this classification; definitive precedence has not been established. Independent scientific validation has not been performed.

## References
- X. Cai, Y. Feng, J. Ren, Y. Peng, Y. Zheng, “Quantum decoherence dynamics in stochastically fluctuating environments,” arXiv:2407.06074 (first submitted 2024-07-08), https://arxiv.org/abs/2407.06074.
- Ł. Cywiński, “Dynamical decoupling noise spectroscopy at an optimal working point of a qubit,” arXiv:1308.3102 (2013), https://arxiv.org/abs/1308.3102.
- L. M. Norris, G. A. Paz-Silva, L. Viola, “Qubit noise spectroscopy for non-Gaussian dephasing environments,” arXiv:1512.01575 (2015), https://arxiv.org/abs/1512.01575.
- Standard background: Gaussian quadratic-form Fredholm determinant identity; compact self-adjoint min–max principle; CP criterion for a qubit phase-damping channel.
