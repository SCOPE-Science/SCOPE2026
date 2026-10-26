# Chiral protection versus tuned pairwise dark resonances in odd alternating quantum chains

## Finding

Let \(m\ge2\), \(a,b,\gamma>0\), and \(N=2m+1\). On an open quantum chain with vertices \(1,\dots,N\), the Hermitian hopping matrix \(H\) has zero diagonal, and positive edge weights alternating \(a,b,a,b,\dots,a,b\). Add a single absorbing site \(s\) through \(H_{\mathrm{eff}}=H-i\gamma |s\rangle\langle s|/2\). Starting from \(|1\rangle\), define \(S_s=\lim_{t\to\infty}\|\exp(-itH_{\mathrm{eff}})|1\rangle\|^2\); let \(D_s\) be the dimension of the nondecaying subspace.

For the first three possible absorbing sites the complete classification is
\[
(D_1,S_1)=(0,0),\qquad
(D_2,S_2)=\left(1,\frac{1}{\sum_{j=0}^{m}(a/b)^{2j}}\right).
\]
For \(s=3\), there are exactly \(\lfloor m/2\rfloor\) admissible ratios at which survival is nonzero. Explicitly, for \(1\le k\le\lfloor m/2\rfloor\), set \(\theta_k=k\pi/(m+1)\). Then
\[
(D_3,S_3)=\begin{cases}
\left(2,\frac{2\sin^2\theta_k}{m+1}\right),&\text{if } b/a=2\cos\theta_k\text{ for some }k,\\
(0,0),&\text{otherwise}.
\end{cases}
\]
The two modes in each resonance have energies \(+a\) and \(-a\), whereas the persistent mode for the second-site sink is the zero-energy chiral mode. All statements, including the limiting probabilities, are independent of the positive absorption strength \(\gamma\).

## Assumptions and scope

The chain has exactly \(2m+1\) vertices, \(m\ge2\), nearest-neighbor real positive alternating couplings \(a\) between \((1,2),(3,4),\dots\), and \(b\) between \((2,3),(4,5),\dots\); no on-site potential; one rank-one absorbing sink at one of sites \(1,2,3\); and initial excitation \(|1\rangle\). The effective Hamiltonian is non-Hermitian and unnormalized: the squared norm gives survival before absorption. The dark subspace means the span of real-eigenvalue eigenmodes of \(H_{\mathrm{eff}}\). With \(a,b>0\), all eigenvalues of \(H\) are simple.

## Proof

**Dark-state reduction.** The dynamics obeys \(d\|\psi(t)\|^2/dt=-\gamma|\psi_s(t)|^2\). Taking the imaginary part of the eigenvalue equation for \(H_{\mathrm{eff}}\) shows that a real-energy mode must vanish at the sink, hence is an ordinary eigenvector of \(H\), and conversely. Every other eigenvalue lies strictly in the lower half-plane. Since the contraction semigroup has no nontrivial Jordan block on its nondecaying spectral subspace (otherwise polynomial growth would contradict contractivity), all other components decay and the surviving squared norm of \(|1\rangle\) is the orthogonal spectral projection of \(|1\rangle\) onto the normalized sink-nodal eigenvectors of the Hermitian \(H\).

**Boundary sinks.** An eigenvector of the Jacobi matrix with \(\psi_1=0\) must vanish everywhere by propagation through nonzero couplings. If \(\psi_2=0\), its first equation reads \(E\psi_1=0\). Because a nonzero eigenvector has \(\psi_1\ne0\), it follows that \(E=0\). For an odd chain there is exactly one zero mode, with amplitudes \(\psi_{2j}=0\) and \(\psi_{2j+1}=(-a/b)^j\psi_1\), \(0\le j\le m\). Normalizing yields the stated value of \(S_2\).

