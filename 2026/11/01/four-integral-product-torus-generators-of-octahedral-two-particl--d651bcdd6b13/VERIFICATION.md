---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The standard Abrams cubical unordered two-point model is valid for the simple octahedral graph under the two-particle subdivision condition. Independent reconstruction gives 15 zero-cells, 48 one-cells, 30 two-cells; all integer cubical boundaries compose to zero. Independent exact rational elimination gives rank ∂1=14, rank ∂2=26, hence Betti (1,8,4). The four opposite triangular-face pairs give embedded products of edge cycles and therefore four closed 2-chains. Their pairwise unique square coordinates yield an explicit 4x4 diagonal unit minor, so they span a primitive rank-four sublattice of C2; since ker∂2 is saturated and rank4, these cycles form an integral basis of H2≅Z4. An independent construction of all four torus cycles found pairwise exclusive square-support witness coordinates (1,7,6,2), with diagonal signs (-1,-1,1,1), certifying the integral unit minor. A fresh signed fixed-cell Euler calculation for all 48 octahedral graph automorphisms independently verified the H1 character formula; the inspected source also computes the H2 representation. Geometrically group action permutes four opposite face pairs and reverses product orientation under central inversion, yielding H2=(1⊕S^(3,1))⊗ε. The equivariant chain Euler identity gives H1=(sgn⊕S^(2,1,1))⊗(1⊕ε); the absence of full-group invariants in H1,H2 gives rationally acyclic quotient after barycentric subdivision. No integral H1 torsion claim or contractible quotient claim is made.

## originality

PASS

Classical Abrams/Farber–Hanbury cubical models and topological rank machinery are credited; Farber–Hanbury full text treats ordered two-point space and its general graph intersection forms, not this unordered octahedral four-torus lattice with full character. Sawicki’s openly available thesis text was checked at its exact octahedral example (§2.1.4) and its relevant configuration-space definitions (§2.2): that example is about Aharonov–Bohm phases in first homology, not a four-generator integral H2 basis or its full symmetry character; the same symmetric group on a *cuboctahedral* two-point space is a different graph. No strong covering implication was identified.

## value

PASS

The octahedral graph is the smallest highly symmetric K2,2,2 with four antipodal triangular-face pairs; four geometrically embedded product tori provide a primitive integral top-homology basis, not just a rank computation. The sign-twisted full symmetry action and vanishing invariant homology of the quotient are natural exact equivariant invariants that a researcher can use beyond generic graph-braid homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
