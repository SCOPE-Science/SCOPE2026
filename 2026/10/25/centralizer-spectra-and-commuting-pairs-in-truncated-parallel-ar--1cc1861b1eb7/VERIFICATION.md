---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Inspected RESULT.md derives the independent length-two path equations a_i tensor b_(i+1)=b_i tensor a_(i+1). Pure-tensor rigidity fixes a common scalar on each one-run of length at least two, while singleton one positions and zeros without neighboring ones each yield h free coordinates; all length-two coefficients commute because J³=0. This gives exact centralizer dimensions and weighted spectrum. For ordered pairs, nonzero 2xh matrices are either rank-two singleton blocks (B=(q^h-1)(q^h-q) possibilities) or contiguous rank-one blocks on one common P¹(F_q) line (weight (q+1)(q^h-1)^ell); insertion of zero separators gives (1+(qA+B)z-ABz²)/(1-(A+1)z-(qA+B)z²+ABz³). The support-run classification of minimum and the center J² follow for h>=2,m>=2. Independently enumerated all q=2,h=2,m=3 arrow arrays: 406 commuting ordered pairs; centralizer support-dimension histogram (6:1,4:15,2:3,1:45), both agreeing with formulas. The complete source verify.py independently assembles linear commutator systems. Finite checks are not infinite proof.

## originality

PASS

Best-of-knowledge comparison of the precise claim against related primary statements, algebraic implications, four named searches, and inspected published records; prior building blocks acknowledged, with explicit limitations for inaccessible full texts.

## value

PASS

PASS: Exact elementwise centralizer multiplicities and complete commuting probabilities are natural invariants for a genuinely noncommutative family of radical-cube-zero quiver algebras. The support-run formula resolves these invariants for all finite field sizes, widths and chain lengths, rather than an unmotivated fixed-instance census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
