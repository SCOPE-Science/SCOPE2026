# A beta-law for macroscopic energy in globally reset harmonic Brownian gases

## Finding

For an interacting, globally reset harmonic Brownian gas, the finite-population stationary mean-square position has an exact **two-mode, common-age chi-square law**. Its large-population limit is a nondegenerate scaled beta random variable: the macroscopic energy fails to self-average despite independent thermal noises. The limiting energy has exact exponential time correlation and a time-average central limit theorem. When particles are noninteracting, a sharp finite-size comparison shows that synchronized resetting creates a strictly positive excess squared coefficient of variation over independent resetting, even though the mean energies coincide.

Write \(b=\kappa+\lambda\), \(a=r/(2b)\), and \(H_N=N^{-1}\sum_{i=1}^N X_i^2\). At stationarity,
\[
 H_N\ \stackrel{d}{=}\ \frac{c_\kappa(A)Z_0^2+c_b(A)\sum_{j=1}^{N-1}Z_j^2}{N},\quad A\sim\mathrm{Exp}(r),
\]
where all \(Z_j\) are independent standard Gaussians, independent of \(A\), and \(c_q(t)=2D\int_0^t e^{-2qs}\,ds\). The stationary age \(A\) is **shared** by all modes. The exact finite-population mean and second moment are
\[
 \mathbb E H_N=\frac{m_\kappa+(N-1)m_b}{N},\qquad
 \mathbb E H_N^2=\frac{3K_{\kappa\kappa}+(N^2-1)K_{bb}+2(N-1)K_{\kappa b}}{N^2},
\]
where \(m_q=2D/(r+2q)\) and \(K_{pq}=r\int_0^\infty e^{-rt}c_p(t)c_q(t)\,dt\). These expressions are finite also at \(\kappa=0\). For \(p,q>0\),
\[
 K_{pq}=\frac{D^2}{pq}\left(1-\frac{r}{r+2p}-\frac{r}{r+2q}+\frac{r}{r+2p+2q}\right),
\]
with continuous limits at zero.

As \(N\to\infty\),
\[
 H_N\ \Longrightarrow\ H_\infty=\frac Db(1-e^{-2bA}),\qquad U:=\frac bD H_\infty\sim\operatorname{Beta}(1,a).
\]
The normalized density is \(f_U(u)=a(1-u)^{a-1}\) for \(0<u<1\). In particular,
\[
 \mathbb E H_\infty=\frac{2D}{r+2b},\quad
 \operatorname{Var}(H_\infty)=\left(\frac Db\right)^2\frac{a}{(a+1)^2(a+2)},\quad
 \frac{\operatorname{Var}(H_\infty)}{(\mathbb E H_\infty)^2}=\frac{a}{a+2}=\frac{r}{r+4b}>0.
\]
Thus population averaging does **not** remove stationary energy noise. For the stationary limiting process \(H_\infty(t)\),
\[
 \operatorname{Corr}(H_\infty(0),H_\infty(t))=e^{-(r+2b)|t|}.
\]
Nevertheless, its *time average* satisfies
\[
 \sqrt T\left(\frac1T\int_0^T H_\infty(t)\,dt-\frac{2D}{r+2b}\right)
 \Longrightarrow\mathcal N\left(0,\frac{2\operatorname{Var}(H_\infty)}{r+2b}\right).
\]

For the noninteracting specialization \(\lambda=0\), \(\kappa>0\), compare a global reset clock to independent rate-\(r\) reset clocks, with identical one-particle dynamics and the same stationary energy mean. Then for every integer \(N\ge2\), the squared coefficients of variation obey the **exact sharp gap**
\[
 \operatorname{CV}_{\mathrm{global}}(H_N)^2-\operatorname{CV}_{\mathrm{local}}(H_N)^2
 =\frac{a}{a+2}\left(1-\frac1N\right)>0,\qquad a=\frac{r}{2\kappa}.
\]
Equivalently,
\[
 \operatorname{CV}_{\mathrm{global}}(H_N)^2
 =\frac{a}{a+2}+\frac{4(a+1)}{N(a+2)},\quad
 \operatorname{CV}_{\mathrm{local}}(H_N)^2
 =\frac{5a+4}{N(a+2)}.
\]
There is no positive global/local gap at \(N=1\), and at fixed \(r,\kappa>0\) the local squared coefficient tends to zero while the global one tends to \(r/(r+4\kappa)\).

