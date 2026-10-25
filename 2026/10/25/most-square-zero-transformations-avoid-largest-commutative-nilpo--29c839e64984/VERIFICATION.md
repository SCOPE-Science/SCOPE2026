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

The standard-library `check.py` generated `check_output.txt` from independently enumerated maps on two through seven labeled points, a total of \(873611\) candidate transformations. Every map was checked for constant second iterate, and its image and fixed-sink fiber were measured directly. Formula counts were computed separately via Stirling recurrences and binomial coefficients. Exact equality held for every tested size. The scientific theorem invokes the published maximum-semigroup classification only for \(n\ge5\); the lower-order runs test the finite summation identity alone.

For \(n=5,6,7\), the verified counts of all square-zero maps and maps extendible to the designated extremal null family are \((205,185)\), \((1176,1146)\), and \((7399,6517)\). The executable has no third-party dependencies. Reproduce with `python check.py` and compare its last line against `check_output.txt`.

The asymptotic claim is not tested exhaustively: it follows from the explicit ratio bounds, the known extremal semigroup classification and a separate elementary unused-occupancy estimate in `RESULT.md`. An independent mathematical audit has not been performed.
