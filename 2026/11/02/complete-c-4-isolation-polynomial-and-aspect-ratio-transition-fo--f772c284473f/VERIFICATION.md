---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every 2<=m<=n, the closed-neighborhood deletion from a cell set D removes exactly its occupied rows and columns; the residual is R_{m-a,n-b}. A non-induced C4 exists iff both residual factors are >=2, or one is 1 and the other >=4. Unique row/column occupancy plus inclusion–exclusion Q_{a,b}(z) yields the whole polynomial without overcount. Sharp lower-bound m-1 and m when n>=m+3 follow by residual widths; full five-case optimizer counts follow from exactly one missing row, one doubled row when n=m+3, and square-board surjection-orientation overlap correction. Independently enumerated all subsets on nine boards across five boundary regimes, and separately reconstructed C4 from adjacency permutations for five boards through 3x5; all predicted minima and polynomial coefficients matched. Universal m,n proof rests on residual-rectangle equivalence and case partition.

## originality

PASS

Bartolo–Borg–Scicluna (2023) prove the universal n/5 isolation bound with exceptional graphs; Wei–Zhang–Zhao (2023) prove the size-based (|E|+1)/6 bound. Neither theorem counts every isolating set or exactly partitions optimizers by rook aspect ratio. The equivalent line graph L(K_mn) wording was searched, but isolating C4 in line graph is not isolating C4 in the bipartite root. General star-isolation cannot subsume the C4 predicate by maximum degree alone; R1,3 and R2,2 are both degree two but differ in four-cycles. Potential unindexed exact polynomial remains risk.

## value

PASS

Square-isolation is an established graph invariant and rook graphs are canonical strongly regular/Cartesian-product examples rich in four-cycles. An all-cardinality polynomial and five explicit optimal-set counts give structurally meaningful aspect-ratio boundary at n=m+3, with two optimizer mechanisms at the threshold; this is neither an arbitrary small finite census nor a routine general bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
