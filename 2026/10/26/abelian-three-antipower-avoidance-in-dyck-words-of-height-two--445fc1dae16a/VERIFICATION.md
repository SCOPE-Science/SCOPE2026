---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For a Dyck word of height≤2, every odd time is height1 and even heights are 2x_j with x0=xn=0 and x_j∈{0,1}; code determines each two-letter block uniquely. Length-p factor zero counts equal (p+H(t+p)−H(t))/2. Three pairwise unequal counts can only occur for even p=2s at even starting time, and then exactly if differences x_(j+s)−x_j,x_(j+2s)−x_(j+s),x_(j+3s)−x_(j+2s) are a permutation of −1,0,+1. Avoidance is equivalent to equal outer bits forcing four identical bits along all 4-term arithmetic progressions. Run-crossing argument forces code constant zero, fully alternating, or three runs 0^a1^b0^c with b≥3,(a,c)∈{(1,1),(1,2),(2,1)}; corresponding n congruences yield five disjoint word templates and T_n formula. Independent full enumeration checked 8,191 height-two codes through semilength13; no finite-census assertion substitutes for run proof.

## originality

PASS

The assessed new statement, not its model/semantic/occupancy/antipower/divisor premises, survives direct implication comparison to the inspected primary literature. A four-term progression avoidance or Dyck-code classification may be known under different terminology. Best-of-knowledge priority is qualified, not certified by unsuccessful searching.

## value

PASS

This supplies a natural complete infinite-language avoidance classification under bounded nesting depth. Four-point progression rigidity is a meaningful structural explanation, and the exact eventually periodic enumeration would be useful for combinatorics on constrained Dyck paths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
