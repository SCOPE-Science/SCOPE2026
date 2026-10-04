# Perfect-matching trichotomy for perfect grid states
## Finding
Let \(\mathbb G\) be a grid diagram of size \(n\) with winding matrix \(M\). Write \(\mathcal R\) and \(\mathcal C\) for the row and column numbers introduced by Itzlinger. If \(\mathcal C\le \mathcal R\), form a bipartite graph \(B_C(M)\) with one vertex for every column and one vertex for every row, and place an edge \(c_jr_i\) exactly when \(M_{i,j}\) is a minimum entry of column \(j\). If \(\mathcal R<\mathcal C\), define \(B_R(M)\) analogously from row minima.

Then the perfect grid states of \(\mathbb G\) are in bijection with the perfect matchings of the corresponding minimizer graph. Hence there is an exact trichotomy:

\[
\#\{\text{perfect grid states}\}=0
\]
exactly when the minimizer graph has no perfect matching;

\[
\#\{\text{perfect grid states}\}=1
\]
exactly when it has a perfect matching with no alternating cycle; and otherwise it has at least two perfect grid states. In the last case, toggling one alternating cycle produces a second perfect grid state explicitly.

For a column-perfect state represented by a permutation \(\sigma\), the loops defined in Itzlinger's Definition 2.1 are precisely alternating cycles of \(B_C(M)\) relative to the matching represented by \(\sigma\). Thus Lemma 2.3 has a converse for column-perfect states: such a state is unique if and only if its minimizer graph contains no alternating cycle relative to it. The row-perfect statement is identical.

This gives a direct polynomial-time classifier of the three outcomes that the source says its peeling procedure does not distinguish: no perfect grid state, a unique perfect grid state, or more than one perfect grid state.

## Assumptions and scope
A grid state chooses one lattice point on each horizontal and each vertical grid line, so it is represented by a permutation. The winding function used by the source is
\[
A'(x)=-\sum_{p\in x}\omega(p).
\]
The source defines
\[
\mathcal R=-\sum_i r_i,
\qquad
\mathcal C=-\sum_j c_j,
\]
where \(r_i\) and \(c_j\) are the row and column minima of \(M\), and calls a state perfect when
\[
A'(x)=\min\{\mathcal R,\mathcal C\}.
\]
No assertion is made here about the existence of a nice grid diagram for every fibered knot. The result classifies perfect states for a fixed winding matrix.

## Proof
Assume first that \(\mathcal C\le\mathcal R\). A grid state \(x\), represented by a permutation \(\sigma\), selects exactly one entry \(M_{\sigma(j),j}\) from each column and exactly one entry from each row. Since every selected entry is at least the minimum \(c_j\) of its column,
\[
\sum_j M_{\sigma(j),j}\ge \sum_j c_j.
\]
After multiplying by \(-1\), this is the source's bound
\[
A'(x)\le \mathcal C.
\]
Equality holds if and only if every selected entry is a column minimum. Therefore \(x\) is perfect if and only if the set
\[
\{c_jr_{\sigma(j)}:1\le j\le n\}
\]
is a perfect matching of \(B_C(M)\). This proves the bijection. When \(\mathcal R<\mathcal C\), the same argument with rows gives the bijection with perfect matchings of \(B_R(M)\). Notice that equality \(\mathcal R=\mathcal C\) causes no ambiguity: a column-perfect state already attains the common minimum and is therefore perfect.

It remains to classify uniqueness. Let \(P\) be one perfect matching in the relevant minimizer graph. If there is a \(P\)-alternating cycle, toggle membership of all edges on that cycle. Every vertex on the cycle remains incident to exactly one chosen edge, so the result is a second perfect matching and hence a second perfect grid state.

Conversely, if \(Q\ne P\) is another perfect matching, the symmetric difference \(P\triangle Q\) is a disjoint union of even cycles whose edges alternate between \(P\) and \(Q\). Thus at least one \(P\)-alternating cycle exists. This proves that \(P\) is the unique perfect matching if and only if no alternating cycle exists.

For the source's loop language, take a column-perfect state \(\sigma\). A loop chooses columns and alternative column-minimal entries so that successive alternatives land on rows occupied by the next matched column and eventually return to the first row. This is exactly an alternating cycle in \(B_C(M)\): matched edges are the entries selected by \(\sigma\), and unmatched edges are the alternative minima. The source proves that a loop gives another equal-grading state. The symmetric-difference argument above gives the converse whenever another column-perfect state exists.

For computation, one first builds the minimizer graph, which has at most \(n^2\) edges. Hopcroft--Karp finds a maximum matching in \(O(E\sqrt n)\), hence \(O(n^{5/2})\) in the dense worst case. If the matching is not perfect, the answer is zero. If it is perfect, contract each matched edge and orient every remaining edge according to the alternating direction. A directed cycle exists exactly when an alternating cycle exists, so a depth-first search gives the unique-versus-multiple decision in \(O(E)\) additional time.

## Verification
The bundled verifier exhaustively checks every binary matrix of sizes at most \(4\). For each matrix it computes all grid-state permutations directly, identifies the perfect states from the numerical definition of \(A'\), constructs the appropriate minimizer graph, enumerates its perfect matchings, and verifies equality of the two sets. It also checks that the alternating-cycle test labels the matching count correctly as zero, one, or multiple.

The exhaustive computation is a regression test only. The general result follows from the equality condition in the row or column minimum bound and the standard symmetric-difference structure of two perfect matchings.

## Relationship to prior work
Itzlinger's 2026 preprint introduces the row and column bounds, defines perfect grid states, proves that a matrix loop produces another equal-Alexander state, and proves that a unique column-perfect state forces a column with a unique minimum. The paper then recursively deletes forced positions. It explicitly notes a limitation: when the recursive test stalls, it cannot distinguish a diagram with several column-perfect states from one with none.

The perfect-matching reformulation closes exactly that gap for a fixed winding matrix. Existence becomes the ordinary perfect-matching problem; nonuniqueness becomes the existence of an alternating cycle; and the source's loops become the standard alternating cycles relative to a perfect matching. The graph-theoretic facts about matchings are classical. The new point is the exact identification with the source's perfect-state problem and the resulting complete trichotomy.

Targeted searches of the preprint, its public software documentation, general web results, and published-finding corpus records did not locate this matching formulation or an exact zero/one/multiple classifier for perfect grid states.

## Limitations
This result does not decide whether every fibered knot has a nice grid diagram. It improves the fixed-diagram decision problem only. It also does not classify maximal grid states that fail to attain the row or column bound, such as the non-perfect unique maximal example discussed by the source.

The matching theorems used in the proof are classical; novelty is claimed only for their explicit application to Itzlinger's perfect-grid-state setup and for resolving the source's stated decision ambiguity. Because the target preprint is recent, a later unindexed revision or note could independently make the same observation.

## References
1. Paul Leon Itzlinger, *Grid Diagrams of Fibered Knots*, arXiv:2602.02642v1, first posted 2026-02-02.
2. Paul Leon Itzlinger, `griddiagrams`, public software repository accompanying the preprint.
3. László Lovász and Michael D. Plummer, *Matching Theory*, North-Holland Mathematics Studies 121, 1986.
