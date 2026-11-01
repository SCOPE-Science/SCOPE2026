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
Execute `python3 verification/verify.py` from the root of this package. It requires only the Python 3 standard library. No outside data or network calls are made. It prints the integral Morse boundary and exact equivariant Lefschetz table and ends with `VERIFY_OK` if every assertion succeeds. The output generated during the review is in `verification/output.txt`.

The procedure separately constructs the generalized Petersen and permutation-star models, verifies the explicit graph isomorphism, and proves full symmetry-group order using a pointwise-stabilizer coloring. It checks all 35,219 augmented independent subsets, all 17,605 matching pairs, the acyclic Hasse orientation, six-by-three signed integral boundary, all 144 group actions, and exact character inner products over the rationals. The preserved recorded output is a reproducibility check, not an independent review.

This certificate proves a finite rational homology representation for the named graph. It does not certify any equivariant integral splitting, an infinite family, independent publication priority, or independent mathematical review.
