# Exact dark-mode arithmetic and a sharp nonuniform quartet in a lossy SSH chain

## Finding
Let \(H_0\) be the real symmetric open-chain tight-binding Hamiltonian on \(2N\) sites with hopping \(a>0\) between sites \((2j-1,2j)\) and hopping \(b>0\) between sites \((2j,2j+1)\). Add one lossy defect at odd site \(2s-1\):
\[
H=H_0-i\Gamma|2s-1\rangle\langle2s-1|,\qquad \Gamma>0,\quad 1\le s\le N.
\]
Write \(u=s-1\), \(L=N-s+1\), and \(r=b/a\). The complete set of real eigenvalues of \(H\) is
\[
E_{k,\pm}=\pm a\sqrt{1+r^2+2r\cos(k\pi/L)}
\]
for precisely those integers \(1\le k\le L-1\) such that
\[
\sin(uk\pi/L)\ne0,\qquad
r=-\frac{\sin((u+1)k\pi/L)}{\sin(uk\pi/L)}>0.
\tag{1}
\]
Each qualifying \(k\) contributes two independent dark modes. There are no real zero eigenvalues, and none when the loss is at the first or last odd site. Outside this finite set of hopping ratios for fixed \((N,s)\), all states decay in norm.

For \(a\ne b\), four or more exact dark states are impossible when \(N\le13\), and the cutoff is attained at \(N=14\), \(s=3\), \(b/a=\sqrt2\). More generally, every \(m\ge1\) gives an exactly four-dimensional dark subspace for
\[
N=12m+2,\quad s=3,\quad b=\sqrt2a,
\]
with energies
\[
\boxed{E\in\{\pm a\sqrt{2+\sqrt3},\ \pm a\sqrt{2-\sqrt3}\}.}
\]
For the initially occupied first site, the exact limiting survival probability is
\[
\boxed{\lim_{t\to\infty}\|e^{-itH}|1\rangle\|^2=
\frac{2(8m+1)}{3(8m+1)^2-1}.}
\tag{2}
\]
The smallest nonuniform example has \(2N=28\) sites and probability \(9/121\). These statements hold for every \(\Gamma>0\).

## Assumptions and scope
The chain has open boundaries, exactly alternating positive real hoppings, an even number of sites, no other onsite potentials, and a single absorptive onsite term \(-i\Gamma\) on an odd (A-sublattice) site. The evolution \(e^{-itH}\) is the non-Hermitian no-jump evolution; its squared norm is the no-jump probability. Dark means an eigenvector with a real eigenvalue, equivalently zero amplitude at the lossy site. The result does not concern many-particle interactions, even-sublattice losses, disorder, or the Lindblad steady-state density matrix.

## Proof
**Step 1: reality and nodes.** For any right eigenvector \(H\psi=E\psi\), taking imaginary parts of \(\langle\psi,H\psi\rangle=E\|\psi\|^2\) gives
\[
\operatorname{Im}E=-\Gamma\frac{|\psi_{2s-1}|^2}{\|\psi\|^2}.
\]
Thus \(E\) is real exactly when \(\psi_{2s-1}=0\); then \(H_0\psi=E\psi\). Since every hopping is nonzero, an eigenvector of each cut segment has a nonzero endpoint component, by the three-term recurrence. Consequently a node at the lossy site exists exactly when the left and right principal subchains share an eigenvalue. Their eigenvectors are then joined uniquely up to scaling by the matching equation \(b\psi_{2s-2}+a\psi_{2s}=0\). The kernel at each common eigenvalue is one-dimensional. (For the endpoint cases the one-sided boundary recurrence forces the zero vector.)

