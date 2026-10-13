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
# Reproduction and scope of checking

Run `python verify_crossing.py` with Python 3 (standard library only). The script was actually run on the included bytes and printed `VERIFY_OK 5011 crossing pairs, 12000 physical-state trials; four exact rational bath cases`.

Exact Fraction assertions cover one pair of bona fide mixed qubit inputs at four distinct thermal biases and check the inverse quadratic identity, both crossing-time inversions, nonnegative square-root branch, and normalization. A fixed-seed 12,000-case numerical sweep checks the closed-form crossing work and time, opposite-time strict orderings, and the no-crossing boundary at six values of the decay factor; the script also checks thermal-bias monotonicity. The numerical sweep cannot establish uniqueness or universality, which instead follow from the written analytic proof.

The public scientific claim is restricted to the shared thermal generalized-amplitude-damping semigroup, nonnegative bath inverse temperature, and physical qubit density matrices. Independent audit has not been performed.
