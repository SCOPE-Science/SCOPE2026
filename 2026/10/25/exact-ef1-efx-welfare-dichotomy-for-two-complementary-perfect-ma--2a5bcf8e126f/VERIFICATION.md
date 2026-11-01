---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For T≥1 and two agent matchings partitioning 2T goods into disjoint pairs, any T completed recipient-valued pairs partition all goods; an alternating cycle must be assigned wholly by one color, so full welfare T is fair iff cycle half-lengths have an almost-balanced subset split (total discrepancy ≤1). If this fails, greedily distribute all but one largest component, cut it into L-1 disjoint colored pairs with two leftovers; choosing the cut near balance and giving leftovers to smaller-value recipient ensures for every deleted item the other-valued bundle ≤floor((size-1)/2), hence strong EFX and welfare T-1. EF1 cannot exceed T except at the same criterion. Standard subset sum DP yields O(T²) witnessing assignment. Independently enumerated 235 labeled ordered pairs of matchings on 2,4,6 goods with all allocation EFX tests; formula passed. Strong all-goods EFX convention and common-edge doubled cycles included.

## originality

PASS

Pyne–Viswanathan–Yang–Zick Proposition 2.1 already contains the 4-good alternating obstruction and general SPOC2 EFX approximation algorithms. This work does NOT claim that example, general EFX existence, or generic 1/3 bound as original. The complete all-T perfect-matching cycle subset-partition iff theorem with exact unit efficiency gap is not implied by those published result statements or the general two-agent complexity classification; qualified best-of-knowledge PASS.

## value

PASS

Exact welfare of a natural, complete and tractable complementary-pair preference domain, with a sharp EF1=EFX classification and constructive polynomial-time optimum, meaningfully distinguishes a special family from generic fairness-efficiency approximation bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
