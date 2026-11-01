---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Congruence puts the old alternating matrix into J_(2r)⊕0_d, with unrestricted new coefficient matrices P (2×2r) and Q (2×d). The Schur residual [P J^{-1} P^T,Q;-Q^T,0] has rank 4 for rank Q=2, rank 2 for rank Q=1, and rank 0/2 for rank Q=0 according to symplectic orthogonality. Rank-Q counts are 1, (q+1)(q^d-1), (q^d-1)(q^d-q). Counting symplectically orthogonal row pairs gives U_r=q^(2r)+(q^(2r)-1)q^(2r-1) for r≥1 and U_0=1; the remaining P cases produce V and W exactly. Direct independent finite-field full enumerations for 12 small cases over F2,F3,F5 agree, and K_(2,2,2) F3 counts 1,1376,198288,331776. Character formula follows via odd-characteristic class-two central character orbit method; characteristic-two characters NOT claimed. Computational confirmations do not replace the all-field block proof.

## originality

PASS

PASS, best of knowledge: the actually read published one-cone result adds a single universal vertex; repeating it makes the new vertices adjacent, not the claimed two-vertex independent set. Rossmann (2022) poses character-degree enumeration and studies conjugacy-class joins. Rossmann–Voll (2025), full PDF pp.1–6 Theorem A/§11, studies ask zeta functions (average kernel sizes) under joins, not a complete fixed-q rank distribution transition. No inspected statement implies all three rank-increment counts; a broad generic bordered alternating matrix theorem could contain an equivalent fact.

## value

PASS

PASS: a uniform exact operator on complete rank distributions for arbitrary graphs, with genuinely different independent-versus-adjacent universal-vertex geometry, preserves polynomial character-degree enumeration and yields all complete tripartite K_(2,a,b) examples. This is a motivated class-two representation-counting construction, beyond rephrasing the bordered rank lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
