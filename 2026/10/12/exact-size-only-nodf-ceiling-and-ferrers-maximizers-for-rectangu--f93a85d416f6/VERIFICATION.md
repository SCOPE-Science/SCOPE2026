---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For a=min(m,n) and b=qa+r, positive column degrees lie in 1..a; equal-degree column pairs contribute zero. Convexity of choose(c_d,2) forces minimum ties T=(a-r)choose(q,2)+r choose(q+1,2), bounding NODF≤1-T/K. Ferrers initial-segment columns with all c_d=q or q+1 attain every available nontied pair contribution, and equality forces a strictly nested row chain, hence Ferrers and balanced degree multiplicities. Choices of r degree labels give exactly choose(a,r) classes; fixed-a asymptotics 1-1/a. Independent exhaustive bitmatrix enumeration checked (2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5): 18,859 valid labeled matrices, maxima and types agree.

## originality

PASS

Britton et al fully characterize only endpoints NODF=0 and 1. The exact shape-dependent *subunit* maximum and all Ferrers multiplicity classes for every rectangular m×n constitute a separate optimization not implied numerically by the square-staircase endpoint theorem.

## value

PASS

A sharp size-only ceiling and complete extremizer classification are directly useful for ecological nestedness benchmarking and identify unavoidable shape bias without confounding prescribed-link-count optimizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
