# Embedded exceptional points and parity-graded amplification in antipodal gain–loss rings

## Finding

For every integer \(m\ge 2\), consider a homogeneous quantum or coupled-mode ring with \(2m\) sites and a gain–loss pair at opposite sites. Write \(H_m(\gamma)\) for the Hamiltonian defined below, with hopping amplitude normalized to one and gain–loss strength \(\gamma\ge 0\). The complete Jordan structure and operator-norm growth of \(e^{-itH_m(\gamma)}\) are classified as follows.

Put
\[
\mathcal K_m=\left\{2\sin\left(\frac{\pi k}{m}\right):1\le k\le\left\lfloor\frac{m-1}{2}\right\rfloor\right\}.
\]
For \(0\le\gamma<2\) outside \(\mathcal K_m\), the Hamiltonian is diagonalizable and has entirely real spectrum, and the propagator is uniformly bounded over real time. At every \(\gamma=2\sin(\pi k/m)\in\mathcal K_m\), the two energies \(E=\pm 2\cos(\pi k/m)\) each have Jordan form \(J_2(E)\oplus J_1(E)\) (algebraic multiplicity three and geometric multiplicity two); all other spectral points are semisimple. Consequently \(\|e^{-itH_m(\gamma)}\|_2=\Theta(t)\) as \(t\to+\infty\), *despite the spectrum remaining entirely real*.

At \(\gamma=2\), the zero-energy Jordan form is \(J_2(0)\) when \(m\) is odd and \(J_3(0)\oplus J_1(0)\) when \(m\) is even, all other spectral points being semisimple. Hence the propagator norm is \(\Theta(t)\) in the odd case and \(\Theta(t^2)\) in the even case. For \(\gamma>2\), the Hamiltonian is diagonalizable, has exactly one nonreal conjugate pair \(\pm i\sqrt{\gamma^2-4}\), and \(\|e^{-itH_m(\gamma)}\|_2=\Theta(e^{t\sqrt{\gamma^2-4}})\).

The spectral polynomial itself is known from earlier work. The finding here concerns the **complete size-uniform Jordan-defect classification, its subthreshold exceptional points, and the resulting exact polynomial growth orders**, not a new eigenvalue formula. The four-site third-order exceptional point at \(\gamma=2\) is also already known.

## Assumptions and scope

The single-particle Hilbert space is \(\mathbb C^{2m}\), with orthonormal basis \(\{|j\rangle:0\le j<2m\}\) and site indices modulo \(2m\). For \(m\ge2\), define
\[
H_m(\gamma)=\sum_{j=0}^{2m-1}\bigl(|j\rangle\langle j+1|+|j+1\rangle\langle j|\bigr)
+i\gamma\bigl(|0\rangle\langle0|-|m\rangle\langle m|\bigr),\quad\gamma\ge0.
\]
Every cycle edge appears once; in particular, the four-site ring has four edges rather than doubled edges. The norm is the Euclidean operator norm, and \(\Theta\) means upper and lower positive constants depending on the fixed \(m,\gamma\), for all sufficiently large positive \(t\). The statements describe linear non-Hermitian Schrödinger/coupled-mode evolution, not norm-preserving quantum probabilities. There is no magnetic flux, disorder, additional onsite energy, or nonlinear saturation.

## Proof

**Reflection decomposition.** Reflection \(R|j\rangle=|2m-j\rangle\) (indices modulo \(2m\)) commutes with \(H_m(\gamma)\). In its even sector, the orthonormal basis is \(|0\rangle\), \((|j\rangle+|2m-j\rangle)/\sqrt2\) for \(1\le j<m\), and \(|m\rangle\). The restricted matrix \(B_m(\gamma)\) is tridiagonal of order \(m+1\), with diagonal entries \(i\gamma,0,\dots,0,-i\gamma\), first and last off-diagonal entries \(\sqrt2\), and all other off-diagonal entries one. The odd sector is the \((m-1)\)-vertex ordinary path adjacency matrix \(A_{m-1}\), with basis \((|j\rangle-|2m-j\rangle)/\sqrt2\). Thus \(H_m(\gamma)\) is unitarily similar to \(B_m(\gamma)\oplus A_{m-1}\).

