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

The length-ℓ difference encoding is injective: reconstruct successively from the first ℓ letters. A duplication is a block of ℓ inserted zeros in the differences. Two cuts give identical results exactly when the intervening segment commutes with the inserted zero block, which holds exactly when that segment is all zeros. Thus B_ℓ−1 is the count of mismatches on distance-ℓ edges. Appending a symbol to an equal last pair gives weights 1 or xy with multiplicities 1 and q−1; from a different pair the weights are y, x, and xy with multiplicities 1, 1, and q−2. The initial pair and final state sum prove the exact polynomial including n=2. Each distance separately gives a forest, and any pair of edges of different distances is also acyclic; independent uniform labels give independent inequalities on a forest. This proves the binomial margins and zero covariance, but the positive-probability constant-word event forces B₂=1, disproving independence for n≥3. For the conditional mean, the k changed adjacent edges are a uniform k-subset; one change over two consecutive edges forces a distance-two mismatch and two changes do so with probability (q−2)/(q−1). These yield the stated mean and, with disjoint channel output lengths, the moments of S. For q≥3 all distance-one and distance-two constraints are simultaneously sharp exactly when a new letter avoids both preceding letters. For q=2 the derivative-bit objective has edge reward 3/2 for alternation, 1 for 11, 0 for 00, and endpoint reward (e₁+e_L)/2. At odd L=n−1 the unique optimum derivative alternates with endpoints 1; at even L the only possible half-unit loss comes from perfect alternation with one zero endpoint or one 11 edge at an odd edge position with endpoints 1. This gives the maxima and multiplicities, also at L=1. Independently generated literal descendant sets for 3732 words across 19 parameter pairs (q=2 through n=8, q=3 through n=6, q=4 through n=5, q=5 through n=4, each starting at n=2) checked joint coefficients, extrema, covariance and conditional means; replay: python3 /workspace/branches/c3e2dd81-0379-4d04-95f8-485b064be96b/bounded_reproduction.py. The supplied script was inspected, not executed; the finite check is corroboration.

## originality

PASS

The supported distinct contribution is the all-n mixed joint enumerator, conditional mean and sharp combined-channel extrema, not the fixed-length difference transform or marginal counts. The strongest related indexed law agrees on several statistics, and gives the joint law in the small regime, but not the frozen all-size spectrum or its sharp extremes.

## value

PASS

When two allowed duplication lengths coexist, the disjoint output lengths make their sum a natural ambiguity measure but do not remove source-level correlation. The full two-state enumerator gives exact joint counts, exposes nonlinear conditional dependence hidden by zero covariance, and explains why the maximum changes regime for a binary alphabet, including the parity-sensitive number of extremizers. These are useful refinements beyond the separately known fixed-length transform.

The dated certificate retains the supplied scientific assessment, sources and limitations.
