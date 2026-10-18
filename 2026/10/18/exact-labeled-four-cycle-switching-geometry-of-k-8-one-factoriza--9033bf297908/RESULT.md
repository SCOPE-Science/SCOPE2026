# Exact labeled four-cycle switching geometry of \(K_8\) one-factorizations

## Finding

Fix the eight vertex labels \(V=\{0,1,\ldots,7\}\). A one-factorization is an *unordered* set of seven disjoint perfect matchings partitioning all 28 edges of the complete graph \(K_8\). Thus matchings (rounds) are not named, but vertices (teams) are named. Let \(R\) have one vertex per such one-factorization. Join distinct factorizations when two of their matchings form two disjoint alternating four-cycles and swapping their two matching colors on either one of those cycles converts one factorization into the other. This is a simple, unlabeled-color, **vertex-labeled** switching graph.

The graph \(R\) has precisely \(6240\) vertices and \(17640\) edges, with degree multiplicities
\[
\begin{array}{c|rrrrrr}
 d&0&3&7&9&13&21\\\hline
 \#\{F:\deg_R(F)=d\}&960&1680&2520&420&630&30.
\end{array}
\]
There are exactly \(961\) connected components: \(960\) isolated vertices and one component of size \(5280\). The nontrivial component has radius \(9\), diameter \(11\), and complete eccentricity multiplicities
\[
\#\{F:\operatorname{ecc}(F)=9\}=30,\qquad
\#\{F:\operatorname{ecc}(F)=10\}=3570,\qquad
\#\{F:\operatorname{ecc}(F)=11\}=1680.
\]
The \(960\) isolated vertices are exactly the perfect one-factorizations (those in which each pair of factors forms an alternating Hamiltonian eight-cycle); this characterization of isolated states is **known** from earlier work, not claimed here. The contribution is the exact *vertex-labeled* switching graph, including connectivity of its \(5280\)-state component and its distance and degree profiles.

## Assumptions and scope

The only graph considered is the complete simple graph on eight *distinguishable* vertices. A one-factor is an unordered set of four disjoint edges spanning all vertices. A factorization is an unordered set of seven one-factors; global permutation of one-factor/color names is identified, but relabeling vertices is **not** allowed. A legal move exchanges the two factor colors on exactly one four-cycle in their union. Since two disjoint perfect matchings on eight vertices produce a union of disjoint alternating cycles of length at least four, a nontrivial move exists precisely for pairs whose union is two four-cycles. Switching either of these two cycles yields the same unordered factorization. Adjacency is between distinct states and duplicate moves count only once.

Distances and eccentricities are ordinary unweighted shortest-path graph distances within each connected component. Radius and diameter stated above refer **only** to the unique non-singleton component; there are no finite paths between different components.

## Proof

**1. Complete canonical state enumeration.** Encode the 28 edges in lexicographic order as bits numbered \(0\) through \(27\). A perfect matching is the bitmask of four pairwise vertex-disjoint edges covering all eight vertices. To generate every such matching exactly once, pair the least as-yet-unmatched vertex with each possible partner and recurse. This generates \(7\cdot5\cdot3\cdot1=105\) distinct matchings.

For a partial factorization whose edge union has mask \(U\), take the least uncovered edge \(e\). Branch over every perfect matching \(M\) containing \(e\) and disjoint from \(U\), then replace \(U\) by \(U\cup M\). If all 28 edges are covered, record the seven matching masks in increasing order. This enumeration neither misses nor duplicates a factorization: in any completed factorization exactly one of its remaining factors contains the canonical edge \(e\), determining the next branch uniquely; after its selection apply induction to the residual edge set. The complete recursion enumerates exactly \(6240\) distinct states. A separate team-zero-anchored recursion cross-checks this count: color classes are indexed during construction by the opponent of team zero, so they are not counted again under round permutations.

