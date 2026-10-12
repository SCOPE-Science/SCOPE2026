# Levelability threshold for matching-deleted complete bipartite graphs
## Finding
Let \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\), and delete the matching \(M_t=\{a_i b_i:1\le i\le t\}\) from \(K_{a,b}\). The resulting graph \(G_{a,b,t}\) is levelable if and only if
\[
t\le 1\quad	ext{or}\quad (a,b,t)=(2,2,2).
\]
This is a sharp matching-deletion threshold: every complete bipartite graph is levelable, deleting one edge always preserves levelability, while deleting two or more independent edges destroys levelability except for \(K_{2,2}-M_2\cong 2K_2\).

The positive-integer levelings are completely determined. For \(t=0\), they are exactly the positive weight functions satisfying \(w(A)=w(B)\). For \(t=1\) and \(a,b\ge2\), arbitrary positive weights may be chosen on \(A\setminus\{a_1\}\) and \(B\setminus\{b_1\}\), after which the deleted-edge endpoints are forced by
\[
w(b_1)=\sum_{i=2}^a w(a_i),\qquad w(a_1)=\sum_{j=2}^b w(b_j).
\]
If \(a=1<b\), only the second displayed equality remains, with \(w(b_1)\) arbitrary; the case \(b=1<a\) is symmetric. If \(a=b=t=1\), every positive weighting works. Finally, for \((a,b,t)=(2,2,2)\), all positive levelings have the form
\[
(w(a_1),w(a_2),w(b_1),w(b_2))=(p,q,q,p)
\]
with \(p,q\in\mathbb Z_{>0}\).

## Assumptions and scope
Graphs are finite and simple. A graph is levelable when its vertices admit positive integer weights for which all inclusion-maximal independent sets have the same total weight. The result concerns only deletion of a matching from a complete bipartite graph; no claim is made for arbitrary edge-deletion sets.

## Proof
First determine the maximal independent sets. If \(t=0\), they are exactly \(A\) and \(B\). Suppose \(t\ge1\). Any independent set that meets both bipartition classes is contained in one deleted pair \(\{a_i,b_i\}\), because every other cross-pair is an edge; hence each deleted pair is a maximal independent set. The full side \(A\) is maximal exactly when \(a\ge2\), or when \(t=0\); symmetrically for \(B\). Therefore, when \(t\ge2\), both \(A\) and \(B\), together with all deleted pairs, are maximal independent sets.

For \(t=0\), equality of the weights of the two maximal independent sets is exactly \(w(A)=w(B)\), proving the stated characterization. For \(t=1\) with \(a,b\ge2\), the three maximal independent sets are \(A\), \(B\), and \(\{a_1,b_1\}\). Requiring their three weights to be equal is equivalent to the two endpoint equations displayed above. They give positive integers whenever the unmatched vertices receive arbitrary positive integer weights. If one side has one vertex, that side itself is not maximal after the unique incident edge is deleted, so only the corresponding surviving equality is required. If both sides have one vertex, the whole graph is independent and has a unique maximal independent set.

Now let \(t\ge2\). The four maximal independent sets \(A\), \(B\), \(P_1=\{a_1,b_1\}\), and \(P_2=\{a_2,b_2\}\) satisfy \(P_1\cap P_2=arnothing\). If \(a+b>4\), then
\[
P_1\cup P_2\subsetneq A\cup B.
\]
The standard positive-weight obstruction for levelable graphs therefore applies: four maximal independent sets with the latter two disjoint and with their union a strict subset of the union of the former two cannot all have the same positive weight. Hence \(G_{a,b,t}\) is not levelable whenever \(t\ge2\) and \(a+b>4\). Since \(t\ge2\) forces \(a,b\ge2\), the only remaining case is \(a=b=t=2\). There all four maximal independent sets have two vertices, so the graph is well-covered and hence levelable. Equating their weights gives exactly the pattern \((p,q,q,p)\).

## Verification
The analytic argument proves the theorem for all parameters. The accompanying script `verify.py` independently reconstructs adjacency, exhaustively enumerates maximal independent sets for every \(1\le a,b\le6\) and every admissible \(t\), verifies the structural list of maximal independent sets, checks explicit positive integer witnesses in every positive case, and checks the four-set obstruction in every negative case. Its replay output is:

`ALL CHECKS PASSED; parameter_cases=127; maximal_sets_checked=438; nonlevel_obstructions=54; a,b_range=1..6`

The finite replay is a stress test, not the proof of the infinite statement.

## Relationship to prior work
Bhaskara, Chong, Hibi, Ragunathan, and Van Tuyl introduced levelable graphs and showed, among other things, that every complete multipartite graph is levelable. Their paper also gives a general four-maximal-independent-set obstruction to levelability and explicitly notes the interest of classifying all possible weight functions for connected levelable graphs. The present result applies that framework to the natural matching-deletion neighborhood of complete bipartite graphs and determines both the exact deletion threshold and the full positive-integer leveling family in every surviving case.

Milanič and Pivač study the broader real well-covered vector space and give algorithms for computing well-covering systems on structured graph classes. Those general algorithms provide a method for fixed inputs but do not state this symbolic matching-deletion classification or its positive-integer cone. Targeted searches for the family under levelable, positive well-covered, crown-graph, and matching-deleted complete-bipartite terminology did not locate a covering statement.

## Limitations
The result does not classify arbitrary deletions from \(K_{a,b}\), and it does not claim a description of the full real well-covered vector space outside the positive cone. The originality assessment remains subject to the possibility that an older weighted-well-covered paper contains the same family under a different notation; targeted semantic and exact-term searches found no such statement.

## References
1. K. Bhaskara, M. Y. C. Chong, T. Hibi, N. Ragunathan, and A. Van Tuyl, “Levelable graphs,” arXiv:2504.02065v1, first public 2025-04-02; later published in *Annals of Combinatorics*, DOI 10.1007/s00026-026-00852-8.
2. M. Milanič and N. Pivač, “Computing well-covered vector spaces of graphs using modular decomposition,” *Computational and Applied Mathematics* 42 (2023), 360, DOI 10.1007/s40314-023-02502-8.
