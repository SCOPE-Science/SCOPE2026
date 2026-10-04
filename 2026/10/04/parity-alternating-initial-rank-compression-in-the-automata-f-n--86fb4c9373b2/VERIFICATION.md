---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem is proved symbolically in `RESULT.md`. The critical checks are:

1. The letter \(a\) has exactly one collision pair, \(\{2,n\}\), so each effective use lowers rank by exactly one.
2. For a shortest word, \(a^2=a\) excludes adjacent copies of \(a\). Between consecutive effective copies, separator length \(2\) is impossible; separator length \(1\) forces the next separator to have length at least \(3\). Pairing separators gives the claimed lower bounds.
3. The two witness families have the displayed missing-state sets, proved by induction. The range \(s\le(n+1)/2\) prevents wraparound from invalidating effectiveness.

`artifacts/verify.py` performs exact power-automaton breadth-first search for every odd \(5\le n\le17\), checking all claimed deficiencies for each such \(n\). It also directly replays every witness and the explicit hole-set formulas for every odd \(5\le n\le301\). Its recorded output ends in `VERIFY_OK`.

The finite computation is not used as an infinite proof and no claim is made for \(s>(n+1)/2\).
