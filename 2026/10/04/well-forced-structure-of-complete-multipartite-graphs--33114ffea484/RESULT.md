# Well-forced structure of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph of order \(N\), with \(r\ge2\), and let \(q\) be the number of singleton parts. Every minimal zero forcing set of \(G\) is minimum; hence every connected complete multipartite graph is well-forced. More precisely, if every part is a singleton, then the minimal zero forcing sets are exactly \(V(G)\setminus\{x\}\), one for each vertex \(x\), and \(Z(G)=N-1\). Otherwise \(Z(G)=N-2\), and the minimal zero forcing sets are exactly \(V(G)\setminus\{x,y\}\), where \(x\) and \(y\) lie in distinct parts and their two parts are not both singleton. Consequently the number of minimal zero forcing sets is \(N\) in the complete case and \[\sum_{1\le i<j\le r} n_i n_j-\binom q2\] otherwise. Among connected complete multipartite graphs, a vertex is zero-forcing-irrelevant exactly when the graph is a nontrivial star \(K_{1,m}\) with \(m\ge2\) and the vertex is its center; every other vertex belongs to some minimal zero forcing set.

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{{n_1,\ldots,n_r}}\) be connected, so \(r\ge2\), with partite classes \(X_1,\ldots,X_r\) and order \(N=\sum_i n_i\). A zero forcing set is an initial blue set from which the standard color-change rule eventually colors every vertex blue. A zero forcing set is minimal if none of its proper subsets is zero forcing, and minimum if it has cardinality \(Z(G)\). A graph is well-forced when every minimal zero forcing set is minimum. A vertex is zero-forcing-irrelevant when it belongs to no minimal zero forcing set.

## Proof
Let \(W\) be the initially white set and let \(w_i=|W\cap X_i|\). A blue vertex in \(X_i\) has exactly \(|W|-w_i\) white neighbors.

Suppose first that \(|W|\ge3\). If a first force occurs from a blue vertex in \(X_i\), then \(|W|-w_i=1\). Thus all but one white vertex lie in \(X_i\). After that unique outside white vertex is forced, at least two white vertices remain, all in \(X_i\). Every blue vertex in \(X_i\) then has zero white neighbors, while every blue vertex outside \(X_i\) has at least two. No further force is possible. Hence every zero forcing set has at most two white vertices.

Now let \(W=\{{x,y\}}\). If \(x,y\) lie in one part, every blue vertex outside that part sees both whites and every blue vertex inside it sees neither, so no force occurs. If they lie in distinct parts \(X_i,X_j\) and both parts are singleton, there is no blue vertex in either omitted part, while every blue vertex in any third part sees both whites; again no force occurs. Conversely, if \(x,y\) lie in distinct parts and at least one of those parts, say \(X_i\), is non-singleton, choose a blue vertex in \(X_i\). It has unique white neighbor \(y\) and forces it. The newly blue vertex \(y\) then has unique white neighbor \(x\) and forces it. Thus \(V(G)\setminus\{{x,y\}}\) is zero forcing exactly when the omitted vertices lie in distinct parts that are not both singleton.

If every part is singleton, then \(G=K_N\). No set with two white vertices is zero forcing, while every set with one white vertex is. Hence the minimal zero forcing sets are exactly the \(N\) sets \(V(G)\setminus\{{x\}}\), all of size \(N-1\).

Assume now that \(G\) is noncomplete. Some part is non-singleton, and connectedness provides a vertex in another part, so an admissible omitted pair exists. Thus \(Z(G)=N-2\), and every admissible \((N-2)\)-set is automatically minimal.

It remains to rule out larger minimal sets. Consider \(B=V(G)\setminus\{{x\}}\). If \(x\) lies in a non-singleton part, choose any \(y\) in another part. If \(x\) lies in a singleton part, choose \(y\) in any non-singleton part. In either case \(\{{x,y\}}\) is an admissible omitted pair, so \(B\setminus\{{y\}}\) is a zero forcing set. Hence no \((N-1)\)-set is minimal, and the full vertex set is not minimal either. This proves that every minimal set is minimum.

For counting, an admissible omitted pair is a cross-part pair except for a pair of singleton parts. There are \[\sum_{{i<j}}n_i n_j-\binom q2\] such pairs.

Finally, a vertex is irrelevant precisely when it is absent from every minimal-set construction. In a star \(K_{{1,m}}\) with \(m\ge2\), every admissible omitted pair consists of the center and one leaf, so the center lies in no minimal zero forcing set. Conversely, if the graph is not such a star, every vertex can be avoided by an admissible omitted pair: with two non-singleton parts choose one omitted vertex from each while avoiding the prescribed vertex; with at least three parts choose one omitted vertex from a non-singleton part and one from another part, again avoiding the prescribed vertex. Complete graphs also have no irrelevant vertex because each vertex belongs to all but one of the \(N\) minimal \((N-1)\)-sets.

## Verification
The included checker constructs every connected complete multipartite isomorphism type of orders \(2\) through \(10\). For each vertex subset it simulates the standard color-change rule directly until either all vertices are blue or no force is available. It then tests inclusion-minimality by deleting each initially blue vertex separately. The computed minimal zero forcing sets are compared exactly with the complement-pair classification, and the checker also compares their common cardinality, total number, and irrelevant-vertex set.

## Relationship to prior work
The 2023 paper introducing the term well-forced focuses on structural well-forcedness, characterizes well-forced trees, and studies irrelevant vertices. Its verified primary MSC is \(05C50\). The complete-multipartite classification above addresses the same structural questions on a canonical dense graph class rather than on trees.

The 2022 paper on minimal zero forcing sets studies the upper zero forcing number and equality between maximum-minimal and minimum zero forcing numbers. It explicitly lists graphs of the form \(K_a\vee\overline{{K_b}}\) among families satisfying this equality, so complete multipartite graphs with only one non-singleton part are prior-covered at the level of well-forcedness. It does not state an arbitrary complete-multipartite classification, and its full text has no occurrence of “multipartite.”

The 2018 zero forcing polynomial paper gives general formulas for zero forcing sets of sizes \(N\), \(N-1\), and \(N-2\), and explicitly gives the complete-bipartite polynomial. Consequently the numerical count of minimum zero forcing sets here is not the originality basis; it is compatible with and recoverable from those coefficient results once the complete-multipartite neighborhood structure is inserted. The surviving contribution is the arbitrary complete-multipartite classification of all inclusion-minimal zero forcing sets, the resulting well-forced theorem beyond the prior one-non-singleton subclass, and the exact irrelevant-vertex classification.

## Limitations
The theorem concerns standard zero forcing, not positive-semidefinite, skew, or other forcing rules. The well-forced conclusion for the one-non-singleton complete split subclass is prior-covered, and the count of minimum sets is compatible with prior general coefficient formulas; these are included for completeness rather than claimed independently. The exhaustive computation through order ten is finite corroboration only; the arbitrary-order theorem follows from the proof. Search coverage cannot exclude a differently phrased or non-indexed arbitrary complete-multipartite well-forced classification.

## References
1. C. Grood, R. Haas, B. Jacob, E. King, S. Nasserasr, “Well-forced graphs,” arXiv:2312.14298v1, 21 December 2023; later published in Graphs and Combinatorics 40 (2024), 129, DOI 10.1007/s00373-024-02827-z.
2. B. Brimkov, J. Carlson, “Minimal Zero Forcing Sets,” arXiv:2204.01810v1, 4 April 2022; Australasian Journal of Combinatorics 90 (2024), 363–377.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1, 26 January 2018; Discrete Applied Mathematics 258 (2019), 35–48.
