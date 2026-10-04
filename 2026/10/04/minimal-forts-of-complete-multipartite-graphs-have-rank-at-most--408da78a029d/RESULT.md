# Minimal forts of complete multipartite graphs have rank at most three
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\), with partite sets \(V_1,\ldots,V_r\). A nonempty vertex set \(F\) is a fort when every vertex outside \(F\) has either zero or at least two neighbors in \(F\). The inclusion-minimal forts are exactly the following three types:

1. two vertices in one part \(V_i\);
2. two vertices in two distinct singleton parts;
3. three vertices in three distinct parts, with at most one of those three parts a singleton.

Thus the fort hypergraph of every complete multipartite graph has rank at most \(3\). If \(q=|\{i:n_i=1\}|\) and \(L=\{i:n_i\ge2\}\), its number of edges is
\[
f_m(G)=\sum_{i\in L}\binom{n_i}{2}+\binom{q}{2}+\sum_{\{i,j,k\}\subseteq L}n_i n_j n_k+q\sum_{\{i,j\}\subseteq L}n_i n_j.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The statement concerns connected complete multipartite graphs, equivalently \(r\ge2\). Minimal means inclusion-minimal among nonempty forts. No claim is made here about compatible collections of forts or about arbitrary graph classes.

## Proof
Write \(f_i=|F\cap V_i|\) and \(s=|F|\). Every vertex \(v\in V_i\setminus F\) is adjacent to all vertices of \(F\) outside \(V_i\) and to none inside \(V_i\), so
\[
|N(v)\cap F|=s-f_i.
\]
Therefore \(F\) is a fort exactly when \(s-f_i\ne1\) for every index \(i\) with \(f_i<n_i\).

A two-set inside one part is a fort: outside vertices in that part see zero members of it, and vertices in every other part see two. A two-set meeting distinct parts is a fort exactly when both of those parts are singleton; otherwise a vertex remaining in one selected part sees exactly the other selected vertex. This proves the two-vertex cases.

Now let \(F\) be an inclusion-minimal fort with no two-vertex fort contained in it. Then \(F\) contains at most one vertex from each part, and it cannot contain vertices from two singleton parts. If \(s=3\), the displayed criterion shows that \(F\) is a fort: a vertex remaining in a selected nonsingleton part sees the other two members, while a vertex in an unselected part sees all three. None of its two-subsets is a fort precisely because at most one selected part is singleton. Hence the stated three-vertex transversals are exactly the minimal forts of size three.

Finally suppose \(s\ge4\). If some part contributes at least two vertices, \(F\) contains a two-vertex fort. Otherwise \(F\) is a transversal of at least four parts. If at least two selected parts are singleton, it contains a two-vertex fort of the second type; if at most one is singleton, any three selected vertices form a fort of the third type. Thus no fort of size at least four is inclusion-minimal. Counting the three disjoint types gives the formula.

## Verification
The accompanying `verify.py` independently constructs every complete multipartite graph type of order at most \(9\), enumerates every nonempty vertex subset, tests the fort condition directly from neighborhoods, extracts inclusion-minimal forts without using the classification, and compares the result with both the structural description and the closed formula. Its recorded replay output is in `verification_output.txt`.

## Relationship to prior work
Abiad and Ghasemi Nezhad study the abundance and algorithmic counting of minimal forts, including an exact linear-time count for trees, which motivates exact fort-hypergraph descriptions for natural graph families. Cameron, Hogben, Kenter, Mojallal, and Schuerger introduced the fort hypergraph and explicitly identify complete bipartite graphs as having only the same-part two-vertex minimal forts. Their complete-bipartite case is recovered here, while three or more parts introduce genuinely new minimal three-vertex transversals. Searches of the relevant full text, web literature, and the semantic research database did not identify an existing complete-multipartite classification.

## Limitations
The theorem classifies and counts minimal forts only for complete multipartite graphs. It does not classify compatible subcollections, compute every fort (as opposed to every minimal fort), or claim a new zero-forcing-number formula. The finite enumeration is a stress test and is not used as the proof of the general theorem. A poorly indexed or unpublished prior classification remains a residual literature risk.

## References
A. Abiad and S. Ghasemi Nezhad, *Fort Abundance in Zero Forcing*, arXiv:2609.11754v1, first submitted 2026-09-10.

T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v3; Australasian Journal of Combinatorics 95 (2026), 214--247.
