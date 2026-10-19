# Single-site detuning produces three exact rank regimes in complete bipartite quantum walks

## Finding
For integers \(a,b\ge2\), place an on-site potential \(\tau\in\mathbb R\) on a single vertex \(w\) of the part of size \(a\) in the complete bipartite graph \(K_{a,b}\). Let \(\widehat M_\tau\) be the infinite-time average-mixing matrix for the continuous-time quantum walk with Hamiltonian \(H_\tau=A(K_{a,b})+\tau e_we_w^{\mathsf T}\). Its rank is exactly
\[
\operatorname{rank}\widehat M_\tau=
\begin{cases}
a+b-\mathbf1_{\{a=2\}}-\mathbf1_{\{b=2\}},&\tau=0,\\
a+b-\mathbf1_{\{a=3\}}-\mathbf1_{\{b=2\}},&\tau\ne0.
\end{cases}
\]
Thus introducing any nonzero mark **increases** rank by one for \(a=2\), **decreases** it by one for \(a=3\), and leaves it unchanged for \(a\ge4\). These conclusions hold for every \(b\ge2\), and are insensitive to the sign or nonzero magnitude of the potential. For \(\tau\ne0\), the matrix is positive definite exactly when \(a\ne3\) and \(b\ne2\).

More precisely, at \(\tau=0\), the kernel is the direct sum of the one-dimensional difference spaces associated with the parts of size two, when present. At \(\tau\ne0\), the kernel is the direct sum of the difference between the two *unmarked* vertices of the first part if \(a=3\), and the difference between the two vertices of the second part if \(b=2\); absent the relevant size, that contribution is zero. Every asserted kernel is an exact linear subspace, not merely a bound on rank.

## Assumptions and scope
Graphs are finite, simple, undirected, and unit weighted. The complete bipartite graph has a distinguished left part of \(a\ge2\) vertices, one of which is marked, and a right part of \(b\ge2\) vertices. Standard basis vectors are indexed by vertices. The Hamiltonian is real symmetric and the time evolution is \(U(t)=\exp(itH_\tau)\) (changing the sign of time does not change the conclusion). Define
\[
M(t)_{uv}=|U(t)_{uv}|^2,\qquad
\widehat M_\tau=\lim_{T\to\infty}\frac1T\int_0^T M(t)\,dt.
\]
If \(E_\lambda\) runs over the orthogonal projectors for the **distinct** eigenvalues of \(H_\tau\), spectral averaging gives \(\widehat M_\tau=\sum_\lambda E_\lambda\circ E_\lambda\), with \(\circ\) the entrywise product.

## Proof
**1. The kernel as spectral compression.** For a real vector \(x\), write \(D_x=\operatorname{diag}(x)\). Orthogonality and symmetry of each spectral projector yield
\[
x^{\mathsf T}\widehat M_\tau x
=\sum_\lambda\sum_{u,v}x_u x_v(E_\lambda)_{uv}^{2}
=\sum_\lambda\operatorname{tr}\bigl((E_\lambda D_xE_\lambda)^2\bigr)
=\sum_\lambda\|E_\lambda D_xE_\lambda\|_{\mathrm F}^{2}.
\]
Hence \(x\in\ker\widehat M_\tau\) if and only if \(E_\lambda D_xE_\lambda=0\) for every distinct eigenvalue. This identity handles degenerate eigenspaces without mistakenly separating eigenvectors that have the same eigenvalue.

**2. Nonzero marking: bright spectrum and means.** Suppose \(\tau\ne0\), and put \(p=a-1\), \(q=b\). Partition the vertices into the marked singleton, the \(p\) other left vertices, and the \(q\) right vertices. The three-dimensional subspace of vectors constant on each of these cells has, in its orthonormal cell basis, the exact matrix
\[
Q=\begin{pmatrix}
\tau&0&\sqrt q\\
0&0&\sqrt{pq}\\
\sqrt q&\sqrt{pq}&0
\end{pmatrix}.
\]
Ordering the cells as second/third/first converts \(Q\) into an irreducible symmetric tridiagonal matrix, so its three eigenvalues are real and simple. Its determinant is \(-\tau pq\ne0\), so none coincides with the eigenvalue zero of the dark subspaces. The dark subspaces are precisely the within-cell zero-sum vectors on the sets of sizes \(p\) and \(q\). The zero spectral projector, extended by zero at the marked singleton, is
\[
E_0=0\oplus P_p\oplus P_q,\qquad P_s=I_s-\frac1sJ_s.
\]
For each of the three nonzero (simple) eigenvalues, the corresponding projector has rank one, and its compression of \(D_x\) vanishes exactly when its eigenvector-weighted diagonal mean vanishes. Put
\[
y=\left(x_w,\;\frac1p\sum_{u\in A\setminus\{w\}}x_u,\;\frac1q\sum_{v\in B}x_v\right)^{\mathsf T}.
\]
In the eigenbasis of \(Q\), the three weighted means are the images of \(y\) under the square-entry (intensity) matrix of an orthonormal eigenvector matrix. To prove this intensity matrix is nonsingular, multiply it by the Vandermonde matrix of the three eigenvalues. The resulting columns are the diagonal entries of \(Q^k\) for \(k=0,1,2\). Explicitly, those three columns form
\[
T=\begin{pmatrix}
1&\tau&\tau^2+q\\
1&0&pq\\
1&0&(p+1)q
\end{pmatrix},\qquad \det T=-\tau q\ne0.
\]
The Vandermonde is invertible by spectral simplicity, so vanishing of all three nonzero-eigenvalue compressions is **equivalent** to \(y=0\). In other words, each of the three cell sums must vanish separately.

