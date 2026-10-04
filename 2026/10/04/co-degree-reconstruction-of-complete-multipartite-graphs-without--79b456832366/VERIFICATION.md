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

The theorem is proved symbolically in `RESULT.md`. The executable check is a finite stress test of two logically separate ingredients.

First, for every integer partition of every order \\(4\\le n\\le30\\) with at least two parts and every part of size at least \\(2\\), `verify.py` computes the exact defect frequencies and applies the displayed triangular recurrence. All \\(5574\\) tested multipartite types reconstruct to the original part-size multiset.

Second, for every such type with \\(n\\le12\\), the verifier explicitly builds the vertex partition, enumerates every unordered vertex pair, counts common neighbors from adjacency, and checks that these direct defects equal the formula used by the recurrence. All \\(65\\) tested types pass.

Expected output:

`ALL CHECKS PASSED; reconstructed_types=5574; direct_types=65; max_order=30`

The finite census does not establish the infinite theorem; it checks the implementation and boundary bookkeeping against the analytical proof. Singleton parts are outside the proved scope and are not silently inferred by the verifier.
