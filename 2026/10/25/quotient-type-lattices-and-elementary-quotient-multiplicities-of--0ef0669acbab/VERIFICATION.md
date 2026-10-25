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

The standard-library-only `check_quotients.py` builds generalized-dihedral multiplication tables, enumerates all subgroups by closure, tests normality by direct conjugation and evaluates elementary quotient exponents. For thirteen finite abelian kernels, its counts match the Gaussian-binomial theorem, and it verifies that normal subgroups meeting reflections always give elementary abelian quotients. Run `python3 check_quotients.py` and check for `VERIFY_OK`.

These are bounded exact tests, not exhaustive over all finite abelian groups. The unrestricted assertions are established by the four-part proof in `RESULT.md`. No independent mathematical audit has been performed.
