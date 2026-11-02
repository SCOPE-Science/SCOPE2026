# Exact Curie--Weiss criticality from collective stochastic anti-Hermitian loss without entanglement

## Finding
A common Gaussian fluctuation in a strictly local one-body loss operator produces an exactly solvable, all-to-all *classical* ordering transition in the normalized ensemble output of noninteracting qubits. The entire density operator is a mixture of identical product states for every finite population; hence no particle-partition entanglement is generated. Despite that separability, its computational-basis diagonal coincides exactly with the zero-field Curie--Weiss ferromagnet at inverse temperature \(t\), showing a sharp ordering transition at \(t=1\). Its connected two-spin \(z\)-correlation has an exact three-regime asymptotic: order \(N^{-1}\) below, order \(N^{-1/2}\) at, and order one above the transition.

For \(N\geq2\), let \(C_N(t)=\operatorname{tr}(\rho_N(t)\sigma_z^{(1)}\sigma_z^{(2)})-\operatorname{tr}(\rho_N(t)\sigma_z^{(1)})\operatorname{tr}(\rho_N(t)\sigma_z^{(2)})\). Then for every fixed \(t>0\),
\[
\lim_{N\to\infty}N C_N(t)=\frac{t}{1-t}\quad(0<t<1),\qquad
\lim_{N\to\infty}\sqrt N C_N(1)=\sqrt{12}\,\frac{\Gamma(3/4)}{\Gamma(1/4)},\qquad
\lim_{N\to\infty}C_N(t)=m_*(t)^2\quad(t>1),
\]
where \(m_*(t)\in(0,1)\) is the unique positive solution of \(m=\tanh(tm)\). The middle constant is approximately \(1.1708286566075286\). These limits are derived here from the exact quantum-state representation; the *classical Curie--Weiss critical theory itself is established prior mathematics*, not a claimed new Ising theorem.

## Assumptions and scope
Let \(N\geq1\) qubits have \(n_j=|1\rangle\langle1|_j\), \(L_N=\sum_{j=1}^{N}n_j\), and initial pure product state \(\rho_N(0)=|+\rangle\langle+|^{\otimes N}\), with \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\). Set the Hamiltonian to zero. Let \(W_t\) be one *shared*, standard real Brownian motion, not independent noise per qubit. For all \(t\geq0\), define
\[
K_t=\exp[-tL_N-N^{-1/2}L_NW_t],\qquad
\widetilde\rho_N(t)=\mathbb E[K_t\rho_N(0)K_t^\dagger],\qquad
\rho_N(t)=\frac{\widetilde\rho_N(t)}{\operatorname{tr}\widetilde\rho_N(t)}.
\]
This is the Gaussian collective-loss specialization of the ensemble *before* normalization construction of [1], at \(\gamma=1/(2N)\). The completely positive averaged evolution is trace-nonincreasing: every eigenspace of \(L_N\) with eigenvalue \(0\leq k\leq N\) has trace multiplier \(\exp[-2tk(1-k/N)]\leq1\). The normalization is after ensemble averaging; replacing it by an average of normalized stochastic trajectories changes the model and is not covered. All limits fix physical \(t\) independently of \(N\), except the explicitly given finite-size scalings.

For an Ising spin word \(s=(s_1,\ldots,s_N)\in\{-1,1\}^N\), identify \(s_j=1\) with computational basis state \(|1\rangle\), and write \(M(s)=\sum_js_j\). Define for \(t>0\):
\[
|\psi_y\rangle=\frac{e^{-y/2}|0\rangle+e^{y/2}|1\rangle}{\sqrt{2\cosh y}},\qquad
\pi_{N,t}(dy)=\frac{e^{N[\log\cosh y-y^2/(2t)]}}{\int_{\mathbb R}e^{N[\log\cosh u-u^2/(2t)]}\,du}\,dy.
\]
At \(t=0\) set \(\pi_{N,0}=\delta_0\).

## Proof
**1. Gaussian semigroup and trace.** For configurations \(s,u\) containing respectively \(k=(N+M(s))/2\) and \(\ell=(N+M(u))/2\) excitations, the Brownian moment generating formula gives
\[
\langle s|\widetilde\rho_N(t)|u\rangle=2^{-N}\exp\!\left[-t(k+\ell)+\frac{t(k+\ell)^2}{2N}\right]
=2^{-N}e^{-Nt/2}\exp\!\left[\frac{t(M(s)+M(u))^2}{8N}\right].
\]
For diagonal entries \(s=u\), cancel the common prefactor by trace normalization to get the *exact*, finite-population Curie--Weiss law
\[
\langle s|\rho_N(t)|s\rangle=
\frac{\exp[tM(s)^2/(2N)]}{\sum_{u\in\{-1,1\}^N}\exp[tM(u)^2/(2N)]}.
\]
In particular, every odd \(z\)-magnetization expectation vanishes by spin-flip symmetry.

