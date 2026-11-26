---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For each side, every vertex sees precisely the other side in its open neighborhood, so adding the vertex's own label gives the closed sum. A best subset omits negatives, giving the two positive-sum thresholds. At total weight ≤2, a negative shore sum can only be −1 or −2, making the other shore all ≥2 or all 3 respectively and the total ≥3. A zero sum needs a −1 on that shore, forcing the opposite sum ≥2 with no negatives; the only weight≤2 option there is two 1s, failing the defense threshold 3. If both sums are positive and the total ≤2, a sum 1 needs a −1, so the opposite sum must be ≥2. For m=2 the displayed weight-3 constructions have shore sums (4,−1) or (3,0) and meet all relevant defense thresholds. For m=3 they have sums (3,0), with opposite positive sum ≥2 even at n=3. For both sizes ≥4, negative sums make weight 3 impossible and nonnegative shore sums totaling 3 each force a −1 and therefore opposite sum ≥2, a contradiction. The parity constructions with sums (2,2) have positive sums ≥3 and are feasible. For (2,2), the published C4 value is 4; directly, weight 3 would have sums (0,3) or (1,2) up to exchange (−1 is not a two-label sum and −2 forces two 3s opposite). In (0,3), the shore (−1,1) cannot defend the opposite 1; in (1,2), the shore (1,1) cannot defend the opposite −1. All 1s attain 4. An independent sorted-shore enumeration matched all 121 cases, 3294225 state pairs, and the recorded aggregate of 9100528918 minima.

## originality

PASS

The published C4 case is credited and excluded from novelty. Neither the inspected primary exact examples and survey nor the dense complete-multipartite record gives the two-part threshold off that boundary. Related Italian and Roman parameters are not equivalent to the label and defense conditions here.

## value

PASS

This is an all-size exact determination of a named graph invariant on a canonical family, not one arbitrary finite slice. It identifies where the two shores first both force negative labels in any candidate of weight 3, and gives witnesses on both parity classes. The threshold supports direct exact comparisons with other bipartite domination invariants without treating the known C4 evaluation as a contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
