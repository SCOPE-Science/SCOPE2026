# Magnetic-flux singularities of quantum-walk Krylov spreading on finite cycles

## Finding

For every integer \(N\ge3\), consider a single particle hopping on the cycle \(\mathbb Z/N\mathbb Z\) with total Peierls flux \(\phi\). Its initial state is a single localized vertex, and the spread complexity uses the Lanczos/Krylov basis rooted at that vertex, with weight equal to the zero-based Krylov index. Define the Cesàro long-time average \(\overline{\mathcal C}_{N}(\phi)\) below. It obeys the *complete flux/parity law*

\[
\boxed{
\overline{\mathcal C}_{N}(\phi)=
\begin{cases}
 (N-1)/2,&\phi\not\equiv0,\pi\pmod{2\pi},\\[2pt]
 N/4,&\phi\equiv0\pmod{2\pi},\quad N\text{ even},\\[2pt]
 (N-2)/4,&\phi\equiv\pi\pmod{2\pi},\quad N\text{ even},\\[2pt]
 (N-1)(N^2-1)/(4N^2),&\phi\equiv0\text{ or }\pi\pmod{2\pi},\quad N\text{ odd}.
\end{cases}}
\]

At generic flux the asymptotic Krylov-index distribution is **exactly uniform on all \(N\) indices**. At zero and half flux, spectral degeneracies reduce the rooted cyclic-space dimension and change both the distribution and the mean, sharply and nonperturbatively. In particular the infinite-time mean has a discontinuity at each of the two time-reversal-invariant fluxes, although the complexity at each fixed finite time is a continuous function of flux. Hence the infinite-time and zero-flux-detuning limits do not commute.

## Assumptions and scope

Fix \(N\in\mathbb Z\), \(N\ge3\), a hopping constant \(J>0\), and \(\phi\in\mathbb R\) modulo \(2\pi\). On \(\mathcal H=\mathbb C^N\) with periodic orthonormal site kets \(\{|x\rangle\}_{x\in\mathbb Z/N\mathbb Z}\), let

\[
H_\phi=J\sum_{x=0}^{N-1}
\left(e^{i\phi/N}|x+1\rangle\langle x|
+e^{-i\phi/N}|x\rangle\langle x+1|\right).
\]

The two contributions are separate hopping orientations even for \(N=3\); the Hamiltonian is Hermitian. The initial state is \(\psi_0=|0\rangle\). Let \(K_0,K_1,\ldots,K_{d-1}\) be the orthonormal basis obtained by *exact* Lanczos tridiagonalization of the cyclic space \(\mathrm{span}\{H_\phi^j\psi_0:j\ge0\}\), in order, with \(K_0=\psi_0\) and \(d\) its dimension. Define

\[
p_j(t;\phi)=|\langle K_j,e^{-itH_\phi}\psi_0\rangle|^2,\qquad
\mathcal C_N(t;\phi)=\sum_{j=0}^{d-1} j\,p_j(t;\phi),
\]

\[
\overline p_j(\phi)=\lim_{T\to\infty}\frac1T\int_0^T p_j(t;\phi)\,dt,
\qquad
\overline{\mathcal C}_N(\phi)=\sum_{j=0}^{d-1}j\,\overline p_j(\phi).
\]

No ensemble averaging, disorder, measurement or nonunitary loss is assumed. The limits exist for every fixed \(N,\phi\) because the system is finite-dimensional; no convergence rate uniform in \(\phi\) is asserted. The value is independent of \(J>0\) because positive energy rescaling does not change either the spectral eigenspaces or the Cesàro projector.

The *complete* averaged populations and rooted cyclic dimensions are as follows, with indexing from \(j=0\):

- Generic \(\phi\not\equiv0,\pi\): \(d=N\) and \(\overline p_j=1/N\) for all \(0\le j<N\).
- Zero flux, even \(N=2m\): \(d=m+1\), \(\overline p_0=\overline p_m=2(N-1)/N^2\), and \(\overline p_j=2(N-2)/N^2\) for \(1\le j<m\).
- Half flux, even \(N=2m\): \(d=m\), and \(\overline p_j=2/N\) for every \(0\le j<m\).
- Zero *or* half flux, odd \(N=2m+1\): \(d=m+1\), \(\overline p_0=(2N-1)/N^2\), and \(\overline p_j=2(N-1)/N^2\) for \(1\le j\le m\).

## Proof

**Step 1: Fourier spectrum and degeneracy classification.** For \(k\in\mathbb Z/N\mathbb Z\), Fourier plane waves diagonalize \(H_\phi\) with eigenvalues (up to the harmless convention of the Fourier orientation)

\[
E_k=2J\cos\!\left(\frac{2\pi k+\phi}{N}\right).
\]

