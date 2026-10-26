# Mathematical review

## Correctness — PASS
The theorem is an exact minimum over canonical one-defender and two-defender strategies. The proof reduces any feasible function to at most two effective defenders without increasing its weight, accounts for zeros in each defender's own part, and performs the remaining one-variable ceiling minimization by residues modulo \(p\). The correction is possible only when both ceiling terms drop upon leaving a third-part vertex labeled \(1\). The construction attains the resulting values. The finite verifier independently searched 844 zero-count configurations and 90 complete label universes; it corroborates but does not replace the proof.

## Originality — PASS
The defining \(p\)-strong Roman paper provides the neighbor-zero defender model, general bounds and a complete-bipartite value, not the arbitrary multipartite formula for \(r\ge3\). The closest published complete-multipartite result proves the ordinary \(p=2\) strong Roman value, while the total strong Roman result changes the positive-support condition. The \(k\)-strong simultaneous-attack invariant is distinct. The new two-defender mod-\(p\) correction is not implied by those statements. Indexed coverage is not exhaustive; an unindexed earlier equivalence remains possible.

## Value — PASS
This resolves a natural graph-class problem for a recent parameter, for every nontrivial integer capacity \(p\) and arbitrary multipartite part sizes, with an \(O(r^2)\)-arithmetic answer and constructive optimizers. In particular, \(\gamma^4_{\mathrm{StR}}(K_{5,5,5})=7\) while the old general single-defender upper strategy gives \(8\). With fixed \(p\ge3\), the improvement for balanced tripartite graphs grows linearly in their part sizes. The exact residue effect and structural reduction justify mathematical interest beyond a single test graph.

## Limits and nearest literature
The result does not enumerate all minimum functions and is restricted to complete multipartite graphs with at least three parts in \(3\le p\le\Delta-1\). The defining source is Valenzuela-Tripodoro et al., *p-Strong Roman Domination in Graphs*, WSEAS Transactions on Mathematics 23 (2024), DOI:10.37394/23206.2024.23.104, arXiv:2501.10140. The closest complete-multipartite ordinary and total strong Roman theorems are cited in `RESULT.md`. Unindexed equivalents remain an originality risk. Independent mathematical evaluation is outstanding.

Self-review: passed. Independent audit: not yet performed.
