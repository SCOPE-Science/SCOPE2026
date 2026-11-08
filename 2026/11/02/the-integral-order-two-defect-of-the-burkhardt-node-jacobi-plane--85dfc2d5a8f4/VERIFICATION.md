---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The 45-node characteristic-two configuration consists of fifteen two-support points and thirty paired-root points over F4. An independent exact F4 six-coordinate generator obtained those 45, enumerated all 13,950 noncollinear node triples, extracted precisely forty 9-node plane spans, and independently reconstructed the 45×40 integer incidence. Exact SymPy Smith form returned fifteen unit and ten factor-two entries, with rational rank 25 and mod2 rank 15. The source proof also establishes every nine-node plane lies on σ4=0 using coefficientwise polynomial expansion and identifies all geometric singular nodes via gradient case split and nondegenerate quadrics. Gram MMᵀ=8I+2A for SRG(45,32,22,24) gives rational rank25; explicit 25×25 minor of determinant -1024 and binary rank15 force exactly ten 2-torsion factors. Finite F4 enumeration is geometrically exhaustive because all node types and planes are separately algebraically classified, not because arbitrary point sampling suffices.

## originality

PASS

Bruin–Nasserden and Cheltsov–Przyjalkowski–Shramov identify the 45 nodes, 40 Jacobi planes and geometric incidence, but those source statements and rational intersection-matrix ranks do not by themselves identify the integer 45×40 node-plane incidence Smith factors. Primary 2024/2025 geometry confirms 9 nodes per plane but no complete Smith form was located. The 1990 and 2026 full primary treatments may contain the equivalent integer calculation and remain important priority risks.

## value

PASS

Integral saturation defects and exact torsion of canonical incidence lattices are natural invariants of this highly symmetric quartic. The ten order-two classes are invisible to the rational incidence rank; they provide exact arithmetic structure beyond known node and plane counts, without conflating incidence cokernel with Picard or divisor-class torsion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
