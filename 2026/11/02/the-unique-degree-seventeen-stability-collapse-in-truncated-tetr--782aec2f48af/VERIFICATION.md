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

Run `python3 CHECKER.py` using the attached standalone file. A successful execution ends with the exact line `TRUNCATED_TETRAHEDRON_HARMONIC_CERTIFICATE_OK`. It verifies the twelve-node coordinate table, rational Legendre recurrence, ranks at degrees zero through six, the exact degree-seventeen constant eigenvalue, the positive lower bound on its eleven-dimensional complementary subspace, and 93 other full-rank degrees from seven through one hundred. The infinite tail is proved using the explicitly cited Bernstein Legendre bound and the verified rational Gershgorin coefficients, not by sampling more degrees.

No external packages or ancillary files are needed. The exact matrix computations use fraction-free leading-minor positivity tests and fail on any nonexact divisibility step. Numerical condition-number approximations are not inputs to acceptance. The reported mathematical status concerns self-review only; independent validation has not been performed.
