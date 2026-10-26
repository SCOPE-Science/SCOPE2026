# Quadrupole oscillations survive the collective-spin dipole overdamping threshold

## Finding

For the exactly solvable precession-plus-dephasing Lindbladian on any spin-\(j\) representation with \(j\ge1\), the five quadrupole modes exhibit two distinct exceptional-point thresholds. The rank-two odd-parity threshold is \(\eta=2/3\), whereas its even-parity threshold is \(\eta_* = 3.379224327784561\ldots\), where \(\eta_*\) is the square root of the unique positive zero of \(9s^3-103s^2+4s-16\). The three dipole modes are nonoscillatory for \(\eta\ge2\). Consequently, in the open interval \(2<\eta<\eta_*\), every dipole observable has only real-rate relaxation while an explicitly preparable quadrupole observable retains a nonzero, exponentially damped oscillatory component. These oscillations are finite-size transients, not persistent time-crystal order.

## Assumptions and scope

Fix any integer or half-integer \(j\ge1\), and let the standard Hermitian spin operators satisfy \([J_a,J_b]=i\epsilon_{abc}J_c\) on \(\mathbb C^{2j+1}\). For \(\Omega>0\), \(N>0\), and \(\Gamma\ge0\), define
\[
\mathcal L(\rho)=-i\Omega[J_x,\rho]+\frac{\Gamma}{N}\left(J_z\rho J_z-\tfrac12\{J_z^2,\rho\}\right),\qquad \eta=\frac{\Gamma}{2N\Omega}.
\]
For an array of \(N\ge2\) symmetrically coupled spin-half constituents, take \(j=N/2\). Time is measured in units \(\Omega^{-1}\), so \(\mathcal L/\Omega=-i\operatorname{ad}(J_x)-\eta\operatorname{ad}(J_z)^2\). The claims concern precisely the rank-one (dipole) and rank-two (quadrupole) operator sectors, not the whole Liouvillian for arbitrary \(j\).

## Proof

**Invariant irreducible sectors.** As in the exact spherical-tensor representation in the first reference, the operator space is the orthogonal direct sum \(\bigoplus_{k=0}^{2j}\mathcal T_k\), where \(\mathcal T_k=\operatorname{span}\{T^k_q:-k\le q\le k\}\) has dimension \(2k+1\) and both adjoint angular-momentum operators preserve each sector. More explicitly,
\[
[J_z,T^k_q]=qT^k_q,\qquad
[J_\pm,T^k_q]=\sqrt{k(k+1)-q(q\pm1)}\,T^k_{q\pm1}.
\]
Therefore the restriction is the finite matrix \(B_k=-iK_x^{(k)}-\eta(K_z^{(k)})^2\). It commutes with the involution \(R|q\rangle=|-q\rangle\). The symmetric and antisymmetric eigenspaces of \(R\) split the spin-two block into the following matrices, in orthonormal reflection-adapted bases:
\[
B_{2,-}=\begin{pmatrix}-\eta&-i\\-i&-4\eta\end{pmatrix},\qquad
B_{2,+}=\begin{pmatrix}0&-i\sqrt3&0\\-i\sqrt3&-\eta&-i\\0&-i&-4\eta\end{pmatrix}.
\]
Here the even block is ordered with the \(q=0\) vector first. Their characteristic polynomials, computed by direct determinants, are
\[
p_-(z)=z^2+5\eta z+4\eta^2+1,\qquad p_+(z)=z^3+5\eta z^2+(4\eta^2+4)z+12\eta.
\]

**Two exact rank-two thresholds.** The quadratic discriminant is \(\Delta_-=9\eta^2-4\). Thus the odd block has a complex-conjugate pair for \(0\le\eta<2/3\), a repeated root at \(\eta=2/3\), and two distinct real eigenvalues for \(\eta>2/3\). Its nonzero off-diagonal entries make the repeated root defective. Direct expansion of the cubic discriminant gives
\[
\Delta_+=16Q(\eta^2),\qquad Q(s)=9s^3-103s^2+4s-16.
\]
For \(0\le s\le1\), write \(Q(s)=s^2(9s-103)+(4s-16)<0\). For \(1\le s\le10\), use \(9s^3\le90s^2\), so \(Q(s)\le-13s^2+4s-16<0\). Moreover \(Q(10)=-1276<0\), \(Q(12)=752>0\), and \(Q'(s)=27s^2-206s+4>0\) for \(s\ge10\), because \(Q'(10)=644\) and \(Q''(s)=54s-206>0\) there. Consequently \(Q\) has precisely one positive zero \(s_*\in(10,12)\). Put \(\eta_*=\sqrt{s_*}\). Cubic-discriminant signs give one real and one nonreal pair for \(0\le\eta<\eta_*\), a repeated real root at \(\eta=\eta_*\), and three simple real roots for \(\eta>\eta_*\). The repeated root is not triple: the depressed-cubic linear coefficient is \(4-(13/3)\eta^2\), which is nonzero at \(\eta_*^2>10\). The unreduced three-site tridiagonal matrix has one-dimensional eigenspaces because both adjacent off-diagonal entries are nonzero. Hence the double eigenvalue is an exceptional point of order two.

