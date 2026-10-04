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

Run `python3 verify.py` in the directory containing `verify.py` and `strategy_certificate.json`.

The verifier independently reconstructs the hypercube adjacency relation and the partial-feedback legal responses. At every certified state it enumerates every simultaneous response tuple that can arise from a currently possible robber vertex, recomputes the exact consistency class, and checks that each nonterminal class expands to a certified child under the robber's stay-or-neighbor move. It also rejects unreachable filler states.

The packaged certificate proves only the upper bounds \(\operatorname{dirloc}(Q_3)\le3\) and \(\operatorname{dirloc}(Q_4)\le4\). The matching lower bounds are taken from the published hypercube dichotomy in arXiv:2609.01745v1. The finite verification is exhaustive for the two supplied strategy trees but is not evidence for any \(Q_n\) with \(n\ge5\).

Expected final line: `ALL CHECKS PASSED`.
