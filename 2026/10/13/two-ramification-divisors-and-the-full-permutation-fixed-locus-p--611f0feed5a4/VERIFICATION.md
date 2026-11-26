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

The graded invariant quotient is obtained by exactness in characteristic zero and the symmetric polynomial theorem, and it is finite. The smooth degree-six surface can also be checked via the weighted power sums: a singular projective point would have at most two distinct coordinates by the rank of the rows 1,x_i,x_i^2, impossible for nonzero x by the weighted first and second sums with positive multiplicities. For projective fixed points one must use every eigenspace of the permutation. On the eigenvalue-one blocks the one- and two-cycle cases are empty, the three-cycle-group cases have nonzero elimination constants 14400,77760,576 times a^6, and the four-cycle-group cases each give six points (distinct singleton cubic roots, or two solutions at s=0 and four when s is normalized to 1). The five-cycle-group block gives the ample connected smooth hyperplane section of genus four. The -1 eigenspaces add two points to (2^2,1^2) and to (4,2), and give a conic for (2^3); both primitive cube-root spaces together give six points for (3^2). Higher-order eigenvalues add two points each for (4,1^2), (4,2), (5,1) and (6), and no other points. Fixed schemes are smooth in characteristic zero. Generic inertia is confirmed by the explicit specializations t^6-6t+5 with one double root and only the trivial stabilizing scalar, and t^6-21t^2+20 with six distinct opposite-paired roots and just the stabilizing scalars +/-1; the latter has roots +/-1, +/-2, +/-sqrt(-5). The curve orbits, the product of squared coordinate differences and the conic degree sum 30 prove the divisor identities and completeness in codimension one. The degree of the finite map is 720 by generic freeness; v=0 is its own branch component, although its generic sextic is squarefree. A separate exact discriminant computation agreed with all seven terms; the elimination and witness checks replay with python /workspace/checks/1.py. The theorem does not determine the scheme structure or inertia in codimension two.

## originality

PASS

Known Hamilton geometry, finite-K3 fixed-locus classifications and the fifteen root pairings are substantial background. Inspected sources support as distinct the explicitly identified coordinate action's reduced coarse branch divisor with inertia, the two divisor pullback descriptions, and its combined projective cycle-type profile. This is a bounded statement comparison, not a claim that every count or pairing criterion is separately new.

## value

PASS

This is a natural symmetric K3 from the Hamilton normal form. The result delineates where a squarefree polynomial nevertheless has projective inertia, identifies the incidence contributors on the surface, and gives the entire cycle-type classification needed to exclude any further divisorial branch. It resolves the specific coarse-versus-root-discriminant distinction on the natural quotient and is useful independently of the full automorphism group or codimension-two analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
