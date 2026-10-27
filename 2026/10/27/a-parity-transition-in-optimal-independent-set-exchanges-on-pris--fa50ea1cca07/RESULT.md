# A parity transition in optimal independent-set exchanges on prism graphs

## Finding

For each integer \(n\geq3\), let \(P_n=C_n\square K_2\) be the simple prism graph with vertex set \(\mathbb Z_n\times\{0,1\}\). Vertices \((i,a)\) and \((j,b)\) are adjacent precisely when either \(i=j\) and \(a\ne b\), or \(a=b\) and \(j=i\pm1\pmod n\). Let \(\mathcal J_k(P_n)\) have as vertices the independent \(k\)-subsets of \(V(P_n)\), with an edge when their symmetric difference contains two vertices (one token jump).

The independence number and the top reconfiguration levels have the following exact descriptions.

1. If \(n\) is odd, \(\alpha(P_n)=n-1\), there are exactly \(2n\) maximum independent sets, and \(\mathcal J_{n-1}(P_n)\cong C_{2n}\).
2. If \(n\) is even, \(\alpha(P_n)=n\), there are exactly two maximum independent sets, \(\mathcal J_n(P_n)\cong2K_1\), and \(\mathcal J_{n-1}(P_n)\cong K_n\sqcup K_n\).
3. For **every** \(n\geq3\), there are exactly \(2n(n-2)\) independent sets of cardinality \(n-2\), and \(\mathcal J_{n-2}(P_n)\) is connected.

Thus a top-level independent configuration on an odd prism is exchange-reconfigurable without loss of cardinality. On even prisms, both the optimal and the one-below-optimal exchange spaces are disconnected, but all configurations become exchange-reconfigurable with two tokens below optimum.

## Assumptions and scope

All graphs are finite, simple, undirected and have labeled vertices; \(n\geq3\) includes the triangular prism. A token jump deletes exactly one occupied vertex and inserts one unoccupied vertex, maintaining independence and cardinality. It is **not** the add/remove model, and all assertions concern the specified three largest natural cardinality levels, not every smaller level. For an odd prism, the level \(n-2\) is one below optimum; for an even prism it is two below optimum. Connectedness means connectedness of the actual full exchange graph, not merely symmetry-equivalence of solutions.

## Proof

**Column encoding and maxima.** Each rung is an edge, so an independent set uses at most one vertex per column. Encode an occupied column by its layer \(0\) or \(1\), and a vacant column by a blank. Successive occupied columns must have opposite layers. The upper bound \(\alpha(P_n)\leq n\) is immediate. If all \(n\) columns are occupied, alternation closes around the cycle only for even \(n\), producing exactly two alternating layer words (the two graph bipartition classes). If \(n\) is odd, one column must be empty and alternating choices on the remaining path give exactly two sets for each choice of the vacancy. This proves \(\alpha(P_n)=n-1\) for odd \(n\), and the claimed counts of maximum independent sets for both parities.

**Odd optimum exchange cycle.** Fix odd \(n\) and one maximum word with a vacant column \(i\). The occupied neighbors at columns \(i-1\) and \(i+1\) have opposite layers: there are \(n-1\) occupied columns in one even-length path. To fill the vacancy while deleting only one token, the deleted token must be in one of these two neighboring columns; deleting any other token leaves neighbors of both layers and makes filling impossible. Deleting the token at either neighboring column and placing one at column \(i\) in the opposite layer to the remaining neighbor gives exactly one legal exchange. Hence every maximum word has degree two and its vacancy moves one column clockwise or counterclockwise. One full clockwise circuit of the odd rim interchanges the two alternating layer assignments for a given vacant column, so the \(2n\) maximum words form one cycle, \(C_{2n}\), rather than two smaller cycles.

**Even top two levels.** Fix even \(n\). The only independent \(n\)-sets are the two disjoint checkerboard classes, and they cannot differ by one token because \(n\ge4\). Any independent \((n-1)\)-set has one vacant column and alternates on the other \(n-1\) columns, a path of odd order. Its two endpoint layers agree, so the missing column can be filled in exactly one layer. Consequently every such set lies in exactly one of the two checkerboard classes. Each class has \(n\) ways to omit one vertex; all these configurations are pairwise exchange-adjacent, while configurations from different classes cannot share the required \(n-2\) vertices. This gives \(K_n\sqcup K_n\).

**All two-vacancy states.** At cardinality \(n-2\), exactly two columns are empty. There are \(n\) unordered adjacent vacancy pairs; each leaves one occupied path and has two alternating layer assignments. There are \(\binom n2-n=n(n-3)/2\) nonadjacent vacancy pairs; each leaves two nonempty occupied paths with two independent layer choices each. Hence the number of states is
\[
2n+4\left(\binom n2-n\right)=2n(n-2).
\]
The formula also holds for \(n=3\), when every pair of columns is adjacent.

