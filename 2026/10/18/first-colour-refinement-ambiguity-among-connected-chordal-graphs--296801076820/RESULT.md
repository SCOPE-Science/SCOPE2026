# First colour-refinement ambiguity among connected chordal graphs occurs at eight vertices

## Finding
Consider finite, uncoloured, connected, simple chordal graphs and ordinary vertex colour refinement (one-dimensional Weisfeiler–Leman refinement), initially with a single vertex colour. Two graphs are **refinement-equivalent** when simultaneous refinement on their disjoint union yields equal multisets of stable vertex colours; equivalently, they satisfy the same sentences of two-variable first-order counting logic \(C^2\).

**Theorem (first ambiguity and complete first layer).** No two nonisomorphic connected chordal graphs with at most seven vertices are refinement-equivalent. Among the \(1614\) isomorphism types of connected chordal graphs on eight vertices, precisely two refinement-equivalence classes contain more than one isomorphism type, and each such class contains exactly two. Thus the minimum order of a refinement-equivalent nonisomorphic connected chordal pair is \(8\), and there are exactly two unordered pairs at that order.

The pairs have distinct edge counts, \(13\) and \(14\). For the \(13\)-edge pair, the common degree-cell sizes, in ascending order of degree \(2,4,5\), are \((4,2,2)\), with equitable quotient
\[
 Q_{13}=\begin{pmatrix}0&1&1\\2&0&2\\2&2&1\end{pmatrix}.
\]
For the \(14\)-edge pair, the degree-cell sizes, in ascending order of degree \(2,5\), are \((4,4)\), with quotient
\[
 Q_{14}=\begin{pmatrix}0&2\\2&3\end{pmatrix}.
\]
For each pair the degree partition is already equitable and hence is its stable refinement partition.

## Assumptions and scope
A graph is chordal if every cycle of length at least four has a chord. The colour-refinement update gives each vertex a fresh colour encoding its previous colour and the multiset of previous colours of its neighbours, with shared colour names across all graphs being compared. A partition is *equitable* when every vertex in a cell has the same number of neighbours in each cell. The theorem concerns uniqueness **within the class of connected chordal graphs**, not identification among all finite graphs. Isomorphism and equivalence refer to unlabelled graphs, not to separately coloured or rooted graphs. The exhaustive census is finite (orders \(1\) through \(8\)), not an asymptotic theorem.

## Proof
**Constructing the two pairs.** Start with a four-vertex core. Add four new independent vertices, each adjacent exactly to the endpoints of one selected core edge; repeated selections are allowed. Each added vertex is simplicial, so the resulting graph is chordal and connected.

For the \(14\)-edge pair the core is \(K_4\). In the first member choose the four selected edges to form a cycle on the four core vertices. In the second choose two disjoint edges of a perfect matching, each with multiplicity two. Every core vertex acquires two added neighbours; the four core degrees become \(5\) and every added vertex has degree \(2\). The two graphs have the displayed quotient \(Q_{14}\), and refinement cannot split either degree cell. They are not isomorphic: the four degree-two vertices have pairwise different open neighbourhoods in the cycle construction, whereas the doubled-matching construction has two repeated neighbourhoods (two twin pairs).

For the \(13\)-edge pair the core is \(K_4\) minus one edge. Its two vertices of core degree two and two of core degree three induce four cross edges, forming a \(K_{2,2}\). In the first member select all four cross edges once. In the second select two disjoint cross edges twice each. The two core-degree-two vertices acquire degree \(4\); the two core-degree-three vertices acquire degree \(5\). Every added vertex has degree \(2\). The quotient is \(Q_{13}\), equal in both graphs, and the same distinct-neighbourhood versus repeated-neighbourhood argument proves nonisomorphism.

**Completeness of the first layer (finite exhaustive certificate).** The supplied standalone checker in `artifacts/verify.py` performs the following finite enumeration and exact decisions; all loops, criteria and data sources appear in that file.

