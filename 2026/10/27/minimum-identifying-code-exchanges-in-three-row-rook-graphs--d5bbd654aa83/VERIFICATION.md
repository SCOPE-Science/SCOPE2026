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
# Reproducibility

Run `python3 verify.py` with Python 3.9 or later; it has no external package dependencies. The verifier independently builds graph closed neighborhoods, checks identifying signatures, classifies all minimum sets, computes one-for-one exchange edges in two independent ways, tests regularity and connectedness, and evaluates natural orbit profiles.

All vertex subsets of size at most the predicted optimum were exhausted for \(m=4,5,6,7\), with respective subset totals 1586, 16384, 155382 and 1401292. The minimum code counts were 72, 540, 3240 and 17010. The corresponding exchange edge counts were 216, 3240, 29160 and 204120, with degrees 6, 12, 18 and 24; each graph was connected. The verifier also checked all 81648 predicted optimum configurations at \(m=8\) and all 1224720 exchanges, degree 30, connected. The terminal result was `ALL_VERIFY_OK`.

These are complete finite searches only for the stated finite domains. The all-\(m\) proof is the combinatorial argument in `RESULT.md`, not a computational extrapolation. Rechecking from the delivered package can detect transport or encoding errors, but does not amount to an independent scientific audit.
