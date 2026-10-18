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

# Reproduction and limits

Run `python verify_direct.py` and `python verify_quotient.py` with Python 3.11 or later and no third-party packages. The corresponding captured outputs, `verify_direct.out` and `verify_quotient.out`, record successful finite checks. The direct check constructs the full symplectic disjointness graphs over the binary field for ranks two through four; it does not use the claimed closed quotient formulas. The quotient check derives its own integer intersection table by Gaussian-moment inversion, checks undirected edge balance and the promised odd/even stable classes for 35 combinations, and separately enumerates symmetric matrices over the prime fields of orders two and three. This is stronger than merely printing expected expressions but remains finite corroboration.

The all-rank, all-prime-power claim is based on the explicit graph parametrization, characteristic-independent nonsingular symmetric-form recurrence, parity-cancellation lemma, and round-count argument in `RESULT.md`. No infinite exhaustive search, mechanized proof certificate, or independent scientific validation is asserted.
