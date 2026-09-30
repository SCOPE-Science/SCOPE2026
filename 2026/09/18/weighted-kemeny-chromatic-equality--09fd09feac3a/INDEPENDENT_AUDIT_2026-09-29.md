# Independent Audit — 2026-09-29

**Record:** `2026/09/18/weighted-kemeny-chromatic-equality--09fd09feac3a`  
**Title:** Weighted equality cases for the chromatic Kemeny bound  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The equality proof is sound. Equality in the partition-compression bound and Cauchy forces quotient eigenvalues 1 and −1/(r−1); equality of the full and compressed squared traces then kills every orthogonal block, so M=SBSᵀ. The zero diagonal forces equal color-class weighted volumes and B off-diagonal 1/(r−1), yielding w_uv=d_ud_v/((r−1)A). The converse spectrum is immediate. The r=n boundary case separately forces the normalized Perron vector to have equal coordinates and hence uniform complete-graph weights.
- **Originality — PASS:** The September 2026 Abiad–Carmona–Encinas–Ghorbani–Jiménez–Samperio source explicitly advertises the chromatic lower bound for weighted graphs but says its equality classification is for unweighted graphs. Targeted searches for weighted multipartite Kemeny equality, rank-one weighted bipartite equality, and equivalent reversible-chain formulations found no prior statement of this weighted classification. Originality remains to the best of the searched evidence.
- **Scientific value — PASS:** The theorem closes a concrete gap left by the motivating weighted bound and gives a structural parameterization: equality is governed by stationary-mass balance, not cardinality balance. It also yields every multipartite shape after weighting, the rank-one bipartite criterion, and the equality-family dimension.

## Independent checks

- Re-derived the quotient-spectrum Cauchy equality condition and the trace-of-squares rigidity step.
- Verified the r=n singleton-part case independently from the spectral equality.
- Checked the converse weighted degrees and normalized spectrum symbolically.
- Recomputed representative unequal-part and nonuniform-mass examples; the prescribed degrees and K=n−2+1/r agree, while generic non-rank-one bipartite weights are strict.

## Literature and evidence

- Abiad et al., Kemeny's constant via matrix compression and eigenvalue interlacing — Primary source: weighted chromatic bound; abstract explicitly limits its equality classification to unweighted graphs.
- Ciardo, Dahl and Kirkland, On Kemeny's constant for trees with fixed order and diameter — Earlier unweighted bipartite context, not the weighted classification.

## Limitations

- Finite connected undirected graphs and strictly positive weights on present edges only.
- Originality is to the best of current indexed literature; an older equivalent reversible-Markov-chain formulation under different terminology remains a residual risk.

**Independent-audit disposition:** passed.
