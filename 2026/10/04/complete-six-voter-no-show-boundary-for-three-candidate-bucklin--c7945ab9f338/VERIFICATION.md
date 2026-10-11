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

Fresh exhaustive replay over all anonymous strict three-candidate profiles found zero Bucklin no-show events for electorates of size at most five and exactly 18 bad profiles at six voters. All 18 events use a single abstainer. Normalizing the abstainer to rank A>B>C gives exactly the three profiles (1,t,0,3,2-t,0) for t=0,1,2; candidate relabeling gives three orbits of size six. There are 462 anonymous six-voter profiles and 417 with unique Bucklin winner, so the two exact incidences are 3/77 and 6/139.

## originality

PASS

Brandt, Matthäus and Saile already prove that the Bucklin No-Show Paradox first appears with three candidates and six voters, so the minimum itself is prior art. Their full article and summary table do not state the complete anonymous six-voter census, its 18 profiles, the three relabeling classes, or the exact incidence fractions. Targeted Resultary and web searches found no prior equivalent boundary classification.

## value

PASS

A complete classification at the exact minimal paradox boundary is a natural finite object: it gives every witness, symmetry classes, abstention size and exact incidence rather than one counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
