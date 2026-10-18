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

The analytic proof in `RESULT.md` establishes the exact finite-dimensional probability law, expectation and limiting theorem. Reproduce independent finite checks with `python3 verify.py` (Python standard library only). The program evaluates quadrature identities for six simplex sizes, the tetrahedral \(N=4\) identity, and seeded Gaussian spacing averages. All checks passed in this package.

Finite quadrature, sampling and finite-size identity tests do not constitute proofs of a weak limit or of identities for all dimensions; Gaussian normal decomposition, pathwise spacing identities, asymptotic Gaussian extremes and conditional binomial concentration supply those analytical steps.

Independent audit has not been performed.
