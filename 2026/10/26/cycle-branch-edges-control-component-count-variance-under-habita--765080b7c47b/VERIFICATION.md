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

# Exact verification

`verify.py` uses Python's built-in `fractions.Fraction`, `itertools`, and `collections`, without external data or dependencies. Its complete exact output is embedded as `verification.json`. The checker obtains induced-component counts by graph traversal on every occupied subset, rather than by invoking the theorem's moment formula. For the two six-vertex networks it checks all fixed quotas and five Bernoulli probabilities. For every connected labeled unicyclic graph with at most five vertices it compares against a representative with the same degree sequence and girth. The proof of the universal identities is analytical and does not rely on this finite census. The full literature is not exhaustively certifiable, and no independent audit has occurred.
