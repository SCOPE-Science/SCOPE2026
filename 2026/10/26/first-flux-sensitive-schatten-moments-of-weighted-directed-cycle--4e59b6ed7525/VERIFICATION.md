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

The mathematical derivation directly counts the net displacement of every monomial trace term in powers of \(R_\theta^*R_\theta\). The first nonzero phase harmonic is isolated at half-order \(k=n/\gcd(n,2)\); its coefficient is computed using the exact identity \(W^n=(\prod_j w_j)I\). AM–GM provides the sharp coefficient and its equality condition. No asymptotic extrapolation is used.

From this package directory, run `python CHECK.py` (NumPy is required). The independently coded numerical matrix-trace computations passed 2,132 finite assertions over dimensions 3–10, general complex weights, zero-edge degeneracies, equal-modulus extremizers, and multiple phases. Checks are finite diagnostics and do not establish exhaustive correctness. No independent external audit or certification was conducted.