**Step 2: exact spectral intersection.** The left subchain has \(2u\) sites, and the right subchain has \(2L-1\) sites. The right subchain has a single zero eigenvalue, plus exactly
\[
E_{k,\pm}=\pm\sqrt{a^2+b^2+2ab\cos(k\pi/L)},\qquad 1\le k<L.
\]
Indeed its odd-sublattice surplus yields the zero mode, and the remaining square-singular-value recurrence is diagonalized by sine waves. The even left subchain has no zero eigenvalue because its odd-even coupling block is triangular with nonzero diagonal \(a\). For \(u\ge1\), its nonzero spectral equation is
\[
U_u(t)+rU_{u-1}(t)=0,\qquad
t=\frac{E^2-a^2-b^2}{2ab},
\]
where \(U_j(\cos\theta)=\sin((j+1)\theta)/\sin\theta\) and \(U_0=1\). At a right-hand energy, \(t=\cos(k\pi/L)\). Substitution yields equation (1). If its denominator vanishes, the adjacent numerator cannot vanish for \(1\le k<L\), so no missing cases occur. Both cut matrices are Jacobi matrices with simple spectra; hence the number of real eigenvectors is exactly twice the count of qualifying indices.

**Step 3: sharp cutoff among genuinely dimerized chains.** Two different positive indices \(k,\ell\) from \(1,\ldots,L-1\) yield at least four dark states at the same ratio exactly if
\[
\sin((u+1)k\pi/L)\sin(u\ell\pi/L)
-\sin((u+1)\ell\pi/L)\sin(uk\pi/L)=0
\tag{3}
\]
with both ratios positive. The attached exact-algebra checker examines every integer \(2\le N\le13\), \(2\le s<N\), and every admissible pair \((k,\ell)\). For each finite case it sets \(x\) to a primitive \(2L\)-th root of unity and reduces the integer Laurent polynomial representing (3) modulo the exact cyclotomic polynomial \(\Phi_{2L}(x)\). Positivity is determined exactly from integer multiples of \(\pi/L\). Every detected collision for these lengths satisfies \(r=1\), checked by reducing the identity \(\sin((u+1)k\pi/L)+\sin(uk\pi/L)=0\) modulo the same polynomial. This is a finite **exhaustive exact certificate**, not an inference from floating-point tests. At \(N=14\), \(s=3\), indices \(k=5,11\) give a shared positive, unequal-bond ratio \(r=\sqrt2\), so the bound is sharp.

**Step 4: an infinite quartet and exact retention.** For \(N=12m+2\), \(s=3\), \(r=\sqrt2\), the right-hand angles \(5\pi/12\) and \(11\pi/12\) occur as \(k=5m\) and \(k=11m\). The left four-site squared-energy characteristic polynomial is
\[
(z-2-\sqrt3)(z-2+\sqrt3)=z^2-4z+1,
\qquad z=(E/a)^2.
\]
Its two positive roots correspond to exactly these right-hand angles, so all four left eigenvalues extend to loss-free modes and there can be no fifth one. For their normalized endpoint weights, set \(a=1\), \(b=\sqrt2\), select the unnormalized real eigenvectors with first odd-site amplitude \(A_1=1\), and write \(A_j=\psi_{2j-1}\), \(B_j=\psi_{2j}\). For either angle \(\theta\in\{5\pi/12,11\pi/12\}\), the bulk recursion, \(A_3=0\), and \(A_1=1\) give
\[
A_j=-\frac{\sin((j-3)\theta)}{\sin(2\theta)},\qquad
B_j=\frac{A_j+\sqrt2A_{j+1}}{E},\qquad A_{N+1}=0.
\]
Since \(|\sin(2\theta)|=1/2\), the first two cells contribute squared norm \(2+2z\) (their four amplitudes have squares \(1,z,z,1\)). Each consecutive 12-cell period beginning at cell \(3\) contributes exactly \(48\): the squared odd amplitudes sum to \(24\), and the squared even amplitudes also sum to \(24\), using equally spaced sine phases and \(E^2=z\). There are exactly \(m\) such periods. Consequently
\[
\|\psi_E\|^2=48m+2+2z,
\qquad z\in\{2+\sqrt3,\ 2-\sqrt3\}.
\]
The four dark eigenvectors are mutually orthogonal eigenvectors of the Hermitian \(H_0\). They span a reducing subspace of \(H\), while all complementary eigenvalues have strictly negative imaginary part by Step 1 and the complete classification. Possible Jordan blocks in the decaying complement still decay exponentially times a polynomial. Hence the limiting no-jump norm from \(|1\rangle\) equals the squared orthogonal projection onto the dark subspace:
\[
\frac{2}{48m+6+2\sqrt3}+\frac{2}{48m+6-2\sqrt3}
=\frac{2(8m+1)}{3(8m+1)^2-1},
\]
proving (2), independently of the loss strength.

