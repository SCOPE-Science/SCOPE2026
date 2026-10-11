# Well-forced structure of complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph of order \(N\), with \(r\ge2\), and let \(q\) be the number of singleton parts.

Every minimal zero forcing set of \(G\) is minimum, so \(G\) is well-forced. The well-forced conclusion itself was previously stated by Grood, Haas, Jacob, King, and Nasserasr. The sharper classification below corrects the boundary in the proof of their complete-multipartite proposition.

If every part is a singleton, then \(G=K_N\), the minimal zero forcing sets are exactly
\[
V(G)\setminus\{x\},
\]
one for each vertex \(x\), and \(Z(G)=N-1\).

Otherwise \(Z(G)=N-2\), and the minimal zero forcing sets are exactly
\[
V(G)\setminus\{x,y\},
\]
where \(x\) and \(y\) lie in distinct parts and their two parts are not both singleton. Consequently the number of minimal zero forcing sets is
\[
\sum_{1\le i<j\le r}n_i n_j-\binom q2.
\]

Among connected complete multipartite graphs, a vertex is zero-forcing-irrelevant exactly when the graph is a nontrivial star \(K_{1,m}\) with \(m\ge2\) and the vertex is its center. Every other vertex belongs to some minimal zero forcing set.

## Assumptions and scope

All graphs are finite and simple. A zero forcing set is an initial blue set from which the standard color-change rule eventually colors every vertex blue. A zero forcing set is minimal if none of its proper subsets is zero forcing, and minimum if it has cardinality \(Z(G)\). A graph is well-forced if every minimal zero forcing set is minimum. A vertex is zero-forcing-irrelevant if it lies in no minimal zero forcing set.

The result concerns the standard zero forcing rule on connected complete multipartite graphs. Its new content is the exact all-part-profile classification of minimal sets, including the singleton-part correction to the earlier complete-multipartite proof, together with the exact irrelevant-vertex classification.

## Proof

Let \(W\) be the initially white set and write \(w_i=|W\cap X_i|\). A blue vertex in \(X_i\) has exactly
\[
|W|-w_i
\]
white neighbors.

Suppose first that \(|W|\ge3\). If a first force occurs from a blue vertex in \(X_i\), then \(|W|-w_i=1\). Thus all but one white vertex lie in \(X_i\). After that unique outside white vertex is forced, at least two white vertices remain, all in \(X_i\). Every blue vertex in \(X_i\) then has no white neighbors, while every blue vertex outside \(X_i\) has at least two. No further force is possible. Hence every zero forcing set has at most two white vertices.

Now let \(W=\{x,y\}\). If \(x,y\) lie in one part, every blue vertex outside that part sees both whites and every blue vertex inside it sees neither, so no force occurs. If they lie in distinct singleton parts, neither omitted part contains a blue vertex, while every blue vertex in any other part sees both whites; again no force occurs.

Conversely, suppose \(x,y\) lie in distinct parts and at least one of those parts, say \(X_i\), is non-singleton. Choose a blue vertex in \(X_i\). It has the unique white neighbor \(y\) and forces it. The newly blue vertex \(y\) then has the unique white neighbor \(x\) and forces it. Therefore
\[
V(G)\setminus\{x,y\}
\]
is zero forcing exactly when \(x,y\) lie in distinct parts that are not both singleton.

If all parts are singleton, \(G=K_N\). No set with two white vertices is zero forcing, while every set with one white vertex is. Thus the minimal zero forcing sets are exactly the \(N\) complements of one vertex and \(Z(G)=N-1\).

Assume now that \(G\) is noncomplete. Some part is non-singleton, and connectedness provides a vertex in another part, so an admissible omitted pair exists. Hence \(Z(G)=N-2\), and every admissible \((N-2)\)-set is automatically minimal.

It remains to exclude larger minimal sets. Let \(B=V(G)\setminus\{x\}\). If \(x\) lies in a non-singleton part, choose \(y\) in another part. If \(x\) lies in a singleton part, choose \(y\) in any non-singleton part. In either case \(\{x,y\}\) is an admissible omitted pair, so \(B\setminus\{y\}\) is zero forcing. Thus no \((N-1)\)-set is minimal, and the full vertex set is not minimal either. This proves that every minimal zero forcing set is minimum.

