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

For q>=3 distinct letter-runs per period and all positive run lengths and k>=1, adjacent half-windows with equal Parikh vectors reduce after deleting full periods to two disjoint circular arcs. The q>=3 unique-run circular-support lemma makes such adjacent arcs monochromatic; for length residue above p/2 the same follows from complement arcs. Long factors encode their starting phase uniquely since the cyclic period is primitive. Counting run placements gives F_h=sum_i max(0,r_i-2h+1), initial T(1)=d and T(2)=d+e, and T(k+2)-T(k)=B=p+2 sum_i floor(r_i^2/4). Thus T(k)=d+(k-1)B/2 for odd k, d+(k/2-1)B+e for even k. Independently enumerated literal distinct contiguous factors for 215 selected run-vector/power cases (1902 half-length profiles), all agreeing with the symbolic total/spectrum. The finite checks corroborate, not prove, the arbitrary-parameter theorem.

## originality

PASS

The all-power explicit distinct-factor Abelian-square count and length-specific phase profile are not entailed by earlier general Abelian-square occurrence algorithms, bounds, or the same-family single-factor Parikh-complexity invariant. In particular runs (4,1,2) and (1,4,2) have identical single-window Abelian factor-complexity but distinct k=2 square counts 7 and 5. The claim retains q>=3, not binary two-run periods, and prior-art risk remains from specialized periodic-word enumeration.

## value

PASS

A natural complete coefficientwise invariant for finite powers of cyclic run-encoded words: exact length spectrum, phase-sensitive boundary term and constant two-power increment are useful for reporting/deduplicating Abelian squares in compressed periodic strings, beyond routine occurrence detection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
