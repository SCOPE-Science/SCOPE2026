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

The proof's finite-degree identities are reconstructed directly from orthogonal reproducing kernels. The limiting constants are derived analytically using Jacobi oscillation asymptotics, a uniform integrable endpoint bound, and an Abel-summation estimate for the sine-series tail. Exact equality cases follow from choosing derivatives to be the signs of the respective kernels. The numerical reproduction checks are corroboration, not an infinite certificate.

The companion `verify.py` evaluates the two absolute-integral formulas at degrees 0, 1, 2, 5, 10, 20, 50, 100 and verifies the degree-two Legendre radical. On its originating run it completed with output `PASS finite-degree consistency checks; limits require analytic proof`. It requires `scipy` and `numpy` and may be executed as `python verify.py` with the script in the same directory.

No human or independent review is represented by this record. Possible previously published special-case evaluations of the same endpoint errors have not been ruled out exhaustively.
