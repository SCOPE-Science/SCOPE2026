---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Take H=⊕_{n≥1}C², λ_n=(n+1)^(-1), a_n=sqrt(1−λ_n²), and U_n=[[λ_n,a_n],[0,0]]. Each row has norm1, so U_n U_n*=diag(1,0) and U is a norm-one partial isometry with closed range ⊕Ce_n; K=U commutes with U. U*e_n=v_n=λ_ne_n+a_n h_n, U*h_n=0, {v_n} orthonormal, R(K*)=closed span(v_n); since λ_n>0, R(K*)∩N(U*)={0}. The one-point family Λ=K* is Parseval K-g-frame. But ΛU*e_n=(U*)²e_n=λ_n v_n and ||K*e_n||=1, so every proposed positive transported lower bound fails as n→∞. In Alizadeh--Rahmani proof, ||K*f||=||UU†K*f|| illegally treats UU† as identity on R(K*) although only trivial kernel intersection was assumed. More precisely, for UK=KU and nonzero K, universal preservation of all continuous K-g-frames is equivalent to δ=inf_{||z||=1,z∈R(K*)}||U*z||>0. Sufficiency follows integral lower bound and K*U*=U*K*; necessity tests Λ=K*. The weaker range inclusion R(K*)⊂R(U) recovers the printed Moore--Penrose constant but is not necessary. Infinite vanishing angles are proved symbolically, not extrapolated from finite n.

## originality

PASS

Bounded best-of-knowledge PASS specifically for the concrete closed-range partial-isometry counterexample to Alizadeh--Rahmani Theorem 2.1 (2023) under its unusually strong assumptions. A separate published SCOPE record already gives the SAME bounded-below universal criterion for DISCRETE K-g frames against Li--Leng--Huang (2017); the universal algebraic lemma is therefore not independently novel and is credited rather than double-counted. The current continuous-source counterexample requires a nonuniform angle construction not supplied by that discrete theorem. Claims of an entirely new general preservation criterion would overstate originality; residual overlap risk documented.

## value

PASS

The infinite closed-range partial-isometry example disproves a specific published theorem under every displayed hypothesis and identifies the false use of Moore--Penrose projection. The sharp δ test follows an already-known discrete template (credited); the mathematically worthwhile work lies in the source-specific vanishing-angle obstruction, not in renaming the universal lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
