# Sharp quenched–annealed cutoff for finite Bernoulli Griffiths survival

## Finding

A finite random one-dimensional landscape has a sharp long-time boundary between representative and rare-sample-dominated disorder averages in the *exactly defined rare-region survival surrogate* below. The crossover is absent from the infinite-volume disorder-averaged saddle-point law. It is not asserted as an exact theorem for an underlying Lindblad evolution.

**Theorem.** Fix a loss-site probability \(p\in(0,1)\), a regional decay exponent \(\beta>0\), and a decay coefficient \(\rho>0\). Independently designate each of \(L\ge2\) sites lossy with probability \(p\). Write \(\mathcal R_L\) for the multiset of lengths \(\ell\ge1\) of maximal consecutive loss-free intervals, including intervals meeting either endpoint. Define the sample-wise coarse-grained survival observable for \(t\ge0\) by

\[
S_L(t)=\frac{1}{L}\sum_{\ell\in\mathcal R_L}\ell\exp\!\left(-\frac{\rho t}{\ell^\beta}\right).
\]

Let \(a=-\log(1-p)>0\), \(\xi=1/a\), and for any fixed \(u>0\) put

\[
t_L(u)=\frac{u(\log L)^{\beta+1}}{\rho},\qquad
F_{\mathrm{ann}}(u)=\inf_{y>0}\left(ay+\frac{u}{y^\beta}\right),\qquad
F_{\mathrm{typ}}(u)=\inf_{0<y\le\xi}\left(ay+\frac{u}{y^\beta}\right).
\]

Then both limits exist, with the first convergence in probability over the Bernoulli landscape:

\[
-\frac{\log S_L(t_L(u))}{\log L}\xrightarrow[L\to\infty]{\mathbb P}F_{\mathrm{typ}}(u),\qquad
-\frac{\log\mathbb E S_L(t_L(u))}{\log L}\longrightarrow F_{\mathrm{ann}}(u).
\]

Here \(\log0=-\infty\) is permitted on the exponentially rare event of no loss-free sites. The rates have the explicit forms

\[
F_{\mathrm{ann}}(u)=(\beta+1)\left(\frac{a^\beta u}{\beta^\beta}\right)^{\!1/(\beta+1)},\qquad u_c=\frac{\xi^\beta}{\beta},
\]

\[
F_{\mathrm{typ}}(u)=
\begin{cases}
F_{\mathrm{ann}}(u),&0<u\le u_c,\\[2pt]
1+u/\xi^\beta,&u\ge u_c.
\end{cases}
\]

Consequently, for every \(u>u_c\), the disorder-averaged surrogate is polynomially larger than a typical realization, in the precise logarithmic sense

\[
\frac{\log(\mathbb E S_L(t_L(u))/S_L(t_L(u)))}{\log L}
\xrightarrow{\mathbb P}F_{\mathrm{typ}}(u)-F_{\mathrm{ann}}(u)>0.
\]

Below and at the threshold the two expressions agree *only to logarithmic order*; no self-averaging ratio is asserted. At \(u_c\) the typical exponent is continuously differentiable but its second derivative jumps from \(-\beta^2/[(\beta+1)\xi^{2\beta}]\) on the left to \(0\) on the right. Thus the sample-wise logarithmic decay rate changes from a stretched-exponential saddle to a linear longest-region regime.

For the physically motivated exponents \(\beta=3\) and \(\beta=1\), the sharp joint-scale thresholds are \(u_c=\xi^3/3\) and \(u_c=\xi\), respectively. They correspond to times of order \((\log L)^4/\rho\) and \((\log L)^2/\rho\). These are thresholds for the stipulated surrogate, not proven crossover times of the microscopic open quantum system.

## Assumptions and scope

The random loss indicators are independent Bernoulli variables at fixed \(p\), the system has open endpoints, and regional contributions are *defined*, without approximation, as length weights multiplied by \(\exp(-\rho t/\ell^\beta)\). The theorem holds for every fixed \(p\in(0,1)\), \(\rho>0\), \(\beta>0\), and fixed \(u>0\), as \(L\to\infty\); the limits are not claimed uniformly in those parameters. A landscape with every site lossy has \(S_L=0\), a probability-\(p^L\) event, which does not affect convergence in probability.

