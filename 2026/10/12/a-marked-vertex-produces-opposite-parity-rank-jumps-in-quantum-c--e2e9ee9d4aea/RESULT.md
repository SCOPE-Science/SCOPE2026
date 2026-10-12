# A marked vertex produces opposite parity rank jumps in quantum cycles

## Finding
For every integer \(n\ge3\) and every real potential \(\tau\), consider the undirected unweighted cycle \(C_n\) with one distinguished vertex labeled \(0\). The real symmetric Hamiltonian is
\[
H_\tau=A(C_n)+\tau e_0e_0^{\mathsf T},
\]
where \(A(C_n)\) has a \(1\) for each cycle edge, and \(e_0\) is the coordinate vector at the marked vertex. Its continuous-time transition matrix is \(U_\tau(t)=\exp(itH_\tau)\). Write \(\circ\) for entrywise product and define the long-time (Cesàro) quantum average-mixing matrix by
\[
\widehat M_\tau=\lim_{T\to\infty}\frac1T\int_0^T U_\tau(t)\circ\overline{U_\tau(t)}\,dt.
\]

**Theorem.** The limit exists for every specified parameter and its exact rank is
\[
\boxed{\operatorname{rank}\widehat M_\tau=\begin{cases}
n,&\tau=0\text{ and }n\text{ odd},\\
n/2,&\tau=0\text{ and }n\text{ even},\\
\lfloor n/2\rfloor+1,&\tau\ne0.
\end{cases}}
\]
Thus a nonzero single-site potential decreases the mixing rank by \((n-1)/2\) for odd \(n\) and increases it by one for even \(n\), no matter how small its magnitude or which nonzero sign it has. The zero-potential cycle formulas are known [1]; the result identifies their complete nonzero-potential transition.

**Exact moment certificate.** Put \(m=\lfloor n/2\rfloor\). Take the vertices of distances \(r=0,\ldots,m\) from the mark as representatives of the reflection orbits and define
\[
d_k(r)=(H_\tau^k)_{rr}.
\]
The square matrix with rows indexed by \(r=0,\ldots,m\) and columns \(\mathbf1,d_1,d_3,\ldots,d_{2m-1}\) has determinant exactly
\[
\boxed{(-1)^m\tau^m.}
\]
It furnishes a direct rational/integer certificate of the nonzero-potential rank lower bound, without evaluating eigenvalues numerically.

## Assumptions and scope
All cycles are simple, finite, undirected and unweighted, with \(n\ge3\). No restrictions are placed on the real onsite potential \(\tau\). The Hamiltonian uses the adjacency convention (not the Laplacian) and the potential is a diagonal entry at precisely one vertex. Time is real and the average is the infinite-time uniform Cesàro average. The rank is the ordinary real matrix rank of \(\widehat M_\tau\), not its nonnegative or completely positive semidefinite rank. Vertex labeling is immaterial by cycle rotations.

## Proof
**1. The spectral identity.** Any real symmetric Hamiltonian has a decomposition \(H=\sum_\lambda\lambda E_\lambda\), where the \(E_\lambda\) are mutually orthogonal real spectral projectors. Entrywise time averaging kills distinct frequencies and gives the identity [1,2]
\[
\widehat M(H)=\sum_\lambda E_\lambda\circ E_\lambda.
\]
When the eigenvalues are simple, write each projector as \(v_jv_j^{\mathsf T}\) with \(v_j\) a real unit eigenvector. The preceding identity becomes
\[
\widehat M(H)=\sum_j s_js_j^{\mathsf T},\qquad s_j=v_j\circ v_j.
\]
Hence \(\operatorname{rank}\widehat M(H)\) equals the dimension of the span of its squared eigenvectors \(s_j\). Furthermore, for every nonnegative integer \(k\), the diagonal-moment vector \(d_k=((H^k)_{vv})_v\) satisfies
\[
d_k=\sum_j\lambda_j^k s_j.
\]
In particular, every diagonal-moment vector lies in that span.

