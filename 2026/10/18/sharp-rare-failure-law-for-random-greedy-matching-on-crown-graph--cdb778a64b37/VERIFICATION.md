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

The restriction of a uniformly random remaining edge order to the available edges has a uniform first edge, and rejected edges never become feasible again. With r unmatched labels on each side and overlap c, there are r²−c available edges. Removing two, one or zero shared labels has the three stated multiplicities, and r≥2 cannot be terminal. A particular surviving shared label is lost to 2(r−1) choices; for two fixed distinct shared labels the union of those choices has size 4r−6, because the two cross edges are counted twice. These hazards independently yield the first- and second-factorial-moment identities. Substituting the first into V_r(c)=2c/[r(r+1)] gives negative drift −4c(c−1)/[r(r−1)(r+1)(r²−c)], which telescopes to the deficit in the finding. The second identity gives the product bound with factors ((j−2)²+2)/j². Factoring out (j−2)²/j² and bounding the remaining product by exp(sum_{t≥1}2/t²) gives e^{π²/3}r²(r−1)²/[n(n−1)], including the empty product at r=n. Then r²−c≥r(r−1) yields the claimed harmonic bound and n q_n→2. The recurrence requires O(n²) arithmetic operations and O(n) rational registers, not that bit cost. A separately written exact labeled-state recursion agrees for n=2 through 7; enumeration of the original edge orders agrees for n=2,3.

## originality

PASS

The supported distinct result is the exact overlap-state failure law and the quantified rare-defect asymptotic for the uniform-edge crown process, not the general greedy algorithm or the line-graph equivalence. The two strongest exact Resultary overlaps are distinct later-dated records: they have the same process, recurrence and asymptotic, with different explicit error bounds; they cannot be cited as evidence of earlier coverage on the inspected record dates. No earlier equivalent quantitative crown law was substantiated in the bounded comparison. This is not a claim of unique discovery or proof of provenance between records.

## value

PASS

Deleting one structurally distinguished perfect matching from K_{n,n} is a natural sparse perturbation of a graph on which greedy matching never fails. Mean matching density misses the defect probability. The exact small-state law and the factor-two leading term, established with an explicit finite-n error bound, quantify that defect; the drift calculation explains why the single surviving forbidden pair rather than the large-n density determines the answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
