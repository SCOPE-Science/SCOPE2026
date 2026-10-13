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

The proof in `RESULT.md` establishes the universal statement; finite checking is corroborative.

`artifacts/verify.py` constructs the generalized windmill adjacency directly, then tests the strong majority condition by counting every color in every open neighborhood. A separate occupancy predicate implements the proposed \(m=2\) global bound and \(m\ge3\) per-blade bounds. A third procedure computes the predicted number of labeled palette maps using a multinomial dynamic program and independently compares it with the direct enumeration.

The exhaustive comparison covers all \(1\le n\le4\), \(2\le m\le5\) with \(nm+1\le9\) and palette sizes \(1\le q\le4\), including one-blade boundary checks. The construction check covers \(1\le n\le40\) and \(2\le m\le40\). The code additionally checks the exact optimal-count formulas for two- and three-vertex blades and the general cube of the blade-local coefficient formula.

Replay output:

`ALL CHECKS PASSED; exhaustive_parameter_cases=35; labeled_maps_checked=609960; constructions=1560; exact_special_counts={(1, 2): 6, (1, 3): 24, (1, 4): 90, (1, 5): 90, (2, 2): 18, (2, 3): 144, (2, 4): 2700, (3, 2): 60, (4, 2): 210}`

The finite tests do not prove the theorem for unbounded \(n,m\); that part is analytic. No independent external audit has been carried out.