**Move any two vacancies together.** If the vacancies are not adjacent, select one vacancy \(i\) and its currently occupied neighboring column \(i+1\) along the clockwise arc leading to the other vacancy. Remove the token in column \(i+1\), and insert a token in column \(i\) opposite in layer to the token at \(i-1\). The latter column is occupied unless the vacancies were already adjacent; all other constraints remain unchanged. This is one legal token jump and moves the first vacancy from \(i\) to \(i+1\). Repeat until the two vacancies become adjacent. Every state therefore connects to a state whose \(n-2\) occupied columns form one alternating path.

**Connect the adjacent-vacancy states for odd \(n\).** Such a state extends to a maximum independent set by filling either end of the occupied path: the newly occupied column has just one occupied neighboring column, so its layer is forced. For any fixed maximum set \(M\), all its \((n-2)\)-subsets are mutually exchange-adjacent (they form a clique). Adjacent maximum sets in the already proved \(C_{2n}\) intersect in an \((n-2)\)-set, so the cliques belonging to consecutive maxima overlap. Their union is connected and contains every adjacent-vacancy state, proving connectedness for odd \(n\).

**Connect the adjacent-vacancy states for even \(n\).** Since the occupied path alternates, every adjacent-vacancy state is a two-vertex deletion from one of the two full checkerboard classes. For either checkerboard class, all its two-vertex deletions form the connected Johnson graph \(J(n,n-2)\) under token jumps. To connect the two classes, take the state with occupied columns \(0,\ldots,n-3\) in one checkerboard pattern and vacant columns \(n-2,n-1\). Move the token at column \(n-3\) to column \(n-2\), then at \(n-4\) to \(n-3\), and so on down to moving the token at column \(0\) to column \(1\), always retaining the original token layer. Each move is legal: it extends the occupied block into a vacant column and vacates the moved token's former column. At the end, columns \(1,\ldots,n-2\) are occupied, with each layer opposite to the checkerboard layer at that *new* column. The endpoint is therefore a two-vertex deletion from the other checkerboard class. Both checkerboard subfamilies lie in one component, and the preceding vacancy-consolidation argument covers all states. This proves connectedness for even \(n\) and completes the theorem.

## Verification

`verify_bitmask.py` constructs prism edges on \(2n\) labeled vertices and exhaustively enumerates cardinality-constrained independent sets by bit masks. It builds actual token-jump adjacency and finds connected components. `verify_ternary.py` independently enumerates cyclic ternary words and verifies reconfiguration by explicit exchanged selected vertex pairs. Both programs check every \(n\) from \(3\) through \(10\) inclusive, including all asserted cardinalities, component and cycle structures, and the two-vacancy counts. Execute `python verify_bitmask.py` and `python verify_ternary.py`; the corresponding captured outputs are embedded alongside the programs.

The proof applies to every integer \(n\geq3\); finite enumeration is corroboration only, not the basis of the universal quantifier.

## Relationship to prior work

The independent-set reconfiguration framework and computational complexity questions were developed by Ito and coauthors (2008; expanded 2011). Avis and Hoang (2023) analyze structural and realizability questions for token-sliding independent-set reconfiguration graphs. The result here addresses a different, explicitly determined token-jumping configuration family: optimal and near-optimal independent sets of the circular ladder \(C_n\square K_2\). The general complexity and realizability statements in those sources do not give these exact parity-dependent exchange graphs or the uniform two-vacancy connectivity assertion. Relevant studies of ladder independence complexes concern topological rather than exchange-graph invariants. No claim of independent publication priority is made.

## Limitations

The theorem does not classify lower levels \(\mathcal J_k(P_n)\) for arbitrary \(k<n-2\) or their diameters, nor does it assert the same connectivity statements under token sliding. Exact two-vacancy edge counts and shortest-path lengths are not claimed. The statement is a deterministic structural theorem with executable finite checks, not an independent external scientific certification. Search of accessible literature cannot exclude an equivalent theorem in unindexed articles or theses.

## References

1. T. Ito, E. D. Demaine, N. J. A. Harvey, C. H. Papadimitriou, M. Sideri, R. Uehara and Y. Uno, *On the Complexity of Reconfiguration Problems*, ISAAC 2008, pp. 28–39, DOI: 10.1007/978-3-540-92182-0_6. Author-hosted full text: https://erikdemaine.org/papers/NPReconfiguration_ISAAC2008/paper.pdf.
2. T. Ito et al., *On the Complexity of Reconfiguration Problems*, Theoretical Computer Science 412 (2011), 1054–1065, DOI: 10.1016/j.tcs.2010.12.005; author-hosted full text: https://erikdemaine.org/papers/NPReconfiguration_TCS/paper.pdf.
3. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, Graphs and Combinatorics 39 (2023), DOI: 10.1007/s00373-023-02644-w; arXiv:2203.16861, https://arxiv.org/pdf/2203.16861.
