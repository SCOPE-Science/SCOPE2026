# The second-independence complex of the Paley graph on \(17\) vertices is eighteen three-spheres

## Finding

Let \(P_{17}\) have vertex set \(\mathbb Z/17\mathbb Z\), with distinct \(i,j\) adjacent when \(j-i\) is a nonzero square modulo \(17\). Its second-independence complex \(X=\operatorname{Ind}_2(P_{17})\) has the exact integral homotopy type
\[
X\simeq\bigvee^{18}S^3.
\]
Although this space has homology in one positive degree, the simplicial complex itself is nonpure: it has \(34\) facets with four vertices and \(68\) facets with five vertices.

Moreover, under the natural translation action of \(C_{17}\), the rational third homology is the direct sum of the trivial and regular representations:
\[
\widetilde H_3(X;\mathbb Q)\cong\mathbb Q\oplus\mathbb Q[C_{17}]
\quad\text{as }\mathbb Q[C_{17}]\text{-modules}.
\]
In particular, its translation-invariant rational third homology has rank \(2\).

## Assumptions and scope

All graphs are simple and undirected. A face of \(\operatorname{Ind}_2(G)\) is a vertex subset for which every connected component of the induced graph contains at most two vertices. Equivalently, the induced subgraph has maximum degree at most \(1\): any connected graph with at least three vertices contains a vertex of degree at least two.

For \(P_{17}\), the quadratic residues are
\[
\{1,2,4,8,9,13,15,16\}\subseteq \mathbb Z/17\mathbb Z.
\]
Each subset is encoded by a \(17\)-bit integer: bit \(i\) records vertex \(i\). The empty subset is included as a face but is not included in the nonempty face-poset Morse matching. The theorem applies to this graph and this second-independence complex only; it does not claim a formula for arbitrary Paley graphs or higher filtration thresholds.

## Proof

**Exact faces and facets.** The membership criterion above yields \(868\) faces including the empty face, with nonempty face numbers
\[
(f_0,f_1,f_2,f_3,f_4)=(17,136,340,306,68).
\]
There are exactly \(34\) maximal faces of cardinality \(4\) and \(68\) of cardinality \(5\). The executable checker computes these numbers in two different ways: by testing induced vertex degrees and by explicitly traversing induced connected components. It visits every one of the \(2^{17}=131072\) subsets.

**Acyclic matching.** Remove the empty face and match by successive element toggles, in the vertex order
\[
(9,3,0,6,15,11,8,10,13,12,1,2,16,4,14,5,7).
\]
At each stage, pair every still-unmatched face not containing the selected vertex with its one-vertex enlargement if that enlargement is also still unmatched. This gives \(423\) disjoint pairs. Orient each nonmatched cover relation from the larger simplex to the smaller one and reverse the \(423\) matched relations. A topological sort of all \(867\) nonempty faces and all \(2856\) codimension-one incidences visits every face, proving acyclicity.

The critical cells comprise one vertex (mask \(512\)), one two-cell (mask \(65569\)), and nineteen three-cells. There are no critical one-cells or cells above dimension three. Forman's discrete Morse theorem therefore produces a CW model with one cell in each of dimensions \(0\) and \(2\), and nineteen in dimension \(3\).

**Integral attaching degrees.** Order vertices increasingly, so removing the \(j\)-th vertex from an oriented simplex has incidence sign \((-1)^j\). For each two-simplex \(\tau\), compute its coefficient in the lone critical two-cell by the following exact recursion. A critical two-cell projects to \(1\); a two-cell that is the upper member of a one/two matched pair projects to \(0\); if \(\tau\) is the lower member paired with a three-simplex \(\beta\), solve the signed boundary relation of \(\beta\) for \(\tau\). The orientation acyclicity guarantees that this recursion terminates. This is integral Morse cancellation, with every division by a pivot equal to \(+1\) or \(-1\).

