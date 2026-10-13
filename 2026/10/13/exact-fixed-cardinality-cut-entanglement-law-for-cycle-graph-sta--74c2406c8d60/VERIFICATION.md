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

# Verification of the cycle entanglement enumerator

Run `python3 verify_cycle_entanglement.py` with Python 3.8 or newer; there are no external dependencies. The program independently constructs the bivariate four-state transfer polynomial and, for every cycle with \(3\le n\le15\), enumerates all \(2^n\) vertex subsets and determines each binary cut-matrix rank by exact Gaussian elimination. It checks every pair of subset size and rank, cardinality totals, cut-complement symmetry, and the stated unrestricted-cut mean. For the balanced \(C_{12}\) case, the exact counts \((12,96,306,386,124)\) at ranks \(2,3,4,5,6\) are reproduced and the associated Shannon entropy is checked to numerical tolerance. The command completed successfully with the line:

`VERIFY_OK: cycles n=3..15; every subset size and rank; C12 balanced histogram (12,96,306,386,124).`

The all-\(n\) polynomial identity, correction of the all-crossing cycle, and central limit theorem are justified analytically in `RESULT.md`. These exact finite tests do not certify results for sizes above fifteen by enumeration and do not constitute external independent validation.
