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

The exact checker `verify_pascal.py` was executed against the current formulation with Python 3 and returned `PASS: 65904 finite exact assertions (no claim of infinite computational proof)`.

It checks the binary Pascal support identity and the strict-index Hamming separation for all integers \(0\le s<t<256\). For heterogeneous and nonfair rational Bernoulli probabilities it evaluates joint-character covariances as exact rational sums and verifies the analytic upper bound for all checked pairs. For short trajectories it also computes \(\mathbb E[Q_N^2]\) by two **independent finite methods**, direct coefficient/path enumeration and pair-covariance expansion, and compares exact fractions.

The infinite assertions require the analytic proof. In particular, the modular Fourier bound, Hoeffding estimate, summability exponent, all-time interpolation, Fubini passage to quenched paths, and martingale functional central limit theorem are not established by finite tests. No independent audit has been performed.
