# Algebraic dark-mode resonances and quadratic loss reopening in finite SSH chains

## Finding
Consider the open, number-conserving fermionic Su–Schrieffer–Heeger (SSH) chain with \(N\ge2\) unit cells, intracell hopping \(1\), intercell hopping \(r>0\), and a single Markovian particle-loss operator \(\sqrt{\gamma}\,c_{A_m}\), where \(1\le m\le N\) and \(\gamma>0\). A *dark orbital* is a one-body eigenvector of the Hermitian hopping matrix whose amplitude at the loss site is exactly zero. Define \(L=N+1-m\) and the finite set
\[
\mathcal R_{N,m}=\left\{-\frac{\sin(m\pi j/L)}{\sin((m-1)\pi j/L)}:\ 1\le j<L,\ \sin((m-1)\pi j/L)\ne0,\ -\frac{\sin(m\pi j/L)}{\sin((m-1)\pi j/L)}>0\right\}.
\]
For \(L=1\), or \(m=1\), this is the empty set. Let \(J_{N,m}(r)\) denote the set of indices \(j\) appearing in this construction whose displayed ratio equals \(r\). Then the number of dark **one-body eigenvectors**, counted over both energy signs, is exactly
\[
q_{N,m}(r)=2\,|J_{N,m}(r)|.
\]
In particular, the loss-driven finite-dimensional fermionic system converges from every initial state to its empty vacuum **if and only if** \(r\notin\mathcal R_{N,m}\); for \(r\in\mathcal R_{N,m}\) it contains a noiseless Fock subspace of dimension \(2^{q_{N,m}(r)}\), hence at least that many mutually orthogonal stationary pure states. A loss on \(B_m\) has precisely the same classification after replacing \(m\) by \(N+1-m\).

Every exceptional ratio is a positive real algebraic number, and for fixed \(N,m\) there are finitely many. A genuinely nonuniform example is \(N=14\), loss on \(A_3\), and \(r=\sqrt2\): exactly four one-body dark orbitals survive, and the noiseless fermionic subspace has dimension \(16\).

There is also a quantitative law for the opening of loss at each isolated nodal orbital. Fix \(j\in J_{N,m}(r_0)\), set \(k_0=\pi j/L\), and let \(E_\pm(r)\) be the two clean eigenvalue branches passing through \(\pm\sqrt{1+r_0^2+2r_0\cos k_0}\). Let \(\lambda_\pm(r,\gamma)\) be the corresponding eigenvalues of the non-Hermitian one-body no-jump Hamiltonian \(H(r)-i\gamma |A_m\rangle\langle A_m|/2\), locally continued from those clean branches. With
\[
F(k,r)=\sin((N+1)k)+r\sin(Nk),\qquad
b=-\frac{\sin(Nk_0)}{(N+1)\cos((N+1)k_0)+r_0N\cos(Nk_0)},
\]
the *iterated weak-loss and near-resonance limit* is
\[
\lim_{r\to r_0}\frac{1}{(r-r_0)^2}
\left[\lim_{\gamma\downarrow0}\frac{-2\operatorname{Im}\lambda_\pm(r,\gamma)}{\gamma}\right]
=\frac{L^2b^2}{2\sum_{h=1}^N\sin^2(hk_0)}>0.
\]
The order of limits is part of the assertion; no uniform two-parameter approximation is claimed.

## Assumptions and scope
All hopping amplitudes are real and strictly positive and the chain is **open**, with \(2N\) sites ordered \(A_1,B_1,\ldots,A_N,B_N\). The one-body Hermitian matrix \(H(r)\) has unit hopping on every \(A_j\leftrightarrow B_j\), hopping \(r\) on every \(B_j\leftrightarrow A_{j+1}\), zero onsite terms, and no other links. The second-quantized Hamiltonian is \(\widehat H=\sum_{u,v}H(r)_{uv}c_u^\dagger c_v\). The dissipative generator acts as
\[
\mathcal L(\rho)=-i[\widehat H,\rho]+\gamma\left(c_{A_m}\rho c_{A_m}^\dagger-\tfrac12\{c_{A_m}^\dagger c_{A_m},\rho\}\right).
\]
The fermions are spinless with the usual canonical anticommutation relations. The statement concerns exact finite-chain modes for all \(N\ge2\), \(m\in\{1,\ldots,N\}\), \(r>0\), and \(\gamma>0\), not a thermodynamic-limit phase transition. The \(B_m\) statement follows by reflection. The near-resonance coefficient concerns only specified simple branches and the iterated limit written above.

