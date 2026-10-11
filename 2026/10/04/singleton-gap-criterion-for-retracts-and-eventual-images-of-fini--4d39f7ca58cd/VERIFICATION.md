---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Necessity follows by testing any omitted level against all retained points on its nearest boundary levels: antichain incomparability forces a singleton at an exterior boundary and at least one singleton around each internal gap. Conversely, the stated conditions define an explicit retraction by fixing Y, collapsing unused points on retained levels inside those levels, and sending each omitted block to an available singleton boundary; target levels are nondecreasing, hence the map is order preserving. The eventual-image equivalence can also be checked directly for finite posets: a stable image carries a finite order-automorphism, so a sufficiently large power of the map retracts onto it. A fresh independent exhaustive search over all weak-order size vectors of height at most three, level sizes at most three, and total size at most six checked 877 nonempty subsets and found exact agreement with the criterion.

## originality

PASS

Originality passes. Pouzet--Zaguia define a different local notion of a retractile set: a convex set that can be collapsed to one internal point while fixing its complement. Their Lemma 10 classifies that notion for weak orders, not subspaces Y admitting a global pointwise-fixing retraction W→Y. The general finite-space eventual-image/retract equivalence also does not classify which subsets of a weak order are retracts. The audited singleton-gap criterion supplies that missing global classification.

## value

PASS

The theorem completely classifies retract subspaces of a natural and widely used finite-poset class and simultaneously classifies all eventual images of its self-maps. The singleton-gate mechanism is structural and explanatory, not merely an enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
