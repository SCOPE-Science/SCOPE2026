# The Heawood independence complex is \(\bigvee^{6}S^{3}\)
## Finding
Let \(H\) be the Heawood graph, realized as the point-line incidence graph of the Fano plane with points \(p_i\) and lines \(\ell_i\) for \(i\in\mathbb Z/7\mathbb Z\), where \(p_j\) is adjacent to \(\ell_i\) exactly when \(j-i\in\{0,1,3\}\). Then
\[
\operatorname{Ind}(H)\simeq\bigvee^{6}S^{3}.
\]

## Assumptions and scope
The independence complex contains one simplex for every independent vertex set of \(H\), including the empty simplex in its face poset. The graph is fixed to the 14-vertex Heawood graph. No statement is made for other incidence graphs, other projective planes, or all cubic bipartite graphs.

## Proof
Order the vertices as \(p_0,p_1,\ldots,p_6,\ell_0,\ell_1,\ldots,\ell_6\). Apply the standard sequential face-poset matching: at each pivot vertex \(v\), among faces still unmatched, pair every face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever that enlarged face is still unmatched. The least pivot at which a matched edge changes gives the usual acyclicity argument for this lexicographic matching; the complete oriented Hasse diagram is also checked directly in `verify.py`.

Exhaustive enumeration gives 458 faces including the empty face, with independent-set counts by cardinality
\[
(1,14,70,154,147,56,14,2).
\]
The matching pairs every face except the following six four-vertex independent sets:
\[
\begin{aligned}
&\{\ell_0,\ell_2,\ell_3,\ell_4\},\quad
\{\ell_0,\ell_1,\ell_3,\ell_5\},\quad
\{\ell_0,\ell_1,\ell_4,\ell_5\},\\
&\{\ell_0,\ell_2,\ell_3,\ell_6\},\quad
\{\ell_0,\ell_2,\ell_4,\ell_6\},\quad
\{\ell_0,\ell_1,\ell_5,\ell_6\}.
\end{aligned}
\]
Thus the only critical simplices have dimension \(3\); the empty face is matched. Discrete Morse theory therefore gives a CW complex with one additional \(0\)-cell and exactly six \(3\)-cells, and no cells in dimensions \(1\) or \(2\). Every attaching map of a \(3\)-cell lands in the single \(0\)-cell, hence is null. The resulting CW complex is \(\bigvee^{6}S^{3}\).

## Verification
`verify.py` reconstructs the graph from the Fano incidence rule, enumerates all \(2^{14}\) vertex subsets, confirms the published independent-set counts, constructs the complete matching, topologically sorts the oriented Hasse graph to verify acyclicity, and independently computes simplicial homology over \(\mathbb F_2\). The boundary ranks are \((13,57,97,44,12,2)\), giving Betti numbers \((1,0,0,6,0,0,0)\). A successful replay ends with `HEAWOOD_INDEPENDENCE_VERIFY_OK`.

## Relationship to prior work
Perarnau and Perkins identify the Heawood graph as the extremal cubic girth-six graph for the independence polynomial and explicitly give the same cardinality counts \((1,14,70,154,147,56,14,2)\); that enumerative result does not determine the homotopy type. Nilakantan and Shukla determine the homotopy type for the cyclic-neighborhood regular-bipartite family \(G_m^d\). Their 14-vertex cubic member \(G_7^3\) has a four-cycle, for example \(a_0-b_0-a_6-b_1-a_0\), while the Heawood graph has girth six, so their family theorem does not specialize to the present graph. Tsukuda gives a general incidence-graph/Alexander-dual equivalence, which is a structural reduction rather than an evaluated Heawood homotopy type in the material inspected.

## Limitations
This is a single-graph homotopy classification. It does not classify independence complexes of projective-plane incidence graphs for general order. The originality comparison is limited to the explicit sources and semantic searches recorded in `AUDIT.json`; differently phrased or unindexed literature remains a residual risk.

## References
- G. Perarnau and W. Perkins, *Counting independent sets in cubic graphs of given girth*, arXiv:1611.01474v1, first submitted 2016-11-04.
- N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789v1, first submitted 2017-09-14.
- S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), DOI:10.55016/ojs/cdm.v12i1.62277.
