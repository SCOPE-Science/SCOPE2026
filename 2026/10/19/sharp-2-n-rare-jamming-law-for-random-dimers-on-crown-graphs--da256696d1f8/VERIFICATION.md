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
# Finite checks and limits

Run `python verify_crown_jamming.py` using the standard library. The checker computes two logically separate exact-rational processes: the intersection-state reduction and direct recursion over subsets of unmatched left/right vertices. It also exhaustively checks all \(720\) orders of the six edges for the smallest connected crown graph (\(n=3\)), compares the finite-size probability bounds, and checks the second factorial-moment inequalities for \(n=2,\ldots,17\). The finite checks confirm the implementation at tested sizes; the inequalities for unbounded \(n\) follow from the analytic proof in RESULT.md.

The full texts of some older broad matching papers were inaccessible; bibliographic completeness and historical novelty cannot be formally certified. No independent scientific audit has been performed.
