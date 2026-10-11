# Vertex-uniform independence-complex splitting for the truncated octahedron

## Finding
Let \(G\) be the edge graph of the three-dimensional permutahedron, equivalently the truncated-octahedral graph on \(24\) vertices. For every vertex \(v\in V(G)\), write \(N_G[v]=\{v\}\cup N_G(v)\) for its closed neighborhood. The ordinary independence complexes have integral homotopy types
\[
\operatorname{Ind}(G)\simeq\bigvee^{4}S^{5},\qquad
\operatorname{Ind}(G-v)\simeq\bigvee^{3}S^{5},\qquad
\operatorname{Ind}(G-N_G[v])\simeq S^{4}.
\]
Moreover, for every \(v\), the usual deletion/link homotopy cofibration splits:
\[
\operatorname{Ind}(G)\simeq
\operatorname{Ind}(G-v)\vee\Sigma\operatorname{Ind}(G-N_G[v]).
\]
Here all homotopy equivalences refer to ordinary geometric realizations and integral homotopy types; the last equivalence is not claimed to be canonical.

## Assumptions and scope
A graph is finite and simple. \(\operatorname{Ind}(H)\) is the simplicial complex of all sets of pairwise nonadjacent vertices of \(H\), including the empty simplex. Specify \(V(G)=S_4\) as the \(24\) words \((p_0,p_1,p_2,p_3)\) that permute \((0,1,2,3)\). Two words are adjacent exactly when one results from the other by interchanging entries in consecutive positions \(j,j+1\) for \(j\in\{0,1,2\}\). This is the \(24\)-vertex, \(36\)-edge cubic permutahedral graph. Vertex deletion means induced deletion, not removal of the vertex from an already-built complex. The theorem concerns all \(24\) possible vertices, no extra graph or asymptotic family.

## Proof
**1. Reduction to one vertex.** Relabelling the four values by any permutation \(\sigma\in S_4\) commutes with the operation of swapping adjacent *positions*. Thus the left action of \(S_4\) on permutation words is by graph automorphisms and is transitive. It suffices to determine the three complexes for the lexicographically first word \(v_0=(0,1,2,3)\).

**2. Finite exhaustive discrete-Morse certificates.** The executable `verification/verify_morse.py` independently specifies the full graph from the preceding definition, constructs all independent faces of the induced graph in each of the three cases, and pairs them by the following fully specified matching: iterate allowed vertices in lexicographic index order, and at each vertex \(j\) match each as-yet-unmatched face \(\tau\) not containing \(j\) with \(\tau\cup\{j\}\) when both faces remain unmatched. All such pairs are disjoint. This is a matching on the *augmented* face poset, including the empty face. The program verifies exhaustiveness of the face lists, face condition, disjointness of all pairs, and the critical faces after all stages.

For acyclicity, for every cover relation \(\tau\subset\tau\cup\{j\}\), orient it upwards precisely when it is a matched pair and downwards otherwise. A complete topological sort of this directed Hasse graph visits every face; no acyclicity is inferred from heuristics or from experiments on partial subcomplexes. The exact verified figures are:

| Induced graph | Nonempty simplices | Matched augmented pairs | Directed incidences | Unmatched augmented cells |
|---|---:|---:|---:|---|
| \(G\) | 37075 | 18536 | 219240 | four cells, dimension five |
| \(G-v_0\) | 27940 | 13969 | 162087 | three cells, dimension five |
| \(G-N_G[v_0]\) | 9134 | 4567 | 48018 | one cell, dimension four |

In each case the empty face participates in exactly one pair with a vertex. Restricting the acyclic augmented matching to the ordinary nonempty face poset therefore makes that formerly paired vertex a critical zero-cell, while retaining precisely the listed higher-dimensional critical cells. Deleting the empty face cannot create an oriented cycle. Forman's finite discrete-Morse theorem consequently gives CW homotopy models with just one zero-cell and respectively \(4\) five-cells, \(3\) five-cells, and one four-cell. Since each higher cell is attached to the unique zero-cell, these CW models are respectively \(\bigvee^4 S^5\), \(\bigvee^3 S^5\), and \(S^4\). The argument proves *integral homotopy equivalence*, not merely agreement of homology ranks.

