    # Independent audit — 2026-09-29

    **Record:** `2026/09/19/gaussian-magnitudes-renyi-and-local-gpi-geometry--70a03a158872`  
    **Title:** Exact Rényi-2 dependence of Gaussian magnitudes and local GPI geometry  
    **Repository:** `SCOPE-Science/SCOPE2026`  
    **Audited tree:** `5a90117604cea4b3953ade41636edfb1f045901b`  
    **Disposition:** **REPAIRED**

    ## Correctness

    **PASS_AFTER_REPAIR** — The retained local product-moment theorem is correct. The normalized Hermite coefficient for |Z|^alpha at H_2 is alpha; parity kills odd vertex degrees. Therefore the only degree-2 surviving multigraph is a doubled edge, giving (1/2) alpha_i alpha_j rho_ij^2, and the only degree-3 survivor is a triangle, giving alpha_i alpha_j alpha_k rho_ij rho_ik rho_jk. The alpha=2 trivariate case reproduces Wick's exact identity. The local quadratic lower bound follows by absorbing the cubic remainder. The exact Rényi-2 determinant and weak-correlation formulas are also correct but are removed from the novelty claim because they already appear in the prior SCOPE record.

    ## Originality

    **PASS_AFTER_REPAIR** — The filed package overclaimed originality by presenting the exact Gaussian-magnitude Rényi-2 theorem despite the earlier 18 September SCOPE record `gaussian-magnitude-renyi2-total-correlation--4eebefe6d8fe`, which already contains the determinant formula, lambda_max<2 finiteness threshold, bivariate identity, and quartic/triangle expansion. Ogasawara's open preprint also supplies general multivariate absolute-product-moment series, so no priority is claimed for that machinery. The repair retains only the explicit low-order signed-triangle extraction and its comparison with Rényi-2 geometry; targeted current searches did not locate that comparison as a stated theorem.

    ## Scientific value

    **PASS_AFTER_REPAIR** — After removing the duplicated Rényi theorem, the residual statement still gives a useful local geometric distinction: positive-exponent GPI moments see pair dependence at quadratic order and the sign of three-way correlation loops at cubic order, whereas magnitude Rényi-2 dependence begins at quartic order and squares the triangle. This is a compact but meaningful local characterization rather than a second copy of the exact divergence theorem.

    ## Findings

    - The original Rényi-2 theorem duplicates the 18 September SCOPE total-correlation record and must not be re-claimed.
- Ogasawara's publicly available preprint gives general multivariate Gaussian absolute-product-moment series, so the series machinery itself is prior art.
- The surviving expansion has doubled-edge coefficient (1/2) alpha_i alpha_j and signed-triangle coefficient alpha_i alpha_j alpha_k.
- For alpha_i=2 in three dimensions, Wick's exact formula reproduces the retained coefficients with no ambiguity.

    ## Independent checks

    - Re-derived the low-order expansion from the multigraph/Hermite series and parity constraints.
- Checked the alpha=2 trivariate specialization against Wick's formula.
- Rechecked the local quadratic lower bound from the Frobenius norm normalization.
- Inspected the open Ogasawara preprint and the earlier SCOPE Rényi-2 record for overlap.

    ## Sources

    - https://arxiv.org/abs/2609.20234 — Ouimet–Greaves strong Gaussian product inequality for all positive exponents.
- https://doi.org/10.1007/s41237-025-00277-2 — Ogasawara general series formulas for multivariate Gaussian untruncated product absolute moments; an author-uploaded preprint is publicly available.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/gaussian-magnitude-renyi2-total-correlation--4eebefe6d8fe — Earlier SCOPE record containing the exact magnitude Rényi-2 theorem and weak-correlation expansion.

    ## Limitations

    - The repaired theorem is fixed-dimensional and local near independence.
- General absolute-product-moment series are prior art and are not claimed as new.
- The residual originality claim is deliberately narrow and remains subject to unindexed specialized coefficient extractions.

    This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
