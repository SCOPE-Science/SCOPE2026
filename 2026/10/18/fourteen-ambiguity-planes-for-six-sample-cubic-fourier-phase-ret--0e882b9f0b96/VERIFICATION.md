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

# Verification of the six-sample cubic theorem

The accompanying `verify.py` runs exact symbolic computations in SymPy; `verification-output.txt` records its completed execution. It computes the full twelve-row Hermitian measurement system with sixteen real coordinates and verifies rank eleven. It independently checks that five explicit basis matrices lie in the kernel. It then verifies that every one of the fourteen algebraic matrices is Hermitian, nonzero, traceless and rank exactly two, verifies that their orthogonal range projections differ for all 91 pairs, and checks the polynomial elimination identities, determinant discriminant and an explicit inequivalent pair.

The completeness of the classification also requires the analytical case division in `RESULT.md`: the code only verifies the critical identities and finite set of algebraic representatives, while the inequalities and branch exclusions in that proof establish that there are no unlisted solutions. No search over finitely many arbitrary complex coefficients is used as an infinite proof.

Reproduce with `python verify.py` using Python 3 and SymPy. Independent audit remains unperformed.
