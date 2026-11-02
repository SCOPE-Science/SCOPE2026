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

# Reproducibility and limitations

Run `python3 verify.py` using Python 3.10 or newer. No third-party packages or external files are needed. The verifier reports 1,528 checks and the concrete \(m=4\), \([-10,10]\) coefficient ratio \(6.943939037987\). The exact-rational tests reconstruct the inverse-Gram identity directly. Independent deterministic integrations test the \(m=2\) rare-event probability and its asymptotic coefficient; scalar quadratures test the Hölder lower bound and strict perturbation gaps.

These finite computations do not establish the limit as the tail threshold tends to infinity, the all-density uniqueness statement, or the general moment threshold. Those conclusions are proved symbolically in `RESULT.md` by the orthogonal Jacobian, dominated convergence, Hölder's inequality, and the layer-cake identity. Claims about wider polynomial spaces or finite-threshold optimality remain unproved.