**3. Cofibration and splitting.** Partition independent sets in \(G\) according to whether they contain \(v\). The second portion is the cone \(v*\operatorname{Ind}(G-N_G[v])\), glued to \(\operatorname{Ind}(G-v)\) along its base. Hence \(\operatorname{Ind}(G)\) is the homotopy cofiber of the inclusion \(\operatorname{Ind}(G-N_G[v])\hookrightarrow\operatorname{Ind}(G-v)\). Its domain is homotopy equivalent to \(S^4\) and its target to \(\bigvee^3 S^5\), which is \(4\)-connected. Every map from \(S^4\) to this target is null-homotopic. The cofiber therefore splits as the asserted wedge of the target with the suspension of the domain. Vertex transitivity extends the argument from \(v_0\) to every vertex.

## Verification
Run, using Python 3 and no third-party packages, `python3 verification/verify_morse.py`; it asserts all graph incidences and face-pairing facts, completely checks the oriented Hasse graph for each induced complex, and terminates with `PERMUTOHEDRON_LOCAL_GLOBAL_MORSE_OK`. In particular, the verified topological sorts visit exactly \(37076\), \(27941\) and \(9135\) augmented faces.

Run separately `python3 verification/check_polynomial.py`. This reconstructs the graph using left multiplication (value swaps), checks the graph isomorphism under inversion, and computes independent-set generating polynomials by the vertex-deletion recurrence with memoization. It independently obtains the complete three face vectors and polynomial values at \(-1\) equal to \(4\), \(3\), and \(-1\), corresponding to reduced Euler characteristics \(-4\), \(-3\), and \(1\). This second check is an independent combinatorial cross-check, not a substitute for the complete acyclicity proof.

## Relationship to prior work
Araujo-Pardo, Del Rio-Francos, Lopez-Dudet, Oliveros and Schulte identify the one-skeleton of the permutahedron with the Cayley graph on the symmetric group generated by adjacent transpositions (Lemma 3.3 of *The Graphicahedron*). Their description supplies the canonical geometric graph identification, but no homotopy computation of its independence complex. Barmak's *Star clusters in independence complexes of graphs* develops general independence-complex methods, including suspension results for triangle-free graphs; the relevant hypotheses and conclusions do not supply any of these three exact integral homotopy types or the uniform vertex-local splitting. The permutahedron graph is bipartite, so its ordinary independence complex being a suspension is consistent with that general theorem.

A known exact independence-complex calculation for the *dodecahedral* graph yields four five-spheres, but that graph has \(20\) vertices and is not the \(24\)-vertex truncated octahedron. A graph-metric Rips filtration of a permutahedral metric concerns clique complexes of distance-threshold graphs, not the ordinary independence complex of the adjacent-transposition Cayley graph. Neither statement implies the new vertex-deletion and link classification. Searches under truncated octahedron, permutahedron, adjacent-transposition Cayley graph, complementary clique complex, and vertex-deletion cofibration revealed no coverage; this nonretrieval is not a mathematical proof of priority.

## Limitations
The claimed classification is specific to the \(24\)-vertex truncated-octahedral graph, though uniform across its vertex orbit. No claim is made for all higher-dimensional permutahedra. The proofs rely on exhaustive finite calculations with fully specified, reproducible checks; a simpler hand-derived matching or a general family formula has not been proved. Completeness of literature search cannot exclude equivalent unindexed or unpublished results. Independent scientific review has not been performed.

## References
1. Jonathan Ariel Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first public submission 2010-07-02), primary MSC 57M15; especially the definitions and star-cluster/suspension results.
2. Gabriela Araujo-Pardo, Maria Del Rio-Francos, Mariana Lopez-Dudet, Deborah Oliveros and Egon Schulte, *The Graphicahedron*, arXiv:0910.3908v1, especially Lemma 3.3 and the permutahedral Cayley-graph description.
3. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; acyclic discrete-Morse matching theorem.
