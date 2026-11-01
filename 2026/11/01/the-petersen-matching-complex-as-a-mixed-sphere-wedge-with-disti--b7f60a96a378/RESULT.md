# The Petersen matching complex as a mixed sphere wedge with distinct symmetric-group homology modules

## Finding
Let \(P\) be the Petersen graph represented as the Kneser graph \(\operatorname{KG}(5,2)\). Its ordinary matching complex \(X=\mathcal M(P)\) has one vertex for each edge of \(P\), and a simplex for each family of pairwise vertex-disjoint edges of \(P\). There is a nonequivariant homotopy equivalence
\[
X\simeq\bigvee^{5}S^2\ \vee\ \bigvee^{5}S^3.
\]
Under the natural relabeling action of \(\mathfrak S_5\), the only nonzero positive-degree rational homology representations are
\[
H_2(X;\mathbb Q)\cong \operatorname{sgn}\otimes \mathbb Q^{\{1,2,3,4,5\}},
\qquad H_3(X;\mathbb Q)\cong S^{(3,2)}.
\]
Here the five-dimensional permutation module is the action on five labels, \(\operatorname{sgn}\) is the sign character, and \(S^{(3,2)}\) is the rational five-dimensional Specht representation. In particular, these two homology modules have equal ranks but different characters. The orbit spaces satisfy
\[
\widetilde H_*(X/\mathfrak S_5;\mathbb Q)=0,
\qquad \widetilde H_i(X/\mathfrak A_5;\mathbb Q)\cong
\begin{cases}\mathbb Q,&i=2,\\0,&i\ne2.\end{cases}
\]
No assertion of a homeomorphism type for either orbit space is made.

## Assumptions and scope
Use labels \(\{0,1,2,3,4\}\). The ten vertices of \(P\) are the unordered two-element subsets of this set, in lexicographic order; two are adjacent if and only if they are disjoint as subsets. Its fifteen graph edges are ordered lexicographically. For an edge-index set \(F\), membership in \(X\) means that all graph endpoints of edges indexed by \(F\) are distinct. This is the ordinary matching complex (capacity one at every graph vertex), **not** the two-matching complex or the discrete Morse complex. The action of \(\mathfrak S_5\) permutes the underlying five labels and preserves this matching condition. All statements concern the entire finite complex, not a sampling of facets.

## Proof
**1. Explicit perfect discrete-Morse matching.** Exhaustive enumeration of the \(2^{15}-1\) nonempty edge subsets produces respectively \(15,75,145,90,6\) simplices of dimensions \(0,1,2,3,4\). At successive edge indices
\[
0,9,2,11,13,4,7,6,3,14,10,12,8,5,1,
\]
consider every as-yet-unmatched simplex not containing that index and pair it with the simplex obtained by adding the index, if the latter also remains unmatched. The recorded deterministic order within each stage is increasing binary edge-mask. This produces exactly 160 disjoint simplex/coface pairs. The remaining cells comprise one vertex, five two-simplices, and five three-simplices. The directed Hasse graph, with matching incidences oriented upward and all others downward, is acyclic; the accompanying verifier checks every incidence and searches the entire directed graph for cycles.

**2. Integral attachments.** Apply integral elementary chain cancellations along the 160 pairs. Every eliminated boundary coefficient is \(+1\) or \(-1\), so each cancellation is an integral chain homotopy equivalence. The exact resulting Morse boundary is identically zero on the eleven critical cells. Forman's discrete Morse theorem supplies a CW complex with precisely these cell dimensions. Since it has one zero-cell and no one-cells, its two-skeleton is \(\bigvee^5S^2\). The vanishing integral Morse boundary says that the attaching maps of its five three-cells have zero degree on each two-sphere. By the Hurewicz isomorphism \(\pi_2(\bigvee^5 S^2)\cong H_2(\bigvee^5 S^2;\mathbb Z)\), each attaching map is nullhomotopic. The asserted wedge decomposition follows. In particular all integral homology is torsion-free, with rank five in each of degrees two and three and no other reduced homology.

**3. Exact homology characters.** On oriented simplicial chains, every relabeling acts by a signed permutation of the edge-index simplices. Direct integer boundary ranks \(\operatorname{rank}(\partial_1),\ldots,\operatorname{rank}(\partial_4)=(14,61,79,6)\) are checked by exact rational elimination. For each of the seven cycle types of \(\mathfrak S_5\), the trace of the action on each boundary-image space is computed from an invertible pivot minor modulo the prime 101. The pivot ranks agree with the exact rational ranks. Therefore the modular homology traces reduce the corresponding rational characters; as these traces are integers bounded in absolute value by the five-dimensional homology ranks, their representatives in \([-5,5]\) are unique. The resulting character values, in cycle-type order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), are

