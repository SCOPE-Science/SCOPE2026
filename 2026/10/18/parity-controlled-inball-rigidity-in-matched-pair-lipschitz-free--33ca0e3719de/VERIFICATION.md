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

# Reproducibility and verification

Run `python matched_metric_check.py` with Python 3. The script uses only the standard library and enumerates the six exact rational vertex states of the planar metric hexagon independently for every matched pair. Its input values are twenty cases from four pair counts \(k=2,3,4,5\) and five rational short distances, two additional cases exactly at the odd-parity transition, and one six-pair case.

For every case it checks the exact squared norm of each product-hexagon vertex against the proposed global formula and checks the complete number of equality cases. In twenty-two cases it additionally computes the rational rank of the centered contact-normal matrix and checks the predicted affine incenter dimension. The full output ends with `ALL EXACT MATCHING-METRIC CHECKS PASSED`.

These finite computations do not prove the result for arbitrary real short distances or arbitrarily large pair counts. The universal proof in `RESULT.md` separately establishes (i) the product-hexagon projection model, (ii) an exact imbalance identity, (iii) strict exclusion of all patterns with at least two split pairs, and (iv) the span of tangent normals in the pair-mean/pair-difference decomposition. No independent audit is claimed.
