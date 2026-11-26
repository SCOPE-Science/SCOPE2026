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

There are t+1 full-alphabet blocks, so every length-(t+1) target embeds and any constant length-(t+2) target fails. Greedy matching within I_q uses a new copy exactly at weak descents. If any of the first t comparisons is a strict increase, the first t+1 symbols fit in I_q^t and the last fits in π. If all are weak descents, the first t+1 cannot fit in I_q^t, so any embedding must use π for at least its last two letters. They fit exactly when their π-positions increase, and then placing the first t targets one per I_q copy suffices. For pivot v the first t symbols have binomial(q−v+t,t) choices by multisets and the last symbol has p_π(v) choices, with the q=1 case also covered. An independent distinct-subsequence-set check covered all 99 hosts with q≤4, t≤3 (34,477 length-(t+2) candidates). A separate exact subset-state dynamic program reproduced every endpoint, omission and support size for t=2, q≤7, including the cutoff among q≥3; no inference from a partial sweep was needed.

## originality

PASS

Credit the exact nonlinear t=2 attainable supports and the first endpoint-only gap transition, not the general arch method, the aligned case, or the t=1 support. The two-order criterion and count can be recovered by specializing a prior general SAS characterization and counting pivot choices. A separate Resultary record also gives a directly specializing formula and extrema, but not the exact attainable supports or transition. Those require deciding which intermediate scores are realizable across permutations, not merely evaluating any one score.

## value

PASS

The first nonlinear weighting of a natural order-dependent SAS count asks whether the extremal interval is actually filled. The two immediate endpoint gaps are intrinsic: sorting any nonextremal rank assignment toward its extremum by adjacent swaps gains at least two, the smallest difference between triangular weights. Thus q=6 is the first case among q≥3 attaining every value not ruled out by the immediate endpoint obstruction, with q=7 a second exact instance. This is a meaningful finite cutoff and gives exact data for broader support questions, not just a list at arbitrary sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
