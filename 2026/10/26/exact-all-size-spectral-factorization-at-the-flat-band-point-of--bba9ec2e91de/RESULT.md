# Exact all-size spectral factorization at the flat-band point of a PT-symmetric Kitaev chain

## Finding

Let \(N\ge 4\) be even, \(J>0\), \(\gamma\ge0\), and \(1\le m\le N/2\). Consider the open-chain Bogoliubov–de Gennes matrix

\[
H_N(\gamma,m)= -\frac J2\sum_{n=1}^{N-1} (|n\rangle\langle n+1|+|n+1\rangle\langle n|)\otimes\sigma_z
+\frac {iJ}2\sum_{n=1}^{N-1} (|n\rangle\langle n+1|-|n+1\rangle\langle n|)\otimes\sigma_x
+\frac {i\gamma}2 (|m\rangle\langle m|-|N+1-m\rangle\langle N+1-m|)\otimes\sigma_z,
\]

which is the zero-chemical-potential, flat-band point \(\mu=0,\delta=J\) with balanced gain and loss at mirror sites. Write \(\chi_{N,m}(\lambda)=\det(\lambda I-H_N(\gamma,m))\), and define

\[
P_4(\lambda)=\lambda^4+\left(\frac{\gamma^2}{4}-2J^2\right)\lambda^2+J^4,
\]

\[
P_6(\lambda)=\lambda^6+\left(\frac{\gamma^2}{2}-3J^2\right)\lambda^4+
\left(3J^4-\frac{\gamma^2J^2}{2}+\frac{\gamma^4}{16}\right)\lambda^2-J^6.
\]

Then the characteristic polynomial is exactly

\[
\chi_{N,1}(\lambda)=\lambda^2\left(\lambda^2-J^2+\frac{\gamma^2}{4}\right)^2(\lambda^2-J^2)^{N-3},
\]

\[
\chi_{N,m}(\lambda)=\lambda^2P_4(\lambda)^2(\lambda^2-J^2)^{N-5},\qquad 2\le m<N/2,
\]

and

\[
\chi_{N,N/2}(\lambda)=\lambda^2P_6(\lambda)(\lambda^2-J^2)^{N-4}.
\]

Consequently, if \(\gamma_{\rm th}(N,m)\) is the infimum of positive \(\gamma\) for which the spectrum is non-real, then

\[
\boxed{\gamma_{\rm th}(N,m)=\begin{cases}2J,&m=1,\\0,&2\le m\le N/2.\end{cases}}
\]

At the end-site setting \(m=1\), the two boundary three-dimensional blocks each become a single size-three Jordan block at \(\gamma=2J\); for \(\gamma>2J\), their moving eigenvalues are non-real. Every interior setting has non-real eigenvalues for arbitrarily small positive \(\gamma\).

## Assumptions and scope

The result is for even finite length \(N\ge4\), open boundary conditions, real hopping and pairing strengths set equal to \(J>0\), zero chemical potential, and a single balanced pair of imaginary on-site potentials of magnitude \(\gamma/2\) at sites \(m\) and \(N+1-m\). The threshold is defined as an infimum, so a zero threshold means that every sufficiently small positive perturbation already produces a non-real eigenvalue. The statement concerns the single-particle \(2N\times2N\) BdG matrix, not the many-body Fock-space spectrum. It does not claim the same classification away from \(\mu=0,\delta=J\), for odd \(N\), or for multiple gain/loss pairs.

## Proof

At the flat-band point the nearest-neighbor block from site \(n+1\) to site \(n\) is

\[
A=-\frac J2\sigma_z+\frac {iJ}2\sigma_x=J|u\rangle\langle v|,
\qquad |u\rangle=\frac{(i,1)^T}{\sqrt2},\quad |v\rangle=\frac{(-i,1)^T}{\sqrt2}.
\]

The vectors \(u,v\) are orthonormal and \(\sigma_z=-(|u\rangle\langle v|+|v\rangle\langle u|)\) in this basis. Thus the Hermitian part decomposes into \(N-1\) independent dimers \((|n,u\rangle,|n+1,v\rangle)\), each with matrix \(\begin{pmatrix}0&J\\J&0\end{pmatrix}\), plus the two zero modes \(|1,v\rangle\) and \(|N,u\rangle\). The gain/loss term couples \(|m,u\rangle\) to \(|m,v\rangle\) with amplitude \(-i\gamma/2\), and the mirrored site couples its two basis vectors with amplitude \(+i\gamma/2\).

