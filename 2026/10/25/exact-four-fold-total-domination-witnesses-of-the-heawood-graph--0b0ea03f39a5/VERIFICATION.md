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

A reproducibility script, `verify.py`, uses Python 3 standard library only. Run `python verify.py` next to this document. It enumerates \(6^7\) Fano-plane assignments without symmetry pruning; a separate exhaustive search of the four off-line labels verifies the normalized eight-choice lemma. It independently constructs the \(168\) invertible linear transformations of \(\mathbb F_2^3\), evaluates the \(24\) permutations of the four names and compares the resulting orbit to the complete accepted assignment set. Finally, it verifies both family counts and divisibility by \(24\). The attached `verify_output.txt` records the actual results and concludes `VERIFY_OK`.

The proof in `RESULT.md` establishes completeness without relying on experimental extrapolation. The code serves as a second finite exhaustive check. The result does not assert anything about larger cubic graphs, arbitrary list colorings, or counting families with merely at-most-two membership. No independent external mathematical audit has been performed.
