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

# Verification performed

The combinatorial formula was checked against brute signed-face enumeration for dimensions 3 through 8, producing 945 exact integer comparisons. Independent quadrature normalized the order-statistic weights to one for dimensions 3, 4, 5, and 7, and 400,000 Gaussian importance-sampling trials for each of dimensions 3, 4, and 6 agreed with the predicted face-vector frequencies to within 0.0021. The checker is supplied as `verify_section_faces.py` and requires Python 3, NumPy, and SciPy.

The proof in `RESULT.md` separately establishes the full face-vector formula and weak logarithmic limit for every dimension and every fixed finite set of face ranks. Simulations do not certify the infinite-dimensional argument. A historical-priority risk remains because not all earlier section-combinatorics literature was inspected. No independent audit has been performed.
