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

# Verification performed
The standalone `verify.py` enumerates every nonempty subset of the 2n edges of the labelled sunlet S_n for orders three through eight, tests connectedness on the edge-supported vertices, and adds singleton subgraphs to pair diagonals. It then computes min_v f(u,v) for every vertex and verifies exactly the two claimed values, index sum and antipodal pair counts. This is an exhaustive finite corroboration: no computational check is claimed for all n. The infinite theorem rests on the path-arc bijection, inclusion-exclusion, finite geometric sums, strict distance monotonicity and endpoint/diagonal comparison.

Verified totals: n=3:81, n=4:288, n=5:930, n=6:2736, n=7:7644, n=8:20352.

No independent external audit or independent mathematical validation was performed. The 2021 relevant article's full text was inaccessible.
