---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Write a nonzero rank-one linear map as P(X)=tr(FX)U, modulo reciprocal scaling. Expanding both averaging identities and nondegeneracy of the matrix trace pairing gives necessary and sufficient U²=λU, FU=UF=λF. For λ≠0 normalize U to unique image idempotent p, with F∈pM_np nonzero; this is a rank-s idempotent incidence vector bundle, irreducible dimension 2s(n−s)+s²=2ns−s². For λ=0, U²=0 and FU=UF=0. The supplied explicit t-dependent idempotents of rank n−r and functionals F_t, whose resulting endomorphism coefficients have no pole at zero, degenerate to each square-zero-image rank-r operator, so no additional reduced components exist. Distinct rank-s open strata remain separated under nonzero-idempotent limits. Counting images/kernels and GL_r gives E_{n,s}(q), Z_{n,r}(q), with scaling/(q−1); dominated convergence of normalized ranks yields the Rogers-Ramanujan density (qR(q^−1)−1)/(q−1). I independently verified exact finite-field count formulas at (n,q)=(2,2),(2,3),(2,4),(3,2), giving 24,112,330,1274; the infinite claims rest on algebraic arguments not finite checks.

## originality

PASS

Bounded best-of-knowledge original contribution is The boundary gluing of rank-one averaging operators on full matrix algebras; source inspections and four implication checks below separate its precise claim from prior theorems; earlier subresults are credited, and stated residual priority risks remain.

## value

PASS

The rank-one averaging-identity scheme has natural geometric strata, and the substantive question is whether nilpotent-image maps constitute new components or lie on boundaries of the idempotent strata. The explicit gluing classification answers it in every dimension and characteristic and unifies geometric and finite-field enumerative behavior, rather than merely reprinting earlier idempotent counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
