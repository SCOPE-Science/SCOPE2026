---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Fresh independent enumeration checked every perfect matching for stability in all 16 two-by-two and 46656 three-by-three profiles. It reproduced the stable-count marginal 34080, 11484 and 1092, and the exact relation histogram 42756 equality, 2928 strict rank-maximal subset of egalitarian, and 972 disjoint. The package verifier independently uses duplicate stability and objective formulations, and the displayed witness has the stated two stable matchings, profiles and costs.

## originality

PASS

The literature defines and optimizes both fairness criteria and Cooper–Manlove compare rank-maximal matchings empirically against egalitarian cost, but the inspected complete paper does not give the sharp first-market boundary or the exact three-by-three optimum-set relation census. Resultary searches did not surface an equivalent table or theorem.

## value

PASS

Rank-maximality and egalitarian cost encode two standard but different fairness goals. Determining their sharp first conflict market and the complete relation structure, including the exact disjoint probability \(1/48\), is a natural finite boundary classification rather than an arbitrary small-instance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
