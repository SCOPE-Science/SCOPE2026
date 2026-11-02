# Graph-gap preparation and quadratic disorder fidelity for bond-dissipative quantum batteries

## Finding

For a connected finite quantum tight-binding network with phase-consistent rank-one bond jumps, the fidelity with its phase-compatible dark mode obeys an explicit two-sided stationary **quadratic** stability law under arbitrary onsite disorder. The upper and lower bounds have computable constants involving the graph Laplacian gap and the Hamiltonian norm; they apply to *every* stationary density matrix, without any assumption of uniqueness. When onsite potentials exactly compensate weighted vertex degrees, this same target is the uniquely attracting, maximally charged state, and the graph-gap coefficient is optimal for a uniform differential fidelity estimate.

Let \(G=(V,E)\) be a connected simple graph, \(n=|V|\ge2\), with an arbitrary orientation of its \(m=|E|\) edges. Fix edge phases \(\eta_{ij}\in\mathbb C\) with \(|\eta_{ij}|=1\). In the single-particle space \(\mathbb C^n\), for each oriented edge \(i\to j\) set
\[
|w_{ij}\rangle=|i\rangle-\eta_{ij}|j\rangle,\quad
|v_{ij}\rangle=|i\rangle+\eta_{ij}|j\rangle,\quad
L_{ij}=|v_{ij}\rangle\langle w_{ij}|.
\]
These jumps are nilpotent, and their unit-modulus phases incorporate the complex-conjugate convention required for a legitimate coherence-pumping bond mode.

Take \(\gamma>0\), strictly positive hoppings \(t_{ij}>0\), real onsite potentials \(a_i\), and the phase-matched Hamiltonian
\[
H=\sum_{i\to j\in E}t_{ij}\bigl(\eta_{ij}|j\rangle\langle i|+\overline{\eta}_{ij}|i\rangle\langle j|\bigr)
+\sum_i a_i|i\rangle\langle i|.
\]
The master equation is \(\dot\rho=-i[H,\rho]+\gamma\sum_{e\in E}\mathcal D[L_e](\rho)\), where \(\mathcal D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2\).

The phases are **compatible** when their oriented product around every cycle is one. Equivalently, there exist \(s_i\in\mathbb C\), \(|s_i|=1\), such that \(s_j=\eta_{ij}s_i\) on each oriented edge. In this case define the normalized dark vector \(u_i=s_i/\sqrt n\), projector \(P=|u\rangle\langle u|\), unweighted covariant Laplacian \(\Lambda=\sum_e|w_e\rangle\langle w_e|\), and its positive second eigenvalue \(\lambda_2\). Write \(d_i=\sum_{j:\{i,j\}\in E}t_{ij}\), \(b_i=a_i+d_i\), and
\[
\delta^2=\|(I-P)Hu\|^2
=\frac1n\sum_i(b_i-\overline b)^2,
\qquad
\overline b=\frac1n\sum_i b_i.
\]
Put \(c=4\gamma\lambda_2/n\) and \(M=2\|H\|_{\mathrm{op}}+8\gamma m\). **For every stationary state** \(\rho_*\) and \(q=1-\operatorname{tr}(P\rho_*)\),
\[
\boxed{\qquad\frac{\delta^2}{M^2}\le q\le
\frac{4\delta^2}{c^2+4\delta^2}.\qquad}
\]
The upper bound is interpreted as zero if \(\delta=0\). Thus \(\rho_*=P\) exactly when the compensated row sums \(b_i\) are constant. For onsite perturbations \(a_i=C-d_i+\varepsilon V_i\) with nonconstant real \(V\), these explicit bounds show \(q=\Theta(\varepsilon^2)\) uniformly over all stationary states as \(\varepsilon\to0\) for fixed graph and fixed \(\gamma>0\).

