---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For diagonal D=diag(1,a,b,c), abc(a²−b)(b²−ac)(ab−c)≠0, the secant/tangent congruences of the standard twisted cubic C and D(C) are closed Veronese P² surfaces in Gr(2,4) via dual Plücker P(A,B,C)=(C²,−BC,AC,B²−AC,−AB,A²). Comparing P with appropriately scaled Q gives a finite intersection. In chart A=U=1 elimination gives C=−(δ/ε)B² and B³=0; at B=V=1 gives A²=C²=0 and uniquely determined Plücker scale; the reverse chart gives another B³=0. Thus the only support points are the shared endpoint tangent lines and the cross-endpoint proper secant, with local Artin rings lengths 3,4,3, total cycle degree ten. Independently built the six Plücker equations and Gröbner eliminated all three projective charts for two rational diagonal triples; standard-monomial counts were 3,4,3. These specializations corroborate the symbolic uniform proof, not replace it.

## originality

PASS

The general ten common secants of two transverse twisted cubics and Veronese secant congruences are established prior results. The source-specific scheme-theoretic degeneration of a diagonal pair to lengths 3+4+3 supported on three lines is more precise than the generic Schubert count and not given in the inspected primary results. Classical degenerations may still contain it.

## value

PASS

The nonreduced local intersection cycle of two explicitly related secant congruences is a natural exact invariant: it exhibits how the classical ten solutions coalesce into three different scheme lengths and distinguishes proper secants from common tangents, useful in enumerative degeneration and multiview geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
