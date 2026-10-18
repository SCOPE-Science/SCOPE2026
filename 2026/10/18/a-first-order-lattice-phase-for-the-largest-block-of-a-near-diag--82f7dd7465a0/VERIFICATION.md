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

# Reproduction

Use Python 3 and run `python3 verify.py`. The script requires only standard-library integer arithmetic, `fractions.Fraction`, and 75-digit `decimal.Decimal`.

The execution completed 96 assertions. Exact recurrence values of \(S(n,n-r)\) were compared against a separate enumeration of every possible finite block profile at small \(n\). Single-tripleton coefficients were checked with rational arithmetic. For \(m\in\{10,20,40,70\}\), two sample-size sequences \(n=m^2\) and \(n=m^2+2m\) were evaluated from exact integers, comparing finite values with their distinct predicted limits and the moving-intensity first-order correction.

Expected limiting scaled values at \(t=1\): \(-e^{-2/3}/9\) and \(11e^{-2/3}/9\). Finite checks use explicit tolerances and do not imply rigorous error bounds outside the tested sizes. The analytic proof in RESULT.md establishes the unrestricted asymptotic claim through profile enumeration, a Poisson-series truncation, and a summable majorant.
