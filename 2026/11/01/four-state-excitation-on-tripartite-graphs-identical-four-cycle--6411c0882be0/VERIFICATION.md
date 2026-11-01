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

Run `python3 gh4_tripartite_verify.py` in a directory containing this file and the standalone checker. The recorded output file `gh4_tripartite_verify.out` is provided for comparison and ends with `GH4_TRIPARTITE_VERIFY_OK`. This checker has no nonstandard dependencies. It exhausts the exact support quotient, retains tagged representatives through coalescences, independently computes the cyclic-contact map, builds both coefficient tables, checks sharp depth witnesses and enumerates \(353600\) labelled microscopic input states. The reduction to tags is the mathematical reason this bounded finite check proves statements for arbitrary shore sizes; the direct microscopic checks alone would not.

The independent_audit front matter records unperformed external validation. Only the self-review represented here have been carried out. Historical-equivalence risks and the unavailable 1993 full paper are documented in the result and review.
