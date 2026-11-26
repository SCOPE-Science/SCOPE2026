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

The repaired theorem is for even n at least four only. Ones are on odd positions and there are no runs 0000, so internal gaps of zeros have lengths one or three. The opposite endpoint parities give L+R=1+2[a=00]+2[b=00], whence the 101 count from the two gap equations. Pair counts and the other allowed triples follow by extending pairs and subtracting the correct one-sided boundary indicator. Conversely failure to extend a pair at each end recovers that end, and one-letter multiplicity recovers K. The independent complete-language factor enumeration covers 65 even lengths and confirms both directions; the gap proof is what establishes all lengths.

## originality

PASS

Distinct only for the repaired all-even, including nondyadic, exact equivalence theorem. The strongest distinct indexed match fully covers the frozen dyadic classification but its two-block rotation and bridge argument requires a dyadic length. The inspected two-Abelian and tentative three-block results do not determine the three-letter counts from just weight and two-letter ends at general even length.

## value

PASS

This is a structural compression for an established complexity invariant on a standard automatic word, applicable across all even lengths. It gives sufficiency of a single one-letter count plus ordered ends, removing all interior triple counters even for nondyadic enumeration. The gain relies on the word's gap geometry and is not the generic fact that equivalence preserves ends.

The dated certificate retains the supplied scientific assessment, sources and limitations.
