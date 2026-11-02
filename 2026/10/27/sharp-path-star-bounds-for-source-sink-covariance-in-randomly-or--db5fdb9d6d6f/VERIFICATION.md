---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For a fixed simple tree, source/sink indicator at a vertex has marginal q_v=2^{-d_v}; diagonal cross covariance is −q_v² and the only off-diagonal dependence occurs at adjacent ordered pairs, each contributing q_u q_v. Summation gives 2Σ_edges q_uq_v−Σ_vertices q_v². Substitution yields path (n−4)/16 and star (n−1)/2^(n−1)−(n−1)/4−4^−(n−1). For any nonstar, at most n−2 leaves and at least two leaf edges give a strict lower bound above star. For any nonpath, detach one pendant arm from an extremal branch vertex and attach it to another arm terminal; the exact covariance gain is ≥5/64, branch excess drops by one, and iteration reaches the path. n=2 and n=3 are handled separately. Independently enumerated every orientation of 47 unlabeled trees n=2..8 and reproduced the local formula and both extremal inequalities. Finite enumeration is diagnostic, not the general argument.

## originality

PASS

Best-of-knowledge: primary same-object comparisons, alias/implication checks and published finding searches distinguish the assessed exact statement from covered components. Historical priority uncertainty is retained; failed search is not novelty proof.

## value

PASS

Sharp sign-changing mixed count covariance provides a complete extremal shape classification under the natural uniform orientation ensemble and explains why the path and star respectively optimize the observable. The strict pendant-path transformation and finite-size sign boundary are useful structural mechanisms in probabilistic graph orientation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