The surrogate is suggested by the Bernoulli-Griffiths lossless-region construction and the approximate region-decoupling formula of Longhi [1, 2]. In that physical approximation the initial uniform and phase-modulated Bloch states correspond to \(\beta=3\) and \(\beta=1\). Inter-region interference, nonorthogonal modes, exact finite-size Lindblad spectra, and finite-dissipation corrections are *outside* the proved domain.

## Proof

**1. Exact finite-volume mean.** Set \(q=1-p\). Let \(N_{L,m}\) count maximal loss-free runs of length \(m\). For \(1\le m\le L-1\), a run may be bounded by two lossy sites or touch one of the two open endpoints, so independent Bernoulli weights give

\[
\mathbb E N_{L,m}=p^2(L-m-1)q^m+2p q^m.
\]

The sole run of length \(L\) occurs if every site is loss-free, and \(\mathbb E N_{L,L}=q^L\). Therefore, for any \(t\ge0\),

\[
\mathbb E S_L(t)=\sum_{m=1}^{L-1}\frac{m q^m}{L}\big[p^2(L-m-1)+2p\big]e^{-\rho t/m^\beta}+q^L e^{-\rho t/L^\beta}.
\tag{1}
\]

This formula includes endpoint runs exactly and has no thermodynamic approximation.

**2. Annealed Laplace principle.** Write \(h_L=\log L\) and \(t=t_L(u)\). For \(m\sim y h_L\) with any fixed \(y>0\), a summand of (1) has logarithm

\[
-\left(ay+\frac{u}{y^\beta}\right)h_L+o(h_L).
\]

Fix \(0<\delta<K<\infty\). In the window \(\delta h_L\le m\le Kh_L\), upper and lower Riemann-window bounds yield the minimum of that continuous cost over \([\delta,K]\). The contribution from \(m<\delta h_L\) is at most \(\exp[-u h_L/\delta^\beta]\) since total initial region weight is at most one. The contribution from \(m>Kh_L\) is at most a polynomial factor times \(q^{Kh_L}\), hence has logarithmic cost at least \(aK+o(1)\). Taking \(\delta\downarrow0\) and \(K\uparrow\infty\), the positive minimizer \(y_*(u)=(\beta u/a)^{1/(\beta+1)}\) yields the announced \(F_{\mathrm{ann}}\). The term \(q^L\) in (1) is exponentially small in \(L\) and therefore irrelevant at the \(\log L\) scale.

**3. Largest-run upper tail.** Let \(M_L\) be the longest loss-free run (zero if none exists). A union bound over starting positions gives, for any integer \(m\ge1\),

\[
\Pr(M_L\ge m)\le Lq^m.
\]

Consequently, for each \(\eta>0\), with probability tending to one,

\[
M_L\le(\xi+\eta)\log L.
\tag{2}
\]

This is an upper bound on a *typical* landscape, not a bound on rare landscapes that can dominate the mean.

**4. Uniform upper bound on run counts.** For \(1\le m<L\), the mean identity implies \(\mathbb E N_{L,m}\le C Lq^m\), for a constant depending only on \(p\). Fix \(\eta,\varepsilon>0\). Apply Markov's inequality and a union bound over \(m\le(\xi+\eta)\log L\). Except on an event of probability \(O((\log L)L^{-\varepsilon})\), every such \(m\) satisfies

\[
N_{L,m}\le L^{\max\{1-am/\log L,0\}+\varepsilon}.
\tag{3}
\]

For lengths \(m\le\delta\log L\), the entire normalized weighted sum is at most \(L^{-u/\delta^\beta}\). For the remaining lengths, (2)–(3) and the fact there are only \(O(\log L)\) terms give an upper log-exponent governed by

\[
\inf_{\delta\le y\le\xi+\eta}\left[\min\{ay,1\}+\frac{u}{y^\beta}\right].
\]

First let \(\delta\downarrow0\), then \(\eta\downarrow0\), then \(\varepsilon\downarrow0\). Continuity at \(y=\xi\) shows

\[
\Pr\!\left(-\frac{\log S_L(t_L(u))}{\log L}<F_{\mathrm{typ}}(u)-\varepsilon_0\right)\longrightarrow0
\]

for each fixed \(\varepsilon_0>0\).

