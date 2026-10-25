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

# Verification

The independent Python standard-library script `dihedral_three_verifier.py` constructs \(D_n\) via exact integer pairs, enumerates each three-element subset, computes \(AA\) and \(AA^{-1}\) without using the analytic classification, and compares every discrepancy count and every number-of-rotations stratum against the theorem's closed formulas. Running `python dihedral_three_verifier.py` returns `VERIFY_OK n=3..36` and checks that the table totals \(\binom{2n}{3}\) for each tested \(n\).

The argument in RESULT.md supplies the complete all-\(n\) proof; finite enumeration validates the code and small cases only. No independent audit or external validation has been performed. The literature comparison concerns known, materially inspected text and cannot rule out all unpublished or unindexed work.
