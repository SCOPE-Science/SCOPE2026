# Minimum edge-cover exchanges on nearly balanced bicliques are permutation-star line graphs

## Finding

For every integer \(n\ge2\), consider the complete bipartite graph \(K_{n+1,n}\), with a distinguished part of \(n+1\) vertices and a second part of \(n\) vertices. A minimum edge cover is an edge set of minimum size incident to every vertex. Two minimum edge covers are **exchange adjacent** when their edge sets differ by deleting exactly one edge and inserting exactly one edge. Let \(X_n\) denote this exchange graph.

**Theorem.** The graph \(X_n\) is isomorphic to the line graph of the permutation star-transposition graph on \(n+1\) symbols. In particular, it is connected and vertex-transitive, and it has
\[
|V(X_n)|=\frac{n(n+1)!}{2},\qquad \deg(X_n)=2n-2,\qquad |E(X_n)|=\frac{n(n+1)!(n-1)}{2},
\]
\[
\#K_3(X_n)=(n+1)!\binom n3,\qquad
\operatorname{diam}(X_n)=\left\lfloor\frac{3n}{2}\right\rfloor.
\]
It also satisfies \(\chi(X_n)=n\), \(\omega(X_n)=n\), and \(\alpha(X_n)=(n+1)!/2\).

By contrast, on \(K_{n,n}\), every minimum edge cover is a perfect matching, and **all** \(n!\) minimum edge covers are isolated under one-edge exchanges. Thus increasing the size of one bipartition class by exactly one changes the optimum-solution exchange graph from completely disconnected to connected, with the displayed sharp diameter.

## Assumptions and scope

Graphs are finite and simple. The minimum edge cover is an *edge* cover (not a vertex cover and not a biclique cover). The exchange rule replaces one chosen edge; intermediate edge covers must remain minimum and feasible. No quotient is taken by graph automorphisms: all bipartition vertices are labeled. \(L(H)\) denotes the line graph of \(H\). The **permutation star graph** \(S_{n+1}\) has all permutations of the symbol set \(\{\ast,1,\ldots,n\}\) as vertices, with two permutations adjacent if one is obtained by exchanging the symbol \(\ast\) with the symbol in one other position. This is the familiar star-transposition Cayley graph on \(n+1\) symbols, not the ordinary tree \(K_{1,n}\).

## Proof

**1. Minimum covers as surjective words.** Because the larger part has \(n+1\) vertices, every edge cover uses at least \(n+1\) edges. This bound is attained by matching each of the \(n\) vertices of the smaller part to a different larger-part vertex and covering the remaining larger-part vertex with one additional edge. In any minimum cover, each larger-part vertex is incident with exactly one chosen edge. Label those vertices by positions \(1,\ldots,n+1\) and the smaller-part vertices by colors \(1,\ldots,n\). A minimum cover is precisely a surjection
\[
f:\{1,\ldots,n+1\}\twoheadrightarrow\{1,\ldots,n\}.
\]
There is one repeated color, occurring exactly twice, with all other colors occurring once. Exchanging one cover edge is exactly changing the value of the word at a single position without destroying surjectivity.

**2. Canonical bijection with star-graph edges.** Let the repeated color in \(f\) occur at positions \(p,q\). Form the two distinct permutations \(\pi_p,\pi_q\) of \(\{\ast,1,\ldots,n\}\) by replacing the entry at \(p\), respectively \(q\), by \(\ast\). Then \(\pi_p\) and \(\pi_q\) differ by interchanging the location of \(\ast\) and the repeated color, so they determine one edge of \(S_{n+1}\). Conversely every edge of \(S_{n+1}\) interchanges \(\ast\) with one color; replacing \(\ast\) in each endpoint with that color gives the same surjective word with that color repeated. These constructions are inverses.

For the adjacency claim, if two surjections differ only at position \(p\), replacing that position by \(\ast\) gives a common permutation endpoint of their two edges of \(S_{n+1}\). Necessarily both original entries at position \(p\) were the repeated colors of their respective words: otherwise changing a uniquely occurring color would lose surjectivity. Conversely, two distinct edges of \(S_{n+1}\) incident at a permutation \(\pi\) with \(\ast\) at \(p\) correspond to surjections whose only different entries are at \(p\). This proves the graph isomorphism
\[
X_n\cong L(S_{n+1}).
\]

