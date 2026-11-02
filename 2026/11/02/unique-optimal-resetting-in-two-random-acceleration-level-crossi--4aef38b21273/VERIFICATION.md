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

The analytical proof in `RESULT.md` establishes the complete positive-parameter uniqueness assertion. The executable `verify.py` evaluates two independent formulas for the reset-free crossing kernels, tests the exact derivative identities numerically at positive times, resolves both one-crossing equations in high precision, and solves the Laplace derivative equations for the maximizing dimensionless rates. Run from this directory with `python verify.py`; requirements are in `requirements.txt`.

The checked outputs for the displaced level are approximately \(z_u=0.81791633596468716693\), \(s_u=0.52032768949327121491\), and peak intensity \(0.10467026210716147384\) after normalizing the intrinsic time to one. The moving-start/zero-target case gives \(z_v=0.42158369002467118230\), \(s_v=0.50594300405017570224\), and peak intensity \(0.05846588284022673328\). The small decimal discrepancies across platforms depend on integration precision; the code's explicit tolerances describe its checks.

No finite set of quadrature evaluations proves uniqueness. The proof instead uses positivity and an exact derivative bound \(E'(z)/E(z)\le1/z\), strict monotonicity of an explicit root ratio, and a positive-support separation argument for two exponentially tilted integrals. No external independent audit was performed; no formal high-precision interval certification is claimed.
