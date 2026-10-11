---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For an off-level point \(p=((i,a),(j,b))\), the proposed survivor at level \(\min\{i,j\}\) is below \(p\). Under lexicographic deletion, any strict predecessor outside the anti-diagonal has already been deleted, while every remaining anti-diagonal predecessor lies below that proposed witness; hence each deletion is genuinely down-beat. The survivors consist of two incomparable orientations at every level and all lower levels precede all higher levels, so the survivor poset is exactly the original minimal sphere. It has no beat points, proving it is the core. I independently replayed the deletion criterion for \(2\le n\le8\), obtaining point/deletion/core counts \((30,24,6)\) through \((306,288,18)\), while the universal quantifier rests on the order argument rather than the finite check.

## originality

PASS

Barmak--Minian classify the minimal finite sphere models and develop beat-point methods, but do not compute deleted products. Kandola studies topological complexity of these same finite sphere models, not the complement of the diagonal. Targeted searches for finite-space configuration/deleted products and Resultary search found the assigned theorem plus separate results for crowns and mapping spaces, not a general theorem forcing this strong finite-space collapse. The classical fact \(F_2(S^n)\simeq S^n\) after realization is weaker because finite-space homotopy and an explicit Stong core are not determined by weak homotopy type.

## value

PASS

Minimal finite spheres are canonical test objects for finite homotopy, and configuration spaces are a natural operation that need not preserve finite-space homotopy in a formal way. The exact all-dimensional core and explicit deletion sequence give reusable structural information beyond the familiar classical sphere configuration-space homotopy type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
