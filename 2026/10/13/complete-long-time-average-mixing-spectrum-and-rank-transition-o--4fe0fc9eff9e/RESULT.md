# Complete long-time average-mixing spectrum and rank transition of Hamming graphs

## Finding
For every pair of integers \(q\ge2\), \(d\ge1\), let \(H(d,q)\) be the Cartesian power of the complete graph \(K_q\), on \(q^d\) vertices, with its unweighted adjacency Hamiltonian. Its infinite-time Cesàro average mixing matrix has exactly the following **indexed eigenvalue list** (coincident values are counted with their combined multiplicities):
\[
\lambda_j(q)=\frac1{q^j}\sum_{a=0}^{\lfloor j/2\rfloor}\frac{j!}{a!^2(j-2a)!}(q-2)^{j-2a},\qquad
\operatorname{mult}(\lambda_j)=\binom dj(q-1)^j,\quad 0\le j\le d.
\]
Consequently, for every \(d\ge1\), the matrix is positive definite if and only if \(q\ge3\). Its rank is \(q^d\) for \(q\ge3\), and is exactly \(2^{d-1}\) when \(q=2\). The positive eigenvalues for the binary case have indices \(j=2a\) and values \(4^{-a}\binom{2a}{a}\); odd-index eigenvalues vanish. In particular, every nonbinary Hamming graph, at any diameter, has a full-rank Cesàro mixing matrix.

## Assumptions and scope
The graph has vertex set \((\mathbb Z/q\mathbb Z)^d\), with two vertices adjacent precisely when they differ in exactly one coordinate. The Hamiltonian is the *ordinary, unweighted adjacency matrix* \(A\), without time normalization or magnetic phases. Set \(U(t)=\exp(itA)\), \(M(t)_{uv}=|U(t)_{uv}|^2\), and
\[
\widehat M=\lim_{T\to\infty}\frac1T\int_0^T M(t)\,dt.
\]
The limit exists entrywise since all adjacency eigenvalue differences are integer multiples of \(q\). The eigenvalues above refer to the real symmetric \(q^d\)-by-\(q^d\) matrix \(\widehat M\), not the graph adjacency matrix or the instantaneous mixing matrices. No prime-power assumption is imposed on \(q\).

## Proof
For \(K_q\), the adjacency is \(J_q-I_q\). Writing \(\theta=qt\), its evolution is
\[
U_q(t)=e^{-it}\left[I_q+\frac{e^{i\theta}-1}{q}J_q\right].
\]
The off-diagonal squared modulus is \(b(t)=2(1-\cos\theta)/q^2\), whereas each diagonal probability is \(1-(q-1)b(t)\). Thus
\[
M_q(t)=a(t)I_q+b(t)J_q,\qquad a(t)=1-qb(t)=\frac{q-2+2\cos\theta}{q}.
\]
On the all-ones direction \(M_q(t)\) has eigenvalue \(1\); on its orthogonal complement it has eigenvalue \(a(t)\). Because the adjacency of \(H(d,q)\) is a sum of commuting coordinate adjacencies, its evolution and mixing matrix factor *at the same time*:
\[
U(t)=U_q(t)^{\otimes d},\qquad M(t)=M_q(t)^{\otimes d}.
\]
Choose a tensor-product eigenbasis in which each factor lies either in the constant direction or in its \((q-1)\)-dimensional orthogonal complement. If exactly \(j\) factors are nonconstant, the instantaneous mixing eigenvalue is \(a(t)^j\), and the eigenspace dimension is \(\binom dj(q-1)^j\). Averaging over the common period \(2\pi/q\) yields
\[
\lambda_j(q)=\frac1{2\pi q^j}\int_0^{2\pi}(q-2+2\cos\theta)^j\,d\theta
=\frac1{q^j}[z^0](q-2+z+z^{-1})^j.
\]
Here \([z^0]\) means the constant Laurent coefficient. In its expansion, selecting \(a\) positive and \(a\) negative powers from the \(j\) factors and taking \(j-2a\) constants yields the claimed finite sum. No other eigenvalues occur because the multiplicities sum to \(q^d\) by the binomial theorem.

