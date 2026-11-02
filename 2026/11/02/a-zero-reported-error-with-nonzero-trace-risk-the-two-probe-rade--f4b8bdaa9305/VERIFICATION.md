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

The result is established analytically by expanding the two leave-one-out rank-one projectors and using orthogonality of degree-two Walsh characters. The rank classification follows from pairwise coefficient vanishing. `verify.py` is an exact-rational finite cross-check and does not replace the proof.

Run `python verify.py` with a standard Python installation. It requires no third-party packages. Expected output: `VERIFY_OK 7168 exhaustive ordered probe pairs; exact mean, variance, equality, and classification checks`.

Scientific limits: real nonzero diagonal matrices; exactly two independent Rademacher test vectors; unnormalized original XTrace with its two-term internal squared-error statistic; exact arithmetic. No independent scientific audit has been performed.
