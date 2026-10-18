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

# Reproducibility checks

Run `python3 verify_hurwitz.py` with Python 3 and no third-party packages. The program evaluates the complete homogeneous Jacobian system at all projective points over 10 prime fields (the primes at most 29) for each of 15 integers from 2 through 16, giving 150 finite-field comparisons. It verifies exact equality with the singular-point equations and nonvanishing of the quadratic coefficient for bad characteristics. Successful execution prints `VERIFY_OK` and selected sample invariants.

The symbolic mathematical argument in `RESULT.md` proves geometric integrality, the full singular locus, the normalization function field and genus, and each completed local cusp type. Finite-field enumeration does not establish singular points defined only over extension fields, the analytic branch count, or novelty. No independently validated computational or mathematical audit is claimed.
