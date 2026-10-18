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

The analytic proof derives the Stieltjes density from the cut of a fractional-power generating function, proves probability normalization and strict complete monotonicity, and then applies the renewal regeneration identity. It proves the large-time coefficient asymptotic by the small-variable behavior of the positive mixing density. Run `python verification.py` with Python 3 and mpmath to reproduce 436 numerical consistency checks. These finite checks do not establish any infinite-limit or novelty claim. Independent audit has not been performed.
