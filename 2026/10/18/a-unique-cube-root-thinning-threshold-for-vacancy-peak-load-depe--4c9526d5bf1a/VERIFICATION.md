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

# Reproducibility
The standalone standard-library Python script `verify.py` calculates the actual joint law independently by enumeration of every three-outcome string for each number of potential arrivals \(2\le L\le7\), and compares it using exact rational arithmetic with the derived formula at six probabilities for each size. It also checks central-binomial monotonicity through 69 objects, small-size boundaries, and transition root signs up to 1000 objects.

Run `python3 verify.py` in a Python 3 environment. It must report 273 passed checks. The general proof is analytic and does not depend on exhaustive enumeration being an infinite proof.

Limitations: numerical root brackets are floating-point corroboration, and neither an independent audit nor external scientific certification has occurred.
