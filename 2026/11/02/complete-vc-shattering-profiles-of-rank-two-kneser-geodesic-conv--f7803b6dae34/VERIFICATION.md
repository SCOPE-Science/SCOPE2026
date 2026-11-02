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
# Reproducibility

The two scripts included with the result use only the Python 3 standard library.

Run `python3 verify_kneser_convexity.py` to reconstruct KG(5,2) and KG(6,2) from disjointness, run breadth-first shortest paths, enumerate all candidate graph-convex subsets, enumerate all trace supports and independently verify the precise structural exceptional classifications. The script also verifies that every intersecting vertex pair generates the full convex hull at orders seven through nine.

Run `python3 verify_kneser_hull_traces.py` to repeat every exceptional shattering profile using Floyd–Warshall distances and a direct convex-hull avoidance test, not the enumerated hypothesis list. Both programs completed successfully on the packaged source bytes. The first outputs `ALL_RANK_TWO_KNESER_SHATTERING_CHECKS_PASS`; the second outputs `ALL_INDEPENDENT_HULL_TRACE_CHECKS_PASS`.

The unrestricted higher-order theorem is justified by the mathematical proof, not these finite checks. No independent audit, external formal-proof certification, or comprehensive historical-priority certification has been performed.
