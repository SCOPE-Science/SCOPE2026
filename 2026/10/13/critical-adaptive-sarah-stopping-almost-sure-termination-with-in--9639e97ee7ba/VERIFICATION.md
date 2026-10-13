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

# Reproducibility and boundaries

Execute `python3 verify.py` from the extracted package. It requires only the Python 3 standard library (`fractions`, `itertools`, `math`). The verifier tests 201 exact rational identities and finite path enumerations. In particular, it checks the explicit rare-event stopped output through 59 upward-step counts, Catalan first hits through 15 steps, finite-cap path bounds through 13 sampled steps, and exact full-gradient contraction.

The mathematical claims of almost-sure hitting, infinite expected stopping time, and infinite second moment come from the analytic Catalan formula and countably many disjoint positive-probability events, **not** finite enumeration. A failed, timed-out, or incomplete enumeration cannot establish an infinite-horizon impossibility claim.

The original published SARAH+ routine enforces a finite maximum number of inner steps. The infinite-work assertion pertains **only** to the rule with that cap removed; for a finite cap the finding gives a lower bound on risk, not infinite risk.

Independent audit has not been performed.
