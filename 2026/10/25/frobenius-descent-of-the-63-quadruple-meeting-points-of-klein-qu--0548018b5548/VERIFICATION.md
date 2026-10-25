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

# Finite exhaustive verification

Execute `python3 verify.py`; it uses Python standard-library exact arithmetic only. The verifier constructs F27 and F729 via irreducible quotient polynomials, confirms all 28 roots of the hyperflex polynomial, calculates 28 distinct tangent lines, inspects all 378 unordered pairs, checks each of 63 distinct intersection points is incident with exactly four lines and lies off the quartic, and determines Frobenius orbits of both schemes. Its assertions demand the exact cycle-type counts, and failure raises an exception.

Expected success line: `VERIFY_OK: bitangents 1+3+4*6; quadruple intersections 3*3+9*6`.

The 28-root algebraic parametrization, the polynomial factorization, and the ambient field size establish that this finite calculation is exhaustive for this specific problem. The computation does not establish priority or test every twist of the quartic. The mathematical argument and checking program are available for independent scrutiny; no independent audit was conducted.
