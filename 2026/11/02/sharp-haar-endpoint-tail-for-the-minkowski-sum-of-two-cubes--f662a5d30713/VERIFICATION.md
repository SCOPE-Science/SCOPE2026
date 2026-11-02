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

From this package's directory, run `python3 verify.py` with Python 3. The script uses no third-party modules or external files. It checks all \(512\) possible \(3\times3\) sign matrices, finds exactly \(192\) with three nonproportional rows, calculates their rational polar optimizers, and confirms exactly \(96\) distinct rotation (determinant \(+1\)) maxima. It then evaluates the zonotope volume by all \(20\) minors on \(250\) reproducible random rotations, and compares the result with \(16(1+\sum|R_{ij}|)\).

The actual execution returned `ALL CHECKS PASSED`, with maximum absolute volume difference \(2.842170943040401\times10^{-14}\). The local quadratic deficit was checked in 500 samples at each of the scales \(0.015\), \(0.0075\), and \(0.00375\), with respective maximal relative discrepancies approximately \(4.96\times10^{-5}\), \(1.14\times10^{-5}\), and \(3.09\times10^{-6}\). The script also evaluates the stated constants numerically.

The proof, not the finite sampling, establishes the exact tail and moment asymptotics for arbitrary limiting parameters. Historical-priority status has not been independently audited.
