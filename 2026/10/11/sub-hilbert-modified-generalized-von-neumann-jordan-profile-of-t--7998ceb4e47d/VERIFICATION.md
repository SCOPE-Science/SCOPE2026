---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For X8 with N(s,t)=max(|s|,|t|,(|s|+|t|)/sqrt2), p>=1 and a=sqrt2-1, Fu--Li ball reduction and separate convexity reduce to 8² ordered vertex pairs. Independent enumeration yields only shifted-norm patterns (2,0), (2,2a), (sqrt2,sqrt2). The three normalized values are 1,1+a^p,2^(1-p/2); Jensen on 1,a, using 1+a=sqrt2, proves 1+a^p>=2^(1-p/2) (strict p>1). For 1<p<2 comparison with the published unrestricted 2^(2-p)(1+a^q)^(p-1), q=p/(p-1)>p, is strictly larger by norm equivalence with unequal nonzero entries. At p=2 both equal 4-2sqrt2; for p>=2 published unrestricted upper bound and vertex witness sandwich to equality. No claim for p<1. Exact octagon finite orbits are exhaustively reconstructed (not extrapolated from numerical sampling); exponent inequality follows analytically.

## originality

PASS

Yang--Wang 2017 published unrestricted regular-octagon exponent-p profile, not the equal-unit-sphere modified constant. The p>=2 modified value is actually implied by that theorem and the elementary equality witness and must not be credited as new. Fu--Li defines and analyzes the modified invariant abstractly, classical Lp examples, but available textual metadata does not exhibit the sub-Hilbert regular-octagon computation. A different prior quadratic mixing-parameter profile in Resultary does not vary p. Full 2017 defining modified paper and Fu-Li article were not newly inspected in full; bibliographic risk explicitly retained rather than automatic O failure.

## value

PASS

Provides the exact equal-radius constrained profile for a natural polygonal Banach-space benchmark, and pinpoints that the restriction is binding precisely 1<p<2. The exact threshold and geometry explain a meaningful structural distinction from published unrestricted constants, not just an arbitrary substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
