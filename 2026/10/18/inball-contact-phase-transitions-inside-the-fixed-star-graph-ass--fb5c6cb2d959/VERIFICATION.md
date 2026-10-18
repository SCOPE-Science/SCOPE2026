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
# Reproduction and checks

Run `python3 verify_star_inballs.py` with Python 3 and NumPy available. The checker reconstructs the Minkowski-sum exposed vertices directly from strict linear-functional orders and separately checks every claimed support inequality, active-facet affine rank, Euclidean distance, and contact count. It covers every cutoff for \(2\le k\le6\) and five weight pairs for each \(k=3,4,5\), for 35 scenarios. A successful complete run prints `VERIFY_OK`.

The source code contains no numerical optimization black box; support maxima are exact integers. Ranks and Euclidean norm comparisons use floating-point NumPy and tolerance, with all finite evaluated instances comfortably separated. The analytical proof in `RESULT.md` is the only support for unrestricted cardinality weights, dimensions, and the full sharp phase statement. No independent mathematical audit has been performed.
