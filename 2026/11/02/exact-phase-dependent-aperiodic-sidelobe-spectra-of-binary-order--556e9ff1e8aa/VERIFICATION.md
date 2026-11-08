---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Every 32-state de Bruijn Hamiltonian successor is determined by one of 2^16 complementary-output Boolean tables on 16 four-bit suffixes; all tables are checked for one 32-cycle, giving a complete 2048-cycle family without rotation duplicates. Inspected independent Euler-tour DFS enumerator for 4-bit de Bruijn graph and mismatch-count versus sign-product correlation equality. Independently enumerated ALL 2048 cycles, their 65536 cuts and all 31 aperiodic lags using bitwise mismatch/bit_count: reproduced every rooted PSL and cycle optimum histogram entry. Lowest PSL=4 on 40 cuts belonging to 32 cycles, with eight cycles having two optimal cuts; eight cycles have best level=16. Computation is exhaustive of claimed finite universe, not extrapolation to higher orders.

## originality

PASS

Spinsante, Andrenacci and Gambi 2011 enumerate the same 2048 cycles but their reported order-five sidelobe-threshold subset counts 12 and 784 refer to PERIODIC autocorrelation, invariant under the cut; Fujisaki/Nabeshima also use periodic autocorrelation. The indexed cut-dependent nonwrapping spectrum is a separate claim; earlier aperiodic data appendix remains a priority risk.

## value

PASS

Peak NONWRAPPING sidelobes determine practical root-sensitive code quality; exact cut distributions and optimized cycle profiles supply a complete natural finite benchmark not determined by periodic correlation tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
