---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The projective stabilizer proof is correct. Degree preservation separates the two conic components from the three lines, and tangency versus secancy intrinsically distinguishes the two conics, so both conics are fixed individually. Restriction to the inner conic embeds the stabilizer into the permutation group of the three line-tangency points; the kernel is trivial because a conic automorphism fixing three points is identity and a plane projectivity fixing a nondegenerate conic pointwise is scalar. The displayed matrices R and S preserve both conics, cyclically permute or reflect the three lines, and satisfy the dihedral relations, so the upper bound S3 is attained. The exact verifier independently checks the matrix relations, conic preservation, line permutation, tangencies, ordinary triple transversality, the two conic intersections at infinity, their orbit behavior, and the complete Bezout count.

## originality

PASS

The Dimca--Pokora article proves the unique projective-equivalence class with two conics, three lines, five tacnodes, and three ordinary triple points, and derives the equilateral geometry. The correction supplies the exact corrected equation used here. Neither inspected source gives the full PGL3 stabilizer or the three singular-orbit decomposition. A targeted Resultary search returned the audited stabilizer as the only direct match. Although the D3 symmetry is suggested by the equilateral realization, proving that there are no additional projective symmetries requires the intrinsic conic distinction and faithful action on three marked tangency points.

## value

PASS

For a unique projective class of a distinguished free conic-line arrangement, the exact stabilizer and its singular-orbit action are natural structural invariants. The result upgrades visible equilateral symmetry to a complete no-hidden-symmetries theorem and records how the group acts on the three different singularity types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
