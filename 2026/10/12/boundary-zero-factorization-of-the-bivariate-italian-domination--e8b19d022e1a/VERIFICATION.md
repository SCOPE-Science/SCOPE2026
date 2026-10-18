---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Canonical twin classes A_1..A_p,B_1..B_p, j<=i adjacency, preserve p>=1 nonempty class sizes and vertex-distinct labels {0,1,2}. Every assignment has unique i=first A class containing zero (or p+1) and j=last B class containing zero (or 0). Local independent class factors P=(u+v)^m forbids zero, Q=(1+u+v)^m allows any, R=Q-P requires a zero. For fixed (i,j), all A zeros are guarded iff weight of prefix B_1..B_i >=2, and all B zeros iff suffix A_j..A_p >=2. Because shore constraints are disjoint, mark relevant u*y,v*y² in respective product and remove coefficients y^0,y^1 when needed; summing products over distinct boundaries yields exact complete bivariate GF and O(poly(n)) arithmetic. For p>=2, extreme-neighborhood checks exclude total Italian weight<=2, two label-twos on A_p and B_1 always give weight4, and exhaustive structural classification of weight3 distributions yields six disjoint indicator cases C3 as in RESULT. Independently enumerated 58 canonical proper profiles with p=2,3, positive twin sizes 1 or2 and total <=9 and directly checked every 3^N vertex labeling: all exact C3 coefficients and weight 3/4 minima match. Infinite-family assertions follow the boundary proof, not the finite sweep.

## originality

PASS

Best-of-knowledge surviving original contribution; compare mathematical implication rather than titles/parameters. Shao–Zhao studies Italian domination polynomial of paths, trees and cycles, not all proper chain graphs; separate Resultary full Roman domination chain-graph polynomial counts a stronger rule (zero must neighbor label2), and its Roman GF cannot infer Italian GF (two label1s may guard zero). Padamutham–Palagiri studies complexity/minimum Roman {2} on chain graphs; no direct complete Italian bivariate weight distribution in accessible material.

## value

PASS

Italian domination is a natural standard invariant, and connected chain graphs have canonical nested neighborhoods that make the full bivariate enumeration tractable. A closed all-weights GF and explicit minimum multiplicity (with sharp 3/4 dichotomy) extend beyond a minimum-value formula, enabling coefficient computations for natural graph families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
