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

# Reproduction and scope of verification

Execute `python checks/verify.py` from this package's root. The program uses only the Python standard library and rational arithmetic to check closed identities: Erlang-two direct cumulant and normalized transform, derivative factorization, symbolic closed optimizer at selected rational points, and exact critical shape coefficients. The exact observed output is preserved in `checks/verify_output.txt`.

The unlimited-parameter phase classification follows from the coefficient-ratio proof, not from the finite test grid. The \(\rho\downarrow0\) singular asymptotic follows from compact localization and a uniform analytic expansion, not from floating-point extrapolation. Direct interpretation of the original log MGF also checks the sign of the centered Gamma jump contribution. Historical priority and independent proof checking remain outside the scope of these tests.
