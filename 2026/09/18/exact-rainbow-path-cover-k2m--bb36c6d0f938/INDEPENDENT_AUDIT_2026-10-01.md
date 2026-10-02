# Independent mathematical audit — SCOPE-20260918-bb36c6d0f938

Final disposition: **PASS**.

## Correctness
**PASS.** The proof was reconstructed directly. Properness makes the two color lists injective and their cross-coincidences a fixed-point-free partial injection phi. For m=2t, a first perfect matching sigma avoids at most one forbidden partner per vertex. The second allowed bipartite graph removes three partial matchings, so both sides have degree at least t-3>=t/2 for t>=6; the standard Hall argument therefore gives tau. The paths sigma(u)-x-u-y-tau(u) are simple, pairwise edge-disjoint, exhaustive, and all four colors are distinct by exactly the three avoidance rules plus properness. The odd case deletes one large-side vertex and uses its two incident edges as a rainbow P3. The degree-m vertex supplies the matching lower bound ceil(m/2).

## Originality
**PASS.** The directly relevant Liu–Xu–Yang 2026 primary abstract gives only an asymptotic formula for complete multipartite graphs; its K_{2,m} specialization is (1+o(1))m/2. Targeted searches did not locate the exact eventual equality or the prescribed-middle P5 decomposition. Full text of that very recent source was not available through the routes tried, so this is a best-of-knowledge conclusion with explicit residual risk.

### Equivalent formulations
No equivalent matching formulation was found stated as an earlier theorem for all proper colorings.

### Broader coverage
The inspected broader results do not imply exact equality for every m>=12.

### Exact database or table
No-table evidence is not treated as proof of novelty.

### Claim versus prior implication
The final theorem is strictly sharper than the inspected asymptotic prior statement.

## Value
**PASS.** The theorem upgrades a motivated asymptotic extremal parameter to exact equality on an infinite complete-bipartite family, strengthens cover to decomposition with prescribed internal roles, and gives a constructive polynomial-time proof. This is a natural structural boundary result.

## Source inspections
- **Sharp Rainbow Path Covers in Dense and Complete Multipartite Graphs** (arXiv:2609.18740): primary abstract; full-text retrieval was attempted but unavailable Assessment: ABSTRACT_ONLY; confirms asymptotic prior but cannot exclude hidden exact special-case material. Evidence: The abstract gives a uniform asymptotic formula for complete multipartite graphs.

## Residual risks
- The motivating September 2026 paper is exceptionally recent and was not read in full, leaving a real simultaneous/hidden-special-case overlap risk.
- The threshold m>=12 comes from the sufficient degree condition and is not claimed optimal.

The JSON companion records the structured four-part originality comparison and the same limitations.