**3. Nonzero marking: dark compressions.** For \(s\ge2\), the identity \(P_sD_zP_s=0\) for a diagonal vector \(z\in\mathbb R^s\) implies
\[
0=(e_i-e_j)^{\mathsf T}D_z(e_i-e_j)=z_i+z_j\quad\text{for every }i\ne j.
\]
When \(s\ge3\), all coordinates \(z_i\) must therefore vanish. When \(s=2\), the only possibilities are scalar multiples of \((1,-1)\). When \(s=1\), \(P_s=0\) imposes no constraint, but the independently necessary cell-mean condition forces its sole coordinate to zero. Conversely, every size-two contrast annihilates its dark compression, has zero cell sum, and so also annihilates all bright compressions. Applying this to the cells of sizes \(p=a-1\) and \(q=b\) gives precisely the kernel stated above and the nonzero-potential rank formula by rank-nullity.

**4. Zero marking.** For \(\tau=0\), use instead the two parts of sizes \(a,b\). The bright subspace spanned by their normalized all-one vectors has eigenvalues \(\pm\sqrt{ab}\). The zero projector is \(P_a\oplus P_b\). Its compression forces every diagonal coordinate to vanish unless that part has exactly two vertices, in which case the antisymmetric contrast is allowed. Any such contrast has zero mean in its part, and therefore also has zero compression under each of the two rank-one bright projectors. Consequently there are no additional kernel vectors, giving the zero-potential rank formula. This establishes the rank transition at \(\tau=0\); the Cesàro limit and the zero-potential limit need not commute when an eigenvalue merges with the dark spectrum.

## Verification
A standalone Python 3 script `verify.py` (requiring SymPy) verifies the rank classification **by exact rational linear algebra**, using the symmetric commutant rather than the eigenvector formulas in this proof. For each of the \(100\) cases with \(2\le a,b\le6\) and \(\tau\in\{0,\tfrac12,-2,3\}\), it calculates the dimension of the projection of diagonal matrices onto the symmetric commutant of \(H_\tau\). The verified output is `VERIFY_OK exact_commutant_cases= 100`. The proof above, not the finite computation, establishes all sizes and all real potentials.

## Relationship to prior work
Coutinho et al. [1] develop exact methods for continuous-time quantum walks and average mixing under integral graph Hamiltonians; their average-mixing formalism motivates the present exact rank question. Coutinho et al. [2] establish the general commutant perspective, including the link between average-mixing rank and the projection of diagonal matrices. Portugal and Moqadam [3], Sec. IV and Appendix B, diagonalize the modified quantum-search Hamiltonian on **balanced** complete bipartite graphs at a specified search coupling; their eigenvectors supply particularly close prior data, but their observable is search evolution, and they do not state the all-parameter Cesàro rank transition or a classification for all unbalanced part sizes. Baptista et al. [4], Sec. 3.1, investigate ordinary complete bipartite graphs under alternative sampling-time distributions and their possible uniform mixing; there is no marked potential or this rank law. These distinctions concern mathematical statements and implications, not title or wording matches.

## Limitations
The result assumes \(a,b\ge2\), a single diagonal mark, and unweighted full bipartite adjacency. It does not classify stars with the marked vertex in a singleton part, multipartite graphs with three or more parts, multiple defects, arbitrary nonuniform edge couplings, or instantaneous state transfer. The theorem is an exact algebraic identity, not a claimed bound on the smallest positive eigenvalue of \(\widehat M_\tau\); the average-mixing entries can themselves have noncommuting long-time and zero-potential limits at a spectral collision. No assertion of external or independent validation is made. The originality comparison is bounded by the inspected literature; results unavailable or not surfaced in the search could contain stronger statements.

## References
[1] Coutinho, Baptista, Godsil, Spier and Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (18 August 2022), DOI:10.1137/22M1521262. https://arxiv.org/abs/2208.08971

[2] Coutinho, Godsil, Guo and Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1 (11 September 2017). https://arxiv.org/abs/1709.03591

[3] Portugal and Moqadam, *Implementation of Continuous-Time Quantum Walks on Quantum Computers*, arXiv:2212.08889v1 (17 December 2022), especially Sec. IV and Appendix B. https://arxiv.org/html/2212.08889v1

[4] Baptista, Coutinho and Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (31 August 2023), especially Sec. 3.1. https://arxiv.org/html/2308.16378v1
