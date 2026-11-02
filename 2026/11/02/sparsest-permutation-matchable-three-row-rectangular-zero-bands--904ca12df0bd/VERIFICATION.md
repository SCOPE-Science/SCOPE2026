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
The proof checks every nonempty row subset through the six equivalent inequalities \(d_i\ge\lceil q/3\rceil\) and \(a_i\le\lfloor q/3\rfloor\). The only imported non-elementary statement is the established balanced-weighting/matching equivalence cited in the main text.

The included `verify.py` exhaustively enumerates multisets of the seven possible nonempty column supports and multiplies by the multinomial number of labeled arrangements. The code compares computed minima and minimizer counts with the analytic result for \(1\le q\le10\), printing `ALL_CHECKS_PASSED`. Computations do not substitute for the proof at unbounded \(q\).

Independent audit has not been performed; there is no claim of independent certification.
