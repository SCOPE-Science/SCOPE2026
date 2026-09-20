# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof decomposes into three independently checkable facts. First, the classical rook-graph correspondence identifies mutual-visibility sets with C4-free bipartite edge sets. Second, the induced rook graph on selected cells is exactly the line graph of the associated bipartite graph. Third, an edge-maximal C4-free bipartite graph cannot have two edge-containing components: adding an edge from the left side of one component to the right side of another cannot create a C4 because a new C4 would require a pre-existing length-three path between those components. Hence every inclusion-maximal mutual-visibility set is connected. This yields mu_c=mu=z immediately. The explicit large-side regime follows from the pair-count inequality sum binom(d_j,2)<=binom(p,2) and its equality conditions. The p=4 exceptions are a finite pair-packing calculation. A standalone exhaustive verifier independently checks all subsets in six small rook graphs, including all 65,536 subsets of K4 square K4.

Adversarial checks considered isolated row/column vertices, one-edge components, and the possibility that the added cross-component edge creates a new C4. Isolated vertices do not affect line-graph connectivity; if there are two edge-components the cross edge is absent and any C4 containing it would leave an impossible old length-three path between the components. No hidden connectivity assumption is used.

## Originality

**PASS, to the best of our knowledge.** The September 2026 preprint introducing connected mutual visibility was inspected in full text. It gives the diameter-two criterion and exact results for several classes and operations, but no rook/Hamming graph or Cartesian-product theorem was found; searching the full text for Hamming gives no match, and Cartesian appears only in a cited reference. The classical Cartesian-product paper was also inspected in full text and proves mu(K_m square K_n)=z(m,n;2,2), but predates and therefore does not treat the connected parameter. Exact and synonymous external searches for connected mutual visibility together with rook graphs, Hamming graphs, Cartesian products, and Zarankiewicz numbers found no equivalent statement. The April 2026 Builder-Blocker paper treats ordinary mutual visibility on Hamming graphs and uses the same C4-free characterization, but likewise predates the connected invariant.

The elementary graph-saturation step may already be implicit or explicit in older C4-saturation literature. In particular, Bryant--Fu (Discrete Mathematics 259 (2002), DOI 10.1016/S0012-365X(02)00371-0) studies C4-saturated bipartite graphs; only bibliographic and abstract material was inspected here. That source could contain the connectivity observation for saturated bipartite graphs, so no novelty is claimed for that standalone observation. It would not itself state the connected-mutual-visibility consequence, whose invariant was introduced in 2026. No concrete inaccessible source was found that is likely to contain the full claimed theorem. Very recent unindexed parallel work remains a residual risk.

## Value

**PASS.** The result completely determines the new connected mutual-visibility parameter on all two-factor Hamming/rook graphs in terms of a classical extremal quantity, and proves the stronger structural fact that connectivity is automatic at every maximal ordinary mutual-visibility set. This both supplies exact infinite regimes (including all K2 square Kq and K3 square Kq, and a full K4 square Kq formula) and shows that the square case inherits the full difficulty of the Zarankiewicz problem. The result therefore identifies a sharp boundary between the extra connectedness constraint and the underlying extremal obstruction rather than merely giving a numerical example.

## Limitations

The theorem reduces the general exact value to z(m,n;2,2), which is itself open. The explicit q+binom(p,2) formula is limited to the regime q>=binom(p,2), apart from the separately stated p=4 cases. Higher-dimensional Hamming graphs are not covered. Finite computation supports but does not replace the proof. No independent validation or independent audit has been performed.
