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
# Verification record

The exact-rational checker `verify.py` uses only the Python standard library. Execute with `python3 verify.py` in the extracted directory. It checks the alternating-binomial and harmonic-number forms, the mixed-moment identity, both marginal variance expressions, and positivity in every dimension \(2\le n\le80\). It separately checks an exponential-order-statistic-increment computation for the mixed moment and independently integrates two small dimensional simplices, giving \(25/48\) and \(349/1080\) for \(n=2,3\) respectively. The observed run completed without errors.

The theorem's quantifier over all finite \(n\) is justified by the analytic beta-integral proof in `RESULT.md`, not by finite testing. No external theorem prover, independent researcher, publication claim, or full joint-distribution validation is asserted. The historical-priority comparison remains limited to the literature actually inspected.
