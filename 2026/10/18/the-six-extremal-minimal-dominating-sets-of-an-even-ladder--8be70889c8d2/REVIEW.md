# Scientific review: maximum minimal domination on ladders

## Correctness — PASS
A selected vertex is essential in a dominating set precisely when it has a private closed-neighborhood witness. Such a witness lies within two ladder columns. This yields an exact finite-state recognizer, independent of ladder length. The standalone verifier exhaustively builds 229 states and 471 transitions, checks the max-plus potential inequalities giving \(|D|\le n\), and verifies a 91-state tight-language/prefix-language product with no forbidden terminal. Explicit periodic constructions attain the bound and the parity conditions give the precise count. A separate brute-force implementation checks all vertex subsets for nine ladder lengths. The infinite result rests on the finite-state proof, not finite-length extrapolation.

## Originality — PASS, with residual risk
Sahbi's arXiv:2610.03785v2, sections 2 and 8, already proves the upper-domination **value** for all bipartite grids, and is not claimed as new. Its examined classification does not enumerate or characterize every extremal minimal dominating set. Mertens' arXiv:2408.08053 counts all dominating sets rather than inclusion-minimal maximizers; OEIS A290379 counts all minimal dominating sets without their maximizing breakdown. Targeted exact and synonymous searches have not found an equivalent ladder optimizer classification. Unindexed equivalent work remains possible; absence from an index is not proof of universal novelty.

## Value — PASS
This gives the entire extremal family, not just a parameter value, for a canonical infinite graph class. Its constant 4/6 optimizer count contrasts with exponentially many minimal dominating sets. The even-length full/empty-rung patterns show that maximum-size minimal dominating sets need not be independent, so the known equality of upper domination and independence numbers does not supply the classification.

## Scope and scientific limitations
The statement covers exactly \(P_2\square P_n\), not wider grids. Computer-assisted exact finite-state exhaustion is essential to the supplied proof. No external independent validation or unindexed-literature completeness is claimed.

Self-review: passed. Independent audit: not yet performed.
