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

The proof was checked directly against the finite p-morphism definition. For the target frame \(\mathbf F\), the only arrows are
\[
rRc,\qquad cRt,\qquad cRf.
\]
A source sink cannot map to \(r\) or \(c\), because back would demand a successor. A clause world cannot map to \(r\), because back would force one of its sink successors to map to \(c\). Surjectivity therefore forces the unique source root to \(r\); forth then forces every clause world to \(c\); every variable world is forced to \(t\) or \(f\).

At a clause world, back for the two arrows leaving \(c\) requires one successor of each color. This is exactly the \(\operatorname{NAE}_3\) condition. Conversely, every satisfying assignment gives such a p-morphism, and a nonempty clause set guarantees that both colors occur and hence that the map is onto.

`verify.py` independently enumerates assignments and all maps for a finite battery of small incidence frames. It checks equality of the two counts and prints `VERIFY_OK` only after all assertions pass.

The exhaustive computation is not used to infer the general theorem. No claim is made about other fixed targets, approximate counting, or minimality of the four-point target.
