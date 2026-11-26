---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the ten-transposition word metric, a move changes cycle count by one and each length-l cycle factors into l−1 transpositions. The central powered-distance matrix has the stated nontrivial block coefficients and multiplicities. I independently formed the four exact 120×120 distance-layer matrices: integer-scaled Lagrange projections for the distinct transposition adjacency eigenvalues 10, 5, 2, 0, −2, −5, −10 sum to the identity after unscaling, have ranks 1,16,25,36,25,16,1, and give the stated four layer scalars on each block. The −10 block is the sign direction. Six-term rational logarithm bounds make g(0), g′(0) and the comparison coefficient in g″ strictly positive for g=2^(−p)F′; the independent rational endpoint bound gives F(8/25)>13773/500000 and 2^(8/25)<5/4. Thus F crosses once, and the five other multipliers are strictly negative up to that crossing by the inequalities in RESULT.md:68–78. Double centering gives ranks 119 and 118; the Gaussian on the resulting distinct Euclidean points is strictly positive definite. Beyond the cutoff the sign-vector quadratic form has a negative first-order term as t decreases to zero, while 119e^(−t)<1 suffices for large-t strict positive definiteness. Replay: python /workspace/checks/5.py (NumPy; checks exact integer/rational identities and reports optional sampled spectra). Frozen check.py was read, not executed. No single-bandwidth cutoff above p* is asserted.

## originality

PASS

The combination of the exact all-positive-exponent S5 threshold and its simple sign nullspace was not covered by the strongest inspected matches. The proof uses known Fourier and negative-type machinery; the classification, not those tools, is the distinct contribution. This is a bounded decision, not a priority certification.

## value

PASS

All transpositions give the canonical conjugation-invariant word metric on S5. The first spectral crossing and its multiplicity are needed for exact squared-Euclidean embedding ranks and describe which metric powers permit Gaussian kernels at every bandwidth. Determining the controlling sign direction rather than merely bounding one block gives a complete and usable invariant of this natural finite metric.

The dated certificate retains the supplied scientific assessment, sources and limitations.
