---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 checker.py` from the package directory. Direct binary-bit counts and independently generated signed Rudin–Shapiro blocks agree for ranks 2–14. For each such rank, all circular cuts were enumerated using direct length-one and length-two occurrence counts in both halves; the observed cut set exactly matches the asserted formula. The checker also tests the signed block-sum and boundary-sign identities.

The infinite-rank theorem is established by the block-recursive argument in RESULT.md, not extrapolated from finite checks. No independent mathematical audit has been performed. The verification does not address higher-order Abelian equivalence or arbitrary prefix lengths.