**2. Simplicity after any nonzero marking.** Let \(R\) be the reflection of the cycle about vertex \(0\), sending the residue class \(r\) to \(-r\). Both \(A(C_n)\) and the marking commute with \(R\). Write the real state space as the direct sum of the reflection-even and reflection-odd sectors. Put \(m=\lfloor n/2\rfloor\). The even-sector restriction of the unmarked adjacency matrix has \(m+1\) *distinct* eigenvalues
\[
\lambda_k=2\cos(2\pi k/n),\qquad k=0,1,\ldots,m.
\]
Every corresponding unit even eigenvector has a nonzero coordinate at vertex \(0\): these are the discrete cosine vectors, with the root coordinate equal to \(1/\sqrt n\) for their singleton Fourier frequencies and \(\sqrt{2/n}\) for paired frequencies. The odd sector has the unmarked eigenvalues \(\lambda_k\) for \(1\le k<n/2\), each once, and the odd vectors vanish at the mark. Thus marking leaves the odd eigenvalues unchanged.

On the even sector, the mark is the rank-one perturbation \(\tau uu^{\mathsf T}\), where the vector \(u\) has nonzero inner product with *every* unperturbed even eigenvector. For each even-sector unperturbed eigenvalue \(\lambda_k\), the characteristic polynomial of the perturbed even-sector restriction has value
\[
-\tau\,|\langle u,v_k\rangle|^2\prod_{\ell\ne k}(\lambda_k-\lambda_\ell),
\]
up to the nonzero conventional leading-sign factor. For \(\tau\ne0\) this is nonzero, so **no perturbed even eigenvalue equals an odd-sector eigenvalue**. The even-sector matrix, in the normalized distance-shell basis, is an irreducible real symmetric tridiagonal (Jacobi) matrix with positive off-diagonal entries; its eigenvalues are simple. The odd-sector eigenvalues are themselves distinct. Consequently **all eigenvalues of \(H_\tau\) are simple whenever \(\tau\ne0\)**.

**3. Reflection upper bound.** For \(\tau\ne0\), each simple eigenvector has definite reflection parity: \(Rv_j=\pm v_j\). Its entrywise square \(s_j\) is therefore constant on the reflection orbits. The reflection has precisely \(m+1\) vertex orbits, represented by the distances \(0,1,\ldots,m\). Every \(s_j\) belongs to their \((m+1)\)-dimensional invariant-vector space. Step 1 consequently gives
\[
\operatorname{rank}\widehat M_\tau\le m+1.
\]

**4. Exact moment lower bound.** For \(s=0,\ldots,m-1\), consider the diagonal moments of odd length \(2s+1\). A term in \((H_\tau^{2s+1})_{rr}\) is a closed walk of that length on the cycle, allowing a stay at vertex \(0\) with weight \(\tau\). A closed odd walk without a stay is impossible when its length is below \(n\): for even cycles this follows from bipartiteness; for odd cycles a closed odd walk must wind at least once around the length-\(n\) cycle. Since \(2s+1\le2m-1<n\), every contributing walk must visit the marked vertex and use at least one marked stay.

A vertex at distance \(r\) from the mark needs at least \(r\) cycle edges to reach the mark and \(r\) to return. Hence
\[
d_{2s+1}(r)=0\quad\text{if }r>s.
\]
For \(r=s<m\), a contributing walk of the minimum possible length \(2r+1\) must follow the unique shortest path to the mark, make exactly one stay, and follow that path in reverse. Its weight is precisely \(\tau\). Therefore
\[
d_{2s+1}(s)=\tau\quad(0\le s<m),
\qquad d_{2s+1}(m)=0\quad(0\le s<m).
\]
Form the \((m+1)\)-square matrix \(W\) with rows indexed by distance shells \(r=0,\ldots,m\) and columns
\[
W=[\mathbf1,d_1,d_3,\ldots,d_{2m-1}].
\]
Its first column is all ones; each remaining column vanishes below its diagonal-shell position, has diagonal-shell entry \(\tau\), and has zero final row. Subtract the final row from all preceding rows and expand along that final row. The resulting triangular minor has diagonal entries all equal to \(\tau\), proving
\[
\det W=(-1)^m\tau^m.
\]
For \(\tau\ne0\), this determinant is nonzero. The \(m+1\) vectors in the columns of \(W\) are restrictions of genuine diagonal-moment vectors, which by Step 1 belong to the span of squared eigenvectors. Thus
\[
\operatorname{rank}\widehat M_\tau\ge m+1.
\]
This agrees with the upper bound from Step 3 and proves the nonzero-marking case.

