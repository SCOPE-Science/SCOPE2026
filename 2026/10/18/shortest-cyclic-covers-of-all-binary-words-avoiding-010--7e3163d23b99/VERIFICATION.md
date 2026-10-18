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

# Verification

`python3 verify.py` uses the Python standard library. For every integer from 3 through 12, it generates every legal length-n edge, verifies degree imbalances, independently computes exact BFS distances from each negative state to the set of positive states, checks the claimed matching as a bijection, reconstructs a balanced Eulerian multigraph, constructs a cyclic word, and verifies its cyclic avoidance and complete length-n coverage. It independently counts all relevant suffix words and checks the coefficient formula. For n=3 and n=4 it exhaustively excludes every shorter binary cycle and finds an optimal cycle.

The generated output is provided in `checks.txt`; the actual finite calculations were replayed. The proof for arbitrary n is the combinatorial argument in `RESULT.md`, not an extrapolation from finite cases. No independent external audit has occurred.
