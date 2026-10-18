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

Deletion-shadow incidence A_{y,x} is exactly 1 for a distinct one-deletion descendant; max code size with each row sum <=L is an unrelaxed 0-1 integer program over all 128 columns and 64 rows (n=7). Independently constructed insertion and deletion incidences coincide and every received word has n+1 one-insertion supersequences. The assigned source verifier checks the stored 7-bit witnesses for L=1..8; independently solved integer programs returned feasible integer optimum vectors at each L. Independent SciPy/HiGHS binary-variable MILP reruns proved optima 16,33,50,65,81,96,112,128 with solver-reported optimality and integrality; similarly n<=6 M1/M2 pairs 1/2,2/3,2/4,4/7,6/12,10/19. Thus n=7 first with M(7,2)>2M(7,1); a 33-word list-two code cannot be a union of two list-one codes. Upper bounds rely on trusted solver termination/dual bound; no separate human-readable integer branch certificate.

## originality

PASS

Theorem 23 of Kiah-Wei-Zeng provides only 170/3 at n7 list2, insufficient to force 33. The Resultary code with n6 list2 under TWO deletions is a distinct channel; its n6 unique-one-deletion optimizer census does not classify n7 list2. Earlier MILP papers target unique decoding. The 33 capacity and first strict two-class size gap are not derived from the checked prior statements.

## value

PASS

The first finite blocklength where true list-two capacity exceeds two optimal unique-decoding classes is a natural, sharply motivated obstruction to a simple time-sharing construction. Full n7 profile is a useful benchmark for exact list decoding, despite no infinite-length theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
