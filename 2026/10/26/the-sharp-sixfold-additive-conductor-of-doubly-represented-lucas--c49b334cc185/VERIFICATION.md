---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The cited Lucas representation theorem has the matching convention allowing indices 0 and 2 together, and its formula has the precise shift n+1. I separately reconstructed the bounded K by the include/skip dynamic program on indices: the count polynomial after adjoining L_j is the preceding one plus X^L_j times the polynomial from two stages earlier, truncated at 1006. This independently finds 171 elements with exactly two representations and recovers the closed-form prefix. Starting from {0}, iterating exact truncated sums with this K proves [997,1006]⊂5K and excludes 1001 from 6K; positive summands make the truncation exact and repetition is allowed at every stage. The gap bound at most 7 follows from successive floors; the translated ten-point blocks therefore overlap without end, beginning at 997+5=1002. For h≤5 the total index T controls every sum via 5h+4T+3S, with S in an open interval of length h and T≤X/(4+3α)+O_h(1). The resulting upper counting density h/(4+3α) is strictly less than one, so the other exact sumsets miss infinitely many positive integers. This is not a claim about the union of sums with at most h summands. Replay: /workspace/replays/recheck_frozen.py, lucas(), an exact direct Lucas-index and sumset check independent of the frozen witness and exclusion code. The infinite conclusions follow from the gap and counting arguments.

## originality

PASS

The set K, its precise generalized Beatty representation and its density are credited to prior work; general effective decidability for additive orders of generalized Beatty sequences is also prior. The supported distinct finding is the minimal exact-summand order six with its exact conductor 1002 and last miss 1001 for this K. No compared source states or directly supplies those numbers. This is a best-of-knowledge comparison, with an uninspected primary Beatty-sumset source explicitly noted.

## value

PASS

The additive basis question is natural for the established set of nonuniquely represented Lucas integers, whose gaps are bounded but whose residue blocks can leave holes in low-order sumsets. The exact minimum order resolves a qualitative obstruction, and the sharp conductor gives a usable membership guarantee for the smallest feasible order. The last exception is certified together with all-size coverage, not presented as a leaderboard number from an arbitrary finite scan.

The dated certificate retains the supplied scientific assessment, sources and limitations.
