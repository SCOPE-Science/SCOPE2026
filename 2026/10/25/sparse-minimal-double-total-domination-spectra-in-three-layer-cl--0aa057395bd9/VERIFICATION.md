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

# Reproducibility checks

Execute `python3 verify.py` using Python 3. The program builds the graph's open neighborhoods from its definition and verifies every double-total-domination predicate and each selected-vertex deletion for all sets in orders \(n=3,4,5,6,7\). It additionally compares the complete inclusion-minimal classification and cardinality polynomial for \(n=6\) and \(n=7\). The 2,396,672 tested subsets do not logically prove the all-order result, which is supplied by the algebraic case analysis in RESULT.md. The proof explicitly excludes \(n<6\) from the claimed formula. No external mathematical audit or independent certification is asserted.
