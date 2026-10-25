---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

Reconstructed the 35-monomial degree-four space, rank-15 evaluation map, 20-dimensional kernel, four-dimensional G·linear subspace, and 16-dimensional quotient. Exhaustive Gray-code reimplementation recovered 288 classes nonsingular at all 15 rational points and 288 distinct tangent matchings; the group-action reimplementation recovered two orbits of size 144. The exact fetched `verify_geometric_smoothness.py` blob (SHA 8b549e111bf90fc9a6daf0b781bbb38620ab0b11) was run; all four chart ideals are unit for the smooth representative and non-unit for the singular representative. The two other local reimplementations were not byte-identical to their package blobs.

## originality

PASS

The claim fixes a cubic and classifies its quartic sections modulo G·linear forms; existence/minimal-degree theorems and cubic-surface isomorphism classifications do not imply the 288 rationally smooth classes or the two section orbits.

No broader inspected result dominates the exact finite section classification and geometric-smoothness orbit split.

No exact published table of these quotient classes and orbits was found.

The full enumeration, distinction between rational and geometric smoothness, and orbit classification are not implied by the closest prior results.

## value

PASS

The exact finite classification separates rational-point nonsingularity from geometric smoothness and computes the orbit structure of a natural section space on a highly symmetric fixed surface. The object and invariant are motivated by minimum-degree space-filling curves and automorphism-group action; the claim is not merely one example or a recomputation of the cubic-surface automorphism group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
