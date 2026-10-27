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

# Verification and reproducibility

The proof in `RESULT.md` establishes the infinite statements. The standalone program `VERIFY.py` provides separate finite checks of its algebra and stationary Gaussian consequences.

Execute `python VERIFY.py` with Python 3, NumPy and SciPy installed. During preparation, the command returned `PASS: 591 deterministic checks`. These checks cover 52 finite positive-coupling chains (sizes 2 through 14, with four sets of asymmetries per size), a three-vertex balanced-cycle network, a frustrated directed triangle, and the two endpoint products of a separate five-vertex chain. They test diagonal-gauge symmetry, positive-definite stiffness, calibrated bath temperatures, Hurwitz stability, Gaussian stationary Lyapunov residuals, the direct Lyapunov covariance against the proposed Gibbs covariance, and the limiting characteristic-function form.

## What the checks do not establish

A finite deterministic test cannot prove the cycle classification for arbitrary connected graphs, continuous-time detailed balance for all times, or the Gamma-difference distribution as observation time diverges. Those conclusions depend on the explicit graph path-product construction, generator adjoints and mixing argument presented in the proof. Independent scientific validation has not been performed.

## Reproducibility notes

The stochastic heat uses the Stratonovich convention \(Q_i(t)=-\int_0^t\gamma_iV_i(s)^2\,ds+\sqrt{2\gamma_iT_i}\int_0^tV_i(s)\circ dB_i(s)\). The position-velocity covariance ordering in `VERIFY.py` is first all positions and then all velocities. Reproducible rational and numerical test inputs are specified directly by that source file; no external datasets or unpublished records are required.
