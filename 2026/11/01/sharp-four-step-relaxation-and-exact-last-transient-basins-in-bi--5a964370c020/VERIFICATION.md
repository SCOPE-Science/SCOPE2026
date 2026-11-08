---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The shore update is exactly zero/one/retain/complement, with symbolic labels that distinguish complementary patterns of equal cardinality. Every real configuration induces one of 80 compatible orders of (a,i,a-i,b,j,b-j), two threshold cuts from 7 and 8 positions. I separately implemented this comparison quotient: all 4480 formal cases satisfy F^6=F^4 and the stated T=4 predicate, with exactly 16 exceptional cases. Independently implemented synchronous labelled-state evolution on 29892 sampled exhaustive-small parameter/state instances found no discrepancy. The quotient, including tied-order overcoverage, is a finite exact proof of all actual order types, not an enumeration cutoff. Summing binomial multiplicities of the two disjoint orientations gives N_4.

## originality

PASS

Earlier synchronous bi-threshold literature gives eventual period at most two, not this uniform bound on the first periodic entry or the labelled T=4 binomial census. Unlike parity automata, the update has state-dependent hysteretic thresholds; unlike majority network results, the two thresholds are arbitrary. Searched Resultary plus primary Boolean network literature by mathematical content. Priority qualified for unindexed biclique-specific analyses.

## value

PASS

A universal relaxation-time cutoff despite unbounded graph size and threshold values, together with the precise structural imbalance criterion and last-transient basin count, is a natural nontrivial strengthening of eventual-period theorems for network hysteresis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
