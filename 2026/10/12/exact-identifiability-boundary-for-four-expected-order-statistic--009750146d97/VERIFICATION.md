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

The analytic proof reduces four expected order statistics to the first two moments of the Okolewski--Papadatos generator. With \(a,b,c\) denoting consecutive gaps and \(S=3a+4b+3c\), the generator variance is exactly
\[
\frac{9ac-4b^2}{S^2}.
\]
This proves the identification boundary after combining zero variance with the published one-to-one generator/normalized-parent correspondence.

The standalone script `verify_four_eos_identifiability.py` checks the displayed boundary reconstruction on twenty-seven rational two-point parents. For five strict-interior gap triples and four parameter values per triple, it checks the two-atom generator moments, builds the displayed three-point parent, and recomputes all four expected order statistics directly from the discrete order-statistic distribution. Its output is:
`VERIFY_OK boundary_cases=27 strict_generators=20`.

The finite checks are regression checks only. The continuum statement and all parameter ranges are established analytically in `RESULT.md`.

No independent audit has been performed.
