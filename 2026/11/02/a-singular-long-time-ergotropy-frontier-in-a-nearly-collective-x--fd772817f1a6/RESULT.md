# A singular long-time ergotropy frontier in a nearly collective XX battery

## Finding

For the two-qubit XX Hamiltonian and interpolation of local and collective amplitude damping specified below, initialize the battery in the Gibbs state at finite inverse temperature \(\beta\geq 0\). Put \(\varepsilon=1-\alpha\), where \(\alpha\) is the bath-collectivity parameter, and define the slow time \(u=\gamma\varepsilon t\). Set
\[
p_\beta=\frac{e^{2\beta J}}{2\cosh(2\beta J)+2\cosh(2\beta h)},\qquad \Delta=2(J-h)>0.
\]
For every compact interval \(K\subset(0,\infty)\), the global ergotropy \(\mathcal W_\varepsilon(t)\) obeys the **uniform singular limit**
\[
\lim_{\varepsilon\downarrow0}\ \sup_{u\in K}
\left|\mathcal W_\varepsilon\left(\frac{u}{\gamma\varepsilon}\right)
-\Delta[1-2p_\beta e^{-u}]_+\right|=0,
\qquad [x]_+=\max\{x,0\}.
\]
Yet the two stationary limits do not commute:
\[
\lim_{\alpha\uparrow1}\lim_{t\to\infty}\mathcal W_\alpha(t)=\Delta,
\qquad
\lim_{t\to\infty}\mathcal W_1(t)=\Delta[1-2p_\beta]_+<\Delta.
\]
The final strict inequality holds for every finite \(\beta\geq0\). The second expression is the **previously known collective-bath plateau**, not a newly discovered critical-temperature equation.

The uniquely defined \(\beta_c>0\) satisfies \(\sinh(2\beta_c J)=\cosh(2\beta_c h)\). When \(\beta>\beta_c\), the limiting work stays zero on \(0<u\leq u_c\), where \(u_c=\log(2p_\beta)\), and becomes strictly positive for \(u>u_c\), with
\[
\Delta[1-2p_\beta e^{-u}]_+=\Delta(u-u_c)+O((u-u_c)^2)
\quad (u\downarrow u_c,\ u>u_c).
\]
For any target work \(w\in(0,\Delta)\) in that cold regime, its sharp slow-time frontier is
\[
u_w=\log\!\left(\frac{2p_\beta}{1-w/\Delta}\right):\quad
\lim_{\varepsilon\downarrow0}\mathcal W_\varepsilon\left(\frac{u}{\gamma\varepsilon}\right)
\begin{cases}<w,&0<u<u_w,\\=w,&u=u_w,\\>w,&u>u_w.
\end{cases}
\]
These are limiting positive-work and target-work frontiers, **not** assertions of exact zero work at finite noncollectivity. The fast residual levels can retain exponentially small, strictly positive work before the slow transition.

## Assumptions and scope

Fix \(J>h>0\), \(\gamma>0\), \(0\leq\alpha\leq1\), finite \(\beta\geq0\), and units \(\hbar=1\). With Pauli operators and \(\sigma^-=(\sigma^x-i\sigma^y)/2\), let
\[
H=J(\sigma_1^x\sigma_2^x+\sigma_1^y\sigma_2^y)+h(\sigma_1^z+\sigma_2^z),
\qquad \rho(0)=\frac{e^{-\beta H}}{\operatorname{tr}(e^{-\beta H})}.
\]
The subsequent evolution is the prescribed completely positive Markovian master equation
\[
\frac{d\rho}{dt}=-i[H,\rho]+\gamma\sum_{i,j=1}^2
\big[(1-\alpha)\delta_{ij}+\alpha\big]
\left(\sigma_i^-\rho\sigma_j^+-\tfrac12\{\sigma_j^+\sigma_i^-,\rho\}\right).
\]
The work functional is full-system ergotropy, \(\mathcal W(\rho)=\operatorname{tr}(H\rho)-\min_U\operatorname{tr}(HU\rho U^\dagger)\), over **all** two-qubit unitaries. This is not local ergotropy, net cycle efficiency or an assertion about a microscopically derived bath outside this generator's validity regime.

## Proof

