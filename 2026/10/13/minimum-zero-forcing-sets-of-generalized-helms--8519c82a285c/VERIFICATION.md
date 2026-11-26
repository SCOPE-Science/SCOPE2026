---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For m≥3 and s≥2, two omitted leaves at the same spoke can never be forced, so s−1 leaves per bundle are mandatory. With just those leaves, the process stops after the spokes turn blue. At the next cardinality there is one extra vertex: a spoke still leaves the hub and one leaf at each spoke white, whereas the hub and an extra leaf give exactly the two claimed classes. In the hub class, round 1 colors the spokes and round 2 the omissions. In the saturated class, no spoke is initially blue; round 1 colors all spokes, only the saturated spoke can force in round 2 (it forces the hub), and round 3 colors the remaining leaves. There are s^m and m s^(m−1) sets, respectively, by independent choices of omissions. This also proves the efficient-set statement.

## originality

PASS

The prior zero forcing number and graph propagation time are explicitly excluded from the distinct contribution. The checked prior proof supplies the bundle obstruction and a hub-containing witness, not the alternatives at minimum size, the coefficient, or the per-set time distribution. No equivalent same-domain classification surfaced in the bounded comparisons.

## value

PASS

This is the complete ordinary minimum-set layer of a natural graph family. The scalar optimum does not identify/count the optimal sets or show that another minimum family takes an extra parallel round. The two-family description and multiplicities supply the first coefficient of the zero forcing polynomial and the time distribution within that coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
