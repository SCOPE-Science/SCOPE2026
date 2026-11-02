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

# Verification of the factorization-delay law

Run `python verify.py` using Python 3 and SymPy. The verifier completely enumerates all monic irreducible inputs for nine tested pairs \((q,n)\) over prime fields, factors their Cohen transforms, checks that the two factors have the predicted degrees and are distinct, and verifies both branches' valuation-stage transitions. All \(315\) tested irreducibles agree with the Möbius count histogram; no Monte Carlo sampling is used in these checks. It also checks the exact integer formulas on \(144\) further parameter pairs for proper prime powers \(q\), without claiming to factor polynomials over those extension fields.

Actual output includes:

```
p=3,n=2,e=3,irreducibles=3,counts_by_splits=[2, 1, 0, 0],mean=1/3
p=3,n=3,e=1,irreducibles=8,counts_by_splits=[4, 4],mean=8/8
p=3,n=4,e=4,irreducibles=18,counts_by_splits=[10, 4, 2, 1, 1],mean=16/18
p=5,n=3,e=2,irreducibles=40,counts_by_splits=[20, 10, 10],mean=40/40
CHECK_OK total_irreducibles=315, complete_finite_field_polynomial_factorizations=1, random_branch_transition_certificates=1
PRIME_POWER_ARITHMETIC_OK parameter_pairs= 144
```

The program is a finite corroboration, not an exhaustive proof over all field sizes. The unrestricted assertions follow from cyclic-group structure, finite-field Frobenius orbit counting, and exact divisor sums in `RESULT.md`. No independent mathematical audit or external certification has been performed.
