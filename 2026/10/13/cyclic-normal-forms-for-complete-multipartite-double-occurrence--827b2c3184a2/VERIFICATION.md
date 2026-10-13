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

# Reproducibility

Run `python3 verify.py` using Python 3 standard library. The script derives alternation from positions of the two occurrences; it does not use the normal-form theorem as its test for whether a word represents a multipartite graph. Canonical restricted-growth words are exhaustively generated for 2 through 7 distinct labels, and eight small labeled multipartite instances are enumerated in full.

Expected success includes:

```text
CANONICAL_OK n=7 exhaustive_words=135135 multipartite_words=120
LABELED_OK parts=(1, 1, 1, 2) words=60 predicted=60
VERIFY_OK complete_multipartite_cyclic_normal_form
```

Coverage limits: this is an exhaustive finite census only through seven labels (canonical) and five labels (labeled examples). It cannot certify all larger graphs; the universal proof is provided in RESULT.md. No independent audit has occurred.