**5. Zero potential.** For \(\tau=0\), the known Fourier-projector calculation for cycles [1, Lemma 6.1] gives, for odd \(n\),
\[
\widehat M_0=\frac{n-1}{n^2}J+\frac1n I,
\]
and for even \(n\),
\[
\widehat M_0=\frac{n-2}{n^2}J+\frac1n(I+P^{n/2}),
\]
where \(J\) is the all-ones matrix and \(P\) is the cyclic permutation matrix. The former is positive definite (rank \(n\)). In the latter, the vectors antisymmetric under the half-turn \(P^{n/2}\) constitute the kernel; its dimension is \(n/2\), hence the matrix also has rank \(n/2\). The full piecewise theorem follows.

## Verification
The standalone `verify.py` works for Python 3; NumPy is optional and is used only for independent floating-point spectral checks. Run `python verify.py`. The exact-arithmetic section computes integer powers of the marked adjacency matrix and the determinant of the distance-shell odd-moment witness by fraction-free elimination for \(n=3,\ldots,22\) and \(\tau\in\{-3,-1,1,2\}\), obtaining precisely \((-1)^m\tau^m\) in all 80 cases. With NumPy present, a second spectral routine computes the average-mixing matrix from projectors at \(n=3,\ldots,18\) for six signed and zero potentials, checking the predicted ranks, stochasticity, symmetry, and known unmarked formulas (96 profiles, 12,624 tested entries). These are finite consistency checks; the proof in Steps 1–5 applies without bound to all \(n\) and all real \(\tau\).

## Relationship to prior work
The Fourier formulas for unmarked cycles and hence both \(\tau=0\) rank values are due to Godsil [1, Lemma 6.1] and are not claimed as new. The spectral-projector and squared-eigenvector methods originate in the established average-mixing literature [1,2]. The source [3] gives methods for exact long-time quantum-walk quantities for integral graph Hamiltonians; its cited cycle examples do not cover a nonintegral diagonal marking parameter. A study of single-point defects [4] treats the infinite-line localization/scattering problem, a different graph and observable. The review [5, Section 4] explains why the rank of the average-mixing matrix is a natural invariant and surveys general bounds. None of the inspected parts of [1–5] gives the nonzero-marked finite-cycle rank law or its moment determinant. The full claim is the parity-dependent **change of rank** under the defect, not the already-known unmarked baseline or the general Gram identity.

## Limitations
This theorem concerns *one* diagonal onsite potential on an otherwise unweighted homogeneous cycle; it does not treat several defects, irregular edge couplings, the Laplacian Hamiltonian, finite averaging times, rates of Cesàro convergence, or distinct notions of matrix rank such as nonnegative rank. The limiting matrix can change rank discontinuously at zero potential because spectral degeneracies change; there is no claim of discontinuity for finite-time dynamics. Literature searching and inspected articles cannot logically rule out every unlocated stronger theorem or equivalent formulation. No independent human audit has been performed.

## References
[1] Chris Godsil, *Average Mixing of Continuous Quantum Walks*, Journal of Combinatorial Theory, Series A 120 (2013), 1649–1662; arXiv:1103.2578, https://arxiv.org/pdf/1103.2578, especially Lemma 6.1.

[2] Gabriel Coutinho, Chris Godsil, Krystal Guo, and Hanmeng Zhan, *A New Perspective on the Average Mixing Matrix*, Electronic Journal of Combinatorics 25 (2018), P4.14; arXiv:1709.03591, https://arxiv.org/pdf/1709.03591.

[3] Gabriel Coutinho, Pedro Ferreira Baptista, Chris Godsil, Thomás Jung Spier, and Reinhard Werner, *Irrational Quantum Walks*, SIAM Journal on Applied Algebra and Geometry 7 (2023), 567–584; arXiv:2208.08971, first posted 2022-08-18, https://arxiv.org/pdf/2208.08971.

[4] Zhi-Jian Li and J. B. Wang, *Single-point position and transition defects in continuous time quantum walks*, arXiv:1502.04289, https://arxiv.org/pdf/1502.04289.

[5] Gabriel Coutinho and Krystal Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236, https://arxiv.org/pdf/2404.02236, especially Section 4.
