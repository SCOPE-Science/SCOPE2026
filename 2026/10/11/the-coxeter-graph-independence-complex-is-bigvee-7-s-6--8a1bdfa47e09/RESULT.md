# The Coxeter graph independence complex is \(\bigvee^{7}S^{6}\)

## Finding
Let \(\mathbb Z_7\) be the integers modulo seven and let the lines of a Fano plane be
\[
\mathcal L=\bigl\{\{i,i+1,i+3\}:i\in\mathbb Z_7\bigr\}.
\]
Define a graph \(G\) with vertex set \(V=\binom{\mathbb Z_7}{3}\setminus\mathcal L\); distinct vertices are adjacent exactly when their three-element subsets are disjoint. This is the standard Coxeter cubic graph (Foster census F28A), with 28 vertices and 42 edges. Define \(K=\operatorname{Ind}(G)\) as its ordinary simplicial independence complex, so a nonempty set of graph vertices is a face precisely when every two associated triples intersect.

**Theorem.** There is a homotopy equivalence
\[
\operatorname{Ind}(G)\simeq\bigvee^{7}S^{6}.
\]
In particular, \(\widetilde H_6(K;\mathbb Z)\cong\mathbb Z^{7}\) and all other reduced integral homology groups vanish. The underlying simplicial complex is 11-dimensional; the displayed six-dimensional homotopy model results from an exact acyclic discrete-Morse matching, not a homology-only inference.

## Assumptions and scope
The vertex triples are listed in lexicographic order after deleting exactly the seven Fano lines; the least triple has index zero. The graph is **not** the 30-vertex Tutte–Coxeter graph, and \(K\) is **not** a Coxeter complex associated with a reflection group. It is the flag complex of pairwise-intersecting triples among the 28 non-lines, equivalently the independence complex of the indicated induced subgraph of the 35-vertex Kneser graph \(KG(7,3)\). Homotopy and homology are ordinary (unreduced for \(H_0\), reduced otherwise), with the latter taken over \(\mathbb Z\). No general assertion about the 35-vertex parent graph or other Fano-derived graphs is made.

## Proof
**1. Exact finite complex.** Construct the seven Fano lines and the 28 remaining three-element subsets of \(\mathbb Z_7\). Join disjoint triples; the resulting graph has exactly 42 edges and every vertex has degree three. The supplied independent recurrence also verifies girth seven. Encode a subset of the 28 vertices as a 28-bit nonnegative integer. Recursively enumerate its independent subsets by taking the least still-eligible index, first visiting the face already constructed, then adjoining each eligible vertex and deleting its neighbors from the available future indices. Since indices increase strictly along any branch, every independent set is visited exactly once. The enumeration yields 196,009 faces counting the empty face, hence 196,008 nonempty faces. Its independent-set counts by cardinality \(0,1,\ldots,12\) are
\[
(1,28,336,2268,9506,25788,45836,52928,38556,16660,3752,336,14).
\]

**2. Explicit matching.** Initially let \(R\) comprise every independent set, including the empty face. For each vertex index \(v\), put
\[
P_v(R)=\{\sigma\in R:v\notin\sigma,\ \sigma\cup\{v\}\in R\}.
\]
If some \(P_v(R)\) is nonempty, choose the index \(v\) maximizing the ordered pair \((|P_v(R)|,v)\). Match **every** pair \(\sigma\leftrightarrow\sigma\cup\{v\}\) with \(\sigma\in P_v(R)\), then delete both faces of all those pairs from \(R\), and repeat. If no such pair exists, stop. Each move pairs two adjacent ranks in the Boolean face poset, and the removals make all pairs disjoint. This deterministic procedure produces the following pivot-index/pair-count sequence:

```
(27,47134), (21,26060), (15,14014), (8,6444),
(13,2782), (5,1164), (3,382), (26,3), (25,3),
(24,3), (23,3), (18,3), (12,3), (10,3)
```

