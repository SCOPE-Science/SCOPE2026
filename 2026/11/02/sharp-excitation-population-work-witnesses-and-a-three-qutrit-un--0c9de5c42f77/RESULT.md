# Sharp excitation-population work witnesses and a three-qutrit universal discharge threshold

## Finding

Let \(N\ge2\) and consider identical, noninteracting V-type three-level cells with a unique ground state \(|g\rangle\), two degenerate excited states \(|a\rangle,|b\rangle\), and excitation energy \(\omega>0\). Under unrestricted joint cyclic-unitary work extraction, every battery state supported entirely in the permutation-symmetric subspace has an exact, sharp population witness: for \(N\ge3\),
\[
\mathcal W_N(\rho)\ge \omega p_{\ge2}(\rho),\qquad
p_{\ge2}(\rho)=\operatorname{Tr}\bigl[\rho\,\mathbf1_{\{H_N\ge2\omega\}}\bigr].
\]
One joint unitary, chosen from the cell number and bare energy structure alone, achieves a work gain **exactly** \(\omega p_{\ge2}(\rho)\) for *every* such state simultaneously. For two cells the sharp uniform coefficient is \(2/3\), and no fixed joint unitary can guarantee a positive coefficient on all symmetric-support states. These are nonasymptotic statements about arbitrary pure and mixed states, with coherences between excitation sectors permitted.

The witness can be positive when the energy-dephased state is passive, hence cannot generally be obtained merely by invoking the lower bound given by incoherent ergotropy.

## Assumptions and scope

For every integer \(N\ge2\), write \(\mathcal H_N=(\mathbb C^3)^{\otimes N}\) with the tensor-product site basis \(|g\rangle,|a\rangle,|b\rangle\). Define
\[
H_N=\omega\sum_{i=1}^{N}\bigl(I-|g\rangle\langle g|\bigr)_i,\quad
P_q=\mathbf1_{\{H_N=q\omega\}},\quad
S=\operatorname{Sym}^N(\mathbb C^3),\quad S_q=P_qS.
\]
The input satisfies \(\rho\ge0\), \(\operatorname{Tr}\rho=1\), and \(\rho=P_S\rho P_S\); there is no diagonality, separability, or fixed excitation-number assumption. Global ergotropy is
\[
\mathcal W_N(\rho)=\operatorname{Tr}(H_N\rho)-\min_{U\in U(3^N)}\operatorname{Tr}(H_NU\rho U^\dagger).
\]
The available control consists of arbitrary cyclic unitaries on the **full** tensor-product Hilbert space, not merely permutations, collective spin rotations, energy-preserving operations, local gates, or operations restricted to \(S\). Thus the constructed discharge unitary may break permutation symmetry. We do not assert an energetically free physical implementation or any charging dynamics; the work gain is the standard difference in battery energy under cyclic unitary driving. Degeneracy of the two excited levels is essential.

## Proof

**Symmetric and ambient excitation multiplicities.** A symmetric state at excitation number \(q\) has one basis vector for each pair of nonnegative occupations \((n_a,n_b)\) with \(n_a+n_b=q\), so
\[
\dim S_q=q+1,\qquad \dim P_q\mathcal H_N=\binom Nq2^q.
\]
For \(N\ge3\) and \(2\le q\le N\), the unused part of the one-quantum-lower eigenspace obeys
\[
\dim(P_{q-1}\mathcal H_N\ominus S_{q-1})
=2^{q-1}\binom N{q-1}-q\ge q+1=\dim S_q.
\]
At \(q=2\) this is \(2N-2\ge3\). At \(q\ge3\), \(\binom N{q-1}\ge q\) and \(2^{q-1}\ge4\), giving a strictly stronger bound.