For \(m=1\), the only affected subspaces are \((|1,v\rangle,|1,u\rangle,|2,v\rangle)\) and its right-edge counterpart. Their matrices have off-diagonals \((-i\gamma/2,J)\) and \((+i\gamma/2,J)\), respectively, so each has characteristic polynomial \(\lambda(\lambda^2-J^2+\gamma^2/4)\). The other \(N-3\) dimers contribute \((\lambda^2-J^2)^{N-3}\). This proves the first factorization. The moving roots are real exactly when \(\gamma\le2J\). At equality each three-dimensional block has characteristic polynomial \(\lambda^3\) and rank two, hence one size-three Jordan block.

For \(2\le m<N/2\), the two perturbations act on disjoint four-dimensional subspaces, each consisting of two adjacent dimers joined by one imaginary link. A block with off-diagonals \((J,\mp i\gamma/2,J)\) has characteristic polynomial \(P_4\); the remaining modes are two zero modes and \(N-5\) untouched dimers. The discriminant of \(P_4\), regarded as a quadratic in \(x=\lambda^2\), is

\[
\gamma^2\left(\frac{\gamma^2}{16}-J^2\right),
\]

which is negative for \(0<\gamma<4J\). Therefore its \(x\)-roots are non-real, and so are the corresponding \(\lambda\)-roots, proving zero threshold in this case.

For \(m=N/2\), the two four-dimensional boundary pieces overlap in the central dimer and form one six-dimensional tridiagonal block with off-diagonals \((J,-i\gamma/2,J,+i\gamma/2,J)\). The determinant recurrence \(D_k(\lambda)=\lambda D_{k-1}(\lambda)-a_{k-1}^2D_{k-2}(\lambda)\) gives \(P_6\); the two zero modes and \(N-4\) untouched dimers give the stated factorization. At \(\gamma=0\), the central block has three independent eigenvectors at eigenvalue \(+J\). Projecting the perturbation onto their span gives

\[
\frac{i\gamma}{4}\begin{pmatrix}0&-1&0\\-1&0&1\\0&1&0\end{pmatrix},
\]

whose eigenvalues are \(0,\pm i\gamma/(2\sqrt2)\). Degenerate perturbation theory therefore gives non-real eigenvalues for arbitrarily small positive \(\gamma\), proving the remaining zero-threshold case.

## Verification

The proof is finite-dimensional and exact. The accompanying standard-library checker constructs the original BdG matrix, transforms it into the \((u,v)\) basis, checks the dimer-plus-onsite-coupling structure for every site position in several even sizes, and independently checks the three tridiagonal characteristic-polynomial recurrences at several positive rational gain/loss strengths. These finite checks test the algebra and matrix conventions; the all-size statement follows from the explicit invariant-subspace decomposition and determinant recurrences above, not from numerical extrapolation.

## Relationship to prior work

Agarwal and Joglekar studied the same position-dependent gain/loss perturbation, reported numerical threshold profiles for even chains, derived a small odd-chain case, and identified the third-order exceptional point at \(\mu=0,\delta=J,m=1,\gamma=2J\). Kawabata, Ashida, Katsura, and Ueda studied the edge-gain/loss Kitaev/Majorana chain and identified the sweet-spot PT boundary \(\gamma=2J\). The threshold at the edge and the existence of an exceptional point are therefore not claimed as new. The contribution here is the exact all-even-size characteristic-polynomial factorization for all mirror-pair positions at this point, including the sharp separation between the protected end pair and every interior pair.

## Limitations

The result relies on exact dimerization at \(\mu=0,\delta=J\); perturbing either parameter couples the dimers and invalidates these factorizations. The zero-threshold assertion is an infimum statement and does not describe the magnitude of the imaginary parts at finite \(\gamma\). No claim is made about non-Hermitian eigenvector conditioning away from the size-three exceptional blocks, the many-body spectrum, or robustness to disorder and interactions. Literature priority for an equivalent all-position factorization cannot be ruled out solely by search; the inspected primary papers state the edge threshold and numerical position dependence but do not state these factorization formulas.

## References

1. K. S. Agarwal and Y. N. Joglekar, “PT-symmetry breaking in a Kitaev chain with one pair of gain-loss potentials,” arXiv:2103.07058v1 (first public version: 2021-03-12).
2. K. Kawabata, Y. Ashida, H. Katsura, and M. Ueda, “Parity-time-symmetric topological superconductor,” arXiv:1801.00499v1 (first public version: 2018-01-01), later Phys. Rev. B 98, 085116 (2018).
