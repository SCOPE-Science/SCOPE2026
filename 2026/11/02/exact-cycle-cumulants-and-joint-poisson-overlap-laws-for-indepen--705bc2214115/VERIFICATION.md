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

Execute `python3 verify.py` in the directory containing the seven files. The standalone program uses only Python's standard library (`fractions`, `itertools`, `heapq`). It evaluates exact integer powers and rational expressions for the host-edge matrix and checks its spectrum at host sizes from three through eight, for powers two through five. It independently enumerates all labeled trees on three and four vertices via Prüfer words, then computes exact forest, triangle and four-index-cycle moments by direct products. Positivity and the explicit third-cumulant polynomial are checked for several additional host sizes.

The actual replay of the supplied script produced `VERIFY_OK 82 exact assertions; all Prufer trees through 4 vertices tested`. Exact computations have no floating-point tolerance or random seeds.

Proof limits: finite checks do not certify any all-order result. The argument establishing all finite host sizes is the Cayley-forest formula combined with an explicit incidence-matrix spectral decomposition. The full joint weak limit is proved using uniformly bounded mixed factorial moments and moment determinacy, not by simulation. Only self-review has been performed; no external mathematical audit is represented.
