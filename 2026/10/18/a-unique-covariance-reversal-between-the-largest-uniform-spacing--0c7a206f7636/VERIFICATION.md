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

The standalone `verify.py` uses only Python's standard library. Execute `python3 verify.py` in the directory containing this document and the program. The recorded execution completed with `PASS: 1037 exact rational assertions`.

The program compares two mathematically independent finite-sum calculations of the covariance: (a) a tagged-coordinate stop-loss distribution found by integrating simplex subset volumes, and (b) inclusion–exclusion for the mixed moment \(\mathbb E[M_m\mathbf1\{X_1>t\}]\). These calculations agree exactly, using rational arithmetic, for dimensions \(2\) through \(12\) over many rational thresholds. Boundary values, rational monotonicity samples, the two-spacing exact threshold, the three-spacing cubic segment, and signs bracketing thresholds are checked.

Unrestricted correctness requires the analytic proof in `RESULT.md`. The finite checks do not establish strict monotonicity for all real thresholds or the double-logarithmic asymptotic. Those statements are established by the stop-loss expectation argument and the uniform exponential-race estimate, respectively. No independent audit or external proof certification has been undertaken.
