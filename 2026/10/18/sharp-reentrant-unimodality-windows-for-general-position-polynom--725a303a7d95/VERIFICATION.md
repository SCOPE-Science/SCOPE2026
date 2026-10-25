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

For a,r>=3 graph diameter two makes GP subsets exactly induced disjoint unions of cliques. Partition into one-row, one-column, coordinate-distinct transversals, and three/four corners of a 2x2 rectangle gives the full c_k formula. Exact c3-c4 and c5-c4 sign cubics/quartics plus binomial-tail monotonicity give a=3 precisely r<=10 or >=18, a=4 precisely r<=11 or >=40; the exceptional r=1,2 formulas have separately checked geometry. Independently enumerated shortest paths and all vertex subsets on seven small graph cases and checked 200 parameter pairs, without mistaking finite tests for the infinite proof.

## originality

PASS

The 2024 primary text General Position Polynomials discusses this exact graph family and explicitly leaves its full unimodality behavior as Problem 5.2; its cited sufficient a=3 bound r>=19 is weaker than the exact 18, and its expression disagrees with the literal graph at r=2,a=3. Existing general-position graph families do not imply the sharp windows.

## value

PASS

Exact complete parameter-window classification for the natural general-position polynomial on two fixed part counts, with a surprising loss and return of unimodality; this answers motivated explicit earlier questions, not an arbitrary sequence test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
