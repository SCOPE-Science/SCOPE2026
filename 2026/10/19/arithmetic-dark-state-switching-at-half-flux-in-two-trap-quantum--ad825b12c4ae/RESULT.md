# Arithmetic dark-state switching at half flux in two-trap quantum cycles

## Finding

Let \(N\ge3\), \(1\le d<N\), \(h\in\mathbb R\setminus\{0\}\), and \(\kappa_0,\kappa_d>0\). On the one-particle Hilbert space of the cycle \(\mathbb Z/N\mathbb Z\), let \(S|j\rangle=|j+1\pmod N\rangle\), and put
\[
H_\Phi=h\bigl(e^{i\Phi/N}S+e^{-i\Phi/N}S^\dagger\bigr),\qquad
K_\Phi=H_\Phi-\frac{i}{2}\bigl(\kappa_0|0\rangle\langle0|+\kappa_d|d\rangle\langle d|\bigr).
\]
Define \(\mathcal D\) as the span of eigenvectors of \(H_\Phi\) whose components at both \(0\) and \(d\) vanish; equivalently, it is the subspace on which \(e^{-iK_\Phi t}\) is norm preserving. Write \(g=\gcd(N,d)\) and \(M=N/g\).

**Theorem.** At every flux not congruent to \(0\) or \(\pi\) modulo \(2\pi\), \(\dim\mathcal D=0\). If \(\Phi\equiv m\pi\pmod{2\pi}\), \(m\in\{0,1\}\), put
\[
C_m=\begin{cases}g\gcd(2,M),&\gcd(2,M)\mid m,\\0,&\text{otherwise},\end{cases}\qquad
S_m=\begin{cases}\gcd(2,N),&\gcd(2,N)\mid m,\\0,&\text{otherwise}.\end{cases}
\]
Then the exact dark-subspace dimension is
\[
\boxed{\dim\mathcal D=\frac{C_m-S_m}{2}.}
\]
In particular, for even \(N\) the two distinguished fluxes obey
\[
\begin{array}{c|cc}
&\Phi=0&\Phi=\pi\\\hline
M\ \text{odd}&(g-2)/2&g/2\\
M\ \text{even}&g-1&0.
\end{array}
\]
For odd \(N\), both fluxes instead have \(\dim\mathcal D=(g-1)/2\). Thus an even cycle with \(M\) odd acquires exactly one additional dark mode upon threading half a flux quantum; when \(M\) is even all its zero-flux dark modes disappear at half flux. For example, \(N=6,d=2\) switches from zero dark modes to one.

For every density matrix \(\rho\), writing \(P_{\mathcal D}\) for the orthogonal dark projector, the no-jump survival satisfies
\[
\lim_{t\to\infty}\operatorname{Tr}\bigl(e^{-iK_\Phi t}\rho e^{iK_\Phi^\dagger t}\bigr)
=\operatorname{Tr}(P_{\mathcal D}\rho).
\]
For \(\rho=I/N\), the right side is \(\dim\mathcal D/N\), independent of both positive sink rates and the nonzero hopping amplitude. The asymptotic capture probability is its complement.

## Assumptions and scope

The ring has uniform nonzero *real* hopping magnitude on every bond and a *uniform* Peierls phase, representing a total Aharonov–Bohm flux \(\Phi\) modulo \(2\pi\). The two distinguished vertices \(0\) and \(d\) have strictly positive, possibly unequal, irreversible loss rates. These assumptions describe conditional no-jump one-particle evolution; other loss channels, site disorder, interactions, and dephasing are excluded. Flux is measured in radians, and \(\Phi=\pi\) represents half a flux quantum. The theorem is exact for all integers \(N,d\) in the stated ranges and for all real times tending to infinity.

## Proof

**1. Fourier eigenvalues and degeneracies.** Use the orthonormal plane waves \(u_k(j)=N^{-1/2}\exp(-2\pi i kj/N)\) for \(0\le k<N\). Since \(Su_k=\exp(2\pi i k/N)u_k\), they diagonalize the hopping Hamiltonian, with
\[
E_k=2h\cos\bigl((2\pi k+\Phi)/N\bigr).
\]
Two *distinct* frequencies \(k,\ell\) have the same energy precisely when \(k+\ell+\Phi/\pi\equiv0\pmod N\); this can occur only when \(\Phi/\pi\) is an integer. Because total flux is taken modulo \(2\pi\), the only special classes are \(0\) and \(\pi\). Away from those classes each eigenspace is one-dimensional, and its plane-wave eigenvector has nonzero amplitude at each vertex. Hence there are no dark eigenvectors at generic flux.

For \(\Phi=m\pi\), define the involution \(\iota_m(k)=-k-m\pmod N\). Its two-element orbits are exactly the doubly degenerate energy eigenspaces. A fixed point represents a simple eigenvalue. In a two-element orbit \(\{k,\ell\}\), the condition that a vector \(a u_k+b u_\ell\) vanish at vertex \(0\) forces \(b=-a\). This one-dimensional line additionally vanishes at \(d\) exactly when
\[
\exp(-2\pi i kd/N)=\exp(-2\pi i\ell d/N)
\quad\Longleftrightarrow\quad N\mid d(2k+m)
\quad\Longleftrightarrow\quad M\mid2k+m.
\]
The last equivalence uses \(\gcd(d/g,N/g)=1\). All such nonfixed orbits contribute one dimension, and no other orbit contributes.

