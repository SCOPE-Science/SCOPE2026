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

The analytical proof in RESULT.md uses a Perron-root cubic to verify resolvent convergence, four exact Katz recursions to separate seed rankings, and all-time clipping bounds for the nonlinear dynamics. The bundled `check.py` performs exact rational tests for \(k=4,8,16,32\) and checks 48 discounted iterations of each of three seed types. The code does not certify infinitely many values of \(k\) or infinite time; those quantifiers are proved symbolically in RESULT.md. The full source model was compared via its open-access HTML text, equations (2), (7), (16), Theorem 6, and the numerical comparison sections. Independent external review and validation have not been performed.
