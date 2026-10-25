# Bipartition-exchange character of the fifteen-dimensional two-matching homology of \(K_{4,4}\)

## Finding
Let \(X=M_2(K_{4,4})\) be the simplicial complex whose vertices are the sixteen edges \((a,b)\) of the bipartite graph \(K_{4,4}\), where \(a,b\in\{0,1,2,3\}\). A subset is a simplex if every row and every column appears at most twice. Let \(G=(S_4\times S_4)\rtimes C_2\) be the full graph automorphism group. The distinguished involution \(s\) transposes the row and column sides, and \((\sigma,\tau)s\) sends \((a,b)\) to \((\sigma(b),\tau(a))\).

Let \(U=S^{(3,1)}\) be the three-dimensional standard rational representation of \(S_4\), and let \(V=S^{(2,1,1)}\cong U\otimes\operatorname{sgn}\). Then all reduced rational homology of \(X\) vanishes outside degree five, and
\[
\widetilde H_5(X;\mathbb Q)\cong
\operatorname{Ind}_{S_4\times S_4}^{G}(\mathbf 1\boxtimes V)
\oplus (U\boxtimes U)^+
\]
as \(\mathbb Q[G]\)-modules. The superscript \(+\) denotes the extension on which \(s\) interchanges the two tensor factors without an extra minus sign. Its dimension is \(2\cdot3+3\cdot3=15\).

Equivalently, if \(u(\pi)=|\operatorname{Fix}_{\{0,1,2,3\}}(\pi)|-1\) and \(v(\pi)=\operatorname{sgn}(\pi)u(\pi)\), then the **complete rational character** is
\[
\chi((\sigma,\tau))=u(\sigma)u(\tau)+v(\sigma)+v(\tau),
\qquad
\chi((\sigma,\tau)s)=u(\sigma\tau).
\]
Thus bipartition exchange itself has trace \(3\), and the swap-class character depends only on the cycle type of \(\sigma\tau\). For the five types \(1^4,2\,1^2,2^2,3\,1,4\), these traces are respectively \(3,1,-1,0,-1\). The invariant subspace of the full automorphism group is zero.

## Assumptions and scope
The vertex set of \(X\) is \(\{0,1,2,3\}^2\), and every simplex obeys the degree bound two independently in both coordinates. The semidirect-product action is by relabeling the two parts and exchanging them; the product in \(\sigma\tau\) means composition (either order has the same cycle type). All representation statements are over \(\mathbb Q\). The integral wedge-of-spheres result is a prior result used here only as a homology-concentration input, and independently rechecked by a complete finite Morse certificate.

## Proof
**Homology concentration.** Encode each nonempty simplex by its 16-bit edge mask, ordered row-major. Testing all \(2^{16}-1\) nonempty masks gives exactly \(7342\) admissible faces with face vector \((16,120,528,1428,2304,2040,816,90)\) by dimension. Apply the ordered element matching with edge order \((7,2,5,10,1,11,13,9,12,15,8,0,4,3,14,6)\): at each edge, match every still-unmatched admissible lower mask not containing the edge to its still-unmatched upper mask obtained by inserting the edge. This makes \(3663\) disjoint Hasse pairs. The unpaired faces consist of a single vertex and fifteen dimension-five simplices. To verify acyclicity, orient every unmatched Hasse incidence from lower to upper and every matched incidence from upper to lower. On all \(37728\) Hasse incidences, Kahn's exact indegree-elimination algorithm visits every one of the \(7342\) masks. Therefore the matching is acyclic. Discrete Morse theory gives \(X\simeq\bigvee^{15}S^5\), hence rational reduced homology is fifteen-dimensional and concentrated in degree five. The cited earlier finite classification is not claimed as a new result.

**Exact fixed-cell character.** For \(g\in G\), let \(\mathcal O_g\) be the set of its cycles on the sixteen edges. For a cycle \(C\), write \(r_i(C)\) and \(c_j(C)\) for its incidences with row \(i\) and column \(j\). Since a setwise-fixed simplex must be a union of edge cycles, its signed reduced Lefschetz number is computed by summing over subfamilies \(\mathcal T\subseteq\mathcal O_g\) satisfying
\[
\sum_{C\in\mathcal T}r_i(C)\le2,\qquad
\sum_{C\in\mathcal T}c_j(C)\le2\quad (0\le i,j\le3).
\]
An included edge cycle of length \(d\) contributes \((-1)^d\) from its cardinality and \((-1)^{d-1}\) from the sign of the induced permutation on its edge vertices; their product is \(-1\). The exact Hopf trace formula, including the empty face's reduced contribution, consequently yields
\[
\chi(g)=\sum_{\substack{\mathcal T\subseteq\mathcal O_g\\\text{all eight degree bounds}}}(-1)^{|\mathcal T|}.
\]
This is a finite expression with at most \(2^{16}\) terms, valid for every group element and independent of any floating-point calculations.

