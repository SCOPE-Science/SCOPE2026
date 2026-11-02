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

The included standalone program `verify_local.py` was executed with Python 3 and SymPy. Its exact symbolic output was:

```
FERMAT_SECOND_TYPE_LOCAL_AND_INCIDENCE_EXACT_OK
components=(10,45) cross_elliptics=180 deep_points=405; deep_local_ideal=(C*G,D*H); implicit_jacobian_det= 1296
```

It checks the cubic restriction, Jacobian, reduced four-plane intersection and squarefree singular-support ideals, together with finite incidence arithmetic. The proof of the local formal equivalence uses the invertible Jacobian and the previously established complete component classification; finite tests alone cannot prove those global statements. The generic one-zero case uses clean smooth intersections established from explicit support tangent directions. Originality relies on inspections listed in AUDIT.json; absence of a search hit is not proof of global novelty. External independent validation remains unperformed.
