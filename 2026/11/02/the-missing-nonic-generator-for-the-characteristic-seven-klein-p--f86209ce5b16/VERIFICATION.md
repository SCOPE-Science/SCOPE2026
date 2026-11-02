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

Execute `python3 klein_bad7_verify.py` with a standard Python 3 interpreter. It performs exact modular arithmetic only, using no external packages and no network. It enumerates the \(57\) rational projective points, evaluates all \(21\) Klein lines to identify the \(49\) singular points, checks the eight-point conic complement and the separator's zero set, and computes the evaluation and ideal-image ranks in each degree up to \(11\). It prints `VERIFY_OK` on success.

The proof's extension from the degree-\(11\) finite checks to the full homogeneous ideal uses the explicit colon-ideal exact sequence, Hilbert series and evaluation-rank stabilization. The program itself is not a certificate of originality or independent validation. References and historical-priority limitations are in `RESULT.md` and `REVIEW.md`.
