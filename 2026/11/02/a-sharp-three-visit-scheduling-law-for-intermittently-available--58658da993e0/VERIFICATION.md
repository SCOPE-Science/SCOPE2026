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

Reproduction requires Python 3 and the attached `check.py`; run `python3 check.py`. The checker enumerates all eight possible hidden availability triples with exact Fraction arithmetic for 729 combinations and independently evaluates the derived closed expression. It also tests 768 numerical parameter configurations for the clipped optimum and strictly positive midpoint convexity, checks invariance of the optimal hazard under four choices of the middle observation probability for each of 81 additional parameter configurations, and reports two numerical examples. It prints `PASS` on completion.

The all-parameter statement rests on the complete probability expansion, strict positivity of both exponential coefficients, and the monotone invertibility of the cumulative hazard. Enumeration is not a proof for continuously varying parameters. There has been no independent external audit, experimental field validation, or exhaustive historical-priority certification.
