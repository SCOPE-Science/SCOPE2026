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

The standalone `verify.py` constructs \(2\times2\) rational symmetric positive-definite matrices from three eigenvalue pairs and four rational rotations, evaluates the exact projection residual after zero through four power steps, averages all four sign vectors, and checks equality with the derived risk formula. The resonant matrix at angle \(\pi/4\) has rational entries and is checked directly for every power depth; the threshold equation, its direction of strict inequalities, and the Gaussian closed form are checked using exact fractions. Three independent numerical angle integrals serve as secondary checks of the analytic Gaussian integral. Execution returned `VERIFY_OK 123`.

Run `python3 verify.py` with Python 3; only the standard library is needed. No finite sample verifies the theorem for all \(a,b,\theta,q\); universal validity rests on the analytic proof in `RESULT.md`. In particular, finite experimentation cannot establish the asymptotic width or originality.
