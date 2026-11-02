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

# Reproduction

Run `python verify.py` using Python 3 and the standard library. The program verifies 32,802 exact integer/rational assertions. Every permutation through length eight is independently enumerated, checking all six pattern probabilities, all total fixed-point covariances, and every site-specific mixed probability; exact combinatorial formulas are additionally checked for all sizes from three through fifty.

# Proof versus finite checking

These tests do not exhaust infinitely many sizes. The all-size proof in RESULT.md is a direct conditional-counting argument and does not rely on a conjectural extrapolation from tests. No statistical simulation or external proof-assistant certificate is used. Independent audit has not been performed.
