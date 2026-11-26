---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Opposite fixed endpoints decouple the two arcs. Updating the interior sites from one endpoint in sequence to copy its opinion is a positive-rate path to the one-interface set, by sweeping away all other walls. A one-interface state remains in that set and the resulting reflecting walk is irreducible (with a singleton state on the one-edge arc). The arc count ratios are q and 1/q, so the stationary variance is the sum of the two truncated-geometric variances and is invariant under q to 1/q. Logarithmic differentiation twice gives W_L; at q=1 the uniform laws give (V_1,V_2,V_3)=(2,3/2,4/3), proving strictness at that endpoint. For q<1 the two exact differences have signs opposite P and Q at z=q+1/q. Each z-2 shifted polynomial has one Descartes sign change and a negative constant, establishing existence and uniqueness of a root above 2; opposite signs at z=27/10 strictly separate the roots. The map back to q reverses their ordering, and the sign comparisons give all three minimizing placements and the two exact ties. A separate exact symbolic and 16-state-generator replay, /workspace/branches/649dd4b5-5b89-417a-8842-335f1ed67568/replay_record3.py, with output in replay_record3_results.txt in the same directory, reproduced the factorizations, roots and all three q=4/9 fractions and verified V_2<V_3<V_1. Here the strict intermediate optimum is the discrete placement a=2 at fixed q, not an optimum over q. The uploaded checker was inspected but not executed. The general-in-q proof is analytic and does not rest on the finite generator comparisons.

## originality

PASS

The supported distinction is the full six-cycle minimum-variance classification, including the strict intermediate regime and the two ordered algebraic boundaries. The count-variance function itself and isolated evaluations of it are covered by the earlier opinion-biased-cycle law under reflection of one arc count. No separate originality is assigned to that variance formula, to the unbiased case, or to the fact that bias changes some placement objectives. The earlier exact law does not classify the crossings or the global minimum as bias varies.

## value

PASS

Stationary total-count fluctuations are a natural objective not captured by expected support or extreme-event probabilities. The first cycle with a genuinely intermediate spacing shows that neither endpoint placement is always best, on a nonempty open interval with exact boundaries and ties. This is a meaningful minimal model and a complete classification within it, not evidence of a larger-cycle phase law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