## Proof
**1. Normal-mode recurrence.** An eigenvector with energy \(E\) has components \((a_j,b_j)\) satisfying \(Ea_j=b_j+r b_{j-1}\) and \(Eb_j=a_j+r a_{j+1}\), with \(b_0=a_{N+1}=0\). The off-diagonal block linking the sublattices is triangular with all diagonal entries \(1\), so \(H(r)\) is invertible and \(E\ne0\). Eliminating the \(b_j\) gives
\[
E^2a_j=(1+r^2)a_j+r(a_{j-1}+a_{j+1}),
\quad a_0=-r a_1,\quad a_{N+1}=0.
\]
For \(E^2=1+r^2+2r\cos k\), the right boundary enforces \(a_j=C\sin((N+1-j)k)\) whenever \(\sin k\ne0\), and the left boundary becomes \(F(k,r)=0\). For \(|\cos k|>1\) the right-boundary solution is hyperbolic or alternating hyperbolic and has no internal zero. At \(\cos k=\pm1\) the nontrivial right-boundary solution is an alternating or ordinary nonzero multiple of \(N+1-j\), likewise without internal zeros. Thus a zero at \(A_m\) forces a real canonical \(k\in(0,\pi)\).

**2. Exact finite resonance set.** If \(a_m=0\), then \(\sin(Lk)=0\), hence \(k=\pi j/L\) for an integer \(1\le j<L\). Since \(N+1=L+m\) and \(N=L+m-1\), substituting in \(F(k,r)=0\) yields
\[
\sin(mk)+r\sin((m-1)k)=0.
\]
The denominator \(\sin((m-1)k)\) cannot vanish at a solution: simultaneous vanishing of \(\sin(mk)\) and \(\sin((m-1)k)\) would force \(\sin k=0\). Hence precisely the positive ratios in \(\mathcal R_{N,m}\) occur. Conversely, for each listed index define \(E=\pm\sqrt{1+r^2+2r\cos k}\), \(a_j=\sin((N+1-j)k)\), and \(b_j=(a_j+r a_{j+1})/E\). This explicitly constructs two dark eigenvectors. The real symmetric irreducible tridiagonal matrix \(H(r)\) has simple spectrum by the nonvanishing-hop recurrence, and distinct \(k\in(0,\pi)\) have distinct positive energies. This proves the exact count. Sines at rational multiples of \(\pi\) are algebraic; finiteness and the endpoint cases follow at once. The chain's reflection symmetry maps \(B_m\) to \(A_{N+1-m}\).

**3. Loss and vacuum attraction.** Put \(K=-iH(r)-\gamma |A_m\rangle\langle A_m|/2\). Every eigenpair \(Kv=zv\) obeys
\[
\operatorname{Re}z=-\frac{\gamma}{2}\frac{|v_{A_m}|^2}{\|v\|^2}\le0.
\]
Equality holds exactly when \(v_{A_m}=0\), in which case \(v\) is a clean eigenvector and hence a dark orbital. If there are no dark orbitals, every eigenvalue of the finite matrix \(K\) has negative real part and \(e^{tK}\to0\), even if \(K\) is defective. For the number-conserving quadratic Hamiltonian and annihilation-only jump, the single-particle correlation matrix evolves as \(C(t)=e^{tK}C(0)e^{tK^\dagger}\). Consequently \(\langle\widehat N\rangle_t=\operatorname{Tr}C(t)\to0\). Since the projection onto nonvacuum states is bounded by \(\widehat N\), the full density matrix converges in trace norm to the vacuum. Conversely, each clean dark orbital defines a fermionic creation operator commuting with the loss annihilator; a Fock occupation configuration of any subset of the \(q\) dark energy orbitals is annihilated by the jump and is an eigenvector of \(\widehat H\). These \(2^q\) mutually orthogonal pure states are stationary, and their span is noiseless under the dynamics.

