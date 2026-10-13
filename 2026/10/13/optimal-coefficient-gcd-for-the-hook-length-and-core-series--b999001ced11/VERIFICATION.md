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

The general result is proved by integral-formal-series identities in `RESULT.md`. The executable tests below are **finite checks only** and confer no independent certification.

The bundled `verify.py` recomputes coefficients of both generating series from their distinct logarithmic-derivative recurrences, checks exact gcds, and reproduces the first prime-adic obstruction for each prime divisor of each integer \(2\le t\le40\). It also directly multiplies finite products for \(2\le t\le7\) and checks agreement coefficient by coefficient, independently of the recurrence method.

Run `python3 verify.py` from the directory containing the bundle. Recorded output is in `verification_output.txt`. It reports 39 parameter cases, 2,543 recurrence-based coefficients, 60 first-obstruction checks, and 228 independent direct-product coefficient comparisons. The tests use only exact integer operations from Python's standard library.

For an infinite proof, the decisive steps are: the Frobenius congruence \(E(x)^{p^r}\equiv E(x^{p^r})\pmod p\), the fact that raising a series congruent to \(1\pmod{p^s}\) to the \(p\)-th power raises the precision by one, and the explicit earliest nonzero coefficient in the reduced quotient. All of these are proven in the result text, including the binary boundary case.
