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

The attached `verify.py` program was run with a standard Python interpreter; it printed:

`PASS: 2157 exact odd-return identities; 947 pairwise-coprime multipliers; 947 prime-product lower-bound comparisons`

The test independently performs ordinary steps of both signed maps for finite odd inputs and checks the exact return identity, coprimality, factorization into return multipliers, and finite prime-product lower bounds. No infinite orbit is certified by these finite computations. The proof in `RESULT.md` establishes the asserted limit inferior analytically using a factorial lower bound and a time-index estimate. The bound is not claimed to be optimal.