**State-independent discharge for all \(N\ge3\).** For each \(q\ge2\), choose an isometry \(V_q:S_q\longrightarrow P_{q-1}\mathcal H_N\ominus S_{q-1}\). Let \(V_0\) and \(V_1\) be the identity on \(S_0\) and \(S_1\), respectively. Images for different \(q\) lie in orthogonal excitation eigenspaces, except the images of \(S_1\) and \(S_2\), which are orthogonal by the complement condition. Hence \(V=\bigoplus_{q=0}^N V_q\) is an isometry from \(S\) into \(\mathcal H_N\), extendible by completing orthonormal bases to a global unitary \(U_N\). Its compression of the energy is the operator identity
\[
P_SU_N^\dagger H_NU_NP_S
=P_S\left(H_N-\omega\sum_{q=2}^NP_q\right)P_S.
\]
Tracing against any admissible \(\rho\), including its inter-sector offdiagonal terms, proves the exact work identity
\[
\operatorname{Tr}(H_N\rho)-\operatorname{Tr}(H_NU_N\rho U_N^\dagger)
=\omega p_{\ge2}(\rho).
\]
The definition of the optimal ergotropy yields the claimed inequality. To see its coefficient is sharp, choose any normalized \(|\psi_2\rangle\in S_2\), and for \(0<p\le1/2\) let \(\rho_p=(1-p)|g\rangle\langle g|^{\otimes N}+p|\psi_2\rangle\langle\psi_2|\). Its only positive eigenvalues are \(1-p\) and \(p\). Its initial energy is \(2p\omega\), while the spectral rearrangement into the unique ground state and a first-excited state has passive energy \(p\omega\). Thus \(\mathcal W_N(\rho_p)=p\omega=\omega p_{\ge2}(\rho_p)\).

**Sharp two-cell constant.** For \(N=2\), \(S_2\) is three-dimensional but the complement \(P_1\mathcal H_2\ominus S_1\) is only two-dimensional. Given any admissible \(\rho\), let \(B=P_{S_2}\rho P_{S_2}\) have eigenvalues \(\lambda_1\ge\lambda_2\ge\lambda_3\ge0\). Choose a unitary that fixes \(S_0\oplus S_1\), sends the eigenvectors for \(\lambda_1,\lambda_2\) into the two vacant first-excitation directions, and retains the third in the second-excitation eigenspace. Orthogonal images extend to a unitary on \(\mathcal H_2\), giving work gain \(\omega(\lambda_1+\lambda_2)\). Because \(\lambda_1+\lambda_2\ge(2/3)\operatorname{Tr}B=(2/3)p_{\ge2}\), the claimed bound follows even when \(\rho\) has inter-sector coherences. For \(\rho_*=P_S/6\), the six positive eigenvalues equal \(1/6\). Its mean energy is \(4\omega/3\), and its passive state occupies the ground state, all four first-excited states, and one second-excited state, giving energy \(\omega\). Hence \(\mathcal W_2(\rho_*)=\omega/3\) while \(p_{\ge2}(\rho_*)=1/2\), proving sharpness of \(2/3\).

**Why no positive two-cell state-independent witness exists.** Suppose one fixed global unitary \(U\) extracted at least \(c\omega p_{\ge2}(\rho)\) from every symmetric-support state, where \(c>0\). For the pure symmetric ground state, whose initial energy is zero, nonnegative work forces \(U\) to fix its one-dimensional eigenspace. For every pure vector in \(S_1\), the desired nonnegative work means its transformed energy is at most \(\omega\). Orthogonality to the occupied ground image, together with the lower bound \(H_2\ge\omega I\) on the ground complement, forces \(U(S_1)\subseteq P_1\mathcal H_2\). That image occupies two of the four first-excitation directions. The linear projection of the three-dimensional \(U(S_2)\) into the remaining two first-excitation directions therefore has a nonzero kernel; a normalized vector \(\psi\in S_2\) is mapped entirely to \(P_2\mathcal H_2\). Its energy is unchanged, yet \(p_{\ge2}(|\psi\rangle\langle\psi|)=1\), contradiction. Thus three cells is the minimal nontrivial size for a fixed-universal positive-work protocol with this population witness.

**Nonimplication by generic incoherent-ergotropy bounds.** For three cells set
\[
\rho_\circ=\frac{69}{100}P_{S_0}+\frac{3}{20}P_{S_1}+\frac1{300}P_{S_2}.
\]
This is normalized because the symmetric-sector dimensions are \(1,2,3\). Its diagonal in the computational energy basis has ground population \(0.69\), each of six one-excitation populations \(0.05\), and twelve two-excitation populations each either \(1/900\) or \(1/1800\); higher-excitation populations vanish. Thus the energy-dephased state is already passive, giving zero incoherent ergotropy, but \(p_{\ge2}(\rho_\circ)=0.01\), so the established fixed unitary extracts \(0.01\omega\). The general incoherent-ergotropy lower bound is therefore insufficient to imply the present population witness.

