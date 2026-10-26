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

The complete-graph update rule was independently implemented in standalone `verify.py` using integer and exact rational arithmetic. The test checks strict hinge-potential improvement after all nontrivial activations, absorbing-profile classification, and the longest switching path in every tested state. The executed test covered 5700 payoff/type cases, 171120 states, 945888 possible individual activations, the all-imitator four-player tied example, and sharp switching constructions for sizes 2 through 14. The script requires Python 3 standard library only.

These finite checks do not certify the universal theorem; that depends on the symbolic sign proof in `RESULT.md`. No external or independent scientific audit has been performed. The work does not address simultaneous updating, heterogeneous payoffs, or other tie conventions.
