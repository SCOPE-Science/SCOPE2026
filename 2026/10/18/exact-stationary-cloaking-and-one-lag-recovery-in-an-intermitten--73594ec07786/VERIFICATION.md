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

Run `python CHECK.py` from the extracted self-contained package. The checker was executed successfully with SymPy, NumPy, and SciPy. It verified exact factorization of the Fourier transform, the static equality condition, the stationary moment identities and the lag covariance ODE, and compared 225 positive-parameter matrix-comparison cases on an explicit test grid against independent 3-by-3 uneliminated Fourier linear systems and matrix-exponential propagation. These tests are supplementary; the infinite-domain iff and strict sign inequalities are established by the analytic proof in RESULT.md, which uses a strictly positive numerator factor and positive response kernel.

No Lean or automated formal theorem prover, independent audit, independent scientific certification, or empirical statistical validation was undertaken. The exact recovery assumes known positive rates and diffusivity, and ideal stationary time-lag covariance. The source-paper propagators are established prior art. Any practical finite-sample extraction, nonlinear extension and mathematical priority beyond the inspected literature remain unproved.
