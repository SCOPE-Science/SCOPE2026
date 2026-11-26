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

Reconstructed the MAS condition for scattered subsequences: deleting the preceding letter forces each proposed next letter to occur in the previous greedy block, since otherwise its greedy position and the eventual failure are unchanged. Conversely, after any single deletion the block witnesses place the remaining suffix one block earlier; deletion of the last letter gives the already embedded prefix. A word has a unique greedy path. At the first position of run j>=3 the only arrivals are from the last position of run j-2 and the first position of run j-1. Both first-position states admit both letters because the intervening run has length at least two, so first-position and within-run totals obey the Fibonacci recurrence with A_1=A_2=1. A final letter of the last-run type fails only after its last position; the other final letter can fail exactly at the end of the penultimate run or at the first position of the last run. The binary complement and two-run cases agree. Independent prefix exploration and individual deletion tests corroborated both counts on 360 run tuples, using lengths 2, 3, 4 and 2–5 runs. The induction, not the finite test, covers unbounded r and lengths.

## originality

PASS

The established greedy criterion and the two-run example are reused. No inspected earlier source gives or subsumes the arbitrary-run-length Fibonacci count together with the terminal-symbol split. The later exact catalogue overlaps are material but cover different subfamilies or statistics and do not establish earlier coverage.

## value

PASS

The cardinality of the minimal obstruction antichain is a natural invariant of the subsequence order. Its independence from arbitrarily large and nonuniform run dilations, and the sharper terminal split, reveal structure beyond enumerating a fixed alternating example or reporting the output of a general algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
