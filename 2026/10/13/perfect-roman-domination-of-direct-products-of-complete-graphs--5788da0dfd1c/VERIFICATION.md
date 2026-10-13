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

# Computational verification

The stand-alone Python standard-library script `verify.py` defines the tensor-product adjacency masks from the coordinate inequalities and calculates the minimum feasible weight for each chosen two-label support. In the seven small-board exhaustive support tests, it verifies the bound, the exact minimum count, and the complete distribution of support sizes among minima. Independent ternary enumeration on two boards explicitly checks the perfect Roman constraint without assuming the support reduction. These two independent methods agree.

Exhaustive support instances: \((3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3)\), totaling \(1,188,352\) support masks. Exhaustive full-label instances: \((3,3),(3,4)\), totaling \(551,124\) assignments. Four further rectangular boards receive deterministic test samples and all support subsets up to size three.

The captured exact stdout is in `verification_output.txt`; run `python3 verify.py` from the same directory to reproduce it. Neither random samples nor finite exhaustive calculations certify any parameters outside their examined range. The general lower bound, classification, and count require the symbolic proof in `RESULT.md`.
