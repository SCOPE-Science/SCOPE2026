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

Run `python3 verification_pair_impurities.py`. Python 3 standard library only.

Actual execution passed 33 rank-distribution comparisons, 409104 direct arrival-priority-order evaluations, 21 paired-seed finite comparisons, and 16 integral/sign/bound checks; the checker also compares exact rational path means with the independently evaluated first-arrival recurrence. Cases cover cycles of lengths four through nine, and integral checks cover separations three through eighteen. The proof in RESULT.md supplies the all-size justification.

No independent third-party verification has been performed. The code is a finite sanity check and not a proof for arbitrarily large cycles.