Each Fourier eigenvector has squared overlap \(1/N\) with \(|0\rangle\). Distinct modes \(k,\ell\) share an eigenvalue precisely when \(k+\ell+\phi/\pi\) is a multiple of \(N\). This follows from \(\cos a=\cos b\), using the nontrivial \(a\equiv-b\pmod{2\pi}\) branch; the trivial branch fixes \(k=\ell\). Consequently all eigenvalues are simple if \(\phi\not\equiv0,\pi\pmod{2\pi}\); at zero flux modes pair as \(k\leftrightarrow-k\), and at half flux they pair as \(k\leftrightarrow-1-k\). Even \(N\) has two fixed modes at zero flux and none at half flux. Odd \(N\) has one fixed mode in either case. Since the seed has a nonzero projection onto each distinct eigenspace, the cyclic dimension equals their number, giving the four stated values of \(d\).

**Step 2: Uniform dephasing with equal spectral weights.** Let \(P_\lambda\) be the orthogonal eigenspace projector at each *distinct* energy. The finite-dimensional Cesàro dephasing identity is

\[
\overline\rho_\phi:=\lim_{T\to\infty}\frac1T\int_0^T
 e^{-itH_\phi}|0\rangle\langle0|e^{itH_\phi}\,dt
 =\sum_\lambda P_\lambda|0\rangle\langle0|P_\lambda.
\]

Write \(w_\lambda=\|P_\lambda|0\rangle\|^2\) and \(e_\lambda=P_\lambda|0\rangle/\sqrt{w_\lambda}\); these are the mutually orthogonal energy eigenvectors spanning the rooted cyclic space. Their weights are \(w_\lambda=g_\lambda/N\), where \(g_\lambda\) is the number of Fourier modes in the energy eigenspace. Hence \(\overline\rho_\phi=\sum_\lambda w_\lambda|e_\lambda\rangle\langle e_\lambda|\). At generic flux every \(g_\lambda=1\), so \(\overline\rho_\phi=I_{\mathcal H}/N\) and \(\overline p_j=1/N\) in *any* orthonormal basis. At half flux and even \(N\), every \(g_\lambda=2\), giving \(\overline\rho_\phi=I_{\mathrm{cyc}}/m\) and \(\overline p_j=1/m=2/N\). Their asserted means follow by summing \(j\).

**Step 3: Zero flux and the exact root Krylov basis.** Reflection about the initial vertex commutes with \(H_0\), and \(H_0\) acts on reflection-symmetric shell kets as the Jacobi operator of a finite path. With positive hopping \(J\), its positive-coefficient Lanczos basis is exactly

\[
K_0=|0\rangle,\qquad
K_j=\frac{|j\rangle+|N-j\rangle}{\sqrt2}
\quad(1\le j< N/2),
\]

with the additional terminal singleton \(K_m=|m\rangle\) for \(N=2m\). The notation \(j<N/2\) includes \(j=m\) for odd \(N=2m+1\) and excludes the antipode in even dimension. The norm-squared spectral overlap with the zero-mode Fourier vector is \(1/N\) for each singleton shell and \(2/N\) for paired shells. For each distinct nonfixed \(k\), its normalized cosine eigenvector has \(w_k=2/N\), and its amplitude on a paired shell \(j\) has squared modulus

\[
|\langle K_j,e_k\rangle|^2=\frac4N
\cos^2\!\left(\frac{2\pi k j}{N}\right).
\]

For odd \(N=2m+1\), the finite trigonometric identity

\[
\sum_{k=1}^{m}\cos^2\!\left(\frac{2\pi kj}{N}\right)
=\frac{N-2}{4},\qquad 1\le j\le m,
\]

and the singleton \(k=0\) contribution yield \(\overline p_j=2(N-1)/N^2\) for \(j\ge1\), whereas \(\overline p_0=(2N-1)/N^2\). For even \(N=2m\), the cosine sum over the paired modes is

\[
\sum_{k=1}^{m-1}\cos^2\!\left(\frac{\pi kj}{m}\right)
=\frac{m-2}{2},\qquad 1\le j<m.
\]

Together with the two fixed Fourier modes \(k=0,m\), this gives \(\overline p_j=2(N-2)/N^2\) on interior shells, and the singleton endpoints give \(\overline p_0=\overline p_m=2(N-1)/N^2\). The cosine identities follow by writing \(2\cos^2\theta=1+\cos2\theta\) and evaluating the corresponding finite geometric series. Weighted arithmetic sums of \(j\) prove the two zero-flux values.

**Step 4: Odd half flux.** For odd \(N\), changing the sign of every edge coupling changes the total loop flux by \(N\pi\equiv\pi\pmod{2\pi}\). Thus \(H_\pi\) is related to \(-H_0\) by a diagonal unitary gauge transformation, and the transformation fixes the initial vertex up to a phase. Multiplication by \(-1\) and such a gauge transformation leave every Krylov-index population unchanged (the Lanczos vectors acquire at most phases). Hence \(\overline p_j(\pi)=\overline p_j(0)\) for odd \(N\). This exhausts all \(N\) and \(\phi\).

