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

The supplied `verify.py` independently computes exact-rational resolvents and Crank–Nicolson matrices for the \(3\times3\) and \(4\times4\) square tori at \(s=1/4\) and \(s=1/3\). It verifies unit row sums, positive off-diagonal entries, the identical diagonal formula, and agreement with the Fourier spectral sum.

The script also verifies the \(n=3\) quadratic root, computes Fourier threshold crossings for ten torus sizes, independently evaluates the square-lattice complete elliptic integral using the arithmetic-geometric mean, and tests the explicit exponential estimate. Executed from the packaged file path, it returned `VERIFY_OK 714 rational matrix entries and Fourier/elliptic thresholds` with limiting physical timestep `0.5881972836856282`.

The finite tests do not certify the infinitely quantified monotonicity, the exact Fourier integral transformation, or the analytic exponential estimate. Those assertions are supported by the proof in `RESULT.md`. No independent audit is claimed.
