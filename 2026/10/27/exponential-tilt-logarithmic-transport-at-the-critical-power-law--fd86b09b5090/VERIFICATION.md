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

# Verification summary

The included `verify.py` is a standalone finite-dimensional and finite-horizon check requiring NumPy and SciPy; run `python verify.py` from the directory containing that file. It passed checks for three positive self-loop weights, three observation lengths and three restart-window parameters. It computes the exact zeta-normalized restart probabilities, renewal mass and backward-age law by finite convolution; verifies the normalization identity and numerical renewal monotonicity; and compares finite logarithmic-age cumulative probabilities with their proposed limiting tilted densities. It constructs the weighted Grover coin explicitly, diagonalizes its Fourier evolution matrices, and compares integrated flat-eigenvector weights with the analytic localized-sector formula, including the exact dark vector.

The finite-size age convergence is slow, and the provided tolerances are deliberately not claims of rigorous error bounds. The claimed arbitrary-horizon limit is established analytically by truncated-sum concentration, a geometric-mixture monotonic renewal argument and its combination with the established Fourier/ballistic weak limit. An independent audit or independent mathematical validation has not been performed.
