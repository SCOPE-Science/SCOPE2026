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

Reproduce with `python verify.py` in the same directory, using Python 3 without additional libraries. The script tests finite fields of orders 2, 3, 4, and 5, including an explicit implementation of the quadratic extension of the binary field. It enumerates every nonzero traceless \(2\times2\) matrix, computes all general-linear conjugacy orbits and stabilizers, and verifies each formula for orbit size, number of classes, centralizer size, and simultaneous Poisson derivation constraints.

Observed output includes `VERIFY_OK`; the classification and symmetry formulas for every prime power follow from the symbolic proof in `RESULT.md`, **not** from finite testing. Independent audit has not been performed.
