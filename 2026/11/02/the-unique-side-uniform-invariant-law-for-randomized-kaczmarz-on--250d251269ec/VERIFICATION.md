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

# Verification of the geometric stationary law

The theorem is established by the two-interval density identity on every side of an acute triangle, together with an independent two-step synchronous-projection contraction. These are infinite mathematical statements and do not depend on finite enumeration.

The reproducible exact arithmetic checker is `verification/check_triangle_stationary.py` (Python with SymPy). Run `python verification/check_triangle_stationary.py` from the package root. It checks the rational acute triangles \((0,0),(4,0),(1,2)\) and \((0,0),(5,0),(2,3)\): twelve exact incoming-density constraints and 72 exact stationary polynomial moments through total degree seven. Its expected final output is `ALL PASSED: 12 exact density constraints and 72 exact polynomial Markov identities`.

This check does not substitute for the arbitrary-triangle proof or establish publication priority. It also does not test or guarantee finite-precision numerical implementation, extension to obtuse triangles, or an optimal contraction coefficient. No independent scientific audit has been performed.
