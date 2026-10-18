# The unique six-vertex colour-refinement collision among finite directed acyclic graphs

## Finding
Let \(\mathcal D_n\) be the isomorphism classes of finite, loopless, simple directed acyclic graphs (DAGs) on exactly \(n\) vertices, with no restrictions on weak connectivity or transitive edges. The language has one directed-arc predicate \(R\), and \(\equiv_{C^2}\) denotes equivalence under **all** sentences of two-variable first-order logic with counting quantifiers. For \(1\le n\le6\), the numbers of isomorphism types and of \(C^2\)-equivalence classes occurring inside \(\mathcal D_n\) are respectively

\[
\begin{array}{c|rrrrrr}
n&1&2&3&4&5&6\\\hline
|\mathcal D_n|&1&2&6&31&302&5984\\
|\mathcal D_n/{\equiv_{C^2}}|&1&2&6&31&302&5983.
\end{array}
\]

Consequently, distinct DAGs with at most five vertices (even of different orders) are always separated by \(C^2\). At six vertices, precisely one \(C^2\)-class contains two nonisomorphic DAGs; all other classes contain one isomorphism type. The exceptional pair is the disjoint union of two transitively oriented triangles and an acyclic orientation of an undirected six-cycle with two sources, two intermediate vertices, and two sinks.

## Assumptions and scope
A directed graph here has a finite, nonempty vertex set, no loops and at most one arc per ordered pair; a DAG has no directed closed walk. It need not be transitively closed (so it is **not** being identified with its reachability poset). Two graphs are considered isomorphic exactly when a vertex bijection preserves the binary arc relation, including its direction. In \(C^2\), only two first-order variable names may occur, but counting quantifiers may specify any nonnegative integer. The classification is only for DAGs of order at most six; equivalence is evaluated in the full class of finite binary-relational structures, not with quantifiers restricted to DAGs.

## Proof
**Logical reduction.** On finite loopless DAGs, globally synchronized directed vertex-colour refinement starts with all vertices one colour and replaces each vertex colour by the ordered triple consisting of its previous colour, the multiset of colours of its in-neighbours, and the multiset of colours of its out-neighbours. This is the ordinary \(C^2\) characterisation by directed one-dimensional Weisfeiler–Leman refinement: the diagonal atomic data are fixed, reciprocal arcs cannot occur, and, conditional on colour-class sizes, absent arcs are determined by the two directed neighbour multisets. In particular, two DAGs have the same \(C^2\)-theory exactly when their stable globally synchronized colour multiplicities agree. Different sizes are distinguished by a counting quantifier.

**Exhaustive finite reduction.** Every finite DAG admits a topological labelling \(0,\ldots,n-1\), and every arc then goes from a smaller to a larger label. Therefore the \(2^{\binom n2}\) upper-triangular Boolean arc matrices cover all \(n\)-vertex DAG isomorphism classes. For every matrix, the exact verifier computes globally synchronized directed refinement to stabilization. Within each resulting colour-histogram bucket, it computes the exact number of isomorphism classes by recursively testing all possible colour-preserving vertex bijections, rejecting assignments as soon as either direction of an already exposed arc differs. The colours may be used as a pruning condition because every directed-graph isomorphism preserves every refinement colour. Hence this finite procedure neither misses a DAG nor identifies nonisomorphic DAGs. Its fully specified executable implementation is `verify_dags.py`.

The verified exhaustive outputs are
\[
\begin{array}{c|rrrrrr}
n&1&2&3&4&5&6\\\hline
\text{topological matrices}&1&2&8&64&1024&32768\\
\text{isomorphism classes}&1&2&6&31&302&5984\\
\text{stable refinement histograms}&1&2&6&31&302&5983.
\end{array}
\]
Every histogram bucket contains exactly one isomorphism class except a single bucket at \(n=6\) containing exactly two. This proves the complete assertion by exhaustive finite disjunction, rather than extrapolating from smaller values.

**Explicit collision and its structure.** Let \(A\) consist of two components \(s_i\to m_i\to t_i\) together with \(s_i\to t_i\), for \(i=1,2\). Let \(B\) have the six arcs
\[
s_1\to m_1,\quad s_1\to t_1,\quad m_1\to t_2,\quad
s_2\to m_2,\quad s_2\to t_2,\quad m_2\to t_1.
\]
Both are DAGs. The underlying graph of \(A\) is two disconnected triangles, while that of \(B\) is a connected six-cycle, so they are not isomorphic. For both, the stable directed-refinement classes consist of two sources with degree pair \((0,2)\), two intermediate vertices with degree pair \((1,1)\), and two sinks with degree pair \((2,0)\). Each source has one out-neighbour in each of the other two classes; each intermediate vertex has one in-neighbour in the source class and one out-neighbour in the sink class; each sink has one in-neighbour from each of the first two classes. These equitable quotient data are identical and already stable, proving \(A\equiv_{C^2}B\) independently of the census.

## Verification
Run `python3 verify_dags.py` from a directory containing the embedded files. It uses only the Python standard library and checks all six rows, including the exceptional bucket, by explicit topological enumeration and exact recursive isomorphism. For an independently implemented route, compile `canon_dags.cpp` with a C++17 compiler and run `./canon_dags 6 > canonical_dags.txt`, then run `python3 analyze_canonical.py`; the second route enumerates isomorphism types by minimising a directed adjacency code over every vertex permutation and separately groups their directed-refinement signatures. The two routes report the same numbers; `verification_output.txt` includes actual recorded outputs. The first route examines \(32768\) topological encodings at order six, not an unexplained sample. No graph orders above six are enumerated or claimed.

## Relationship to prior work
The equivalence between \(C^2\) and colour refinement, and a much broader structural criterion for \(C^2\)-identified finite relational structures, are established by Kiefer, Schweitzer and Selman (2015); these are not proposed as new. Arvind, Köbler, Rattan and Verbitsky (2015) study colour-refinement amenability of undirected graphs, not the exact DAG-restricted first failure layer. The classical DAG isomorphism counts \(1,2,6,31,302,5984\) are recorded in OEIS A003087 and are not claimed here. The claim is **only** the sharp six-vertex \(C^2\) threshold, its exact \(5983\)-class count, and the uniqueness and description of the collision inside all DAGs of order six.

## Limitations
The novelty comparison does not exclude an obscure earlier table of directed-DAG refinement classes. The 2015 general relational classification is strong enough to motivate alternative derivations, but it does not supply these order-by-order DAG counts in its inspected theorem and discussion. The finite verification is exhaustive only through six vertices and makes no assertion about larger DAGs, nor does it address higher-dimensional Weisfeiler–Leman refinement, reachability relations, or first-order logic without counting.

## References
1. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (first public version 2015-03-30), especially the introduction and Theorem 27 on finite relational structures. https://arxiv.org/abs/1503.08792
2. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public version 2015-02-04). https://arxiv.org/abs/1502.01255
3. OEIS A003087, *Number of acyclic digraphs with n unlabeled nodes*, including earlier references to R. W. Robinson. https://oeis.org/A003087
4. J. Böker, *Color Refinement, Homomorphisms, and Hypergraphs*, arXiv:1903.12432 (2019), Section 1.1 discussing directed graphs and DAG homomorphism counts. https://arxiv.org/abs/1903.12432