**Characteristic factors.** Define the Chebyshev polynomials \(U_{-1}=0\), \(U_0=1\), and \(U_j(z/2)=zU_{j-1}(z/2)-U_{j-2}(z/2)\). The path block has characteristic polynomial \(U_{m-1}(z/2)\). For the even block, the tridiagonal determinant recursion begins with \(D_0=1\), \(D_1=z-i\gamma\), \(D_2=z(z-i\gamma)-2\). For \(3\le j\le m\), it obeys \(D_j=zD_{j-1}-D_{j-2}\); at the final row, \(D_{m+1}=(z+i\gamma)D_m-2D_{m-1}\). Using \(D_j=(z-i\gamma)U_{j-1}(z/2)-2U_{j-2}(z/2)\) for \(1\le j\le m\) and the recurrence yields
\[
\det(zI-B_m(\gamma))=(z^2+\gamma^2-4)U_{m-1}(z/2).
\]
Consequently
\[
\det(zI-H_m(\gamma))=(z^2+\gamma^2-4)U_{m-1}(z/2)^2.
\]
This determinant also follows from the previously published zero-flux spectrum, but the block decomposition supplies geometric multiplicities.

**Geometric multiplicities and Jordan blocks.** Since all sub- and superdiagonal entries of \(B_m(\gamma)\) are nonzero, the eigenvector recurrence determines every coordinate from the first. In particular, for any eigenvalue its eigenspace is one-dimensional. Therefore an eigenvalue of algebraic multiplicity \(r\) in \(B_m(\gamma)\) is represented by exactly one block \(J_r\). The odd block \(A_{m-1}\) is real symmetric with distinct eigenvalues \(\mu_j=2\cos(\pi j/m)\), \(1\le j<m\); it contributes one simple block at each \(\mu_j\), for every \(\gamma\).

For \(0\le\gamma<2\), the two other roots are \(\pm\sqrt{4-\gamma^2}\). They collide with fixed roots exactly when \(\gamma=2\sin(\pi k/m)\), taking one representative \(1\le k<m/2\). These strengths are distinct because sine is strictly increasing on \((0,\pi/2)\). At such strengths the even block contains two size-two Jordan blocks, at the distinct energies \(\pm2\cos(\pi k/m)\), while the odd block contributes one simple block at each; outside these strengths the even-block eigenvalues are all simple. At \(\gamma=0\), the entire original Hamiltonian is Hermitian, so repeated eigenvalues do not create defects.

At \(\gamma=2\), the two moving roots both equal zero. When \(m\) is odd, \(U_{m-1}(0)\ne0\); the zero in \(B_m\) has order two, with no zero in the odd block. When \(m\) is even, \(U_{m-1}\) has exactly one simple zero; the even block has a third-order zero and the odd block one additional simple zero. Thus the zero Jordan forms stated in the finding are exhaustive.

For \(\gamma>2\), the two moving roots are the distinct imaginary pair \(\pm i\sqrt{\gamma^2-4}\), disjoint from the real fixed roots, so both sectors are diagonalizable and no other eigenvalue is nonreal.

**Time evolution.** For each finite-dimensional Jordan block \(J_r(E)=EI+N\),
\[
e^{-itJ_r(E)}=e^{-itE}\sum_{q=0}^{r-1}\frac{(-itN)^q}{q!}.
\]
At real \(E\), a largest block of order \(r\) gives an operator-norm upper bound \(O(t^{r-1})\) and a matching lower bound \(\Omega(t^{r-1})\) by applying the propagator to its terminal generalized eigenvector. Similarity to a fixed Jordan basis changes the bounds only by finite nonzero constants. Semisimple real spectra give uniform boundedness; a simple eigenvalue \(+i\sqrt{\gamma^2-4}\) gives the asserted exponential growth, with all other terms bounded or exponentially decreasing. This proves every classification and bound for every \(m\ge2\).

