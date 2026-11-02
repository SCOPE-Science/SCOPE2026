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

The exact argument is given in `RESULT.md`: primitive square-zero conjugacy, its centralizer order, valuation-shell lifting, and the deep-ideal count. Its scope is all finite commutative chain rings, not merely the finite rings enumerated computationally.

Run `python verify.py` with Python 3. The checker directly enumerates twenty configurations, including nonprime residue field \(\mathbb F_4\), mixed-characteristic rings \(\mathbb Z/p^d\mathbb Z\), and equal-characteristic truncated-polynomial rings. Each of the four entries of a squared matrix is tested using independently implemented ring operations. Exact valuations and totals are compared with the displayed formula. The verified output ends with `VERIFY_OK: 20 finite configurations`.

Finite enumeration does not certify the infinite family; its purpose is to expose mistakes in the explicit equations and small boundary cases. The derivation for arbitrary chain rings is the proof in `RESULT.md`. Source-access restrictions and possible older priority claims are separate from correctness of this direct proof.
