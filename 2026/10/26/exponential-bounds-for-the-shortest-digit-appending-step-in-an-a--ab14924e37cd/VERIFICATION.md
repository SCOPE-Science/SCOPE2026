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

Run the included `verify.py` with Python 3. Its exact-integer search returns `VERIFY_OK: 10 power, 6 shifted-power, 6 negative-root cases`. The tested families have one simple dominant root and independent base: \(a_n=2^n\) in base \(10\), \(a_n=3^n+1\) in base \(2\), and \(a_n=(-2)^n\) in base \(10\). The tests independently check the appended-digit inequality, step index ordering, and positive block length for the first known witnesses; finite experiments do not establish infinite claims.

The analytical verification of the theorem has four parts: (1) the Binet error ratio is uniform in the index increment; (2) every step gives an exponentially small nonzero logarithmic form, which Baker–Wüstholz bounds below polynomially in its integer coefficients; (3) the irrational rotation \(\log_b r\) has polynomial discrepancy for all shifted index blocks by Erdős–Turán; (4) a visit to an interval of length \(\asymp r^{-m}\) at an exponentially large even-adjusted index produces an actual signed digit block because the residual characteristic-root contribution becomes less than one third of a unit.

Boundaries: \(m\) must be sufficiently large, the dominant root may be negative but must be simple and unique in modulus, the base must be multiplicatively independent of its absolute value, and the theorem specifies exponential **order** only. No independent audit is asserted.
