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

Run `python3 verify_f2_4_5_9.py` from the directory containing this file. The verifier uses only the Python standard library.

It verifies that the affine generators partition all \(\binom{16}{5}=4368\) five-point supports into orbits of sizes \(1680\) and \(2688\). For each representative it checks all \(\binom{16}{7}=11440\) seven-character zero sets. A rank-five result modulo \(1000003\) proves rank five over the rationals because it exhibits a nonzero integer minor modulo that prime. Every case not certified full-rank in this way is recomputed by exact rational row reduction.

Expected exact census:

- Representative \(\{0,1,2,3,4\}\): \(3248\) rank-deficient sets; ranks \(4\) in \(3200\) cases and \(3\) in \(48\) cases; \(3184\) force a zero time coefficient and the remaining \(64\) force an additional Fourier zero.
- Representative \(\{0,1,2,4,8\}\): \(160\) rank-deficient sets, all rank \(4\), all forcing a zero time coefficient.
- Admissible exact \((5,9)\) cases: \(0\).

The final line must be `VERIFY_OK`. No floating-point computation or tolerance is used. The verification is exhaustive only for the finite domain stated in the claim and does not establish results for other support sizes, groups or orders.
