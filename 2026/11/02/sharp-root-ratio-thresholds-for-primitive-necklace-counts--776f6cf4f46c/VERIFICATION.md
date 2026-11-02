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

# Verification evidence

The standalone source `verify.py` uses Python 3's standard-library integer arithmetic and `fractions.Fraction`. Execute `python3 verify.py` in the package directory. Successful execution prints:

```text
VERIFY_OK finite_suffix=115 exact_witnesses=7 inversion_cases=168
CHECK_OK analytic_rational_inequalities=8
```

The 115 assertions compare exact integer powers equivalent to the required strict root-ratio inequality over every \(q\in\{2,3,4,5,6,7,8\}\) at every \(T(q)\le n\le22\). Each of the seven immediately preceding indices is independently checked to have the reverse strict sign. The 168 separate Möbius-inversion identities are checked for \(q=2,\ldots,8\) and \(n=1,\ldots,24\). Rational assertions separately check simple numerical inequalities used in the analytic proof. The source's complete code is supplied; no network, external package, floating-point comparison, or hidden certificate is required.

The source file's finite tests do **not** certify infinite index ranges by enumeration. Those are proved in RESULT.md from the explicit analytic remainder estimate, a ratio induction beginning at \(n=6\) for \(q\ge9\), another beginning at \(n=23\) for all \(q\ge2\), and closed-form small-index estimates. There has been no independent mathematical audit.
