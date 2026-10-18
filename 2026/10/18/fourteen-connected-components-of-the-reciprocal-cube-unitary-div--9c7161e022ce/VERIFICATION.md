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

# Reproducing the exact component classification

Run `python3 verify_components.py` (Python 3.8 or newer). No packages beyond Python's standard library are needed. The run should end with `VERIFY_OK`, after printing `COMPONENTS 14` and the exact endpoint pairs.

The checker uses exact rational arithmetic throughout: the zeta constants are enclosed by certified integral-test bounds, and every component union or separation is decided by a strict rational inequality. It verifies both increasing- and decreasing-prime processing and their agreement; it checks that each of the 13 gaps is strictly positive and the final right endpoint equals the full Euler product. This is a finite verification **conditional on** the mathematical infinite-tail interval argument in `RESULT.md`, whose hypothesis is established there analytically from Nagura's theorem, not experimentally.

The scientific verification is self-reviewed only. Independent audit has not been performed. No claim is made about parameters other than the fixed exponent -3.
