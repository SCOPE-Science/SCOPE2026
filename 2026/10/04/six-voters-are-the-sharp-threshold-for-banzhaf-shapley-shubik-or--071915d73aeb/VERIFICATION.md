---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS for the final mathematical theorem, with one non-substantive count typo flagged. The recursive representation of monotone Boolean functions by ordered restriction pairs f0≤f1 enumerates all games exactly. Independently enumerated the complete 1,4,18,166,7579 simple games on 1..5 labeled players (TOTAL 7768) and calculated every Banzhaf/SS pairwise order using exact fractions: 0 mismatches. The specified six-player minimal-winning coalitions {2345},{156},{36},{26} yield raw swings (2,8,8,2,4,24), SS (1/30,1/6,1/6,1/20,1/12,1/2), so Banzhaf ties players 1 and 4 while SS separates them. The source RESULT.md accidentally says 5768 total games in its Verification paragraph, although its enumerated per-size counts and actual program correctly total 7768. This editorial error does not alter quantifiers, exhaustive coverage or sharp result; it blocks uncorrected public-file publication.

## originality

PASS

PASS (best of knowledge, with explicit inaccessible-primary risk). Freixas’s 2011 primary lecture (materially read) and related power-index theory establish ordinal-equivalence definitions and sufficient classes such as weakly complete or semicomplete games, but do not supply an all-simple-game sharp first separation at n=6. Resultary’s close Johnston 5-player and Deegan–Packel boundaries compare different indices. A highly relevant 2012 Freixas–Marciniak–Pons full article was not accessible: OA/preprint attempts yielded only metadata and authorized institutional retrieval reported an expired human-verification tab; no claim that its full text lacks the result. That risk remains explicit, rather than automatically failing O.

## value

PASS

PASS. The exact first-order divergence threshold for two canonical voting-power rankings over ALL monotone simple games is a natural finite classification question. Exhaustion of 7,768 games establishes the universal small-n bound, and the explicit n=6 witness proves sharpness. Tie-to-strict separation is still genuinely ordinal inequivalence; no stronger reversal is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
