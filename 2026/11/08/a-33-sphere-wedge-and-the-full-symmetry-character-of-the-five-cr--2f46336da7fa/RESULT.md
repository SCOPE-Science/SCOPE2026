# A 33-sphere wedge and the full symmetry character of the five-crown perfect-matching complex

## Finding
Let \(C=K_{5,5}-\{\{i_L,i_R\}:i\in\{0,1,2,3,4\}\}\) be the five-crown graph, and let \(X=\mathcal M_p(C)\) be the simplicial complex whose simplices are sets of graph edges extendible to a perfect matching. Then
\[
X\simeq\bigvee^{33}S^2.
\]
The full graph automorphism group is \(G\cong S_5\times C_2\), where \(S_5\) relabels both vertex classes simultaneously and the central involution \(\tau\) exchanges the classes. Write \(S^\lambda\) for the rational Specht module indexed by a partition \(\lambda\vdash5\), and use superscripts \(+\) and \(-\) for the eigenvalues of \(\tau\). The induced rational representation has the complete decomposition
\[
\begin{aligned}
\widetilde H_2(X;\mathbb Q)^+&\cong S^{(3,2)}\oplus S^{(3,1,1)}\oplus S^{(2,2,1)}\oplus S^{(2,1,1,1)}\oplus S^{(1,1,1,1,1)},\\
\widetilde H_2(X;\mathbb Q)^-&\cong S^{(5)}\oplus S^{(3,2)}\oplus S^{(2,2,1)}\oplus S^{(1,1,1,1,1)}.
\end{aligned}
\]
The two eigenspaces have dimensions \(21\) and \(12\), respectively. In particular, the full automorphism group fixes no nonzero rational second-homology class. Moreover, \(X\) is a pure four-dimensional complex that is not shellable.

## Assumptions and scope
The vertex classes are \(L=\{0_L,\ldots,4_L\}\) and \(R=\{0_R,\ldots,4_R\}\). There is an edge \(\{i_L,j_R\}\) precisely when \(i\ne j\). A perfect matching is therefore the graph of a derangement \(\pi\in S_5\), with edge set \(\{\{i_L,\pi(i)_R\}:0\le i\le4\}\). The simplicial vertices are the \(20\) graph edges and every face is a subset of one of these perfect matchings. The statement concerns this specific ten-vertex graph and the complete rational \(S_5\times C_2\) action on \(\widetilde H_2\); it is not a family-wide classification or an integral equivariant decomposition.

## Proof
**Exhaustive combinatorial model.** There are exactly \(!5=44\) derangements and thus \(44\) facets, each containing five graph edges. Generating their subsets gives \(735\) faces, including the empty face, and the face vector in dimensions \(0,1,2,3,4\) is \((20,130,320,220,44)\). A second enumeration builds all perfect matchings by independently assigning an unused right endpoint to each left vertex. Separately, all \(2^{20}\) edge subsets are tested using a vertex-disjointness test followed by a dynamic residual perfect-matching test; exactly the same \(735\) subsets are accepted.

**An explicit acyclic discrete-Morse matching.** Order the twenty simplicial vertices lexicographically by pairs \((i,j)\), with \(0\le i,j\le4\) and \(i\ne j\). Initially mark every nonempty face unpaired. For each simplicial vertex \(e\) in that order, pair every currently unpaired face \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever both are unpaired. After processing all twenty vertices, this specifies \(350\) disjoint face/coface pairs and leaves exactly one critical vertex and \(33\) critical two-dimensional faces. To certify acyclicity, orient each Hasse incidence downward from the larger face to the smaller face, except reverse each matched incidence. Topological sorting of the resulting directed graph visits all \(734\) nonempty faces across all \(2320\) incidences; hence there is no directed cycle. Reversing the lexicographic order and repeating the entire construction independently gives the same critical-cell vector and passes the same acyclicity test.

By the simplicial discrete-Morse theorem, \(X\) is homotopy equivalent to a CW complex having one zero-cell, no one-cells, and \(33\) two-cells, with no other cells. Every attaching map from \(S^1\) into the single zero-cell is constant. The resulting CW space is exactly \(\bigvee^{33}S^2\), proving the integral homotopy claim. Independently, direct mod-two simplicial boundary elimination yields ranks \((19,111,176,44)\) for boundary maps in dimensions one through four, consistent with reduced second Betti number \(33\).

