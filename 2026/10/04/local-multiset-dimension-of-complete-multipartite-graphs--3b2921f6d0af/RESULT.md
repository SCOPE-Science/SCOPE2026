# Local multiset dimension of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), and let \(W\subseteq V(G)\). Put \(w_i=|W\cap X_i|\). Then \(W\) is a local multiset resolving set if and only if at most one \(w_i\) is zero and the positive numbers among \(w_1,\ldots,w_r\) are pairwise distinct. Writing the part sizes in nondecreasing order as \(a_1\le\cdots\le a_r\), the local multiset dimension is finite if and only if \(a_i\ge i-1\) for every \(2\le i\le r\). In that case \[\operatorname{lmd}(G)=\binom{r}{2}.\] Moreover, the local multiset bases are exactly the vertex sets whose part-count vector is a permutation of \((0,1,\ldots,r-1)\) respecting \(w_i\le n_i\); hence their number is \[\sum_{\sigma\in S_r}\prod_{i=1}^r\binom{n_i}{\sigma(i)-1},\] with \(\binom{n}{k}=0\) for \(k>n\).

## Assumptions and scope
All graphs are finite, simple, and connected. Let \(G=K_{n_1,\ldots,n_r}\) have partite classes \(X_1,\ldots,X_r\), with \(r\ge2\) and every \(n_i\ge1\). For a vertex set \(W\), the multiset representation of a vertex \(v\) is the multiset of distances from \(v\) to the vertices of \(W\). A set \(W\) is local multiset resolving when adjacent vertices have distinct representation multisets.

## Proof
Let \(s=|W|\) and \(w_i=|W\cap X_i|\). If \(v\in X_i\cap W\), its representation contains one zero, \(s-w_i\) copies of one, and \(w_i-1\) copies of two. If \(v\in X_i\setminus W\), its representation contains \(s-w_i\) copies of one and \(w_i\) copies of two.

Vertices in one part are nonadjacent. Across two different parts, selected vertices collide exactly when their positive part counts are equal; unselected vertices collide exactly when their part counts are equal. Positive equality is already excluded, so the only additional obstruction is two zero counts. A selected and an unselected vertex never collide because only the selected representation contains zero. This proves the all-set criterion.

Thus any valid set has at least \(r-1\) positive, pairwise distinct part counts, whose sum is at least
\[
1+2+\cdots+(r-1)=\binom r2.
\]
A minimum set therefore has exactly one zero count and positive counts \(1,2,\ldots,r-1\).

Sort the capacities as \(a_1\le\cdots\le a_r\). Assigning \(0,1,\ldots,r-1\) to the parts is feasible precisely when, after omitting one part for count zero, the remaining sorted capacities can receive \(1,\ldots,r-1\). Omitting the smallest capacity is optimal, and the elementary sorted matching criterion gives
\[
a_i\ge i-1\qquad(2\le i\le r).
\]
This proves the finiteness criterion and the value \(\binom r2\).

For a feasible minimum count assignment, the number of vertex sets realizing it is \(\prod_i\binom{n_i}{w_i}\). Summing over all permutations of \(0,1,\ldots,r-1\) gives the basis-count formula.

## Verification
The included checker reconstructs complete multipartite graphs from part labels, computes distance multisets directly for every vertex subset, and tests all adjacent pairs. It independently verifies the all-set criterion, finiteness condition, exact minimum, and basis-count formula for every complete multipartite isomorphism type of orders two through nine.

## Relationship to prior work
The 2019 foundational paper introduces local multiset dimension and gives exact values for several elementary families, including paths and stars, but does not treat complete multipartite graphs. A 2025 paper develops general bounds and several small-diameter families; targeted full-text searches found no occurrence of complete multipartite, multipartite, or complete bipartite. Its bipartite theorem agrees with the \(r=2\) specialization here.

Targeted database searches for the complete-multipartite local parameter returned complete-multipartite results for the outer multiset dimension instead. That parameter has a different admissibility condition and does not imply the selected-count collision criterion above.

## Limitations
The theorem concerns local multiset dimension, not ordinary or outer multiset dimension. The finite computation is corroborative only. Search coverage cannot exclude differently phrased or non-indexed prior work.

## References
1. R. Alfarisi, Dafik, A. I. Kristiana, I. H. Agustin, “The local multiset dimension of graphs,” International Journal of Engineering & Technology 8(3) (2019), 120–124, DOI 10.14419/ijet.v8i3.11643.
2. R. Simanjuntak, M. A. Hasan, M. Anggarawan, “Local (Outer) Multiset Dimensions of Graphs,” arXiv:2507.15071 (2025).
