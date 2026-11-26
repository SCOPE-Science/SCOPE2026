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

An independently written exact census reproduced the complete 11-by-4 table, with 34 nonzero entries, an all-zero L=22 row, no other entries, and N(31,5)=92. For replay, python3 /tmp/opencode/independent_order5_census.py fixes the root 00000 edge first and varies the outgoing-edge visit order at the other 15 vertices. Every rooted Euler tour prescribes its own ordering and the ordering determines at most one completed tour; checking the 32 distinct five-bit factors verifies the accepted words. This gives 2048 distinct rotation classes. Discrepancy was evaluated by all length/start pairs, through prefix differences on the doubled period, including wrap and the full period. Over GF(2) a recurrence is a linear relation between consecutive cyclic shifts by the same coefficients at every coordinate. If the first dependency is at T^L w, the first L shifts are independent and span all shifts by iterating the dependency. Hence the cyclic shift matrix rank equals the minimal recurrence length. Exact row reduction of the 32 rotations is an independent alternative to the supplied polynomial division; a fresh rooted depth-first Euler census with Berlekamp–Massey also matched. Rotation does not change the rank or the windows, and no complement or reversal was used to identify the words. The minimum discrepancy is 5; L=31 is maximal; 92/224=23/56 differs from 1024/2048=1/2. Frozen Python files were inspected, not executed. Their stated Python 3.8 floor in VERIFICATION.md is too low for int.bit_count; use Python 3.10+ for that optional frozen replay. The result is an exact finite census at order five, not a general-order result or formal certification.

## originality

PASS

The supported distinct result is the joint recurrence-complexity/discrepancy table and hence the count 92 of simultaneous optima for these two specific metrics. The full D and L marginals are covered by other catalogue records, and the known general extremum results are not contributions of this record. No inspected source covers the joint table. In particular, the closest catalogue table sharing the L marginal uses periodic autocorrelation, not cyclic window discrepancy, and an explicit pair with equal L and sidelobe but unequal D rules out direct recovery via that statistic. The same number 92 in a rooted Lempel–Ziv bin is not evidence of the same claim. This is a bounded statement-level assessment, not historical priority certification.

## value

PASS

Low cyclic discrepancy measures local balance, whereas high linear complexity measures resistance to short linear recurrences. These are motivated objectives independent of this enumeration. The classification gives exact simultaneous selection rates on a complete finite population: maximal L occurs in 23/56 of minimum-D cycles instead of 1/2 overall, so combining the two separate quality criteria is not independent. The full conditional distribution is a useful order-five benchmark not supplied by already known marginals, with no claim of a general-order tradeoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
