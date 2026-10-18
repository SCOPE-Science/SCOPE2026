# Higher-independence homotopy of the icosahedral graph beyond the two-vertex stage

## Finding

Let \(I\) be the graph of the regular icosahedron, and let \(\operatorname{Ind}_r(I)\) be the simplicial complex of vertex subsets for which every induced connected component has at most \(r\) vertices. The exact **integral homotopy types**, for every integer \(r\geq 3\), are

\[
\begin{aligned}
\operatorname{Ind}_3(I)&\simeq\bigvee^{10}S^3,\\
\operatorname{Ind}_4(I)&\simeq\bigvee^{70}S^3,\\
\operatorname{Ind}_5(I)&\simeq\bigvee^{350}S^4,\\
\operatorname{Ind}_6(I)&\simeq\bigvee^{450}S^5.
\end{aligned}
\]

For every integer \(7\leq r\leq11\),
\[
\operatorname{Ind}_r(I)=\operatorname{skel}_{r-1}(\Delta^{11})
\simeq\bigvee^{\binom{11}{r}}S^{r-1};
\]
for \(r\geq12\) it is the full simplex \(\Delta^{11}\), hence contractible. These are nonequivariant homotopy equivalences; no claim about the maps induced by inclusions of filtration stages is made.

The substantive finite cases are \(r=3,4,5,6\): the numbers and dimensions change from ten three-spheres to seventy three-spheres, then to 350 four-spheres and 450 five-spheres. The higher cases are determined structurally by the graph's vertex connectivity.

## Assumptions and scope

The graph is simple and undirected, with vertex set \(\{0,1,\ldots,11\}\). Write \(a_i=2+i\) and \(b_i=7+i\) for \(i\in\mathbb Z/5\mathbb Z\). Its edges are exactly
\[
\{0,a_i\},\quad \{1,b_i\},\quad
\{a_i,a_{i+1}\},\quad\{b_i,b_{i+1}\},\quad
\{a_i,b_i\},\quad\{a_i,b_{i-1}\},
\qquad i\in\mathbb Z/5\mathbb Z.
\]
There are twelve vertices, thirty edges, twenty triangles and degree five at every vertex. This is a labeled realization of the icosahedral graph. A face \(\sigma\) belongs to \(\operatorname{Ind}_r(I)\) exactly when \(I[\sigma]\) has no component of order greater than \(r\). The empty face is included for enumeration but omitted from the Morse face poset. All homotopy statements concern the usual geometric realizations over the integers and require no choice of coefficient field.

## Proof

**Connected-subset characterization.** For every finite graph and integer \(r\geq1\), an induced vertex set has a component of size greater than \(r\) if and only if it contains an induced connected set of exactly \(r+1\) vertices. For the forward implication, grow a connected vertex set inside that component one vertex at a time; the converse is immediate. Hence membership may be tested by the component-size bound or independently by avoidance of the connected \((r+1)\)-subsets, as in the connected-set hypergraph formulation of Abdelmalek et al. [3].

**Four explicit acyclic matchings.** Represent a face by its twelve-bit membership mask. In each fixed stage \(r\in\{3,4,5,6\}\), remove the empty face from the collection of admissible masks. For the ordered list \((v_1,\ldots,v_{12})\) below, scan the currently unmatched nonempty faces in increasing numerical mask order, pairing any still-unmatched pair \(\sigma,\sigma\cup\{v_j\}\) with \(v_j\notin\sigma\). Remove both faces before processing the next vertex. The exact pivot orders are:

- \(r=3\): \((0,9,4,8,6,3,2,10,7,5,1,11)\);
- \(r=4\): \((0,4,5,8,7,3,1,10,9,11,2,6)\);
- \(r=5,6\): \((1,9,8,5,10,2,3,7,4,0,11,6)\).

The exhaustive face counts (including the empty face) and the matched pairs / unpaired nonempty cells are:

| Stage | Counts by face cardinality, starting at zero | Matched pairs | Critical cells by dimension |
| --- | --- | ---: | --- |
| \(r=3\) | \((1,12,66,220,285,120,10)\) | 351 | one dimension-zero, ten dimension-three |
| \(r=4\) | \((1,12,66,220,495,300,40)\) | 531 | one dimension-zero, seventy dimension-three |
| \(r=5\) | \((1,12,66,220,495,792,112)\) | 673 | one dimension-zero, 350 dimension-four |
| \(r=6\) | \((1,12,66,220,495,792,924,12)\) | 1,035 | one dimension-zero, 450 dimension-five |

