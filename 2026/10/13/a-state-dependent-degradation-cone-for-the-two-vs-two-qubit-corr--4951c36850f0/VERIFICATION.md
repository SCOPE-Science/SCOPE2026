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

The analytic proof reduces the new claim to a binary-channel identity. With Alice Schmidt-unbiased, direct expansion gives \(W_C(y\mid x)=(1+yu+xyCt)/2\). For \(t\ne0\), any binary output post-processing mapping the corresponding Bell channel to \(W_C\) must have affine conditional mean \(u+Cy_0\), so stochasticity is exactly \(|u|+C\le1\). Substitution verifies the kernel identity, and \(C^2+r^2=1\) gives the displayed cone.

`artifacts/verify.py` replays the probability and kernel formulas on deterministic parameter grids and checks the resulting mutual-information inequality. The numerical grid is supplementary and is not used to infer the universal statement.

The final two-vs-two implication additionally uses the maximally-entangled theorem from arXiv:1210.8317v1. The package does not verify that external theorem computationally and does not claim the cone is necessary for the mutual-information inequality itself.
