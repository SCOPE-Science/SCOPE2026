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

# Reproducibility and limitations

The included standalone `verify.py` (Python with NumPy and SymPy) constructs a Laplacian for each helm graph directly from every spoke, rim and pendant edge; its eigenvalues are computed from the full matrix independently of the analytical Fourier formula. It checks the symbolic radial characteristic polynomial and identities for the radial and Fourier support bounds. It computes optimal conductances by bisection of a monotone derivative for \(n\) from \(5\) to \(18\), eight relative rim prices for each size, verifies exact normalized-budget accounting and a unit spectral gap, and evaluates hundreds of asymmetric feasible allocations. The exact transition price case is checked at five distinct points in its symmetric continuum. The executed checker produced:

`PASS 1180 exact-symbolic and numerical assertions`

The program does not constitute a computer proof of the infinite-size theorem. That follows from the explicit spectral blocks, concavity of \(\lambda_2\), and the strict convexity of the one-variable unit-gap expenditure. Assertions of equality and signs at all real prices are justified by these analytic arguments rather than by sampled matrices. The numerical bisection does not decide mathematical equality cases; the theorem treats them exactly.
