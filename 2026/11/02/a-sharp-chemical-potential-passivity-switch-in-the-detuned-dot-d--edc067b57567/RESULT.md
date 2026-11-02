# A sharp chemical-potential passivity switch in the detuned-dot dephasing battery

## Finding

Consider the strongly blockaded three-dot open battery defined below. For every fixed real reservoir chemical potential \(\mu\), onsite baseline \(\varepsilon\in\mathbb R\), hopping \(\Omega>0\), electronic thermal energy \(\vartheta=k_{\mathrm B}T>0\), contact strength \(\Gamma>0\), and local dephasing strength \(\gamma>0\), let \(\rho_\Delta\) be the unique steady state of the specified four-dimensional Lindblad generator at detuning \(\Delta>0\). Let \(\mathcal E_\Delta=\operatorname{Tr}(H_\Delta\rho_\Delta)\) and \(\mathcal W_\Delta\) be the corresponding unitary ergotropy. Put

\[
 h=\frac{\Omega}{\vartheta},\qquad
 z=\exp\!\left(\frac{\mu-\varepsilon}{\vartheta}\right),\qquad
 a=ze^h,\quad b=ze^{-h},\quad Z=1+\frac32(a+b).
\]

In the ordered basis of the empty, bonding, antibonding, and detuned states, the stationary populations converge as \(\Delta\to+\infty\) to

\[
 (p_0,p_g,p_e,p_d)=\frac1Z\left(1,a,b,\frac{a+b}{2}\right).
\]

The leading stored energy and ergotropy are

\[
 \lim_{\Delta\to\infty}\frac{\mathcal E_\Delta}{\Delta}
 =\frac{a+b}{2Z},\qquad
 \lim_{\Delta\to\infty}\frac{\mathcal W_\Delta}{\Delta}
 =\frac{(a+b)/2-\min\{1,b\}}{Z}.
\]

In particular, the limiting ergotropic fraction exists and has the **complete chemical-potential classification**

\[
 \boxed{\eta_\infty(\mu)
 =\lim_{\Delta\to\infty}\frac{\mathcal W_\Delta}{\mathcal E_\Delta}
 =\begin{cases}
 \tanh h,&\mu\le\varepsilon+\Omega,\\[2pt]
 1-\displaystyle\frac{e^{-(\mu-\varepsilon)/\vartheta}}{\cosh h},&\mu\ge\varepsilon+\Omega.
 \end{cases}}
\]

At the sharp threshold \(\mu_c=\varepsilon+\Omega\), \(\eta_\infty\) is continuous but not differentiable: its left derivative is zero and its right derivative is \((1-\tanh h)/\vartheta>0\). Above the threshold the limiting fraction increases strictly with \(\mu\), tending to \(1\) as \(\mu\to+\infty\), while the limiting stored-energy coefficient tends to \(1/3\). This is a sequential limit: first \(\Delta\to\infty\) at each fixed finite \(\mu\), then \(\mu\to\infty\). It is not a thermodynamic work-conversion efficiency.

## Assumptions and scope

The Hilbert space is \(\mathbb C|0\rangle\oplus\operatorname{span}\{|1\rangle,|2\rangle,|3\rangle\}\), with at most one electron. The empty level has energy zero; the single-electron Hamiltonian in the local site basis is

\[
 H_\Delta^{(1)}=\begin{pmatrix}
 \varepsilon+\Delta&-\Omega&0\\
 -\Omega&\varepsilon&-\Omega\\
 0&-\Omega&\varepsilon
 \end{pmatrix}.
\]

Let \(|g_\Delta\rangle,|e_\Delta\rangle,|d_\Delta\rangle\) be its normalized real eigenvectors in increasing eigenenergy order, with corresponding energies \(E_g,E_e,E_d\), and put \(u_j=\langle1|j_\Delta\rangle\), \(w_j=\langle3|j_\Delta\rangle\). The full Hamiltonian \(H_\Delta\) is zero on the empty level and equals \(H_\Delta^{(1)}\) on the one-electron sector. With \(f_\mu(E)=[1+\exp((E-\mu)/\vartheta)]^{-1}\), define

\[
 L_j^+=\sqrt{\Gamma|w_j|^2 f_\mu(E_j)}\,|j_\Delta\rangle\langle0|,
 \qquad
 L_j^-=\sqrt{\Gamma|w_j|^2[1-f_\mu(E_j)]}\,|0\rangle\langle j_\Delta|,
 \qquad
 L_\gamma=\sqrt\gamma\,|1\rangle\langle1|,
\]

and the dynamical generator, in units with \(\hbar=1\),

\[
 \mathcal L_\Delta(\rho)
 =-i[H_\Delta,\rho]
 +\sum_{j\in\{g,e,d\}}\bigl(\mathcal D[L_j^+]\rho+\mathcal D[L_j^-]\rho\bigr)
 +\mathcal D[L_\gamma]\rho,
 \qquad
 \mathcal D[L]\rho=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
\]

