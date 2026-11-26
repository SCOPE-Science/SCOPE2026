---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the one-spike model the restricted maximizer in K=span(v,W) is ±P_K e/||P_K e|| because the objective on the unit sphere is λ_-+(λ_+−λ_-)|eᵀz|² and the starting overlap is nonzero. Write e=cv+sqrt(1−c²)w with w unit in the tangent space. Orthogonality gives exactly Δ_new/Δ_old=1−||P_Ww||². With a Haar s-plane in dimension m, the complement projection has the law X/(X+Y), for independent X~χ²_(m−s) and Y~χ²_s. For s<m this keeps the gap positive almost surely at each finite step, and overlap cannot vanish. Conditional on the whole past, each ratio law depends only on the chosen deterministic size, proving independence (and identical laws for constant s). The beta integral gives the stated gamma ratio on p>−(m−s)/2; its derivative at zero is the integrable mean log-ratio, so the strong law gives the digamma rate. For s=m the span is all space and the gap vanishes on that step; no ratios are needed after termination. The reduced Gram matrix uses only cached Av and the new forward images, and the next cached image is their linear combination. Therefore the counted cost is exactly Σs_j and expected factors multiply. Replacing a split a,b by a+b removes the positive ab/m² term; all other factors of a genuine split are positive when the total is ≤m. This gives strict uniqueness for a genuine split and the full-budget zero gap. The one-block mean and variance give its proportional-size concentration. As an independent check of the serial limit, the first two moments of a single-direction factor are (m−1)/m and (m−1)(m+1)/(m(m+2)); raising them to s powers for s/m→θ gives e^(−θ) and e^(−2θ), hence L² convergence of the serial product. For s=m−1, the chi-square representation and (X+Y)/m→1 give the stated χ²_1 limit and the serial mean comparison is asymptotic to e/m. The frozen verifier was inspected, not executed; its bounded numerical checks do not supply the universal assertions.

## originality

PASS

Credit the exact all-block adaptive product law with the strict all-partition forward-product comparison, not the already published block algorithm or the standard Haar projection distribution. Prior observations about iteration and runtime performance concern a different cost comparison; the strongest exact catalog match treats a single direction and is later. No inspected earlier source gives the exact state-independent adaptive gap law for every block size and the resulting optimal allocation under this budget.

## value

PASS

Forward applications are a natural cost when the adjoint is unavailable and applying the forward operator is expensive. The result compares all deterministic groupings of a fixed number of such calls in the benchmark one-spike model, not just a simulation against another method. Strict finite-budget dominance and the order-1/m versus order-one gap near a full block give a concrete, interpretable resource separation. The full product laws quantify variability as well as the mean, without assuming a wall-clock advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
