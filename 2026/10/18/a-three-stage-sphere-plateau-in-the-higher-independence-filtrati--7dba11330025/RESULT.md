# A three-stage sphere plateau in the higher-independence filtration of the Grötzsch graph

## Finding
Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph, and write \(I_r=\operatorname{Ind}_r(G)\) for the simplicial complex of vertex subsets whose induced connected components have at most \(r\) vertices. The **stagewise integral homotopy classification and inclusion-level plateau** are
\[
I_3\searrow I_2\searrow I_1\simeq S^2,
\]
where the two actual simplicial collapses use, respectively, \(90\) and \(105\) free-face pairs. For \(4\le r\le10\),
\[
I_r\simeq\bigvee^{b_r}S^{r-1},\qquad
(b_4,b_5,b_6,b_7,b_8,b_9,b_{10})=(59,151,175,115,45,10,1).
\]
The complex \(I_r\) is contractible for \(r\ge11\). In particular, the persistent integral reduced homology of the inclusions \(I_1\subseteq I_2\subseteq\cdots\) consists of one degree-two generator persisting through stages \(1,2,3\), and \(b_r\) generators in degree \(r-1\) supported at exactly stage \(r\), for each \(4\le r\le10\). No other reduced integral groups occur, and no torsion occurs. The previously established \(I_1\simeq S^2\) is an input/baseline, not asserted to be new.

## Assumptions and scope
The graph is finite, simple and undirected. Number its eleven vertices \(0,\ldots,10\): original cycle vertices \(0,\ldots,4\), clone vertices \(5,\ldots,9\), and the new apex \(10\). For each \(i\in\{0,\ldots,4\}\), with \(j=i+1\pmod5\), put edges \(\{i,j\},\{i,j+5\},\{i+5,j\},\{i+5,10\}\). Repeated edges, if any, are identified. This specifies the familiar Mycielski construction on a five-cycle and yields exactly twenty edges. For each integer \(r\ge1\), a subset \(\sigma\) is a face of \(I_r\) if the maximum cardinality of a connected component of \(G[\sigma]\) is at most \(r\); the empty subset is included. All homotopy equivalences are nonequivariant and integral (they are statements about spaces, not only field-valued homology).

## Proof
**(1) Complete face determination.** Enumerate the \(2^{11}=2048\) vertex masks. The component-size criterion is decidable independently by graph flood fill and by union-find on the induced edge set. Both methods agree on every mask. For \(r=1,\ldots,11\), the exact face counts **including the empty face** are
\[
(103,313,493,763,1135,1521,1821,1981,2036,2047,2048).
\]
The checker also verifies closure under taking faces and the twenty-edge graph presentation.

**(2) The two natural inclusion maps.** The files `gr_collapse_2_3.json` and `gr_collapse_1_2.json` give ordered, zero-based bitmask pairs \((\sigma,\tau)\) of codimension-one faces. Starting from \(I_3\), each of the ninety pairs removes a face \(\sigma\) contained in exactly one current immediate coface \(\tau\). The remaining face set is **exactly** \(I_2\). Starting from \(I_2\), 105 further such elementary simplicial collapses leave **exactly** \(I_1\). The verifier independently recomputes all face sets and tests the uniqueness of each coface at the moment of removal. Hence \(I_1\hookrightarrow I_2\hookrightarrow I_3\) consists of simple-homotopy equivalences and induces integral homology isomorphisms.

