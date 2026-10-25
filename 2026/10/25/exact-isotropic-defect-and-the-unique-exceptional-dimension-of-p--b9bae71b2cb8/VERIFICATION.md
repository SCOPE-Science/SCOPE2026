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

The accompanying `verify.py` uses only the Python standard library and reconstructs all rational formulas from \(n=3\) through \(n=80\), including the exact special-dimension comparisons and algebraic coefficient identity. Run `python verify.py` in a directory containing the extracted embedded files. It checks finite instances but does not replace the analytic proof for arbitrary \(n\).

The separately supplied `verify_polytope.py` (optional Python dependencies: `numpy` and `scipy`) constructs the halfcube from parity sign vertices, calls SciPy's ConvexHull independently of the corner-truncation derivation, and integrates the first two uniform simplex moments on each origin-coned simplicial boundary face for dimensions three through six. It was executed successfully for all four dimensions: polytope volumes and covariance matrices matched theoretical values to better than \(5\cdot10^{-15}\) on the tested inputs. The finite verification does not certify global novelty or independently validate the all-dimensional theorem.

The proof's critical inputs are the classical parity-polytope outer description, the exact standard-simplex first/second moments, and the elementary Hamming-disjointness, group-symmetry, polynomial-sign, Bernoulli, and logarithmic-asymptotic arguments. The statement and proof use the same \(\pm1\) normalization and ordinary Euclidean volume.