Acyclicity is not inferred from the counts. For every Hasse incidence between nonempty faces, orient its edge upwards precisely if it belongs to a matched pair, and downwards otherwise. The standalone checker constructs the entire directed graph and verifies, by topological sorting, that it is acyclic. The respective numbers of oriented Hasse incidences are 2,592, 4,512, 7,404 and 12,360. Thus Forman's discrete Morse theorem yields a CW complex having exactly one zero-cell and, respectively, only the listed cells of dimension \(3,3,4,5\). Since each of these dimensions is at least two, every higher-cell attaching map lands in the zero-skeleton and is null-homotopic. The four asserted sphere wedges follow **integrally**, without assuming that field homology determines homotopy.

**The later skeleton regime.** Directly inspect all vertex deletions of cardinality at most four. Their icosahedral induced complements remain connected. Consequently every induced vertex subset of cardinality at least eight is connected. For \(7\leq r\leq11\), precisely the vertex subsets of size at most \(r\) are admissible, hence the complex is the full \((r-1)\)-skeleton of an eleven-simplex. Pair every face avoiding vertex zero with its union with that vertex when admissible. This elementary acyclic toggle has one critical zero-cell and \(\binom{11}{r}\) critical \((r-1)\)-cells (the size-\(r\) faces avoiding zero), giving the stated wedge. For \(r\geq12\), every vertex subset is admissible and the full simplex is contractible.

## Verification

Run `python3 verify_higher_icosahedral.py` from the directory containing the included standalone verification program. It uses only Python's standard library and reconstructs the graph from the displayed edge rule. It performs an exhaustive comparison of component sizes computed by graph search and by a separately implemented disjoint-set union; checks the alternative connected-forbidden-set membership criterion; compares every one of the 4,096 vertex masks; verifies all matching pairs and the absence of directed Hasse cycles; computes ordinary simplicial mod-two boundary ranks as a separate homological cross-check; and enumerates all deletions of at most four vertices.

The full mod-two boundary-rank vectors in increasing positive boundary degree are, respectively, \((11,55,165,110,10)\), \((11,55,165,260,40)\), \((11,55,165,330,112)\), and \((11,55,165,330,462,12)\). These checks are finite exhaustive verifications for a graph with exactly twelve vertices; the integral homotopy conclusion rests on the verified acyclic Morse matchings, not on field homology alone. Successful execution prints `ICOSAHEDRAL_HIGHER_INDEPENDENCE_STAGES_VERIFIED`.

## Relationship to prior work

Deshpande and Singh [1] formalize these higher-independence complexes and determine homotopy types for complete multipartite graphs, fully whiskered graphs, paths, cycles and regular rooted trees. Deshpande, Shukla and Singh [2] give homological connectivity bounds and a wedge result for chordal graphs. Abdelmalek et al. [3] give a connected-set hypergraph equivalence and shellability/vertex-decomposability results for trees and caterpillars. The icosahedral graph is neither chordal nor among those treated families.

The two-vertex stage \(\operatorname{Ind}_2(I)\) is excluded from the present claim of novelty: it coincides with the induced-forest subcomplex with degree bound one and has been calculated separately. For \(r\geq3\), the complex admits cycles inside components of size at most \(r\) (in particular, triangles at \(r=3\)), unlike any induced-forest subcomplex. Computations of ordinary independence, graph-metric neighborhood/Čech complexes, matching complexes and cut complexes on the same graph use different face conditions and do not imply these four explicit homotopy types.

## Limitations

The result is confined to the standard twelve-vertex icosahedral graph. It does not determine persistence maps between the stages, group actions on their integral homology, behavior for other Platonic or strongly regular graphs, or a general formula for arbitrary graphs. The large-\(r\) skeleton description is an elementary consequence of five-vertex-connectivity, whereas the main new calculations are the four intermediate stages. An independent mathematical audit has not yet been performed, and equivalent unindexed work cannot be ruled out solely by search.

## References

[1] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types* (first public 2020-01-15), arXiv:2001.05448, https://arxiv.org/abs/2001.05448.

[2] P. Deshpande, S. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs* (first public 2020-01-19), arXiv:2001.06775, https://arxiv.org/abs/2001.06775.

[3] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes* (first public 2021-06-21), arXiv:2106.10863, https://arxiv.org/abs/2106.10863.
