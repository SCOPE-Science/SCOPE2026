# Equal Betti ranks but distinct Pappus point–flag Rips characters

## Finding
Let \(P\) be the Pappus incidence graph, with eighteen vertices and twenty-seven edges. Put \(L=L(P)\), its twenty-seven-vertex line graph, and use shortest-path distance in each graph separately. Define the inclusive graph-metric Vietoris–Rips complexes
\[
X=\operatorname{VR}_{\le 2}(V(P)),\qquad Y=\operatorname{VR}_{\le 2}(V(L)).
\]
Both have rational reduced homology concentrated in degree two, with \(\widetilde H_2(X;\mathbb Q)\cong\widetilde H_2(Y;\mathbb Q)\cong\mathbb Q^{26}\). Nevertheless, their natural representations of the full graph-automorphism group \(A=\operatorname{Aut}(P)\), of order \(216\), are inequivalent. More precisely, all but twenty-seven automorphisms have equal rational second-homology traces in the two complexes. Of the twenty-seven exceptions, nine bipartition-preserving involutions have traces \((-10,2)\) on \((X,Y)\), while eighteen bipartition-exchanging involutions have traces \((2,-4)\).

The *complete* character table, grouped by automorphism order, whether it exchanges the incidence bipartition, the two traces, and the number of elements, is:

| Order | Exchanges sides | Trace on \(X\) | Trace on \(Y\) | Count |
|---:|:---:|---:|---:|---:|
| 1 | No | 26 | 26 | 1 |
| 2 | No | -10 | 2 | 9 |
| 2 | No | 0 | 0 | 18 |
| 2 | Yes | 2 | -4 | 18 |
| 3 | No | -1 | -1 | 2 |
| 3 | No | 2 | 2 | 12 |
| 3 | No | 5 | 5 | 12 |
| 4 | Yes | 2 | 2 | 18 |
| 6 | No | -1 | -1 | 18 |
| 6 | No | 0 | 0 | 36 |
| 6 | Yes | -1 | -1 | 36 |
| 12 | Yes | -1 | -1 | 36 |

Thus equal ordinary rational Betti numbers do **not** identify the automorphism-equivariant homology of point sampling and incident-flag (edge) sampling of this canonical configuration.

## Assumptions and scope
The graph \(P\) is the standard unweighted cubic bipartite Pappus graph with vertices labeled \(0,\dots,17\) and LCF sequence `(5,7,-7,7,-7,-5)` repeated three times. Its edges consist of the cycle \(i\sim i+1\pmod{18}\) and the nine undirected LCF chords. The line graph \(L(P)\) has one vertex per unordered edge of \(P\), with two line-graph vertices adjacent exactly when the corresponding edges of \(P\) share an endpoint. Each Rips simplex is a nonempty set of vertices whose pairwise shortest-path distances are at most two **in its respective underlying graph**. The action of \(A\) on line-graph vertices is \(\{u,v\}\mapsto\{g(u),g(v)\}\); no identification of the point and flag vertex sets is made. Traces refer to reduced rational homology.

## Proof
**1. Complete finite complexes and rational homology.** Direct distance calculation on the stated finite graphs yields the face vectors
\[
(f_0,f_1,f_2,f_3)(X)=(18,81,108,18),
\]
\[
(f_0,f_1,f_2,f_3,f_4)(Y)=(27,162,270,135,27).
\]
Using the full unsigned simplicial boundary matrices over \(\mathbb F_2\), exact bitset elimination gives successive ranks \((17,64,18)\) for \(X\) and \((26,136,108,27)\) for \(Y\). The resulting ordinary mod-two Betti vectors are \((1,0,26,0)\) and \((1,0,26,0,0)\), respectively. Since integral boundary matrices reduce modulo two, the rank over \(\mathbb Q\) of each boundary matrix is at least its rank modulo two, so the rational Betti dimensions cannot exceed the corresponding mod-two Betti dimensions. Thus every positive rational Betti number outside degree two vanishes. Both face vectors give Euler characteristic \(27\). Connectedness is already certified by boundary rank \(f_0-1\), whence the Euler–Poincaré identity forces rational second Betti number \(26\) in each case. This proves the claimed rational homology assertions without assuming torsion-freeness.

