# Parity-filtered detuning resonances for single-sink cooling of an XX ring

## Finding

**Theorem.** For any integer \(n\ge4\), positive \(J\) and \(\gamma\), and real \(\delta\), define the following Lindblad evolution on a periodic chain of \(n\) qubits:
\[
H=J\sum_{j=0}^{n-1}(\sigma_j^+\sigma_{j+1}^-+\sigma_j^-\sigma_{j+1}^+)+\delta\sigma_1^+\sigma_1^-,\qquad
\dot\rho=-i[H,\rho]+\gamma\left(\sigma_0^-\rho\sigma_0^+-\tfrac12\{\sigma_0^+\sigma_0^-,\rho\}\right),
\]
where site indices are reduced modulo \(n\). Put
\[
\mathcal R_n=\{0\}\cup\left\{2\cos\frac{k\pi}{n-2}:1\le k\le n-3,\ k\ \text{odd}\right\}.
\]
Then, for **every** initial density matrix \(\rho(0)\), the evolution tends in trace norm to \(|0\cdots0\rangle\langle0\cdots0|\) as time tends to infinity **if and only if** \(\delta/J\notin\mathcal R_n\). For every excluded ratio, at least one orthogonal excited pure state is stationary. No constraint on \(\gamma/J>0\) is imposed.

In particular, one cooled site is not a zero-forcing set on the cycle, yet almost every real detuning suffices. A subtle distinction is essential: the auxiliary antiperiodic fermionic one-body sector can have a dark mode at \(\delta/J=2\cos(k\pi/(n-2))\) with even \(k\), but this *does not* produce a physical excited invariant sector.

## Assumptions and scope

The Hilbert space is \((\mathbb C^2)^{\otimes n}\). The basis vector \(|0\rangle\) denotes an unexcited qubit, \(\sigma^-|1\rangle=|0\rangle\), and \(N=\sum_j\sigma_j^+\sigma_j^-\) counts excitations. The only noise is the Markovian loss at site \(0\). The coherent couplings on every cycle edge are equal, real, and positive. Site \(1\), immediately adjacent to the loss site, has the sole nonzero diagonal defect. The cycle has no longitudinal \(ZZ\) interactions. All conclusions concern global convergence for all initial states, not rates of convergence or ground-state ordering.

## Proof

**1. Dark states are the only obstruction.** Since \([H,N]=0\), direct evaluation of the adjoint generator gives
\[
\frac{d}{dt}\operatorname{tr}(N\rho(t))=-\gamma\operatorname{tr}(\sigma_0^+\sigma_0^-\rho(t))\le0.
\]
Every stationary state must therefore have support in \(\ker\sigma_0^-\); on this subspace the dissipator vanishes and stationarity forces commutation with \(H\). Conversely, any Hamiltonian eigenvector annihilated by \(\sigma_0^-\) produces a stationary pure state. Because the state space is compact and the excitation expectation is a strict Lyapunov function outside the maximal invariant subset of \(\ker\sigma_0^-\), the finite-dimensional invariance principle proves that absence of excited dark eigenvectors entails convergence to the vacuum for every input. Equivalently, one may apply the global-attraction criterion of Beer and Burgarth, Proposition II.1 [1]. It remains to classify such vectors in every excitation sector, not just in the one-excitation sector.

**2. Exact parity-resolved fermion reduction.** Fix an excitation number \(1\le p\le n\). The Jordan–Wigner mapping identifies the corresponding Hamiltonian with the \(p\)-particle exterior-power action \(d\Gamma(h_q)\) on \(\bigwedge^p\mathbb C^n\), where
\[
q=(-1)^{p-1},\quad (h_q)_{j,j+1}=(h_q)_{j+1,j}=J\ (0\le j<n-1),\quad (h_q)_{0,n-1}=(h_q)_{n-1,0}=qJ,\quad (h_q)_{1,1}=\delta,
\]
with all other entries zero. The parity-dependent sign on the closing edge is indispensable; an unsigned free-fermion reduction in every excitation sector would give the wrong exceptional set. At site \(0\), fermion annihilation is exactly the local lowering operator, since its Jordan–Wigner string is empty.

For each boundary sign define the cyclic Krylov subspace and its orthogonal complement
\[
K_q=\operatorname{span}\{e_0,h_qe_0,\ldots,h_q^{n-1}e_0\},\qquad D_q=K_q^\perp.
\]
The **exterior-dark-subspace lemma** states that the \(p\)-particle Hamiltonian has a dark eigenvector if and only if \(\dim D_q\ge p\). Indeed, if \(\Psi\) is such an eigenvector, the full orbit remains annihilated by the site-zero fermion; under quadratic Heisenberg evolution, this is equivalent to \(a(e^{-ith_q}e_0)\Psi=0\) for all real \(t\). Analytic expansion in \(t\) therefore gives \(a(w)\Psi=0\) for every \(w\in K_q\). In the exterior algebra, their common kernel is exactly \(\bigwedge^p D_q\). Conversely, \(D_q\) is invariant under the Hermitian matrix \(h_q\), so whenever its dimension is at least \(p\), the nonzero invariant subspace \(\bigwedge^pD_q\) contains an eigenvector. The lemma does not assume nondegenerate many-particle energies.