For \(q\ge3\), each summand is nonnegative and the term \(a=0\), equal to \((q-2)^j\), is strictly positive, including \(j=0\); hence every eigenvalue is strictly positive. For \(q=2\), the Laurent polynomial is \(z+z^{-1}\), whose odd powers have zero constant coefficient and whose \(2a\)-th power has constant coefficient \(\binom{2a}{a}\). Therefore the rank is \(\sum_{j\text{ even}}\binom dj=2^{d-1}\). This proves the full statement for all stated integers.

An independent spectral-projector derivation checks the normalization and shows why the Laurent coefficient appears. For each additive character of \((\mathbb Z/q\mathbb Z)^d\), adjacency eigenvalues depend only on the number of nonzero character coordinates; let \(E_k\) project onto that weight class. Standard spectral averaging gives \(\widehat M=\sum_{k=0}^d E_k\circ E_k\). For a character \(\eta\) with \(j\) nonzero coordinates, its mixing eigenvalue equals \(q^{-d}\) times the number of ordered pairs of characters of equal weight and difference \(\eta\). A zero coordinate of \(\eta\) gives \(q\) weight-balanced choices. A nonzero coordinate produces local weight-difference counts \(1,q-2,1\) for differences \(-1,0,+1\). Thus the count is \(q^{d-j}[z^0](q-2+z+z^{-1})^j\), proving the formula once more.

## Verification
The accompanying standalone `verify_hamming.py` uses exact integer enumeration of equal-weight character pairs for \(45\) parameter-index triples with \(2\le q\le6\) and \(1\le d\le3\), including the exact rank boundary. Independently it reconstructs all adjacency eigenspace projectors from additive characters for ten Hamming graphs and compares the full average-mixing matrix spectrum to the closed formula, with maximal numerical deviation below \(8\times10^{-16}\). The exact finite checks test implementation and normalization; the proof of the infinite family is analytical above. To reproduce, install Python with NumPy and run `python verify_hamming.py`.

## Relationship to prior work
Godsil's *Average mixing of continuous quantum walks* establishes the spectral-projector averaging formula; Coutinho, Godsil, Guo and Zhan's *A New Perspective on the Average Mixing Matrix* proves, among other results, full rank for abelian Cayley graphs of odd order. Thus the rank conclusion for odd \(q\) is already covered by that theorem. The present finding instead supplies an explicit entire mixing spectrum, resolves even \(q\ge4\) as well, and quantifies binary-kernel dimension. Coutinho and Guo's *Selected Open Problems in Continuous-Time Quantum Walks* poses full rank of the Cesàro mixing matrix for primitive distance-regular graphs: the result verifies this for the nonbinary Hamming family (the binary family is bipartite). The motivating mathematical-physics treatment *Irrational quantum walks* provides exact averaging methods for integral Hamiltonians; the present tensor calculation isolates an elementary closed form for this family. No claim is made to an all-distance-regular-graph theorem.

## Limitations
This statement concerns standard Cesàro mixing, not instantaneous uniform mixing, randomized observation-time mixing under a designed law, or arbitrary weighted graph Hamiltonians. The indexed eigenvalues can coincide, and multiplicities must then be added. No general theorem is inferred for Johnson graphs or other distance-regular families. A general association-scheme identity not identified in the inspected literature could make the explicit formula implicit in prior results; that remains an originality risk. No independent peer audit has been performed.

## References
1. C. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578 (2011). https://arxiv.org/abs/1103.2578
2. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591 (2017). https://arxiv.org/abs/1709.03591
3. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first posted 2022-08-18). https://arxiv.org/abs/2208.08971
4. G. Coutinho, K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236 (2024), §4, Problem 4.2. https://arxiv.org/abs/2404.02236
