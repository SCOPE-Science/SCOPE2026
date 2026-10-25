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
# Verification and limits

Run `python3 verify.py` with standard Python 3. Expected final line: `VERIFY_OK 579`.

The program constructs all affine lines for prime powers 2, 3, 4 and 5, checks each parallel-line incidence axiom, constructs the line-flagified complex and validates mod-two reduced homology in dimensions through four for orders 2–4. It computes all affine actions for orders 2 and 3 and selected further actions for orders 4 and 5, comparing the tensor factor character with an independent signed fixed-simplex Lefschetz count for orders 2 and 3; it checks translation traces in all four orders.

A finite script does not prove the stated all-prime-power theorem, integral orientation lattice, or odd-characteristic representation decomposition. Those follow from the explicitly written augmented integral chain, incidence-cycle, and Fourier arguments in RESULT.md. The ordinary Dowker to flagified comparison is only one of abstract representations after a grading shift and is noncanonical. Independent audit has not been performed.
