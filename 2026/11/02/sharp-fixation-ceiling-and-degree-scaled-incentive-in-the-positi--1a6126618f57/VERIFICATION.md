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

The analytical proof reduces the finite Markov chain to two scalar harmonic recurrences and verifies explicit formulae at every admissible state. Independent symbolic checks simplify the transition identities, boundary values, rational closed form, strong-bias square identity, and degree-scaled limit to zero. A separate exact-rational absorbing-chain solver checks 28 full transient matrices (7 star sizes, 4 incentive levels), not merely trajectories. Run `python verification/star_check.py` with Python 3.10+ and SymPy installed. Computations support the stated algebra but do not replace the arbitrary-size argument. Only self-review is recorded; independent assessment is not performed.