All fixed positive parameters remain independent of \(\Delta\). The generator contains no phonon channel, second-electron state, additional quantum orbital, or time-dependent control. We define the passive-state energy by sorting density-matrix eigenvalues decreasingly against Hamiltonian eigenvalues increasingly. The ergotropy is \(\mathcal W_\Delta=\mathcal E_\Delta-\mathcal E_{\mathrm{pass},\Delta}\). No claim about finite-detuning exact kink location is made.

## Proof

**1. Energies, overlaps, and uniqueness.** Standard perturbation of the real symmetric tridiagonal Hamiltonian gives, for fixed \(\Omega\),

\[
 \begin{gathered}
 E_g=\varepsilon-\Omega+O(\Delta^{-1}),\quad
 E_e=\varepsilon+\Omega+O(\Delta^{-1}),\quad
 E_d=\varepsilon+\Delta+O(\Delta^{-1}),\\
 |u_g|^2=\frac{\Omega^2}{2\Delta^2}+O(\Delta^{-3}),\quad
 |u_e|^2=\frac{\Omega^2}{2\Delta^2}+O(\Delta^{-3}),\quad
 |u_d|^2=1+O(\Delta^{-2}),\\
 |w_g|^2=\frac12+O(\Delta^{-1}),\quad
 |w_e|^2=\frac12+O(\Delta^{-1}),\quad
 |w_d|^2=O(\Delta^{-4}).
 \end{gathered}
\]

For every finite \(\Delta\) the contact amplitudes \(w_j\) are nonzero, because the nonzero nearest-neighbor hopping connects all three sites. At positive temperature \(0<f_\mu(E_j)<1\). The six forward/backward jump operators connect the empty state to every energy eigenstate. Their invariant operator algebra is irreducible, so the finite-dimensional quantum Markov semigroup has one faithful stationary state. Gauge invariance of the generator and uniqueness eliminate empty–one-electron stationary coherences.

**2. Control of energy-basis coherences.** Set \(q=\Omega/\Delta\). In the energy basis the dephasing projector \(P=|1\rangle\langle1|\) has \(P_{dg},P_{de}=O(q)\), \(P_{ge}=O(q^2)\), and \(P_{dd}=1+O(q^2)\). The stationary off-diagonal equations have Hamiltonian frequencies \(E_d-E_{g,e}=\Delta+O(1)\) or \(E_e-E_g=2\Omega+O(\Delta^{-1})\). The low–low entry also has a strictly positive dissipative decay from the contact, bounded below for each fixed \(\mu,\vartheta,\Gamma\); the reservoir does not create energy-basis coherences. The only leading diagonal-to-off-diagonal source involving the detuned state is \(O(q)\), and the low–low source is \(O(q^2)\). Solving these three linear stationary equations, with uniformly bounded density-matrix entries and fixed parameters, yields

\[
 \rho_{dg},\rho_{de}=O(\Delta^{-2}),\qquad \rho_{ge}=O(\Delta^{-2}).
\]

Indeed, the first two frequency denominators have magnitude \(\Delta+O(1)\) and the third has a nonzero limiting denominator; the inter-coherence perturbations are at most \(O(q)\), permitting a bounded Neumann-resolvent expansion. This step is needed because the dephasing dissipator is not pre-secularized in the energy basis.

**3. Stationary population balance.** Write \(p_j(\Delta)=\langle j_\Delta|\rho_\Delta|j_\Delta\rangle\) and \(p_0(\Delta)=\langle0|\rho_\Delta|0\rangle\). The \(g\)- and \(e\)-population equations are

\[
 0=\Gamma|w_j|^2\{f_\mu(E_j)p_0(\Delta)-[1-f_\mu(E_j)]p_j(\Delta)\}+O(\Delta^{-2}),
 \quad j=g,e.
\]

Since the contact prefactor has a positive limit, their equations imply

\[
 p_g(\Delta)=a\,p_0(\Delta)+o(1),\qquad
 p_e(\Delta)=b\,p_0(\Delta)+o(1).
\]

The detuned population equation is more delicate. The direct reservoir exchange is \(O(\Delta^{-4})\). Its dephasing contribution is the exact diagonal exchange term \(\gamma\sum_{j=g,e}|P_{dj}|^2[p_j(\Delta)-p_d(\Delta)]\), plus terms containing off-diagonal density entries. By the coherence bounds and \(P_{dj}=O(\Delta^{-1})\), the latter are \(O(\Delta^{-3})\). Consequently

\[
 0=\frac{\gamma\Omega^2}{2\Delta^2}
 \{p_g(\Delta)+p_e(\Delta)-2p_d(\Delta)\}+O(\Delta^{-3}),
\]

so \(p_d(\Delta)=\tfrac12[p_g(\Delta)+p_e(\Delta)]+o(1)\). Normalization now fixes the unique limit \(Z^{-1}(1,a,b,(a+b)/2)\). The coherence estimates show simultaneously that the full stationary density matrix converges to this diagonal state in the energy basis.

