# Bell nonlocality in a strong-coupling quantum-reset window

## Finding
Consider the two-spin transverse-field Ising Hamiltonian and the Poisson resetting protocol specified below. Write \(\alpha=J/\Omega\) and \(R=r/\Omega\), and denote by \(\mathcal B(\alpha,R)\) the maximal stationary Clauser–Horne–Shimony–Holt (CHSH) expectation over all local dichotomic projective qubit measurements.

**Finite-coupling activation.** For every \(\alpha\ge2\), resetting at \(R=1/(2\alpha)\) gives \(\mathcal B(\alpha,R)>2\), so the stationary two-qubit state is Bell-nonlocal. For every fixed finite \(\alpha>0\), the state is CHSH-local for all sufficiently small positive \(R\) and all sufficiently large \(R\). Thus at each \(\alpha\ge2\) the violation occurs in an intermediate-rate region, rather than being guaranteed at either resetting extreme. No uniqueness or connectedness of the entire violation set is asserted.

**Singular strong-coupling scaling.** For every fixed \(s>0\),
\[
\lim_{\alpha\to\infty}\mathcal B\left(\alpha,\frac{s}{\alpha}\right)
=2\sqrt{1+\left(\frac{2s}{1+4s^2}\right)^2}.
\]
The unique maximizing scaled rate is \(s=1/2\), with limiting CHSH value \(\sqrt5\). This is the **maximum within the stated scaling family**, not a claimed global finite-parameter upper bound.

## Assumptions and scope
Let \(J,\Omega,r>0\) and set \(\hbar=1\). The two qubits evolve under
\[
H=-J\,\sigma_z\otimes\sigma_z+\frac{\Omega}{2}(\sigma_x\otimes I+I\otimes\sigma_x).
\]
Independent Poisson resets with rate \(r\) replace the complete two-qubit state with \(\rho_0=|11\rangle\langle11|\). Between resets the system evolves unitarily and experiences no further noise. The stationary state is
\[
\rho_{\alpha,R}=R\int_0^\infty e^{-Rt}e^{-iH_\alpha t}\rho_0e^{iH_\alpha t}\,dt,
\qquad H_\alpha=-\alpha\,\sigma_z\otimes\sigma_z+\frac12(\sigma_x\otimes I+I\otimes\sigma_x),
\]
where \(t\) is time in units \(\Omega^{-1}\). The CHSH maximum uses unrestricted local projective measurements, rather than a fixed detector configuration.

## Proof
Set
\[
D=(1+R^2)^2+4\alpha^2R^2,\qquad F=4\alpha^2+R^2+4.
\]
Let \(T_{ij}=\operatorname{tr}(\rho_{\alpha,R}\,\sigma_i\otimes\sigma_j)\), with rows and columns indexed by \((x,y,z)\). Its exact real, symmetric form is
\[
T=\begin{pmatrix}
0&-2\alpha R/D&2\alpha R^2/D\\
-2\alpha R/D&2/F&-R/F\\
2\alpha R^2/D&-R/F&1-2/F
\end{pmatrix}. \tag{1}
\]
To reconstruct (1), for each Pauli product \(O\) use stationarity of the reset master equation:
\[
0=i\operatorname{tr}(\rho_{\alpha,R}[H_\alpha,O]) +R\bigl(\operatorname{tr}(\rho_0 O)-\operatorname{tr}(\rho_{\alpha,R}O)\bigr).
\]
The sixteen Pauli products form a closed basis under the commutator, giving a finite linear system with unique solution because \(R>0\). Its two-spin entries are (1); the single-spin entries are \(\langle\sigma_x\otimes I\rangle=-2\alpha/F\), \(\langle\sigma_y\otimes I\rangle=R(1+R^2)/D\), and \(\langle\sigma_z\otimes I\rangle=-R^2(4\alpha^2+R^2+1)/D\), together with their interchanged-spin counterparts. Substitution verifies the closed stationary system. The attached reproduction program separately evaluates the stationary density matrix in the Hamiltonian eigenbasis, avoiding use of (1).

