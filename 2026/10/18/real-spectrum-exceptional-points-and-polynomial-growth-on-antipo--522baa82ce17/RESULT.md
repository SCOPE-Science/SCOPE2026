# Real-spectrum exceptional points and polynomial growth on antipodal gain–loss rings

## Finding
Let \(m\ge2\) be an integer and consider the \(2m\)-site periodic nearest-neighbor tight-binding Hamiltonian
\[
H_m(\gamma)=A(C_{2m})+i\gamma\bigl(|0\rangle\langle0|-|m\rangle\langle m|\bigr),\qquad\gamma\ge0,
\]
where every edge has hopping amplitude one. The **entire spectrum is real for \(0\le\gamma\le2\)**, as already characterized by Ortega, Benet, and Larralde. The new assertion concerns exact diagonalizability and the resulting time evolution throughout that real-spectrum interval.

For every \(m\ge3\), the Hamiltonian is **defective at each distinct interior parameter**
\[
\gamma_k=2\sin(k\pi/m),\qquad 1\le k<m/2.
\]
At \(\gamma=\gamma_k\), the eigenvalues \(\pm2\cos(k\pi/m)\) each have algebraic multiplicity three and geometric multiplicity two. Their Jordan normal forms each comprise one size-two Jordan block and one size-one block. The amplitudes of suitable initial states therefore grow linearly with time even though all spectral energies are real:
\[
\|\exp(-itH_m(\gamma_k))\|=\Theta(t)\qquad(t\to+\infty).
\]
Conversely, at every \(0\le\gamma<2\) outside these finitely many values, \(H_m(\gamma)\) is diagonalizable with real spectrum and \(\sup_{t\in\mathbb R}\|\exp(-itH_m(\gamma))\|<\infty\).

At \(\gamma=2\), the zero-energy Jordan structure is one size-two block if \(m\) is odd, and one size-three plus one size-one block if \(m\) is even; the corresponding propagator grows respectively as \(\Theta(t)\) and \(\Theta(t^2)\). At \(\gamma>2\), the eigenvalues \(\pm i\sqrt{\gamma^2-4}\) imply exponential growth. Thus the **first exceptional-point threshold** for \(m\ge3\) is \(2\sin(\pi/m)\), strictly below the fixed complex-spectrum threshold \(2\). The first threshold is asymptotic to \(2\pi/m\).

For \(m=2\), there are no exceptional points strictly inside \((0,2)\): the first occurs at \(\gamma=2\), with zero-energy Jordan blocks of sizes three and one.

## Assumptions and scope
Indices are taken modulo \(2m\), with standard Euclidean vector norm and its induced matrix operator norm. The adjacency matrix \(A(C_{2m})\) has entries one between each pair of nearest neighbors; there are no other onsite potentials. Gain and loss are exactly opposite, equal in magnitude, and have real strength \(\gamma\ge0\). The assertions are exact for every integer \(m\ge2\). A Jordan block refers to an invariant subspace of the given finite-dimensional matrix; polynomial growth refers to the operator norm of its physical-time propagator \(\exp(-itH)\), not to the growth of every individual initial state.

## Proof
**1. Reflection decomposition.** Reflect the ring by \(j\mapsto-j\pmod{2m}\). The reflection fixes the gain and loss vertices. Its odd subspace has basis \((|j\rangle-|-j\rangle)/\sqrt2\), \(1\le j<m\), and the Hamiltonian restricts to the path adjacency matrix \(T_-\) of size \(m-1\), hence
\[
\det(zI-T_-)=U_{m-1}(z/2),
\]
where \(U_q\) is the Chebyshev polynomial of the second kind, normalized by \(U_0=1\), \(U_1(\xi)=2\xi\) and \(U_{q+1}(\xi)=2\xi U_q(\xi)-U_{q-1}(\xi)\).

The even subspace contains the two fixed vertices plus \((|j\rangle+|-j\rangle)/\sqrt2\) for \(1\le j<m\). Its matrix \(T_+(\gamma)\) is a tridiagonal chain of dimension \(m+1\), with off-diagonals \(\sqrt2\) at the two endpoints and one on internal edges, and endpoint diagonals \(+i\gamma\) and \(-i\gamma\).

**2. Exact characteristic polynomial.** At \(\gamma=0\), the full matrix is free cycle adjacency with eigenvalues \(+2,-2\) once each and \(2\cos(k\pi/m)\), \(1\le k<m\), twice each. Therefore \(\det(zI-T_+(0))=(z^2-4)U_{m-1}(z/2)\). Determinant multilinearity in the two endpoint diagonal entries makes the linear terms in \(\gamma\) cancel by endpoint reversal, whereas their product contributes \(+\gamma^2\) times the interior-path determinant \(U_{m-1}(z/2)\). Consequently
\[
\det(zI-T_+(\gamma))=(z^2+\gamma^2-4)U_{m-1}(z/2),
\]
\[
\boxed{\det(zI-H_m(\gamma))=(z^2+\gamma^2-4)U_{m-1}(z/2)^2.}
\]
The two mobile levels are \(\pm\sqrt{4-\gamma^2}\), and the pinned levels \(2\cos(k\pi/m)\) are each algebraically double away from coincidences.

