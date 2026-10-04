# Exact three-point simultaneous exponential bases in binary vector spaces
## Finding
Let \(d\ge 2\), let \(G=\mathbb F_2^d\), and let \(E_1,E_2\subset G\) be three-element sets. For \(i=1,2\), define the direction plane
\[
U_i=\operatorname{span}_{\mathbb F_2}(E_i-E_i).
\]
Because three distinct points over \(\mathbb F_2\) are affinely independent in their two-dimensional affine span, each \(U_i\) has dimension \(2\). Put \(r=\dim(U_1+U_2)\), so \(r\in\{2,3,4\}\).

Identify the dual group \(\widehat G\) with \(G\) by \(\chi_\xi(x)=(-1)^{\langle x,\xi\rangle}\). The number of three-element sets \(B\subset G\) for which \(\{\chi_\xi|_{E_i}:\xi\in B\}\) is a basis of functions on \(E_i\) for both \(i=1,2\) is exactly
\[
N(E_1,E_2)=m_r2^{3(d-r)},\qquad m_2=4,\quad m_3=16,\quad m_4=96.
\]
Thus every pair of three-element subsets of every binary vector space has a simultaneous exponential Riesz basis. The sharp minimum over all pairs is \(4\) when \(d=2\), \(16\) when \(d=3\), and \(3\cdot2^{3d-7}\) when \(d\ge4\). For \(d\ge4\), equality occurs exactly when \(U_1\cap U_2=\{0\}\).

## Assumptions and scope
The group is the additive group of \(\mathbb F_2^d\) with \(d\ge2\). Each \(E_i\) has exactly three distinct points. A frequency set \(B\) also has exactly three elements. In a finite-dimensional space, an exponential Riesz basis is simply an invertible character evaluation matrix, so no conditioning claim is made here.

The count is for unordered frequency sets \(B\subset G\), not ordered triples. Translation of either \(E_i\) does not change which \(B\) are basis partners, because translating the spatial set multiplies each character column by a nonzero scalar.

## Proof
Translate each \(E_i\) so that
\[
E_i=\{0,a_i,b_i\},
\]
where \(a_i,b_i\) are linearly independent and span \(U_i\). Define
\[
\pi_i:G\longrightarrow\mathbb F_2^2,\qquad
\pi_i(\xi)=(\langle a_i,\xi\rangle,\langle b_i,\xi\rangle).
\]
For a frequency \(\xi\), the corresponding column of the evaluation matrix on \(E_i\) is
\[
c(\pi_i(\xi))=(1,(-1)^{\langle a_i,\xi\rangle},(-1)^{\langle b_i,\xi\rangle})^T.
\]
There are four possible column types, indexed by \(\mathbb F_2^2\). Every three distinct types have determinant \(\pm4\), while a repeated type makes the determinant zero. Hence \(B\) is a basis partner for \(E_i\) exactly when \(\pi_i\) is injective on \(B\).

Now combine the two projections:
\[
\Pi=(\pi_1,\pi_2):G\longrightarrow\mathbb F_2^2\times\mathbb F_2^2.
\]
Its rank is \(r=\dim(U_1+U_2)\), its kernel has size \(q=2^{d-r}\), and its image \(H\) projects surjectively onto both \(\mathbb F_2^2\) factors. Regard \(H\) as the edge set of a simple bipartite graph with four left and four right vertices. A three-element set \(B\) is a simultaneous basis exactly when its three image edges form a matching. Every three-edge matching in \(H\) has exactly \(q^3\) lifts to \(B\), because its three image points have disjoint fibers of size \(q\).

It remains to count three-edge matchings in \(H\). If \(r=2\), both coordinate projections are isomorphisms on \(H\), so \(H\) is a perfect matching on four edges and has \(\binom43=4\) three-edge submatchings. If \(r=3\), every left and right vertex has degree \(2\), so \(H\) is either an eight-cycle or the disjoint union of two four-cycles. In either case it has exactly \(16\) matchings of size three. If \(r=4\), then \(H=\mathbb F_2^2\times\mathbb F_2^2\), the complete bipartite graph \(K_{4,4}\), and the number of three-edge matchings is
\[
\binom43^2 3!=96.
\]
Multiplying by \(q^3=2^{3(d-r)}\) proves the exact formula.

For the minima, when \(d=2\) only \(r=2\) can occur. When \(d=3\), the smaller of the \(r=2\) and \(r=3\) counts is \(16\). For \(d\ge4\), the three possible counts are \(2^{3d-4}\), \(2^{3d-5}\), and \(3\cdot2^{3d-7}\), the last being smallest. Disjoint two-planes exist exactly when \(d\ge4\), giving sharpness.

## Verification
The standalone script `verify.py` uses exact integer arithmetic. It checks the determinant criterion against the projection criterion, evaluates canonical cases for every possible \(r\) in dimensions \(2\) through \(6\), exhausts all \(1596\) unordered pairs of three-element subsets in \(\mathbb F_2^3\), and exhausts all \(630\) unordered pairs of two-dimensional subspaces in \(\mathbb F_2^4\). It returns `VERIFY_OK` and reproduces the formulas \(4,16,96\) before the fiber factors. These finite checks are consistency tests; the theorem for all \(d\) is established by the proof above.

## Relationship to prior work
Ferguson, Mayeli, and Sothanaphan define simultaneous bases for equal-size families of subsets of a finite abelian group and ask whether every pair of equal-size nonempty subsets has one. They explicitly note a three-set obstruction in \(\mathbb Z_2^2\), state that the two-set question remains unresolved, and prove that every equal-size family in a cyclic group has a simultaneous basis by a Vandermonde argument. The present result settles the entire three-point stratum of that pair question for the noncyclic family \(\mathbb F_2^d\), with an exact count of common basis partners.

A published published-finding corpus record on the order-eight Sylvester Hadamard matrix exhausts all square minors for discrepancy purposes. That finite database can in principle recover determinant information in the special case \(d=3\), but it states no simultaneous-basis intersection theorem and has no claim beyond order eight. The proof here is dimension-free and gives the exact count for every \(d\ge2\).

## Limitations
The argument uses the special four-column-type geometry of a three-point set over characteristic two. It does not settle the simultaneous-basis question for four-point subsets, for fields of odd characteristic, or for arbitrary finite abelian groups. It establishes existence and exact counts, not optimal Riesz ratios or conditioning of the common bases.

The literature search found no source stating this binary three-point classification, but absence from a bounded search is not a proof of global novelty. The closest finite database covers only the order-eight Walsh matrix and therefore overlaps the \(d=3\) slice computationally.

## References
- S. Ferguson, A. Mayeli, and N. Sothanaphan, “Riesz bases of exponentials and multi-tiling in finite abelian groups,” arXiv:1904.04487, first posted 2019-04-09; see Question 1.8 and Section 7.1.
- published-finding corpus, “Exact hereditary discrepancy and determinant-bound gap for the canonical order-8 Sylvester Hadamard matrix,” record `2026/9/9/SCOPE037`.