**1. Exact invariant population sector.** Write \(|e\rangle=|ee\rangle\), \(|g\rangle=|gg\rangle\), and \(|s/a\rangle=(|eg\rangle\pm|ge\rangle)/\sqrt2\). Their distinct Hamiltonian energies, increasingly ordered under \(J>h>0\), are
\[
E_a=-2J<E_g=-2h<E_e=2h<E_s=2J.
\]
The Gibbs state is diagonal in this basis, with initial populations \(a_0=p_\beta\), \(g_0=e^{2\beta h}/Z\), \(e_0=e^{-2\beta h}/Z\), \(s_0=e^{-2\beta J}/Z\), where \(Z=2\cosh(2\beta J)+2\cosh(2\beta h)\). Diagonalizing the positive Kossakowski matrix gives jump operators \(L_\pm=\sqrt{\gamma(1\pm\alpha)/2}(\sigma_1^-\pm\sigma_2^-)\). They map \(|e\rangle\to|s\rangle\to|g\rangle\) with rate \(q_s=\gamma(1+\alpha)\) and \(|e\rangle\to|a\rangle\to|g\rangle\) with rate \(q_a=\gamma(1-\alpha)\). The diagonal sector remains invariant because \(H\), \(L_\pm^\dagger L_\pm\), and the jump images of diagonal states are diagonal in this basis.

**2. Exact time-dependent populations.** They satisfy
\[
\dot e=-2\gamma e,\quad \dot s=q_s(e-s),\quad
\dot a=q_a(e-a),\quad \dot g=q_s s+q_a a,
\]
with the conservation equation \(g=1-a-s-e\). If \(\alpha<1\), direct integration yields
\[
\begin{aligned}
e(t)&=e_0e^{-2\gamma t},\\
a(t)&=e^{-q_a t}\!\left[a_0+\frac{q_a}{q_s}e_0(1-e^{-q_s t})\right],\\
s(t)&=e^{-q_s t}\!\left[s_0+\frac{q_s}{q_a}e_0(1-e^{-q_a t})\right].
\end{aligned}
\]
For \(\alpha=1\), the continuous expressions are \(a(t)=a_0\), \(e(t)=e_0e^{-2\gamma t}\), \(s(t)=e^{-2\gamma t}(s_0+2\gamma e_0t)\). In particular, for each fixed \(\alpha<1\) all three excited populations decay to zero and \(\rho(t)\to|g\rangle\langle g|\), whereas for \(\alpha=1\) the limit is \(a_0|a\rangle\langle a|+(1-a_0)|g\rangle\langle g|\).

**3. Exact stationary work and noncommutation.** For \(|g\rangle\langle g|\), moving its unit population to the lowest-energy state \(|a\rangle\) extracts \(E_g-E_a=\Delta\). For a two-level mixture on \(|a\rangle,|g\rangle\) with \(|a\rangle\)-weight \(p\), passive rearrangement gives exactly \(\Delta[1-2p]_+\). The stationary formulas in the finding follow. Since \(p_\beta>0\) for every finite \(\beta\), their difference is strictly positive.

**4. Uniform slow-time limit.** Take \(\varepsilon=1-\alpha\downarrow0\), \(t=u/(\gamma\varepsilon)\). Then \(q_a t=u\), \(q_st=(2-\varepsilon)u/\varepsilon\), and the displayed exact formulas show, uniformly on \(u\in[\delta,M]\), with \(0<\delta<M<\infty\),
\[
a(t)=p_\beta e^{-u}+O(\varepsilon),\quad
s(t)=O\!\left(\varepsilon^{-1}e^{-(2-\varepsilon)\delta/\varepsilon}\right),\quad
e(t)=O(e^{-2\delta/\varepsilon}).
\]
Let \(\widetilde\rho=a(t)|a\rangle\langle a|+(1-a(t))|g\rangle\langle g|\). Since \(\|\rho(t)-\widetilde\rho\|_1=2[s(t)+e(t)]\) and \(\|H\|_\infty=2J\), the variational definition of ergotropy gives
\[
|\mathcal W(\rho)-\mathcal W(\widetilde\rho)|\le 2\|H\|_\infty\|\rho-\widetilde\rho\|_1
=8J(s+e).
\]
The map \(p\mapsto\Delta[1-2p]_+\) is Lipschitz. Combining these bounds proves the stated uniform slow-time limit. The same exact formulas establish the intermediate plateau when \(\gamma t\to\infty\) but \(\varepsilon\gamma t\to0\), and the noncollective final plateau when \(\varepsilon\gamma t\to\infty\) with \(\varepsilon\downarrow0\).

