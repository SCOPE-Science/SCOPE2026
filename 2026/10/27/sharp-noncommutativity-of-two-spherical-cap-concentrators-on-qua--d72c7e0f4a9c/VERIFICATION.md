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

# Reproduction and mathematical limits

Execute `python verify_two_caps.py` using Python 3 with SymPy installed. The script checks spherical probability-density normalizations and their integrated differences; verifies the real five-dimensional rotation matrix modulo the unit-circle identity; compares squared entries of the resulting commutator with the two stated sector formulas; and constructs an exact rational Bernstein certificate for strict positivity of the polynomial measuring the gap between the sharp squared constant and the competing sector.

The exact certificate has 17 visited dyadic nodes and 9 accepted boxes; its minimal leaf coefficient exceeds \(1/40000\). The two-dimensional sector reaches \(9/250\) at thresholds \(1/\sqrt5\) and squared axis overlap \(1/2\). Every assertion uses symbolic or exact rational arithmetic rather than random sampling.

A Bernstein basis on a compact box consists of nonnegative partition-of-unity functions, so positivity of every exact coefficient is an all-parameter proof. The checker does not establish that the result is absent from every historical publication; comparison with prior literature is a separate scientific question. No human or independent verification is claimed.