**(3) Acyclic matchings at every sphere stage.** For each \(r\in\{1,4,5,6,7,8,9,10\}\), apply the sequential element matchings to its complete augmented face poset, in exactly the vertex orders defined by the `ORDERS` table in `verify.py`. At each vertex in the order, pair every still-unmatched face not containing it with the face obtained by adding it, provided both are still unmatched. This produces an explicit disjoint matching. All covering incidences of the entire augmented face poset are oriented upward for matching pairs and downward otherwise; the checker exhaustively removes the resulting directed acyclic graph in topological order. For stage \(1\), there are 51 pairs and one critical two-face; for \(r=4,5,6\), respectively, there are \(352,492,673\) pairs and \(59,151,175\) critical faces in dimensions \(3,4,5\); for \(r=7,8,9,10\), there are \(853,968,1013,1023\) pairs and \(115,45,10,1\) critical faces in dimensions \(6,7,8,9\). **There are no other critical faces** in any of these augmented matchings. Every claim follows from complete finite sets, not sampling. The acyclic-matching theorem of discrete Morse theory, with one zero-cell replacing the paired empty face, therefore gives a CW model with one zero-cell and just the stated same-dimensional positive cells. As their attaching maps land in a zero-cell, that CW model is a wedge of spheres of the claimed dimension, integrally and at the level of homotopy.

**(4) Endpoint and persistence.** At \(r\ge11\), every subset is allowed, giving a simplex. Because each nonzero reduced homology group of stages \(4\) through \(10\) occupies a strictly increasing degree, every inclusion-induced map there and into the next stage is zero on all positive-degree groups. The maps through stages \(1,2,3\) are isomorphisms by (2), and the generator necessarily dies on entering stage \(4\), whose reduced homology is concentrated in degree \(3\). This proves the asserted complete integral persistence module.

## Verification
The standalone `verify.py` requires Python 3 and only the standard library. It reads the two collapse-certificate JSON files from its own directory and checks the graph presentation, **all** subset memberships by two algorithms, simplicial face closure, the \(195\) individual free-face pairs and their exact final subcomplexes, each complete discrete-Morse matching, and directed acyclicity across every face incidence. Separately it calculates all reduced mod-two Betti numbers by sparse binary boundary elimination; these agree with the integral wedge classification. From the directory containing the three files run `python3 verify.py`; success ends with `GROETZSCH_HIGHER_INDEPENDENCE_FILTRATION_CHECKS_OK`. The mod-two computations are consistency tests rather than a substitute for the integral homotopy proof. In particular, no signed integer boundary computation is needed once the matching leaves cells only in one positive dimension.

## Relationship to prior work
Deshpande and Singh's higher-independence framework (arXiv:2001.05448, publicly available January 15, 2020) defines exactly these induced-component complexes and proves homotopy formulas for complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect-ary trees. Their discrete-Morse formalism supplies the matching theorem used here, but the Grötzsch Mycielskian is none of their classified families. Goyal, Shukla and Singh (arXiv:1905.06926, Theorem 4.1) already proved that the **ordinary** independence complex of a Mycielskian is a suspension; this entails the baseline \(I_1\simeq S^2\) and is explicitly not new. Work on **chordal** higher-independence complexes (arXiv:2106.10863) does not cover this triangle-free nonchordal graph, and work on ordinary independence complexes of generalized Mycielskians (arXiv:2601.13432) does not classify the higher thresholds or the inclusion maps. Published results on the Grötzsch graph's **matching** complex and graph-metric Čech nerve concern different simplicial constructions. The new statement concerns the actual vertex-subset filtration, its pairwise simple-homotopy maps, and all integral homotopy types; those conclusions do not follow from the cited published statements.

## Limitations
This is a finite-graph classification, not a theorem for all Mycielskians or all four-chromatic triangle-free graphs. It gives the persistent **homology** maps and homotopy type of each stage, not a complete classification of all homotopy-coherent inclusion diagrams, nor a description of graph-automorphism actions. Higher-threshold sphere counts may be easier to derive from general face-poset formulas; the substantive new information is their verified exact inclusion-level context and the nontrivial three-stage plateau. Complete literature indexing and independent mathematical validation are not guaranteed.

## References
1. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first posted 2020-01-15), especially Definitions 3.1–3.2, Proposition 2.10 and Theorem 2.4. https://arxiv.org/abs/2001.05448
2. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019), Theorem 4.1. https://arxiv.org/abs/1905.06926
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863. https://arxiv.org/abs/2106.10863
4. A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432 (2026), for the ordinary-independence comparison. https://arxiv.org/abs/2601.13432
