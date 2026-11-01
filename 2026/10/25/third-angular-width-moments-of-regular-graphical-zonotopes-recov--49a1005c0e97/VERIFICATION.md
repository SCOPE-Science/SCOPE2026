---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Independent reconstruction of the Gaussian-to-sphere radius factor Γ((n−1)/2)/Γ((n+2)/2) and joint cumulant expansion confirms that only repeated-edge terms and three connected three-edge motifs (path, star, triangle) contribute. The path count is Σ_{ij∈E}(d_i−1)(d_j−1)−3t; under d-regularity m,w,s and p+3t are fixed. The triangle contrast coefficient δ=k_T−3k_P≈−0.0768578615748493 is strictly negative by the stated analytic rational upper-bound certificate. Independent 750000 Gaussian-draw witness comparing triangular prism and K_{3,3} gave a third-cumulant difference −0.8383 versus analytical prediction −0.922294, a finite sampling corroboration, not an exact proof. Exact finite checks in the actual package cover 141 connected graphs through six vertices; the universal result follows from the cumulant classification and trivariate Gaussian integral, not those runs.

## originality

PASS

Classical Nabeya Gaussian trivariate absolute moments and Padrol–Pilaud–Poullot graphical-zonotope structural theory are inputs; the separate published second-width-moment variance theorem cannot recover triangle counts between regular graphs of equal order/degree. No covering full third-moment motif theorem was identified in the searched primary studies. Residual equivalence with older Gaussian graph-total-variation cumulant formulas remains.

## value

PASS

A third angular moment differentiates connected regular graphs invisible to the first two width moments; the triangular prism and K3,3 give a concrete sharp witness. The motif formula is an exact graph-geometric invariant with a natural statistical interpretation, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
