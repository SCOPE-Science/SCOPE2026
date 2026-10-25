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

# Verification details

The proof first obtains the exact action of both ordered monomial slant Toeplitz products on the normalized Bergman basis. It checks the normalization and strict upper weight bound, then separates the mutually exclusive residue cases modulo the square of the slant order. Disjoint residue classes yield a diagonal adjoint square converging to a scalar; coincident classes yield, modulo compacts, an integer-step discrete Laplacian with symbol \(2-2\cos(q\theta)\). Each case supplies a sharp norm, an essential norm and an essential spectrum; strict weights or missing top eigenvalues establish nonattainment.

Run `python check_slant.py` after extracting the package into one directory, with NumPy and SciPy installed. The standalone implementation reported **PASS 29766 deterministic assertions**. Finite-section largest singular values for seven sample parameter triples lie below their respective analytical sharp bounds and provide lower checks only. The checker tests selected finite degrees and matrix sections, and cannot prove the complete infinite-dimensional theorem. External independent verification has not been performed.

The known literature comparisons concern qualitative commutation criteria and differently normalized spectral studies. One historical source could not be read in full; its possible overlap remains unresolved as a priority risk.