**3. Jordan multiplicities.** An irreducible tridiagonal matrix with all off-diagonal entries nonzero has eigenspaces of dimension one: the first component of an eigenvector recursively determines all subsequent components. All off-diagonals of \(T_+\) are nonzero. Thus a collision of the moving eigenvalue with a root \(2\cos(k\pi/m)\) of \(U_{m-1}\) makes an algebraic double eigenvalue in \(T_+\) with geometric multiplicity one and one length-two Jordan chain. This collision occurs for \(\gamma=2\sin(k\pi/m)\), with \(1\le k<m\); at \(0<\gamma<2\) such values are uniquely indexed by \(1\le k<m/2\), each giving distinct energies \(\pm2\cos(k\pi/m)\). The odd block supplies one independent eigenvector of each pinned energy, proving algebraic multiplicity three and geometric multiplicity two in the full matrix.

At \(\gamma=2\), the quadratic factor is \(z^2\). If \(m\) is odd, \(U_{m-1}(0)\ne0\), and \(T_+\) has one length-two zero Jordan block. If \(m\) is even, \(U_{m-1}(0)=0\) is a simple root and \(T_+\) has one length-three zero Jordan block, while \(T_-\) gives a distinct length-one zero block. Outside the stated collision set, each block has simple eigenvalues and is diagonalizable, and the full block direct sum is diagonalizable even if eigenvalues occur in both blocks.

**4. Dynamical consequence.** Every real-energy Jordan block of length \(r\) contributes a polynomial of degree \(r-1\) to \(e^{-itH}\); an invertible similarity preserves its order of growth in operator norm. The global largest Jordan-block size is two at each interior collision, and two or three at the endpoint according to parity. A diagonalizable matrix with real spectrum has uniformly bounded propagator, since its diagonal phase factors are all unimodular. For \(\gamma>2\), at least one eigenvalue has positive imaginary part, leading to exponential propagator growth. Finally, \(2\sin(\pi/m)\sim2\pi/m\).

## Verification
A standalone checker `verify_antipodal_pt.py` reconstructs the matrices from their definitions and tests symbolic characteristic factorization for five cycle sizes, exact Jordan-nullity patterns at the endpoint and selected interior collisions, independent numerical first-order perturbations away from opposite sites, and real-spectrum values below the threshold. Its finite checks support, but do not replace, the all-size tridiagonal argument. Reproduce with `python verify_antipodal_pt.py` using Python 3, NumPy and SymPy.

## Relationship to prior work
Scott and Joglekar's 2012 ring analysis gives a two-arc tunneling model and a generic gain–loss threshold formula; singular equal-coupling, opposite-defect geometry requires separate attention. Ortega, Benet, and Larralde (2021) directly analyze the **same opposite-site, zero-contact-energy ring**. Their Section III.B and equation (19) establish the pinned states and the moving spectral circle \(E^2+\gamma^2=4\), including the reality threshold \(2\). These spectral facts are **prior work, not novelty claimed here**. The present claim instead determines all finite-strength Jordan collisions and proves that real spectrum need not imply bounded evolution, with the first defective point approaching zero as the ring grows. Znojil's earlier work examines exceptional behavior in other ring-shaped non-Hermitian lattices with distinct onsite/coupling choices; it does not supply this Jordan classification. Broader equivalence through general non-Hermitian matrix analysis remains a possible literature risk.

## Limitations
The result requires perfectly homogeneous hopping, exactly diametrically opposite balanced imaginary onsite potentials, and finite even cycles; any detuning can split the pinned energies. It is not a theorem of noise robustness, nonlinear dynamics, or driven/open density-matrix evolution. Polynomial operator-norm growth is witnessed by suitable vectors and does not imply growth for every initial state. The previously known spectral factorization is an input/rederived identity, not an independent discovery. No exhaustive historical novelty certification or independent validation has been performed.

## References
1. D. D. Scott and Y. N. Joglekar, *PT-symmetry breaking and universal chirality in a PT-symmetric ring*, arXiv:1203.1345v1 (first public 2012-03-06), https://arxiv.org/abs/1203.1345.
2. A. Ortega, L. Benet, and H. Larralde, *Spectra, eigenstates and transport properties of a PT-symmetric ring*, arXiv:2107.00286v1 (first public 2021-07-01), https://arxiv.org/abs/2107.00286, especially Section III.B and equation (19).
3. M. Znojil, *Decays of degeneracies in PT-symmetric ring-shaped lattices*, arXiv:1108.0620v1 (first public 2011-08-02), https://arxiv.org/abs/1108.0620.
4. D. D. Scott and Y. N. Joglekar, *PT-symmetry breaking and maximal chirality in a nonuniform PT-symmetric ring*, arXiv:1207.1945v1 (first public 2012-07-09), https://arxiv.org/abs/1207.1945.
