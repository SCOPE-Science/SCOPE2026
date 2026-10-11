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

The proof uses the exact planar Steiner formulas
\[
\operatorname{area}(K+sB_2)=A+sP+\pi s^2,
\qquad
\operatorname{per}(K+sB_2)=P+2\pi s,
\]
followed by scaling. These give the exact area and perimeter of \(K_t\), so the theorem reduces to algebra plus the planar isoperimetric inequality.

The packaged `verify.py` is a standard-library exact sparse-polynomial checker. It treats \(\pi\) as a formal variable, clears all displayed denominators, and checks two identities: the finite Jensen numerator factorization and the second-derivative factorization. Replaying the packaged file returns:

`VERIFY_OK`

`finite_jensen_identity_residual_monomials=0`

`second_derivative_identity_residual_monomials=0`

The checker does not certify the planar Steiner formula or the isoperimetric theorem; those are the external mathematical inputs. It also does not test higher-dimensional or non-disk interpolation, which are outside the claim.
