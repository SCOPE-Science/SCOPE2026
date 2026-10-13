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
# Verification

Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the induced graph from the ternary length-\(3\) overlap rule. For every deleted vertex, it checks the supplied order is a permutation of the remaining \(16\) vertices, orients all edges forward, enumerates every directed path, and verifies that any directed path of at least three edges whose endpoints are adjacent has a clique as its vertex set. Hence no orientation contains a shortcut.

The new positive certificates are completely replayed from the embedded data. The undeleted graph's non-word-representability is a published theorem and is not re-certified computationally here.

Independent audit has not been performed.
