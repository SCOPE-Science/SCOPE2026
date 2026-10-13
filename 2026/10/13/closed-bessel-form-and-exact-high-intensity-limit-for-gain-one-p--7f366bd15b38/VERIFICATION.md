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

The analytic proof reduces the published double series by grouping terms with fixed \(k=m+n\), applies Vandermonde's identity, identifies the resulting \({}_1F_1\) with \(e^{\zeta}I_0(\zeta)\), and then applies the standard positive-real large-argument expansion of \(I_0\).

`verify.py` is an independent numerical replay using only Python's standard library `decimal` module. It evaluates \(I_0\) from its defining power series, evaluates the original double sum directly, compares both sides at several \(\zeta\), checks the source's reported value near \(\zeta=1.2357\), and verifies convergence toward the displayed asymptotic approximation.

The numerical checks do not prove the infinite identities; they only test the implemented formulas. The proof does not establish uniqueness of the finite-\(\zeta\) maximum or optimize gain.
