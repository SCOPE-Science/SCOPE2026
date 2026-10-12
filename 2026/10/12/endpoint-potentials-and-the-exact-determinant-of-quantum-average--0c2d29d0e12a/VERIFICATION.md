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

# Verification of the endpoint-potential mixing identity

The exact symbolic verifier is `verify.py` (requires Python 3 and `sympy>=1.12`). Run `python3 verify.py` from the same directory as the script. The checker constructs a rational Hamiltonian for each instance, computes its traces of powers, and forms \(VG^{-1}V^{\mathsf T}\), where \(V\) comprises diagonals of powers and \(G\) is their trace Gram matrix. This is an exact reconstruction of the Cesàro mixing matrix, independent of numerical eigenvalue approximations.

Checks include 48 instances, orders \(2,3,4,5,6,7\), both unit and varying positive integer couplings, potentials \(0,1,-1,1/2\); a total of 1,112 matrix entries. For each, the code verifies Gram invertibility, mixing-matrix symmetry, exact unit row sums, the claimed rank, positive characteristic discriminant and the exact closed determinant formula.

Observed output:

```text
VERIFY_OK exact_cases=48 exact_mixing_entries=1112 orders=2..7 including_zero_and_signed_field
```

This finite experiment is not an exhaustive check of arbitrary real couplings or all graph orders. The all-order assertions rely on the Vandermonde/resultant argument in `RESULT.md`; the determinant formula must not be inferred merely from this check.
