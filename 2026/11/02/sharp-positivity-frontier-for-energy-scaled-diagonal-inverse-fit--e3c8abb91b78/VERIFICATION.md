---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Expansion of the exact energy-scaled Frobenius loss gives the strictly convex quadratic n/2-sum_i A_ii x_i+(1/2)sum_ij A_ij^2 x_i x_j. The Hessian A Hadamard A is SPD by Schur product; its normal equations reduce after correlation scaling to (R Hadamard R)w=1. Cramer determinants for a three-by-three SPD R yield d1x1=(1-t)(1+t-u-v)/Delta and cyclic analogues with u=a^2,v=b^2,t=c^2, Delta=1+2uvt-u^2-v^2-t^2>0. The sign inequalities and their equalities are necessary and sufficient, and two nonpositive coefficients would force one squared correlation >=1. Dimensions 1 and 2 always give positive coefficients. In the symmetric family R(r,s), 0<s<1 and 2r^2<1+s guarantee SPD; the optimum loses positivity exactly when (1+s^2)/2<r^2<(1+s)/2. A zero-first-coordinate KKT solution is the unique nonnegative optimum, with exact gap (2r^2-1-s^2)^2/[2(1+s^2)(1+s^2-2r^4)], while strictly positive fitting attains only its infimum. Independent rational checks recovered x=(-650,950,950)/889 and gap 4225/132461 for r=9/10,s=7/10, including leading principal minors.

## originality

PASS

Xia–Moxey introduce the exact energy-scaled fitting objective and warn qualitatively about indefinite fitted inverses, but the accessible source description does not provide the complete 3D normalized sign boundary or cone penalty. Resultary bidirectional Gauss–Seidel inverse uses a distinct factorized inverse. Condition-number-based diagonal scaling (Qu et al.) and fixed-sparsity ordinary Frobenius approximation (Amsel et al.) have different objectives. Full original paper was inaccessible via both OA and authorized institutional access, retained as priority risk rather than unsupported whole-document noncoverage.

## value

PASS

The positivity failure of energy-congruence weighted Frobenius approximate inverse fitting, already noted in DG preconditioner work, has a useful sharp all-SPD dimension-three classification, minimal dimension, concrete open failure region and exact price of a PSD constraint. These are natural optimizer-definiteness invariants that guide diagonal approximate-inverse implementations; the result has mathematical substance beyond an isolated negative example or textbook Schur positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
