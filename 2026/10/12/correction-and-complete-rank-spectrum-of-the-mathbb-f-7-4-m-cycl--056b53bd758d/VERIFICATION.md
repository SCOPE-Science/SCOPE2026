---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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
`python3 artifacts/verify.py` checks the primitive-order obstruction and the quartic degree via Frobenius, verifies the identity for \(\alpha^2\), and enumerates all 2402 projective messages using the basis \(g,xg\) of the actual cyclic ideal. Each representative is tested at the two roots \(1,\alpha\) to ensure code membership. Modular elimination gives projective counts 1, 49 and 2352 at ranks 1, 2 and 3. Scaling by the 2400 nonzero scalars per line gives the ordinary enumerator. The analytical proof in `RESULT.md` independently derives the spectrum via the quadratic subfield and proves the generalized weights.
