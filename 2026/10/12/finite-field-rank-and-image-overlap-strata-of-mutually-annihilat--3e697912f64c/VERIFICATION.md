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

Run `python3 verify.py` using Python 3 standard library. It constructs every square-zero matrix in each tested finite field and dimension, checks all ordered pairs for the four annihilation equations, and computes the three invariant parameters directly. It independently evaluates the Gaussian product formula and asserts equality of the complete frequency dictionaries.

Tested cases: `(n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)`. Respectively the total ordered pairs are `10,33,76,148,1665,8296`. The extension-field test uses polynomial arithmetic modulo `t*t+t+1` over `F_2`, not integer arithmetic modulo `4`.

Expected output concludes with `VERIFY_OK`. The result is an exhaustive check only at these finite sizes. The proof of the formula for every dimension and finite field is the subspace-and-surjection bijection in `RESULT.md`; no finite computation is interpreted as establishing an infinite statement. The checker supplies no orbit enumeration, component classification, or proof of bibliographic priority.
