---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Every 9-element subset of [10] is [10] minus exactly one m. For m=5, a hypothetical four increasing positive summands with largest two sum≤10 necessarily includes a pair summing to 5: if largest=4 then {1,2,3,4}; if largest in {5,6}, the other three form 3-subset of {1,2,3,4}, containing (1,4) or (2,3); if largest≥7, three smaller must be {1,2,3}. For every other missing m, explicit witness quadruples are (1,2,3,4) for m∈{1,2,8,9,10}, (1,3,4,5) for m=3, (1,2,4,5) for m=4, (1,2,3,6) for m=6, and (1,2,3,7) for m=7. Independent direct positive-integer quartet enumeration found witness counts for missing m=1..10 of [10,10,4,4,0,3,1,3,3,6]. The n≤3 cases are formally vacuous h4(n)=n+1 (no four-distinct-positive witness fits [2n]); n4=4 and n5=5, while n≥6 value 4 is properly cited rather than independently proved.

## originality

PASS

van Doorn–Erlbacher 2026 proves stable h4(n)=4 for n≥6 and reportedly notes h4(5)=5 using exactly [10] without 5, but gives no equality-case uniqueness in abstract/search-accessible material. The present extra statement classifies all ten 9-element subsets at exceptional n=5, not the known numerical h4(5) value or its published example. No Resultary prior hit with this exact small-edge classification was found; complete primary PDF remains inaccessible, so a statement buried in the source cannot be definitively excluded.

## value

PASS

This is a small but sharply motivated exact equality classification at the unique exceptional threshold point n=5 immediately preceding the stable n≥6 theorem. It identifies the sole extremal obstruction instead of merely reproducing known bound and example; a later researcher studying boundary equality cases can use the precise uniqueness. The value is bounded: ten missing-singleton cases and no general n≥6 extremizer theory. The trivial/vacuous n≤3 values alone are not assigned standalone value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
