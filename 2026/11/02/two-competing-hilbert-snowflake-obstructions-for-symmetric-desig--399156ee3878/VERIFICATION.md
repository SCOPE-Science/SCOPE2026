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

# Reproducible checks and proof boundaries

The analytical verification is the eigenvalue decomposition of the complete powered-distance kernel on the real zero-sum subspace and the elementary scalar root comparison. See RESULT.md, especially the block identity and the sign formula for the global mode at the spectral threshold. This derivation covers *every existing* symmetric design satisfying the stated assumptions, not merely the examples below.

Execute `python verify.py` with Python 3 and NumPy. The script constructs incidence matrices for \(\mathrm{PG}(2,q)\) over prime fields \(q=2,3,5,7\), their complement designs, and the cyclic symmetric \(2\)-\((11,5,2)\) design with its complement. It independently reconstructs graph distances by breadth-first search, checks exact integer design equations, computes incidence singular values, compares every eigenvalue of the full centered distance-power matrix with the predicted spectral branches at six exponents per graph, and checks critical rank and phase.

The observed critical exponents include approximately \(0.694280092777\) for the Fano incidence and nonincidence graphs, \(0.560762760130\) for \(\mathrm{PG}(2,3)\) incidence, and \(0.248493254733\) for its nonincidence graph. The latter critical affine dimension is \(24\), versus \(13\) for the incidence graph. All ten numerical cases passed.

Floating-point diagonalizations use an absolute tolerance of \(5\cdot10^{-8}\); no finite enumeration certifies an infinite theorem. No check claims independence, formal machine proof, or an external expert review. The resonance existence question remains open within this report.