**5. Constructive typical lower bound.** Fix \(0<y<\xi\), choose \(m_L=\lfloor y\log L\rfloor\), and partition the sites into \(\lfloor L/(m_L+2)\rfloor\) disjoint blocks of length \(m_L+2\). The event that a block is \(1,0,\ldots,0,1\) (one lossy marker, \(m_L\) loss-free sites, one lossy marker) has probability \(p^2 q^{m_L}\), independently from block to block. Its number of occurrences has mean of order \(L^{1-ay}/\log L\). Chernoff's binomial inequality thus implies that, for any fixed \(\varepsilon>0\), with probability approaching one there are at least \(L^{1-ay-\varepsilon}\) such blocks. Each supplies a distinct maximal run and a positive survival contribution. It follows that

\[
S_L(t_L(u))\ge L^{-ay-u/y^\beta-\varepsilon+o(1)}
\]

with probability approaching one. Take \(y\) arbitrarily close to the minimizer over \(0<y\le\xi\), approaching \(\xi\) from below if required, to match step 4. This proves the stated convergence in probability.

**6. Threshold and comparison.** The unrestricted minimizer \(y_*(u)\) reaches the longest typical run scale \(\xi\) precisely at \(u_c=\xi^\beta/\beta\). Before this point the typical and annealed minima coincide. After it, the constrained minimum occurs at \(y=\xi\) while the unconstrained saddle remains at \(y_*(u)>\xi\). Strict convexity of \(ay+u/y^\beta\) gives \(F_{\mathrm{typ}}(u)>F_{\mathrm{ann}}(u)\). Elementary differentiation gives the stated \(C^1\) matching and second-derivative jump. Subtracting the already proved two logarithmic limits yields the ratio law.

## Verification

The standalone standard-library program `verify.py` exhaustively enumerates all Bernoulli words for short \(L\), compares directly weighted survival with exact formula (1), checks threshold minimization and strict separation on rationally selected parameter grids, and performs reproducible seeded finite-sample sanity checks. The latter are *finite experiments* and do not establish convergence. The proof above supplies the arbitrary-length arguments.

## Relationship to prior work

Longhi's 2026 photonic rare-loss study [1] and the later quantum Mpemba study [2] derive the model's lossless-region phenomenology and its two inverse-power linewidth exponents. In particular [2, Appendix C, equations (C6)–(C18)] provides the disorder-averaged region sum, continuum saddle and stretched-exponential decay. The exact finite-volume definition here is deliberately restricted to that *coarse-grained surrogate*, with no assertion that this sum equals the microscopic quantum survival probability. The unrestricted saddle law \(F_{\mathrm{ann}}\), including its optimization, is **prior input** rather than the novel component.

The contribution is the *quenched* joint system-size/time limit with a constrained saddle, its precise break at \(u_c\), and the strict polynomial-scale separation of a typical finite landscape from its disorder mean beyond that threshold. The distinction depends on actual random run counts rather than substituting an average count into a finite-size truncated sum. Related Griffiths reviews [3] describe rare-region anomalies and typical-versus-average phenomena generally, but do not supply this model-specific joint-scaling theorem. Classical extreme-run bounds and the saddle-point method are known tools and are not claimed to be novel in isolation.

## Limitations

This is a theorem about the *mathematically exact* finite Bernoulli rare-region surrogate, not about the full coherent lattice, quantum density matrix, trace distance, or a measured Mpemba crossing time. In the original physical model, the factorized region contributions are approximate and calibrated phenomenologically. The joint time scale grows with \(L\), so error control for the physical coarse-graining at that growing time has not been established. The results concern logarithmic decay exponents in probability and in expectation; they do not assert convergence of survival ratios, a limiting fluctuation distribution at the critical point, or universality under correlated site losses. Typical finite-size simulations converge slowly because the governing scale is \(\log L\). The Bernoulli assumption and open boundaries are essential to the current proof.

## References

[1] S. Longhi, “Griffiths Anomalous Absorption in Sparse-Loss Photonic Lattices,” arXiv:2607.03205 (initial public posting 2026-07-03); *Optics Letters* **51**, 4068–4071 (2026), DOI: 10.1364/OL.604778. Original sparse-loss rare-region phenomenology and annealed decay.

[2] S. Longhi, “Statistical Quantum Mpemba Effect From Griffiths Rare Regions,” *Advanced Quantum Technologies* **9**, e70425 (first published 2026-08-30), DOI: 10.1002/qute.70425. Full open article, Sections 2–4 and Appendices B–C, especially equations (C6)–(C18).

[3] K. Agarwal et al., “Rare-Region Effects and Dynamics near the Many-Body Localization Transition,” *Annalen der Physik* **529**, 1600326 (2017), DOI: 10.1002/andp.201600326. Related general Griffiths context, not a claim of direct coverage.
