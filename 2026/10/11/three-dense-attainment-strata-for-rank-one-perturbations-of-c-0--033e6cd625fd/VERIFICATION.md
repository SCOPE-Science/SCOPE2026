---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Over K=R or C and a∈ℓ1 nonnegative with A=Σa_n>0,t>0, each row functional φ_a−tδ_n has norm A+t−2min(a_n,t); because a_n→0 the operator norm is A+t. If y=T x, the coordinate limit equals c=φ_a(x), hence |c|≤||y|| and t||x||≤2||y||, so closed range and NA⇔QNA. Norm attainment in c0 forces equality |φ_a(x)|=A and all positive-weight coordinates x_k share unimodular phase; that is possible in c0 precisely for finite support, with a zero j used for −phase. S extension to ℓ∞ is weak-star continuous by ℓ1 pre-adjoint, B_ℓ∞ is weak-star closure of B_c0, and compactness yields exact weak-star image K. If some a_j=0 choose z_j=−1, z on support +1 for a maximizer. If all a_n>0, any norm-maximizing sup sequence forces |Σa_nz_n|=A, hence every z_n is the same unimodular phase, contradicting ||S z||=A+t. Finite-support, infinite-support-with-zero and full-support strata each dense in the A-simplex via truncation/mass transfer/positive summable mixing. Full-support is dense Gδ and zero-coordinate weak-star QNA union is dense meager Fσ. Both fields and normalization boundaries tracked.

## originality

PASS

Choi et al general weak-star quasi norm attainment density and example separating QNA from weak-star QNA are antecedents. The present exact coefficient-support trichotomy and simultaneous density of 3 attainability statuses inside one fixed-norm 2-parameter affine family, including generic nonattainment, are not given by those broader-existence statements.

## value

PASS

The same-norm family exhibits dense but meager weak-star quasi norm attainment, with a clean coefficient-level distinction between three notions. This supplies a motivated explicit stratification and compact convex nonremotal image within a central Banach-space operator-geometry problem; not a textbook finite-support norm estimate alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
