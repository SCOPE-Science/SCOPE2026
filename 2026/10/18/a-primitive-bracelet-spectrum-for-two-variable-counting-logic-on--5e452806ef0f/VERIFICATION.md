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

# Reproducibility and limits

Run `python pseudo_count.py` and `python pseudo_verify_independent.py` in an environment containing Python 3 and the dependency from `requirements.txt`. Both scripts must finish with successful assertions and show the ten class numbers `1 1 2 4 9 19 45 106 267 685` (printed as lists or as rowwise values). The second independently constructs unlabelled pseudoforests and also reports isomorphism-type numbers `1 1 2 4 9 19 46 108 273 696`.

`pseudo_count.py` obtains the exact formal-series factors from rooted/unrooted tree types and primitive bracelets. Its separate graph-atlas check tests class numbers through order seven. `pseudo_verify_independent.py` does not use the primitive-factor formula: it enumerates arbitrary decorated cyclic necklaces and tree multisets, constructs the associated finite graphs, and groups them by ordinary stable colour refinement through nine vertices. The actual assertions and encoded graph operations, not stored transcripts, are the finite computational evidence.

The universal-cover spine reconstruction and formal-product argument in `RESULT.md` prove the full unbounded-size statement. The finite enumerations do not certify originality or independently audit that proof. Different network-analysis library versions may produce different opaque hash strings, but equality-group counts are expected to remain unchanged. The class is restricted to simple undirected pseudoforests without vertex colours. This package does not include a third-party scientific validation.
