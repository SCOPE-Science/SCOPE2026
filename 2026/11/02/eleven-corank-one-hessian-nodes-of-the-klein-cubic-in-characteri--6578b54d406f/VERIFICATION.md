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
# Exact verification and limitations

Running `python3 verify.py` with the dependency in `requirements.txt` produced the stored `verification_output.txt` ending in `VERIFY_OK`. The checker computes the Hessian determinant, rank at the diagonal point, quadratic tangent cone and nonzero discriminant, checks the diagonal symmetry exponents and factorization of the eleventh-root polynomial over the prime field. The all-geometric-point classification uses the proof in `RESULT.md` based on adjugate derivatives and cubic polarization; direct finite-field enumeration is neither required nor claimed as complete. The classification is limited to Hessian matrix rank exactly four, and it does not compute the remaining lower-rank singular locus. No independent audit has been performed.
