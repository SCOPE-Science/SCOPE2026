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

The results are reproducible from `REPRODUCE.md`: exact projective orbit enumeration, rank-36 Jacobian smoothness tests, local tangent-contact evaluation, an independent direct coefficient scan for all forms having at least seven candidate flex points, and an independently implemented orbit-representative cross-check. Both complete finite-census implementations and the extremal example replayed with identical results. This does not constitute independent external audit.

The complete domain is the 7,174,453 normalized nonzero ternary quartic equations over the three-element field. The orbit enumerator accounts for every equation, and the direct scan of the entire domain independently finds 6,097 candidate equations having at least seven rational smooth-point flexes before global smoothness filtering. Of these only 936 pass exact geometric smoothness, each of contact type (6 ordinary,1 hyperflex). No form has eight rational smooth-point flexes. The representative's partial derivatives have no common nontrivial geometric zero. The certificate does not assert the same counts over another field or for geometric flex points over an algebraic closure.