**4. Passive sorting and the sharp threshold.** The three low Hamiltonian levels (including the empty state) remain \(O(1)\), while the detuned energy is \(\Delta+O(1)\). Hence the coefficient of \(\Delta\) in the ordinary energy is \(p_d\), whereas the coefficient of \(\Delta\) in passive energy is the *least eigenvalue* of the limiting density matrix. Since \(a>b>0\),

\[
 b<\frac{a+b}{2}<a,
 \qquad
 \min\left\{1,a,b,\frac{a+b}{2}\right\}=\min\{1,b\}.
\]

This proves the two energy limits. If \(b\le1\), the least occupation is the antibonding state and \(\mathcal W_\Delta/\Delta\to(a-b)/(2Z)\); if \(b\ge1\), the least occupation is the vacuum and \(\mathcal W_\Delta/\Delta\to[(a+b)/2-1]/Z\). The crossing \(b=1\) is precisely \(\mu=\varepsilon+\Omega\). Division by the strictly positive stored-energy coefficient gives the displayed piecewise formula. Its value and one-sided derivatives follow by direct differentiation, and \(\lim_{\mu\to\infty}\eta_\infty(\mu)=1\), \(\lim_{\mu\to\infty}p_d=1/3\) follow directly from the positive rational expressions. The positive limiting \(\eta\) for every fixed finite \(\mu\) does not assert uniformity as \(\mu\) or \(\vartheta\) varies with \(\Delta\).

## Verification

Run `python verify.py` with NumPy and SciPy. The deterministic program constructs all sixteen matrix elements of the full four-state Lindblad superoperator, solves the trace-one stationary linear system, computes ergotropy from **the entire density-matrix spectrum**, and compares multiple detunings, temperatures, chemical potentials and positive dephasing/contact strengths with the derived coefficients. It separately checks the chemical-potential branch, population normalization, strict right slope, and reduced-state limiting identities. The analytical proof, not finite numerical evaluation, establishes the quantified infinite-detuning theorem.

## Relationship to prior work

Singh, Sánchez and Jordan [1] define the exact same Hamiltonian, reservoir contact and local-dephasing generator. Their published high-detuning formulas (10) and (11) cover chemical potentials **between the two low-energy modes** and give the \(\tanh h\) efficiency. Their numerical main text sets \(\mu=\varepsilon\), and their higher-charge leakage check explores a limited window about this value. Those results are recovered on the lower branch. The current claim extends the *same specified stationary generator* to every fixed finite chemical potential and identifies the previously unaddressed change in **which level receives the smallest density eigenvalue under passive rearrangement** once the reservoir chemical potential crosses the upper low-energy state.

The general passive-state sorting rule belongs to the foundational ergotropy theory of Allahverdyan, Balian and Nieuwenhuizen [2], and population inversion and coherent/incoherent distinctions are discussed broadly by Wang and Dou [3]. Neither general sorting by itself, nor the restricted-chemical-potential formulas of [1], specifies this generator's all-chemical-potential stationary population vector and the resulting sharp fixed-temperature passivity switch. The new claim is an exact natural-parameter classification of an explicit physical generator, not a new general ergotropy definition or a universal bound for arbitrary batteries.

## Limitations

The claim is for the strict empty-plus-one-electron Hilbert space and fixed positive \(\gamma,\Gamma,\Omega,\vartheta\); it does **not** extend to vanishing dephasing, multielectron injection, phonon-induced relaxation, chemical potentials scaling with \(\Delta\), or finite-detuning exact phase boundaries. In particular, [1] directly tested two-electron leakage only over a restricted reservoir-chemical-potential interval, so physical feasibility of the higher-chemical-potential branch requires checking charging energies and leakage for a specific device. The fraction \(\mathcal W/\mathcal E\) is the share of stored internal energy extractable by cyclic unitaries; it does not account for chemical work supplied by filling the device, nor assert near-unity total thermodynamic conversion efficiency. At finite detuning the crossing location and its subleading corrections may differ; the exact finite-detuning location is not asserted. Publication priority remains subject to a broader literature check; independent validation has not been performed.

## References

[1] A. N. Singh, R. Sánchez and A. N. Jordan, *Dephasing-powered open quantum-dot battery*, arXiv:2610.33408v1 (public October 24, 2026), https://arxiv.org/html/2610.33408v1 . Model in Sec. II, high-detuning expressions in Sec. III.1, physical higher-charge sector in Appendix D.

[2] A. E. Allahverdyan, R. Balian and Th. M. Nieuwenhuizen, *Maximal work extraction from quantum systems*, arXiv:cond-mat/0401574 (2004), https://arxiv.org/abs/cond-mat/0401574 .

[3] C.-J. Wang and F.-Q. Dou, *Ergotropy in Quantum Batteries*, arXiv:2512.21855v1 (December 26, 2025), https://arxiv.org/html/2512.21855v1 .
