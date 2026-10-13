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

# Verification and limits

The full proof reconstructs the conditional label probabilities, both martingales, the memory normalization, the alternating correction, the predictable quadratic variation, and the conditional-on-finite-history mixing argument. The covariance is projected onto the memory martingale and its sign is certified for all \(1/2<q<1\) by a positive recurrence and an alternating-series pairing, not by numerical evidence.

To replay finite identities, run `python elephant_joint_checker.py` with Python 3 and no dependencies. It enumerates all histories through length ten at four exact rational persistence parameters and verifies the pathwise decomposition, joint moment recursions, and cross-covariance projection; expected output is `EXACT_CHECKS_PASS 28712`. The finite checker is supplementary and does not establish any continuum limit. The martingale functional central limit theorem is used in its standard bounded-jump and deterministic-bracket form. No independent review or formal certificate was performed.