**3. Counts and other invariants.** The root graph \(S_{n+1}\) has \((n+1)!\) vertices, degree \(n\), and hence \(n(n+1)!/2\) edges. It is connected because the star transpositions generate the symmetric group; it is vertex-transitive by relabeling permutations. Its edges change permutation parity, so it is bipartite and triangle-free. Its line graph therefore has the claimed order and constant degree \(2(n-1)\). The edge count follows by the handshake lemma. Every triangle of a line graph of a triangle-free simple graph is formed by three root edges sharing an endpoint. Hence \(\#K_3(X_n)=(n+1)!\binom n3\).

Each root vertex supplies a clique of size \(n\), and a clique larger than \(n\) cannot exist: in a triangle-free root graph any collection of pairwise incident edges shares an endpoint. Therefore \(\omega(X_n)=n\). Since \(S_{n+1}\) is \(n\)-regular bipartite, its edges have a proper \(n\)-coloring by the bipartite edge-coloring theorem. Thus \(\chi(L(S_{n+1}))=n\). A maximum matching of the regular bipartite graph \(S_{n+1}\) is perfect, with \((n+1)!/2\) edges, and an independent set in its line graph is exactly a matching; therefore \(\alpha(X_n)=(n+1)!/2\).

**4. Exact diameter of the root graph.** Identify \(\ast\) with \(0\), and (if necessary) invert the position-to-symbol permutation convention. Then \(S_{n+1}\) is the Cayley graph of permutations of \(\{0,1,\ldots,n\}\) with generators \(t_i=(0\ i)\) for \(1\le i\le n\); either left or right multiplication gives the same undirected network and metric. Suppose \(\sigma\) has a cycle containing \(0\) of length \(\ell_0\), and its other nontrivial cycles have lengths \(\ell_1,\ldots,\ell_r\) (fixed points outside the central cycle are omitted). The exact minimum number of star transpositions expressing \(\sigma\) is
\[
d_{S_{n+1}}(\mathrm{id},\sigma)=(\ell_0-1)+\sum_{j=1}^r(\ell_j+1).
\]
For an upper bound, the cycle containing \(0\) has an expression of length \(\ell_0-1\), and an off-center cycle of length \(\ell_j\) has an expression of length \(\ell_j+1\), obtained by first introducing \(0\) and finally restoring it. For the lower bound, work from \(\sigma\) to the identity. A star transposition either joins two cycles or splits one. Let \(c\) be the number of cycles of \(\sigma\), including fixed points; if \(M\) of the steps merge cycles, the total number of steps is \((n+1-c)+2M\), since the total number of cycles must increase to \(n+1\). Every nontrivial cycle not containing \(0\) must be joined to the central cycle at least once, as no step can alter that cycle before the symbol \(0\) joins it. Thus \(M\ge r\), giving the displayed expression.

For each \(\ell_j\ge2\), one has \(\ell_j+1\le3\ell_j/2\). The central contribution is \(\ell_0-1\). Counting all symbols, the distance is at most \(\lfloor3n/2\rfloor\). Equality is attained when \(n\) is even by \(\sigma=(1\ 2)(3\ 4)\cdots(n-1\ n)\), fixing \(0\), and when \(n\) is odd by \(\sigma=(0\ 1)(2\ 3)\cdots(n-1\ n)\). Therefore
\[
\operatorname{diam}(S_{n+1})=D:=\left\lfloor\frac{3n}{2}\right\rfloor.
\]

**5. Exact diameter of the line graph.** For distinct edges \(e,f\) of a connected graph, their distance in its line graph is
\[
d_{L(S_{n+1})}(e,f)=1+\min_{u\in e,\,v\in f}d_{S_{n+1}}(u,v).
\]
Since the root graph is bipartite of diameter \(D\), the distances from a fixed endpoint of \(f\) to the two adjacent endpoints of \(e\) have opposite parity. They therefore cannot both equal \(D\), and the minimum endpoint distance is at most \(D-1\). This proves \(\operatorname{diam}(X_n)\le D\).

For sharpness take the extremal permutation \(\sigma\) from Step 4, and choose \(i=1,j=2\) when \(n\) is even, or \(i=j=1\) when \(n\) is odd. In either case \(t_i\sigma t_j=\sigma\). Consider the root edges \(e=\{\mathrm{id},t_i\}\) and \(f=\{\sigma,\sigma t_j\}\). Since every root edge changes parity and \(\sigma\) is distance \(D\) from the identity, the cross-endpoint distances are exactly
\[
d(\mathrm{id},\sigma)=d(t_i,\sigma t_j)=D,\quad
d(\mathrm{id},\sigma t_j)=d(t_i,\sigma)=D-1.
\]
Indeed, the latter two are adjacent to a diameter-distance vertex, and must have the opposite parity while not exceeding \(D\). Thus \(d_{X_n}(e,f)=D\), proving the formula for all \(n\ge2\).

**6. Balanced discontinuity.** On \(K_{n,n}\), minimum edge covers consist of \(n\) edges, hence are perfect matchings. Distinct perfect matchings cannot differ in only one edge: once \(n-1\) matching edges are fixed, the final edge is forced. There are \(n!\) perfect matchings, all isolated in the exchange graph. This completes the proof.

## Verification

The self-contained `verify.py` enumerates all surjective words directly and independently by duplicate-position construction, reconstructs the permutation star graph, and tests incidence versus single-coordinate exchanges. It verifies the line-graph identification for \(2\le n\le5\), independent direct surjection enumeration for \(2\le n\le6\), and connectedness, degree and distance from a representative vertex for \(2\le n\le7\). Vertex-transitivity, proved above, makes the representative-vertex maximum distance the graph diameter. At the checked values the results are:

| \(n\) | Vertices | Edges | Triangles | Diameter |
|---:|---:|---:|---:|---:|
| 2 | 6 | 6 | 0 | 3 |
| 3 | 36 | 72 | 24 | 4 |
| 4 | 240 | 720 | 480 | 6 |
| 5 | 1800 | 7200 | 7200 | 7 |
| 6 | 15120 | 75600 | 100800 | 9 |
| 7 | 141120 | 846720 | 1411200 | 10 |

The infinite-family proof is combinatorial. Enumeration does not serve as its proof.

## Relationship to prior work

The permutation star-transposition graph and its diameter are classical network and permutation results. Irving and Rattan study minimal star factorizations of permutations; Kumar, Rajendraprasad and Sudeep recall the undirected star-graph diameter while investigating **oriented** diameters. The present contribution is the exact identification of the **minimum-edge-cover exchange graph** of \(K_{n+1,n}\) with the **line graph** of that permutation network, together with the consequences for feasible-cover reconfiguration and the balanced/unbalanced discontinuity. The known root-star diameter is not itself presented as new.

## Limitations

The theorem concerns only complete bipartite graphs with part sizes \(n,n\) or \(n+1,n\), and only single-edge replacements constrained to remain minimum edge covers. It does not assert corresponding statements for larger part imbalances, weighted covers, or other reconfiguration rules. The literature comparison does not rule out every earlier equivalent formulation, particularly an unindexed treatment of surjective-word Hamming graphs or line graphs of star networks. Independent review of the present proof has not been performed.

## References

1. J. Irving and A. Rattan, *Factorizations of Permutations into Star Transpositions*, arXiv:math/0610640 (first posted 2006-10-21); journal version *Discrete Mathematics* **309** (2009), 1435–1442.
2. K. S. Ajish Kumar, D. Rajendraprasad and K. S. Sudeep, *Oriented Diameter of Star Graphs*, arXiv:1911.10340 (2019). Its introduction states the classical diameter of the undirected permutation star graph.
3. S. B. Akers and B. Krishnamurthy, *A Group-Theoretic Model for Symmetric Interconnection Networks*, *IEEE Transactions on Computers* **38** (1989), DOI:10.1109/12.21148. Foundational network context; complete text was not inspected here.
