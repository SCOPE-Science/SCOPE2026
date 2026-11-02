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

## Reproducible checks

The standalone standard-library `verify.py` generates optimum witnesses for all even alphabet sizes from \(2\) to \(30\), checks that every target \(a b\bar b\bar a\) occurs as a literal circular or linear factor, counts all chosen overlap distances, and independently solves the complete target ordering problem by Held–Karp dynamic programming for the first two alphabets \(q=2,4\).

Expected results: \((L_{\mathrm{cyc}},L_{\mathrm{lin}})=(9,10)\) for \(q=2\) and \((38,39)\) for \(q=4\), with the final line `VERIFY_OK`.

These checks validate finite instances and explicit witnesses. The all-even-alphabet theorem is proved by the partner-module lower bound and the Eulerian stitching construction in `RESULT.md`, not by extrapolation from tested sizes.
