# Parity-doubled magnetic-flux onset in dephasing Liouvillian spectral moments

## Finding
Let \(N\ge3\) and let \(H_\phi\) be a uniform nearest-neighbor tight-binding Hamiltonian on the \(N\)-cycle with hopping magnitude \(J>0\) and total magnetic flux \(\phi\). Consider the Markovian dephasing generator \(\mathcal L_{\phi,\boldsymbol\gamma}\) defined below for arbitrary site-dependent rates \(\gamma_j\ge0\). Its unnormalized superoperator spectral moments are \(M_k(\phi)=\operatorname{Tr}_{\mathrm{End}(M_N(\mathbb C))}(\mathcal L_{\phi,\boldsymbol\gamma}^{\,k})\), for integers \(k\ge1\).

**Even cycles.** For even \(N\), \(M_k(\phi)=M_k(0)\) for every \(1\le k<N\), while
\[
M_N(\phi)-M_N(0)=4N^2(-1)^{N/2}J^N(\cos\phi-1).
\]
**Odd cycles.** For odd \(N\), \(M_k(\phi)=M_k(0)\) for every \(1\le k<2N\), while
\[
M_{2N}(\phi)-M_{2N}(0)=-4N^2J^{2N}\left(\binom{2N}{N}-2\right)\sin^2\phi.
\]
The displayed responses are exact for all rates \(\boldsymbol\gamma\), including nonuniform and zero rates, and are nonzero precisely when \(\phi\notin2\pi\mathbb Z\) for even \(N\), or \(\phi\notin\pi\mathbb Z\) for odd \(N\). The earliest flux-sensitive moment of the full Liouvillian therefore occurs at order \(N\) for even cycles but order \(2N\) for odd cycles, for generic flux.

## Assumptions and scope
Label the orthonormal site basis by \(j\in\mathbb Z/N\mathbb Z\), and put \(P_j=|j\rangle\langle j|\). Define \(H_{\phi}\) by \(\langle j|H_{\phi}|j+1\rangle=J e^{i\phi/N}\), \(\langle j+1|H_{\phi}|j\rangle=J e^{-i\phi/N}\), and all other entries zero, including the diagonal. Distinct edges exist for \(N\ge3\). Let
\[
\mathcal L_{\phi,\boldsymbol\gamma}(\rho)=-i[H_\phi,\rho]+\sum_{j=0}^{N-1}\gamma_j\left(P_j\rho P_j-\tfrac12\{P_j,\rho\}\right).
\]
Every \(\gamma_j\) is a fixed arbitrary nonnegative real. The trace in \(M_k\) is over the \(N^2\)-dimensional complex vector space of matrices, not the quantum-state trace and not a normalized average. Flux is a real angle, identified modulo \(2\pi\). The theorem makes no assumption of translation-invariant dephasing.

## Proof
**1. Closed walks bound the Fourier harmonics.** In the operator basis \(E_{xy}=|x\rangle\langle y|\), the dissipator is diagonal: it is zero for \(x=y\), and otherwise has diagonal entry \(-\tfrac12(\gamma_x+\gamma_y)\). The Hamiltonian commutator moves either \(x\) or \(y\) by one step around its respective \(N\)-cycle. Consequently, \(\operatorname{Tr}(\mathcal L^k)\) is a finite sum over length-\(k\) closed walks on the doubled torus, with diagonal waiting steps. If the two coordinate windings are \(w_x,w_y\in\mathbb Z\), the walk's magnetic phase is \(e^{i\phi(w_y-w_x)}\), up to the convention for orientation. Its total number of non-waiting hops is at least \(N(|w_x|+|w_y|)\). Thus a nonconstant Fourier harmonic \(e^{i\ell\phi}\) in \(M_k(\phi)\) necessarily satisfies \(k\ge N|\ell|\). In particular every order below \(N\) is flux-blind.

**2. Odd-cycle half-flux periodicity.** Vectorize matrices in the \(E_{xy}\) basis and write \(\mathcal L_H=A_H+D\), where \(A_H=-i(I\otimes H-H^{\mathsf T}\otimes I)\) and \(D\) is the diagonal dissipator. The coordinate-swap permutation \(S(E_{xy})=E_{yx}\) satisfies \(SDS=D\) and \(S A_H^{\mathsf T}S=-A_H\). Hence \(S\mathcal L_H^{\mathsf T}S=\mathcal L_{-H}\), so these two generators have the same characteristic polynomial and all spectral moments. For odd \(N\), multiplying all hoppings by \(-1\) shifts the total cycle flux by \(N\pi\equiv\pi\pmod{2\pi}\); the resulting Hamiltonian is related to \(H_{\phi+\pi}\) by a diagonal unitary gauge. Such a gauge fixes the site projectors and hence the dissipator. Therefore \(M_k(\phi+\pi)=M_k(\phi)\) for odd \(N\). Only even Fourier harmonics are allowed. Combined with Step 1, this proves flux-blindness at all orders \(k<2N\) for odd \(N\).