## Verification
The standalone exact checker `verify.py` uses exact integer cyclotomic polynomial remainders for all finite cases \(2\le N\le13\), proves the first nonunit collision at \((N,s,k,\ell)=(14,3,5,11)\), and verifies the four-site characteristic polynomial and both algebraic energies symbolically. The independent `check_numeric.py` diagonalizes the clean and lossy matrices at \(m=1,2,3\) and verifies the four energies and no-jump limit for those finite cases. Numerical diagonalization is corroboration, not the proof of the infinite family. All decisive infinite-family steps are in the analytic proof above.

## Relationship to prior work
Li, Cardoso, Bergholtz and Jiang (2023 preprint; 2024 publication) introduced the open SSH chain with a localized lossy defect and derived a Chebyshev-form characteristic equation, emphasizing exceptional-point braiding rather than complete real-eigenvalue multiplicity and endpoint survival. Yang, Molignini and Bergholtz (2023) studied dissipative preparation of boundary states in SSH and related systems, including odd-site-count protected zero modes and dissipative spectra; their loss placement and state-selection claims differ from the even-chain A-site-loss arithmetic considered here. Wang and Zhang (2026) described the general nodal criterion for localized-loss dark states and a secular factorization, but did not give this complete finite-chain commensurability classification, sharp unequal-bond cutoff, or endpoint survival formula. These antecedents supply the mechanism and the starting spectral formulas; neither the nodal criterion nor generic existence of protected states is claimed as original. The nontrivial contribution is the arithmetic collision/cutoff and exact length-dependent quartet survival law.

## Limitations
The minimality certificate is exhaustive only over the specified \(N\le13\) finite set, as required for the sharp lower bound; it is not a classification of every equal-hopping resonance at all larger lengths. The analytically proved infinite family covers the exact parameters stated, not perturbations of hopping or defect position. For positive but generic unequal hopping ratios the dark subspace is empty at each finite size. Other published formulations may encode some spectral intersections implicitly; these have been compared by their mathematical implications, and unindexed equivalent collision classifications remain a residual originality risk. The result is about no-jump single-excitation propagation, not a many-body stationary state.

## References
1. Z.-J. Li, G. Cardoso, E. J. Bergholtz and Q.-D. Jiang, *Braids and Higher-order Exceptional Points from the Interplay Between Lossy Defects and Topological Boundary States*, arXiv:2312.03054 (first submitted 2023-12-05); Phys. Rev. Research **6**, 043023 (2024). https://arxiv.org/abs/2312.03054
2. F. Yang, P. Molignini and E. J. Bergholtz, *Dissipative Boundary State Preparation*, arXiv:2305.00031 (first submitted 2023-04-28); Phys. Rev. Research **5**, 043229 (2023). https://arxiv.org/abs/2305.00031
3. Wang and Zhang, localized-loss non-Hermitian lattice study, arXiv:2607.10218 (2026), Sec. III and secular-factorization discussion. https://arxiv.org/abs/2607.10218
4. Q. Zhou, *Recovering dark states by non-Hermiticity*, comparison of dark-state mechanisms in a different coupling geometry. Details and bibliographic identity are not used as a premise of the proof.
