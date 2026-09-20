# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof first classifies DFS-tree shapes in a complete bipartite graph using the defining ancestor-comparability property of undirected DFS trees: vertices in distinct child subtrees are incomparable, while every cross-part pair in a biclique is adjacent. This forces any genuine branching to occur only at a terminal vertex of the alternating spine, with all extra vertices as same-side leaves. For a root in the larger part, every spine cut can then be counted exactly, producing the two quadratic families \(h_i\) and \(g_i\). Leaf-envelope loads are dominated by the terminal spine cut. The alternative root side has the same \(g_i\) cuts and no smaller counterpart to any \(h_i\), so the larger-side root is optimal.

The comparison identities \(h_i-g_i=2i-b\), \(h_i-g_{i-1}=a-2i+2\), and \(h_a-g_{a-1}=2-a\) reduce the optimum to the single concave sequence \(g_i\), except for the explicitly isolated balanced odd case. Maximizing that quadratic gives the two formula regimes separated between \(b=3a-2\) and \(b=3a-1\). For complete graphs, every DFS tree is a Hamilton path, and direct cut counting gives \(i(n-i)-1\), hence \(\lfloor n^2/4\rfloor-1\).

Adversarial checks included stars \(a=1\), \(K_{2,b}\), balanced odd and even bicliques, the regime boundary, the possibility that enveloping back edges dominate a leaf edge, the root-side choice, and the distinction between KLX and crossing-only DFS-tree congestion. In the canonical optimal tree, the global maximum is attained on a spine edge by crossing back edges, proving \(\operatorname{DTC}=\operatorname{KLX}\) for these families. A standalone definition-level verifier checks small bicliques by enumerating spanning trees, roots, and child orders, and checks all rooted Hamilton-path orders through \(K_8\); all tested cases agree with the formulas. Computation supports but does not replace the proof.

## Originality

**PASS, to the best of our knowledge.** The current full arXiv text of Bourotte--Ducloz--Orponen--Seki was inspected around the KLX definition, the DTC comparison, the small-KLX structural results, and the treewidth result. It develops \(\operatorname{KLX}\le1\) and \(\operatorname{KLX}\le2\), but no exact formula for cliques or complete bipartite graphs was found. Searches using KLX, kissing-loop crossing, DFS-tree congestion, Trémaux-tree congestion, normal-spanning-tree congestion, open back edges, complete graphs, and complete bipartite graphs found no equivalent formula.

The older congestion literature was checked as a possible stronger/general source. Kozawa--Otachi--Yamazaki and earlier work determine ordinary spanning-tree congestion for complete multipartite families; survey statements give \(\operatorname{stc}(K_n)=n-1\) and \(\operatorname{stc}(K_{m,n})=m+n-2\). This does not imply the present theorem because ordinary STC minimizes over arbitrary spanning trees, whereas DTC restricts to DFS trees and KLX additionally permits ordered envelope effects. The new formulas in fact quantify an order-linear separation between unrestricted and DFS-restricted congestion on balanced dense families.

The main residual risk is very recent unindexed work on KLX, since the parameter itself is new in 2026. Older literature might also phrase DFS-restricted cut congestion under an unusual traversal term, but no concrete source found states the formulas, the biclique phase transition, or the equality \(\operatorname{DTC}=\operatorname{KLX}\) on these families.

## Value

**PASS.** The result gives the first exact dense-family values located in the KLX literature search, including both cliques and all bicliques. The complete-bipartite theorem is not a numerical example: it classifies the allowable DFS-tree geometry, produces a closed formula for every \((a,b)\), identifies a sharp transition from an interior bottleneck to a terminal bottleneck, and resolves the possible contribution of enveloping edges. The corollary comparing ordinary STC with DFS-restricted STC shows that the DFS requirement can cost a factor linear in the part size, giving a concrete quantitative separation between two closely related congestion notions.

## Limitations

The theorem covers complete graphs and complete bipartite graphs, not general complete multipartite graphs. It does not classify every KLX-minimizing ordered DFS tree; it supplies and proves optimality of a canonical larger-part-rooted tree. No stability statement is given for nearly complete graphs or bicliques with deleted edges. Very recent unindexed KLX work and older literature under substantially different terminology remain residual originality risks. Finite computation is supporting evidence only. No independent validation or independent audit has been performed.
