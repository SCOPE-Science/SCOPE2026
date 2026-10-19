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

# Exact verification and limits

Run `python3 verify.py` using only the Python 3 standard library. It reconstructs the full twenty-one-row homogeneous inequality matrix and tests all 20349 possible five-row active sets; verifies the fourteen primitive rays explicitly; determines the rational face lattice of the normalized cross-section and sums 2184 six-simplex determinant volumes exactly; and requires the result \(289/2488320\). The code additionally compares direct seven-one word enumeration with gap-lattice enumeration for lengths 7 through 17 and requires equality. Its successful console output includes `VERIFIED_EXACT_VOLUME 289/2488320` and `RAYS 14 FACES 155 SIMPLEX_FLAGS 2184`.

The proof of the infinite asymptotic is the gap-bijection and rational-polytope Ehrhart argument; finite counts are checks only. The full rational generating function for density seven and lower order quasi-polynomial terms are not supplied. The exact volume computation has not been independently audited, and historical originality cannot be guaranteed against unavailable sources.
