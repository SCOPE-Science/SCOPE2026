# A mixed-Poisson Zeno crossover under common quantum resetting

## Finding

Consider \(N\) noninteracting spins with Hamiltonian
\[
H_N=\sum_{j=1}^N(\Omega\sigma_j^x+\Delta\sigma_j^z),
\qquad \Omega>0,\quad\Delta\in\mathbb R.
\]
They are collectively reset to \(|\uparrow\rangle^{\otimes N}\) at the events of one Poisson clock of rate \(\gamma_N>0\). At stationarity, measure all spins once in the \(\sigma^z\) basis, and let \(K_N\) count outcomes \(|\downarrow\rangle\). Set \(c_N=\gamma_N/(\Omega\sqrt N)\).

**Theorem (three-regime collective Zeno law).** When \(c_N\to c\in(0,\infty)\),
\[
K_N\ \Longrightarrow\ Z_c,\qquad
Z_c\mid E\sim\operatorname{Poisson}(E^2/c^2),\quad E\sim\operatorname{Exp}(1).
\]
Equivalently, for \(0\le s\le1\),
\[
\lim_{N\to\infty}\mathbb E[s^{K_N}]
=G_c(s)=\int_0^\infty e^{-u-(1-s)u^2/c^2}\,du.
\]
The complete limiting distribution has factorial moments
\(\mathbb E[(Z_c)_k]=(2k)!/c^{2k}\) for all integers \(k\ge0\), with
\[
\mathbb E Z_c=\frac2{c^2},\qquad
\operatorname{Var}(Z_c)=\frac2{c^2}+\frac{20}{c^4},\qquad
\frac{\operatorname{Var}(Z_c)}{\mathbb E Z_c}=1+\frac{10}{c^2}.
\]
Its upper tail is stretched exponential, in the sharp logarithmic sense
\[
\lim_{k\to\infty}\frac{-\log\Pr(Z_c\ge k)}{\sqrt k}=c.
\]
If instead \(c_N\to\infty\), then \(K_N\to0\) in probability. If \(c_N\to0\) while \(\gamma_N\to\infty\), then
\[
c_N^2K_N\ \Longrightarrow\ E^2,\qquad E\sim\operatorname{Exp}(1),
\]
and the displayed convergence also holds in the second-moment sense under a common coupling.

**Protocol contrast.** Resetting each spin independently at rate \(\gamma_N\), rather than using a shared clock, leaves every single-spin stationary marginal unchanged. However, at \(c_N\to c\in(0,\infty)\) its total down-spin count converges to \(\operatorname{Poisson}(2/c^2)\), rather than \(Z_c\). In particular, its limiting variance is \(2/c^2\), not \(2/c^2+20/c^4\). In the shared-clock protocol, the exact no-flip probability is asymptotically
\[
\Pr(Z_c=0)=\frac{\sqrt\pi c}{2}e^{c^2/4}\operatorname{erfc}(c/2)
>e^{-2/c^2},
\]
the independent-clock no-flip limit. The threshold exponent \(1/2\), limiting law, and detuning independence are all consequences of quadratic short-time Rabi excitation.

## Assumptions and scope

The model uses unitary evolution with \(\hbar=1\), independent, identically driven spins, **one global complete Poisson reset** in the first protocol, fixed \(\Omega>0\) and fixed real \(\Delta\), a stationary observation time, and a single simultaneous projective readout in the \(\sigma^z\) basis. The long-time stationary limit is taken for every finite \(N\) before the joint \(N\to\infty\) and \(\gamma_N\)-scaling limit. The observation readout is not used to select the reset state. The comparison protocol has one independent rate-\(\gamma_N\) clock per spin.

Let \(\omega=(\Omega^2+\Delta^2)^{1/2}\). At elapsed time \(t\) after a collective reset, the probability that one spin is down is
\[
p(t)=\frac{\Omega^2}{\omega^2}\sin^2(\omega t).
\]
There is no restriction on the sign or magnitude of the fixed detuning. The regime \(c_N\to0\) includes only sequences with \(\gamma_N\to\infty\) in its additional statement; a bounded reset rate has a different macroscopic limit.

## Proof

