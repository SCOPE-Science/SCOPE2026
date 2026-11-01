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

# Verification and reproducibility

The analytical certificate consists of the exact polar reduction, forced radial derivative data, the sign classification of the unique affine interpolant, and a globally nonvanishing same-sign sum of squares at the prescribed nodes. Together these steps prove the full parameter classification without a finite enumeration.

Run `python3 verify.py` from the directory containing this document. The executable uses only Python's standard library. It constructs the relevant polynomials with exact rational coefficients, checks degrees, interpolation values, and radial derivatives, and verifies for an explicit witness that degree seven forces an extraneous positive circle while degree nine realizes the two requested transverse logarithmic multipliers. The execution returned:

`PASS: exact interpolants, degree 5/7/9 examples, positive angular speeds, Floquet logs, and forced extra root`

Finite grid positivity checks are illustrations only; the universal positivity assertions follow from the algebraic identity expressing the cardinal polynomials as a partition of unity and the equal-sign sum-of-squares construction. The checker does not establish historical originality, independently audit the proof, or certify degrees for arbitrary real input data. Those questions are addressed, respectively, by source comparison and the symbolic arguments in the mathematical result.
