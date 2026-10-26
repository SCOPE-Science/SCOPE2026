# Sharp star-degree concurrence laws for postselected quantum-spin transport

## Finding
For the monitored, bidirectionally incoherent, coherent XY spin-star model below, with \(m\ge2\) leaves and fixed \(J,\gamma>0\), \(0<\eta<1\), the unique conditional stationary state \(\rho_m\) has the following large-degree limits. Put
\[
a=\frac{4J^2}{\gamma^2(1-\eta)^2}.
\]
The stationary unnormalized growth exponent, hub occupation, hub–leaf concurrence, and distinct-leaf concurrence satisfy
\[
\lim_{m\to\infty}\lambda_m=-\gamma\eta(2-\eta),\qquad
\lim_{m\to\infty}m\langle0|\rho_m|0\rangle=1-\eta,
\]
\[
\boxed{\lim_{m\to\infty}m^2 C_{0j}(\rho_m)=\frac{4J\eta}{\gamma(1+a)}}\!,\qquad
\boxed{\lim_{m\to\infty}m^2 C_{jk}(\rho_m)=\frac{2a\eta}{1+a}}\quad(j\ne k).
\]
All four asymptotics have \(O(m^{-1})\) remainders after the indicated rescaling. In particular,
\[
\lim_{m\to\infty}\frac{C_{jk}}{C_{0j}}=\frac{2J}{\gamma(1-\eta)^2}.
\]
Thus, away from equality, hub–leaf concurrence is eventually larger for \(2J<\gamma(1-\eta)^2\), and distinct-leaf concurrence is eventually larger for \(2J>\gamma(1-\eta)^2\). Individual concurrences vanish quadratically in the star degree although the number of leaf pairs grows quadratically.

## Assumptions and scope
The physical Hilbert space is the one-excitation subspace of \(m+1\) qubits, spanned by \(|0\rangle\) (hub) and \(|j\rangle\), \(1\le j\le m\) (leaves). The Hamiltonian and the \(2m\) directed jump operators are
\[
H_m=J\sum_{j=1}^m(|0\rangle\langle j|+|j\rangle\langle0|),\qquad
L_{0j}=|0\rangle\langle j|,\quad L_{j0}=|j\rangle\langle0|.
\]
Every jump has rate \(\gamma>0\). A fraction \(\eta\in(0,1)\) of jumps is discarded by postselection. With \(\{A,B\}=AB+BA\), the normalized conditional master equation is
\[
\dot\rho=-i[H_m,\rho]+\gamma\sum_{\alpha}\Big((1-\eta)L_\alpha\rho L_\alpha^\dagger-\tfrac12\{L_\alpha^\dagger L_\alpha,\rho\}+\eta\operatorname{Tr}(L_\alpha^\dagger L_\alpha\rho)\rho\Big).
\]
The corresponding linear, non-trace-preserving generator \(\mathcal L_m\) omits the final nonlinear trace-renormalization term. For any nonzero positive initial state, \(e^{t\mathcal L_m}\rho/\operatorname{Tr}(e^{t\mathcal L_m}\rho)\) converges as \(t\to\infty\) to \(\rho_m\), and \(\mathcal L_m(\rho_m)=\lambda_m\rho_m\). Concurrence is Wootters two-qubit concurrence of the reduced two-site density matrix in the full qubit embedding.

## Proof
**Existence, uniqueness and symmetry.** The generator \(\mathcal L_m\) defines a completely positive trace-decreasing semigroup: its effective Hamiltonian gives the no-jump part, and the positive jump part has coefficient \(\gamma(1-\eta)>0\). For every positive nonzero initial operator and every \(t>0\), the time-ordered jump-path expansion includes positive multiples of every rank-one site projector. Indeed, some initial site occupation is positive, and the bidirectional connected star admits a finite jump path from it to each prescribed target; paths with very short intervening no-jump intervals give nonzero weights. Hence the semigroup is positivity improving. Finite-dimensional Perron–Frobenius theory for the cone of positive semidefinite matrices yields a real, simple spectral-bound eigenvalue \(\lambda_m\) with a strictly positive stationary eigenmatrix, and normalized convergence for every nonzero positive input. Leaf-permutation invariance and uniqueness imply that this eigenmatrix is invariant under all leaf permutations.

Let \(|s\rangle=m^{-1/2}\sum_{j=1}^m|j\rangle\), and \(P_D=\sum_j|j\rangle\langle j|-|s\rangle\langle s|\). The stationary matrix consequently has the form
\[
\rho_m=h|0\rangle\langle0|+s|s\rangle\langle s|+dP_D+z|0\rangle\langle s|+\bar z|s\rangle\langle0|,
\quad h+s+(m-1)d=1,
\]
where \(h,s,d\) are real and nonnegative. Set \(\Gamma_m=\gamma(m+1)/2\). Direct substitution in \(\mathcal L_m(\rho_m)=\lambda_m\rho_m\) gives
\[
\begin{aligned}
(\lambda_m+\gamma m)h&=\gamma(1-\eta)[s+(m-1)d]+T_m(\lambda_m)(s-h),\\
(\lambda_m+\gamma)s&=\gamma(1-\eta)h-T_m(\lambda_m)(s-h),\\
(\lambda_m+\gamma)d&=\gamma(1-\eta)h,\\
z&=-i\frac{J\sqrt m}{\lambda_m+\Gamma_m}(s-h),\qquad
T_m(\lambda)=\frac{2J^2m}{\lambda+\Gamma_m}.
\end{aligned}
\]
The final two expressions apply for sufficiently large \(m\), as follows from the limiting solution below; alternatively, the original five-dimensional linear system makes sense at every \(m\).

