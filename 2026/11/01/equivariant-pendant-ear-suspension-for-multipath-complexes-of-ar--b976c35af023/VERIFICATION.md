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
# Verification and limits

The mathematical proof and the exact verified domain appear in `RESULT.md`. Reproduce the independent finite check using `python3 verify.py`, with a standard Python 3 interpreter; no network or nonstandard packages are required.

The executable independently constructs arc sets for the base digraph and each attached ear. It tests in/out-degree limits and detects all directed cycles, including two-cycles. For every admissible face in ten explicit attachment instances it checks that the retraction image is a valid face, the union with the face is a valid simplex (simplicial contiguity), the retraction is idempotent, and the retraction image equals exactly the asserted simplicial join. Cases include base directed cycles, fully bidirected triangles, repeated roots, and four ears on a single root.

It calculates the complete mod-two reduced chain ranks for once-subdivided stars with one through four arms. The resulting reduced Betti numbers are concentrated in degrees zero through three, respectively, each with rank one. It also checks every arm permutation and both orientation-reversal choices, on every enumerated face for those examples, and checks the claimed orientation character combinatorially.

The successful last output line is `BIDIRECTED_EAR_EQUIVARIANT_SUSPENSION_CHECKS_OK`. The all-order integral simple-homotopy and equivariant claims rely on the explicit contiguity and dominated-vertex proofs, not on these finite tests. This does not certify novelty or substitute for independent scientific review.
