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

# Verification of the strict cycle–descent association

Run `python3 verify.py` under Python 3 using the standard library. The script returns `PASS: 3295 exact checks` on the supplied source. Assertions employ `fractions.Fraction` throughout for exact rational arithmetic. The checks enumerate every fixed-point-free permutation for each size from two through eight, for each of four Ewens parameters, and compare the directly computed mixed moments with the formula obtained by marking a two-cycle. They also verify the conjugacy-class conditional descent identity in the actually encountered classes, the two-variable stochastic sandwich through size 35, and the negative unconditioned covariance through size eight.

The all-size and all-positive-real-parameter conclusions are established by the analytic argument in RESULT.md. The finite test program is neither an infinite proof nor an independent audit. Historical priority has not been independently validated.
