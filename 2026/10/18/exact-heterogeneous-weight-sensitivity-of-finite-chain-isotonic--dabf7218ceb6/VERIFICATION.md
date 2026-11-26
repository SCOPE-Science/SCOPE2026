---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed RESULT.md (1)–(6) for a fixed positive diagonal quadratic objective and ordinary data/output ℓ_p norms. At each input, stationary variation of each strictly separated maximal fitted level gives its weighted average. The continuous fit is a selection of finitely many linear partition maps; restricted to a segment their affine traces can cross only at finitely many points except for identical traces. The slope bound thus gives the global upper bound. For any chosen block, strictly decreasing block data give strictly positive weighted prefix residual sums relative to the full mean; strictly increasing and separated outside coordinates give strict fitted gaps. The KKT conditions then realize that partition throughout a neighborhood. A Hölder extremizer attains the block operator norm there, including a maximum-weight coordinate at p=1 and the constant direction at p=∞. Singletons and n=1 give 1; every unequal adjacent pair gives strict amplification for finite p. For fixed block size, the derivative with respect to one weight has sign B t^(q−1)−A, so an endpoint maximizer exists; for p=1 the optimum has one maximal weight and the largest allowable block. For interior p the endpoint profiles reduce to the fraction r/k. The nested grids become dense, and the affine derivative sign gives the stated unique scalar maximizer and value. This also verifies the κ=1 cases in the finite formulas. The supplied floating-point witness and envelope script was inspected, not rerun; it is not a universal certificate.

## originality

PASS

The distinct supported claim is the exact heterogeneous fixed-objective global sensitivity and its sharp finite contrast envelope. Block means and scalar reverse-Hölder/Kantorovich bounds are not new. The strongest inspected sources do not yield the matching upper bound and all-block realization for this fixed heterogeneous map in ordinary ℓ_p, or its discrete contrast envelope; the argument uses both facts. This is a best-of-knowledge comparison, not a claim of priority for the scalar limit in isolation.

## value

PASS

The exact finite modulus directly quantifies how heteroscedastic objective weights can amplify an ordinary data perturbation despite Hilbert-space nonexpansiveness in the weighted norm. It identifies realizable worst blocks, separates ℓ∞ from all finite p, and gives sharp finite-size design bounds from contrast alone rather than only a norm-equivalence bound or an asymptotic inequality. The finite fraction restriction can change the exact guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
