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

Reproduce with `python verify_root_triangle.py` using Python 3 and its standard library only. The saddle section computes the positive Lambert inverse with Newton iteration. Executing the script in this research package passed 99 assertions. The graph-enumeration section counts all labeled graphs on 3 to 6 vertices for probabilities 1/3 and 2/5 and checks the closed rooted-triangle-free degree weights. The numerical section checks conditional mode versus the Lambert-W approximation and the critical log-probability exponent. No central-limit or infinite convergence theorem is certified by these finite tests; analytic arguments appear in RESULT.md.