**2. Enumerating every symmetry.** Enumerate all bijections of the eighteen labeled graph vertices that preserve the twenty-seven undirected edges. The exhaustive graph-isomorphism backtracking in the verifier returns exactly \(216\) such bijections. The induced edge maps are then explicit bijections of the twenty-seven vertices of \(L(P)\). Every such bijection preserves graph distance and therefore acts simplicially on the appropriate Rips complex. For each automorphism, enumerate its cycles to obtain its order and compare the image of vertex zero with the fixed bipartition coloring to decide whether it exchanges sides.

**3. Exact homological traces.** For an automorphism \(g\) acting simplicially on a finite complex \(Z\), and a nonempty invariant simplex \(\sigma\), let \(\epsilon(g,\sigma)\in\{1,-1\}\) be the sign of the permutation of the vertices of \(\sigma\) under \(g\), in the fixed lexicographic orientation. The reduced simplicial Lefschetz identity gives
\[
\sum_j(-1)^j\operatorname{tr}\bigl(g\mid\widetilde H_j(Z;\mathbb Q)\bigr)
=-1+\sum_{\substack{\sigma\ne\varnothing\\g\sigma=\sigma}}(-1)^{|\sigma|-1}\epsilon(g,\sigma).
\]
Since the only nonzero reduced rational homology in either complex is degree two, this quantity equals precisely the trace on \(\widetilde H_2\). The complete simplex lists and all \(216\) automorphisms permit exhaustive evaluation of this finite signed sum; the twelve distinct order/side/trace combinations and their cardinalities are those in the table. The counts sum to \(216\). Exactly twenty-seven elements have unequal traces, with the specified decomposition into nine side-preserving and eighteen side-exchanging involutions. Equal finite-dimensional rational group representations must have equal characters. Therefore these two twenty-six-dimensional representations are inequivalent.

## Verification
The accompanying `verify.py` reconstructs both metric graphs, enumerates every Rips simplex, computes the exact mod-two boundary ranks, exhaustively enumerates all graph automorphisms, and evaluates signed reduced Lefschetz sums on each complex. Assertions match both face vectors, all boundary ranks and Betti vectors, all twelve character groups, and the count of exactly twenty-seven distinguishing elements. The script requires Python 3 and NetworkX 3.6.1 (`requirements.txt`). Execute `python verify.py`. The complete successful standard output is supplied as `verify.out`. In particular the final line is `VERIFY_OK_PAPPUS_POINT_FLAG_RIPS_CHARACTERS`.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (2011), especially the discussion of line graphs and clique constructions, concerns the radius-one clique complex of the line graph and general graph powers; its line-graph identity does not identify the radius-two metric Rips complex of a line graph with that of the original graph. The published *Complete Rips homotopy and persistence of the Pappus graph* and *Complete graph-metric Vietoris–Rips filtration of the Pappus graph* classify the original **eighteen-point** radius-two complex, including its twenty-six sphere summands, but their full results do not give the \(216\)-element equivariant character or the twenty-seven-edge line-graph complex. Neither ordinary Betti ranks nor an ordinary wedge-of-spheres classification determines the two characters. More distant computations on Pappus matching, independence, or intrinsic Čech complexes concern different functors. The novelty claimed here is solely the complete point-versus-flag equivariant character distinction; neither the known twenty-six-sphere homotopy type of the point complex nor standard Lefschetz theory is claimed new.

## Limitations
The proof concerns the standard unweighted Pappus graph and the two inclusive integer-scale radius-two constructions. It establishes the rational representation characters and distinguishes them; it does **not** assert that the flag complex has the same integral homotopy type as the point complex, prove vanishing of integral torsion, or classify equivariant maps between them. Exhaustive calculations are proofs for this explicitly finite instance, not a universal theorem for incidence graphs. Bibliographic comparison is bounded; equivalent unindexed or differently phrased equivariant computations remain possible, notwithstanding inspection of the closest accessible same-graph full texts. There has been no independent external mathematical audit.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public posting 2011-04-03. https://arxiv.org/abs/1104.0433.
2. *Complete Rips homotopy and persistence of the Pappus graph* (public research record, 2026), full scientific result: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-complete-rips-homotopy-and-persistence-of-the-pappus-graph--eaf5944a94f8/RESULT.md.
3. *Complete graph-metric Vietoris–Rips filtration of the Pappus graph* (public research record, 2026), full scientific result: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-pappus-gra--4d3507a898b5/RESULT.md.
4. E. W. Weisstein, *Pappus Graph*, MathWorld, for the standard LCF encoding. https://mathworld.wolfram.com/PappusGraph.html.
