# Sharp parity-dependent magnetic-flux design for quantum-ring dephasing

## Finding

Fix an integer \(N\geq 3\), hopping magnitude \(J>0\), and total magnetic flux \(\Phi\in\mathbb R/(2\pi\mathbb Z)\). For the nearest-neighbor Hermitian tight-binding ring
\[
H_\Phi=J\sum_{x\in\mathbb Z/N\mathbb Z}\left(e^{i\Phi/N}|x+1\rangle\langle x|+e^{-i\Phi/N}|x\rangle\langle x+1|\right),
\]
let \(\Delta_N(\Phi)\) be the smallest absolute difference between distinct *indexed* Fourier energy levels. Repeated energy levels therefore give \(\Delta_N=0\).

**Theorem (sharp all-size flux optimization).** With \(\alpha=\pi/N\), the global maximum of this smallest Bohr frequency is, for odd \(N\),
\[
\max_\Phi\Delta_N(\Phi)=4J\sin\alpha\sin(\alpha/2),
\qquad \Phi\equiv\pi/2,\ 3\pi/2\pmod{2\pi},
\]
and, for even \(N\),
\[
\theta_*=\arctan\!\left(\frac{\tan\alpha}{3}\right),\qquad
\max_\Phi\Delta_N(\Phi)=4J\sin(2\alpha)\sin\theta_*
=\frac{8J\sin^2\alpha}{\sqrt{9+\tan^2\alpha}},
\]
with exactly the two maximizers \(\Phi\equiv N\theta_*\) and \(\Phi\equiv2\pi-N\theta_*\pmod{2\pi}\). All stated maximizers are distinct and all spectra there are simple.

For any nondegenerate flux, define the channel on \(N\times N\) complex matrices
\[
\mathcal C_T^\Phi(A)=\frac1T\int_0^T e^{-itH_\Phi}A e^{itH_\Phi}\,dt,
\qquad
\mathcal D(A)=\sum_{k=0}^{N-1}P_kAP_k,
\]
where \(P_k\) is the rank-one Fourier spectral projector; \(\mathcal D\) is independent of flux at nondegenerate phases. The following sharp long-time convergence coefficient holds in the induced Hilbert--Schmidt operator norm:
\[
\limsup_{T\to\infty}T\|\mathcal C_T^\Phi-\mathcal D\|_{2\to2}
=\frac2{\Delta_N(\Phi)}.
\]
Consequently exactly the displayed parity-dependent fluxes uniquely minimize this asymptotic error envelope, over all nondegenerate fluxes. At each optimal flux the coefficient is \(2/\max_\Phi\Delta_N(\Phi)\).

The optimal flux has an enduring parity signature:
\[
\Phi_{\mathrm{odd}}\equiv\pi/2,\qquad
\Phi_{\mathrm{even},-}\longrightarrow\pi/3\quad(N\to\infty),
\]
whereas the respective optimal gaps satisfy
\[
N^2\Delta_N^{\max}\longrightarrow
\begin{cases}2J\pi^2&N\text{ odd},\\(8/3)J\pi^2&N\text{ even}.\end{cases}
\]

## Assumptions and scope

The graph is one uniform cyclic nearest-neighbor ring, with precisely \(N\ge3\) sites, no impurities, uniform positive hopping magnitude \(J\), and static flux. The entire analysis is single-particle, unitary and noiseless, with \(\hbar=1\). Adding a common scalar potential to the Hamiltonian leaves all gaps and results unchanged. Flux is the total gauge-invariant phase, modulo \(2\pi\). The displayed dephasing channel uses uniform averaging over a real time interval \([0,T]\); \(\|\cdot\|_{2\to2}\) is the superoperator norm induced by the matrix Hilbert--Schmidt norm, not the trace-to-trace or diamond norm. The optimization concerns the sharp asymptotic \(T^{-1}\) limsup coefficient and the equivalent smallest-Bohr-frequency maximin problem, not pointwise-in-time convergence.

