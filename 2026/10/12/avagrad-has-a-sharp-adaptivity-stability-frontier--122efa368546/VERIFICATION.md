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
The package verifies AvaGrad's exact one-step adaptivity-stability frontier on an isotropic quadratic.

`verify.py` reconstructs the source root-mean-square normalization, checks the sharp minimum and maximum effective coordinate rates, compares direct objective ratios with the closed endpoint envelope, and verifies the stable boundary, reflection case, unstable side, and limiting weak- and strong-adaptivity regimes.

The finite computations are transcription guards. The sharp rate bounds and if-and-only-if stability frontier are proved analytically in `RESULT.md`.
