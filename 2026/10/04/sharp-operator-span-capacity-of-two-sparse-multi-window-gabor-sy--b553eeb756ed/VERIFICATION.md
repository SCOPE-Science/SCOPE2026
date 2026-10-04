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

The universal statement is analytic. The verification program is a finite consistency replay, not an exhaustive proof for unbounded dimension.

`artifacts/verify.py` performs three checks. First, for every dimension from 2 through 20 and every tested window budget through one above the injective threshold, it constructs the stated two-sparse windows and counts the union of nonzero ambiguity coordinates, comparing it with the formula `N*min(N,1+2*s)`. Second, for dimensions 2 through 10 it explicitly constructs every full Gabor rank-one projector and numerically computes the complex matrix rank of their span, comparing that rank with the ambiguity-support count. Third, for dimensions 2 through 9 it exhausts collections of support pairs and verifies the sharp translation-row coverage bound `min(N,1+2*s)`.

The replay output is:

`VERIFY_OK ambiguity_cases=119 projector_rank_cases=34 exhaustive_support_N=2..9`

Floating-point linear algebra is used only in the finite projector-rank replay. The proof of the theorem uses no numerical approximation: it follows from exact Weyl-character decomposition, support intersections, and explicit nonvanishing formulas.
