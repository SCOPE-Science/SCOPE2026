# Self-review

## Correctness — PASS

The proof determines the exact error-output sets for weight-two codewords under **exactly two consecutive** deleted coordinates. The marker transformation sends nonadjacent parents to edges/loops on \(n-2\) vertices, where each selected edge consumes all of its marker vertices in weight-one output space. Loops at distance two share a weight-two output. This gives the maximum number \(\alpha_m\) of permitted loops and the sharp \(f(m)\) bound. At most one adjacent parent can be selected, and a boundary adjacent parent achieves the strongest bound. The closed-form construction occupies disjoint markers, avoids the only remaining weight-two collision (translation by two), and is independently replayed from raw deletion balls. Endpoint cases \(n=2,3\) and modulo-four residues have been checked. The finite verifier is supporting evidence, not a substitute for the infinite proof.

## Originality — PASS (with limitations)

Actual searches for constant-weight burst-2 deletion codes and the sharp coefficient were compared with published results and accessible historical mathematical claims. The closest arXiv papers on general consecutive-burst coding [1,2] do not give the fixed-weight-two exact optimum. The closest constant-weight graph method [3] treats **unrestricted deletion locations**, so its theorems do not directly imply this capacity. Previously published finite results for other burst channels and covering-code syndrome sizes likewise are not the stated invariant. A hidden earlier specialization remains a residual bibliographic risk; the searches do not prove absolute uniqueness.

## Mathematical value — PASS

The result solves a natural sparse-marker exact-burst synchronization-code capacity problem for every block length and gives an explicit optimal family rather than an isolated small case. The graph reduction exhibits why the rate of growth is \(3/4\) codeword per additional source coordinate, with a four-coordinate periodic construction. The exact formula is neither a generic sphere-packing estimate nor a routine substitution into an unrestricted-channel bound.

## Scientific limits and relationships

The theorem does not extend the exact result to arbitrary two-deletion positions, variable-length bursts or other weights. No external independent scientific validation is asserted. Literature comparison focused on [1]–[3], the published related coding records identified in the audit, and their claim implications.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Wang et al., *Non-binary Codes for Correcting a Burst of at Most t Deletions*, arXiv:2210.11818 (2022).

[2] Schoeny et al., *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820 (2016).

[3] Cullina et al., *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056 (2012).