**Evaluation on all conjugacy classes.** Conjugacy classes of the side-preserving subgroup are indexed by pairs of the five cycle types of \(S_4\). Direct evaluation of the preceding exact formula yields the following \(5\times5\) array, with rows and columns in the order \(1^4,2\,1^2,2^2,3\,1,4\):
\[
\begin{pmatrix}
15&5&-1&3&1\\
5&-1&-3&-1&-1\\
-1&-3&-1&-1&1\\
3&-1&-1&0&1\\
1&-1&1&1&3
\end{pmatrix}.
\]
For side-exchanging elements, conjugacy classes are indexed by the cycle type of the product \(\sigma\tau\), and the same cycle-orbit enumeration gives the five values \((3,1,-1,0,-1)\). (The complete automorphism group has fifteen nonswap and five swap classes.)

For any \(\pi\in S_4\), the standard character satisfies \(u(\pi)=\#\operatorname{Fix}(\pi)-1\), and the conjugate-hook character satisfies \(v(\pi)=\operatorname{sgn}(\pi)u(\pi)\). Substitution at the five cycle types verifies that the displayed array is \(u(\sigma)u(\tau)+v(\sigma)+v(\tau)\); the swap values equal \(u(\sigma\tau)\). The induced representation \(\operatorname{Ind}(\mathbf1\boxtimes V)\) has restricted character \(v(\sigma)+v(\tau)\) and vanishing swap-class trace. The flip-positive extension of \(U\boxtimes U\) has nonswap trace \(u(\sigma)u(\tau)\) and swap trace \(u(\sigma\tau)\). Equality of these exact character functions proves the asserted isomorphism of rational representations. Neither summand has a trivial constituent upon restriction to \(S_4\times S_4\), proving the invariant-space claim.

## Verification
The included standalone `verify.py` reconstructs every admissible mask and all Hasse incidences, verifies the acyclic matching and critical cells, evaluates the fixed-edge-orbit character for all \(24^2\cdot2=1152\) automorphisms, and independently computes signed fixed-simplex Lefschetz traces for representatives of all 20 full-group conjugacy classes (25 nonswap product-type representatives, including duplications, and five swap representatives). It independently verifies the zero invariant average. Run `python3 verify.py` with the standard library; the success line begins `K44_TWO_MATCHING_EQUIVARIANT_VERIFIED`. The exact finite checks are exhaustive for this fixed graph, not experiments extrapolated to a larger parameter range.

## Relationship to prior work
Reiner and Roberts' Theorem 3.3 covers the characteristic-zero \(S_4\times S_4\)-module of the same complex abstractly as the weight space of a multiple chessboard complex with row and column capacities \((2,2,2,2)\). The complete **side-preserving** representation is therefore not presented as newly implied information, although the explicit \(5\times5\) character is included to identify the restriction. Their stated theorem does not treat exchange of the two bipartition classes as an element of the acting group and does not select either of the two possible flip extensions of \(U\boxtimes U\). The new contribution is the full \((S_4\times S_4)\rtimes C_2\)-character, especially its five swap-class traces and the identification of the **positive** tensor-flip extension.

Singh's 2020 article defines higher matching complexes, but its complete-bipartite sphere theorem covers the different complex \(M_3(K_{4,4})\). A separately published finite calculation determines \(M_2(K_{4,4})\simeq\bigvee^{15}S^5\) by a discrete-Morse certificate, but expressly does not compute the \(S_4\times S_4\) homology action, much less the part-exchanging automorphisms. Vega studies two-matching complexes for other graph classes. Searches for algebraic aliases (degree-bound-two four-by-four multiple chessboard complex and symmetric row-column exchange) did not identify an existing full exchange-character classification.

## Limitations
The result is specific to the fixed graph \(K_{4,4}\) and its two-matching complex; it does not generalize the numerical character to all \(M_2(K_{m,n})\). It identifies a rational \(G\)-module, not its integral lattice or an equivariant homotopy wedge decomposition. The side-preserving character is already covered abstractly by Reiner–Roberts and is not claimed as a separate original contribution. Existing sources may contain an unindexed equivalent description of the full swap extension; no negative search can eliminate that risk. Independent mathematical validation has not been performed.

## References
1. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632v1, first public June 24, 2020; https://arxiv.org/abs/2006.13632.
2. V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, Journal of Algebraic Combinatorics 11 (2000), 135–154, Theorem 3.3; https://www-users.cse.umn.edu/~rober005/chessmatch.pdf.
3. J. Vega, *2-Matching Complexes*, arXiv:1909.10406v1, first public September 23, 2019; https://arxiv.org/abs/1909.10406.
4. *The two-matching complex of \(K_{4,4}\) is a wedge of fifteen five-spheres*, public mathematical research record, October 11, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-two-matching-complex-of-k-4-4-is-a-wedge-of-fifteen-five-sph--915eed6b65e5.
