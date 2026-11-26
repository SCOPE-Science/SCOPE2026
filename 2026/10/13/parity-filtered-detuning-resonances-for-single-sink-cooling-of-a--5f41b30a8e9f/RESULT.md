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

One cooled site is not a zero-forcing set on the cycle, yet almost every real detuning suffices. At a **nonzero** ratio \(\delta/J=2\cos(k\pi/(n-2))\) with even \(k\) in the indicated range, the auxiliary antiperiodic one-body problem has exactly one dark orbital, but there is no physical excited dark state. Zero detuning is always an exception to cooling, including when it occurs as an even-index cosine root.

## Assumptions and scope

The Hilbert space is \((\mathbb C^2)^{\otimes n}\). The basis vector \(|0\rangle\) denotes an unexcited qubit, \(\sigma^-|1\rangle=|0\rangle\), and \(N=\sum_j\sigma_j^+\sigma_j^-\) counts excitations. The only noise is the Markovian loss at site \(0\). The coherent couplings on every cycle edge are equal, real, and positive. The only site that can have a diagonal defect is site \(1\), immediately adjacent to the loss site. The cycle has no longitudinal \(ZZ\) interactions. All conclusions concern global convergence for all initial states, not rates of convergence or ground-state ordering.

## Proof

**1. Dark states are the only obstruction.** Since \([H,N]=0\), direct evaluation of the adjoint generator gives
\[
\frac{d}{dt}\operatorname{tr}(N\rho(t))=-\gamma\operatorname{tr}(\sigma_0^+\sigma_0^-\rho(t))\le0.
\]
A dark Hamiltonian eigenvector is one annihilated by \(\sigma_0^-\); its projector is stationary. Conversely, the excitation expectation has a limit. By continuity of the evolution, the forward orbit of any accumulation point of \(\rho(t)\) has constant excitation expectation equal to that limit. The identity above and positivity force this entire orbit to have support in \(\ker\sigma_0^-\), so that the dissipator vanishes and the orbit is unitary under \(H\). The span of the unitary translates of its initial support lies in \(\ker\sigma_0^-\) and is \(H\)-invariant. Since \(H\) and \(\sigma_0^+\sigma_0^-\) preserve excitation number, an excited part of this span would yield an excited dark Hamiltonian eigenvector in a fixed excitation sector. In their absence, every accumulation point is the vacuum state. Compactness in finite dimension gives trace-norm convergence. This is the finite-dimensional invariance argument underlying the global-attraction criterion of Beer and Burgarth, Proposition II.1 [1].

**2. Exact parity-resolved fermion reduction.** Fix an excitation number \(1\le p\le n\). In the ordered occupation basis the Hamiltonian on the \(p\)-excitation sector is the exterior-power action \(d\Gamma(h_q)\) on \(\bigwedge^p\mathbb C^n\), where
\[
q=(-1)^{p-1},\quad (h_q)_{j,j+1}=(h_q)_{j+1,j}=J\ (0\le j<n-1),\quad (h_q)_{0,n-1}=(h_q)_{n-1,0}=qJ,\quad (h_q)_{1,1}=\delta,
\]
with all other entries zero. An internal nearest-neighbor hop does not cross another occupied position in the wedge ordering. A hop across the closing bond crosses \(p-1\) occupied positions and hence acquires \((-1)^{p-1}\), which is canceled by the coefficient \(q\). At site \(0\), fermion annihilation is exactly the local lowering operator because the first site has no Jordan–Wigner string.

For each boundary sign define
\[
K_q=\operatorname{span}\{e_0,h_qe_0,\ldots,h_q^{n-1}e_0\},\qquad D_q=K_q^\perp.
\]
The common kernel of the annihilators \(a(w)\), \(w\in K_q\), in \(\bigwedge^p\mathbb C^n\) is \(\bigwedge^pD_q\): in an orthonormal basis adapted to \(K_q\oplus D_q\), annihilation by each \(K_q\) basis vector forces all occupation coefficients containing that vector to vanish. If \(\Psi\) is a dark eigenvector, its unitary orbit is annihilated by \(a(e_0)\). Conjugating the annihilator by the exterior powers of the one-body evolution (using the same auxiliary \(h_q\) on both exterior degrees) then shows \(a(e^{ith_q}e_0)\Psi=0\) for all real \(t\). Differentiation implies \(\Psi\in\bigwedge^pD_q\). Conversely \(D_q\) is \(h_q\)-invariant and, if \(\dim D_q\ge p\), \(\bigwedge^pD_q\) is a nonzero invariant subspace of the \(p\)-particle Hamiltonian consisting of dark vectors and hence contains an eigenvector. This argument requires no nondegeneracy of the many-particle energies.

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

