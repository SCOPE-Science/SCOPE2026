# Independent Audit — 2026-09-29

**Record:** `2026/09/19/complete-ultraspherical-minimizer-classification--58eedb8b1030`  
**Title:** Complete minimizer classification for the ultraspherical lower envelope  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `16fa0e17f2ad55550c3c47126e7bd1c4f289f68a`  
**Disposition:** **REPAIRED**

## Three-axis assessment

- **Correctness — PASS:** The mathematical classification remains correct, including the α=0 Legendre case. The strict auxiliary-polynomial argument is sufficient to rule out later-degree ties in the relevant cells, and the low-degree factors isolate the unique non-adjacent equality P_1(−1/3)=P_2(−1/3)=P_5(−1/3). As an independent stress check, direct Legendre evaluation through degree 80 for the first ten cells reproduced a unique interior minimizer k and exactly {k,k+1} at each breakpoint, except {1,2,5} at −1/3. The required repair is not mathematical but originality/scope related.
- **Originality — PASS AFTER REPAIR:** The record’s broad originality claim is no longer current. Castillo–Sadigova revised arXiv:2609.15473 on 25 September 2026, after this SCOPE record was published. New Proposition 6.3 now proves for every α>0 that interiors have a unique minimizer and breakpoints exactly the adjacent pair, which directly covers the record’s α>0 classification. The same v2 still treats α=0 only by exhibiting the Legendre 1,2,5 counterexample and does not state a complete α=0 minimizer classification. The publishable residual contribution is therefore the Legendre (α=0) completion and uniqueness of that anomaly, not the full α≥0 theorem.
- **Scientific value — PASS AFTER REPAIR:** After narrowing, the result still has clear value: it completes the one parameter value left outside the source’s new Proposition 6.3 and proves that the known Legendre 1,2,5 coincidence is the only non-adjacent minimizer tie and the unique obstruction to de Oliveira Filho’s arbitrary-minimizer monotonicity question at α=0. The α>0 part should be credited to source v2 rather than republished as a new finding.

## Independent checks

- Compared the SCOPE theorem line by line with the 25 September v2 Proposition 6.3 and its Legendre discussion.
- Rechecked the strict W_N<1 mechanism in the λ=1/2 case, including the positive projection path and strict energy-product bounds.
- Numerically evaluated Legendre P_n at interiors and breakpoints for k≤10, n≤80; all minimizer sets matched the repaired theorem.

## Literature and evidence

- Castillo and Sadigova, The lower envelope of ultraspherical polynomials, v2 — Revised 25 September 2026. New Proposition 6.3 now supplies the complete minimizer classification for α>0; Section 6 gives the Legendre 1,2,5 example but not a complete α=0 classification. (https://arxiv.org/abs/2609.15473)
- de Oliveira Filho, New Bounds for Geometric Packing and Coloring via Harmonic Analysis and Optimization — Original source of the minimizer monotonicity questions. (https://ir.cwi.nl/pub/14499)

## Limitations

- The repaired research claim is restricted to the Legendre family α=0; α>0 is now prior coverage in Castillo–Sadigova v2.
- The proof classifies minimizers but does not optimize quantitative gaps away from breakpoints.
- The α=0 originality conclusion is to the best of current indexed literature.

**Independent-audit disposition:** repaired.

GitHub was read only as evidence; no repository writes were made by this audit run.
