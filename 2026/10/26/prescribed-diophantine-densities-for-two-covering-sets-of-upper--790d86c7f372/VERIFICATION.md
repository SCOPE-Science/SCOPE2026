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

# Reproduction and limits

Run `python3 verification.py` from the directory containing the accompanying source. The program uses only the Python standard library and exact integer arithmetic.

It checks five exact rational values of the core parameter, all coprime numerator classes for denominators in the stated finite interval, the partition of positive integers through the first 65,536 values, and finite-stage core counts. It confirms the inequality used in the Dirichlet construction by comparing integer numerators, not floating-point approximations.

Expected result:

`VERIFY_OK rational_dirichlet_checks=102510 integer_partition_checks=65536 exact_fraction_floor_checks=PASS all_finite`

The infinite cardinality bound, the all-real-parameter assertion, and the two asymptotic density equalities are proved in `RESULT.md`. No finite check establishes those universal statements, nor does it establish novelty or independent validation.
