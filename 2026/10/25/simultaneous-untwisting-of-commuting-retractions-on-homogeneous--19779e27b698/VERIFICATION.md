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

# Verification record
The included `verify_gacts_multi.py` is executable with Python 3 and the standard library, using `python verify_gacts_multi.py`. It constructs genuine finite group multiplication laws (cyclic groups, Klein four, and nonabelian \(S_3\)), composes group-labelled transformations from their definitions, detects idempotents, and compares direct ordered commutation-tuple counts against a separately enumerated base-family profile weighted by \(|W|^{n-c}\).

Successfully checked cases: \(n=2\), cyclic group order \(2\), four idempotents per tuple, total \(61\); \(n=3\), cyclic group order \(6\), tuple size \(4\), total \(35,641\); \(n=3\), nonabelian \(S_3\), tuple size \(4\), total \(35,641\); \(n=4\), cyclic group order \(4\), tuple size \(3\), total \(286,673\); and \(n=4\), Klein four, tuple size \(3\), total \(286,673\). In each case every product-rank cell matches. For \(S_3\) in size three, all \(8,137\) commuting ordered triples were additionally untwisted directly using the labels of their product and the inverse group multiplication table.

The observed final output is `VERIFY_OK simultaneous higher-arity group-labelled idempotents`.

Boundary: these are finite checks only. The proof in RESULT.md establishes unrestricted finite-group and finite-arity claims; no independent external assessment has been made.
