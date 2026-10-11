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
# Reproducing the integral homology certificate

Place `verify.py` and `certificate.json` in the same directory, then execute `python3 verify.py certificate.json` with Python 3.8 or newer. The script uses only the standard library and generates graph adjacency, eleven closed neighborhoods, all 213 nonempty simplices, and every signed incidence needed for the integer boundary matrix.

The verification checks each of 55 recorded free-face/codimension-one coface pairs **against the changing simplicial complex**, not against an unverified list. It checks the resulting two-dimensional spine, the explicit ten-edge spanning tree, the resulting 36-by-46 cellular boundary, the exact signed determinant \(+2\) of a specified minor, the mod-two rank 35 and mod-three rank 36. Together these establish Smith invariant factors \(1\) (35 copies) and \(2\) (one copy), and a ten-dimensional integral kernel. A successful run prints `VERIFY_OK` followed by the verified face counts and ranks.

This finite exact certificate proves the stated integral homology, not the fundamental group, a precise integral homotopy type, or a result about all triangle-free graphs. The equivalence between the graph-metric Čech complex and its closed-neighborhood facet construction is justified separately in the mathematical proof; neither a failed keyword search nor the executable alone proves bibliographic novelty.