If \(\eta\ne0\), the second boundary equation forces \(U_m\ne0\). Thus \(U_{m-2}=0\), giving the distinct roots
\[
t_k=2\cos\frac{k\pi}{n-2},\quad 1\le k\le n-3.
\]
At such a root, \(U_{m-1}(t_k/2)=(-1)^k\), so the boundary sign must be \(q=(-1)^{k+1}\); the defect condition then gives \(\eta=t_k\). Conversely at any such nonzero \(t_k\) these equations construct an eigenvector with \(v_0=0\). For fixed nonzero \(\eta\) there is at most one dark one-body direction for either \(q\): the roots are pairwise distinct and the eigenvector at each root is fixed by \(v_m\). Thus \(\dim D_q\le1\) for \(\eta\ne0\).

**4. Physical excitation parity and the zero-detuning exception.** The one-excitation sector has \(q=+1\), so for nonzero detuning it has a dark eigenstate exactly at the odd-index roots. For nonzero detuning, all sectors \(p\ge2\) are excluded by \(\dim D_q\le1<p\), even when an even-index root supplies one antiperiodic dark orbital. At \(\eta=0\), the periodic one-excitation ring has the dark eigenvector with amplitudes \(v_j=\sin(2\pi j/n)\), independently of whether zero is a root in the cosine list. Nor is the bound \(\dim D_q\le1\) valid in general at zero detuning: for \(n=6\), \(t_2=0\), and the auxiliary antiperiodic modes \(\sin(\pi j/6)\) and \(\sin(3\pi j/6)\) are independent dark eigenvectors. Their wedge gives a physical two-excitation dark eigenvector. Together with step 1 this proves the classification, including the stated scope of the even-index exclusion.

## Verification

The standalone program `verify.py` reconstructs the many-body spin matrices and compares them to parity-dependent fermionic exterior-power matrices for cycle lengths \(4\) through \(8\). It also verifies the Chebyshev continuant identity symbolically through degree \(28\), tests explicit dark eigenvectors and the listed parity branches through cycle length \(16\), and checks representative full-sector dark eigenvalue multiplicities. Invocation: `python verify.py` with Python 3, NumPy, and SymPy. The recorded run returned `VERIFY_OK 369`. Finite checks corroborate, but do not replace, the all-parameter proof above.

For illustration, the five-site cycle has physical exceptional ratios \(\{0,1\}\): setting \(\delta=-J\) produces an auxiliary antiperiodic one-body dark eigenvector but still cools every physical initial state. The six-site physical exceptional set is \(\{0,\sqrt2,-\sqrt2\}\).

## Relationship to prior work

Beer and Burgarth [1] prove a global-attraction criterion for local cooling and a sufficient condition based on the cooling vertices being a graph-theoretic zero-forcing set. A singleton on the cycle is not zero forcing, so that sufficient condition does not decide this example. The no-dark-overlap and cyclic-subspace viewpoint is closely related to the controllability framework of Burgarth, D'Alessandro, Hogben, Severini, and Young [2]. Wang, Pemberton-Ross, and Schirmer [3] study one-node Hamiltonian controls and symmetry obstructions in spin networks, including single-excitation subspaces. The result here is the explicit exact all-detuning classification for the single-loss XX ring, including the passage from one-body modes to physical fixed-excitation sectors.

## Limitations

Only an XX Hamiltonian with one adjacent detuning and one strictly positive local loss is treated; longitudinal interactions, extra defects, arbitrary graphs, collective reservoirs, and driving are outside the theorem. The argument establishes eventual trace-norm convergence, not a positive lower bound uniform in \(n\) for the Liouvillian gap. The cooling vacuum need not be the ground state of the bare Hamiltonian without an additional chemical potential. Priority remains subject to unindexed or differently formulated prior results, particularly spectral controllability treatments of cycles.

## References

[1] K. Beer and D. Burgarth, *Global zero-excitation state preparation through subsystem cooling*, arXiv:2609.23960v1 (first publicly submitted 2026-09-21), https://arxiv.org/abs/2609.23960.

[2] D. Burgarth, D. D'Alessandro, L. Hogben, S. Severini, and M. Young, *Zero forcing, linear and quantum controllability for systems evolving on networks*, arXiv:1111.1475, https://arxiv.org/abs/1111.1475.

[3] X. Wang, P. Pemberton-Ross, and S. G. Schirmer, *Symmetry & Controllability for Spin Networks with a Single-Node Control*, arXiv:1012.3695, https://arxiv.org/abs/1012.3695.
