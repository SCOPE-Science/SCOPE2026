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

The standalone `artifacts/verify_tree_collision.py` uses only Python 3 standard-library modules. Execute `python3 artifacts/verify_tree_collision.py` from the directory containing the files. Successful output ends in `VERIFY_OK` and prints per-order unlabeled tree counts, number of matching-profile collisions, the complete coefficient certificate, and sample field multiplicities.

The tree classification enumerates all isomorphism classes of orders 1 through 10 using leaf attachments and exact rooted-center canonical codes. Every edge-support subset is checked. The independent skew-matrix rank tests cover each of the 512 supports of both explicit ten-vertex trees over each of the fields of sizes 3 and 5. The equal-spectrum claim for **all** odd fields is proved via identity of the integer matching-support polynomials and the established rank-to-character formula, not by extrapolating the sample tests.

No full-character-table equality or independent audit is claimed. Mathematical provenance and residual overlap uncertainties are set out in the result and review.
