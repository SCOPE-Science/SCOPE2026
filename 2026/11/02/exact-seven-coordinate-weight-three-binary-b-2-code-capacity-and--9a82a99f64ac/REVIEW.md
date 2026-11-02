# Scientific assessment of the seven-coordinate constant-weight \(B_2\) theorem

## Correctness — PASS

The theorem is entirely finite and has a reproducible exhaustive certificate. Every candidate three-subset, integer-sum collision and exclusion quadruple is generated from scratch. The link-graph C4 obstruction is proved by an explicit pair-sum equality; its seven-edge bound is verified by exhaustive enumeration of all six-vertex graphs. The branch search partitions the remaining completion space without omitting a feasible branch, checks sizes 15 and 14, and verifies each size-14 extremizer has incidence parameter two on all pairs. A separate implementation independently checks all pair sums on the full 120-element orbit. Risks: the search is computational rather than a short human-only derivation; the finite parameter scope must not be extrapolated.

## Originality — PASS (qualified)

The 2023 paper of Sima, Li, Shomorony and Milenkovic provides the direct constant-weight \(B_2\) model and broader bounds but does not in its inspected text state this complete length-seven/weight-three optimum. The 2018 Meszka–Rosa article already gives the double-Fano design isomorphism and labeled count, which are therefore only background. Neither reviewed source proves that exactly those designs maximize the integer pair-sum codebook property. Searches across the published mathematical research index using constant-weight \(B_2\), binary weight-three, Sidon triples, double Fano planes and the 14/120 parameters did not surface such a correspondence. A 2022 general \(B_2\)-code paper was accessible as a bibliographic abstract only; possible unindexed equivalences remain a priority risk. Source snippets were not treated as whole-document proof of absence.

## Mathematical value — PASS

The problem is the smallest sharp fixed-weight source-identification problem that directly connects distinct unordered pair sums to an incidence geometry. The result identifies the exact zero-collision capacity, not just a lower bound, and completely classifies every optimal design, enabling code construction and symmetry reduction. The classification is natural at the seven-coordinate/three-marker boundary where the double Fano plane exists. This is not a claim that the already published count of double Fano planes itself is novel.

## Outcome and limits

The accepted claim is restricted to seven coordinates, Hamming weight three, and distinct-source unordered pairs summed over the integers. The statement, both verifier sources, and all public files use the same restricted claim. C, O and V passed with the originality access caveats recorded in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
