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

Run `python3 verify.py` in the directory containing the six public documents and the standalone verifier. With Python and SymPy installed, it should print `VERIFY_OK` followed by the exact Pfaffian quadratic form, Hessian rank, degree, genus and discrepancy. The direct execution of the accompanying file returned `VERIFY_OK`.

The verifier expands the Pfaffian of a model rank-four plus four-dimensional kernel alternating block; checks the six-variable quadratic form and its Hessian; evaluates the published Harris–Tu degree formula; and checks the normal-determinant/adjunction arithmetic and blow-up discrepancy.

The universal geometric steps are mathematical arguments, not empirically certified by finite computation: universal rank-locus codimensions, generic avoidance of rank at most two, Bertini smoothness/irreducibility, the kernel-normal-bundle isomorphism, relative Grassmannian identification and smoothness of the blow-up. All are proved in `RESULT.md` under the explicit generality assumptions. The accessible originating manuscript was inspected; the full 1984 Harris–Tu article could not be obtained through available full-text routes. No independent review or external validation is claimed.
