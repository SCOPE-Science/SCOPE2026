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

# Verification

The runnable, standalone `verify_spider.py` uses Python 3 and SymPy (declared in `requirements.txt`). It constructs the actual weighted Laplacian for each graph, grounds each unordered two-vertex leader set, and evaluates the inverse trace using exact rational arithmetic for \(k\in\{3,4,5,6\}\) and \(t\in\{1/7,1/2,1,3/2,7/2\}\). It checks each result against the corresponding one of six symbolic orbit formulas, then verifies the complete optimizing orbit set for each parameter. There are exactly 950 direct grounded-matrix inversions. Additional algebraic assertions verify the crucial rational identities and positivity-slope expressions for the analytic all-parameter proof.

Invocation: `python verify_spider.py` from a directory containing that file and the declared SymPy dependency.

Successful actual execution output:

`VERIFY_OK: 950 exact grounded-Laplacian inversions; complete orbit formulas; two exact parameter regimes; symbolic difference certificates.`

Numerical or finite exact tests alone do not establish the full real-parameter classification; the analytical Green-function and sign arguments in RESULT.md do. One closely relevant later paper was not available as full text and remains an originality limitation. No independent verification or audit is asserted.
