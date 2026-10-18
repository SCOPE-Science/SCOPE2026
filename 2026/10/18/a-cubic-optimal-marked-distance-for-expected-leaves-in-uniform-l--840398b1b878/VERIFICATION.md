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

The exact-rational `verify.py` can be executed under standard Python 3 without third-party libraries. Its output from the complete packaged source is `passed 994 exact assertions`.

The checks enumerate all labeled trees via Prüfer codes for sizes two through seven. For every marked distance they independently compute the number of trees, the conditional expected total leaves, marked-endpoint leaves, off-path leaves and adjacent conditional-mean differences. For sizes two through three hundred they also verify exact arithmetic signs and every maximizing index.

The proof for arbitrary sizes is the forest-extension count, leaf-deletion bijection, exact rational difference factorization, and explicit asymptotic expansion. Exhaustive checks through seven vertices and finite checks through three hundred are not claims of exhaustive verification for larger sizes. Historical novelty has not been independently certified.