**Automorphisms and the integral origin of the rational character.** Because \(C\) is connected and bipartite, every graph automorphism preserves the bipartition or exchanges the two classes. Preserving the missing diagonal matching forces the same permutation on both classes. Therefore \(G=S_5\times\langle\tau\rangle\), of order \(240\). Each element acts simplicially on \(X\). Since the reduced rational homology is concentrated in degree two, the reduced Lefschetz number equals the trace on \(\widetilde H_2(X;\mathbb Q)\):
\[
\chi(g)=\sum_{\substack{\varnothing\ne\sigma\in X\\g\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma)-1,
\]
where the sign is the parity of the permutation induced by \(g\) on the vertices of the oriented simplex \(\sigma\). This equality is a simplicial chain-trace identity; it does not presume an equivariant Morse matching.

For the simultaneous relabelings of the seven conjugacy types of \(S_5\), the traces without and with \(\tau\), respectively, are:

| Cycle type | Class size | Trace without \(\tau\) | Trace with \(\tau\) |
|---|---:|---:|---:|
| \((5)\) | 24 | 3 | −1 |
| \((4,1)\) | 30 | −1 | −1 |
| \((3,2)\) | 20 | 0 | 0 |
| \((3,1,1)\) | 20 | 0 | 0 |
| \((2,2,1)\) | 15 | 5 | −3 |
| \((2,1,1,1)\) | 10 | −3 | −3 |
| \((1,1,1,1,1)\) | 1 | 33 | 9 |

The table is obtained by enumerating all \(240\) group elements, their invariant faces, and the exact orientation signs. The standard Murnaghan–Nakayama rim-hook rule for \(S_5\) irreducible characters and exact class-weighted inner products give precisely the two Specht decompositions stated above. Their total dimensions are \(21\) and \(12\). The average of the \(240\) traces is zero, proving the fixed-space assertion.

Finally, all facets have cardinality five, so \(X\) is pure of dimension four. A pure shellable complex has no reduced homology below its top dimension, whereas \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z^{33}\). Hence \(X\) is not shellable.

## Verification
Run `python3 verify_crown5.py` using an ordinary Python 3 interpreter. The self-contained program enumerates the derangements and perfect matchings independently, checks every edge subset against a dynamic extendibility predicate, constructs both full Morse pairings, checks every directed Hasse incidence for acyclicity, calculates the four mod-two simplicial boundary ranks, computes the exact Lefschetz character for every group element, and obtains the rational irreducible multiplicities by a direct rim-hook recursion. Its expected output is preserved in `verification_output.txt` and begins with `CROWN5_PERFECT_MATCHING_HOMOTOPY_AND_CHARACTER_VERIFIED`. A script execution is a finite exact certificate coupled with the discrete-Morse and Lefschetz theorems, not an independent external certification.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega introduce the same perfect-matching-complex definition and prove homotopy results for honeycomb graphs and their line/hexagonal cases. Chandrakar and Singh prove results for polygonal line tilings and two-by-\(n\) grids. Their object-specific results do not include this dense bipartite crown graph. The complete bipartite case reduces to an ordinary chessboard complex because every matching extends, as explicitly discussed by Bayer and coauthors; removing the diagonal edges changes both the simplicial vertex set and the extendibility condition, so results for the complete bipartite case do not settle the crown case. Limonchenko and Yu study generalized chessboard complexes defined by row/column capacity constraints, including the fact that the ordinary five-by-five chessboard complex has \(\mathbb Z/3\)-torsion in second homology. Neither their stated general definition nor their theorems applies directly to this forbidden-diagonal, perfect-extendible complex; the resulting torsion contrast motivates the present exact calculation. Searches for crown graphs, diagonal-forbidden chessboards, derangement-facet complexes, perfect-matching complexes and equivalent group representations yielded no checked result implying this specific nonequivariant or equivariant classification. This is a best-knowledge originality assessment, not a claim of exhaustive bibliographic uniqueness.

## Limitations
The theorem applies only to \(K_{5,5}\) with a fixed perfect matching deleted. It does not determine the homotopy type for arbitrary \(K_{n,n}\) with diagonal deletion, general crown graphs, or an integral \(G\)-module splitting. The representation statement is rational. The complete finite certificate relies on the accepted mathematical discrete-Morse and Lefschetz theorems. Relevant unindexed or inaccessible work could still establish the same conclusion. No independent audit or external validation has been performed.

## References
1. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803, first public posting 2022-09-06, https://arxiv.org/abs/2209.02803.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tiling*, arXiv:2407.05809, first public posting 2024-07-08, https://arxiv.org/abs/2407.05809.
3. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827, first public posting 2026-10-27, https://arxiv.org/abs/2610.37827.
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145; used only for the standard acyclic matching theorem.
5. Standard simplicial Lefschetz trace identity and the Murnaghan–Nakayama rule for symmetric-group characters; both applied through explicit finite calculations in the verifier.
