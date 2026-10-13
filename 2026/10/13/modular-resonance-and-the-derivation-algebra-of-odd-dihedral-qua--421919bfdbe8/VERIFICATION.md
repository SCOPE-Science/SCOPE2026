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

# Verification record

The file `checker.py` is standalone Python 3 code. Execute `python3 checker.py` from the same directory as these files. It constructs the Leibniz equations directly from the defining quandle product and computes their nullities by modular Gaussian elimination; independently, it evaluates the arithmetic orbit formula for the dimension.

All 68 applicable pairs from odd orders 3 through 21 (sampled odd orders 3,5,7,9,11,13,15,17,19,21) and prime characteristics 2,3,5,7,11,13,17,19 with the characteristic not dividing the order matched. The nonzero tested cases were (11,3), (13,5), and (19,3), each with dimension one. The explicit quadratic-character convolution at order 11 over characteristic 3 passed all 1331 basis-product/target-coefficient Leibniz comparisons. The checker emitted `VERIFY_OK`.

These are finite checks, not a substitute for the proof for all odd orders and eligible fields. In particular, the checker does not test fields beyond the prime fields, nor the excluded case in which the characteristic divides the order. No independent audit has been performed.