By the Horodecki two-qubit criterion, if \(s_1\ge s_2\ge s_3\ge0\) are the singular values of \(T\), then \(\mathcal B=2\sqrt{s_1^2+s_2^2}\). The variational characterization of the top two eigenvalues of \(T^{\mathsf T}T\) gives
\[
\frac{\mathcal B^2}{4}\ge\|T e_x\|^2+\|T e_z\|^2
\ge T_{xy}^2+T_{zz}^2. \tag{2}
\]
For \(\alpha\ge2\) and \(R=1/(2\alpha)\),
\[
T_{zz}=1-\frac2F\ge\frac9{10},
\quad |T_{xy}|=\frac1{1+(1+1/(4\alpha^2))^2}\ge\frac{256}{545}.
\]
Thus (2) exceeds \((9/10)^2+(256/545)^2>1\), establishing strict CHSH violation for every stated coupling.

For fixed finite \(\alpha>0\) as \(R\downarrow0\), (1) tends to \(\operatorname{diag}(0,c,1-c)\) with \(c=1/[2(1+\alpha^2)]\in(0,1/2)\). Hence \(\lim\mathcal B=2\sqrt{c^2+(1-c)^2}<2\), so continuity gives CHSH locality for small positive rates. As \(R\to\infty\) at fixed \(\alpha\), the largest singular value is \(1-R^{-2}+O(R^{-4})\) and the second is \(O(R^{-2})\); therefore
\[
\mathcal B(\alpha,R)=2-2R^{-2}+O(R^{-4})<2
\]
for sufficiently large \(R\).

Finally, substituting \(R=s/\alpha\) in (1) and taking \(\alpha\to\infty\) gives
\[
T_\infty(s)=\begin{pmatrix}
0&-2s/(1+4s^2)&0\\
-2s/(1+4s^2)&0&0\\
0&0&1
\end{pmatrix}.
\]
Its singular values are \(1,u(s),u(s)\), where \(u(s)=2s/(1+4s^2)\in(0,1/2]\). The claimed limiting CHSH formula follows. Since \(u'(s)=2(1-4s^2)/(1+4s^2)^2\), its unique maximum on \(s>0\) is \(u(1/2)=1/2\), proving the scaling optimum \(\sqrt5\).

## Verification
Run `python verify.py` with NumPy installed. The program computes the stationary density matrix independently by diagonalizing the Hamiltonian and integrating the exact Poisson-age spectral factors, then checks (1) on 400 parameter pairs. It also tests the explicit finite-coupling witness, the scaling formula at five scaled rates and three large couplings, and CHSH locality at representative very small and very large reset rates. These finite computations are corroboration, **not** the proof of claims with universal quantifiers. The strict inequalities and limits follow from the preceding algebra and spectral variational principle.

## Relationship to prior work
Kulkarni and Majumdar, *Generating Entanglement by Quantum Resetting* (arXiv:2307.07485, first posted 2023-07-14), introduce precisely this transverse-Ising reset model, its exact stationary density operator, and numerical stationary concurrence. The density operator and its entanglement are established prior results. The contribution here is instead a **Bell-inequality** witness valid for all \(\alpha\ge2\), rigorous locality at either rate extreme for each fixed coupling, and the scaled CHSH profile and unique \(\sqrt5\) optimum. These Bell claims are not the source paper's stated concurrence maxima; Bell violation is strictly stronger than entanglement.

The CHSH optimization theorem itself is due to Horodecki, Horodecki, and Horodecki (1995). The work of Wald and collaborators (arXiv:2410.11497, posted 2024-10-15) studies reset-induced correlations in **discrete-time** quantum circuits and resonant gates rather than this continuous-time Hamiltonian and its inverse-coupling Bell scaling. A published general two-qubit-state correlation formula can of course be specialized, but none of the inspected relevant source sections states this combined Bell activation/scaling theorem.

## Limitations
The result does not prove the exact Bell-nonlocality boundary, a global optimum over all finite \((\alpha,R)\), or the uniqueness of the violation window at finite coupling. The parameter \(\sqrt5\) is sharp only in the specified strong-coupling scaling family. The conclusion concerns the full-reset, closed-system, symmetric two-spin model and ideal projective CHSH tests; it makes no claim for local resetting, detector inefficiencies, decoherence between resets, or larger spin chains. Priority against unidentified broader CHSH applications to reset states remains a residual risk.

## References
1. M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485, first public posting 2023-07-14, https://arxiv.org/abs/2307.07485.
2. R. Horodecki, P. Horodecki, and M. Horodecki, *Violating Bell inequality by mixed spin-1/2 states: necessary and sufficient condition*, Physics Letters A 200 (1995), 340–344, DOI: 10.1016/0375-9601(95)00214-N.
3. S. Wald et al., *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, first public posting 2024-10-15, https://arxiv.org/abs/2410.11497.