**4. Quadratic opening and coefficient.** For any resonance index, \(F(k_0,r_0)=0\). Its derivative in \(k\) is nonzero because it parametrizes a simple eigenvalue of the irreducible Jacobi matrix at an interior Bloch phase, and \(\partial_rF=\sin(Nk_0)\ne0\). The implicit function theorem gives \(k'(r_0)=b\ne0\). The normalized clean orbital on the \(A\)-sublattice has amplitude
\[
\phi_{A_m}(r)=\frac{\sin(Lk(r))}{\sqrt{2\sum_{h=1}^N\sin^2(hk(r))}},
\]
where the factor \(2\) follows from chiral symmetry and equality of the squared \(A\)- and \(B\)-sublattice norms for nonzero \(E\). Therefore
\[
|\phi_{A_m}(r)|^2=\frac{L^2b^2}{2\sum_{h=1}^N\sin^2(hk_0)}(r-r_0)^2+O((r-r_0)^3).
\]
First-order analytic perturbation in \(\gamma\) of the simple Hermitian eigenvalue gives \(-2\operatorname{Im}\lambda_\pm(r,\gamma)/\gamma\to |\phi_{A_m}(r)|^2\) at each fixed nearby \(r\). Taking the limits in the stated order proves the coefficient for both particle-hole partners.

**5. Nonuniform coexistence example.** For \(N=14,m=3,L=12\), the indices \(j=5\) and \(j=11\) both give \(-\sin(3\pi j/12)/\sin(2\pi j/12)=\sqrt2\); direct finite checking of the ten remaining indices shows none other has this ratio. Their distinct positive energies are \(\sqrt{3+2\sqrt2\cos(5\pi/12)}\) and \(\sqrt{3+2\sqrt2\cos(11\pi/12)}\). Each has a negative partner, giving exactly four dark orbitals and a \(16\)-dimensional dark Fock sector.

## Verification
The standalone script `verification/check.py` constructs the matrices independently from their alternating bonds; checks the trigonometric construction against direct real-symmetric eigensolvers across a finite grid of \(N,m\); checks reflection; verifies the uniform-chain greatest-common-divisor benchmark; verifies the nonuniform \(\sqrt2\) coexistence example under actual lossy evolution; and compares the explicit quadratic coefficient with nearby clean eigenvector weights. Run using `python verification/check.py` after installing `verification/requirements.txt`. Finite calculations corroborate rather than replace the infinite family of analytic arguments above.

## Relationship to prior work
Wang and Zhang (arXiv:2607.10218v1, 2026) establish the rank-one non-Hermitian reduction, weak-loss local-weight rule, exceptional-point behavior and Zeno scaling for a single-site lossy SSH chain. They mention exact nodal modes at special commensurabilities. The present claim is the explicit complete algebraic set of all such positive hopping ratios at arbitrary finite chain size and loss site, the exact number of undamped particle-hole modes, the resulting vacuum-attraction criterion, and the sharp weak-loss quadratic detuning coefficient. The general implication from zero site amplitude to a dark mode is not asserted to be new.

Yang, Molignini and Bergholtz (arXiv:2305.00031; Phys. Rev. Research 5, 043229, 2023) derive dissipative boundary-state preparation using nodal sublattice modes, particularly the odd-site-chain topological boundary mode. That construction is distinct from the positive-ratio resonances of bulk modes on even-site SSH chains classified here. General Jacobi recurrence and spectral simplicity are established mathematical ingredients, not claimed as innovations.

## Limitations
All results are for finite, noninteracting, spinless fermions, strictly positive alternating hoppings, one loss site and no gain or dephasing. The stationary-state count is a guaranteed collection of mutually orthogonal stationary states, not an enumeration of all stationary density matrices. The quadratic coefficient is for the ordered limits of weak loss followed by coupling detuning and is not a uniform approximation for simultaneously varying parameters. The formulas do not establish robustness to arbitrary static disorder; generically, exact dark modes disappear off the discrete ratios. Broad generalizations of Jacobi nodal observability could imply portions of the criterion; literature-wide priority is not independently certified.

## References
1. Y. T. Wang and X. Z. Zhang, *From local weight selection to Zeno slowdown in an open Su-Schrieffer-Heeger chain with a single local loss*, arXiv:2607.10218v1 (11 July 2026); Phys. Rev. A **114**, 012457 (2026), DOI 10.1103/99h3-p7rj.
2. F. Yang, P. Molignini and E. J. Bergholtz, *Dissipative boundary state preparation*, arXiv:2305.00031; Phys. Rev. Research **5**, 043229 (2023), DOI 10.1103/PhysRevResearch.5.043229.
3. T. Prosen, *Third quantization: a general method to solve master equations for quadratic open Fermi systems*, New J. Phys. **10**, 043026 (2008), cited as standard quadratic-Lindbladian background.
