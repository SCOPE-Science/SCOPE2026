---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The unconditioned discrete-time Moran absorption problem has transient states the nonempty proper mutant subsets S, birth-death transition probabilities 1/(n deg(u)) for each oriented disagreeing edge, and self-loops for unchanged attempts. First-step conditioning gives (I-Q)a=1, (I-Q)b=2a-1; mixture over all singleton starts gives mean (1/n)sum a_singleton and variance (1/n)sum b_singleton minus the squared mixture mean. Independent exact rational linear algebra reimplemented from the model, rather than from saved outputs, exhaustively tested the 0, 3, 84 and 3140 labeled connected-graph/nonedge cases for orders 2,3,4,5 (zero discordant signs). Both six-vertex displayed edge-insertion witnesses were recomputed exactly, including the full four huge rational differences, and have opposite strict mean/variance signs in both possible directions. Exhaustion proves only <=5 lower bound; n=6 examples prove upper bound, not six-vertex uniqueness.

## originality

PASS

The model and absorbing-chain moment recurrences are prior. The claimed six-vertex sharp threshold combines unconditioned extinction-or-fixation mean and variance changes, unlike the conditional fixation-time counterexamples and unconditioned expectation bound literature. A fresh exact mathematical comparison of the closest primary statements and semantic published-record searches uncovered no implication of the paired strict sign patterns or sharp minimum, but priority under alternative voter/coalescent consensus-time terminology remains a real risk.

## value

PASS

Mean absorption duration and its variance quantify genuinely different stability/risk dimensions in evolutionary stochastic networks. A single-edge intervention can improve expectation while worsening fluctuation or vice versa, first possible at a sharp graph order, making the finite cutoff and both directions a meaningful complete qualitative boundary. This is not merely a known mean phenomenon reworded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
