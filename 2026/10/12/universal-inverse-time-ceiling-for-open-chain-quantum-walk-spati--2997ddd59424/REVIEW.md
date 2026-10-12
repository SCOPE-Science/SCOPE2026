# Review

## Correctness

PASS. The source's Eq. (25) makes each site density matrix diagonal in the \(2^M\)-configuration basis, and Eq. (26) makes every configuration probability a product of the per-walker presence/absence probabilities. Summing squared configuration probabilities therefore factorizes exactly. The finite-time ceiling then follows from \(1-\prod_i(1-x_i)\le\sum_i x_i\), normalization \(\sum_j p_{ij}=1\), and the source's Eq. (24). The proof covers arbitrary \(M\ge1\) and all times for which the source's product model is defined. Exact-rational replay checks 19,607 local cases and three multi-site distributions, but the analytic proof is decisive.

## Originality

PASS, with residual literature risk. The full primary paper was inspected at its many-particle construction, Meyer--Wallach definition, Eqs. (24)--(26), the numerical open-chain phase diagram, and the closed-chain comparison. It supplies the premises and a qualitative/numerical decay observation but not the factorized purity identity, the inverse-participation-ratio refinement, or the universal \(O(t^{-1})\) ceiling. Focused published-finding corpus searches using the paper identifier, Meyer--Wallach terminology, the product-probability formulation, and the proposed inverse-time bound returned no implication-equivalent record. The later two-walker exchange-symmetry paper arXiv:2203.00873 concerns a different two-walker/post-selection problem; only its public preprint material was used for comparison, so an equivalent statement hidden elsewhere remains a residual risk.

## Value

PASS. The source's central numerical observation is that open-chain spatial entanglement eventually falls as the available lattice region expands, whereas a fixed closed chain need not exhibit the same late-time decrease. The theorem turns that model-specific numerical/heuristic observation into a finite-time, coin-independent structural obstruction: at fixed \(M\), no choice of one-particle probability profiles within the stated independent-walker model can keep the prescribed open-chain Meyer--Wallach quantity bounded away from zero. The sharper inverse-participation-ratio bound also identifies how localization can only reduce the ceiling further.

## Closest literature and limitations

The direct source is arXiv:0901.0671 / DOI:10.1088/1751-8113/43/23/235303. A later plausible title, arXiv:2203.00873, studies exchange symmetry for two walkers rather than the all-
\(M\) product Meyer--Wallach quantity. The theorem does not cover interacting walkers, correlated initial particle positions, fixed-cycle asymptotics, or other spatial-entanglement measures, and it does not claim sharpness.

Self-review: passed. Independent audit: not yet performed.
