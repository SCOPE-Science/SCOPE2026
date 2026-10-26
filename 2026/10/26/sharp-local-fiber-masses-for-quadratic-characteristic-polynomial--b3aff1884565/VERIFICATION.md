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

Reproduce the exact arithmetic tests using `python3 matrix_density_verifier.py` (Python standard library only). The script directly counts the three free matrix entries subject to the determinant congruence for 500 prime-power parameter configurations and compares them to the independent formula involving quadratic roots. It additionally checks 22 high-level normalized counts against the explicit local rational density for split, unramified, ramified, repeated-root, and dyadic examples.

Expected output: `CERTIFICATE_OK exact_finite_fibers= 500 local_classification_samples= 22`. These experiments are not infinite proofs. The universal finite identity follows from a valuation-by-valuation pair count, and the limit and sharpness from the p-adic root-proximity integral in RESULT.md.

No independent audit has been performed. The most material residual scientific risk is that older, more general local-density literature could implicitly contain the same classification.
