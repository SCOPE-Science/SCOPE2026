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

# Reproducibility and scope

Run `python3 verify.py` in a Python 3 environment. It uses no third-party packages.

The certificate enumerates all 3-by-3 integer contingency matrices with margins \((d,d,d)\) and \((d,d-1,d-1)\) for \(1\le d\le10\); the observed counts agree with both closed formulas. It also enumerates actual ordered triples of monic polynomial factors over small prime fields, computes the product-multiplicity square sum, and checks the exact degree-one polynomial \(6q^3-9q^2+4q\).

The general claim is a formal generating-function theorem, not a computational extrapolation. Calculations with a finite set of degrees and fields are supplementary consistency checks only. A separate independent audit has not been performed.
