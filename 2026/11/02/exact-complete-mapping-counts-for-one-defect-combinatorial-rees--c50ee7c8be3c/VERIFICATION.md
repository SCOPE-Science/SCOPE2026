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

# Reproducible verification

Run `python3 verify_complete_maps_missing_edge.py` using the standard library. The script enumerates all bijections of the nonzero elements and tests the **original** semigroup product, not merely a derived set of permutation constraints. It checks full and single-zero sandwich patterns at \((m,n)=(2,2),(2,3),(3,2),(3,3)\). The observed single-zero counts are \(2,48,48,9984\); corresponding full-support counts are \(16,288,288,46656\). All equality assertions passed and the checker printed `VERIFY_OK`.

The exhaustive tests cover only these four finite parameter pairs. The theorem for arbitrary \(m,n\ge2\) and the \(e^{-1}\) limit require the symbolic permutation-bijection and inclusion-exclusion proof given in `RESULT.md`. No independent audit has been performed.
