---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The verification is a direct logical replay of the orbit classification.

For an off-diagonal ordered pair \((x,y)\), record
\[
I(x,y)=\bigl(d(x,y),\mathbf 1_E(x,y)\bigr).
\]

**Invariant check.** Every automorphism preserves \(d\) and \(E\), so equal-orbit pairs must have equal \(I\).

**Completeness check.** If two ordered pairs have equal \(I\), the coordinatewise map between them is an isometric isomorphism of their induced two-point graph structures. Strict homogeneity of the primary structure extends that map to a global automorphism. Hence equal \(I\) is sufficient for equal orbit.

**Realization check.** The Baire-space graph's finite-extension property allows a second point to be introduced at any canonical positive distance \(2^{-k}\), with the off-diagonal edge either present or absent. Thus every proposed \(O_{k,0}\) and \(O_{k,1}\) is nonempty.

**Diagonal check.** Any singleton isomorphism extends by homogeneity, so all diagonal pairs lie in one orbit.

Together these checks give exactly one diagonal orbit and two off-diagonal orbits for every \(k\in\omega\). Fixing the first coordinate gives the point-stabilizer statement.

The verification uses no finite truncation as evidence for the infinite theorem. Its non-computational inputs are precisely the source-supported strict homogeneity, canonical distance set, and finite-extension property.

No independent audit has yet been performed.
