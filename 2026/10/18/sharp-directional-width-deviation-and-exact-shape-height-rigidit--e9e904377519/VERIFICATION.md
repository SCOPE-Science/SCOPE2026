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

The analytical proof uses the exact product support-function decomposition and five explicit one-variable spherical integrals, a one-variable height derivative, and two nonnegative algebraic deficit terms. It does not infer infinite shape classifications from numerical tests. The complete planar polygonal equality classification for side counts not powers of two is a cited theorem of Akiyama and Kamae (arXiv:2201.06736v1, Theorems 6–7), not an independently proved lemma here.

The standalone `verify.py`, executed from its package directory with `python3 verify.py`, returned `VERIFY_OK 16020` and numerical optimum `0.0753372200107355` with height-to-width ratio `0.7519383938841089`. Tests cover 4,000 random parameter pairs, three exact sharp constants/planar identities, four polygon bases integrated in 12 sphere integrals, and three constant-width numerical profiles. The checker does not establish the general theorem or historical originality; those are addressed separately by exact analysis and literature comparison. External independent validation is not performed.
