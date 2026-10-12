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
# Verification

Execute `python artifacts/verify.py` with a standard Python 3 interpreter. No third-party packages are required.

The checker independently constructs ordinary Möbius values by a linear sieve, the square-splitting function from its local prime-power rules, and the same function from the square-divisor Dirichlet-convolution formula. All three paths agree for \(1\le n\le400000\). It verifies the fourth-power-free support identity for the same range, and validates **146** exact finite progression support counts with an independent CRT-based inclusion-exclusion calculation over moduli \(1,2,3,4,6,8,9,12,16,24,25,36\). The program additionally checks representative local Euler-product factors, numerical limits, and structurally forbidden classes.

The packaged replay begins with:

`VERIFY_OK limit=400000 class_tests=146 mobius_convolution=yes fourth_power_free=yes crt_exact_counts=yes local_product_values=yes`

The infinite sign equidistribution comes from the unconditional prime number theorem in arithmetic progressions plus the proved finite reduction, not from running the finite checker. There is no claimed signed discrepancy exponent or uniformity as the modulus grows.
