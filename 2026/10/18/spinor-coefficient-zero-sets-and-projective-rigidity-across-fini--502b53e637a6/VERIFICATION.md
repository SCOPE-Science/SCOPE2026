---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed the exact hypothesis G≤SU(2) finite nonabelian, defining irreducible two-dimensional unitary block, nonzero u,v and rank-weighted transform normalization. Schur orthogonality puts only a nonzero rank-one defining block in Fourier space, giving sigma=2. SU(2)≅S³ unit quaternions and complex orthogonality identify coefficient zero equations with real two-planes P=a C_J; conversely every such plane occurs. Their intersections with G are empty or left cosets g(G∩U_J), finite cyclic; order two yields one antipodal pair, order>2 yields a maximal noncentral cyclic axis. To prove exactly two coefficient rays for a fixed coset, diagonalize a noncentral h in C: two independent complex vanish constraints annihilate A11,A22, rank(A)=1 forces off-diagonal product bc=0, hence E12 or E21 and no other rays. For an antipodal pair, the nondegenerate rank-one hyperplane section is a projective conic with finitely many extra-zero incidences; generic coefficients have none. Finite-axis arithmetic: 2T {4:3,6:4}, 2O {4:6,6:4,8:3}, 2I {4:15,6:10,10:6}, dicyclic one order-2n axis and n order-4 axes, yielding all displayed 2T/2O/2I/Dic_n zero-set and projective-ray counts. Recomputed Git tree SHA exactly and checked all 7 blob hashes against main. Independently enumerated real rank-two flats of all 24,48,120 exceptional unit-quaternion vectors by exact integer/quadratic-field arithmetic: {2:18,3:16}, {2:72,3:32,4:18}, {2:450,3:200,5:72}. Independently enumerated maximal cyclic subgroups and cosets for Dic_n n=2..20; all predictions matched. Infinite claim is proved by quaternionic plane and abstract group argument, not by finite enumeration.

## originality

PASS

Best-of-knowledge qualified PASS for the cross-family theorem about zero sets and projective coefficient fibres; rank-one Schur orthogonality, finite-group classification and all 2I H4 root-plane numerical multiplicities are prior mathematical inputs, not individually new. No materially inspected prior result states or implies the full SU(2) binary-family rank-one coefficient/cyclic-coset stratification together with the exactly-two-projective-ray realization. Because standard spinor/Segre geometry could encode the same equivalence, this is not a global novelty guarantee.

## value

PASS

A complete nonabelian Fourier support-set diagram for a canonical two-dimensional spin representation is mathematically motivated by the large gap between the general support-product uncertainty inequality and the actual allowed coefficient zeros. Beyond known subgroup and H4 flat counts, the classification uniquely specifies which cyclic cosets can occur as zero sets of a rank-one coefficient, proves converse realization in every binary polyhedral family, and separates finite identifiable two-ray projective fibres from infinite fibres for antipodal pairs. This structural identifiability boundary is useful to researchers reconstructing coefficients or classifying sharp noncommutative support constraints. The exact 2I table alone is covered prior art and is not counted as the standalone contribution; small finite cases are not the primary source of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