**Analytic large-degree limit.** Put \(t=1/m\), \(h=tH\), \(s=tS\), \(d=tD\), and
\[
T(t,\lambda)=\frac{4J^2}{\gamma(1+t)+2\lambda t}.
\]
The four independent eigenvalue/normalization equations become
\[
\begin{aligned}
(\gamma+\lambda t)H&=\gamma(1-\eta)[D+t(S-D)]+tT(S-H),\\
(\lambda+\gamma)S&=\gamma(1-\eta)H-T(S-H),\\
(\lambda+\gamma)D&=\gamma(1-\eta)H,\\
D+t(S-D)+tH&=1.
\end{aligned}
\]
At \(t=0\) this system is triangular after using normalization and has the unique solution
\[
D_0=1,\quad H_0=1-\eta,\quad
\lambda_0=-\gamma\eta(2-\eta),\quad
S_0=\frac{1+a(1-\eta)}{1+a},\quad
a=\frac{4J^2}{\gamma^2(1-\eta)^2}.
\]
The Jacobian in \((H,S,D,\lambda)\) is nonsingular: the normalization fixes \(D\); the first equation then fixes \(H\); the third fixes \(\lambda\) because \(D_0=1\); the second fixes \(S\) with positive coefficient \(\gamma(1-\eta)^2+4J^2/\gamma\). The analytic implicit-function theorem therefore gives \((H,S,D,\lambda)=(H_0,S_0,D_0,\lambda_0)+O(t)\). For small \(t>0\) the resulting normalized matrix is strictly positive: \(h,s,d\) are positive of order \(t\) and its hub/bright coherence is \(O(t^{3/2})\). It must therefore be the unique positive Perron eigenmatrix found above.

**Concurrences.** Any two-site qubit reduction of a state supported on the one-excitation sector has zero doubly-excited population, and its concurrence is twice the modulus of the corresponding single-excitation off-diagonal matrix entry. The symmetric decomposition yields
\[
\rho_{0j}=z/\sqrt m=-i\frac{J(s-h)}{\lambda_m+\Gamma_m},\qquad
\rho_{jk}=(s-d)/m\quad(j\ne k).
\]
Since \(S_0-H_0=\eta/(1+a)\), \(S_0-D_0=-a\eta/(1+a)\), and \(\lambda_m+\Gamma_m=\gamma m/2+O(1)\), these expressions give precisely the two boxed limits and their stated \(O(m^{-1})\) rescaled errors. Both constants are strictly positive; their ratio gives the sharp large-degree crossover.

## Verification
A standalone `verify.py` constructs both the symmetry-reduced generator and, for small stars, the full complex superoperator directly from its Hamiltonian and jump matrices. It checks agreement of the leading eigenvalue and concurrences for \(m=2,3,5\), positivity of the stationary operator, and large-degree asymptotic constants at several parameter values. These tests are finite-dimensional consistency checks; the universal all-degree results follow from the analytic semigroup and implicit-function arguments above.

## Relationship to prior work
Adithya L. J., Hegde and Meena (2026), arXiv:2603.17629v1, analyze the same family of monitored quantum-spin transport dynamics and numerically demonstrate stationary localization and surviving entanglement for a six-spin star, while also treating a distinct graph-Laplacian quantum-stochastic-walk model. Their work does not provide these large-degree sharp concurrence limits or the hub-versus-leaf pairing crossover. Liu and Chen (2024), arXiv:2405.11812, develop the general jump-loss nonlinear master-equation framework, emphasizing one-dimensional nonreciprocal dynamics rather than a symmetric spin star and its two-qubit concurrence. General quantum-jump and finite-dimensional Perron theory are established ingredients, not claimed as original.

## Limitations
The result is for equal-strength bidirectional edge jumps, identical coherent hub–leaf couplings, the one-excitation spin sector and fixed \(J,\gamma>0\), \(0<\eta<1\). It does not cover the unmonitored or fully monitored endpoints, simultaneous degree-dependent scaling of the parameters, arbitrary graphs, many-excitation states, or a finite-degree global concurrence ordering at the crossover equality. Analytical asymptotics are not inferred from the numerical tests. The literature comparison is best-knowledge and not a proof of global priority.

## References
1. Adithya L. J., Suraj S. Hegde and Chandrakala Meena, *Postselection-induced localization and coherence in quantum walks on heterogeneous networks* (first public version March 18, 2026), arXiv:2603.17629, https://arxiv.org/abs/2603.17629 .
2. Yu-Guo Liu and Shu Chen, *Lindbladian dynamics with loss of quantum jumps* (2024), arXiv:2405.11812, https://arxiv.org/abs/2405.11812 .
3. W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, Physical Review Letters 80 (1998), 2245–2248; DOI:10.1103/PhysRevLett.80.2245.
