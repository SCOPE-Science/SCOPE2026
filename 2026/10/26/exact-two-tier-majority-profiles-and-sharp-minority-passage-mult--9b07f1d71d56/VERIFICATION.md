---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

An isolated run of length one flips; every longer run remains unchanged, so P=h-s+t. Marking any one-run gives the exact n/r normalization and the product of singleton-refined composition counts. The proof upper-bounds P by h+floor(h/2)-1 for h<n/2 and constructs the matching run configurations, then enumerates all critical feasible (r,s,t). Independently rebuilt all labeled binary input histograms for n=3..13; formula, threshold, and multiplicities matched; the universal claim is supplied by the run argument, not the finite experiment.

## originality

PASS

The known local-majority coalition threshold and general regular-graph results are prior; the assessed new part is the full labeled joint H/P distribution and exact critical multiplicities. A relevant 1986 primary local/global-majority paper was not retrieved in full; priority remains qualified. No exact covering SCOPE/Resultary entry emerged from the five topic searches.

## value

PASS

The labeled input/output histogram and the multiplicity of the smallest successful minority are natural exact invariants of a one-step local-majority rule; they answer stronger questions than mere feasibility, and the all-cycle formula can be reused for probabilistic input ensembles. This is a complete, object-motivated enumeration, not a raw small-size census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
