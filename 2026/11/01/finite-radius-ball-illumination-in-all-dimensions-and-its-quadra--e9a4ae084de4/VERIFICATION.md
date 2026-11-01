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

The proof in `RESULT.md` covers every integer dimension \(n\ge3\) and positive radii \(r<R\). The accompanying `verify.py` uses `mpmath` quadrature for the cross-sectional formula, compares independently to the elementary planar circular-arc area in \(n=2\), and tests endpoint expansions at two rational radius pairs for dimensions \(2,3,4,6\). It reports 140 finite checks passed. To reproduce, install `requirements.txt` and execute `python verify.py` in the directory containing these files.

The finite checks are not an infinite proof. Strict hull nesting and the beta-function derivative are proved analytically, not inferred from samples. Scientific historical priority is not independently established; no external audit was performed.
