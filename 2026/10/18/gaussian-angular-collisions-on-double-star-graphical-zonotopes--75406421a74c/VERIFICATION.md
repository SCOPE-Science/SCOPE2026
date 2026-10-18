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

# Verification and reproducibility

The standalone `CHECK.py` uses only the Python standard library. Execute `python CHECK.py` in the directory containing the embedded files. It evaluates \(I_{i,j}^{p,q}\) and \(C_{p,q}\) in exact rational arithmetic; it independently enumerates every rank permutation of the tree vertices in seven small parameter profiles; it checks symmetry of the two hub classes; and it separately enumerates one-hub star probabilities for six leaf counts. It prints finite checks for moderate sizes against the expected asymptotic scale.

The equality between Gaussian normal-cone collisions and rank-permutation orientation collisions follows from the explicit tree edge-sign characterization and continuity of Gaussian coordinate ranks. The universal exact formula is proved by conditioning and beta integration in `RESULT.md`; the asymptotic is proved there by Laplace corner localization and elementary exponential order statistics. No finite enumeration or observed numerical convergence is presented as an infinite proof.

The proof makes no independence or external-certification claim. The only status indicated is a self-review, with independent audit not performed. Its bibliographic novelty statement is qualified by the risk of equivalent prior results under other graph-ordering or solid-angle terminology.
