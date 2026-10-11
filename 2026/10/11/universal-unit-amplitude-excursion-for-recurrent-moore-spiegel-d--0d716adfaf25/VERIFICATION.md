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
The packaged symbolic checker `verify.py` was executed from its actual package path and returned `VERIFY_OK`. It verifies the two stationary balance generators, the new identity from `L(xy)`, and the equality-set tangency formula. The proof of strictness is analytic: equality in Cauchy–Schwarz gives `z=-T*x` on the support, and invariance reduces the support to the origin. No numerical trajectory sampling is used as proof.

Limits: compact support and positive `T,R` are required; the theorem does not prove that a nontrivial recurrent set exists.