**3. The first nonconstant term ignores the dissipator.** At order \(N\) in an even cycle, the only potentially flux-dependent closed walks have \(|w_y-w_x|=1\), which forces \(N\) actual hopping steps and no waiting steps. At order \(2N\) in an odd cycle, half-flux periodicity eliminates odd harmonics, and the first remaining ones have \(|w_y-w_x|=2\), again forcing all \(2N\) steps to be hopping steps. Thus the flux-dependent difference of the relevant moment equals that of the purely coherent commutator \(A_{H_\phi}=-i[H_\phi,\cdot]\), regardless of the rates \(\boldsymbol\gamma\).

**4. Exact coefficient from the coherent spectral moments.** Set \(h_r(\phi)=\operatorname{tr}(H_\phi^r)\) and \(h_0=N\). Since left and right multiplications commute,
\[
\operatorname{Tr}(A_{H_\phi}^k)=(-i)^k\sum_{r=0}^k(-1)^{k-r}\binom{k}{r}h_r(\phi)h_{k-r}(\phi).
\]
For any \(N\), the only flux-sensitive length-\(N\) closed walks are the two uniform orientations around the ring, so \(h_N(\phi)-h_N(0)=2NJ^N(\cos\phi-1)\). If \(N\) is even, in the above sum for \(k=N\) only the two endpoint terms are flux-dependent, yielding \(4N^2(-1)^{N/2}J^N(\cos\phi-1)\).

For odd \(N\), there is no closed walk of odd length strictly less than \(N\), so \(h_r=0\) for odd \(r<N\). Moreover \(h_N(\phi)=2NJ^N\cos\phi\), and the flux-dependent part of \(h_{2N}(\phi)-h_{2N}(0)\) is exactly \(2NJ^{2N}(\cos2\phi-1)\): a length-\(2N\) closed walk with nonzero winding must wind twice, since one winding has odd parity. At \(k=2N\), the only flux-dependent terms in the binomial sum are \(r=0,N,2N\); all other possible nonzero windings multiply a vanishing odd moment. Inserting these three terms gives
\[
-4N^2J^{2N}\left[\cos2\phi-1-\binom{2N}{N}(\cos^2\phi-1)\right]
=-4N^2J^{2N}\left(\binom{2N}{N}-2\right)\sin^2\phi.
\]
This proves both statements. The coefficient \(\binom{2N}{N}-2\) is strictly positive for \(N\ge3\), so the onset orders are sharp away from the indicated gauge-equivalent fluxes.

## Verification
The accompanying `CHECK.py` constructs the full \(N^2\times N^2\) Liouvillian in the site-operator basis, including independent dephasing rates at different sites, and compares all moments through the claimed first sensitive order to the closed forms. The test covers \(3\le N\le8\), three independently specified rate/hopping configurations, and three nonexceptional flux values, totaling 432 comparisons. All passed with maximum relative discrepancy below \(2.11\times10^{-15}\) under the script's scaling. These finite computations test implementations and signs; the infinite-family theorem follows from Steps 1–4, not from numerical sampling.

## Relationship to prior work
Esposito and Gaspard analyzed quantum diffusion on finite cyclic tight-binding systems with environment-induced dephasing and derived a Bloch decomposition and spectral relaxation picture; the inspected 2005 full article treats real untwisted hoppings and does not state a magnetic-flux moment-onset classification. Klausen and Werner studied single-particle translation-covariant Lindblad spectra, including local dephasing and finite-volume periodic approximations; the inspected primary text focuses on untwisted Hamiltonians and thermodynamic-limit spectra, not the full trace-moment parity threshold with spatially nonuniform dephasing. The result here does **not** claim these standard physical models, vectorization, or closed-walk trace identities as novel. It identifies the exact parity-dependent first spectral response to cycle holonomy, including its rate-independent closed coefficient for arbitrary sitewise dephasing.

## Limitations
This is a spectral-moment statement, not a claimed finite-time measurement protocol, lower bound on relaxation, or assertion of dynamical transfer fidelity. The moments are unnormalized and may grow quickly with \(N\). The proof assumes uniform hopping magnitudes, no diagonal site energies, and pure site-projector dephasing; additional incoherent hopping channels or nonuniform edge couplings are not covered. The absence of an identical statement in inspected literature is not an independent priority certification.

## References
1. M. Esposito and P. Gaspard, *Emergence of diffusion in finite quantum systems*, Phys. Rev. B **71** (2005), 214302, doi:10.1103/PhysRevB.71.214302. Inspected the lawful open-access postprint text, particularly the model definition and spectral analysis; also searched complete document for flux terms.
2. F. R. Klausen and A. H. Werner, *Spectra of generators of Markovian evolution in the thermodynamic limit: From non-Hermitian to full evolution via tridiagonal Laurent matrices*, arXiv:2206.09879 (first public posting 20 June 2022). Inspected primary article sections 3.6–3.7 and 5.1 as reproduced within the author's 2023 academic thesis, *Random Problems in Mathematical Physics* (University of Copenhagen).
