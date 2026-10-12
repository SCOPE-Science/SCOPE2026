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

The primary publisher full text was inspected at equation (24): each of the twelve coordinates has a constant additive Brownian term \(\sigma_i dB_i\), and the text declares the noise intensities positive. Remark 2 retains positive noise in zero-at-DFE infected coordinates while calling the deterministic disease-free state stochastically asymptotically stable.

The proof uses the exact small-time decomposition at a boundary point,
\[
X_i(t)=\int_0^t b_i(X(s))ds+\sigma_i B_i(t).
\]
After division by \(\sqrt t\), the drift term converges to zero in probability and the Brownian term is \(N(0,\sigma_i^2)\), so the negative-side probability tends to \(1/2\). This is sufficient to disprove orthant invariance and stochastic-equilibrium status of the DFE.

`verify.py` checks the structural boundary condition and the list of zero-at-DFE coordinates carrying positive additive diffusion. It does not numerically simulate Brownian paths and does not assess unconstrained stationary distributions. Running `python3 verify.py` returns `VERIFY_OK`.