There are 98,001 such pairs in the augmented complex; the first batch contains the pair \(\varnothing\leftrightarrow\{27\}\). Delete **only this pair** from the matching, discard the empty face, and restore the singleton \(\{27\}\) as unmatched. We obtain 98,000 pairs on the ordinary nonempty-face poset, leaving exactly one critical zero-dimensional simplex and seven critical six-dimensional simplices. The seven latter faces have vertex-index sets

```
(1,6,9,12,14,16,20)
(0,7,11,16,18,19,22)
(0,10,17,18,20,23,24)
(1,4,10,11,17,23,25)
(2,4,10,14,22,24,26)
(6,7,12,18,23,25,26)
(2,9,12,19,24,25,26)
```

**3. Acyclicity certificate.** On the entire Hasse diagram of the 196,008 nonempty faces, orient each unmatched codimension-one incidence from the smaller face toward the larger, and reverse the orientation on every matched incidence. The standalone checker constructs every such incidence, counting 1,319,724 directed edges, and applies a complete Kahn topological sort. All 196,008 vertices are removed, with exactly 1,319,724 directed edges traversed. Thus there is no directed cycle in the oriented Hasse diagram: the matching is acyclic, not merely an experimentally observed gradient. The enumeration and topological-sort assertions are integer-exact and enumerate the **entire** finite complex.

**4. Homotopy consequence.** Forman's acyclic-matching theorem yields a CW complex homotopy equivalent to \(K\), having one zero-cell and precisely seven six-cells, with no critical cells in dimensions one through five. Its five-skeleton is a point, so every attaching map from a five-sphere is null-homotopic. This CW complex is a wedge of seven six-spheres. The conclusion follows.

## Verification
Run `python3 verify_coxeter.py` from the directory containing the embedded files. It reconstructs the graph and all nonempty faces, checks the full matching and every directed incidence, and reports `COXETER_VERIFY_OK` with 196008 nonempty faces, 98000 matched pairs, one critical vertex, seven critical six-cells and 1319724 directed incidences. Run `python3 check_independence_polynomial.py` for an independent computation by deletion–closed-neighborhood recurrence. It verifies the face vector, girth seven, and \(I_G(-1)=-7\). Therefore the Euler characteristic is eight, in agreement with the theorem, but Euler characteristic alone would not establish the homotopy result.

## Relationship to prior work
Barmak [1, Theorem 3.4] establishes that the independence complex of every triangle-free graph is homotopy equivalent to **a suspension**; the theorem does not identify the Coxeter graph's sphere dimension, multiplicity, or attaching data. His exact Kneser result, Theorem 4.11, treats \(KG(2,k)\), not this induced subgraph of \(KG(7,3)\). Feng and Wang [2, Theorem 8 and Table 1] analyze the 35-vertex **full** Kneser graph \(KG(7,3)\), with mod-field homology ranks 29 in degree six and seven in degree nine, and construct a Fano-plane-supported cross-polytopal cycle. Removing the seven line vertices passes to a proper induced subcomplex; homotopy groups and sphere multiplicities of a vertex-deletion subcomplex are not determined by those of its parent. The full-parent table therefore does not imply the result stated here. Dejter [3] describes the Coxeter graph and its 7-cycle/Klein-graph geometry, not its independence-complex homotopy.

## Limitations
The proof is an exhaustive, finite, reproducible acyclic-matching certificate for exactly this 28-vertex graph. It does not give a uniform classification for arbitrary induced subgraphs of Kneser graphs, distinguish equivariant homotopy actions, or establish a general parameter-family theorem. The cited comparisons do not exclude an equivalent result in unindexed or otherwise uninspected literature. The graph identification, graph-specific certificate, and prior-work implications are deliberately separated; no uniqueness of the result is inferred merely from an unsuccessful search.

## References
[1] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418 (first public 2010-07-02; later Advances in Mathematics 241 (2013)); author's full text https://mate.dm.uba.ar/~jbarmak/starclusters.pdf. Original primary mathematics classification 57M15.

[2] Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566, especially Theorem 8 and Table 1; https://arxiv.org/pdf/2404.10566.

[3] I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960, especially the graph description in Section 1; https://arxiv.org/pdf/1002.1960.

[4] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic discrete-Morse matching theorem).
