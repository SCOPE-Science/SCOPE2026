---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Read the printed Eq. (12) and state-space definitions, not just the checker. The entire active f5 block has a homogeneous right-hand side along any trajectory of the other compartments: every incoming, neighboring or loss term contains an active f5 factor. The terminal j=1 and j=m levels are classified into separate endpoint compartments on pp. 296–297 and are not additional f5 coordinates feeding into Z; the endpoint transfers appear in the aggregate equations. For arbitrary finite m, setting the entire block to zero therefore solves its equation, and local polynomial uniqueness on each transmission interval and continuity at switches imply invariance. Nonnegative data stay nonnegative (gains are nonnegative on the boundary of the orthant), and summing (12) telescopes the adjacent transfers and cancels transfers between compartments by Eq. (1), so the normalized solution is globally bounded and extends. The finite-grid checker is only corroborative and does not independently settle the terminal-state convention. The finding concerns the simultaneous zero block and does not say that individually zero coordinates in a nonzero block cannot become nonzero. The source confirms nonzero initial variant state in §4 and its stated value in Figures 6–8, not an inference from numerical curves.

## originality

PASS

The general zero-solution argument is standard and the nonzero initialization is already explicit in the article. Neither is claimed as new. The supported distinct finding is that the printed equation cannot represent endogenous appearance from exactly variant-free data, despite the surrounding mutation-onset framing. The closest indexed records use related zero-face reasoning, but apply it to different equations and conclusions.

## value

PASS

The distinction between generation of a state from zero and evolution of a state already present changes what a reader can infer from the article's simulations. The proof diagnoses a precise limitation of the printed model under a natural initial condition, rather than presenting coordinate invariance as a new mathematical technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
