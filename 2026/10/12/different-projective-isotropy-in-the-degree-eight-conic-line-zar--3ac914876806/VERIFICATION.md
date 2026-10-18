---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Three conic quadratic forms Q1=diag(1,1,−1), Q2=diag(1/3,1,−1), Q3=diag(1,1/3,−1). Their intrinsic tangency incidence fixes C1 and preserves {C2,C3}. A map fixing C2,C3 must commute with the generalized eigenoperators Q1^-1Q2 and Q1^-1Q3; their unique 1/3 eigenspaces force both X and Y axes invariant, so the map is diagonal; Q1 then forces coordinate sign changes. Together with swapping X,Y these are all eight D8 conic symmetries. Independent exact rational action on four tangent lines gives exactly two stabilizers of {L1,L2} and four of {L1,L3}, respectively C2 and C2×C2. Exhaustive finite check occurs only AFTER symbolic completeness in PGL3(C).

## originality

PASS

The primary 2021 Zariski-pair paper provides the equations and tangencies, not the full projective symmetry groups. The later 2025 strong Ziegler-pair work studies Jacobian/syzygy invariants, not this pair of full projective automorphism groups. Resultary returned a projective stabilizer for a DIFFERENT 2-conic/3-line arrangement; no exact matching computation identified. Historical unindexed coordinate symmetries remain possible.

## value

PASS

The pair already has equal intersection combinatorics but differing embedded topology. Different full PGL3 isotropy orders 2 versus 4 give a precise non-topological embedded-projective moduli distinction of these natural explicit degree-eight arrangements. Exhaustiveness makes the exact stabilizers a reusable invariant rather than a trivial visible reflection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
