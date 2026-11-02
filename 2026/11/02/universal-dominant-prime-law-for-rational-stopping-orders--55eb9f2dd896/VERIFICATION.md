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

# Reproducibility and limitations

Run `python3 verify.py` with Python 3 and SymPy. All checks use exact integers, fractions, polynomial rational functions, and unrounded comparisons. The program separately verifies cancellations of the dominant pole for 29 composite denominators, checks prime-power exact-order distributions against the recursive formula in 510 instances, and directly iterates the original map over complete residue periods in 15 finite cases. The expected terminal line is:

`VERIFY_OK symbolic_pole_cancellations=29 divisor_recurrence_primepower_cases=510 direct_orbit_cases=15 exact_arithmetic=yes`

The direct iteration checks only orders one through three for a finite set of denominators. Neither those checks nor symbolic examples are a proof of the universal statement. The full divisor-inductive proof and an exact bound on the locations of all remaining poles appear in `RESULT.md`. The underlying divisor recurrence and the prime-power case are independently established in Carvalho (2026); the analytic cancellation argument is supplied here. No independent mathematical audit has been performed.
