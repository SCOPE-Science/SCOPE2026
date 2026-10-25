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

# Verification of the grid visibility polynomials

All numerical assertions are integers obtained by exhaustive finite enumeration; no random sampling or external software dependency is involved. Execute `python3 verify_grid.py` and `python3 verify_paths.py` from the same directory. Both completed successfully during preparation of this package. The first enumerates all exact bounding boxes up to \(4\times4\) and uses a distance-decreasing graph search; the second independently enumerates every monotone shortest route as an interior-vertex bitmask before counting each size. Both certify every coefficient of the 16-box table for \(k=2\) and \(k=3\), including zero cases.

The mathematical locality reduction is essential: any selected pair must have Manhattan distance at most \(k\), so the occupied row and column spans cannot exceed \(k\). Every shortest path lies inside its endpoint bounding rectangle; this makes the finite classification exhaustive for all ambient dimensions. The formula sums disjoint anchored types with exactly \((m-h+1)_+(n-w+1)_+\) translations. No calculation alone is treated as proof of a claim outside the reduced finite universe.

For \(G_{3,3}\), the two polynomial coefficient vectors from constant to highest degree are `(1,9,26,24,1)` and `(1,9,34,64,29,4)`; for \(G_{4,4}\) at distance three they are `(1,16,90,212,140,32,4)`. Both code paths reproduce the underlying anchored table. Limitations: no check of \(k>3\), unrestricted grids of more than two factors, or independent human assessment.