**2. Exact switching graph.** In a factorization \(F\), take every pair of its seven matching masks \((A,B)\). Their union is an eight-cycle or two disjoint four-cycles; there are no other possible cycle decompositions. Only the second case yields a distinct switch, and the two ways of choosing a cycle give the same unordered replacement \((A',B')\). Form \(F'=(F\setminus\{A,B\})\cup\{A',B'\}\) and look up its unique canonical index. Deduplicating the resulting index pairs constructs *exactly* the graph \(R\), not a subgraph or an approximate sample. Both independent programs construct the same ordered \(17,640\)-edge list from distinct independent state enumerators and independent switch detection methods.

**3. Finite graph certificate.** The attached `factorization_states.txt` contains all \(6240\) lexicographically ordered seven-mask configurations, one per line, using seven-digit lowercase hex encodings per factor. The attached `fourcycle_edges.txt` contains all \(17640\) edges \(i<j\), with zero-based indices into that state list. Its SHA-256 is `278543195bffe9e837bb1ed4358cc87cabb4b2ac7929b06a24e6c4bcbc253c4a`. The states-file SHA-256 is `544c02ebaa1e834f533f4e04aa3b8524b517d46fbc5900c8d72d43e70e36e9f3`. The programs assert undirected symmetry, enumerate every connected component by graph traversal, and perform breadth-first search from *each* of the \(5280\) non-isolated vertices. The resulting exact degree, component, and eccentricity counts are precisely the numbers in the Finding. Every connected pair has an explicitly constructed shortest path of length at most \(11\), while the \(1680\) vertices of eccentricity \(11\) witness that no smaller diameter suffices.

The finite enumeration is exhaustive for this **one eight-vertex graph**; no extrapolation to an arbitrary order is used.

## Verification

Run either `python3 verify_matchings.py .` in a writable directory or `python3 verify_coloring.py` with standard-library Python 3.10 or later. The first program enumerates perfect matchings then covers the first unused edge in each recursion, detects two-component pairs by union-graph traversal, writes the ordered state and edge certificates, and runs full-source breadth-first searches. The second program instead enumerates colorings by forcing the seven partners of fixed vertex zero to index the seven factors, detects valid switches by scanning all four-vertex subsets, and recomputes components and every eccentricity.

Their standard outputs are in `verify_matchings.output` and `verify_coloring.output`; they are byte-identical, including both ordered certificate hashes. The finite certificate is fully contained in this package and is not an external computational assumption. The complete runs are bounded finite computations (not informal random search or a timeout inference). No computer-assistant proof or independent scientific referee assessment is claimed.

## Relationship to prior work

Kaski, de Souza Medeiros, Östergård and Wanless (2014), DOI 10.37236/3606, introduced factor switching, vertex switching, and their shared four-cycle move, and computed a switch graph \(G^i_8\) on the **six isomorphism classes** of factorizations (vertex labels identified); their Table 1 has two components, one isolated perfect factorization and five other classes connected. They also proved that perfect one-factorizations have no factor-switch moves. These are prior results. The known enumeration of \(6240\) vertex-labeled factorizations is in OEIS A000438 and earlier literature.

Crucially, quotient connectivity under arbitrary permutations of graph vertices does *not* imply connectivity of all **fixed-label** representatives: a path in the six-class quotient may lift to a path ending at a relabelled, rather than the requested, factorization. Likewise the six-class quotient does not yield the \(5280\)-state diameter \(11\), eccentricity multiplicities, or degree profile. The exact labeled graph and its full distances are the retained claim. They quantify the number of four-cycle schedule edits needed when the participants' identities cannot be permuted.

## Limitations

The statement is finite and only concerns eight distinguishable vertices, unordered rounds, and single alternating four-cycle switches. It does not classify switching for orders ten or above and does not imply connectivity across the \(960\) isolated perfect factorizations. The published isomorphism-class graph and perfect-factorization isolation must not be mistaken for new results. Unindexed calculations of the full labeled switch graph or ancillary data not retrieved could overlap the finite statistics. Exact finite verification is not independent external validation of publication priority.

## References

1. P. Kaski, A. de Souza Medeiros, P. R. J. Östergård, and I. M. Wanless, *Switching in One-Factorisations of Complete Graphs*, Electronic Journal of Combinatorics **21**(2), #P2.49 (2014), DOI: `10.37236/3606`. Public full text: `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p49/pdf/`, published 2014-06-09. See Sections 3, 6, and 8, especially Table 1.
2. OEIS A000438, *Number of 1-factorizations of complete graph on \(2n\) vertices*: `https://oeis.org/A000438`. This records the known count of 6240 for \(K_8\).
