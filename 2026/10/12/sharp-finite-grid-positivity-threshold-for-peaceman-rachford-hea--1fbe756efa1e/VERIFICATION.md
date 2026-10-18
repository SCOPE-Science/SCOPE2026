---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The two tensor-split Peaceman–Rachford factors commute, yielding G=C_m(s_x)⊗C_n(s_y) with C_k=2(I+sT_k)^{-1}−I and T_k=tridiag(−1,2,−1). Cofactor inversion yields strictly positive offdiagonal C entries and diagonal (R_k)_{ii}=D_{i−1}D_{k−i}/D_k. Decreasing q_j=D_j/D_{j−1} makes minimum diagonal equal D_{k−1}/D_k at endpoints; derivative −vᵀT_kv<0 supplies exactly one crossing. If one factor has negative diagonal, a positive offdiagonal in the other detects a negative Kronecker entry. The limit is from q∞=(1+2s+sqrt(1+4s))/2, root 2−sqrt(2). Independent exact SymPy matrix identities give C_2(3/5)=[[-1,15],[15,−1]]/56, negative tensor entry −15/3136, and C_2(11/20) positive.

## originality

PASS

Peaceman–Rachford/Hundsdorfer–Verwer stability theories are not lattice maximum principles: norm stability does not entail entrywise nonnegativity. The inspected 1989 primary paper does not present the finite Dirichlet resolvent endpoint polynomial threshold. Resultary positivity-preserving CN filtering uses a different composed scheme.

## value

PASS

A sharp necessary-and-sufficient step-size restriction for the physically essential positivity of heat solutions, including grid-size dependence and asymptotic frontier, clarifies a practical property absent from unconditional stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
