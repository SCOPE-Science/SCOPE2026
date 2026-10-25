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

The result is derived analytically in `RESULT.md`, from the exact matrix entry integral, trace-norm differentiability of the moving-boundary operator, spectral perturbation across a strict disk eigenvalue gap, and Poisson/Parseval identities. These steps prove the full formula for every fixed positive area, rank and smooth mean-zero real deformation; the finite checks below do not establish the general case.

The executable `CHECK.py` depends only on Python's standard library. Run `python CHECK.py` in the extracted file directory. It uses exact rational arithmetic to test the diagonal telescoping identity, the translation-mode cancellation and the two-crossing-pair elliptic multiplier formula over many ranks and rational areas. Expected output: `CHECK_OK`.

A separate numerical experiment computed finite Fock-matrix Ky Fan sums for cosine-two radial deformations and compared the centered second-order difference with the analytic coefficient at areas \(s=0.5,2,6\), ranks \(N=1,2,3,5\), and decreasing perturbation magnitudes. Agreement was observed as the step decreased, but finite truncation is not proof of an infinite-dimensional statement; that experiment is not required to reproduce the exact proof.

The operator is normalized with the weight \(e^{-\pi|z|^2}\,dA(z)\); the radial variable is \(t=\pi r^2\). The error term is pointwise in \(N,s,h\). Independent audit has not been performed.
