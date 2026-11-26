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

For fixed zero sets of sizes p,q, a positive A vertex at a common-positive index can cover all q B zeros for excess ceil(q/2) above one. If no common-positive defender is used, each A defender misses its own opposite zero, so at least two are necessary and two distinct ones suffice at cost 2ceil((q-1)/2), if available. The same argument holds on B, independently, with zero cost when there are no zeros to defend. This gives the exact support formula and the bound w>=2n-floor(p/2)-floor(q/2). If an entire shore is zero, the other cannot have any zeros and the cost is at least n+2ceil((n-1)/2), strictly above the matched-pair witness for n>=3. For n=2m+1, equality forces both zero counts 2m (the floor drops at 2m-1), and the only positives must form a deleted matched pair. For n=2m, equality forces p,q in {n-2,n-1}; only a common-positive defender can realize equality if n>=6 because the two-defender excess is strictly larger. At n=4 a side with two opposite zeros also has strict excess for inside-only defense. For three opposite zeros the possible cost tie cannot occur at equality: the opposite shore has a sole positive which must have a common-positive index; this leaves at most one inside-index candidate. With nonempty support intersection exactly the five claimed support patterns remain, and on each side only one common-positive vertex carries excess. The counts are n; n(n-1) each for the asymmetric 2-by-1 cases; n(n-1)(n-2) for two 2-supports meeting once; and 4 binom(n,2) for identical 2-supports. Summing gives n(n^2+n-1) for even n. The labels fit the degree-based cap and each listed family attains the lower bound.

## originality

PASS

The scalar formula and the matched-pair witnesses are explicitly prior and are not a contribution here. A same-day indexed result enumerates a restricted subclass whose minima coincide with the matched-pair functions at both parities. Even-order ordinary equality beyond those n functions is the clearest distinct contribution: the other four families and full census are not implied by either source. The closed classification of all ordinary optimizers therefore goes beyond the inspected results.

## value

PASS

The exact equality families show that the even case has cubic multiplicity and four additional support geometries, where the known scalar formula only identifies a one-unit change. This gives a reusable optimum-set benchmark for the canonical almost-complete bipartite family and distinguishes ordinary from restricted response; it is not a recomputation of the scalar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
