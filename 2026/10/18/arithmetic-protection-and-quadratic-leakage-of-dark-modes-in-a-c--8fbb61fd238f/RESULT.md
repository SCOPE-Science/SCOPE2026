# Arithmetic protection and quadratic leakage of dark modes in a centrally lossy quantum chain

## Finding
For every integer \(m\ge1\), hopping \(J>0\), central loss rate \(\gamma>0\), impurity position \(s\in\{1,\dots,m\}\), and nonzero real detuning \(\varepsilon\), define the one-excitation no-jump Hamiltonian
\[
K_{\varepsilon}=J\sum_{j=1}^{2m} (|j\rangle\langle j+1|+|j+1\rangle\langle j|)-\frac{i\gamma}{2}|m+1\rangle\langle m+1|+\varepsilon|s\rangle\langle s|.
\]
Its real eigenvalues, each supporting an exactly nondecaying eigenvector, are **precisely**
\[
E_k=2J\cos\left(\frac{\pi k}{m+1}\right),\qquad 1\le k\le m,\quad (m+1)\mid sk.
\]
All other eigenvalues lie in the **strictly lower** half-plane. The number of real eigenvalues, equivalently the dimension of the one-excitation subspace immune to central loss and invariant under this Hamiltonian, is exactly \(\gcd(m+1,s)-1\), independent of the nonzero detuning amplitude and loss strength. The same assertions hold when the defect is reflected to site \(2m+2-s\).

At zero detuning there are \(m\) distinct real dark eigenvalues \(E_k\). For each \(k\), its unique locally analytic eigenvalue continuation \(\lambda_k(\varepsilon)\), at any **fixed** \(m,J,\gamma\), satisfies
\[
\operatorname{Im}\lambda_k(\varepsilon)
=-\frac{\gamma\,\sin^4\!\left(\frac{\pi sk}{m+1}\right)}{8J^2(m+1)\sin^2\!\left(\frac{\pi k}{m+1}\right)}\,\varepsilon^2+O(\varepsilon^3).
\]
The leading single-particle probability decay rate is twice the magnitude of this imaginary part. If \((m+1)\mid sk\), the branch instead stays **exactly constant** \(\lambda_k(\varepsilon)=E_k\) for every real detuning.

## Assumptions and scope
The Hilbert space is \(\mathbb C^{2m+1}\) with orthonormal site states. Time evolution between loss events is \(\exp(-itK_\varepsilon)\) in units with \(\hbar=1\). The central loss is the non-Hermitian term resulting from one Lindblad jump \(\sqrt\gamma|\mathrm{vac}\rangle\langle m+1|\) on the zero/one-excitation sector. This is a **one-particle no-jump spectral statement**, not a general many-body Lindblad stationary-state or mixing-time claim. The on-site defect is real and occurs on exactly one noncentral site. The error estimate refers to each fixed parameter set as \(\varepsilon\to0\) and is not uniform as \(\gamma\to0\) or \(\gamma\to\infty\).

Let \(T_m=JA(P_m)\) be the real symmetric open-half-chain adjacency matrix, with normalized eigenvectors \(v_k(j)=\sqrt{2/(m+1)}\sin(j\theta_k)\), \(\theta_k=\pi k/(m+1)\). Its eigenvalues are the distinct \(E_k\), and \(v_k(m)\ne0\). At zero detuning, antisymmetric reflection eigenvectors \(\psi_k\) have left-half component \(v_k/\sqrt2\), right-half component the negative reflection of it, and vanishing center.

## Proof
**1. Unperturbed real modes and strict dissipation.** If \(K_\varepsilon\psi=z\psi\) and \(\psi\ne0\), then
\[
\operatorname{Im}z=-\frac{\gamma}{2}\frac{|\psi(m+1)|^2}{\|\psi\|^2}\le0.
\]
Thus a real eigenvalue forces the center component to vanish. The separate left and right halves then obey Dirichlet equations. Neither half can vanish identically, since the center-site equation would force the endpoint of the remaining half to vanish and the tridiagonal recurrence would force its entire vector to vanish. The **unperturbed right half** must therefore be proportional to some \(v_k\), and its energy must equal \(E_k\).

**2. Exact arithmetic survival.** The left half must have the same eigenvalue \(E_k\) for \(T_m+\varepsilon|s\rangle\langle s|\). The rank-one determinant lemma in its polynomial form gives, at the simple eigenvalue \(E_k\),
\[
\det(E_kI-T_m-\varepsilon|s\rangle\langle s|)
=-\varepsilon|v_k(s)|^2\prod_{\ell\ne k}(E_k-E_\ell).
\]
For \(\varepsilon\ne0\), this vanishes if and only if \(v_k(s)=0\), equivalently \((m+1)\mid sk\). Conversely, at such nodes the explicit original antisymmetric vector \(\psi_k\) is annihilated by both the central loss and impurity projectors, and remains an exact eigenvector at \(E_k\). Thus there are no other real energies, and all remaining eigenvalues have strictly negative imaginary part. The number of integers \(1\le k\le m\) such that \((m+1)\mid sk\) is \(\gcd(m+1,s)-1\). The protected eigenvectors have distinct energies and span the entire loss-free invariant one-particle sector.

**3. Bright-sector invertibility.** At \(\varepsilon=0\), pass to reflection-odd and reflection-even orthonormal bases. The odd block is \(T_m\). The even block \(B\) has \(T_m\) in its first \(m\) coordinates, an additional center coordinate with diagonal \(-i\gamma/2\), and a coupling of \(\sqrt2J\) between this center and site \(m\). To show \(E_k-B\) is invertible, suppose \((E_k-B)(y,t)=0\). Multiplying the first block row by \(v_k^*\) yields \(t=0\), since \(v_k(m)\ne0\). The first row then gives \(y=av_k\), and the center row gives \(y(m)=0\), so \(a=0\). Therefore each dark \(E_k\) is a simple eigenvalue of the **entire** unperturbed non-Hermitian matrix and admits an analytic eigenvalue branch in \(\varepsilon\).

