---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

With three candidates and two seats, unique committee is equivalent to a unique bottom-scoring candidate. After orienting a hypothetical AV {A,B} / SAV {B,C} conflict, strict comparisons imply e-d>=1, 2d-e>=1 for d=c-a and e=ab-bc, so d>=2 and e>=3: at least five ballots. Five forces 3AB+2C, yielding SAV A/B tie, not distinct UNIQUE committees. At six, d=2,e=3 and one leftover ballot: among B,AC,ABC, only B yields both unique committees, giving 3AB+B+2C. Exact independent enumeration of all anonymous compositions of n ballots into 7 nonempty approval types for n=1..6 and multinomial labeled weighting gave (both unique,distinct) at n6=(75051,360), 6 anonymous profiles one candidate-relabeling orbit. All q-rational score comparisons exact; scope fixes 3 candidates, 2 seats and nonempty ballots.

## originality

PASS

Brams–Kilgour introduces AV versus normalized SAV and supplies a 17-voter three-candidate differing unique committee example, which proves upper bound 17 but not the minimal 6-voter threshold and its entire first-orbit census; their Proposition 6 uses 9 voters where AV and SAV agree. The later standard score linearization makes the strict integer comparison possible but does not imply six-ballot sharpness without the bounded diophantine argument. Closest published result on Bucklin six-voter paradox concerns different rule. Best-of-knowledge PASS, unindexed illustrative 6-voter example possible.

## value

PASS

SAV was motivated as a correction to multiwinner approval bloc overrepresentation. The first electorate size where the two rules force distinct unique committees with the fewest candidates and seats, plus classification of all first conflict profiles, provides a precise natural finite threshold useful as a canonical voting example and boundary test; proof relies on nontrivial strict-score inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