Applying the resulting chain projection to the boundaries of the nineteen critical three-cells gives three nonzero coefficients, all \(-1\), at critical-cell masks \(67620\), \(69728\), and \(99360\). The remaining sixteen coefficients are \(0\). Thus the sole Morse differential has the primitive degree vector with entries \(0\) or \(-1\), and its image is all of the critical two-chain group \(\mathbb Z\).

The two-skeleton of the CW model is \(S^2\), and each three-cell attachment is classified by its degree in \(\pi_2(S^2)=\mathbb Z\). Attach one of the degree-\(-1\) cells first: the resulting \(S^2\cup_{\deg(-1)}e^3\) is contractible. Each of the other eighteen three-cells then has a nullhomotopic attaching map into that contractible skeleton, and hence the full model is a wedge of eighteen three-spheres.

**Translation representation.** The translation \(i\mapsto i+1\) preserves adjacency and therefore acts simplicially on \(X\). Since \(17\) is prime and no nonempty face has more than five vertices, no nonidentity translation fixes a nonempty face setwise. Every nonidentity translation consequently has simplicial Lefschetz number \(0\). The integral homotopy classification gives \(H_0(X;\mathbb Q)\cong\mathbb Q\) and \(\widetilde H_3(X;\mathbb Q)\cong\mathbb Q^{18}\), with all other reduced groups zero. The Lefschetz identity forces trace \(1\) on \(H_3\) for every nonidentity translation, and its identity trace is \(18\). This is the character of \(\mathbb Q\oplus\mathbb Q[C_{17}]\), which determines the rational representation of the cyclic group.

## Verification

The accompanying standalone `verify_paley17.py` uses only the standard Python library and recomputes the full face set, facet counts, the complete acyclic matching, the exact signed critical boundary, independent mod-two simplicial ranks, and the translation permutation checks. The file `certificate.json` records the finite output. The checker confirms mod-two boundary ranks \((16,120,220,68)\) and Betti ranks \((1,0,0,18,0)\) in dimensions \(0\) through \(4\), consistent with the integral Morse argument. The Smith invariant factor of the only nonzero Morse differential is \(1\).

To replay: run `python -S verify_paley17.py` using Python 3; successful completion prints `PALEY17_SECOND_INDEPENDENCE_EXACT_CHECK_OK` and the computed certificate.

## Relationship to prior work

Deshpande and Singh introduced extensive homotopy calculations for higher-independence complexes, including complete multipartite graphs, whiskered graphs, cycles and rooted trees [1]. Their results do not cover the Paley graph here. Deshpande, Shukla and Singh proved domination-connectivity bounds and chordal-graph results [2]. The graph \(P_{17}\) is not chordal: vertices \(\{0,1,3,4\}\) induce the four-cycle \(0-1-3-4-0\). The work of Abdelmalek and collaborators develops shellability and vertex-decomposability for trees and caterpillars and other chordal constructions [3], and does not imply this nonchordal homotopy type.

A distinct published calculation studies the *open-neighborhood* complex of \(P_{17}\). That complex is not \(\operatorname{Ind}_2(P_{17})\): the open-neighborhood complex contains an eight-vertex simplex from any vertex's neighborhood, whereas every face of the present complex has at most five vertices. Likewise, results for second-independence complexes of smaller Paley graphs and ordinary independence complexes of larger Paley graphs do not imply this specific homotopy classification or translation character.

## Limitations

The Morse proof is finite and computer-assisted, with all enumerated faces and boundary cancellations reconstructed by the standalone checker; its validity depends on the precisely specified graph and face criterion. No general formula for Paley graphs, no integral group-ring classification of the translation module, and no claim of shellability or Cohen–Macaulayness is made. Search-based comparisons do not exclude unindexed equivalent work. An independent mathematical audit has not been performed.

## References

[1] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 2020-01-15. https://arxiv.org/abs/2001.05448

[2] P. Deshpande, S. Shukla, and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775, 2020-01-19. https://arxiv.org/abs/2001.06775

[3] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, 2021-06-21. https://arxiv.org/abs/2106.10863
