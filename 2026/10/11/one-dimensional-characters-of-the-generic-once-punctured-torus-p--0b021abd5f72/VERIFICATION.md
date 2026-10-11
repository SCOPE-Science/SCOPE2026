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

The scientific certificate is `artifacts/verify.py`. It reconstructs the scalarized Theorem 32 relations with the convention \([x,y]_r=rxy-r^{-1}yx\), defines the four parameter expressions used in the claim, and checks all listed assignments by exact symbolic simplification. It then checks the exact factor identities used in each completeness branch.

Run `python artifacts/verify.py`. The expected output is `VERIFY_OK candidates=10 scalar_relations=7 completeness_branches=6`.

The computation is symbolic over rational functions in \(q\). The proof uses the explicit assumptions \(q^4\neq1\) and \(q^6\neq1\) to justify the cancellations. No finite enumeration over numeric parameter values is used to infer the general statement.
