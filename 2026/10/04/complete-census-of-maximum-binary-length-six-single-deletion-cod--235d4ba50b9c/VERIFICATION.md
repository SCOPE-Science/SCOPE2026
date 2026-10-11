---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Fresh exhaustive construction of the 64-word deletion-compatibility graph and exact maximal-clique enumeration found 62,707 maximal cliques, maximum size ten, and exactly nine maxima. Their intersection is precisely the four displayed words; direct deletion-ball unions give coverage histogram 26x1, 28x3, 30x4, 32x1. The unique coverage-32 code satisfies the VT0 checksum. Applying reversal/complement to all nine gives three size-two and three singleton orbits. The enumeration is complete and exact.

## originality

PASS

Sloane gives the known optimum sequence and exhibits a nonperfect size-ten length-six code obtained by replacing two words of \(\mathrm{VT}_0(6)\); No gives later optimization/bound machinery. Those results establish the optimum and nonuniqueness, but not a complete census. No inspected source or Resultary entry supplies exactly nine labeled maxima, their common four-word core, the coverage histogram, unique perfect maximum, or the six symmetry orbits.

## value

PASS

Length six is a classical small deletion-code benchmark where prior work explicitly showed the optimum is nonunique but stopped at examples. Completing the optimizer census, isolating the universal core and unique perfect code, and describing the symmetry/coverage strata is a natural finite classification rather than a recomputation of \(A(6,1)\).

The dated certificate retains the supplied scientific assessment, sources and limitations.
