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

# Reproducibility and limits

The proof is analytic and applies to every triple of pairwise distinct integers together with zero. Run `python checks/check_tetra_crossings.py` in the extracted package directory with Python 3, SymPy, and mpmath installed.

The checker directly verifies 120 exact barycentric-weight sets and the negative determinant of the restricted quadratic form. It also evaluates the tetrahedral Fourier integral through its independent convergent simplex-moment series: at the stated non-lattice frequency, the difference from the closed divided-difference formula was below `6e-52`. At the lattice node with integer phase coordinates `(1,2,3)`, it constructs four high-precision roots lying on the two predicted nearby analytic zero curves and finds residuals below `4e-53`. Their ratios approach the two predicted tangent lines.

These finite algebra and numerical tests are diagnostic. The theorem for infinitely many nodes follows instead from the displayed general barycentric identity, exact sign of the Vandermonde product, the implicit-function theorem, and the real-analytic Morse lemma. No global classification of Fourier zeros away from these reciprocal nodes is established. No independent external proof audit has been performed.
