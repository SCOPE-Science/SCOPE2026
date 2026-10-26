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

Run `python3 checker.py` with Python 3 and no third-party packages. A recorded successful output is included in `checker_output.txt`. The checker performs 1,321 exact assertions for dimensions \(4\) through \(9\), including direct convolution coefficients for complex Gaussian-integer arrays, combinatorial fourth-moment formulas, graph spectral identities, coefficient stability, and vertex-phase extremizers.

The global theorem for all integer dimensions \(n\ge4\) is proved analytically in `RESULT.md`: (i) character collision classification, (ii) two elementary four-cycle majorants, (iii) line-graph incidence diagonalization, (iv) equality-phase reconstruction. Computational checks are finite corroboration, not exhaustive proof of unbounded-dimensional statements. The stability coefficient is not claimed optimal, and independent validation has not been performed.
