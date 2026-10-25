---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For KG(n,2), n>=5, vertex-to-edge distance is 0 for either edge endpoint doubleton, 2 for the other four doubletons lying in its four-point support, and 1 outside. Thus for two graph edges with supports meeting in h points, the resolving neighborhood has size 12-2*C(h,2)+q, where q is the number of intersection doubletons in exactly one endpoint matching. Independent examination of the finite matching choices on prescribed union supports t=4,5,6,7,8 gives respectively (size,count): (4,3),(6,30),(8,60),(10,225),(11,180),(12,630),(12,315); unique union support yields the six-term claimed polynomial. Uniform weights 1/4 are feasible and three distinct-matching-pair inequalities on each 4-support yield the matching LP dual lower bound C(n,2)/4. Directly independently written BFS reproduces complete histograms n=5,6,7, not a proof for all n. Empty binomial terms make all formulas valid at n=5.

## originality

PASS

Best-of-knowledge primary-source and Resultary comparison; no searched statement/table/general theorem shown to imply the exact submitted additional invariant. Crucial established premises and special cases are credited. Full-text versus abstract material is explicitly distinguished; inaccessible literature is retained as risk, not assumed noncovering.

## value

PASS

Exact six-term pairwise resolving-neighborhood polynomial is a natural complete ambiguity invariant for an infinite canonical edge-location graph family; beyond the previously known scalar the seven overlap types expose how four-point supports lose distance information. Tight matching LP witness makes the exact fractional optimum reproducible and intrinsic, not an arbitrary computational slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
