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

# Reproducibility and limits

Execute `python CHECKER.py` with the Python standard library. The checker reconstructs the W-map critical orbit with rational arithmetic, computes sign-correct branch-sum weights, and bounds the uncomputed tail at cutoff \(N=72\) by \((2+a)^{-N}/(1+a)\). Exact interval arithmetic then encloses the finite-parameter invariant density and centered-window probabilities. The executable was run with output `VERIFY_OK`, including seven sites on both sides of multiple predicted dyadic left-edge discontinuities.

Analytic completeness rests on the cited invariant density representation and normalization together with the geometric tail bounds and dominated convergence in the proof. Finite rational computations do not demonstrate the asymptotic statements for all small parameters, nor priority over published or unpublished work. The externally established family and weak-* theorem remain attributed to Li–Góra–Boyarsky–Proppe–Eslami.
