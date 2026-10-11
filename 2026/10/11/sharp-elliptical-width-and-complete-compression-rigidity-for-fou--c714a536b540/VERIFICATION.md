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
# Verification of the four-corner compression theorem

The theorem is proved analytically in `RESULT.md` for every real parameter pair \(a,b>0\). The essential steps are the four rank-one positive effects \(E_{s,t}\), the elementary joint-compatibility inequality, the \(2\)-by-\(3\) singular-value characterization of the compression ellipse, the explicit equality witness and the forced uniform-weight equality classification.

To replay the exact arithmetic witnesses, run `python3 verify_rectangle.py` from the directory containing that file. The script uses only the Python standard library, the rational number type `fractions.Fraction`, and the stated integer Pythagorean triples; the expected output is `FOUR_CORNER_RATIONAL_CERTIFICATE_OK`. It checks positivity, rank-one factorization, normalization, spectral combination and the extremal semiaxis identity with exact rational arithmetic. These discrete examples do not verify all positive real parameters and are not substituted for the universal proof.

A comparison of theorem statements with arXiv:2610.04377v1, arXiv:2111.15180v1, arXiv:0706.1415 and arXiv:0805.1538 is documented in `REVIEW.md` and `AUDIT.json`. The older qubit compatibility tradeoff supplies the upper-bound mechanism, not a prior all-subspace compression rigidity classification. No independent audit or external validation is asserted.
