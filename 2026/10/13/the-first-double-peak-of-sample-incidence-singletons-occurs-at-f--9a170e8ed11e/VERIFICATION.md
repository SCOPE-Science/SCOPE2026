---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For a species with occupancy d, exactly d*C(N−d,k−1) of C(N,k) k-site samples contain it once, giving g_d(k). Linearity yields u_k=g_a(k)+g_b(k) even when species supports overlap. The ratio g_d(k+1)/g_d(k) has sign of difference controlled by N+1−d(k+1), proving single-species unimodality. Independently enumerated every N=2..15 and every 1<=a<=b<=N, exactly 679 occupancy triples, with exact rational fractions and strict interior peak tests; exactly one double-peak case N15 (2,9) with peaks at k=2,7. Rechecked witness fractions and distinct neighboring comparisons. Separately inspected full Git verify.py that additionally enumerates all 2^15 site subsets for both disjoint/nested representations. The finite census is exhaustive for the stated finite parameter domain, not a numerical extrapolation. u_k/k nonincreasing is separately justified via hypergeometric avoidance probability and is not claimed novel.

## originality

PASS

The 2001 hypergeometric expectation formula and later normalized incidence novelty rate are prior results. The new object is a sharp complete finite first-bimodality/unique-witness classification for the raw unnormalized expected singleton curve; neither the original formula nor monotonicity of u_k/k supplies this threshold without genuinely exhaustive parameter comparison.

## value

PASS

The smallest possible double peak in the expected singleton-frequency curve is a natural strict-unimodality boundary in incidence rarefaction, identifying the first resource size and a unique occupancy obstruction. The effect need not be empirically large to be an exact useful structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
