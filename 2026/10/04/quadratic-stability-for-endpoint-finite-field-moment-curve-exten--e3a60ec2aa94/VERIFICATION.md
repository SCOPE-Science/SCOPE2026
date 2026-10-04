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

The infinite theorem is established by the symbolic proof in `RESULT.md`. The crucial source inputs are the exact merge identity, the polynomial expansion of \(H_s\), and the endpoint fiber identity from arXiv:2609.29882v1. The new steps are elementary inequalities and an exact telescoping argument.

`verify_quadratic_stability.py` performs an independent exact-rational sanity check. It directly enumerates \(F_d(\theta)=\mathbb E_\theta[M(T)]\) for \(2\le q\le4\), \(2\le d\le5\), and deterministic rational probability vectors including vertices, sparse laws, uniform laws, and skew laws. It checks the local pair-averaging lower bound and the global quadratic remainder, and it checks equality for every tested \(d=2\) case. The captured replay is:

`VERIFY_OK global_cases=68 pair_cases=236`

These finite computations do not certify the all-parameter theorem and are not used as a substitute for proof. No claim of coefficient optimality is made for \(d>2\).
