---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Exact distinct pair sums (after subtracting 2a) are 0,x,2x,x+y,2x+y,2x+2y; ordering gives gap words x,x,y−x,x,y for x<y, x,y,x−y,y,y for x>y, or four x when x=y. Consecutive unit-gap runs prove complete four-row classification for all x,y>0. Whenever there is a five-term run it starts at even integer 2a or 2a+2; requiring 0,1,2,3 forces its start to 0 and hence includes 4, excluding anchored length3. Explicit witnesses produce lengths 0,1,2,4; nonnegative presence of 0 and 1 forces 2, excluding length1. Independent separate exhaustive run checked all 39,601 pairs x,y=1..199; unrestricted scope rests on symbolic sorted-gap proof.

## originality

PASS

Best-of-knowledge originality with disclosed antecedents and material access limits. The problem is a concrete first nontrivial slice of established signed basis spectra, not a general additive combinatorial theorem. Unlike unsigned maximum formulas, the signed anchored length1 and forbidden length3 require exact classification. No checked prior result was shown to entail all rows and signed/nonnegative distinction; this is a modest exact first-case classification, not an unresolved broad conjecture.

## value

PASS

Nathanson formulated exact signed and unanchored basis spectra as natural problems, and the first three-generator/two-summand case has a complete inverse classification with unexpected forbidden coverage length 3 and signed length1 absent without negatives. The proof is elementary, but the precise first-case attainable-set spectrum is independently useful; no artificial general-theorem requirement is imposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
