# Universal position–sector Schmidt profile for a quadratic-density quantum-optical oscillator

## Finding

Let \(H\) be the two-component quantum-optical Hamiltonian in the assumptions below, and let \(\Psi_n=(\phi_n,\alpha_n)\), \(n\geq1\), denote its normalized simple bound states, with increasing energies \(w_n>\Omega\). Identify \(L^2(\mathbb R)\oplus L^2(\mathbb R)\) with \(L^2(\mathbb R)\otimes\mathbb C^2\), and reduce a pure bound state over its **spatial** factor:

\[
 R_n=\begin{pmatrix}\|\phi_n\|_2^2&\langle\phi_n,\alpha_n\rangle\\
 \langle\alpha_n,\phi_n\rangle&\|\alpha_n\|_2^2\end{pmatrix}.
\]

Write \(p_n=\|\alpha_n\|_2^2\), and let \(r_{2j-1}=|a_j'|\), \(r_{2j}=|a_j|\) be the increasing, interlaced positive magnitudes of the negative Airy-derivative and Airy zeros. The **exact** atomic-sector occupation is

\[
 p_n=\frac{w_n}{4w_n-3\Omega},\qquad
 w_n^3(w_n-\Omega)=g^2r_n^3.
\]

The substantive new observable is the off-diagonal coherence, and hence the position–sector Schmidt spectrum. Define \(\eta_n\) by the dimensionless scalar-photon spatial expectation in the proof. For every \(n\),

\[
 R_n=\begin{pmatrix}1-p_n&\sqrt{3p_n(1-p_n)}\,\eta_n\\
 \sqrt{3p_n(1-p_n)}\,\eta_n&p_n\end{pmatrix},\qquad
 \eta_n\longrightarrow\frac12.
\]

In particular, at **fixed** \(g,\Omega>0\) and \(n\to\infty\),

\[
 R_n\longrightarrow R_\infty=
 \begin{pmatrix}3/4&3/8\\3/8&1/4\end{pmatrix},\qquad
 \operatorname{spec}(R_\infty)=
 \left\{\frac{4+\sqrt{13}}8,\frac{4-\sqrt{13}}8\right\}.
\]

Its limiting purity is \(29/32\), and its position–sector von Neumann entropy (natural logarithms) is
\[
 S_\infty=-\sum_{\pm}\frac{4\pm\sqrt{13}}8
 \log\left(\frac{4\pm\sqrt{13}}8\right)
 =0.196466978464698\ldots.
\]

More sharply, allow \(g=g_n>0\) and \(\Omega=\Omega_n>0\) to vary while \(n\to\infty\) and \(g_n n/\Omega_n^2\to s\in(0,\infty)\). Let \(z=z(s)>1\) be the unique solution of

\[
 z^3(z-1)=\left(\frac{3\pi s}{4}\right)^2,
 \qquad p(s)=\frac{z(s)}{4z(s)-3}.
\]

Then
\[
 R_n\longrightarrow R(s)=
 \begin{pmatrix}
 1-p(s)&\frac{\sqrt3}{2}\sqrt{p(s)(1-p(s))}\\
 \frac{\sqrt3}{2}\sqrt{p(s)(1-p(s))}&p(s)
 \end{pmatrix}.
\]

The limiting Schmidt eigenvalues are
\[
 \lambda_{\pm}(s)=\frac{1\pm\sqrt{1-p(s)(1-p(s))}}2.
\]

Their binary entropy is **strictly increasing** for \(0<s<s_*\) and **strictly decreasing** for \(s>s_*\), with the unique maximum at
\[
 s_*=\frac{\sqrt3}{\pi},\quad z(s_*)=\frac32,\quad
 p(s_*)=\frac12,\quad
 \operatorname{spec}(R(s_*))=
 \left\{\frac{2+\sqrt3}4,\frac{2-\sqrt3}4\right\}.
\]

This is a **spatial-position versus two-component-label** Schmidt entropy, not an assertion of entanglement between two separately tensor-factorized many-body photon and atomic subsystems.

## Assumptions and scope

Take \(g,\Omega>0\) and the essentially self-adjoint closure on \(L^2(\mathbb R)\oplus L^2(\mathbb R)\) of
\[
 H_0=\begin{pmatrix}|D|&g|x|\\g|x|&\Omega\end{pmatrix}
\]
initially on Schwartz functions. The Fourier symbol of \(|D|\) is \(|k|\). The bound eigenpairs \((w_n,\Psi_n)\) are those above \(\Omega\) characterized in Johar–Kraisler (2026). Normalize \(\|\phi_n\|_2^2+\|\alpha_n\|_2^2=1\), and choose their common phase so the scalar photonic wavefunction has real parity; the eliminated atomic component has the same phase and parity. The results concern the stated fixed-parameter and positive-double-scaling limits, **not** the continuous spectrum or finite-index extremizers of entropy.

## Proof

**1. Exact scalar reduction and occupation.** Eliminate the second component of the eigenvalue equation:
\[
 \alpha_n(x)=\frac{g|x|}{w_n-\Omega}\phi_n(x),\qquad
 (|D|+\kappa_n x^2)\phi_n=w_n\phi_n,
 \quad\kappa_n=\frac{g^2}{w_n-\Omega}.
\]

Set \(u_n=\phi_n/\|\phi_n\|_2\). The dilation virial identity for the homogeneous kinetic symbol \(|k|\) and quadratic potential gives
\[
 \langle u_n,|D|u_n\rangle=2\kappa_n\langle u_n,x^2u_n\rangle,
 \qquad
 \langle u_n,x^2u_n\rangle=\frac{w_n}{3\kappa_n}.
\]

These are valid for the actual Airy eigenfunctions (or by a cutoff dilation followed by the eigenfunction decay). Consequently
\[
 \frac{\|\alpha_n\|_2^2}{\|\phi_n\|_2^2}
 =\frac{g^2}{(w_n-\Omega)^2}\frac{w_n}{3\kappa_n}
 =\frac{w_n}{3(w_n-\Omega)},
\]
which proves the exact formula for \(p_n\). This occupation alone also follows from Hellmann–Feynman differentiation of the earlier spectral equation and is **not claimed to be new**.

**2. Dimensionless spatial overlap.** Introduce the positive spatial scale
\[
 L_n=\sqrt{\frac{w_n}{\kappa_n}},\qquad
 \eta_n=\int_{\mathbb R}\frac{|x|}{L_n}|u_n(x)|^2\,dx.
\]

The same virial identity gives \(\int (x/L_n)^2|u_n(x)|^2dx=1/3\). Since \(\alpha_n\) is a positive multiplier of \(\phi_n\), their overlap is real and
\[
 \langle\phi_n,\alpha_n\rangle
 =\sqrt{3p_n(1-p_n)}\,\eta_n.
\]
Cauchy–Schwarz gives \(0<\eta_n<1/\sqrt3\), so \(R_n\) is positive definite and has determinant
\[
 \det R_n=p_n(1-p_n)(1-3\eta_n^2).
\]

**3. Airy semiclassical position law.** Under the unitary change of variable \(K=k/w_n\) in Fourier space, the normalized scalar eigenfunction becomes \(F_n\) satisfying
\[
 \bigl(-h_n^2\partial_K^2+|K|\bigr)F_n=F_n,
 \qquad h_n=r_n^{-3/2}\longrightarrow0.
\]

Up to a real normalization factor, its explicitly known momentum profile is
\[
 F_n(K)=c_n\,\sigma_n(K)
 \operatorname{Ai}\!\left(\frac{|K|-1}{h_n^{2/3}}\right),
\]
where \(\sigma_n\equiv1\) for odd \(n\), and \(\sigma_n(K)=\operatorname{sgn}(K)\) for even \(n\). The stated Airy root condition ensures continuity and the correct matching derivative at \(K=0\). Let \(X_n=i h_n\partial_K\), which is precisely the dimensionless spatial position \(x/L_n\) on this Fourier representation.

We show weak convergence of the probability law of \(X_n\) to uniform measure on \([-1,1]\). Put \(h=h_n\), and fix \(0<\delta<1/4\). On either closed subinterval satisfying \(\delta<|K|<1-\delta\), the standard Airy oscillatory formula gives uniformly
\[
 F_n(K)=\frac{\sigma_n(K)}{\sqrt2(1-|K|)^{1/4}}
 \left[\sin\!\left(\frac{2(1-|K|)^{3/2}}{3h}+\frac\pi4\right)+o(1)\right].
\]

Here the amplitude \(1/\sqrt2\) follows by normalizing the squared oscillations: \(\int_{-1}^1(1-|K|)^{-1/2}dK=4\), and the oscillatory mean of \(\sin^2\) is \(1/2\). Standard absolute Airy bounds also give, uniformly after normalization, total probability \(O(\sqrt\delta)+o(1)\) in the two \(\delta\)-neighborhoods of turning points \(K=\pm1\), and \(O(\delta)+o(1)\) in \(|K|\le\delta\); the exterior \(|K|>1+\delta\) is exponentially suppressed. These bounds justify discarding all three short regions before taking \(\delta\downarrow0\).

For any fixed real \(t\), translation of momentum by \(ht\) computes the characteristic function:
\[
 \langle F_n,e^{itX_n}F_n\rangle
 =\int_{\mathbb R}\overline{F_n(K)}F_n(K-ht)\,dK.
\]

On the retained interiors, the Airy phase difference tends to \(t\operatorname{sgn}(K)\sqrt{1-|K|}\); the sum of phases has nonzero derivative and its integral vanishes by an elementary nonstationary-phase estimate. The product-of-sines identity therefore yields
\[
 \lim_{n\to\infty}\langle F_n,e^{itX_n}F_n\rangle
 =\frac14\int_{-1}^{1}\frac{\cos\bigl(t\sqrt{1-|K|}\bigr)}{\sqrt{1-|K|}}\,dK
 =\frac{\sin t}{t},
\]
with the value \(1\) at \(t=0\). By the continuity theorem this is weak convergence to the uniform law on \([-1,1]\). The exact virial identity gives \(\mathbb E[X_n^2]=1/3\) for all \(n\), hence uniform integrability of \(|X_n|\), and therefore
\[
 \eta_n=\mathbb E|X_n|\longrightarrow\frac12.
\]
This Airy translation calculation is the critical nontrivial step: the spectrum by itself does not fix the off-diagonal spatial overlap.

**4. The two limiting Schmidt laws.** The known Airy-zero asymptotic \(r_n^3/n^2\to(3\pi/4)^2\) and exact spectral equation imply \(w_n\to\infty\) for fixed \(g,\Omega\), so \(p_n\to1/4\). Insert the limit \(\eta_n\to1/2\) into the exact reduced matrix to obtain \(R_\infty\). Diagonalization gives the two eigenvalues, purity and entropy displayed in the finding.

In the variable-parameter regime, divide \(w_n^3(w_n-\Omega_n)=g_n^2r_n^3\) by \(\Omega_n^4\). Strict monotonicity of \(z^3(z-1)\) on \(z>1\) proves \(w_n/\Omega_n\to z(s)\), hence \(p_n\to p(s)\). The spatial factor \(\eta_n\) depends only on the Airy index after scaling, not on \(g_n,\Omega_n\), so the same limit gives \(R(s)\).

Finally \(p(s)\) decreases strictly from \(1\) to \(1/4\) as \(s\) runs from \(0+\) to \(+\infty\). Since \(\det R(s)=p(s)(1-p(s))/4\), the smaller Schmidt eigenvalue, and hence its binary entropy, increases strictly with \(p(s)(1-p(s))\). This quadratic has its unique maximum at \(p=1/2\). Solving \(z/(4z-3)=1/2\) gives \(z=3/2\), and then the spectral equation yields \(s_*=\sqrt3/\pi\). This establishes the unique maximum and completes the proof.

## Verification

The standalone `verify.py` directly computes Airy roots, solves the original quartic spectral equation, and independently Fourier-transforms normalized Airy momentum eigenfunctions on a large numerical grid. It checks the dimensionless second moment against \(1/3\), the first absolute moment against its \(1/2\) limit, spatial characteristic functions against \(\sin(t)/t\), and reconstructed reduced-matrix eigenvalues and determinants. It also checks the variable-parameter scaling for several finite indices and three positive scaling constants. The packaged script produced **256 passing assertions** with NumPy/SciPy. The finite checks corroborate the formulas; they do not replace the oscillatory-Airy proof of the infinite-level limits.

## Relationship to prior work

Johar and Kraisler (2026) establish the model's self-adjointness, full spectrum, bound eigenvectors and exact Airy-zero energy equation. The present result **uses** those formulas rather than rediscovering them. Exact photon/atomic occupation via virial or Hellmann–Feynman is included solely to normalize the reduced spatial–sector density matrix. The asserted new contribution is the explicit weak spatial Airy law, the limiting **off-diagonal** coherence and Schmidt spectrum, and the uniquely maximized double-scaled Schmidt-entropy crossover.

Lőrinczi and Małecki (2012) investigate the scalar massless relativistic harmonic oscillator, including eigenfunctions and spectral asymptotics. General one-dimensional semiclassical methods help motivate the weak orbit measure; neither that general machinery nor the scalar spectral equation alone specifies the reduced light–matter label entropy of this two-component quadratic-density Hamiltonian. Hiltunen et al. (2024) analyze nonlocal optical models with localized atomic densities and finite bound-state structures; their spectral setting is different. Related polaritonic entanglement works use physically different multimode/dissipative models and bipartitions. No assertion of literature-wide priority or external validation is made.

## Limitations

The profile concerns **spatial versus component-label Schmidt entanglement** in a single-excitation direct-sum Hilbert space. It does not quantify entanglement between independently tensor-factorized photon and atomic Fock spaces. The exact eigenvalue/occupation formulas are prior-derived, not new discoveries. The limits require \(n\to\infty\), and the entropy maximum is for the limiting double-scaled profile, not an established finite-\(n\) optimizer. The atomic density grows quadratically and need not be physically realizable globally; no perturbative robustness for other densities is proved. The earlier scalar oscillator paper was inspected in its lawful open preprint, including its eigenfunction and spectral sections; an unlocated general semiclassical statement with an immediate implication for this mixed-component entropy remains a residual originality risk.

## References

1. Sam Johar and Joseph Kraisler, *Spectral Theory of an Exactly Solvable Quantum-Optical Oscillator*, arXiv:2610.18421 (first public October 13, 2026), Sections 1, 3, 4 and the Airy-eigenvector construction. https://arxiv.org/abs/2610.18421
2. József Lőrinczi and Jacek Małecki, *Spectral Properties of the Massless Relativistic Harmonic Oscillator*, Journal of Differential Equations 253 (2012), DOI:10.1016/j.jde.2012.07.010 (2010 arXiv preprint, 2012 journal; original sections 3.2–3.3 inspected). https://arxiv.org/abs/1006.3665
3. Erik Orvehed Hiltunen, Joseph Kraisler, John C. Schotland and Michael I. Weinstein, *Nonlocal PDEs and Quantum Optics: Bound States and Resonances*, arXiv:2306.10431 (2023 preprint; 2024 publication), Sections 1–2. https://arxiv.org/abs/2306.10431
4. Jian Huang and Zhedong Zhang, *Room-temperature exciton-vibration-photon entanglement in polariton optomechanics*, Physical Review A 112, 013509 (2025), DOI:10.1103/2dfx-23qp (different polaritonic setting; abstract and model summary consulted). https://doi.org/10.1103/2dfx-23qp
