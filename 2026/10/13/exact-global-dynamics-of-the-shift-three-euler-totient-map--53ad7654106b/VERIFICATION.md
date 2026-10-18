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

Every orbit enters odd integers at least five, since phi(n) is even for n>=3 and 1,2 route via 4 to 5. For any composite m>=27, its least prime factor gives phi(m)<=m-sqrt(m), so F(m)<m. For prime p>=29, F(p)=p+2; if p+2 composite there is strict descent within two steps, otherwise twin prime arithmetic gives 3|(p+4), hence F^3(p)<p. The resulting strictly decreasing odd block-endpoints must reach the eleven odd states 5..25. Exact evaluation of the forward-invariant eleven-state set gives precisely cycles (9),(11,13,15),(23,25); 25 on the last cycle proves sharpness. Fresh independent sieve verifies complete small-state table and local descent alternatives through 10000, which is supplementary to the infinite proof.

## originality

PASS

Leonetti–Luca Theorem 2 establishes eventual periodicity and a bound dependent on the starting value, not the complete k=3 phase portrait or best eventual ceiling. The published 'Sharp period-size bound and extremal structure for shifted Euler cycles' exhibits 23↔25 and bounds max cycle by a function of its length but does not constrain the possible length T, hence does not imply the complete list. The Danh et al. follow-up concerns a two-step recurrence. No stronger complete shift-three list located; residual unindexed-priority risk remains.

## value

PASS

A complete all-initial-value orbit classification and best possible universal eventual bound for a natural arithmetical map advances from general eventual periodicity to exact global dynamics. The proof excludes every other possible periodic orbit by a uniform 3-step descent, not bounded computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
