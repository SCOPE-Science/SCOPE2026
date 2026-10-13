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

The proof reduces the event for a fixed rank-\(r\) matrix to nilpotency of a uniformly random endomorphism of an \(r\)-space, then evaluates an expected kernel size of an arbitrary product using the survival probability of each nonzero vector. The resulting matrix-factor identity is exact for every prime power, dimension, and positive number of independent uniform factors. The finite-ring extension uses the nilpotent Jacobson radical and the semisimple structure theorem.

Run `python3 verify.py`. It uses only the Python standard library and performs exact integer-weighted convolution of all matrix products and several finite-ring products; no floating-point arithmetic or Monte Carlo trials are used. The output must end with `EXACT_CHECKS=21 VERIFY_OK`.

This checker exhausts the selected finite instances only. It does not independently prove the all-dimension matrix enumeration, finite Wedderburn theorem, or general proof. It is not an independent audit.
