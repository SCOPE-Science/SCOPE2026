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

Run `python3 verify_endofunctions.py` in the same directory as `verification_output.txt`. It uses only Python's standard library; a comparison with the saved output can be made by redirecting stdout. The program generates each of the `n ** n` maps for each `n` from 1 through 6, forms a primitive-necklace signature from rooted in-tree encodings and cycle rotations, and independently refines the finite directed relation using loop/reciprocal flags, the unique forward neighbor, and backward-neighbor color counts. It checks equality of all resulting partitions. It additionally canonicalizes complete decorated-cycle necklaces to count isomorphism types and certify the unique collision layer at six points. The observed counts are 1, 3, 7, 19, 47, 129 for logical classes, and 130 for six-point isomorphism types.

These finite checks cannot establish the unrestricted theorem. That proof uses two-variable-definability and balanced equitable partitions as presented in RESULT.md. No external formal verification or independent audit has been performed.
