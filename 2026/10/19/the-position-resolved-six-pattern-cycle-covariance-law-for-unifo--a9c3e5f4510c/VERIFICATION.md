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

# Reproducibility and exact checks

Execute `python verify.py` with Python 3.9 or newer; no external packages are required. The script independently traverses the cycles of all permutations through eight elements, computes the complete six-pattern positional covariance table using exact fractions, and compares every entry with the claimed rational formula. It also reconstructs the prescribed one/two/three-cycle counts from their elementary image-rank constraints over the full parameter ranges \(3\le n\le150\), \(1\le i\le n-2\). The run produced `PASS: 66282 independent finite checks, n=3..8 exhaustive; n=3..150 combinatorial`.

The accompanying proof establishes all sizes via the contraction lemma and exact symbolic counting. The finite checks are not a proof for unbounded \(n\); no independent audit, formal certificate, or external validation has been performed. The newest result's provenance is limited to the cited scientific material and the supplied reproducible checks.
