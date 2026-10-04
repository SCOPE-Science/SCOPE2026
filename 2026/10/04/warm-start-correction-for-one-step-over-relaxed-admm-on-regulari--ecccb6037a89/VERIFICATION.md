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

The algebraic verification starts from the exact over-relaxed ADMM equations at \(ho=\delta\) and \(lpha=2\). It checks three identities: the first-step \(x\)-error, the first-step \(z\)-error, and \(\mu^{k+1}=\delta z^{k+1}\). The last identity forces the dual-consistency defect to zero after one update, so a second update is exact for arbitrary initialization.

`verify.py` independently replays the scalar witness with rational arithmetic and checks a grid of rational scalar instances. It does not establish novelty and it does not simulate floating-point or inexact-subproblem effects.