**Step 5: The noncommuting limits.** The piecewise values give strictly positive jumps, since for every \(N\ge3\) the generic mean \((N-1)/2\) exceeds either exceptional mean. Yet for any fixed finite \(t\), \(\mathcal C_N(t;\phi)\) is continuous at exceptional flux. Indeed, as \(\phi\to\phi_*\), the first \(d_*\) Lanczos vectors converge to the corresponding \(d_*\) Krylov vectors at the exceptional flux \(\phi_*\), because their norm-positive Gram–Schmidt steps remain nonsingular. The span of those vectors thus converges to the entire exceptional cyclic subspace; unitarity and the continuity of \(e^{-itH_\phi}|0\rangle\) imply that the total weight in any additional Krylov vectors tends to zero. All Krylov indices are bounded by \(N-1\), so the weighted sum converges as well. At any exceptional flux \(\phi_*\), therefore,

\[
\lim_{\substack{\phi\to\phi_*\\\phi\ne\phi_*}}\lim_{T\to\infty}
\frac1T\int_0^T\mathcal C_N(t;\phi)\,dt
=\frac{N-1}{2}
\ne
\lim_{T\to\infty}\frac1T\int_0^T\mathcal C_N(t;\phi_*)\,dt.
\]

## Verification

The companion standalone `verify_flux_cycle.py` uses only the Python standard library. It independently reconstructs orthogonal polynomials on the *actual distinct Fourier spectral support*, obtains the averaged Krylov populations from the spectral weights without substituting the claimed populations, and checks the formulas for \(3\le N\le27\) at two nonexceptional fluxes and both exceptional fluxes. It also checks exact rational sum and mean identities through \(N=149\) and independently approximates the time integral of the evolved amplitudes on smaller cycles. The script reports 1,300 finite checks passing. These tests are bounded diagnostics; the proof for arbitrary \(N\) and the exact infinite-time average is given above.

For illustration, \(N=6\) yields \(\overline{\mathcal C}_6=5/2\) at generic flux, \(3/2\) at zero flux, and \(1\) at half flux. The corresponding cyclic-space dimensions are \(6\), \(4\), and \(3\).

Reproduce with `python3 verify_flux_cycle.py`. No external package or downloaded table is needed.

## Relationship to prior work

B. Jeevanesan, *Krylov Spread Complexity of Quantum-Walks* (arXiv:2401.00526v1, publicly posted 2023-12-31), defines the same Krylov-index observable, establishes its long-time spectral-measure framework, and analyzes paths, complete graphs, hubs and trees. The specific magnetic-cycle phase/parity law, its averaged Krylov-index distributions and its flux-limit discontinuities are distinct from the graph examples computed there.

A. Adamczak and collaborators, *Non-uniform mixing of quantum walk on cycles* (arXiv:0708.2096), study long-time **vertex** measurement probabilities on unthreaded rings. Vertex mixing and Krylov-index mixing are different observables except for specific bases; degeneracy can obstruct uniform *vertex* mixing even when the Krylov-index distribution is uniform. P. Luppi, *Flux control of measurement back-action and Leggett–Garg correlations in chiral quantum walks* (arXiv:2608.12519), uses flux-threaded cycles and their rooted Fourier spectra to study return and sequential-measurement correlations rather than the long-time averaged *spread complexity*. The present exact classification builds on standard spectral dephasing and finite-cycle Fourier analysis, not on a claimed new dephasing principle.

## Limitations

The theorem is for one localized initial vertex, homogeneous nearest-neighbor hopping, a single finite cycle, an exactly unitary evolution and the **Cesàro** infinite-time average. It does not assert uniformity of the *spatial* vertex distribution, a finite-time flux-discontinuity, a flux-uniform convergence rate, an analogous result with disorder, or universality on multicycle graphs. The order of the infinite-time and zero-detuning limits is essential. A separate scientific priority comparison against all possible consequences of the large literature on finite orthogonal-polynomial spectra has not been independently audited.

## References

1. B. Jeevanesan, *Krylov Spread Complexity of Quantum-Walks*, arXiv:2401.00526v1 (2023-12-31). https://arxiv.org/html/2401.00526v1
2. A. Adamczak et al., *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096 (2007). https://arxiv.org/abs/0708.2096
3. P. Luppi, *Flux control of measurement back-action and Leggett–Garg correlations in chiral quantum walks*, arXiv:2608.12519 (2026). https://arxiv.org/abs/2608.12519
4. V. Balasubramanian, P. Caputa, J. M. Magán and Q. Wu, *Quantum chaos and the complexity of spread of states*, arXiv:2202.06957 (2022). https://arxiv.org/abs/2202.06957
