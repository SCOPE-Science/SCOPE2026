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
# Reproducibility and limits

Run `python verify_density.py` from the directory containing the supplied checker, using Python 3.10+ and NumPy 1.24+. The program reads no external files or networks. Its actual observed output was:

`DENSITY_PROJECTION_CHECK_OK exact-polynomial=25 numerical-nonexpansive=150 numerical-expansive=14`

The analytic proof uses (i) Hermitian eigenvalue difference majorization; (ii) scalar strict-convex KKT; (iii) the trace-zero \(3\times3\) quartic identity; (iv) a sign-nonzero diagonal derivative in dimension four; and (v) a golden-ratio spectral-derivative obstruction in dimension three. The \(p=4,n=3\) identity is an exact algebraic equality, not an empirical generalization. The quartic identity is additionally checked by exact integer arithmetic on 25 instances; the other tests use floating-point approximations and do not certify universal quantifiers, the complete literature record, or any independent mathematical review.
