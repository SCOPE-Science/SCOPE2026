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

Execute `python verify.py` with NumPy installed. The standalone program constructs the exact six-site Hermitian Hamiltonian, computes its spectral decomposition, tests analytic transition amplitudes for all nine internal/external pairs at seven times, and checks the upper bound at 500 additional time samples for each pair, totaling 4,563 amplitude comparisons. It verifies eigenvalues, unitarity, and the exact closed-form constant. A deterministic 300,000-point scan for each cyclic separation finds probabilities exceeding \(0.7010\), approaching the claimed exact supremum.

Numerical finite-time checks do **not** establish the supremum or prove finite-time nonattainment. Those follow respectively from the explicit Fourier-sector kernel, rational independence and Kronecker density, and the irrationality of \(\sqrt7\), as detailed in RESULT.md. No computer-assisted infinite certification or independent audit is claimed. The checked statement concerns fixed unit hopping magnitudes, on-site energies zero, flux magnitude \(\pi/2\), and single-site internal-to-external transfer only.
