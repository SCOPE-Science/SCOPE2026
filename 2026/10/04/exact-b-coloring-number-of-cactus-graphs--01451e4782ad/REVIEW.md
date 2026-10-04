# Review: Exact \(B\)-coloring number of cactus graphs

## Correctness
**PASS.** The lower bounds are forced independently by the maximum degree, a rainbow \(C_4\), and odd-cycle edge-coloring parity. The upper bound is constructive on the block-cut tree: a child bridge needs one color absent at its cut vertex; a child cycle always has two available colors at the cut vertex, a \(C_4\) has two further palette colors, and an attached odd cycle has a third color because its attachment forces \(\Delta\ge3\). Every cycle of a cactus lies within one block, so no cross-block \(C_4\) is omitted. The exact conflict-graph census on all \(6074\) connected labeled cacti of orders \(2\) through \(6\) found no counterexample.

## Originality
**PASS.** The closest general results are broader upper bounds rather than this exact classification. The 2026 outerplanar theorem of Kong, Wang, and Zheng already implies \(q_B=\Delta\) for the slice \(\Delta\ge7\); it does not imply the low-degree cactus formula or the sharp threshold four. Hu–Kong–Wang and Jiang give degeneracy/codegree or \(K_{{2,t}}\)-free bounds, and the earlier outerplanar work gives \(\Delta+1\)-type control. Exact searches for cactus \(B\)-coloring, rainbow-
\(C_4\) cactus edge-coloring, and extended-line-graph cactus formulations found no statement matching the formula. The subcubic preprint SSRN 6528922 is a residual risk because only its abstract was available; that abstract states a six-color extremal characterization, not the present exact cactus values.

## Value
**PASS.** Cacti are a standard block-sparse outerplanar class, and the finding gives a natural complete classification rather than an arbitrary finite slice. It resolves the degree-optimal \(B\)-coloring behavior for the entire class from the sharp threshold \(\Delta=4\), strengthening the previously available all-outerplanar threshold \(\Delta=7\) on this subclass. The sharp obstruction at maximum degree three is concrete: a \(C_4\) with one pendant edge has \(q_B=4>3\).

## Closest literature and limitations
The proof uses no unproved computational extrapolation. The finite verifier checks the exact conflict-graph chromatic number only through six vertices. High-degree cases overlap with the general outerplanar theorem, while the new content is the exact all-degree cactus classification. The inaccessible full text of the subcubic preprint leaves a bounded literature-comparison risk, explicitly retained rather than treated as evidence of novelty.

Same-model review: passed. Independent audit: not yet performed.
