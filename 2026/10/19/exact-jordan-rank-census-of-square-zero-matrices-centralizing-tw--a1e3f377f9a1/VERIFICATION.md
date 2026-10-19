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
# Verification of rank-count formula

The argument is mathematical and valid for every finite field; the checker corroborates small cases without establishing the general theorem by enumeration. Run `python checker.py` with an ordinary Python 3 interpreter from the folder containing this file and the script.

The program computes the right-hand side using exact rational arithmetic, then independently iterates the four entries of \(2\times2\) matrices over \(\mathbb F_q[t]/(t^n)\), multiplies truncated polynomials to test square-zero, builds the associated \(2n\times2n\) linear map and computes its actual \(\mathbb F_q\)-rank by modular Gaussian elimination. The exhaustive cases are \((n,q)=(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(1,5),(2,5)\). It also checks the integer coefficient totals for \(1\le n\le12\) and \(q\in\{2,3,4,5,7,8,9,11\}\), which are formula-only checks, not brute-force extension-field enumeration.

The final success marker is `ALL_EXACT_CHECKS_PASSED`. The executable needs no network, and has no dependencies beyond the Python standard library. No assertion of external or independent audit is made.
