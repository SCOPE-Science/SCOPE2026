# A sharp eigenmode-selection transition in critical Hatano–Nelson quantum sensing

## Finding
For a non-Hermitian open Hatano–Nelson chain, optimizing the quantum Fisher information (QFI) for the hopping-asymmetry parameter over **all right eigenstates** exhibits a sharp critical-window switch. In the scaling \(\theta_N=\exp(u/(N+1))\), \(u\in\mathbb R\) fixed, the limiting optimal QFI coefficient is
\[
\mathcal M(u):=\lim_{N\to\infty}\frac{1}{(N+1)^2}\max_{1\le m\le N}F_{N,m}(\theta_N)
=\mathcal V(u)+\frac{2(u^2-4\pi^2)_+}{(u^2+4\pi^2)^2},
\quad\mathcal V(u)=\frac1{u^2}-\frac1{4\sinh^2(u/2)},\quad\mathcal V(0)=\frac1{12}.
\]
Here \((t)_+=\max(t,0)\) and the expression is continuous at zero. For \(|u|<2\pi\), any maximizing mode must recede from both mode-spectrum endpoints. For \(|u|>2\pi\), the only maximizing modes for all sufficiently large sizes are \(m=1\) and \(m=N\). At equality the limiting coefficients coincide but no finite-size uniqueness or location is asserted. For \(|u|>2\pi\), the endpoint-mode asymptotic coefficient exceeds the delocalized-mode coefficient by the explicitly positive correction in the display.

## Assumptions and scope
Fix \(N\ge2\). Take positive nearest-neighbor hopping strengths \(J_L,J_R>0\) on an open chain and set \(\theta=J_R/J_L>0\). Up to an irrelevant eigenvector scalar, the normalized right eigenstate for mode \(m\in\{1,\ldots,N\}\) is
\[
|\psi_{N,m}(\theta)\rangle=\frac{1}{\sqrt{Z_{N,m}(\theta)}}\sum_{j=1}^N\theta^{j/2}\sin\!\left(\frac{\pi m j}{N+1}\right)|j\rangle,
\quad Z_{N,m}(\theta)=\sum_{j=1}^N\theta^j\sin^2\!\left(\frac{\pi m j}{N+1}\right).
\]
For definiteness, the non-Hermitian hopping operator is \(H=\sum_{j=1}^{N-1}(J_L|j\rangle\langle j+1|+J_R|j+1\rangle\langle j|)\). A fixed position-dependent phase convention for the backward hopping leads to the same position probabilities and QFI. All states are normalized in the standard Hilbert-space norm. The model estimates the positive real parameter \(\theta\); eigenstate preparation cost, non-Hermitian postselection success probabilities, and the information in those probabilities are **not** included in \(F_{N,m}\). The quantum Fisher information is \(F_{N,m}(\theta)=4(\langle\partial_\theta\psi|\partial_\theta\psi\rangle-|\langle\psi|\partial_\theta\psi\rangle|^2)\). The maximization is over these \(N\) *individual right eigenstates*, not over arbitrary superpositions or experiment-wide protocols. We consider \(N\to\infty\) with \(u\in\mathbb R\) held fixed, followed by no further joint limits.

## Proof
**Step 1: exact QFI as position variance.** Put \(p_j(\theta)=\theta^j\sin^2(\pi m j/(N+1))/Z_{N,m}(\theta)\). Differentiating normalized real amplitudes gives
\[
\partial_\theta\langle j|\psi\rangle=\frac{j-\mathbb E_p j}{2\theta}\langle j|\psi\rangle,
\qquad F_{N,m}(\theta)=\frac{\operatorname{Var}_p(j)}{\theta^2}.
\]
The position-basis classical score is \(\partial_\theta\log p_j=(j-\mathbb E_p j)/\theta\), so position measurement attains the same Fisher information, even when a sine coefficient vanishes (the zero-probability term contributes zero).