**1. Exact stationary count law.** The age \(A_N\) since the last event of a stationary Poisson reset clock is exponential of rate \(\gamma_N\). The state conditional on \(A_N=t\) is a tensor product of identical pure spin states, so the projective readout satisfies
\[
K_N\mid A_N=t\sim\operatorname{Bin}(N,p(t)).
\]
Consequently the following finite-size identity holds, for every \(N\ge1\), \(\gamma_N>0\), and \(0\le s\le1\):
\[
\mathbb E[s^{K_N}]=\int_0^\infty\gamma_Ne^{-\gamma_N t}
\bigl[1-(1-s)p(t)\bigr]^N\,dt.
\tag{1}
\]
One-spin and two-spin averages, evaluated from exponential-weighted sine integrals, are
\[
\mu_N:=\mathbb E[p(A_N)]
=\frac{2\Omega^2}{\gamma_N^2+4\omega^2},
\quad
\mathbb E[p(A_N)^2]
=\frac{24\Omega^4}{(\gamma_N^2+4\omega^2)(\gamma_N^2+16\omega^2)}.
\]
Their difference is
\[
C_N:=\operatorname{Var}(p(A_N))
=\frac{4\Omega^4(5\gamma_N^2+8\omega^2)}
{(\gamma_N^2+4\omega^2)^2(\gamma_N^2+16\omega^2)}.
\]
It follows exactly that
\[
\mathbb E K_N=N\mu_N,\qquad
\operatorname{Var}(K_N)=N\mu_N(1-\mu_N)+N(N-1)C_N.
\tag{2}
\]
The connected two-spin covariance in this formula is also obtainable from the published connected-correlation formula for the underlying fixed-rate global-reset protocol. No novelty is claimed for that earlier fixed-rate covariance.

**2. Critical limiting distribution.** Take one \(E\sim\operatorname{Exp}(1)\) and couple all ages by \(A_N=E/\gamma_N\). Put
\[
p_N(u)=\frac{\Omega^2}{\omega^2}
\sin^2\!\left(\frac{\omega u}{\gamma_N}\right).
\]
For fixed \(u\ge0\) and \(c_N\to c\in(0,\infty)\),
\[
Np_N(u)\to\frac{u^2}{c^2},\qquad p_N(u)\to0.
\]
Hence \([1-(1-s)p_N(u)]^N\to\exp(-(1-s)u^2/c^2)\). The integrand after the change of variables \(u=\gamma_Nt\) in (1) is bounded by \(e^{-u}\) for \(0\le s\le1\); dominated convergence proves the asserted probability-generating function limit and therefore convergence in law to the displayed mixed Poisson variable. In fact, the conditional factorial moments satisfy
\[
\mathbb E[(K_N)_k]=(N)_k\,\mathbb E[p_N(E)^k]
\longrightarrow\frac{\mathbb E[E^{2k}]}{c^{2k}}=\frac{(2k)!}{c^{2k}}.
\]
Here domination follows from \(Np_N(E)\le E^2/c_N^2\), and \(c_N\) stays bounded away from zero. The first two moments give the mean, variance and Fano formula above. The critical law is independent of \(\Delta\), because \(p(t)=\Omega^2t^2+O(t^4)\) at the short times selected by rapid resetting.

**3. Regimes on either side.** For \(c_N\to\infty\), (2) and the bound \(\mathbb E K_N\le2/c_N^2\) give \(K_N\to0\) by Markov's inequality. If \(\gamma_N\to\infty\) and \(c_N\to0\), on the preceding coupling
\[
\mathbb E[c_N^2K_N\mid E]=c_N^2Np_N(E)
=\frac{\gamma_N^2}{\Omega^2}p_N(E)\longrightarrow E^2.
\]
Since \(0\le c_N^2Np_N(E)\le E^2\), dominated convergence applies in \(L^2\). Moreover,
\[
\mathbb E\!\left[\operatorname{Var}(c_N^2K_N\mid E)\right]
\le c_N^4N\mu_N\le2c_N^2\longrightarrow0.
\]
Thus \(c_N^2K_N\to E^2\) in \(L^2\) under this explicit coupling, proving the stronger subcritical statement.

**4. Independently reset clocks.** With independent rate-\(\gamma_N\) Poisson clocks, the stationary readout variables for distinct spins are independent Bernoulli variables, each of parameter \(\mu_N\). The count is exactly \(\operatorname{Bin}(N,\mu_N)\). In the critical regime \(N\mu_N\to2/c^2\), so the standard binomial-to-Poisson limit gives \(\operatorname{Poisson}(2/c^2)\). The global count has the same mean, but the additional covariance term in (2) satisfies \(N(N-1)C_N\to20/c^4\). Also
\(\Pr(Z_c=0)=\mathbb E[e^{-E^2/c^2}]\), which evaluates to the stated complementary-error-function formula. Its strict inequality over \(e^{-2/c^2}\) follows from Jensen's inequality, because \(E^2\) is nonconstant and \(\mathbb E E^2=2\).

