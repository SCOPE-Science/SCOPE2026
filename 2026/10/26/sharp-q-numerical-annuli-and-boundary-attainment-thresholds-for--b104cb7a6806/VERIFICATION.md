---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The proof in `RESULT.md` is analytic. It derives the exact scalar envelope for each overlap, evaluates its unique maximizer, and uses that overlap's presence or absence to decide whether the outer boundary is included. The direct-sum example is checked block by block; a strict weighted-average inequality gives nonattainment of the supremum. The rational-parameter disk checks in `RESULT.md` are illustrative, not a substitute for the proof. The frozen planar sampling script is not used to verify the narrowed higher-dimensional claim.