**2. Full separability, not merely a diagonal identity.** The Hubbard--Stratonovich Gaussian identity, with \(Y\sim\mathcal N(0,t/N)\), gives
\[
\exp\!\left[\frac{t(M(s)+M(u))^2}{8N}\right]
=\mathbb E\exp\!\left[\frac Y2(M(s)+M(u))\right].
\]
For every \(N\geq1\) and \(t\geq0\), after factoring the norm \((2\cosh Y)^N\), this identity proves the *entire matrix equality*
\[
\boxed{\rho_N(t)=\int_{\mathbb R}(|\psi_y\rangle\langle\psi_y|)^{\otimes N}\,\pi_{N,t}(dy).}
\]
Since this is an explicit convex mixture of product states, it is separable across **every** partition. In this mixture \(\langle\psi_y|\sigma_z|\psi_y\rangle=\tanh y\). Symmetry of \(\pi_{N,t}\) therefore gives \(C_N(t)=\int \tanh^2 y\,\pi_{N,t}(dy)\), with \(C_N(0)=0\).

**3. Sharp phase diagram.** Let \(f_t(y)=\log\cosh y-y^2/(2t)\). Its derivative vanishes when \(y=t\tanh y\). For \(0<t\leq1\), strict concavity away from the origin and \(\tanh y<y\) for positive \(y\) show that \(y=0\) is the unique global maximum. For \(t>1\), \(\tanh y/y\) strictly decreases for \(y>0\), producing exactly two global maxima \(\pm y_*(t)\), the unique positive root satisfying \(y_*=t\tanh y_*\); they are nondegenerate. The Gaussian tails \(f_t(y)\leq|y|-y^2/(2t)\) justify Laplace localization and convergence of all bounded continuous observables.

For \(0<t<1\), the local quadratic expansion \(f_t(y)=-(1-t)y^2/(2t)+O(y^4)\) and Laplace's method yield \(N\mathbb E_{\pi}y^2\to t/(1-t)\). The estimate \(\tanh^2y=y^2+O(y^4)\) yields \(NC_N(t)\to t/(1-t)\). At \(t=1\), \(f_1(y)=-y^4/12+O(y^6)\), so \(N^{1/4}Y\) tends in moments to the distribution with density proportional to \(e^{-v^4/12}\). Its second moment is \(\sqrt{12}\Gamma(3/4)/\Gamma(1/4)\), proving the critical limit. For \(t>1\), concentration at \(\pm y_*\) yields \(C_N(t)\to\tanh^2 y_*=m_*^2\).

For each fixed subsystem size \(k\), bounded continuity of the rank-one product projectors in \(y\) further implies the *trace-norm* reduced-state limits: \(|+\rangle\langle+|^{\otimes k}\) when \(t\leq1\); and for \(t>1\) the equal mixture of \((|\psi_{y_*}\rangle\langle\psi_{y_*}|)^{\otimes k}\) and \((|\psi_{-y_*}\rangle\langle\psi_{-y_*}|)^{\otimes k}\). No limit here asserts convergence of full \(N\)-body states on changing Hilbert spaces.

## Verification
The independent script `verify.py` evaluates the finite-population Gaussian ensemble by two separate methods: explicit computational-basis matrix elements and Gaussian quadrature over the shared noise. It checks positivity, unit trace, exact Curie--Weiss diagonals, symmetry, and physical trace nonincrease for \(N=2,3,4,5\) at five positive times, and tests the asymptotic regime and the quartic critical constant. It passed 136 deterministic checks. The proof, rather than the finite calculations, establishes the universal identities and thermodynamic limits. Run with `python verify.py` using Python, NumPy and SciPy.

## Relationship to prior work
[1] develops the stochastic non-Hermitian ensemble-before-normalization evolution; its formula is specialized above to collective diagonal loss. [2] gives classical Curie--Weiss thermodynamics, the Hubbard--Stratonovich formalism and mean-field symmetry breaking. Neither separately supplies the full-separable quantum identification and observed two-qubit correlation trichotomy for this noise model. [3] covers non-Hermitian mixed-state dynamics but not the collective Gaussian-induced Ising transition. The original component being evaluated is the exact **quantum-to-classical reduction with separability** and its explicit critical two-qubit correlation profile, not the already-known Curie--Weiss magnet's phase transition itself. Mathematically equivalent rephrasings through postselected weak measurement or other Gaussian collective-noise constructions remain possible in broader literature.

## Limitations
The output is obtained by averaging an unnormalized stochastic quantum operation and only then renormalizing. It does not describe normalized trajectories averaged afterwards, generic Lindblad trace-preserving dynamics, independent local noise, or any positive-temperature interacting quantum Hamiltonian. The transition is in the large-\(N\) limit for fixed \(t\); no nonanalyticity at finite \(N\). Classical correlations do not imply quantum entanglement. No entropy-production formula, finite-sample statistical detection law, or priority against every possible alternate representation is established.

## References
[1] A. Martínez-Azcona, A. Kundu, A. Saxena, A. del Campo and A. Chenu, *Quantum Dynamics with Stochastic Non-Hermitian Hamiltonians*, arXiv:2407.07746, publicly posted 2024-07-10.

[2] M. Kochmański, T. Paszkiewicz and S. Wolski, *Curie--Weiss magnet—a simple model of phase transition*, arXiv:1301.2141 (2013).

[3] D. C. Brody and E.-M. Graefe, *Mixed-state evolution in the presence of gain and loss*, arXiv:1208.5297 (2012).