**4. Exact imaginary resolvent identity.** Let \(G_k=(E_k-B)^{-1}\). The matrix identity
\[
G_k-G_k^*=G_k(B-B^*)G_k^*=-i\gamma G_k|c\rangle\langle c|G_k^*
\]
gives \(\operatorname{Im}(G_k)_{ss}=-\gamma|(G_k)_{sc}|^2/2\). Solve \((E_k-B)(y,t)=|c\rangle\): the first block, projected against \(v_k\), forces \(t=0\), while the center row yields \(y(m)=-1/(\sqrt2J)\). Consequently \(y=-v_k/(\sqrt2Jv_k(m))\), hence
\[
(G_k)_{sc}=-\frac{v_k(s)}{\sqrt2Jv_k(m)},\qquad
\operatorname{Im}(G_k)_{ss}=-\frac{\gamma v_k(s)^2}{4J^2v_k(m)^2}.
\]
These are **exact at each fixed positive \(\gamma\)**; no small-loss approximation was made.

**5. Second-order eigenvalue perturbation.** The defect vector \(|s\rangle\) has equal amplitude \(1/\sqrt2\) in odd and even parity sectors. Its normalized overlap with \(\psi_k\) is \(v_k(s)/\sqrt2\). Standard simple-eigenvalue perturbation for a complex-symmetric matrix, with the dark eigenvector chosen real, gives
\[
\lambda_k(\varepsilon)
=E_k+\frac{v_k(s)^2}{2}\varepsilon
+\varepsilon^2\frac{v_k(s)^2}{2}\left(\frac12(G_k)_{ss}+R_k\right)+O(\varepsilon^3),
\]
where \(R_k=\frac12\sum_{\ell\ne k}v_\ell(s)^2/(E_k-E_\ell)\) is real. Taking the imaginary part and inserting the exact resolvent expression yields
\[
\operatorname{Im}\lambda_k(\varepsilon)
=-\frac{\gamma v_k(s)^4}{16J^2v_k(m)^2}\varepsilon^2+O(\varepsilon^3).
\]
Finally \(v_k(m)^2=\frac2{m+1}\sin^2\theta_k\) and \(v_k(s)^4=\frac4{(m+1)^2}\sin^4(s\theta_k)\), giving the stated coefficient. At arithmetic nodes, the earlier exact eigenvector construction applies for **all** detunings, not merely perturbatively.

## Verification
The standalone `verify.py` builds the full matrices without using the parity-block derivation. With NumPy it independently checks the exact number of real eigenvalues for \(1\le m\le8\), every allowed \(s\), and two different positive loss rates at a nonzero real detuning. It checks the algebraic node eigenvectors by matrix residuals, and compares quadratic widths for every nonnode \((m,s,k)\) using two detuning sizes; the 380 nonnode mode/defect/rate combinations passed. The separate `verify_exact.py` uses SymPy and characteristic-polynomial implicit differentiation on small chains to check the second-order coefficient for \((m,s)=(1,1),(2,1),(3,1),(3,2)\). These finite checks detect errors but **are not the all-size proof**, which is the determinant, resolvent, and perturbation argument above. Run `python verify.py` with NumPy and `python verify_exact.py` with SymPy installed; no external data are required.

## Relationship to prior work
Dutta and Cooper, *Long-Range Coherence and Multiple Steady States in a Lossy Qubit Array* (first preprint 2020-04-16), established central-loss protection of reflection-odd single-particle modes and discussed their many-body role. Its supplementary symmetry analysis discusses generic symmetry-breaking Hamiltonian perturbations and first-order robustness of **steady-state density operators**, not the exact impurity-position arithmetic classification or the explicit one-particle complex-energy linewidth proved here. Dutta and Cooper, *Out-of-equilibrium steady states of a locally driven lossy qubit array* (first preprint 2020-07-17), further analyzes locally driven chains and the positions of nodes in unperturbed modes, but does not supply this all-detuning single-defect count together with the exact second-order linewidth coefficient. The result also uses familiar rank-one spectral perturbation techniques, but evaluates them at a central-loss resonance to produce a closed position-sensitive coefficient that is not stated by those general principles alone.

## Limitations
Only single-excitation no-jump dynamics of an odd open nearest-neighbor path with a single off-center real on-site defect is treated. The quadratic expansion is pointwise in \(m,J,\gamma,s,k\), not uniform in the Zeno or zero-loss limits, and does not yield many-body relaxation rates or a global Liouvillian gap. Finite numerical checks do not certify larger sizes; the proofs are analytic. The source comparison is a targeted best-knowledge literature comparison, not a universal guarantee of priority; broader literature may contain an equivalent formulation requiring further independent review.

## References
1. S. Dutta and N. R. Cooper, *Long-Range Coherence and Multiple Steady States in a Lossy Qubit Array*, arXiv:2004.07981 (first posted 2020-04-16), Phys. Rev. Lett. 125, 240404 (2020), https://arxiv.org/abs/2004.07981.
2. S. Dutta and N. R. Cooper, *Out-of-equilibrium steady states of a locally driven lossy qubit array*, arXiv:2007.08938 (first posted 2020-07-17), Phys. Rev. Research 3, L012016 (2021), https://arxiv.org/abs/2007.08938.
