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

The standalone `verify.py` constructs exact rook-graph adjacency bit masks without consulting theorem formulas, enumerates all possible vertex subsets on ten specified small boards, tests dominating and capacity constraints directly, and compares the minimum size, number of minimizers, and proposed structural classification with explicit coefficient computations. It tests all positive capacities through the degree on each board (49 cases). See `verification_output.txt` for the observed successful run.

The exhaustive finite tests do not constitute a proof for unbounded dimensions. The unrestricted result depends on the four case-splitting arguments and coefficient extraction in `RESULT.md`. The bibliographic investigation does not establish absolute priority, and an independent mathematical audit has not been performed.
