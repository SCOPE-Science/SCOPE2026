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

# Verification record

The analytical proof derives the finite normalized cross-Gram entries, a Hilbert–Schmidt limit for each parity submatrix, an exact Volterra singular system, and the sharp decomposition constant via principal vectors. This establishes the infinite-dimensional and asymptotic statements without relying on finite sampling.

The standalone `checker.py` executes 43,864 finite checks. It verifies all grid incidence entries for sizes \(3\le n\le32\), unit common singular values and a strict third singular-value gap, exact rational coefficients of the Volterra eigenpolynomial differential equations through degree thirteen, and numerical agreement of eight limiting singular-value pairs at dimension 220. These are reproducibility tests, not exhaustive verification of all dimensions.

No independent mathematical audit has been performed. No exact finite-dimension formula for all principal-angle cosines is asserted; the spectral and stability limits are the scope of the proof.
