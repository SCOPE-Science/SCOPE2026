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

The exact return map is derived directly from the original piecewise definition, with the full \(\nu^M\) correction retained. `verify.py` checked the multiplier identity and first-order threshold coefficient using SymPy, and performed 64 high-precision full-orbit tests with mpmath at rational exponents \(1/2\), \(1/3\), \(2/5\) and \(3/7\), for periods \(6\), \(8\), \(12\) and \(40\). Each full trajectory was checked to have one nonlinear branch visit, \(M-1\) strict linear visits, and the appropriate stable/neutral/unstable multiplier classification.

All tests passed when executed in the candidate's own package directory. The analytical proof establishes the infinite family and strict asymptotics; these finite tests do not certify arbitrary exponents or periods. A complete independent mathematical audit has not been performed.