| Rational module | Identity | 2 | 2,2 | 3 | 3,2 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(H_2\) | 5 | -3 | 1 | 2 | 0 | -1 | 0 |
| \(H_3\) | 5 | 1 | 1 | -1 | 1 | -1 | 0 |

For a permutation \(g\) of five labels, \(\chi_2(g)=\operatorname{sgn}(g)\,|\operatorname{Fix}_{[5]}(g)|\). Also \(\chi_3(g)=|\operatorname{Fix}_{\binom{[5]}2}(g)|-|\operatorname{Fix}_{[5]}(g)|\), the character of the two-subset permutation representation minus the point permutation representation. The standard decomposition of these permutation modules gives precisely \(\operatorname{sgn}\otimes\mathbb Q^5\) and \(S^{(3,2)}\). The verifier checks these equalities in all seven classes.

**4. Rational quotient homology.** For a finite simplicial group action, rational homology of the orbit space is the invariant part of rational homology, after an equivariant barycentric subdivision if needed. Neither positive-degree module contains a trivial \(\mathfrak S_5\)-summand. On restriction to the alternating group, the sign twist disappears and the permutation module on five labels has a one-dimensional invariant subspace; \(S^{(3,2)}\) has none. The stated orbit-space rational homology follows.

## Verification
The standalone file `verify_homotopy.py` enumerates all 331 nonempty faces, checks the 160 matched pairs and every directed incidence for acyclicity, and carries out unit-pivot integral cancellations through the zero critical differential. The separately constructed `verify_equivariant.py` checks the integral boundary compositions, exact rational ranks, group-induced signed simplex permutations, modular boundary-image trace computations, and the two character identities. Both programs produce success markers when run with a standard Python interpreter and dependencies in `requirements.txt`. Their captured outputs are embedded as `homotopy_output.txt` and `equivariant_output.txt`.

## Relationship to prior work
Björner–Lovász–Vrećica–Živaljević and Wachs survey and establish classical matching-complex topology and symmetric-group homology for complete graphs and complete bipartite graphs. Their complexes \(\mathcal M(K_n)\) and \(\mathcal M(K_{m,n})\) are not \(\mathcal M(P)\). Larrión–Pizaña–Villarroel-Flores identify the **Petersen graph itself** as the one-skeleton of \(\mathcal M(K_5)\); that is a different object from taking matchings of the Petersen graph. Nikseresht studies Gorenstein and Cohen–Macaulay classifications for graph matching complexes, not these homology representations. Exact graph-symmetry literature supplies the canonical \(\mathfrak S_5\)-action. The new calculation gives the complete integral homotopy type and rational equivariant homology for the specific \(15\)-edge Petersen matching complex, rather than applying the complete-graph formulas with relabeled parameters.

## Limitations
The wedge equivalence is not claimed equivariant. The integral \(\mathbb Z[\mathfrak S_5]\)-module structure and integral homology of the orbit spaces have not been calculated. The quotient statements concern rational homology, not homotopy type. Novelty comparisons cannot exclude an uncatalogued equivalent calculation. The result is supported by a finite exhaustive computational certificate and mathematical arguments, but has not undergone independent review.

## References
1. A. Björner, L. Lovász, S. T. Vrećica and R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society 49 (1994), 25–39; DOI: 10.1112/jlms/49.1.25; first published 1994-02-01.
2. M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, Algebra Universalis 49 (2003), 345–385; DOI: 10.1007/s00012-003-1825-1; open preprint https://www.math.miami.edu/~wachs/papers/tmc.pdf.
3. F. Larrión, M. A. Pizaña and R. Villarroel-Flores, *The clique operator on matching and chessboard graphs*, Discrete Mathematics 309 (2009), 85–93; DOI: 10.1016/j.disc.2007.12.047; open preprint https://xamanek.izt.uam.mx/map/papers/chessmatch7.pdf.
4. A. Nikseresht, *Gorenstein and Cohen-Macaulay Matching Complexes*, arXiv:2106.13993 (first submitted 2021-06-26); https://arxiv.org/abs/2106.13993.
5. T. Zaslavsky, *Six signed Petersen graphs, and their automorphisms*, Discrete Mathematics 312 (2012), 1558–1583; DOI: 10.1016/j.disc.2011.12.010.
