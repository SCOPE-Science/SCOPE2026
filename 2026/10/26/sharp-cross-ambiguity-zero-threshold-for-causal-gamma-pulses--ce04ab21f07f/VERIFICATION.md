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

The proof is analytic and applies to every integer \(m\ge0\). Reproducible auxiliary checks are supplied in `checker.py`, `checker_output.txt`, and `requirements.txt`.

* Exact Routh–Hurwitz minors computed for orders one through five and symbolic factorization of the general order-three minor.
* Algebraic identity \(E_m-E_{m-1}=z^m/m!\) used for the all-order simplicity argument. The checker additionally checks low orders.
* A fifth-order conjugate pair is found with high precision and mapped to positive-delay coordinates; this witness is not substituted for the general Routh proof.
* Four independent numerical integral comparisons for both delay signs match the closed form to high precision.

The source preprint https://arxiv.org/abs/1407.4321 is public from 2014-07-16. Later comparative literature https://arxiv.org/abs/1811.03937 is used for scientific priority assessment, not as an archival anchor. No independent audit has been performed.
