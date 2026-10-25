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

Aubry–Iezzi Proposition 5.2 forces normalization of 37-point maximal geometric-genus1 arithmetic-genus2 curve over F25 to be maximal genus1, exactly one F25-rational singularity of delta=1 whose preimage is a degree-two point. E:y^2=x^3+1 has 6 points/F5 and Frobenius over F25 equals [-5], so E(F25)=E[6] has36 and E(F625)=E[24] has576, giving 270 degree-two closed points. Supersingular j=0 twists of E over F25 have point counts 36 for only its one twist class. Every branch R has Delta=F(R)-R=[-6]R in nonzero E[4], and Aut_F25(E)=E[6]⋊mu6 acts on Delta. Mu6 acts in three orbits of sizes 3,6,6, leading to 270 closed points in 54,108,108 orbits and stabilizers 4,2,2; the order4 stabilizer is commuting involutions V4. Independently coded finite 24-torsion affine-orbit enumeration recovered [54,108,108].

## originality

PASS

Earlier Aubry–Iezzi settles maximality structure and degree-two pinching; recent Hilario–Salomão–Martins constructs one example on this same E. No inspected accessible prior result determines ALL 270 gluing-point automorphism orbits, their three isomorphism classes, and V4/C2/C2 stabilizers. Best-of-knowledge passage with explicit risk because the most relevant 2026 article was not fully accessible.

## value

PASS

The full natural extremal moduli question at a fixed small finite field is resolved in abstract k-isomorphism classes rather than by listing examples. Orbit sizes and automorphism-group types distinguish two classes with identical stabilizer order, a worthwhile exact arithmetic classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
