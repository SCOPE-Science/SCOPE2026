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

Exact independent polynomial multiplication, monic Euclidean-gcd calculations and direct collision enumeration reproduce the formula for all degree pairs in fields of sizes 2, 3, 4, and 5 at the cutoff ranges specified in RESULT.md. For the four-element field, the verifier implements an explicit irreducible quadratic representation. Rational-arithmetic computations also reproduce the finite-degree total-variation bound and scalar energy formula, including higher cutoffs. See checker.py and checker_output.txt for the reproducible program and output.

No finite computation certifies the formulas for all fields or all degrees. The general proof is the unique coprime-factor parametrization, polynomial Möbius inversion, and normalized-mass comparison in RESULT.md. The full relevant motivating source was read and compared; complete historical novelty is not independently certified.
