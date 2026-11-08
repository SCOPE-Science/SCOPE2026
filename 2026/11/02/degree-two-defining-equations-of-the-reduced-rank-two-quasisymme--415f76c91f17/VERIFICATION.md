---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The n-2 toric maximal components with ordered partition {1}|{2..b+1}|{b+2..n} restrict each Pluecker coordinate to 0 or a signed monomial t_i t_j. Z^n-degree separates quadratic weights. Two-index weights restrict nontrivially, three-index weights vanish exactly when the repeated index is the middle b>=2, and four-index weights have one Pluecker kernel relation if index 1 occurs and an additional disjoint-index kernel when not. This proves the direct sum and dim(I_n)_2=2*C(n,4) in every n>=4. Independent exact-rational restriction-rank computation for n=4..9 returned 2,10,30,70,140,252 respectively, corroborating but not replacing the general weight split.

## originality

PASS

Bergeron–Gagnon–Spink–Tewari arXiv:2604.24903 Theorem B/5.1 already gives the set-theoretic quasisymmetric-Johnson cuts and §9 the toric components, so those parts are not novel. The new degree-two *radical ideal* vector-space decomposition distinguishes set-theoretic generators from additional independent quadratic consequences. No explicit dimension 2*C(n,4) or extra C(n-1,4) basis appeared in the inspected original. General positroid ideals could imply it with an extra component-intersection rank calculation; prior implicit coverage risk remains.

## value

PASS

The first homogeneous ideal piece of a natural toric-component union is fundamental projective algebraic geometry. A complete independent quadratic basis and sharp n=5 onset clarify why the known set-theoretic defining equations are not all quadrics in the reduced embedded ideal. It avoids claiming unverified generation in higher degrees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