**5. Exact logarithmic upper-tail rate.** For every fixed \(0<\varepsilon<1\), split the mixture at the exponential clock values \(c\sqrt{(1-\varepsilon)k}\) and \(c\sqrt{(1+\varepsilon)k}\). The Poisson Chernoff bounds show that the probability of exceeding \(k\) is exponentially small in \(k\) when the conditional Poisson mean is at most \((1-\varepsilon)k\), and approaches one exponentially fast in \(k\) when that mean is at least \((1+\varepsilon)k\). Since \(\Pr(E\ge u)=e^{-u}\), these comparisons sandwich \(-\log\Pr(Z_c\ge k)/\sqrt{k}\) between \(c\sqrt{1-\varepsilon}\) and \(c\sqrt{1+\varepsilon}\) asymptotically. Letting \(\varepsilon\downarrow0\) gives the stated rate. In contrast, a fixed-mean Poisson law has a much lighter, roughly \(\exp(-k\log k)\), upper tail.

## Verification

The supplied `checker.py` evaluates (1) by independent high-precision quadrature, checks the exact one- and two-spin moment identities against independent quadrature, compares critical probability-generating functions with the evaluated complementary-error-function expression, verifies limiting factorial moments, tests variance decomposition and the three scaling regimes numerically. It passed 132 deterministic assertions using `mpmath` 1.3.0. The accompanying `CHECK_RESULTS.json` records the execution result. Analytic limit and upper-tail proofs are in this document; finite numerical tests are not substituted for them.

## Relationship to prior work

Magoni, Carollo, Perfetto and Lesanovsky (arXiv:2202.12655, first submitted 2022-02-25) introduced precisely the noninteracting Rabi-spin Protocol I of unconditional global Poisson resetting, its reset-age renewal state, excitation-density mean and distance-independent two-spin connected correlation. Their supplement also gives the conditional binomial measurement law in the setting of a majority-conditioned Protocol II. These established ingredients explain equation (1) and the fixed-rate covariances, and are not asserted to be new. The presently assessed claim concerns the **joint many-spin/rapid-reset regime**, the entire mixed-Poisson limit, its sharp \(\sqrt N\) threshold, its stretched-exponential count tail, and the contrasting independent-clock Poisson limit; these statements were not found in the examined source.

Perfetto, Carollo, Magoni and Lesanovsky (arXiv:2106.13761) developed a general reset-renewal stationary-state framework for quantum spin systems. Mukherjee, Sengupta and Majumdar (arXiv:1806.00019) described quantum resetting, including the large-rate Zeno effect at fixed system size. Rose, Touchette, Lesanovsky and Garrahan (arXiv:1806.01298) established spectral resetting principles. Carollo, Lesanovsky and Garrahan (arXiv:2310.06981) studied universal **ordering probabilities of trajectory observables**, not the simultaneous spatial spin-count law here. Generic mixed-binomial Poisson approximation provides a method after the special physical scaling is identified; that method itself is not new. A previously published equivalent specialization remains a scholarly priority risk.

## Limitations

The limit is stationary-in-time first and is not a uniform-in-time theorem. It assumes independent coherent spins, a fixed Hamiltonian as \(N\) varies, perfect complete resets, no decoherence between resets and readout in the \(\sigma^z\) basis. An externally imposed common clock is essential to the mixed-Poisson law; independent clocks produce the ordinary Poisson law. The proof does not analyze conditional-reset Protocols II/III, interacting spin chains, imperfect resets, or a physical thermodynamic cost of resetting. In particular, it does not claim that published fixed-rate two-spin covariance formulas are new.

## References

1. M. Magoni, F. Carollo, G. Perfetto, I. Lesanovsky, *Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting*, arXiv:2202.12655 (first submitted 2022-02-25), https://arxiv.org/abs/2202.12655.
2. G. Perfetto, F. Carollo, M. Magoni, I. Lesanovsky, *Designing non-equilibrium states of quantum matter through stochastic resetting*, arXiv:2106.13761 (2021), https://arxiv.org/abs/2106.13761.
3. B. Mukherjee, K. Sengupta, S. N. Majumdar, *Quantum dynamics with stochastic reset*, arXiv:1806.00019 (2018), https://arxiv.org/abs/1806.00019.
4. D. C. Rose, H. Touchette, I. Lesanovsky, J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (2018), https://arxiv.org/abs/1806.01298.
5. F. Carollo, I. Lesanovsky, J. P. Garrahan, *Universal and nonuniversal probability laws in Markovian open quantum dynamics subject to generalized reset processes*, arXiv:2310.06981 (2023), https://arxiv.org/abs/2310.06981.