## Proof

**1. Fourier reduction and the pair-gap identity.** Circulant diagonalization gives the indexed eigenvalues
\[
E_k(\Phi)=2J\cos\left(\frac{2\pi k+\Phi}{N}\right),\qquad k=0,\ldots,N-1.
\]
The Fourier eigenvectors and their rank-one projectors do not depend on \(\Phi\). For distinct indices \(j,k\), the cosine-difference identity gives
\[
|E_j-E_k|=4J\left|\sin\left(\frac{\Phi+\pi(j+k)}N\right)\right|
\left|\sin\left(\frac{\pi(j-k)}N\right)\right|.
\]
Write \(\theta=\Phi/N\) reduced modulo \(2\pi/N\), and set \(\alpha=\pi/N\). In absolute value, the two sine factors depend only on the sum and difference of the indices modulo \(N\).

**2. Odd cycles.** If \(N\) is odd, multiplication by \(2\) is invertible modulo \(N\), so the sum and difference of \(j,k\) range independently over all residues, subject only to nonzero difference. Thus
\[
\Delta_N(\Phi)=4J\sin\alpha\min_{s\in\mathbb Z/N\mathbb Z}|\sin(\theta+s\alpha)|.
\]
The \(N\) sine zeros modulo \(\pi\) are spaced by \(\alpha\); the distance to the nearest zero is maximized exactly at the two midpoints \(\theta=\alpha/2\) and \(\theta=3\alpha/2\) of the two cells in \([0,2\alpha)\). Their distances are \(\alpha/2\). This proves the odd formula and uniqueness modulo \(2\pi\).

**3. Even cycles.** If \(N\) is even, the sum and difference of indices have the same parity, and every pair of residues with matching parity occurs. For odd differences the least possible magnitude of the second factor is \(\sin\alpha\), while for nonzero even differences it is \(\sin(2\alpha)\). Reflecting \(\theta\) about \(\alpha\) preserves the unordered spectrum, so restrict to \(0\le\theta\le\alpha\). For odd sums the smallest possible first factor is \(\sin(\alpha-\theta)\) and for even sums it is \(\sin\theta\). Hence the **exact** gap formula on this half-cell is
\[
\Delta_N(\Phi)=4J\min\{\sin\alpha\sin(\alpha-\theta),\ \sin(2\alpha)\sin\theta\}.
\]
The first entry strictly decreases from a positive value to zero, while the second strictly increases from zero to a positive value. Their minimum has a unique global maximum at their intersection. The equality reduces to
\[
\sin(\alpha-\theta_*)=2\cos\alpha\sin\theta_*,\qquad
\tan\theta_*=\frac{\tan\alpha}{3}.
\]
Because \(0<\theta_*<\alpha\), this root is unique. Reflection gives the second and only other maximizer in the full flux circle. Substitution and elementary trigonometry give both expressions for the optimum.

**4. Sharp convergence norm and its attainment.** Let \(F_{jk}=|k_j\rangle\langle k_k|\) denote the Hilbert--Schmidt orthonormal matrix units in the Fourier energy basis. On diagonal units, both \(\mathcal C_T^\Phi\) and \(\mathcal D\) act as the identity. On \(j\ne k\) they act by a scalar multiplier and zero, respectively:
\[
(\mathcal C_T^\Phi-\mathcal D)(F_{jk})=
 e^{-i(E_j-E_k)T/2}
 \frac{\sin((E_j-E_k)T/2)}{(E_j-E_k)T/2}\,F_{jk}.
\]
Orthogonality proves that the induced Hilbert--Schmidt superoperator norm is exactly the largest magnitude of these sinc multipliers. If \(\Delta_N>0\), this is at most \(2/(T\Delta_N)\). Choose a pair attaining the finite minimum gap and take \(T_m=(2m+1)\pi/\Delta_N\) for integers \(m\ge0\). At every such time that pair attains the bound, hence \(T_m\|\mathcal C_{T_m}^\Phi-\mathcal D\|_{2\to2}=2/\Delta_N\) exactly. The limsup and the full optimizing flux classification follow.

