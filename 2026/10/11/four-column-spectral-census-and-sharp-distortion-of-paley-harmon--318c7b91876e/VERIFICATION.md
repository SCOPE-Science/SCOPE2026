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

# Verification evidence and limits
The supplied `check_paley4.py` is a standalone reproducibility check, executed using Python 3, SymPy 1.14.0 and NumPy 2.3.5. It symbolically evaluates all four canonical characteristic polynomials and polynomial-comparison identities. It separately forms the true complex Fourier Gram matrices and tests all 13,096 unordered four-column subsets of the prime cases 7, 11, 19 and 23, classifies their tournaments and checks census formulas. The last successful run printed `VERIFY_OK exact_symbolic_characteristic_polynomials_and_comparison_identites=PASS exhaustive_4subsets= 13096 primes=[7,11,19,23] counts=PASS`. It establishes reproducibility for these computations, not a separate independent audit or a computer-only proof for infinitely many primes. The unrestricted theorem follows from the analytic finite-field Gauss-sum, double-regularity counting, symbolic four-vertex determinant identities, root comparisons and simple-root asymptotics presented in the RESULT.