**Third-site sink.** Suppose \(\psi_3=0\). The first two Jacobi equations become \(E\psi_1=a\psi_2\) and \(E\psi_2=a\psi_1\). Thus any nonzero eigenvector has \(E=\pm a\). Chiral conjugation (multiplication by alternating \(+1,-1\) on consecutive vertices) exchanges these signs and preserves zeros and endpoint modulus. It therefore suffices to analyze \(E=a\). Set \(\psi_1=\psi_2=1\), \(r=b/a>0\), and \(x_\ell=\psi_{4+2\ell}\) for \(0\le\ell\le m-1\), with terminal \(x_{m-1}=\psi_{N+1}=0\). The first equations give \(x_0=-r\) and \(x_1=r^2-1\); eliminating the interleaved odd-site amplitudes gives \(x_{\ell+1}=-r x_\ell-x_{\ell-1}\). Consequently \(x_\ell=(-1)^{\ell+1}U_{\ell+1}(r/2)\), for Chebyshev polynomials \(U_j\) of the second kind. A nonzero solution satisfies the terminal condition exactly when \(U_m(r/2)=0\). Its positive roots are \(r=2\cos(k\pi/(m+1))\), with \(1\le k\le\lfloor m/2\rfloor\). Distinct \(k\) yield distinct positive ratios. No other energies or ratios can produce a third-site dark mode.

**Normalization.** Let \(\theta=k\pi/(m+1)\) and choose the positive-energy eigenvector with \(\psi_1=\psi_2=1\). The recurrence solution and the intermediate Jacobi equations give, up to irrelevant alternating signs, the remaining nonzero amplitudes \(\psi_{4+2\ell}=\sin((m-1-\ell)\theta)/\sin\theta\) and \(\psi_{5+2\ell}=\sin((m-\ell)\theta)/\sin\theta\) for \(0\le\ell\le m-2\), with all other entries specified by the equations. The trigonometric identity \(\sum_{j=1}^{m}\sin^2(j\theta)=(m+1)/2\) shows that the total squared norm is \((m+1)/\sin^2\theta\). Thus the normalized squared amplitude at site \(1\) is \(\sin^2\theta/(m+1)\). The opposite-energy chiral partner has the same overlap; summing them yields the stated \(S_3\) and \(D_3=2\). The two energies are distinct because \(a>0\). This concludes the proof.

## Verification

The included script `verify_odd_ssh.py` constructs the original Hermitian alternating hopping matrices and diagonalizes them independently for \(2\le m\le11\), checks all predicted positive resonances, the endpoint and second-site rules, detuned nonresonant cases, normalized survival overlaps, and Chebyshev recurrence identities. Running it with the package dependencies produced: `PASS: 111 checks of spectral dark ranks, overlap probabilities, off-resonance absence, and exact Chebyshev identities`. The all-\(m\) result follows from the algebraic proof; finite computations are corroborative only.

## Relationship to prior work

The SSH alternating-hopping lattice and its protected zero modes are established subjects, as in Li–Xu–Chen (2013). The invariant-subspace/dark-state method for quantum trapping is standard, including Novo and colleagues (2014). Zhu–Lu–Chen (2014) examine an even-length chain with balanced gain and loss at boundaries. Wang–Zhang (2026) study an even-length SSH chain with a single local loss and a general Chebyshev secular formula, closely related in technique, but the inspected results neither contain an odd-length chain nor the present three-site classification and explicit resonance-survival expression. Therefore neither topological edge states nor the generic dark-state method are claimed new; the focus is the exact odd-chain three-site, first-end-initialized resonance dichotomy. A more general previous theorem might imply the statement, so historical priority remains qualified.

## Limitations

The findings concern strictly positive real hopping magnitudes, odd finite chains, a single absorber at one of the first three sites and initial excitation at the left endpoint. They do not classify simultaneous sinks, disordered hoppings, even-chain topological behavior, general loss positions, finite-time decay, or the noncommuting limits of large length and small detuning. The isolated positive-ratio resonances are exact equalities, not stable finite-width plateaus. No independent scientific validation has been performed.

## References

- Li, Xu, Chen, *Topological phases of generalized Su-Schrieffer-Heeger models*, arXiv:1309.4558 (first publicly posted 2013-09-18).
- Zhu, Lu, Chen, *PT-Symmetry in Non-Hermitian Su-Schrieffer-Heeger model with complex boundary potentials*, arXiv:1405.5591 (first publicly posted 2014-05-22).
- Novo et al., *Systematic Dimensionality Reduction for Quantum Walks*, arXiv:1412.7209 (first publicly posted 2014-12-22).
- Wang and Zhang, *From local weight selection to Zeno slowdown in an open Su-Schrieffer-Heeger chain with a single local loss*, arXiv:2607.10218 (first publicly posted 2026-07-11); later comparison literature, not the archival motivating source.
