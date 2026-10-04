# Failed skew zero forcing at the false-twin-free boundary of threshold graphs
## Finding
Let \(G\) be a connected noncomplete threshold graph with canonical creation string
\[
01^{b_1}01^{b_2}\cdots01^{b_p},
\]
where \(p\ge2\), every \(b_i\ge1\), and at least one \(b_i\ge2\). Write \(A_i\) for the singleton \(0\)-block immediately preceding the clique block \(B_i\), let \(|B_i|=b_i\), and set
\[
N=p+\sum_{i=1}^p b_i,
\qquad
c_j=j+\sum_{h<j}b_h.
\]
Then
\[
F^{-}(G)=N-3.
\]
The maximum failed skew zero forcing sets are exactly the complements of the following three-vertex white sets:

1. three vertices from one block \(B_j\); or
2. two vertices from \(B_j\) together with any one vertex occurring strictly before \(B_j\) in the creation string.

Consequently the exact number of maximum failed skew zero forcing sets is
\[
M(G)=\sum_{j=1}^p\left(\binom{b_j}{2}c_j+\binom{b_j}{3}\right).
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. A skew zero forcing process starts from a filled set \(S\). At any stage, any vertex, filled or unfilled, that has exactly one unfilled neighbor may force that neighbor to become filled. A set is failed if this process cannot fill every vertex. Equivalently, a nonempty white set \(W\) is skew-stalled when every vertex has either zero or at least two neighbors in \(W\).

The canonical threshold representation used here has each \(0\)-block of size one. Thus \(A_i\) is adjacent precisely to \(B_i\cup\cdots\cup B_p\), all vertices in the \(B\)-blocks form a clique, and a vertex of \(B_j\) is adjacent to \(A_1,\ldots,A_j\). The hypotheses \(p\ge2\) and at least one \(b_i\ge2\) exclude complete graphs and ensure that nonempty stalled white sets exist.

This family is a natural boundary class. If a threshold graph has a \(0\)-block of size at least two, two vertices in that block are nonadjacent open twins and already form a two-vertex skew-stalled white set. Here that immediate false-twin obstruction is absent.

## Proof
Let \(m(G)\) be the minimum size of a nonempty skew-stalled white set. A failed filled set \(S\) terminates with some nonempty stalled white residue \(W\subseteq V(G)\setminus S\), so \(|S|\le N-|W|\le N-m(G)\). Conversely, the complement of a minimum stalled set is itself a failed filled set. Therefore
\[
F^{-}(G)=N-m(G),
\]
and maximum failed filled sets are exactly the complements of minimum stalled white sets.

There is no stalled white set of size one because \(G\) is connected. There is no stalled white set of size two. If the two white vertices are adjacent, each sees the other as its unique white neighbor. If they are nonadjacent and the pair were stalled, they would have identical open neighborhoods. In this threshold representation the only nonadjacent pairs lie among the vertices \(A_i\), and for \(i<j\),
\[
N(A_i)=B_i\cup\cdots\cup B_p
\supsetneq
B_j\cup\cdots\cup B_p=N(A_j),
\]
because every \(B_i\) is nonempty. Hence \(m(G)\ge3\).

Now consider a three-vertex white set \(W\). If \(W\) contains no vertex from any \(B_j\), let \(A_s\) be its least-indexed member. Then a vertex of \(B_s\) sees exactly that one white vertex, so \(W\) is not stalled. If \(W\) contains exactly one \(B_j\)-vertex, then \(A_j\) sees exactly that white vertex, so again \(W\) is not stalled. Thus every stalled triple contains at least two \(B\)-vertices.

Let \(j\) be the largest block index for which \(W\cap B_j\ne\varnothing\). Suppose first that \(|W\cap B_j|=1\). Let \(r<j\) be the largest index of another represented \(B\)-block. Then \(A_{r+1}\) is adjacent to the unique white vertex in \(B_j\), but to no white \(B\)-vertex in blocks of index at most \(r\), and it is adjacent to no \(A\)-vertex. Hence \(A_{r+1}\) sees exactly one white neighbor, a contradiction. Therefore \(|W\cap B_j|\ge2\).

With three white vertices total, either all three lie in \(B_j\), or exactly two lie there and the third vertex is some \(q\notin B_j\). By maximality of \(j\), a third \(B\)-vertex can only lie in an earlier block. If \(q=A_i\) with \(i>j\), either white vertex in \(B_j\) sees the other white \(B_j\)-vertex but not \(A_i\), hence has exactly one white neighbor. Thus such a triple is not stalled. The only remaining possibility is that \(q\) occurs before \(B_j\) in the creation string.

Conversely, every triple of either stated form is stalled. Every \(A_i\) sees either both selected vertices of \(B_j\) or none of them. Every \(B\)-vertex outside the triple sees at least the two selected vertices of \(B_j\). A selected vertex of \(B_j\) sees the other selected \(B_j\)-vertex and also the earlier third vertex, while in the three-in-\(B_j\) case it sees the other two. Hence no vertex has exactly one white neighbor.

So \(m(G)=3\), proving \(F^{-}(G)=N-3\), and the classification of maximum failed sets follows by complementation. For fixed \(j\), there are \(\binom{b_j}{3}\) all-in-\(B_j\) triples and \(\binom{b_j}{2}c_j\) triples with exactly two vertices in \(B_j\), because exactly \(c_j\) vertices occur before that block. The largest represented \(B\)-block is unique, so these families are disjoint and summing gives the formula for \(M(G)\).

## Verification
A standalone verifier exhaustively checked every positive block-size vector \((b_1,\ldots,b_p)\) with \(p\ge2\), at least one \(b_i\ge2\), and total graph order from \(5\) through \(11\). For each graph it independently enumerated all white subsets of sizes one through three, compared the skew-stalled triples with the theorem's structural list, then enumerated all initial filled sets and replayed skew closure to check both \(F^{-}(G)=N-3\) and the maximum-set count. The replay result was:

`VERIFY_OK graphs=129 subset_checks=179848 stalled_triples=3787 maximum_sets=3787 max_order=11`

The finite computation is a stress test of the proof, not an argument for the infinite family.

## Relationship to prior work
Shitov's complexity paper formalizes failed skew zero forcing through skew-stalled sets and proves the general decision problem NP-complete; it does not supply an exact threshold-graph classification. The 2022 characterization of graphs with failed skew zero forcing number one covers a different low-parameter regime and explicitly raises the question of counting maximum failed skew zero forcing sets. A 2025 study determines the parameter for path powers and circulant graphs and surveys several previously treated families, but does not state a threshold-graph formula in its inspected text.

The original 2016 article introducing the failed skew parameter reports classifications and formulas for several graph families in its abstract. Its full text was not available from the lawful sources inspected, so possible hidden overlap with a threshold-graph specialization remains a bibliographic risk. No covering threshold-graph result was located in the searched sources, but failed search is not a proof of novelty.

## Limitations
The theorem is restricted to connected noncomplete threshold graphs whose canonical \(0\)-blocks are all singletons. It deliberately excludes complete graphs and does not classify the complementary case with larger \(0\)-blocks beyond noting the immediate two-vertex false-twin stalled set. It also does not enumerate failed sets of nonmaximum size.

Computational verification was exhaustive only through order \(11\); the unrestricted statement rests on the proof above. Bibliographic coverage is limited by the inaccessible full text of the 2016 foundational article and by the possibility of older results indexed under alternate threshold/split/creation-sequence terminology.

## References
- Y. Shitov, *On the complexity of failed zero forcing*, arXiv:1609.00211, first version posted 2016-09-01.
- M. Ansill, B. Jacob, J. Penzellna, D. Saavedra, *Failed skew zero forcing on a graph*, Linear Algebra and its Applications 509 (2016), DOI: 10.1016/j.laa.2016.07.019.
- E. I. Johnson, P. J. Vick, A. Narayan, *Characterization of All Graphs with a Failed Skew Zero Forcing Number of 1*, Mathematics 10 (2022), 4463, DOI: 10.3390/math10234463.
- E. I. Johnson, P. J. Vick, R. Flórez, A. Narayan, *Failed Skew Zero Forcing Numbers of Path Powers and Circulant Graphs*, AppliedMath 5 (2025), 32, DOI: 10.3390/appliedmath5020032.
