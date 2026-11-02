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

# Reproducibility and verification

The reproducible file `verification.py` contains finite arithmetic tests independent of the displayed symbolic simplifications. Run `python3 verification.py`. The script requires Python's standard library only; it represents large repeated eigenvalue blocks by multiplicities rather than allocated dense matrices.

A run produced `PASS: 5575 finite arithmetic checks`. Representative diffuse one-probe/mixed mean-square-error ratios for \(k=1\), \(k=20\), and \(k=100\) were approximately 4.9739583333, 80.97890625, and 400.9791145833. For \(k=1\) and a sufficiently small positive concentration parameter, the mixed/one risk ratio exceeded \(10^{15}\). The latter is a finite illustration, not a substitute for the limiting proof.

The proof in RESULT.md independently establishes the exact spectral multiplicities, two pilot residual identities, exact Gaussian MSEs, increasing diffuse risk ratio, and positive limiting concentrated mixed risk. The Lanczos exactness claim follows from the at-most-three-point spectrum of each ideal preconditioned matrix and standard minimal-polynomial termination. No randomized Nyström experiment or claimed validation of its leave-one-out estimator is performed. The exact-rank spectral oracle remains a scope assumption.

Independent mathematical audit has not been performed.
