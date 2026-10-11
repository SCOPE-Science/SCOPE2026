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
# Reproducible verification

Run `python checker.py` in the directory containing the embedded files. Expected output: `PASS 460 independent field/phase/Fourier checks; fields: 3, 5, 7, 11, 9, 25`.

The program builds finite-field addition and multiplication directly in the prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\) and in quadratic extensions \(\mathbb F_9,\mathbb F_{25}\) using irreducible polynomials. It computes threefold convolution independently of directly evaluating the normalized Fourier sixth moment. It checks the predicted multiplicity partitions, the closed formulas, the inequalities and equal-modulus extremizers with characteristic-sensitive phases. Floating-point comparisons use a declared tolerance, so they are checks rather than exact infinite certificates.

Additional exact symbolic validation is available from the two deficit identities in `RESULT.md` by expanding \(S^3=A_3+3B_{21}+6P\) and \(SV=A_3+B_{21}\). All finite tests are unnecessary for the universal proof: the latter uses the nonzero Vandermonde determinant, the mod-characteristic multiplicity classes, orthogonality and nonnegative algebraic decompositions. The proof makes no statements about unrestricted \(q>3\) extension sharpness.