**5. Asymptotic parity constants.** The odd expression follows from \(\sin z\sim z\). In the even case \(N\arctan(\tan(\pi/N)/3)\to\pi/3\), and \(\sin(2\pi/N)\sim2\pi/N\), \(\sin\theta_*\sim\pi/(3N)\). This proves the stated limits.

## Verification

The standalone file `verification_check.py` requires only Python's standard library. Run `python verification_check.py`. It independently enumerates Fourier energy differences, checks the parity-separated closed gap formula for each cycle size from \(3\) to \(40\), compares the claimed optimal gap with all indexed pairs and a finite flux grid, tests Fourier eigenvectors against the literal hopping action, verifies the exact norm-envelope saturation at several odd half-periods, and checks large-size scaling. The executed checker reported **11,446 passing finite assertions**. The full proof of the all-size theorem and optimizer uniqueness is analytic; neither the grid nor finite diagnostics constitute a universal proof.

## Relationship to prior work

Frigerio, Benedetti, Olivares and Paris established and exploited the gauge-equivalent fluxed-cycle Hamiltonian, its Fourier spectrum and phase-dependent transport (arXiv:2106.11685, 2021); those parts are not new. Baptista, Coutinho and Marques (arXiv:2308.16378v1, 2023) developed general averaging frameworks for continuous-time quantum walks, which also precede the present channel calculation. Levine and collaborators (arXiv:2605.04414v1, 2026), Theorem 5, already prove uniform average vertex mixing for any circulant with distinct eigenvalues, including these nondegenerate magnetic rings. Thus average uniformity itself is emphatically *not* a new claim. The 2026 work on quantum-ring thermometry (DOI:10.3389/frqst.2026.1894991) optimizes temperature sensitivity using the *ground-to-first-excited* gap, a different parameter objective that neither implies nor is implied by the maximum of the smallest difference among **all** pairs of energies. The present theorem isolates and exactly solves that latter maximin problem and links its optimizers to the sharp induced Hilbert--Schmidt Cesàro channel convergence coefficient. Comparisons found no directly covering all-size magnetic-flux optimization theorem; this is not a proof that none exists.

## Limitations

The optimization is restricted to a clean uniform nearest-neighbor ring, static flux, a single particle and the induced Hilbert--Schmidt norm. It does not prove the same flux minimizes the convergence error at every finite observation time, the trace norm, diamond norm, or noisy-mixing distance. At degenerate fluxes, the rank-one Fourier dephasing channel is not the infinite-time limit, so the asymptotic channel identity is asserted only at nondegenerate phases. A related spectral-optimization result in unindexed literature could change publication priority. The package records analytical derivations and finite reproducibility diagnostics, not an independent scientific audit.

## References

1. M. Frigerio, C. Benedetti, S. Olivares, M. G. A. Paris, *Quantum-classical distance as a tool to design optimal chiral quantum walks*, arXiv:2106.11685 (first public 2021-06-22). https://arxiv.org/abs/2106.11685
2. P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (first public 2023-08-31). https://arxiv.org/html/2308.16378v1
3. L. Levine, J. J. Mesapam, B. Mustico, C. Tamon, G. Tucker, H. Zhan, *Uniform Mixing in Chiral Quantum Walks*, arXiv:2605.04414v1 (2026). https://arxiv.org/html/2605.04414v1
4. L. Zanoli, G. Ragazzi, P. Bordone, M. G. A. Paris, *Quantum walks on a ring as a versatile single-parameter sensor*, Frontiers in Quantum Science and Technology (2026), DOI:10.3389/frqst.2026.1894991. https://doi.org/10.3389/frqst.2026.1894991
