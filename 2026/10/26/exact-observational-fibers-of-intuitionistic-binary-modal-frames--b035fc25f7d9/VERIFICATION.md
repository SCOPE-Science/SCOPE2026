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

# Reproducibility and verified limits

Run `python3 checker.py` with the standard Python library; no external files or dependencies are needed. The checker evaluates the published ternary monotonicity conditions from their original quantifiers, and also evaluates the proposed row-downset and suffix-upset conditions. It independently computes the binary-modal operations on all hereditary input truth sets, and compares these to the reconstructed modal observational records. All ternary relations over one and two ordered worlds are checked, including empty and illegal relations. Legal frames are grouped by both semantic signatures and shadow signatures, and each actual fiber size is compared with its predicted Boolean-interval cardinality.

Observed counts: \(n=1\): 2 tested, 2 legal, 2 observational classes, maximum fiber 1. \(n=2\): 256 tested, 67 legal, 45 classes, maximum fiber 8, fiber multiplicities 33 of size 1, 9 of size 2, 2 of size 4, and 1 of size 8. The implementation additionally tests 5,000 nontrivial legal three-world relations and samples the sharp class of cardinality \(2^{16}=65{,}536\). It finishes with `ALL_CHECKS_OK`.

The symbolic proof in RESULT.md is required for the claims for all \(n\ge1\). Finite samples do not prove the general claims, determine publication priority, or constitute independent validation. The entire study assumes fixed finite chain orders and standard hereditary valuations; no claim about stronger frame equivalences is tested or inferred.
