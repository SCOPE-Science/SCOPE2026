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

The proof derives the exact three local equations for each cubic ladder, rules out identical rim words, and establishes the forced strict period-four sequence plus alternating rungs. Closure constraints yield the two congruence conditions. Three independent starting bits give eight solutions, and proper three-edge-colourings finish both upper bounds. These are mathematical arguments for all permitted orders, not finite extrapolation.

The accompanying `verify.py` reconstructs simple graphs directly from endpoint lists, verifies four edge-neighbours on every edge, and checks the majority criterion without reusing the theorem's recurrence. Exhaustive cases cover nine small graph/order pairs. Independent binary mixed-integer feasibility checks cover 157 cases, and 477 constructive instances are checked; details and success counts are in `verification_output.txt`. The MILP solver returns an explicit feasible assignment or an integer infeasibility decision in each reported case. The finite checks neither certify every order nor establish bibliographic originality.

Install `requirements.txt`, then run `python verify.py` in a folder containing these three files; compare output with `verification_output.txt`. Independent audit has not been performed.