## Verification

Run `python verification/check.py` with Python 3, NumPy, and SciPy. The standalone file constructs orthonormal symmetric sector bases, numerically completes the energy-lowering isometries for \(N=3,4,5\), checks their compressed energy operators and sixteen reproducible random mixed states at each size, checks the two-cell exact sharpness witness, checks the passive-dephasing counterexample, checks one three-cell equality case, and checks the dimension inequality for all integer \(3\le N\le29\). It prints `PASS` and returns zero on success. These finite tests support, but do not replace, the preceding proof for every integer \(N\ge2\).

## Relationship to prior work

Wang and Dou [1], first available publicly on December 26, 2025, establish general passive-rearrangement and coherent/incoherent-ergotropy bounds and study qubit Jaynes–Cummings and Tavis–Cummings examples. Their general inequality using incoherent ergotropy is not the present positive bound because \(\rho_\circ\) above makes that lower bound vanish. Their energy-population investigations do not state the sharp \(N=2\) versus \(N\ge3\) symmetric V-type witness or a state-independent discharging unitary.

Hajizade, Ameri, and Askari [2], first available October 4, 2026, address two coupled three-level cells, correlation ergotropy and decoherence; the accessible abstract is relevant but the complete manuscript was not accessible for decisive section-by-section comparison. Grazi et al. [3] study noise-generated ergotropy in two- and four-qubit XX batteries and dark subspaces, a different Hamiltonian and noise-controlled question. Andolina et al. [4] study correlation-locked energy and asymptotically recoverable ergotropy for qubit Dicke batteries, not this finite V-type symmetric-support dimensional threshold. The standard passive-state spectral rearrangement formula [5] is used, not claimed as new. The new result is the *specific sharp uniform population bound, the fixed-discharge threshold, and its two-cell obstruction*, not a new definition of ergotropy or a generic restatement of spectral rearrangement.

## Limitations

The symmetric-support assumption is exact; symmetry-breaking support leakage is outside the theorem. The excited levels must be exactly degenerate, and unconstrained joint unitaries must be available; local-only, symmetry-conserving, or autonomous discharge may have much lower work. The theorem is static and does not establish that a concrete charging dissipator produces symmetric-support states or that implementing the selected global unitary is free of energetic control costs. The nearest three-level two-cell study [2] was accessible at abstract level only, and broader unpublished or unlocated subspace rearrangement results could cover part of the construction. No independent mathematical or publication-priority audit has been carried out.

## References

[1] C.-J. Wang and F.-Q. Dou, *Ergotropy in Quantum Batteries*, arXiv:2512.21855, first submitted 2025-12-26; Chinese Physics Letters 43 (2026), 060602, https://arxiv.org/abs/2512.21855 and https://doi.org/10.1088/0256-307X/43/6/060602.

[2] H. Hajizade, V. Ameri, and A. Askari, *Erasure of entanglement-locked energy in multi-cell quantum batteries through decoherence*, arXiv:2610.05592, first submitted 2026-10-04, https://arxiv.org/abs/2610.05592.

[3] R. Grazi, D. Farina, N. Traverso Ziani, and D. Ferraro, *Charging Quantum Batteries via Dissipative Quenches*, arXiv:2604.08151, first submitted 2026-04-09, https://arxiv.org/abs/2604.08151.

[4] G. M. Andolina et al., *Extractable Work, the Role of Correlations, and Asymptotic Freedom in Quantum Batteries*, arXiv:1807.08656, first submitted 2018-07-23; Physical Review Letters 122 (2019), 047702, https://arxiv.org/abs/1807.08656.

[5] A. E. Allahverdyan, R. Balian, and T. M. Nieuwenhuizen, *Maximal work extraction from finite quantum systems*, Europhysics Letters 67 (2004), 565–571, https://arxiv.org/abs/cond-mat/0401574.
