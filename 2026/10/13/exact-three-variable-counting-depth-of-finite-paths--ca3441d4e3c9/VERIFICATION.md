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

The standalone verifier implements standard joint ordered-pair two-dimensional Weisfeiler--Leman refinement from equality/edge/nonedge colors. It checks every path-plus-cycles rival for orders 5 through 18 against the exact pairwise first-diagonal-difference formula (390 decompositions), then checks an extremal witness for every order 19 through 40.

Observed terminal output:

`VERIFY_OK decompositions=390 exhaustive_n=5..18 extremal_n=19..40`

The computation is finite and supplementary. The theorem for all orders rests on the uniform diagonal-census proof in RESULT.md.
