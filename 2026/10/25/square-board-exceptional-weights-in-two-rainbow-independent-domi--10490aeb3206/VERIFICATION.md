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

# Reproducible verification

Run `python3 verify.py` with Python 3 and its standard library. The complete recorded stdout is in `verification_output.txt`.

The checker enumerates every ternary cell labeling (not merely rook placements) for \((p,q)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)\), totaling 617,544 assignments. It also enumerates every ordered pair of nonattacking rook placements for \((p,q)=(2,6),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6)\), totaling 20,260,210 pairs; a preliminary exact neighborhood-complement test filters candidates and every accepted candidate is replayed against the original definition. There are 326,838 valid second-stage functions, and all graded counts agree with the closed formulas.

The code's admissibility predicate uses only row-column graph adjacency, colorwise independence, and the two-neighbor condition for zero cells. The predicted coefficients are computed independently from falling-factorial and derangement sums. This is a finite stress test and does not prove the formulas for arbitrary board sizes; the proof in `RESULT.md` establishes the universal statement.
