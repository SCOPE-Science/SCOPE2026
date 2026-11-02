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

The standalone Python checker `bdf3_green_verify.py` uses exact integers and rational arithmetic. It proves positivity of the required finite collections of polynomial Bernstein coefficients on rational intervals, verifies the cross-multiplied all-index recursion identities, and isolates the algebraic threshold root. The mathematical proof uses induction to extend the verified identities to every index, and complex-root dominance to prove sign oscillation on the high-parameter range. Numerical approximations are supplementary only.

Run `python3 bdf3_green_verify.py` from this directory. The criterion is established for the scalar zero-prehistory Green sequence, not arbitrary BDF3 solutions. Independent audit: not performed.
