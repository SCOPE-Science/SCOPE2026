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

The observation is a ten-coordinate multiset of unordered adjacent pairs in a four-letter LINEAR word, without known endpoints. It is realizable iff the looped multigraph on active letters is connected and has 0 or 2 odd-degree vertices. Counting connected support graphs with 1,2,3,4 active letters and subtracting the eight four-odd parity supports (3 perfect matchings, 4 stars, complete K4), with positive odd and even multiplicity series O=z/(1-z^2), E=z^2/(1-z^2), yields exactly the quoted rational function with denominator (1-z)^10(1+z)^4. Exact symbolic subtraction and factor cancellation verified the numerator, N(1)=14 and N(-1)=-6, establishing leading feasible fraction 7/8 and genuine quasipolynomial period 2 for all m>=1. Independent complete literal word enumeration matched coefficients m=1..7. The Euler argument, not that finite enumeration, proves the infinite count.

## originality

PASS

The four-letter unordered length-two composition multiset, absent endpoints, is a different output channel from ordered fixed-length spectra or all-length compositions; no exact same all-length enumeration was found in inspected literature. Classical Euler-trail parity is credited. Priority remains qualified by unindexed graph-enumeration tables.

## value

PASS

A natural zero-error channel has precisely T_m distinguishable outputs, so the all-length rational function, sharp feasibility fraction 7/8, and first obstruction from 4 odd vertices provide substantive combinatorics and coding capacity information beyond elementary Euler-trail criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