## Assumptions and scope

Fix an integer \(N\ge2\), \(D>0\), \(r>0\), \(\kappa\ge0\), \(\lambda\ge0\), with \(b=\kappa+\lambda>0\). Let \(B_1,\ldots,B_N\) be independent standard Brownian motions and let a separate rate-\(r\) Poisson process have jump times at which **all** positions reset instantaneously to zero. Between these times,
\[
 dX_i=\left[-\kappa X_i-\lambda(X_i-\overline X)\right]dt+\sqrt{2D}\,dB_i,\qquad \overline X=\frac1N\sum_i X_i.
\]
A unique regenerative stationary law exists for each \(N\), also when \(\kappa=0\), since the next reset occurs almost surely and all polynomial stationary moments are finite. Statements about population limits concern the stationary ensembles for fixed \(D,r,\kappa,\lambda\); the chronological central limit concerns the limiting stationary energy process, not a uniform-in-\(N\) double limit. The independent-reset comparator applies only when \(\lambda=0\), \(\kappa>0\).

## Proof

**Regeneration and orthogonal modes.** At a stationary observation time the elapsed time \(A\) since the most recent event of a homogeneous Poisson clock has distribution \(\mathrm{Exp}(r)\), independent of the post-reset Brownian increments. The drift matrix has one unit center eigenvector with eigenvalue \(-\kappa\), and \(N-1\) orthogonal relative-coordinate eigenvectors with eigenvalue \(-b\). An orthogonal transform preserves the independence and variance of Brownian increments. Starting all modes from zero, conditional on \(A=t\) they are independent centered Gaussians with variances \(c_\kappa(t)\) and \(c_b(t)\), respectively. Parseval's identity proves the stated distribution of \(H_N\). Conditional chi-square moments \(\mathbb E Z^4=3\) and \(\mathbb E(\chi^2_m)^2=m(m+2)\) prove the finite-\(N\) expressions; integrating with respect to exponential \(A\) evaluates \(m_q\) and \(K_{pq}\). The integral definition covers \(q=0\) without division by zero.

**Population limit and non-self-averaging.** Couple the chi-square variables for different \(N\) using one age \(A\), one center Gaussian and an infinite sequence of independent relative-mode Gaussians. The strong law gives \((N-1)^{-1}\sum_{j=1}^{N-1}Z_j^2\to1\) almost surely, while \(N^{-1}c_\kappa(A)Z_0^2\to0\). Hence \(H_N\to c_b(A)\) almost surely in this coupling. Since \(e^{-2bA}\) has distribution function \(z^a\) on \((0,1)\), its complement has \(\operatorname{Beta}(1,a)\) density; its first two beta moments give all displayed limit formulas. Positive beta variance proves absence of thermodynamic self-averaging. The same limit holds in probability at every fixed physical time for the stationary population process by conditional independence of relative Gaussian modes, and therefore determines finite-dimensional temporal correlations.

