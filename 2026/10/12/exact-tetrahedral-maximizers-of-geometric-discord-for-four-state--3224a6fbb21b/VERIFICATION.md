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

The analytic proof has four independently checkable steps: (1) diagonal-generator completeness reduces the source matrix to \(G=\frac14\sum_a r_ar_a^{\mathsf T}\); (2) \(\operatorname{Tr}G=1\) gives \(\lambda_{\max}(G)\ge1/3\); (3) equality makes \(\frac34R^{\mathsf T}R\) a rank-three projection with diagonal \(3/4\), forcing the signed-tetrahedron Gram form; and (4) the two QRAC Walsh sums have squared norms at most \(16/3\) on that equality class.

`verify.py` uses exact `Fraction` arithmetic. It checks the regular-tetrahedron second moment, the geometric-discord value \(1/12\), the signed Gram formula for all sixteen sign choices, and the exact Walsh-norm ceiling. The finite sign loop is exhaustive only after the analytic classification has reduced all equality cases to sixteen sign patterns; it is not evidence for the continuous maximization before that reduction.

The script also checks the strict comparison by squaring positive quantities: \(1/\sqrt3<1/\sqrt2\). No claim of global bibliographic uniqueness or independent validation is made.
