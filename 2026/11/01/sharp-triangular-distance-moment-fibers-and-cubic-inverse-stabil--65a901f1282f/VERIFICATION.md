---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Exact barycentric simplex factorial moments yield m1=e1/18,m2=(e1^2-2e2)/60,m3=(23e1^3-62e1e2+20e3)/4200 for elementary symmetric functions of squared side lengths. I independently symbolically integrated all three polynomials in four barycentric variables and verified them identically, and checked both isosceles endpoints with exact sixth-moment gap d^3/420. The fixed e1,e2 plane-sphere circle has theta in [0,pi/3], h<alpha ensures positive sides, and Heron positivity ensures triangle inequalities. e3 varies by (h^3/4)cos3theta, proving full fiber; cubic roots recover the sides. Rouché componentwise root clustering yields the 1/3 inverse modulus, and an explicit near-equilateral pair shows optimality.

## originality

PASS

Best-of-knowledge positive originality for the full final claim after identifying all presently established subclaims; actual source-material inspections and possible dominating alternatives are recorded. Literature gaps are residual risks, not proof of novelty.

## value

PASS

Exact rotationally invariant pair-distance measurements give a natural shape-reconstruction problem. The theorem provides a complete realizability region, rigorously identifies two-measurement ambiguity and its isosceles extremizers, establishes a sharp three-moment cutoff, and quantifies intrinsic cubic ill-conditioning near equilateral shape rather than just recomputing known forward moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