**Step 2: all mode-index regimes.** Write \(n=N+1\), \(y_j=j/n\), \(r_N=\min(m_N,n-m_N)\), and \(\theta_N=e^{u/n}\). Then
\[
\frac{F_{N,m_N}(\theta_N)}{n^2}=e^{-2u/n}\operatorname{Var}_{p_{N,m_N,u}}(y_j),\quad p_{N,m,u}(j)\propto e^{uy_j}\sin^2(\pi m y_j).
\]
For a fixed positive integer \(m\), ordinary Riemann convergence of the first three weighted moments shows that the limiting law on \([0,1]\) has density proportional to \(e^{uy}\sin^2(\pi m y)\). For \(r_N\to\infty\), use \(\sin^2(\pi m y_j)=(1-\cos(2\pi m j/n))/2\). For each of the three smooth functions \(f(y)=y^q e^{uy}\), \(q=0,1,2\), the geometric-sum and summation-by-parts bound is
\[
\left|\frac1n\sum_{j=1}^{n-1}f(j/n)e^{2\pi i m_Nj/n}\right|\le\frac{C_{f}}{n|1-e^{2\pi i m_N/n}|}\le\frac{C'_{f}}{r_N}.
\]
(The constants depend only on \(f\), not on the mode or size.) Thus all normalized moments converge to those of the tilted-uniform density proportional to \(e^{uy}\). Since the denominator stays bounded away from zero, the variances converge as well. The symmetry \(\sin^2(\pi(n-m)j/n)=\sin^2(\pi mj/n)\) covers indices tending to the opposite edge.

**Step 3: the two exact limiting variance families.** For a fixed mode \(m\), let \(a_m=2\pi m\). The relevant partition integrals are
\[
I_m(u)=\int_0^1e^{uy}\sin^2(\pi my)\,dy
=\frac{e^u-1}{2u}\frac{a_m^2}{u^2+a_m^2},
\quad I_\infty(u)=\int_0^1e^{uy}\,dy=\frac{e^u-1}{u}.
\]
All expressions are continued at \(u=0\). Differentiating the logarithms twice (equivalently using the first two moments) yields the limiting QFI coefficients
\[
V_m(u)=\partial_u^2\log I_m(u)
=\mathcal V(u)+\frac{2(u^2-a_m^2)}{(u^2+a_m^2)^2},
\quad V_\infty(u)=\partial_u^2\log I_\infty(u)=\mathcal V(u).
\]
The factor \(1/2\) in the sinusoidal partition function is independent of \(u\) and does not alter the variance.

**Step 4: optimize, including mode sequences that vary with size.** Write \(g_m(u)=V_m(u)-\mathcal V(u)\). If \(|u|\le a_1=2\pi\), every \(g_m(u)\le0\); modes diverging from both spectral endpoints attain \(\mathcal V(u)\). If \(|u|>a_1\), then \(g_1(u)>0\). For any \(m\ge2\), either \(a_m\ge|u|\), making \(g_m(u)\le0\), or \(a_m<|u|\); in the latter case the function \(t\mapsto2(u^2-t)/(u^2+t)^2\) has derivative \(2(t-3u^2)/(u^2+t)^3<0\) on \(0<t<u^2\), so \(g_m(u)<g_1(u)\). For any sequence of potentially maximizing modes, pass to a subsequence on which \(r_N\) is constant or tends to infinity. Steps 2–3 then show that no other limiting coefficient can exceed \(\max\{V_1,\mathcal V\}\); fixed \(m=1\) and diverging \(r_N\) supply the matching lower bounds. For \(|u|<2\pi\), a bounded maximizing \(r_N\) would have a strictly inferior limit, which is impossible. For \(|u|>2\pi\), if infinitely many exact maximizers had \(r_N\ne1\), a fixed-or-diverging subsequence would again contradict the positive strict gap; hence eventually only \(m=1\) and \(m=N\) maximize. These two have exactly equal finite-size position distributions. At equality \(|u|=2\pi\), \(V_1=\mathcal V\) but finite-size maximizing indices are not classified.

## Verification
The companion standalone program `verify.py` independently evaluates the finite Hamiltonian right-eigenvector residuals, position probabilities and their score variance, compares with the normalized pure-state formula, checks the endpoint-reflection identity, tests fixed and diverging modes against the integral limits, numerically differentiates the closed-form partition function, and tests full-spectrum maximization on finite chains. Its deterministic run produces `VERIFY_OK 2716 finite scores/integral/argmax comparisons`. These finite tests are diagnostics; the all-size and subsequence statements rely on the proof above. Reproduce using `python3 verify.py` with Python's standard library; no external dependencies are required. Intermediate-size convergence near the transition is nonuniform as \(u\to\pm2\pi\) on a size-dependent scale, which this theorem does not resolve.

## Relationship to prior work
Sarkar, Ciccarello, Carollo, and Bayat (2024; first preprint 2023), in *Critical non-Hermitian topology induced quantum sensing*, give the Hatano–Nelson right eigenstates and mode-dependent QFI construction (Appendix C, equations (C.6)–(C.13)), establishing quadratic critical scaling. Their stated result does not optimize that coefficient across every mode and every fixed critical-window bias. Liu, Shi, Wu, and Yu (2026; preprint originally posted 2025) establish an optimal fixed-basis measurement principle and apply it to these Hatano–Nelson eigenstates; they do not state the mode-selection threshold. Wiersig and Rotter (2026) analyze a distinct scattering-matrix QFI for non-Hermitian resonators, not this all-eigenmode open-chain positional QFI. The present claim is the complete critical-window coefficient and sharp transition between diverging modes and the spectral-edge mode, **not** the previously published eigenstate formula, position-basis measurement optimality, or the \(N^2\) scaling alone.

## Limitations
The QFI omits right-eigenstate preparation and postselection costs; the mathematical optimizer need not be the easiest mode to prepare. Only positive real hopping ratios, standard-normalized right eigenstates, a finite open chain, and a fixed-bias critical scaling \(\theta_N=e^{u/(N+1)}\) are treated. No finite-size optimizer location is asserted at \(|u|=2\pi\), and there is no claim about superpositions, noisy probes, adaptive sensing, or quantum-channel capacity. Independent publication-priority verification has not been performed; a relevant prior paper's appendix derives a general mode-dependent expression from which this result can be computed but does not state the optimized threshold. Unindexed earlier derivations remain possible.

## References
1. J.-X. Liu, H.-L. Shi, C. Wu, and S. Yu, *Quantum Estimation with State Symmetry-Induced Optimal Measurements*, Nature Communications **17**, 7898 (2026), doi:10.1038/s41467-026-73507-0; arXiv:2508.07150, first submitted 2025-08-10, revised 2026-03-09. The main manuscript, including equation (6), was examined.
2. S. Sarkar, F. Ciccarello, A. Carollo, and A. Bayat, *Critical non-Hermitian topology induced quantum sensing*, New Journal of Physics **26**, 073010 (2024), preprint arXiv:2311.12756. The full accessible manuscript, especially Appendix C, was examined: https://inspirehep.net/files/c391930897e4d6b303670fe2e513209e.
3. J. Wiersig and S. Rotter, *Fundamental Limits of Non-Hermitian Sensing from Quantum Fisher Information*, Reports on Progress in Physics **89**, 067501 (2026), arXiv:2603.10614; comparison used the published abstract and paper description of the scattering formulation.
