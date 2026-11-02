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

The proof proceeds by normalizing the Drury–Arveson monomial basis, deriving each block of the two matrix Gramians, proving the scalar affine identity between them, and diagonalizing the row Gramian. The resulting eigenvalues and multiplicities yield the full spectral statement, compactness, ideal thresholds and logarithmic coefficients through binomial counts and elementary asymptotics.

The included standalone `spectral_check.py` builds multiplier matrices from directly enumerated monomials, checks the Gram blocks and both eigenvalue branches by numerical diagonalization, and verifies dimensional counts. Actual run: `python spectral_check.py`; output: `PASS 1012 independent finite degree, dimension, and multiplicity assertions`. Python 3 and NumPy are needed. These are finite checks only; they do not constitute validation of an infinite-dimensional theorem or independent review.

The degree-one, two-variable check matches the earlier published determinant near \(-0.133975\). This comparison fixes the orientation of the operator-matrix indices and the square-root conventions.

Source comparison covered the published semi-hyponormality framework, \(d\)-shift commutator ideals, essential normality, and related available research records. The theorem's claimed originality remains a best-knowledge assessment subject to further independent bibliographic review. The earliest complete day of the motivating article's 2025 journal release remains unresolved; its dated May 2026 arXiv posting is recorded separately.
