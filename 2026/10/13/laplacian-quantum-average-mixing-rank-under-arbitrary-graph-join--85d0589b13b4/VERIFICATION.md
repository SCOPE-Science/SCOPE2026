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

From the pinned RESULT.md, the shifted factor eigenprojectors are supported on disjoint factor vertex sets. Resolving collision with the join eigenvalue N gives an exact Schur-square positive-semidefinite block decomposition diag(B_X,B_Y)+J_N/N^2+pp^T. For a factor G, the complement-component argument makes ker Q_G subset ker F_s(G) for s>=3; only connected K_2 has a rank-one gain. The constant directions already lie in B-block ranges for n,m>=2; singleton blocks contribute exactly one direction. Thus rank Mhat_L(X join Y)=rho(X)+rho(Y)+1_(min orders=1)+1_(X=K2)+1_(Y=K2), where Q_G is built after subtracting the constant-direction spectral projector even if G disconnected. Finite exact spectral-projector checks on 49 pairs corroborate, not prove, the all-graph lemma.

## originality

PASS

Primary Kirkland--Monterde (2023) develops Laplacian join eigenfrequencies and transition amplitudes; Coutinho et al. (2018) develops the general average-mixing projector formula. Neither inspected result gives this arbitrary-join rank identity or the complement-component kernel lemma. This is a nontrivial new synthesis best-of-knowledge, with an unlocated stronger commutant theorem a residual risk.

## value

PASS

A full structural rank classification for arbitrary connected/disconnected factors under a natural quantum-walk invariant, with exactly identified exceptional K_2 and singleton factors. The all-order theorem determines nullity under joins, not just a finite example or restatement of projector calculus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