1. NetworkX's unlabelled graph atlas supplies all simple graph isomorphism types on at most seven vertices. Connectedness and chordality filtering produces, at orders \(1,\ldots,7\), the respective counts \(1,1,2,5,15,58,272\).
2. Every connected chordal graph on at least two vertices has a simplicial vertex whose deletion leaves a connected chordal graph. Indeed, any simplicial vertex has a clique as its neighbourhood: a path passing through it can replace its two incident edges by the edge between its neighbours; the deletion remains connected. The standard perfect-elimination characterization guarantees existence. Therefore, every connected chordal eight-vertex graph arises by adjoining one vertex whose nonempty neighbourhood is a clique of some seven-vertex connected chordal graph. Conversely, such an attachment always preserves connectedness and chordality. The checker enumerates every such clique-neighbourhood attachment (\(7268\) candidates including duplicates).
3. Each candidate is deduplicated up to exact graph isomorphism. A Weisfeiler–Leman hash groups potential isomorphs to accelerate comparisons; this hash is isomorphism-invariant, and every candidate sharing a hash with an existing representative is tested with `networkx.is_isomorphic`. The resulting number of isomorphism types is exactly \(1614\), agreeing with Brendan McKay's independently published count for connected chordal eight-vertex graphs.
4. Across all retained graphs of orders at most eight, the checker recomputes simultaneous vertex-refinement colours by *exact interning* of the complete previous-colour/neighbour-multiset tuples, not by numerical hashing. Their vertex-colour partition is checked to stabilize. At stability there are no collisions between distinct isomorphism types in orders at most seven and exactly two classes of size two at order eight; all remaining eight-vertex classes have size one. For each ambiguous pair the checker verifies nonisomorphism, chordality, identical degree-cell quotients and the stated open-neighbourhood data.

The construction step gives existence, while the exhaustive generation plus stable-colour comparison gives the minimality and exact two-pair count. The finite enumerative portion is a reproducible computer-assisted proof conditional on the standard graph-atlas and graph-isomorphism implementations; it is not claimed to be a purely handwritten classification of \(1614\) objects.

## Verification
From a directory containing this package, with Python 3.10+ and NetworkX 3.5+ installed, run `python artifacts/verify.py`. The verifier uses only the bundled code and NetworkX's built-in graph atlas. It checks the complete \(n\le 7\) counts, \(7268\) clique-attachment attempts, \(1614\) eight-vertex representatives, the two ambiguous pair sizes \((2,2)\), graph nonisomorphism and the explicit quotient matrices. Its final line is `VERIFICATION_PASS: 1-WL ambiguities are precisely two unordered pairs on eight vertices.` The graph enumeration is cross-checked against the independent public count, but the external graph6 archive is not a required code input.

## Relationship to prior work
Kiefer–Schweitzer–Selman's *Graphs Identified by Logics with Counting* (first public 2015) classifies when a general finite graph is identified by \(C^2\); Arvind–Köbler–Rattan–Verbitsky's *Graph Isomorphism, Color Refinement, and Compactness* (first public 2015) independently characterizes amenability. These broader structural characterizations explain the conceptual equivalence between counting logic and colour refinement but do not explicitly furnish the connected-chordal minimal order and complete four-graph first ambiguity layer. McKay's connected-chordal table supplies the count \(1614\) and graph data, but does not tabulate colour-refinement equivalence classes. The new contribution is the restricted extremal threshold, exact multiplicities, and explicit structures of the first two collisions, not the general \(C^2\) characterization nor a new chordal-enumeration algorithm.

## Limitations
No classification is asserted for chordal graphs beyond eight vertices, disconnected chordal graphs, coloured graphs, higher-dimensional Weisfeiler–Leman algorithms, or graph equivalence against arbitrary nonchordal competitors. The exact exhaustive count relies on NetworkX's unlabelled atlas, graph isomorphism and chordality routines, with an independent catalogue count as corroboration rather than independent re-enumeration of all edge sets. A broader prior characterization may permit recovery of this small-order census through extra casework; the precise finite table has not been claimed here as a publication-priority certificate. Independent mathematical audit has not been performed.

## References
- S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first submitted 2015-03-30. https://arxiv.org/abs/1503.08792
- V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first submitted 2015-02-04. https://arxiv.org/abs/1502.01255
- O. Pikhurko, O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865, first submitted 2010-03-25. https://arxiv.org/abs/1003.4865
- B. D. McKay, *Combinatorial Data: Graphs*, connected chordal graphs (eight vertices: \(1614\)). https://users.cecs.anu.edu.au/~bdm/data/graphs.html
- NetworkX, graph atlas, chordality, exact graph isomorphism, and graph hashing algorithms, version 3.6.1 for the reported computation. https://networkx.org/
