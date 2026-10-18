---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The nested falsity sets B_0=empty, B_{j+1}={x: exists y in R[x], R[y] subset B_j} reproduce falsity of (Box Diamond)^(j+1) top. The rank-core minimal-finite-rank contradiction forces every finite-rank point to have an infinite-rank successor. Starting with a stage-(m+1) new failure, alternating x_j (ranks j) and y_{j-1} (infinite rank, with R[y] subset B_{j-1} but not B_{j-2}) gives 2(m+1) different points. The 2m+2-vertex directed path has initial distance 2m+1 to terminal and first failure at m+1. All nonempty arbitrary frames allowed. Independent direct recurrence checks cover all labelled relations n<=3 and 4096 n=4; finite enumeration cannot replace the rank proof.

## originality

PASS

Alpay–Basaran (2026) give directed path of size 2m+2 and certify smallest sizes only m=1,2,3; the all-m minimality proof via disjoint finite/infinite-rank witnesses is not contained in their reported bounded SAT results. Semantic searches found generic finite Kripke/model reduction results but no matching exact all-m lower bound.

## value

PASS

An exact minimum separating model size for every iteration depth closes the specifically identified gap between known path witnesses and bounded certificates. The finite-rank/infinite-rank ladder is a structural combinatorial obstruction with potential use for modal model-size bounds, not merely one more finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
