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

The cited June 2026 exact identity is an imported theorem. The independent calculations for this finding are the precise algebraic change of variables, monotonicity/uniqueness of the scalar stationary point, the global maximizer bounds, equations (2)–(4), and the final substitution. Both ends of the scalar objective vanish for every \(p>2\), so there is no overlooked boundary maximizer. The small-parameter remainder is uniform at the maximizing solution because \(y=\Theta(\varepsilon)\) and \(\varepsilon|\log y|\to0\).

`verify.py` (Python standard library) was executed successfully and compares a stationarity-root calculation against an independent golden-section maximum for several finite exponents. It also prints scaled asymptotic residuals. These finite checks support the formulas but do not establish an asymptotic identity by themselves.

No independent scientific audit has been carried out. Literature comparisons cannot rule out equivalent results outside the inspected sources.
