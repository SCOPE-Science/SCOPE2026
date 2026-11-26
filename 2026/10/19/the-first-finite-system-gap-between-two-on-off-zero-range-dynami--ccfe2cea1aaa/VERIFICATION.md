---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the repaired active class, empty sites remain ON, and on the triangle every occupied OFF can activate because it has an empty ON neighbor. All-ON configurations communicate by alternating hops with activation; choosing hop destinations realizes all five phase/occupation types and their relabelings. Independently constructed and solved the exact five-state lumped chains. The only rate difference is the escape rate from the split state with both occupied clocks OFF, 2c versus c. With escape rate αc, collision mass is (c+1)(c+2) divided by (c+1)(c+2)+2/α+4c+2c². This yields both stated stationary laws for all c>0 and the positive factorized gap, tending to 1/6 at zero and decaying as 1/(9c²). With all clocks initially ON, there is at most one OFF site when there is one particle (OFF implies occupied) or when there are only two sites (every hop leaves an ON source). Hence all eligible neighbors are ON in the smaller cases. The repair excludes all-OFF absorbing states rather than asserting they do not exist. Replay: python3 /workspace/branches/reproduce_triangle_seasons.py, output /workspace/branches/triangle_seasons_reproduction.txt.

## originality

PASS

The corrected scope matches the physically active class of the exact symmetric-ring model in the literature and does not reclaim the known gated canonical law. The supported contribution is the finite original-model stationary collision probability and its strict signed discrepancy at the first active-class size. The exact gated product law and mean-field behavior of the original model do not determine this difference.

## value

PASS

The repaired finite boundary case pinpoints when the solvable neighbor-gated surrogate first changes a natural stationary observable, holding all hopping and reset rules fixed. The all-rate sign and distinct slow- and fast-clock scales distinguish physical neighbor gating from an artifact of an arbitrarily chosen absorbing start. This is a useful exact benchmark even without a general-size inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
