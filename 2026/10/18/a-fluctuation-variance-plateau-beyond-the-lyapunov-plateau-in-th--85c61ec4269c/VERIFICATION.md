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

The executable `verification/check.py` implements all parameter-dependent identities in symbolic rational arithmetic with the parameter \(\beta\) indeterminate: strict endpoint order is established analytically for \(2<\beta<3\), while a rational interior test checks the chosen symbolic partition orientation. It verifies the transfer operator's action, the invariant density, Poisson certificate \(w-\mathcal Lw=\rho h\), normalization, zero mass of \(w\), \(\int h w=4/27\), \(\int h^2d\mu=2/9\), and the one-step covariance \((\beta-4)/18\). The script prints `VERIFY_OK` if all identities pass.

The infinite-time variance conclusion depends additionally on the mathematically proved bounded coboundary decomposition, \(Pm=0\), orthogonality of the resulting reverse-martingale differences, and negligible bounded boundary terms; it is not inferred from finite orbit sampling. The calculation does not prove a central limit theorem. This report records self-review only; independent audit has not occurred.