## Verification

The standalone finite checker `checker.py` constructs the full ring Hamiltonian, verifies the characteristic identity symbolically for \(2\le m\le6\), checks exact nullities of powers at \(\gamma=2\), and verifies embedded defect nullities for selected sizes. It separately checks sample matrix-exponential growth exponents numerically. An executed run returned `PASS: 23 independent polynomial, nullity, and propagator checks.` These finite checks support, but do not replace, the unrestricted analytic proof above. For a concrete instance, a six-site ring has embedded defective energies \(\pm1\) at \(\gamma=\sqrt3\); an eight-site ring has quadratic growth at \(\gamma=2\).

## Relationship to prior work

Scott and Joglekar (arXiv:1203.1345, first public 2012-03-06) studied gain/loss impurities on a ring with two possibly different uniform arm hoppings, including the homogeneous and opposite-site specialization. Their central contributions concern the PT-breaking threshold and wave-packet chirality for the broader family, not this complete Jordan-block classification. Their typical large-ring phase-boundary formula should not be applied without its stated finite-size and geometric qualifications to the exactly symmetric specialization here.

Jin and Song (arXiv:1605.08953, 2016-05-29), Section IV, Eq. (11), and Fig. 3 explicitly give the zero-flux fixed doubly-degenerate bands and the moving pair \(\pm\sqrt{4-\gamma^2}\); Section III identifies the \(3\times3\) Jordan block in the four-site ring at \(\gamma=2\). Neither of those spectral facts is claimed as new. The current Jordan classification also identifies *subthreshold* defective eigenvalues where the moving pair intersects a fixed double level, determines geometric multiplicities, and gives all-size polynomial propagator growth including the even-versus-odd half-ring transition.

Ortega, Benet and Larralde (arXiv:2107.00286, first public 2021-07-01), Section III.B and Fig. 3, study stationary singular/opaque levels on the same antipodal zero-onsite family and illustrate the six-site \(\gamma=2\) exceptional point. Their more general ring treats additional real onsite potentials and transport properties. Their displayed eigenvalue and eigenstate formulas substantially overlap the background, but the inspected text does not state the all-size embedded-Jordan/growth classification. The possibility that a general formula yields parts of it under additional work remains a historical-priority risk.

The block decomposition and Jordan argument here add data that the published characteristic polynomial alone does not specify: geometric multiplicities and nilpotent block sizes. No assertion of independent validation or exhaustive historical uniqueness is made.

## Limitations

The theorem requires a finite *even* cycle, diametrically opposite gain and loss, equal real nearest-neighbor hopping, zero flux, and fixed nonnegative \(\gamma\). It does not classify odd cycles, asymmetrically located sites, disordered couplings, nonzero magnetic flux, nonlinear saturation, or generic perturbations. At exceptional strengths, the classification is exact; small experimental detuning can change long-time behavior. Time-evolution norms are unnormalized amplitudes, not detection probabilities. Historical coverage beyond the inspected primary literature has not been exhaustively ruled out; no independent audit has been performed.

## References

1. D. D. Scott and Y. N. Joglekar, *PT-symmetry breaking and universal chirality in a PT-symmetric ring*, arXiv:1203.1345, 2012-03-06. https://arxiv.org/abs/1203.1345 ; published as *PT-symmetry breaking and ubiquitous maximal chirality in a PT-symmetric ring*, Phys. Rev. A 85, 062105 (2012).
2. L. Jin and Z. Song, *Parity-time symmetry under magnetic flux*, arXiv:1605.08953, 2016-05-29. https://arxiv.org/abs/1605.08953
3. A. Ortega, L. Benet, and H. Larralde, *Spectra, eigenstates and transport properties of a PT-symmetric ring*, arXiv:2107.00286, 2021-07-01. https://arxiv.org/abs/2107.00286
4. M. Znojil, *Decays of degeneracies in PT-symmetric ring-shaped lattices*, arXiv:1108.0620, 2011-08-02. https://arxiv.org/abs/1108.0620 (different ring matrix family; conceptual background).
