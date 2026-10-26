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

# Reproducibility and limits

Execute `python3 verify.py` with Python 3.9 or later from a directory containing `verify.py` and `canonical_table.json`; only the standard library is required. The script rebuilds all twenty-eight Cartesian-product adjacency matrices, computes complete rank-three logical types through ordered-triple atomic diagrams, checks the embedded classification, and independently plays the adversarial three-round game on all sixty-six pairs of class representatives. It confirms equality on representative cross-shape comparisons and samples beyond the cutoff. The finite computation reports `VERIFY_OK`; complete recorded output appears in `verification_output.txt`.

The type recursion and direct-game recursion are distinct algorithms. The direct game checks all class separations, not all twenty-eight by twenty-eight pairs; complete type equality checks all memberships. The samples for parameters exceeding seven are illustrative only. The infinite family follows from the self-contained path cutoff and product preservation proof in `RESULT.md`. No claim about higher quantifier ranks, other graph products, or independent validation is made.
