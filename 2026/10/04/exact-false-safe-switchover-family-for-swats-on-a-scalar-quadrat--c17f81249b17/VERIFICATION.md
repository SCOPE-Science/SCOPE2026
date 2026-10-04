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
The package verifies the exact two-step SWATS construction on the scalar quadratic.

`verify.py` reconstructs the source Adam-phase update with \(\beta_1=0\), computes the projection estimates and bias-corrected monitor, confirms the automatic switch at iteration \(2\), and checks geometric divergence of the resulting SGD phase for multiple interior \(\beta_2\) values and multiple prescribed rates \(q>2\).

It also brackets the source-scale example with \(\alpha=10^{-3}\), \(\beta_2=0.999\), and \(\varepsilon=10^{-9}\).

The proof is algebraic; floating-point replay is only a transcription guard.