**Dipole contrast.** In the rank-one block the antisymmetric mode has eigenvalue \(-\eta\), and the two remaining modes have polynomial \(z^2+\eta z+1\). Both roots are real and distinct for \(\eta>2\). Hence every dipole expectation is a linear combination of nonoscillatory real-rate decays in that interval. (The boundary \(\eta=2\) permits a polynomial times a real exponential.)

**A physical quadrupole witness.** Let \(Q_{zz}=3J_z^2-j(j+1)I\). This is a nonzero traceless Hermitian element of \(\mathcal T_2\) for \(j\ge1\), proportional to \(T^2_0\). For sufficiently small nonzero real \(\varepsilon\), \(\rho_0=I/(2j+1)+\varepsilon Q_{zz}\) is a positive trace-one density matrix, by the finite-dimensional operator-norm bound \(|\varepsilon|\|Q_{zz}\|<1/(2j+1)\). The Hilbert-Schmidt response \(\operatorname{tr}(Q_{zz}e^{t\mathcal L}\rho_0)\) is a positive scalar multiple of the even-block matrix element \([e^{\Omega tB_{2,+}}]_{00}\). Its Laplace transform, with dimensionless spectral variable \(z\), is
\[
[(zI-B_{2,+})^{-1}]_{00}=\frac{(z+\eta)(z+4\eta)+1}{p_+(z)}.
\]
The numerator is coprime to \(p_+\) for \(\eta>0\): since \(p_+(z)=z[(z+\eta)(z+4\eta)+1]+3(z+4\eta)\), any common zero would require \(z=-4\eta\), at which the numerator is \(1\). Thus both nonreal eigenvalues have nonzero residues for \(2<\eta<\eta_*\), giving an actual damped oscillatory term in the real quadrupole expectation, despite complete dipole overdamping.

## Verification

Running \(\texttt{python verify\_quadrupole.py}\) with SymPy and NumPy checks the exact characteristic polynomials and discriminants, computes the uniquely characterized positive threshold, and compares the rank-two spectrum against an independently assembled spin-\(j\) Lindbladian for five values of \(j\) and eleven rates (55 finite comparisons). The maximum eigenvalue mismatch across those checks was \(7.35\times10^{-8}\), occurring near a defective point where floating-point eigenvalues are ill-conditioned. A separate dimensionless test at \(\eta=5/2\) finds a nonreal even quadrupole pair while the three dipole eigenvalues are real. These finite calculations corroborate, but do not replace, the analytic proof for every \(j\ge1\).

## Relationship to prior work

Nemeth, Nazir, Slager, and Principi (arXiv:2604.14291v1, 15 April 2026) derive the exact spherical-tensor block generator and compute the rank-one dipole spectrum. Their generic finite-rank matrix formulas imply a way to compute our rank-two matrices, which are **not** new as algebraic starting data. The additional result here is the complete rank-two exceptional-point classification, its unique cubic threshold, and the physical quadrupole witness in the interval with no dipole oscillations. Nemeth, Principi, and Nazir (arXiv:2507.06998, first public 9 July 2025; inspected version 2) study the same dephasing/precession class in a different normalization, including weak-dissipation spectra and dipole dynamics; the inspected text does not give these exact finite-strength rank-two thresholds. A more general existing theory of spin-multipole exceptional points could subsume this result; no universal priority claim is made.

## Limitations

The two thresholds classify only rank-one and rank-two operator sectors. Higher multipoles may have other complex eigenvalues even above \(\eta_*\). The quadrupole oscillation is damped and initial-state dependent, not persistent time-crystalline order. Claims of direct experimental detectability, robustness to extra Hamiltonian terms or noise, and novelty across inaccessible literature are not established. At \(\eta=0\), the two block decompositions remain valid but the dephasing threshold interpretation concerns \(\eta>0\).

## References

1. D. Nemeth, A. Nazir, R.-J. Slager, and A. Principi, *Operator Space Transport and the Emergence of Boundary Time Crystals*, arXiv:2604.14291v1 (15 April 2026), especially Sec. IV.1 and App. E, https://arxiv.org/html/2604.14291v1.
2. D. Nemeth, A. Principi, and A. Nazir, *Analytical solution of boundary time crystals via the superspin basis*, arXiv:2507.06998 (first public 9 July 2025; inspected v2), Sec. IV.2, https://arxiv.org/html/2507.06998v2.
