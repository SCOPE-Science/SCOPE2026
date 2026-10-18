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

# Reproducibility

With SymPy installed, run `python artifacts/check_double_star.py` from the top-level extracted artifact directory. The checker verifies the five symbolic rational entry identities in the two variables, sign-polynomial evaluations, and direct exact-rational Laplacian matrices for nine sizes \(m=2,\ldots,10\) at eight rational timesteps, including all orbit-representative entries, row sums, and symmetry. The independent full-matrix computations supplement, and do not replace, the analytic quartic root and sign arguments in RESULT.md. The method is the completed rational step \(T_m(h)\), not its internal Runge–Kutta stages. No external or independent validation is claimed.
