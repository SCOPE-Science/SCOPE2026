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

For h=V+Kz with V symplectic nondegenerate alternating dim 2n, n>=1 over any field including characteristic 2, every derivation preserves one-dimensional center so a local derivation must preserve Kz. Conversely any center-preserving T=(L,ell,c) is pointwise represented by a derivation: for v!=0 choose a symplectic basis and matrix S=[[A,0],[C,-A^T]], C symmetric, with Sv=Lv; choose phi(v)=ell(v)+ct, set D(z)=0. For v=0, choose conformal-symplectic M(e_i)=0,M(f_i)=cf_i and D(z)=cz. Characteristic 2 is covered by alternating-form identities. Der dimension n(2n+1)+1+2n, LocDer dimension 4n²+2n+1; gap n(2n−1). Independent F2 h3 exhaustive count 64 derivations,128 local,128 center-preserving maps. Finite case is corroboration only.

## originality

PASS

The previously published Heisenberg witness and general two-step existence theorem, including its char≠2 restriction, were explicitly separated from this all-field complete local-derivation space classification. Best-of-knowledge PASS after examination of main theorem/examples and related prior work.

## value

PASS

The exact algebraic reflexive hull of the derivation space for a canonical nilpotent Lie algebra, uniformly in rank and field characteristic, is a natural structural classification. The dimension gap quantifies failure of local-to-global rigidity; a single known witness cannot supply it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