**2. Exact congruence census.** The linear congruence \(2k+m\equiv0\pmod M\) has \(\gcd(2,M)\) residue solutions modulo \(M\) if \(\gcd(2,M)\mid m\), and none otherwise. Each lifts to precisely \(g\) residues modulo \(N\); thus there are exactly \(C_m\) indices meeting the two-sink cancellation condition. Among them, the involution's fixed points are precisely the solutions of \(2k+m\equiv0\pmod N\). Their number is \(S_m\) by the same congruence argument, and each is automatically among the \(C_m\) indices. Every remaining index belongs to a two-element orbit, so there are exactly \((C_m-S_m)/2\) dark eigendirections. Evaluating the greatest common divisors gives the displayed parity table, including all boundary cases.

**3. No hidden nondecaying directions.** Let \(\Gamma=\kappa_0|0\rangle\langle0|+\kappa_d|d\rangle\langle d|\). For any eigenpair \(K_\Phi v=zv\), taking imaginary parts of the scalar product gives
\[
2\operatorname{Im}(z)\|v\|^2=-\langle v,\Gamma v\rangle
=-\kappa_0|v(0)|^2-\kappa_d|v(d)|^2\le0.
\]
Equality holds if and only if \(v(0)=v(d)=0\), in which case \(K_\Phi v=H_\Phi v\) and \(v\in\mathcal D\). Since \(H_\Phi\) is Hermitian, its invariant subspace \(\mathcal D\) is reducing. Also \(\Gamma\mathcal D=0\), so \(\mathcal D^\perp\) is invariant under both \(H_\Phi\) and \(\Gamma\), and hence under \(K_\Phi\). The restriction of \(K_\Phi\) to \(\mathcal D^\perp\) has no real eigenvalue; all its eigenvalues have negative imaginary part. Its finite-dimensional matrix exponential therefore decays to zero even when its Jordan form is not diagonal. On \(\mathcal D\), \(e^{-iK_\Phi t}=e^{-iH_\Phi t}\) is unitary. Orthogonality then yields the asserted asymptotic trace for every \(\rho\).

## Verification

The included standalone script `verification/check_cycle.py` implements the integer formula, enumerates the qualifying congruence classes independently, and independently computes the nullities of the two-sink evaluation map restricted to each Fourier energy eigenspace. It passed 5,307 spectral comparisons for every \(3\le N\le60\), every \(1\le d<N\), and fluxes \(0\), \(\pi\), and a generic nonresonant value. Integer congruence checks passed for all \(3\le N\le120\), both special fluxes, and all sink separations. Finally, direct non-Hermitian time evolution at eight representative geometries approached the exact mixed-state survival values. These finite calculations are reproducibility checks only; the proof above establishes all sizes and the exact infinite-time limit.

To reproduce in an environment with Python 3, NumPy, and SciPy installed, run `python verification/check_cycle.py`. The script prints its checks and exits with an assertion if any comparison fails. No external datasets are required.

## Relationship to prior work

Parlangeli and Notarstefano [1, Theorem 4.10 and Lemma 4.9] already give a general number-theoretic characterization of *unweighted, zero-flux* cycle observability from selected vertices, including two observers. Their zero-flux unobservable subspace is the appropriate mathematical baseline; the \(\Phi=0\) portion of the formula above is **not** claimed as an independent novelty. In particular, the exact two-observer arithmetic absence criterion at zero flux follows from that older work. The present theorem determines instead the full magnetic-flux dark-space census and the half-flux parity reversal in a two-loss quantum cycle. The negative part of the claim (generic-flux absence of dark states) follows directly from the lifted spectral degeneracy analysis; half-flux admits new paired modes not covered by a gauge reduction to the ordinary unweighted cycle when its signed loop is unbalanced.

Kassal and Aspuru-Guzik [2, Section 3] treat transport on a quantum cycle and Fourier-mode interference with a **single** trapping vertex and without the magnetic two-trap parameter family. Wang and collaborators [3, Sections 2–5] develop a related flux-threaded ring Hamiltonian, but their explicit dark-state calculations concern three- and four-dot devices with a source and a drain, not the stated all-size two-loss census. Razzoli, Paris and Bordone [4, Sections 2–4] give the general Krylov/trapping-subspace method, rather than this flux-and-separation gcd formula. Liu and Ji [5] derive dimensions for unweighted cycle controllable subspaces, again without Peierls flux. Generic results about observability or non-Hermitian damping supply methodology but do not, on their own, specify the parity-dependent two-sink magnetic ranks.

## Limitations

This is an exact result only for a single particle on a homogeneous ring with the two stated absorbers. Finite-time capture can be slow as flux approaches \(0\) or \(\pi\): the generic-flux zero-survival conclusion does not provide a uniform-in-flux decay estimate, and the long-time and small-flux limits need not commute. Arbitrary static disorder, nonuniform bond strengths, additional jumps, dephasing, and interacting-particle sectors are not covered. The relationship with all published signed-cycle observability results cannot be declared exhaustive; a specialized pre-existing flux formula may still exist outside the searched literature.

## References

[1] G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556 (first public version 16 September 2011), especially §IV.B, Lemma 4.9 and Theorem 4.10. https://arxiv.org/abs/1109.3556

[2] I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202 (first public version 25 January 2012), especially §3. https://arxiv.org/abs/1201.5202

[3] Q. Wang, J. Liu, N. Tang, and H.-S. Zeng, *Dark states and Aharonov–Bohm oscillations in multi-quantum-dot systems*, Chinese Physics B **20** (2011), 020303, DOI:10.1088/1674-1056/20/2/020303.

[4] L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794, especially §§2–4. https://arxiv.org/abs/2011.13794

[5] X. Liu and Z. Ji, *Controllability of multiagent systems based on path and cycle graphs*, International Journal of Robust and Nonlinear Control **28** (2018), 296–309; first published 30 June 2017, DOI:10.1002/rnc.3870.
