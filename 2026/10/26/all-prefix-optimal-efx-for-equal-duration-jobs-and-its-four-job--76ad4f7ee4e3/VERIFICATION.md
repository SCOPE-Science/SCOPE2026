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
# Reproduction

The mathematical proof in `RESULT.md` gives the universal claims. Run `python check.py` using Python 3.10 or later and the standard library. The checker enumerates 19,305 equal-length scheduling inputs (one to three machines, up to eight intervals, integer starts from 0 through 6, duration 3); it searches all subsets for the best unconstrained scheduling cardinality. It verifies feasibility and EFX load balance of the cyclic algorithm at every arrival.

For the instability witness, the checker uses exact `Fraction` arithmetic at four nonzero perturbations, enumerating all three-way assignments (two machines or rejected) of four intervals and confirming the unrestricted maximum of four versus the EFX maximum of three. It also enumerates all cases with at most three jobs over a small integer-endpoint grid, finding equal fair and unrestricted optima in all 455.

Actual successful execution produced:

```
equal_length_exhaustive_instances 19305
exact_fractional_perturbations 4 max_unrestricted 4 max_ef1 3
three_job_minimality_checks 455
```

Finite enumeration does not establish the theorem for arbitrary input sizes, real intervals, or arbitrary positive duration spreads; those assertions follow from the exchange, cyclic-feasibility, and parametric-witness arguments. Independent audit is not performed.
