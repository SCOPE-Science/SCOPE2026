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
Run `python verify_ewens_cumulant.py` with Python 3 and SymPy installed. The checker verifies the exact third-cumulant rational factorization, its special values at 0, 2 and 3, positivity-relevant derivative identity, and the two-term root-scale expansion. Its independent branch enumerates integer partitions for \(6\le n\le12\) and all seven parameters \(1/2,1,2,3,5,9,20\) with exact rational Ewens weights; 49 full-distribution comparisons pass.

The proof for every integer \(n\ge6\) and every real \(\theta>0\) is in RESULT.md and does not depend on finite enumeration. A general claim for other block-size triples is not established; independent audit and external priority verification have not been performed.
