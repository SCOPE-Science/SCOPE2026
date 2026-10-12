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

The mathematical proof uses the connected-flacet criterion for matroid base polytopes, the exact toric divisor sequence, and an explicit integral spanning argument. The computation is supplementary, not an infinite proof.

To reproduce the exact finite test, run `python3 checker.py` in the directory containing the supplied files. The program uses only the Python standard library. It enumerates all labeled spanning trees of complete graphs on four, five, and six vertices, checks every candidate local-rank formula, and verifies proposed facet dimensions for the two smaller sizes using finite-field exact elimination. The output should match `checker_output.txt`.

A self-review addressed correctness, originality and value. No independent audit or outside mathematical validation has been performed. Literature searches are not a proof of novelty, and exact historical specialization may remain unindexed.
