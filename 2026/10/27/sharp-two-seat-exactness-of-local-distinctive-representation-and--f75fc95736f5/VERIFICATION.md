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
# Verification instructions

Run `python3 verify_local_dr_threshold.py` with the standard Python library. It checks all profile combinations for \(1\le n\le4\), \(2\le m\le4\), \(k\in\{1,2\}\) when DR exists, a total of 149,848 checks; all three-seat four-candidate profiles with up to four voters; and the explicit three-voter five-candidate interval witness. It computes JR from uncovered supporters and the full admissible-swap condition of Definition 27. The result is `EXACT VERIFICATION PASSED`.

The numerical runs are corroboration. The proof for arbitrarily many voters and candidates depends on the two-seat insertion lemma, the quota-seat replacement case split, and single-exchange adjacency with one extra candidate. No independent human/third-party audit has been performed.
