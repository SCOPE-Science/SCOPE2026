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
# Reproduction and limits

Run `python3 verify.py` using Python's standard library. The verifier enumerates all acyclic subsets of \(n-2\) edges of \(K_n\) for \(2\le n\le8\); verifies the forest normalizer, the full joint \((Q,D)\) probabilities with exact rational arithmetic, \(\mathbb E S\), \(\mathbb E S^2\), the exact covariance, and strict adjacent binomial likelihood ratios. All 240 comparisons pass. The precise total for \(n=8\) is 200704 forests.

Verification is finite evidence only; the infinite statements are justified by the displayed analytical proof. The Green-matrix identity for two-point floating inclusion is credited to the named prior literature. No independent audit or external certification has been performed.
