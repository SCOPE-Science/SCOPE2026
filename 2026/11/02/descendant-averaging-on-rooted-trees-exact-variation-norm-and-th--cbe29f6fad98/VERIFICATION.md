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

# Verification of the finite-tree variation theorem

The proof consists of an exact subtree-indicator coordinate expansion, a telescoping calculation for each averaged indicator, an exhaustive branching argument for the contraction criterion, and upper and lower bounds for the size-extremal limit. None of those arguments depends on a numerical fit.

Execute `python verify_tree_subtree_bv.py` with Python 3.9 or later and no external packages. The verified test execution reported: `PASS 8726 exact rooted-tree tests; 5957 noncontractive cases; ratio samples: [(100, 0.29964706), (400, 0.33123523), (1600, 0.34895674), (6400, 0.35826159)]`.

All comparison values are computed directly as fractions from the defining averages. The checker exhausts rooted labeled trees of sizes two through six, supplements these with 250 randomized trees, and evaluates four explicit increasing-size constructions. Finite tests cannot establish the universal norm formula or the asymptotic coefficient; proof steps in RESULT.md establish those statements. No independent audit or formal proof-assistant certificate has been performed.