When \(\delta=0\), all initial density matrices satisfy
\[
1-\operatorname{tr}(P\rho(t))\le
\exp(-ct)\bigl[1-\operatorname{tr}(P\rho(0))\bigr],
\]
so \(\|\rho(t)-P\|_1\le2e^{-ct/2}\sqrt{1-\operatorname{tr}(P\rho(0))}\). The coefficient \(c\) is the **largest possible universal coefficient in the differential inequality** \(p'(t)\ge c(1-p(t))\), in the sense that equality holds at time zero for an initial pure state in a \(\lambda_2\)-eigenspace.

More generally, a pure stationary state exists **if and only if** the phases are cycle-compatible and the \(b_i\) are constant. This specialization of general dark-state criteria distinguishes the exact-design regime from unavoidable mixed-state charging. In the exact-design regime the top eigenvalue of \(H\) is \(C=b_i\), is simple, and the stationary ergotropy is exactly the spectral diameter \(\lambda_{\max}(\sum_e t_e|w_e\rangle\langle w_e|)\). If either compatibility or degree compensation fails, all stationary states are mixed and their ergotropy is strictly below the Hamiltonian spectral diameter.

## Assumptions and scope

The assertions are finite-dimensional, in the **single-particle sector** and with no particle interactions, one positive Lindblad rate \(\gamma\) per edge, unit-modulus bond phases, a connected graph and strictly positive real hopping magnitudes. The onsite perturbation is Hermitian and diagonal. Complex phases in the jump are conjugated between creation and annihilation as specified above. The preparation-fidelity statement concerns the projector \(P\), not total thermodynamic efficiency or an experimentally measured work distribution.

## Proof

**Dark-mode and spectral geometry.** For each edge, \(\langle w_e|v_e\rangle=0\), so \(L_e^2=0\), \(L_e^\dagger L_e=2|w_e\rangle\langle w_e|\). A pure stationary state of a Lindblad generator must be a simultaneous eigenstate of all its jumps (by the equality case of the dissipation-induced purity derivative). Since these jumps are nilpotent, the eigenvalues vanish. The equations \(\langle w_e|\psi\rangle=0\) enforce \(\psi_j=\eta_e\psi_i\). Connectedness forces equal moduli and, around cycles, unit holonomy. The common kernel is then exactly \(\mathbb C u\). For \(P\) to be stationary it must additionally commute with \(H\), equivalently \(Hu\) proportional to \(u\). Direct substitution gives \((Hu)_i=(a_i+d_i)u_i\); hence constant \(b_i\) is necessary and sufficient. When constant \(C\), \(H=C I-\sum_e t_e|w_e\rangle\langle w_e|\), which has simple top eigenvalue \(C\) by connectedness and positive hoppings.

**Exact fidelity identity.** Under compatible phases, \(L_eu=0\), \(\langle u|v_e\rangle=2\overline{s_i}/\sqrt n\), and the anticommutator terms vanish against \(P\). Consequently for \(p(t)=\operatorname{tr}(P\rho(t))\),
\[
p'(t)=-i\operatorname{tr}(P[H,\rho(t)])
+\frac{4\gamma}{n}\operatorname{tr}(\Lambda\rho(t)).
\]
Because \(\Lambda\ge\lambda_2(I-P)\) and \(\operatorname{ker}\Lambda=\mathbb Cu\), the dissipative term is at least \(c(1-p)\). When \(\delta=0\), the Hamiltonian term is zero. Grönwall's inequality gives exponential fidelity convergence and uniqueness. The trace-distance bound is the pure-target fidelity inequality. Taking an initial projector onto a normalized eigenvector of \(\Lambda\) of eigenvalue \(\lambda_2\) gives equality in the derivative bound at time zero, establishing optimality of the coefficient in this stated sense.

**Upper stationary defect.** Set \(h=(I-P)Hu\), so \(\|h\|=\delta\). At stationarity the Hamiltonian contribution to \(p'\) has absolute value \(2|\operatorname{Im}\langle h|\rho_*|u\rangle|\le2\delta\sqrt{pq}\), by positivity and Cauchy–Schwarz. Therefore \(cq\le2\delta\sqrt{(1-q)q}\). When \(q>0\), solving this inequality gives \(q\le4\delta^2/(c^2+4\delta^2)\); the zero case is immediate.

**Lower stationary defect.** Since the dissipator annihilates \(P\), \(\mathcal L(P)=-i[H,P]\), whose trace norm is \(2\delta\). Each jump has operator norm \(2\), and the trace-norm induced bound for its dissipator is at most \(8\). Thus \(\|\mathcal L(X)\|_1\le M\|X\|_1\). Using \(\mathcal L(\rho_*)=0\),
\[
2\delta=\|\mathcal L(P-\rho_*)\|_1
\le M\|P-\rho_*\|_1\le2M\sqrt q.
\]
This proves the lower bound. For \(a_i=C-d_i+\varepsilon V_i\), the exact identity \(\delta=|\varepsilon|\sqrt{n^{-1}\sum_i(V_i-\overline V)^2}\), together with bounded \(M\), proves matching quadratic order. A stationary state always exists by finite-dimensional compactness of the dynamical semigroup and time averaging.

**Ergotropy.** In the compensated case the globally attracting projector occupies the simple maximal-energy eigenvector of \(H\). A pure top eigenstate has ergotropy equal to \(E_{\max}-E_{\min}\). If no stationary pure state exists, equality with this diameter is impossible for a stationary density matrix (it would require a pure top-energy state). Compactness of the stationary set gives a strict gap for each fixed set of parameters, without claiming a graph-uniform numerical gap.

## Verification

The included program `verify.py` independently constructs the bond jumps, phase-compatible dark projectors, Hamiltonians, and full Lindbladians for several irregular and cyclic graphs. It checks the stationary-state residual, positivity, row-sum variance identity, both fidelity bounds, convergence of the Hamiltonian-compensated dynamics, and a frustrated cycle with no dark kernel. `requirements.txt` states the only external Python dependencies. Run `python verify.py` in a Python environment with the listed dependencies. Numerical assertions do not replace the analytic quantifiers in the theorem.

## Relationship to prior work

Xu et al., *Dissipative charging of tight-binding quantum batteries* (arXiv:2602.17326, first submitted 2026-02-19), introduce the bond jumps and numerically study the steady charging of periodic chains, graphene and disordered lattices; their Section III and Appendix A are the immediate physical starting point. Kraus et al., *Preparation of Entangled States by Quantum Markov Processes* (arXiv:0803.1463, 2008), establish general pure-stationary-state conditions; these are used rather than claimed as novel. Klausen and Warzel, *Decoherence is an Echo of Anderson Localization in Open Quantum Systems* (Annales Henri Poincaré 26, 3665–3693, 2025), explicitly identify the real-phase coherence-creating bond jumps and their graph Laplacian and discuss disorder and dark states. These earlier results already cover the bare uniform dark mode and the abstract pure-state criterion. The **evaluated addition** is the explicit graph-wide two-sided *stationary* disorder-fidelity corridor, its \(\Theta(\varepsilon^2)\) rigidity for any stationary state, and the sharp spectral coefficient of the fidelity differential inequality under degree compensation. The gauge-compatible version and compensation prescription place these quantitative statements in the battery Hamiltonian. No literature-wide priority guarantee is asserted.

## Limitations

The stationary bounds can be loose and do not give the exact coefficient of the quadratic infidelity or a graph-size-uniform perturbation theorem. The coefficient \(c\) is optimal only for the stated all-state differential inequality, not asserted equal to the Liouvillian mixing gap. Incompatible bond flux rules out pure stationary states but does not determine their mixed-state purity. The statement is not a theorem for interacting many-particle batteries, independently varying jump rates, or unconstrained phase-mismatched hopping. General dissipative preparation and perturbation theorems may have implications for this specialization; the originality review is best-knowledge rather than independent certification.

## References

1. M. Xu, Y. Liu, Y. Song, X.-P. Jiang, and L. Pan, *Dissipative charging of tight-binding quantum batteries*, arXiv:2602.17326 (first public version 2026-02-19), https://arxiv.org/html/2602.17326v2 .
2. B. Kraus, H. P. Büchler, S. Diehl, A. Kantian, A. Micheli, and P. Zoller, *Preparation of Entangled States by Quantum Markov Processes*, arXiv:0803.1463 (2008), https://arxiv.org/abs/0803.1463 .
3. F. R. Klausen and S. Warzel, *Decoherence is an Echo of Anderson Localization in Open Quantum Systems*, Annales Henri Poincaré 26 (2025), 3665–3693, https://doi.org/10.1007/s00023-024-01528-w .
4. C.-E. Bardyn et al., *Topology by dissipation*, New Journal of Physics 15 (2013), 085001, arXiv:1302.5135, https://arxiv.org/abs/1302.5135 (broader distinct dissipative-topology setting).