**5. Thresholds.** \(p_\beta\) is strictly increasing in \(\beta\) because \(E_a\) is the unique lowest energy and \(d p_\beta/d\beta=p_\beta(\langle H\rangle_\beta-E_a)>0\). Its limits at zero and infinite inverse temperature are \(1/4\) and \(1\). The equation \(p_{\beta_c}=1/2\) is equivalent to \(\sinh(2\beta_cJ)=\cosh(2\beta_ch)\) and admits exactly one positive root. For \(\beta>\beta_c\), solving \(2p_\beta e^{-u}=1\) gives \(u_c\), while solving \(\Delta[1-2p_\beta e^{-u}]=w\) gives \(u_w\). Strict monotonicity in \(u\) above the positive-work onset proves the frontier and the first-order expansion.

## Verification

The standalone `CHECK.py` constructs the complete \(4\times4\) Hamiltonian and the \(16\times16\) Lindblad superoperator independently of the four-population closed-form expressions. It compares evolved density matrices, trace and positivity, exact populations, global ergotropy, and the slow-time asymptotic profile on deterministic test cases. Run `python CHECK.py` with NumPy and SciPy installed. In the checked environment it reports `PASS: 580 density-matrix and slow-limit checks`.

As an illustration, at \(J=1\), \(h=0.1\), \(\beta=2\), \(p_\beta\approx0.9615971513\) and \(u_c\approx0.6539875029\). The limiting ergotropy is zero at \(u=0.4\), but approximately \(0.2445355731\) at \(u=0.8\). All numerical tests and examples are subordinate to the exact spectral and population proof; finite testing is not an infinite certificate.

## Relationship to prior work

Grazi, Farina, Traverso Ziani and Ferraro, *Charging Quantum Batteries via Dissipative Quenches* (arXiv:2604.08151v1, 2026), provide the XX Gibbs-state dissipator and the collective-bath critical-temperature equation, and examine finite-time interpolation plots (their Secs. II–III and Appendix B). Those inputs and the critical-temperature equation are acknowledged; the result here derives the **noncommuting limits, exact slow-time ergotropy profile, and target-work observation frontier** for weakly noncollective dynamics. Reitz, Mineo and Genes (2018) explain the familiar symmetric/antisymmetric subradiant decay rates in a different emitter setting; the single-mode decay mechanism is not new. Khoudiri, Ullah, El Allati and Müstecaplıoğlu (arXiv:2608.09693v1, 2026) analyze dark and frozen states of a transverse-field Ising battery with local or collective dissipation, rather than the weakly interpolated XX Gibbs dynamics and its quantified slow-work frontier. Known general open-system metastability could provide a broader framework, but no checked cited result supplied this exact work profile or target criterion.

## Limitations

The theorem concerns the stated Lindblad generator and full-system unitary ergotropy, not universal physical realizability of local baths at arbitrary coupling strength. It does not extend to unequal qubits, arbitrary initial coherent states, larger XX chains, or baths with excitation. The singular limit is uniform only for slow times bounded away from zero; at finite \(\varepsilon>0\), small fast-sector populations can produce nonzero work even on an apparently passive plateau. The master-equation and dark-state mechanisms are established prior results, and a more general unpublished or unlocated theorem might encompass the calculation. Independent mathematical verification and publication-priority assessment have not been carried out.

## References

- R. Grazi, D. Farina, N. Traverso Ziani and D. Ferraro, *Charging Quantum Batteries via Dissipative Quenches*, arXiv:2604.08151v1, first public April 9, 2026. https://arxiv.org/html/2604.08151
- A. Khoudiri, A. Ullah, A. El Allati and O. E. Müstecaplıoğlu, *Collective-dissipation-induced dark and metastable-like states for enhanced quantum battery performance*, arXiv:2608.09693v1, August 10, 2026. https://arxiv.org/abs/2608.09693
- M. Reitz, F. Mineo and C. Genes, *Energy transfer and correlations in cavity-embedded donor-acceptor configurations*, Scientific Reports **8**, 9050 (2018), https://pmc.ncbi.nlm.nih.gov/articles/PMC5998034/
