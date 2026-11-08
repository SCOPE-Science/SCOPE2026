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

For n=6, disjoint coordinate matchings with four independent sign choices per matched pair give the exact cover face vector (60,720,960). Global sign reversal fixes no simplex setwise, preserves the pair-index orientation, and produces the quotient Delta-complex with (30,360,480) orbit cells. Independent reconstruction of every boundary incidence verifies ∂1∂2=0, connected quotient 1-skeleton and rank(∂1)=29. An independent sparse integral unimodular ±1-pivot elimination of the 360×480 ∂2 finds 270 unit pivots and a 90×210 residual consisting of exactly 120 entries +2 and 120 entries -2; dividing by 2 permits 15 further unit pivots, leaving a zero 75×195 matrix. Thus Smith factors are 1^270,2^15, with 195 zero columns. Separate modular ranks were 270 over F2 and 285 over F3,F5,F101. Since ker∂1 is primitive, H1=Z^(360−29−285)⊕(Z/2)^15=Z^46⊕(Z/2)^15; H2=Z^(480−285)=Z^195. Euler characteristic 150 agrees. All integer reduction steps are exact, not inference from finite-field ranks. The covering wedge assertion uses Wachs inflation theorem and is distinguished from the newly computed quotient.

## originality

PASS

The exact integral quotient homology, notably fifteen independent Z/2 classes, is not stated or mechanically implied by the inspected definitions/connectivity theorem for D2, the ordinary cover wedge decomposition, the equivariant homology module of that cover, or flabby-sheaf-conditional wedge results. These adjacent theorems are credited; no exact signed-orbit Smith table was located. Originality is best-of-knowledge and unindexed equivalent computations remain possible.

## value

PASS

This is a canonical, structurally motivated quotient: doubling the boundary of the six-dimensional cross-polytope and dividing by its global sign symmetry. Dimension six is the first cross-polytope dimension whose double has 2-cells; for dimensions ≤5 the corresponding quotient has dimension ≤1 and cannot acquire first-homology torsion. The exact 15 two-torsion generators therefore exhibit a natural first-dimensional obstruction to naive descent of an inflation wedge theorem and provide a concrete integral invariant for equivariant-topology comparisons. No arbitrary parameter selection, unmotivated tiny slice or general classification is claimed; standalone exact topology is worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