An admissible omitted pair is a cross-part pair except for a pair of singleton parts, yielding the stated count.

Finally, a vertex is irrelevant precisely when every admissible omitted pair contains it. In a star \(K_{1,m}\) with \(m\ge2\), every admissible omitted pair consists of the center and one leaf, so the center belongs to no minimal zero forcing set. Conversely, outside this case, every prescribed vertex can be avoided by some admissible pair: if there are two non-singleton parts, choose one omitted vertex from each while avoiding the prescribed vertex; if there is exactly one non-singleton part and at least two other parts, choose one omitted vertex from the non-singleton part and one from another part while avoiding the prescribed vertex. Complete graphs have no irrelevant vertex because each vertex belongs to all but one of the \(N\) minimal \((N-1)\)-sets.

## Verification

A direct exhaustive checker constructs every connected complete multipartite isomorphism type through order ten. For every initial blue subset it simulates the standard forcing rule to termination and tests inclusion-minimality by deleting each initially blue vertex. The computed minimal sets agree with the complement classification, their cardinalities agree with the stated zero forcing numbers, and the resulting irrelevant-vertex sets agree with the star-center criterion.

The finite computation is corroborative only. The arbitrary-order theorem follows from the white-profile proof above.

## Relationship to prior work

Grood, Haas, Jacob, King, and Nasserasr previously stated in Proposition 3.2 of *Well-forced graphs* that every complete multipartite graph with at least two partite sets is well-forced. Their proof says that a zero forcing set may omit at most two vertices, that two omitted vertices must lie in different parts, and that every set satisfying that condition is zero forcing.

The last assertion needs a singleton-part qualification. If the two omitted vertices lie in two singleton parts, there is no blue vertex in either omitted part and every blue vertex elsewhere sees both white vertices, so no force is possible. In particular, the assertion fails for complete graphs. The well-forced conclusion remains correct, but the earlier proof does not give the correct all-profile classification of minimal sets.

The result here therefore does not claim originality for well-forcedness itself. Its contribution is the corrected exact criterion: in the noncomplete case the omitted pair must lie in distinct parts that are not both singleton. This gives the full set of inclusion-minimal zero forcing sets for arbitrary part profiles and yields the exact zero-forcing-irrelevant vertex boundary.

Brimkov and Carlson previously treated minimal zero forcing sets in general and covered the complete-split family \(K_a\vee\overline{K_b}\) at the level of equality between the upper and minimum zero forcing numbers. Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart gave general top-degree coefficients of the zero forcing polynomial and the complete-bipartite polynomial. Those results provide prior coverage of special subclasses or numerical counts, but they do not supply the corrected arbitrary complete-multipartite minimal-set classification and star-center irrelevance criterion.

## Limitations

The well-forced conclusion for complete multipartite graphs is prior-published and is not claimed as new. The present contribution is the corrected minimal-set classification across singleton and non-singleton part profiles and the exact irrelevant-vertex classification.

The theorem concerns standard zero forcing, not positive-semidefinite, skew, or other forcing rules. The complete-split subclass is also prior-covered at the equality level, and the numerical count of minimum sets is compatible with prior zero-forcing-polynomial coefficient formulas.

The exhaustive computation through order ten is finite corroboration only; the arbitrary-order result follows from the proof. A differently phrased or non-indexed exact classification may exist.

## References

1. C. Grood, R. Haas, B. C. Jacob, E. L. C. King, S. Nasserasr, “Well-forced graphs,” arXiv:2312.14298v1; *Graphs and Combinatorics* 40 (2024), 129, DOI 10.1007/s00373-024-02827-z.
2. B. Brimkov, J. Carlson, “Minimal Zero Forcing Sets,” arXiv:2204.01810v1; *Australasian Journal of Combinatorics* 90 (2024), 363–377.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1; *Discrete Applied Mathematics* 258 (2019), 35–48.
