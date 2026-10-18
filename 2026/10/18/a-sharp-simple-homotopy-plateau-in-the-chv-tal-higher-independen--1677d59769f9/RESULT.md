# A sharp simple-homotopy plateau in the Chvátal higher-independence filtration

## Finding

Let \(G\) be the twelve-vertex, four-regular, triangle-free Chvátal graph, and let \(\operatorname{Ind}_r(G)\) consist of graph-vertex subsets whose induced connected components have at most \(r\) vertices. The canonical inclusion for thresholds two and three is a **simple-homotopy equivalence**, realized by an actual simplicial collapse:

\[
\boxed{\operatorname{Ind}_3(G)\searrow\operatorname{Ind}_2(G)\simeq S^3.}
\]

There are exactly 152 explicit elementary face/coface removals in this collapse. The plateau is sharp: the neighboring Euler characteristics are
\[
\chi(\operatorname{Ind}_1(G))=2,\quad
\chi(\operatorname{Ind}_2(G))=\chi(\operatorname{Ind}_3(G))=0,\quad
\chi(\operatorname{Ind}_4(G))=-63.
\]
Consequently neither neighboring natural inclusion can be a homotopy equivalence. The homotopy statement is integral, not merely a rational or finite-field homology calculation.

## Assumptions and scope

The graph has vertices numbered \(0,1,\ldots,11\) and exactly these undirected edges, each ordered with its smaller endpoint first:

```
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

Each vertex has degree four and no edge has a common neighbor, proving regularity and triangle-freeness directly. This is the standard Chvátal graph, the smallest graph simultaneously four-regular, triangle-free and four-chromatic (the chromatic fact is a classical external characterization, not needed for the homotopy proof).

For each integer \(r\ge1\), a nonempty subset is a face of \(\operatorname{Ind}_r(G)\) exactly when every connected component of its induced subgraph contains at most \(r\) vertices. All face posets and collapses below use nonempty faces; the empty face is present as usual in the abstract simplicial complexes.

## Proof

**Exact complex construction.** Enumerate all \(2^{12}=4096\) masks of graph vertices. Use a complete flood-fill on each induced subgraph to test its component sizes. For the second stage independently check that its maximum induced degree is at most one; the two conditions coincide for any graph. The full face vectors (dimensions from zero upwards) for thresholds one through four are

\[
\begin{array}{c|l}
 r & (f_0,f_1,\ldots)\\\hline
 1&(12,42,52,20)\\
 2&(12,66,148,142,52,4)\\
 3&(12,66,220,282,132,16)\\
 4&(12,66,220,495,324,58).
\end{array}
\]

The corresponding counts of nonempty simplices are \(126,424,728,1175\), and their alternating face sums yield the stated Euler characteristics.

**Integral sphere at threshold two.** On the \(424\) nonempty simplices of \(\operatorname{Ind}_2(G)\), sequentially process pivot vertices in order \(11,10,\ldots,0\), pairing each still-unmatched face not containing the pivot with its one-vertex extension when both are still unmatched. Exactly \(211\) pairs are formed. The two unmatched faces have dimensions zero and three, respectively. Orient matched cover incidences from the larger to smaller face, all other cover incidences the opposite way; an exhaustive topological sort consumes every one of the \(424\) faces across all \(1428\) cover incidences. Hence the matching is acyclic. The integral discrete-Morse reduction is a CW complex with exactly one \(0\)-cell and one \(3\)-cell, attached necessarily by the unique attaching map from a two-sphere to a point. Thus \(\operatorname{Ind}_2(G)\simeq S^3\) integrally.

**Actual relative collapse.** Start with all \(728\) nonempty simplices of \(\operatorname{Ind}_3(G)\), keeping the \(424\) simplices of \(\operatorname{Ind}_2(G)\) as an immutable target. In each step inspect the remaining extra faces by increasing cardinality and bitmask order; choose the first extra face having exactly one codimension-one coface left, provided that coface is also extra. Such a face is globally free: every larger coface would contain a codimension-one intermediate coface, contradicting uniqueness. Remove the face and its unique coface. The attached verifier constructs, stores temporarily and replays this complete sequence; it terminates with **exactly 152 pairs**, no extra faces and precisely the target complex. Each operation is a legal elementary simplicial collapse. Therefore the canonical inclusion \(\operatorname{Ind}_2(G)\hookrightarrow\operatorname{Ind}_3(G)\) is a simple-homotopy equivalence, proving the displayed plateau.

**Sharpness.** The alternating face counts show \(2\ne0\) between thresholds one and two and \(0\ne-63\) between thresholds three and four. Since homotopy equivalences preserve Euler characteristic, the plateau cannot extend to either adjacent threshold. Independently, exact mod-two simplicial boundary elimination gives one connected component and one degree-three Betti class, and no others, at thresholds two and three, consistent with the integral proof.

## Verification

Execute `python3 verify_chvatal_plateau.py` using Python 3.10 or later, with only standard-library dependencies. The program reconstructs the complete graph from the explicit edge list, checks four stages by exhaustive induced-component testing, independently checks the degree characterization of stage two on every mask, computes all face vectors and boundary ranks over \(\mathbb F_2\), verifies a complete acyclic matching, constructs all 152 legal relative free-face collapses, and confirms the two Euler-characteristic obstructions. Successful execution prints `CHVATAL_IND2_IND3_SHARP_SIMPLE_HOMOTOPY_PLATEAU_VERIFIED`.

## Relationship to prior work

Deshpande and Singh [1] establish higher-independence constructions and homotopy classifications for several graph families, but do not classify this nonchordal four-regular graph. Abdelmalek et al. [2] prove shellability or decomposability statements for chordal, tree and caterpillar settings; these do not include the Chvátal graph. The primary texts were compared at definitions and applicable stated graph families.

The complete published same-graph result [3] proves \(\operatorname{Ind}_1(G)\simeq S^2\) and classifies its vertex deletions and links, but does **not** classify the two- and three-independence complexes or their natural inclusion. A separate published comparison [4] identifies an equivariant collapse of this ordinary independence complex onto the **open-neighborhood** complex, a different subcomplex of the first threshold. Both same-graph full result texts were inspected, including their definitions and proofs. Neither yields the 152-pair collapse here, and neither implies the integral sphere at threshold two. The existence of an unindexed equivalent result cannot be ruled out by search.

## Limitations

The exact simple-homotopy plateau and its Euler-characteristic sharpness are proven only for this explicitly labeled Chvátal graph. The result does not determine full higher-threshold homotopy types, equivariant action, or a general theorem for arbitrary four-chromatic graphs. Computational checks are complete for the stated twelve-vertex finite graph only.

## References

[1] P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (first public submission 2020-01-15), https://arxiv.org/abs/2001.05448 .

[2] F. M. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1 (first public submission 2021-06-21), https://arxiv.org/abs/2106.10863 .

[3] *The Chvátal graph independence complex and its vertex-deletion dichotomy*, published full result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-chv-tal-graph-independence-complex-and-its-vertex-deletion-d--676b14391238 .

[4] *An equivariant collapse connecting the Chvátal independence and neighborhood complexes*, published full result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-equivariant-collapse-connecting-the-chv-tal-independence-and--3077dabdf181 .

[5] V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory 9 (1970), 93–94. DOI:10.1016/S0021-9800(70)80057-6 .