**Temporal covariance and central limit.** The limiting normalized energy \(U_t=bH_\infty(t)/D\) evolves deterministically as \(\dot U_t=2b(1-U_t)\) between rate-\(r\) resets and jumps to zero at resets. Its generator on smooth functions is \(Lf(u)=2b(1-u)f'(u)+r[f(0)-f(u)]\). Setting \(\overline u=2b/(r+2b)\), one has \(L(u-\overline u)=-(r+2b)(u-\overline u)\). The Markov conditional-expectation formula therefore gives exactly \(\operatorname{Cov}(U_0,U_t)=e^{-(r+2b)t}\operatorname{Var}(U_0)\). For the time-average central limit, Dynkin's martingale \(M_t=U_t-U_0-\int_0^t LU_s\,ds\) has bounded jumps \(-U_{s-}\) and predictable quadratic variation \(\langle M\rangle_t=r\int_0^t U_s^2\,ds\). Regenerative ergodicity gives \(T^{-1}\langle M\rangle_T\to r\mathbb E U^2\) almost surely. Bounded jumps imply the martingale Lindeberg condition. The martingale central limit theorem, together with bounded endpoint terms and the Poisson-equation identity, proves the stated Gaussian limit, because \(r\mathbb E U^2/(r+2b)^2=2\operatorname{Var}(U)/(r+2b)\). Multiplication by \(D/b\) restores units.

**Independent versus global clocks.** When \(\lambda=0\), each stationary particle has the same marginal Gaussian exponential-age mixture regardless of clock coupling. Write \(a=r/(2\kappa)\), and let \(V=1-e^{-2\kappa A}\sim\operatorname{Beta}(1,a)\). In the global case \(H_N\) has law \((D/\kappa)V\chi_N^2/N\), with independent factors; thus its squared coefficient of variation is \((1+2/N)\mathbb E V^2/(\mathbb E V)^2-1\). In the local case, \(H_N\) averages \(N\) independent copies of \((D/\kappa)VZ^2\), giving squared coefficient \([3\mathbb E V^2/(\mathbb E V)^2-1]/N\). Since \(\mathbb E V=1/(a+1)\) and \(\mathbb E V^2=2/[(a+1)(a+2)]\), subtraction gives the exact positive gap. There are no unquantified parameter restrictions or omitted equality cases.

## Verification

Run `python verify.py` with NumPy installed. The program evaluates finite-population moments in two independent ways: the exponential-age Gaussian mixture and exact stationarity equations for quadratic and quartic normal-mode polynomials. It then compares 100,000 stationary samples in each of four parameter regimes, including one with zero center-mode confinement. It checks the finite-\(N\) global/local gap algebraically for twelve parameter combinations and beta first and second moments at three reset ratios. The executed program printed `PASS`. Finite Monte Carlo is corroboration only, not evidence for the population or time-asymptotic theorem.

## Relationship to prior work

P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization* (arXiv:2401.03501, first posted 2024-01-07), establishes the general distinction between global and local reset clocks and persistence of macroscopic correlations. Its Sec. III treats locally reset Curie-Weiss interactions, while Sec. IV establishes functional-density correlation equations for globally resetting **noninteracting** particles, without the present interacting finite-\(N\) energy law or global/local energy-variance gap. The paper's explicitly solved resetting Kuramoto-order-parameter distribution is mathematically analogous to a one-dimensional reset-driven observable, and the present beta transform is **not claimed to be a novel general resetting mechanism**.

G. De Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols* (arXiv:2509.06658), treats freely diffusing particles, exhibits the common-age conditional independence structure, and evaluates positional order, spacings and counting statistics. Its general age-mixture argument anticipates a key ingredient, but it does not evaluate the harmonic Curie-Weiss finite-\(N\) energy, the sharp independent/global variance gap, or the interacting macroscopic energy dynamics. The novelty claimed here is the **combined evaluated physical energy-statistics theorem**, not the underlying regenerative representation, Gaussian filtering, beta change of variables, or standard martingale central limit methodology.

## Limitations

All resets are simultaneous jumps to the origin, the interaction is linear and mean-field, and each thermal noise is independent. The normalized energy is empirical **mean-square position**, not thermodynamic internal energy including the quadratic interaction potential; physical interaction energy would require a separately stated normalization. The large-\(N\) stationary law is proved at fixed parameters; interacting independent-reset particles do not satisfy the independent comparator's assumptions. Statistical novelty is assessed from inspected primary publications and targeted research records, not from an exhaustive proof of publication priority. Generic regenerative and linear-Gaussian theorems could subsume constituent steps. No experiment is asserted to establish the infinite-population or long-time limit.

## References

1. P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501 (2024), https://arxiv.org/abs/2401.03501; full preprint https://arxiv.org/pdf/2401.03501.
2. G. De Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025), https://arxiv.org/abs/2509.06658; full preprint https://arxiv.org/pdf/2509.06658.