**3. One-particle dark eigenvectors.** Rescale \(\lambda/J=t\), \(\delta/J=\eta\), and let \(m=n-1\). For a nonzero eigenvector \(v\) of \(h_q\) with \(v_0=0\), the Jacobi recurrence along sites \(m,m-1,\ldots,1\) implies
\[
v_j=U_{m-j}(t/2)v_m\qquad(1\le j\le m),
\]
where \(U_r\) is the Chebyshev polynomial of the second kind, \(U_0=1\), \(U_1(t/2)=t\), and \(U_{r+1}=tU_r-U_{r-1}\). The endpoint amplitude \(v_m\) cannot vanish for a nonzero solution. The equations at sites \(0\) and \(1\) become
\[
U_{m-1}(t/2)=-q,\qquad U_m(t/2)=\eta U_{m-1}(t/2).
\]
The continuant identity
\[
U_m(t/2)U_{m-2}(t/2)-U_{m-1}(t/2)^2=-1
\]
shows that \(U_mU_{m-2}=0\) at any dark eigenvalue.

If \(\eta\ne0\), the second boundary equation forces \(U_m\ne0\). Thus \(U_{m-2}=0\), giving the *distinct* roots
\[
t_k=2\cos\frac{k\pi}{n-2},\quad 1\le k\le n-3.
\]
At such a root, \(U_{m-1}(t_k/2)=(-1)^k\), so the boundary sign must be \(q=(-1)^{k+1}\); the defect condition then gives \(\eta=t_k\). Conversely these equations construct an eigenvector with \(v_0=0\). For fixed nonzero \(\eta\), there is **at most one** dark one-particle eigenvector for either choice of \(q\), because the listed cosine values are pairwise distinct and every solution is uniquely fixed by \(v_m\). Therefore \(\dim D_q\le1\) when \(\eta\ne0\).

**4. Physical excitation parity excludes the even-index resonances.** In the one-excitation sector \(p=1\), the Jordan–Wigner boundary sign is \(q=+1\). The preceding equations produce a physical excited dark eigenstate precisely at nonzero \(\eta=t_k\) with **odd** \(k\). For all \(p\ge2\), the exterior-dark-subspace lemma and \(\dim D_q\le1<p\) forbid a dark many-body eigenvector, for either \(q\). Hence the even-index roots, which require \(q=-1\), cannot prevent physical cooling. Finally, at \(\eta=0\), the ordinary zero-defect cycle has a one-excitation dark eigenvector, e.g. the standing wave with amplitudes \(v_j=\sin(2\pi j/n)\) (the loss amplitude vanishes at \(j=0\)); this includes \(n=4\). Combining this classification with step 1 completes both directions for all \(n,J,\gamma,\delta\).

## Verification

The standalone program `verify.py` reconstructs the many-body spin matrices independently and compares them to parity-dependent fermionic exterior-power matrices in all sectors for cycle lengths \(4\) through \(8\). It also verifies the Chebyshev continuant identity symbolically through degree \(28\), tests explicit dark eigenvectors and all listed parity branches through cycle length \(16\), and checks representative full-sector dark eigenvalue multiplicities. Invocation: `python verify.py` with Python 3, NumPy, and SymPy. The completed run returned `VERIFY_OK 369`. Finite checks corroborate, but do not replace, the all-parameter proof above.

For illustration, the five-site cycle has physical exceptional ratios \(\{0,1\}\): setting \(\delta=-J\) produces an auxiliary antiperiodic one-body dark eigenvector but **still cools every physical initial state**. The six-site physical exceptional set is \(\{0,\sqrt2,-\sqrt2\}\).

## Relationship to prior work

Beer and Burgarth [1] prove a global-attraction criterion for local cooling and a sufficient condition based on the cooling vertices being a graph-theoretic zero-forcing set. The single vertex on a cycle is not zero forcing, and [1] does not give the present exact detuning-resonance classification. The no-dark-overlap and cyclic-subspace viewpoint is closely related to the known controllability framework of Burgarth, D'Alessandro, Hogben, Severini, and Young [2]. Wang, Pemberton-Ross, and Schirmer [3] study one-node Hamiltonian controls and symmetry obstructions in spin networks, including single-excitation subspaces. The new assertion is the explicit all-cycle, all-detuning **dissipative all-excitation-sector** classification, including the parity-filtered resonances of the periodic Jordan–Wigner map; neither the general zero-forcing criterion nor one-particle controllability by itself settles these parity sectors.

## Limitations

Only an XX Hamiltonian with one nearest-neighbor detuning and one strictly positive local loss is treated; longitudinal interactions, extra defects, arbitrary graphs, collective reservoirs, and driving are outside the theorem. The argument establishes eventual trace-norm convergence, not a positive lower bound uniform in \(n\) for the Liouvillian gap. The cooling vacuum need not be the ground state of the bare Hamiltonian without an additional chemical potential. Priority remains subject to unindexed or differently formulated prior results, particularly spectral controllability treatments of cycles.

## References

[1] K. Beer and D. Burgarth, *Global zero-excitation state preparation through subsystem cooling*, arXiv:2609.23960v1 (first publicly submitted 2026-09-21), https://arxiv.org/abs/2609.23960.

[2] D. Burgarth, D. D'Alessandro, L. Hogben, S. Severini, and M. Young, *Zero forcing, linear and quantum controllability for systems evolving on networks*, arXiv:1111.1475, https://arxiv.org/abs/1111.1475.

[3] X. Wang, P. Pemberton-Ross, and S. G. Schirmer, *Symmetry & Controllability for Spin Networks with a Single-Node Control*, arXiv:1012.3695, https://arxiv.org/abs/1012.3695.
